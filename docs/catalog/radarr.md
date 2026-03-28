---
nav_exclude: false
title: "Radarr"
category: "applications/media"
status: "stable"
license: "GPL-3.0"
source: "https://radarr.video"
repository: "https://github.com/Radarr/Radarr"
documentation: "https://wiki.servarr.com/radarr"
docker_image: "linuxserver/radarr"
community: "https://www.reddit.com/r/radarr/"
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

# Radarr

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Automated movie collection manager. Monitors for new releases, searches indexers, downloads via Usenet or BitTorrent clients, and organizes your library with proper naming and metadata. Part of the *arr stack ecosystem.

## Architectural Role

Applications/media layer: the automated librarian for movies. Integrates with download clients (qBittorrent, SABnzbd), indexers (via Prowlarr), and media servers (Jellyfin, Plex). Watches for movies you want, grabs them when available, renames and sorts them.

## Technical Autonomy

- ✅ Works without internet (manages existing library offline)
- ✅ Stores data locally (SQLite database, config)
- ✅ Does not require external accounts
- ✅ Allows data export (database backup, API access)
- ⚠️ Needs internet to search indexers and download new content

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅ | Stop container, existing library stays. Queue pauses. |
| Exit                  | ✅ | Media files are standard video files. Config is SQLite. |
| Recoverability        | ✅ | Backup SQLite database. Media files are independent. |
| Visibility            | ✅ | GPL-3.0, fully auditable. |
| External Dependencies | ✅ | Self-hosted. Indexer connections are user-configured. |

## Configuration (Minimal)

```yaml
services:
  radarr:
    image: linuxserver/radarr
    container_name: radarr
    ports:
      - "7878:7878"
    volumes:
      - ./config/radarr:/config
      - /path/to/movies:/movies
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
| Manual downloads | — | Full control but no automation. |
| Plex | A1 / T0 | Has its own watchlist but cloud-dependent. |

---

## Trajectory

**Direction: stable.**

Part of the *arr ecosystem. Actively maintained, GPL-3.0, regular releases. Community-driven development with a clear scope.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | GPL-3.0, unchanged. |
| Feature gating | ✅ | No paid tier. |
| Self-hosting | ✅ | Docker-first, well documented. |
| Governance | ✅ | Community-driven, multiple maintainers. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [radarr.video](https://radarr.video)
- **Repository:** [github.com/Radarr/Radarr](https://github.com/Radarr/Radarr)
- **Docker image:** `linuxserver/radarr`
