---
nav_exclude: false
title: "Podman"
category: "compute/container"
status: "stable"
license: "Apache-2.0"
source: "https://podman.io"
repository: "https://github.com/containers/podman"
documentation: "https://docs.podman.io"
docker_image: "-"
community: "https://podman.io/community"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
trajectory: "opening"
parent: Technology Catalog
nav_order: 99
---

# Podman

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Daemonless, rootless container engine compatible with Docker CLI. Drop-in replacement for Docker without the Docker daemon, without Docker Hub dependency by default, and without commercial licensing concerns. Developed by Red Hat, community-governed under the Containers organization.

## Architectural Role

Compute/container layer: alternative to Docker as the container runtime. Same CLI commands (`podman run`, `podman compose`), same image format (OCI), but no daemon process, no root requirement, and no centralized registry dependency. Can use any OCI registry including self-hosted ones.

## Technical Autonomy

- ✅ Works without internet (after images are cached)
- ✅ Stores data locally
- ✅ Does not require external accounts (no Docker Hub login needed)
- ✅ OCI-standard images — portable to Docker, containerd, CRI-O
- ✅ No daemon — no single point of failure
- ✅ No commercial licensing concerns

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅ | Containers can be stopped, started. No daemon to manage. |
| Exit                  | ✅ | OCI images work with any compatible runtime. No lock-in. |
| Recoverability        | ✅ | Containers recreated from images. Volumes backed up normally. |
| Visibility            | ✅ | Apache-2.0. Fully open source. |
| External Dependencies | ✅ | No mandatory registry. Default pulls from multiple registries, not just Docker Hub. |

## Configuration (Minimal)

```bash
# Install (Debian/Ubuntu)
sudo apt install -y podman

# Use exactly like Docker
podman run -d --name nginx -p 8080:80 nginx

# Docker Compose compatibility
pip install podman-compose
podman-compose up -d
```

Alias for drop-in replacement:

```bash
alias docker=podman
```

## Related Recipes

- Any TAS recipe — replace `docker` with `podman` and `docker compose` with `podman-compose`

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Docker](docker.md) | A3 / T2 | Industry standard. Docker Hub dependency. Commercial licensing for Desktop. |
| containerd | A3 / T2 | Lower-level runtime. No CLI — used by Kubernetes. |
| LXC/LXD | A3 / T2 | System containers. Different use case. |

---

## Trajectory

**Direction: opening.**

Podman is growing as the Docker alternative for users concerned about Docker Inc.'s commercial direction. Red Hat-backed but Apache-2.0 licensed and community-governed under the Containers GitHub organization. Rootless by default — better security model than Docker.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | Apache-2.0, unchanged. |
| Feature gating | ✅ | No paid tier. No commercial version. |
| Self-hosting | ✅ | Native package in every major distro. No daemon to manage. |
| Governance | ✅ | Containers organization on GitHub. Multiple maintainers from multiple companies. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [podman.io](https://podman.io)
- **Repository:** [github.com/containers/podman](https://github.com/containers/podman)
- **Documentation:** [docs.podman.io](https://docs.podman.io)
