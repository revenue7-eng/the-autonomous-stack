---
nav_exclude: false
title: "Portainer"
category: "compute/container"
status: "stable"
license: "Zlib"
source: "https://portainer.io"
repository: "https://github.com/portainer/portainer"
documentation: "https://docs.portainer.io"
docker_image: "https://hub.docker.com/r/portainer/portainer-ce"
community: "https://github.com/portainer/portainer/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: []
depended_by: []
critical_criteria: ["Recoverability"]
trajectory: "mixed"
parent: Technology Catalog
nav_order: 99
---

# Portainer

> **TAS Score: S3/3 — D4/5** — A3 / T2
> D4 not D5: Community Edition is free and open source, but Business Edition gates advanced features behind a paid license (Q8).
> **Critical criteria for this category:** Recoverability.


## Brief Description

Web-based GUI for managing Docker, Kubernetes, and Swarm environments. Portainer Community Edition provides a visual interface for container lifecycle management, making self-hosted infrastructure accessible to less technical users.

## Architectural Role

Compute management layer: sits on top of Docker or Kubernetes to provide visual management of containers, images, volumes, and networks. Not required for operations — purely a management convenience.

## Technical Autonomy

- ✅ Works without internet (all management is local against Docker socket)
- ✅ Stores data locally (configuration and state in a single volume)
- ✅ Does not require external accounts (CE edition)
- ✅ Allows data export (backup/restore of Portainer database)
- ✅ Provides offline updates (manual Docker image pull and replace)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status  | Comments |
| --------------------- | ------- | -------- |
| Pause                 | Yes     | Portainer can be stopped without affecting running containers. It is a management tool only. |
| Exit                  | Yes     | All managed resources (containers, volumes) exist independently. Removing Portainer changes nothing. |
| Recoverability        | Yes     | Single Docker volume contains all state. Backup is trivial. |
| Visibility            | Yes     | Community Edition is open source (Zlib license), fully auditable. |
| External Dependencies | None    | Fully local. Optional: Portainer Hub for templates (not required). |

## Configuration (Minimal)

```yaml
services:
  portainer:
    image: portainer/portainer-ce:latest
    container_name: portainer
    ports:
      - "9000:9000"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - portainer_data:/data
    restart: unless-stopped
```

## Alternatives

* Yacht — lighter Docker GUI, less features
* Dockge — minimal Docker Compose manager by the Uptime Kuma author
* Lazydocker — terminal-based Docker management
* Docker CLI — no GUI, maximum control

---

## Trajectory

**Direction: mixed.**

Portainer Community Edition remains open source under the Zlib license. However, Portainer has a Business Edition with advanced features (RBAC, registry management, GitOps) behind a paid license. The CE/BE feature gap has been growing. Core container management remains solid in CE.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | Zlib for CE; unchanged. |
| Feature gating | ⚠️ | RBAC, advanced registry, GitOps are BE-only. Gap growing. |
| Self-hosting | ✅ | CE self-hosting is well-supported. |
| Governance | ➖ | Corporate-controlled roadmap; community contributions accepted but direction is commercial. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

* [Website](https://portainer.io)
* [Documentation](https://docs.portainer.io)
* [Repository](https://github.com/portainer/portainer)
* [Docker image](https://hub.docker.com/r/portainer/portainer-ce)
