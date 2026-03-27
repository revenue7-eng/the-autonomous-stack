---
nav_exclude: false
title: "Jellyfin"
category: "applications/media"
status: "stable"
license: "GPL-2.0"
source: "https://jellyfin.org"
repository: "https://github.com/jellyfin/jellyfin"
documentation: "https://jellyfin.org/docs/"
docker_image: "https://hub.docker.com/r/jellyfin/jellyfin"
community: "https://github.com/jellyfin/jellyfin/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: []
depended_by: []
critical_criteria: ["Exit"]
trajectory: "stable"
parent: Technology Catalog
nav_order: 99
---

# Jellyfin

> **TAS Score: S3/3 -- D5/5** -- A3 / T2
> **Critical criteria for this category:** Exit.


## Brief Description
Free software media server that streams your personal media collection without cloud dependencies. A full alternative to Plex/Emby.

## Architectural Role
Media server: serves movies, TV shows, music, and photos to clients (TVs, phones, browsers) over the local network.

## Technical Autonomy
- ✅ Works without internet (after initial setup)
- ✅ Stores data locally (media files and metadata)
- ✅ Does not require external accounts
- ✅ Allows data export (media files are yours; metadata can be exported)
- ✅ Provides offline updates (manual upgrade via packages or Docker)

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
|-----------|--------|----------|
| **Pause** | ✅ | User controls playback; can stop at any time. No auto-playing content unless configured. |
| **Exit** | ✅ | Data is stored as ordinary files; you can delete the server and keep all media. No lock-in. |
| **Recoverability** | ✅ | Media files are separate; configuration and metadata can be backed up and restored. |
| **Visibility** | ✅ | Open source, fully transparent architecture. |
| **External Dependencies** | ✅ | No required external services; can run completely offline. |

## Configuration (Minimal)

Example `docker-compose.yml` snippet:

```yaml
services:
  jellyfin:
    image: jellyfin/jellyfin:latest
    ports:
      - "8096:8096"
    volumes:
      - ./jellyfin-config:/config
      - ./media:/media
```

## Related Recipes

- [Minimal Autonomous Server](../recipes/minimal-server.md) – uses Jellyfin as media server component.

## Alternatives

- **Plex** – requires cloud account and internet for authentication.
- **Emby** – similar to Plex, proprietary with cloud dependencies.
- **Kodi** – more of a client-centric media center, not a server.

---

## Trajectory

**Direction: opening.**

Jellyfin was created in 2018 as a fork of Emby after Emby's source was closed. It is governed by the Jellyfin project organisation (non-corporate), GPL-2.0 licenced, and has no paid tier. The trajectory since inception has been consistently toward openness and community governance.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | GPL-2.0; forked explicitly to preserve open source after Emby closed. |
| Feature gating | ✅ | No paid tier; all features free for all users. |
| Self-hosting | ✅ | Self-hosting is the only model; no cloud service exists or is planned. |
| Governance | ✅ | Community-governed non-corporate project; transparent decision-making. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- [Website](https://jellyfin.org)

- [Documentation](https://jellyfin.org/docs/)

- [Repository](https://github.com/jellyfin/jellyfin)

- [Docker image](https://hub.docker.com/r/jellyfin/jellyfin)

- [Community](https://github.com/jellyfin/jellyfin/discussions)
-e
