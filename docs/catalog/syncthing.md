---
title: "Syncthing"
category: "storage/sync"
status: "stable"
license: "MPL-2.0"
source: "https://syncthing.net"
---

# Syncthing

## Brief Description
Continuous file synchronization program that synchronizes files between two or more devices in real time, peer-to-peer, without a central server.

## Architectural Role
Data synchronization layer: keeps folders in sync across devices (desktop, laptop, phone, server) without cloud intermediaries.

## Technical Autonomy
- ✅ Works without internet (over local network)
- ✅ Stores data locally (synced folders are ordinary files)
- ✅ Does not require external accounts
- ✅ Allows data export (files are already yours; can stop sync anytime)
- ✅ Provides offline updates (manual upgrade via packages or Docker)

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
|-----------|--------|----------|
| **Pause** | ✅ | Sync can be paused or stopped via UI or CLI; no forced background activity. |
| **Exit** | ✅ | Disabling sync leaves your files untouched. No lock-in; you can switch to any other tool. |
| **Recoverability** | ✅ | File versioning is built-in (configurable); deleted or changed files can be restored. |
| **Visibility** | ✅ | Open source, fully transparent architecture. |
| **External Dependencies** | ✅ | No central server required; can run entirely offline. |

## Configuration (Minimal)

Example `docker-compose.yml` snippet:

```yaml
services:
  syncthing:
    image: syncthing/syncthing:latest
    ports:
      - "8384:8384"   # Web UI
      - "22000:22000" # TCP sync
    volumes:
      - ./syncthing-config:/var/syncthing/config
      - ./data:/var/syncthing/data
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
