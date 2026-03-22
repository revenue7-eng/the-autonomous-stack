---

title: "Jellyfin"
category: "applications/media"
status: "stable"
license: "GPL-2.0"
source: "https://jellyfin.org"
autonomy_level: "A3"
transparency_level: "T2"
------------------------

# Jellyfin

## Brief Description

Free software media server that streams your personal media collection without cloud dependencies. A full alternative to Plex and Emby.

## Architectural Role

Media server: serves movies, TV shows, music, and photos to clients (TVs, phones, browsers) over the local network.

## Technical Autonomy

* Works without internet (after initial setup)
* Stores data locally (media files and metadata)
* Does not require external accounts
* Allows data export (media files are yours; metadata can be exported)
* Provides offline updates (manual upgrade via packages or Docker)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments                                              |
| --------------------- | ------ | ----------------------------------------------------- |
| Pause                 | Yes    | User controls playback; can stop at any time.         |
| Exit                  | Yes    | Data stored as ordinary files; no lock-in.            |
| Recoverability        | Yes    | Media and config can be backed up and restored.       |
| Visibility            | Yes    | Open source, fully transparent architecture.          |
| External Dependencies | Yes    | No required external services; fully offline capable. |

## Configuration (Minimal)

Example docker-compose.yml snippet:

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

* Minimal Autonomous Server – includes Syncthing for file sync between devices.

## Alternatives

* Plex – popular but requires account and has cloud dependencies
* Emby – similar architecture, partially proprietary
* Kodi – local media player, less server-oriented

## Sources

* Jellyfin Official Website
* Jellyfin Documentation
