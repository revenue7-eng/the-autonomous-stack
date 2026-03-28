---
nav_exclude: false
title: "Watchtower"
category: "compute/container"
status: "stable"
license: "Apache-2.0"
source: "https://containrrr.dev/watchtower/"
repository: "https://github.com/containrrr/watchtower"
documentation: "https://containrrr.dev/watchtower/"
docker_image: "containrrr/watchtower"
community: "https://github.com/containrrr/watchtower/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: []
depended_by: []
critical_criteria: ["Pause", "Recoverability"]
trajectory: "stable"
parent: Technology Catalog
nav_order: 99
---

# Watchtower

> **TAS Score: S3/3 — D4/5** — A3 / T2
> D4 not D5: by default pulls updated images from Docker Hub — inherits the Docker Hub dependency (Q6). Automatic updates without testing can break services (Q3 recoverability risk).

## Brief Description

Automated Docker container updater. Monitors running containers, detects when a newer image is available, pulls it, and restarts the container with the same configuration. Unattended updates for your self-hosted stack.

## Architectural Role

Compute/maintenance layer: automates the tedious task of keeping Docker containers up to date. Runs alongside your stack and ensures you're running the latest images without manual intervention. Important for security patches.

## Technical Autonomy

- ✅ Works without internet (but cannot check for updates without registry access)
- ✅ Stores no persistent data (stateless)
- ✅ Does not require external accounts
- ✅ Nothing to export (stateless)
- ⚠️ Pulls from Docker Hub by default — same centralized dependency as Docker itself

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅ | Stop Watchtower, containers stay at current versions. No data loss. |
| Exit                  | ✅ | Remove Watchtower, nothing changes. Containers continue running. |
| Recoverability        | ⚠️ | Automatic updates can introduce breaking changes. Pin image versions and use Kopia backups as safety net. |
| Visibility            | ✅ | Apache-2.0, fully auditable. |
| External Dependencies | ⚠️ | Depends on container registries (Docker Hub by default) for checking and pulling updates. |

## Configuration (Minimal)

```yaml
services:
  watchtower:
    image: containrrr/watchtower
    container_name: watchtower
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    environment:
      - WATCHTOWER_CLEANUP=true
      - WATCHTOWER_SCHEDULE=0 0 4 * * *
    restart: unless-stopped
```

Monitor only (notify without auto-updating):

```yaml
    environment:
      - WATCHTOWER_MONITOR_ONLY=true
      - WATCHTOWER_NOTIFICATIONS=shoutrrr
      - WATCHTOWER_NOTIFICATION_URL=generic+https://ntfy.example.com/watchtower
```

## Related Recipes

- [Minimal Autonomous Server](../recipes/minimal-server.md) — add Watchtower for automated maintenance

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| Diun | A3 / T2 | Notification-only — tells you updates are available, doesn't auto-update. Safer. |
| Ouroboros | A3 / T2 | Similar to Watchtower but less maintained. |
| Manual updates | — | `docker compose pull && docker compose up -d`. Full control. |

---

## Trajectory

**Direction: stable.**

Watchtower is a mature, single-purpose tool. Minimal feature creep, stable releases, Apache-2.0 license. Does one thing well.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | Apache-2.0, unchanged. |
| Feature gating | ✅ | No paid tier. |
| Self-hosting | ✅ | Docker-only by design. |
| Governance | ➖ | Maintained by containrrr collective. Lower activity than peak but stable. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [containrrr.dev/watchtower](https://containrrr.dev/watchtower/)
- **Repository:** [github.com/containrrr/watchtower](https://github.com/containrrr/watchtower)
- **Docker image:** `containrrr/watchtower`
