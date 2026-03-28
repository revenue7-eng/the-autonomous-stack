---
nav_exclude: false
title: "Bazarr"
category: "applications/media"
status: "stable"
license: "GPL-3.0"
source: "https://www.bazarr.media"
repository: "https://github.com/morpheus65535/bazarr"
documentation: "https://wiki.bazarr.media"
docker_image: "linuxserver/bazarr"
community: "https://www.reddit.com/r/bazarr/"
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

# Bazarr

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Automated subtitle manager for Radarr and Sonarr. Searches multiple subtitle providers, downloads the best match for your movies and TV shows, and syncs them automatically. Supports 20+ subtitle sources and automatic subtitle synchronization.

## Architectural Role

Applications/media layer: companion to the *arr stack. Monitors your Radarr and Sonarr libraries, detects missing subtitles, and downloads them automatically. Essential for non-English content or accessibility.

## Technical Autonomy

- ✅ Works without internet (existing subtitles stay)
- ✅ Stores data locally (SQLite database, subtitle files)
- ✅ Does not require external accounts for basic providers
- ✅ Subtitles are standard .srt/.ass files — portable
- ⚠️ Needs internet to search subtitle providers

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅ | Stop container, existing subtitles stay. |
| Exit                  | ✅ | Subtitles are standard files alongside media. Remove Bazarr, subtitles remain. |
| Recoverability        | ✅ | SQLite backup. Subtitles are independent files. |
| Visibility            | ✅ | GPL-3.0, fully auditable. |
| External Dependencies | ✅ | Self-hosted. Subtitle provider connections are user-configured. |

## Configuration (Minimal)

```yaml
services:
  bazarr:
    image: linuxserver/bazarr
    container_name: bazarr
    ports:
      - "6767:6767"
    volumes:
      - ./config/bazarr:/config
      - /path/to/movies:/movies
      - /path/to/tv:/tv
    environment:
      - TZ=UTC
    restart: unless-stopped
```

## Related Recipes

- [Media Server](../recipes/media-server.md) — add Bazarr for automatic subtitles

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| Manual subtitle download | — | OpenSubtitles, Subscene. Manual per movie/episode. |
| Sub-Zero (Plex plugin) | A1 / T0 | Plex-only, proprietary ecosystem. |

---

## Trajectory

**Direction: stable.**

Single-purpose tool, GPL-3.0, actively maintained. Part of the *arr ecosystem. No commercial pressure.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | GPL-3.0, unchanged. |
| Feature gating | ✅ | No paid tier. |
| Self-hosting | ✅ | Docker, well documented. |
| Governance | ⚠️ | Primary maintainer (morpheus65535). Bus factor = 1. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [bazarr.media](https://www.bazarr.media)
- **Repository:** [github.com/morpheus65535/bazarr](https://github.com/morpheus65535/bazarr)
- **Docker image:** `linuxserver/bazarr`
