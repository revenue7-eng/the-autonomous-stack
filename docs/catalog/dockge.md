---
nav_exclude: false
title: "Dockge"
category: "compute/container"
status: "stable"
license: "MIT"
source: "https://dockge.kuma.pet"
repository: "https://github.com/louislam/dockge"
documentation: "https://github.com/louislam/dockge#readme"
docker_image: "louislam/dockge"
community: "https://github.com/louislam/dockge/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: []
depended_by: []
critical_criteria: ["Pause", "Exit"]
trajectory: "opening"
parent: Technology Catalog
nav_order: 99
---

# Dockge

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Simple, reactive Docker Compose manager with a web UI. Create, edit, start, stop, and monitor docker-compose stacks from your browser. Built by the creator of Uptime Kuma. Unlike Portainer, Dockge works directly with your `docker-compose.yml` files — no abstraction layer, no lock-in.

## Architectural Role

Compute/management layer: web UI for managing Docker Compose stacks. Does not replace Docker — sits on top of it. Your compose files remain standard YAML on disk, editable by hand or by Dockge interchangeably.

## Technical Autonomy

- ✅ Works without internet
- ✅ Stores data locally (compose files on disk)
- ✅ Does not require external accounts
- ✅ No lock-in — compose files are standard YAML, usable without Dockge
- ✅ Remove Dockge, stacks continue running

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅ | Stop Dockge, all managed stacks keep running. |
| Exit                  | ✅ | Zero lock-in. Compose files are plain YAML on disk. Remove Dockge, nothing changes. |
| Recoverability        | ✅ | Compose files are the source of truth. Dockge is stateless UI. |
| Visibility            | ✅ | MIT license. Simple codebase. |
| External Dependencies | ✅ | Fully self-contained. |

## Configuration (Minimal)

```yaml
services:
  dockge:
    image: louislam/dockge:1
    container_name: dockge
    ports:
      - "5001:5001"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - ./data/dockge:/app/data
      - /opt/stacks:/opt/stacks
    environment:
      - DOCKGE_STACKS_DIR=/opt/stacks
    restart: unless-stopped
```

## Related Recipes

- [Minimal Autonomous Server](../recipes/minimal-server.md) — manage your stack with a UI

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Portainer](portainer.md) | A3 / T2 | More features, more complex. Has its own abstraction layer. |
| Yacht | A3 / T2 | Lightweight container management. Less maintained. |
| Lazy Docker | A3 / T2 | Terminal UI, not web. For CLI users. |
| docker compose CLI | — | Direct command line. Full control, no UI. |

---

## Trajectory

**Direction: opening.**

Created by Louis Lam (same developer as Uptime Kuma). MIT licensed, rapidly growing, simple by design. Philosophy: no vendor lock-in, compose files are the source of truth.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | MIT, maximally permissive. |
| Feature gating | ✅ | No paid tier. |
| Self-hosting | ✅ | Docker-first, single container, minimal setup. |
| Governance | ⚠️ | Single developer (louislam). Bus factor = 1. But same developer maintains Uptime Kuma successfully. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [dockge.kuma.pet](https://dockge.kuma.pet)
- **Repository:** [github.com/louislam/dockge](https://github.com/louislam/dockge)
- **Docker image:** `louislam/dockge`
