---
nav_exclude: false
title: "Sonarr"
category: "applications/media"
status: "stable"
license: "GPL-3.0"
source: "https://sonarr.tv"
repository: "https://github.com/Sonarr/Sonarr"
documentation: "https://wiki.servarr.com/sonarr"
docker_image: "linuxserver/sonarr"
community: "https://www.reddit.com/r/sonarr/"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: ["prowlarr", "jellyfin"]
depended_by: []
critical_criteria: ["Pause", "Exit"]
trajectory: "stable"
parent: Technology Catalog
nav_order: 99
---

# Sonarr

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Automated TV series collection manager. Monitors for new episodes, searches indexers, downloads, and organizes your TV library. Handles season packs, quality upgrades, and proper naming. Part of the *arr stack ecosystem.

## Architectural Role

Applications/media layer: the automated librarian for TV shows. Same architecture as Radarr but for series — monitors air dates, grabs episodes, renames, and sorts into season folders for your media server.

## Technical Autonomy

- ✅ Works without internet (manages existing library offline)
- ✅ Stores data locally (SQLite database, config)
- ✅ Does not require external accounts
- ✅ Allows data export (database backup, API access)
- ⚠️ Needs internet to search indexers and fetch TV metadata

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅ | Stop container, library stays. Missed episodes queue when resumed. |
| Exit                  | ✅ | Media files are standard video files. Config is SQLite. |
| Recoverability        | ✅ | Backup SQLite database. Media files are independent. |
| Visibility            | ✅ | GPL-3.0, fully auditable. |
| External Dependencies | ✅ | Self-hosted. TheTVDB/TMDB metadata lookups are optional. |

## Configuration (Minimal)

```yaml
services:
  sonarr:
    image: linuxserver/sonarr
    container_name: sonarr
    ports:
      - "8989:8989"
    volumes:
      - ./config/sonarr:/config
      - /path/to/tv:/tv
      - /path/to/downloads:/downloads
    environment:
      - TZ=UTC
    restart: unless-stopped
```

## Related Recipes

- Media Server recipe (planned)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| SickChill | A3 / T2 | Older alternative. Less maintained. |
| Medusa | A3 / T2 | Fork of SickRage. Less polished than Sonarr. |

---

## Trajectory

**Direction: stable.**

One of the original *arr applications. Actively maintained since 2014. GPL-3.0, community-driven, regular releases.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | GPL-3.0, unchanged. |
| Feature gating | ✅ | No paid tier. |
| Self-hosting | ✅ | Docker-first, extensive wiki. |
| Governance | ✅ | Community-driven, multiple maintainers. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [sonarr.tv](https://sonarr.tv)
- **Repository:** [github.com/Sonarr/Sonarr](https://github.com/Sonarr/Sonarr)
- **Docker image:** `linuxserver/sonarr`
