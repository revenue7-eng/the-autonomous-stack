---
nav_exclude: false
title: "Overseerr"
category: "applications/media"
status: "stable"
license: "MIT"
source: "https://overseerr.dev"
repository: "https://github.com/sct/overseerr"
documentation: "https://docs.overseerr.dev"
docker_image: "sctx/overseerr"
community: "https://discord.gg/overseerr"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: ["radarr", "sonarr", "jellyfin"]
depended_by: []
critical_criteria: ["Pause", "Exit"]
trajectory: "stable"
parent: Technology Catalog
nav_order: 99
---

# Overseerr

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Media request and discovery tool. Family members browse movies and TV shows through a polished interface, click "request", and Overseerr sends the request to Radarr/Sonarr automatically. No one needs to know how the *arr stack works — they just ask for what they want to watch.

## Architectural Role

Applications/media layer: the family-friendly frontend for the media stack. Hides the complexity of Radarr, Sonarr, and Prowlarr behind a Netflix-like discovery interface. Users browse, request, and get notified when content is ready.

## Technical Autonomy

- ✅ Works without internet (browse existing requests offline)
- ✅ Stores data locally (SQLite database)
- ✅ Does not require external accounts
- ✅ Allows data export (database backup)
- ⚠️ Needs internet for TMDB metadata (movie/show info and posters)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅ | Stop container, requests queue. Media still playable. |
| Exit                  | ✅ | Request history in SQLite. Remove Overseerr, use Radarr/Sonarr directly. |
| Recoverability        | ✅ | SQLite backup. Non-critical — media stack works without it. |
| Visibility            | ✅ | MIT license. |
| External Dependencies | ⚠️ | TMDB API for metadata. Works without it but loses discovery features. |

## Configuration (Minimal)

```yaml
services:
  overseerr:
    image: sctx/overseerr
    container_name: overseerr
    ports:
      - "5055:5055"
    volumes:
      - ./data/overseerr:/app/config
    environment:
      - TZ=UTC
    restart: unless-stopped
```

## Related Recipes

- [Media Server](../recipes/media-server.md) — add Overseerr for family-friendly requests

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| Jellyseerr | A3 / T2 | Fork of Overseerr with native Jellyfin support. Recommended for Jellyfin users. |
| Petio | A3 / T2 | Simpler request tool. Less maintained. |
| Manual requests | — | Tell someone to add it in Radarr. Works but doesn't scale for families. |

---

## Trajectory

**Direction: stable.**

MIT licensed, steady development. Originally built for Plex, community forks (Jellyseerr) added Jellyfin support. Mature and focused.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | MIT, unchanged. |
| Feature gating | ✅ | No paid tier. |
| Self-hosting | ✅ | Docker, simple setup. |
| Governance | ⚠️ | Primary maintainer less active. Jellyseerr fork is more actively maintained. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [overseerr.dev](https://overseerr.dev)
- **Repository:** [github.com/sct/overseerr](https://github.com/sct/overseerr)
- **Docker image:** `sctx/overseerr`
