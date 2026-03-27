---
nav_exclude: false
title: "MinIO"
category: "storage/cloud"
status: "stable"
license: "AGPL-3.0"
source: "https://min.io"
repository: "https://github.com/minio/minio"
documentation: "https://min.io/docs/minio/linux/index.html"
docker_image: "https://hub.docker.com/r/minio/minio"
community: "https://slack.min.io"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Exit"]
trajectory: "mixed"
parent: Technology Catalog
nav_order: 99
---

# MinIO

> **TAS Score: S3/3 — D4/5** — A3 / T2
> D4 not D5: AGPL-3.0 core, but MinIO also offers a commercial SUBNET license. Recent trademark enforcement actions signal corporate control tightening (Q8).
> **Critical criteria for this category:** Exit.


## Brief Description

High-performance, S3-compatible object storage. Self-hosted alternative to Amazon S3. Designed for AI/ML workloads, data lakes, and cloud-native applications. Single binary deployment with enterprise-grade features in the open-source edition.

## Architectural Role

Storage layer: provides S3-compatible API for applications that need object storage. Can serve as backup target, media storage, or data lake backend. Drop-in replacement for AWS S3 in most applications.

## Technical Autonomy

- ✅ Works without internet (fully local object storage)
- ✅ Stores data locally (all objects stored on local or attached disks)
- ✅ Does not require external accounts
- ✅ Allows data export (S3 API is an industry standard; data is portable to any S3-compatible storage)
- ✅ Provides offline updates (manual binary or Docker image replacement)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status  | Comments |
| --------------------- | ------- | -------- |
| Pause                 | Yes     | Service can be stopped. Data persists on disk. Applications lose storage API but data is safe. |
| Exit                  | Yes     | S3 API is an industry standard. Data is plain files on disk. Can migrate to any S3-compatible storage. |
| Recoverability        | Yes     | Supports erasure coding for redundancy. Backup via standard S3 tools (mc mirror, rclone). |
| Visibility            | Yes     | Open source (AGPL-3.0), fully auditable. |
| External Dependencies | None    | Fully self-contained. No cloud dependencies. |

## Configuration (Minimal)

```yaml
services:
  minio:
    image: minio/minio:latest
    container_name: minio
    ports:
      - "9000:9000"
      - "9001:9001"
    volumes:
      - ./data/minio:/data
    environment:
      MINIO_ROOT_USER: ${MINIO_ROOT_USER}
      MINIO_ROOT_PASSWORD: ${MINIO_ROOT_PASSWORD}
    command: server /data --console-address ":9001"
    restart: unless-stopped
```

## Alternatives

* SeaweedFS — distributed file system with S3 compatibility, lighter weight
* Garage — lightweight S3-compatible storage for self-hosting, designed for geo-distributed setups
* Ceph (RADOS Gateway) — enterprise-grade, much more complex
* AWS S3 — cloud-only, A0/T0

---

## Trajectory

**Direction: mixed.**

MinIO core is AGPL-3.0 and fully functional for self-hosting. However, MinIO Inc. has been aggressively enforcing trademarks and pushing the commercial SUBNET license for enterprise features (SSE, LDAP, bucket replication). The AGPL license itself is strong copyleft which may deter some commercial adopters, but it guarantees the code stays open.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ➖ | AGPL-3.0 keeps code open, but commercial license push is growing. |
| Feature gating | ⚠️ | Some enterprise features require SUBNET license. |
| Self-hosting | ✅ | Fully supported and well-documented. |
| Governance | ⚠️ | Corporate-controlled; trademark enforcement actions against forks. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

* [Website](https://min.io)
* [Documentation](https://min.io/docs/minio/linux/index.html)
* [Repository](https://github.com/minio/minio)
* [Docker image](https://hub.docker.com/r/minio/minio)
