---
tags: [sync, files, storage, p2p]
title: "Syncthing"
category: "storage/sync"
status: "stable"
license: "MPL-2.0"
source: "https://syncthing.net"
repository: "https://github.com/syncthing/syncthing"
documentation: "https://docs.syncthing.net"
docker_image: "https://hub.docker.com/r/syncthing/syncthing"
community: "https://forum.syncthing.net"
autonomy_level: "A3"
transparency_level: "T2"
parent: Technology Catalog
nav_order: 4
---

# Syncthing

## Brief Description

Peer‑to‑peer file synchronisation tool that keeps folders in sync across multiple devices — without a central server, without cloud accounts, without trusting a third party.

## Architectural Role

Storage layer: provides continuous, encrypted file sync between devices over the local network or via relay. Replaces Dropbox, Google Drive, and similar cloud sync services.

## Technical Autonomy

- ✅ Works without internet (syncs over LAN when devices are on the same network)
- ✅ Stores data locally (files live on your devices, not in the cloud)
- ✅ Does not require external accounts
- ✅ Allows data export (files are ordinary files — stop Syncthing and keep everything)
- ✅ Provides offline updates (manual upgrade via packages or Docker)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
| --------------------- | ------ | -------- |
| Pause                 | Yes    | Sync can be paused per folder or per device at any time. |
| Exit                  | Yes    | No lock‑in; files are ordinary files on disk. Stop the service and everything stays. |
| Recoverability        | Yes    | File versioning built in; deleted/changed files can be recovered from versioning archive. |
| Visibility            | Yes    | Open source, fully documented protocol and implementation. |
| External Dependencies | Yes    | No mandatory external services. Relay servers are optional and can be self‑hosted. |

## Configuration (Minimal)

Example `docker-compose.yml` snippet:

```yaml
services:
  syncthing:
    image: syncthing/syncthing:latest
    container_name: syncthing
    ports:
      - "8384:8384"    # Web UI
      - "22000:22000"  # Sync protocol
    volumes:
      - ./syncthing-config:/var/syncthing/config
      - ./syncthing-data:/var/syncthing/data
    restart: unless-stopped
```

## Related Recipes

* [Minimal Autonomous Server](../recipes/minimal-server.md) – uses Syncthing for file sync between devices.

## Alternatives

* Nextcloud – heavier, server‑centric, but offers more features (calendar, contacts, office).
* Resilio Sync – proprietary, similar P2P model but closed source.
* Seafile – self‑hosted cloud storage, not P2P.

## Sources

* [Website](https://syncthing.net)

* [Documentation](https://docs.syncthing.net)

* [Repository](https://github.com/syncthing/syncthing)

* [Docker image](https://hub.docker.com/r/syncthing/syncthing)

* [Community](https://forum.syncthing.net)
-e 
## Trajectory
**Stable — opening.**

Syncthing is maintained by a non-profit foundation with no commercial entity behind it. No VC funding, no enterprise tier, no cloud features. Has been consistently open for over a decade. Direction: **stable opening**.
