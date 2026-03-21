
---

### 🔹 Jellyfin → `applications/media`

**Файл:** `docs/catalog/jellyfin.md`

```markdown
---
title: "Jellyfin"
category: "applications/media"
status: "stable"
license: "GPL-2.0"
source: "https://jellyfin.org"
autonomy_level: "A3"
transparency_level: "T2"
---

# Jellyfin

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
| **Pause** | ✅ | User controls playback; can stop at any time. No auto‑playing content unless configured. |
| **Exit** | ✅ | Data is stored as ordinary files; you can delete the server and keep all media. No lock‑in. |
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
- Minimal Autonomous Server – includes Syncthing for file sync between devices.

## Alternatives
- **Resilio Sync** – proprietary, uses a central tracking server.
- **Nextcloud** – heavier, requires server-client architecture rather than P2P.
- **rsync + cron** – more manual approach, no real-time synchronization.

## Sources
- Syncthing Official Website  
- Syncthing Documentation
