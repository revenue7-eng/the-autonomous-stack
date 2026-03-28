---
nav_exclude: false
title: "Docker"
category: "compute/container"
status: "stable"
license: "Apache-2.0"
source: "https://www.docker.com"
repository: "https://github.com/moby/moby"
documentation: "https://docs.docker.com/engine/"
docker_image: "https://hub.docker.com/_/docker"
community: "https://forums.docker.com"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: ["authentik", "forgejo", "grafana", "immich", "jellyfin", "kopia", "nextcloud", "nginx-proxy-manager", "paperless-ngx", "pi-hole", "prometheus", "syncthing", "traefik", "uptime-kuma", "vault", "vaultwarden", "wireguard"]
critical_criteria: ["Recoverability"]
trajectory: "mixed"
parent: Technology Catalog
nav_order: 99
---

# Docker

> **TAS Score: S3/3 — D3/5** — A3 / T2
> D3 not D5: Docker Engine is A3/T2 but almost every `docker compose up` depends on Docker Hub (A0/T0) for pulling images — a centralized registry controlled by Docker Inc. that can enforce rate limits, restrict regions, or change terms at any time (Q5, Q6). Docker Desktop requires a paid subscription for organizations with 250+ employees (Q6). Engagement pressure through Docker Hub's login requirements and pull rate limits nudges users toward paid accounts (Q5).
> **Critical criteria for this category:** Recoverability.

**Why this matters:** Docker is the most depended-upon technology in the TAS catalog. 43 out of 73 technologies require it. A failure or policy change in Docker's ecosystem affects everything built on top of it. Understanding this dependency honestly is critical.


## Brief Description

Platform for developing, shipping, and running applications in lightweight containers. Docker Engine (the runtime) is open source and works fully offline after images are downloaded. But the ecosystem around it — Docker Hub, Docker Desktop, Docker Scout — is increasingly commercial.

## Architectural Role

Compute layer: the foundation that nearly everything else runs on. Docker is to the autonomous stack what an operating system is to applications — invisible when working, catastrophic when broken. Its position as a single point of failure for 43+ technologies makes it the most critical dependency in any self-hosted infrastructure.

## Technical Autonomy

- ✅ Works without internet (after images are cached locally)
- ✅ Stores data locally (images, volumes, configuration)
- ✅ Does not require external accounts (for Engine)
- ✅ Allows data export (images via `docker save`, volumes via tar)
- ⚠️ Image pulls depend on Docker Hub by default — a centralized, rate-limited registry
- ⚠️ Docker Desktop requires login and commercial license for large orgs

## The Docker Hub problem

Docker Engine is autonomous. Docker Hub is not. This distinction matters:

| Component | Autonomy | Transparency | Notes |
|-----------|----------|-------------|-------|
| Docker Engine | A3 | T2 | Open source (Apache-2.0), runs anywhere, fully offline |
| Docker CLI | A3 | T2 | Open source, part of Moby project |
| Docker Hub | A0 | T0 | Centralized registry, proprietary, rate limits, login required for higher limits |
| Docker Desktop | A1 | T0 | Proprietary GUI, requires login, commercial license for large orgs |
| Docker Scout | A0 | T0 | Cloud-only vulnerability scanning |

When you run `docker compose up`, the runtime is A3 but the image source is A0. This is the dependency that didn't disappear — it moved.

**Mitigation:** Use a self-hosted registry (Harbor, Gitea Container Registry, or `registry:2`) to mirror images locally. Pull once, serve from your own infrastructure. This moves image distribution from A0 to A3.

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
|-----------|--------|----------|
| Pause | ✅ | Containers can be stopped, started, or paused at any time. All data persists in volumes. |
| Exit | ✅ | No lock-in to Docker specifically. Images are OCI-standard, compatible with Podman, containerd, CRI-O. |
| Recoverability | ✅ | Volumes can be backed up. Containers are ephemeral by design — recreate from images anytime. |
| Visibility | ✅ | Engine is open source (Moby project). Fully transparent. |
| External Dependencies | ⚠️ | Docker Hub is the default and implicit dependency for almost every Docker workflow. Rate limits (100 pulls/6h anonymous, 200 authenticated) enforce this dependency. |

## Configuration (Minimal)

Installation (on Debian/Ubuntu):

```bash
sudo apt update
sudo apt install docker.io docker-compose -y
sudo systemctl enable docker
```

Self-hosted registry (eliminate Docker Hub dependency):

```yaml
services:
  registry:
    image: registry:2
    container_name: registry
    ports:
      - "5000:5000"
    volumes:
      - ./data/registry:/var/lib/registry
    restart: unless-stopped
```

Mirror an image locally:

```bash
docker pull nginx:latest
docker tag nginx:latest localhost:5000/nginx:latest
docker push localhost:5000/nginx:latest
```

## Related Recipes

- [Minimal Autonomous Server](../recipes/minimal-server.md) — uses Docker to run all services
- [Family Cloud](../recipes/family-cloud.md) — all services containerized
- [Monitoring Stack](../recipes/monitoring-stack.md) — monitoring for Docker containers

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| Podman | A3 / T2 | Daemonless, rootless, Docker CLI-compatible. No commercial licensing. Red Hat-backed. |
| containerd | A3 / T2 | Lower-level runtime. Used by Kubernetes. No desktop/hub commercial layer. |
| LXC/LXD | A3 / T2 | System containers, not application containers. Different use case. |

---

## Trajectory

**Direction: mixed.**

Docker Engine (Moby project) remains open source and stable. But Docker Inc. is increasingly monetizing the ecosystem around it: Docker Desktop licensing (2021), Docker Hub rate limits (2020), login requirements, Docker Scout (cloud-only). The engine is opening; the ecosystem is closing.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ➖ | Docker Engine: Apache-2.0, unchanged. Docker Desktop: commercial licence for large orgs since 2021. |
| Feature gating | ⚠️ | Docker Desktop features (Dev Environments, Extensions, Scout) are commercial. Docker Hub free tier increasingly restricted. |
| Self-hosting | ✅ | Docker Engine self-hosting unchanged. Podman is a credible drop-in replacement. |
| Governance | ➖ | Moby project (upstream) is community-governed. Docker Inc. controls Desktop, Hub, and commercial products. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [docker.com](https://www.docker.com)
- **Documentation:** [docs.docker.com](https://docs.docker.com/engine/)
- **Repository:** [github.com/moby/moby](https://github.com/moby/moby)
- **Community:** [forums.docker.com](https://forums.docker.com)
