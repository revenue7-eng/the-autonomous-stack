---
nav_exclude: false
title: "Prowlarr"
category: "applications/media"
status: "stable"
license: "GPL-3.0"
source: "https://prowlarr.com"
repository: "https://github.com/Prowlarr/Prowlarr"
documentation: "https://wiki.servarr.com/prowlarr"
docker_image: "linuxserver/prowlarr"
community: "https://www.reddit.com/r/prowlarr/"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: ["radarr", "sonarr"]
depended_by: []
critical_criteria: ["Pause", "Exit"]
trajectory: "stable"
parent: Technology Catalog
nav_order: 99
---

# Prowlarr

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Indexer manager for the *arr stack. Centralizes indexer configuration — add your Usenet and torrent indexers once in Prowlarr, and it syncs to Radarr, Sonarr, and other *arr applications automatically. Replaces Jackett with native *arr integration.

## Architectural Role

Applications/media layer: the index broker. Sits between your *arr applications and content indexers. Instead of configuring indexers separately in each *arr app, configure once in Prowlarr and sync everywhere.

## Technical Autonomy

- ✅ Works without internet (cached indexer configs remain)
- ✅ Stores data locally (SQLite database)
- ✅ Does not require external accounts
- ✅ Allows data export (database backup)
- ⚠️ Needs internet to search indexers

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅ | Stop container, *arr apps fall back to their own cached indexer configs. |
| Exit                  | ✅ | Remove Prowlarr, configure indexers directly in Radarr/Sonarr. |
| Recoverability        | ✅ | SQLite backup. Indexer configs are simple. |
| Visibility            | ✅ | GPL-3.0, fully auditable. |
| External Dependencies | ✅ | Self-hosted. Indexer connections are user-configured. |

## Configuration (Minimal)

```yaml
services:
  prowlarr:
    image: linuxserver/prowlarr
    container_name: prowlarr
    ports:
      - "9696:9696"
    volumes:
      - ./config/prowlarr:/config
    environment:
      - TZ=UTC
    restart: unless-stopped
```

## Related Recipes

- Media Server recipe (planned)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| Jackett | A3 / T2 | Older indexer proxy. No native *arr sync — uses Torznab/Newznab API. |

---

## Trajectory

**Direction: stable.**

Built by the *arr team as the official replacement for Jackett. GPL-3.0, actively maintained, growing indexer support.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | GPL-3.0, unchanged. |
| Feature gating | ✅ | No paid tier. |
| Self-hosting | ✅ | Docker-first. |
| Governance | ✅ | Part of *arr ecosystem, community-driven. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [prowlarr.com](https://prowlarr.com)
- **Repository:** [github.com/Prowlarr/Prowlarr](https://github.com/Prowlarr/Prowlarr)
- **Docker image:** `linuxserver/prowlarr`
