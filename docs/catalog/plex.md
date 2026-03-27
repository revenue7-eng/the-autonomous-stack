---
nav_exclude: false
title: "Plex"
category: "applications/media"
status: "stable"
license: "Proprietary"
source: "https://www.plex.tv"
repository: "-"
documentation: "https://support.plex.tv"
docker_image: "https://hub.docker.com/r/plexinc/pms-docker"
community: "https://forums.plex.tv"
autonomy_level: "A1"
transparency_level: "T0"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Exit"]
parent: Technology Catalog
nav_order: 99
---

# Plex

> **TAS Score: S1/3 -- D2/5** -- A1 / T0
> S1 (not S3): Pause and Recoverability are partial — requires Plex auth servers to be reachable; Plex-specific metadata (playlists, watch history) is not fully recoverable (Q1, Q3). D2 (not D5): proprietary server, telemetry cannot be fully disabled (Q4, Q7); depends on Plex account system (Q6).
> **Critical criteria for this category:** Exit.


## Brief Description

Media server that organises and streams your personal media collection. Self‑hosted, but requires a Plex account and internet connection for authentication.

## Architectural Role

Media server: serves movies, TV shows, music, and photos to clients. Runs on your hardware but depends on Plex's cloud for login and some features.

## Technical Autonomy

- ⚠️ Works without internet — media playback works offline for some clients, but initial authentication and many features require internet
- ✅ Stores data locally — media files and metadata are on your server
- ❌ Does not require external accounts — requires Plex account for authentication
- ✅ Allows data export — media files are yours; metadata can be partially exported
- ❌ Provides offline updates — updates are pushed by Plex

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status  | Comments |
| --------------------- | ------- | -------- |
| Pause                 | Partial | You can stop the server, but some clients won't work without Plex auth servers being reachable. |
| Exit                  | Partial | Media files are yours. But playlists, watch history, and user accounts are tied to Plex. |
| Recoverability        | Partial | Media is recoverable (it's your files). Plex‑specific data (metadata, playlists) is harder to back up and restore. |
| Visibility            | No      | Proprietary server. No source code. Telemetry cannot be fully disabled. |
| External Dependencies | No      | Requires Plex authentication servers. If Plex goes down or changes terms, your server's functionality is reduced. |

## Why it's in the catalog

Plex is the most popular media server — and a perfect example of A1: you host the data, but the control layer is someone else's. Your media is local. Your identity is not.

**What you gain:** Polished UI. Excellent client apps. Automatic metadata. Remote access without VPN setup.

**What you give up:** Independence from Plex's account system. Full offline operation. Visibility into what the server software does.

## Autonomous alternatives

* [Jellyfin](jellyfin.md) (A3/T2) — fully open‑source, no account required, no cloud dependencies

## Trajectory

**Direction: closing.**

Plex has been steadily increasing cloud dependencies and moving features behind Plex Pass. Authentication has always required Plex servers. Ad-supported free streaming was added (shifting focus from personal media server to content platform). API restrictions have increased. The trend is clear: Plex is moving from a media server you run toward a media platform you use.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ⚠️ | Proprietary; server source closed. Direction unchanged. |
| Feature gating | ⚠️ | Free features increasingly require Plex Pass; ad-supported content added without user control. |
| Self-hosting | ⚠️ | Authentication still requires Plex's servers; offline operation is degraded. |
| Governance | ⚠️ | Fully corporate-controlled; no community input into direction. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

## Sources

* [Website](https://www.plex.tv)

* [Documentation](https://support.plex.tv)

* [Docker image](https://hub.docker.com/r/plexinc/pms-docker)

* [Community](https://forums.plex.tv)
