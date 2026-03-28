---
nav_exclude: false
title: "qBittorrent"
category: "applications/downloads"
status: "stable"
license: "GPL-2.0"
source: "https://www.qbittorrent.org"
repository: "https://github.com/qbittorrent/qBittorrent"
documentation: "https://github.com/qbittorrent/qBittorrent/wiki"
docker_image: "linuxserver/qbittorrent"
community: "https://forum.qbittorrent.org"
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

# qBittorrent

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Open-source BitTorrent client with a web UI. Lightweight, feature-rich, and completely free. Built-in search engine, RSS subscription, sequential downloading, and remote control via web interface. The download client that *arr applications talk to.

## Architectural Role

Applications/downloads layer: the download engine for the media stack. Radarr and Sonarr send download requests to qBittorrent, which handles the actual data transfer. Web UI allows management from any device.

## Technical Autonomy

- ✅ Works without internet (manages existing downloads, seeding on LAN)
- ✅ Stores data locally (downloads, config, torrent files)
- ✅ Does not require external accounts
- ✅ Standard torrent files — portable across any client
- ✅ No telemetry, no tracking

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅ | Pause all torrents, resume anytime. |
| Exit                  | ✅ | Downloads are standard files. Torrent files are portable. |
| Recoverability        | ✅ | Config backup. Re-add torrents from .torrent files or magnet links. |
| Visibility            | ✅ | GPL-2.0, fully auditable. C++/Qt codebase. |
| External Dependencies | ✅ | Fully self-contained. DHT/PEX for decentralized peer discovery. |

## Configuration (Minimal)

```yaml
services:
  qbittorrent:
    image: linuxserver/qbittorrent
    container_name: qbittorrent
    ports:
      - "8080:8080"
      - "6881:6881"
      - "6881:6881/udp"
    volumes:
      - ./config/qbittorrent:/config
      - /path/to/downloads:/downloads
    environment:
      - TZ=UTC
      - WEBUI_PORT=8080
    restart: unless-stopped
```

## Related Recipes

- Media Server recipe (planned)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| Transmission | A3 / T2 | Simpler, lighter. Fewer features. |
| Deluge | A3 / T2 | Plugin-based architecture. Python. |
| rTorrent + ruTorrent | A3 / T2 | Terminal client + web UI. Power user choice. |

---

## Trajectory

**Direction: stable.**

qBittorrent has been the go-to open-source torrent client since ~2010. GPL-2.0, community-driven, no commercial interests. Consistent releases, active development.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | GPL-2.0, unchanged. |
| Feature gating | ✅ | No paid tier. No ads. |
| Self-hosting | ✅ | Native + Docker. Cross-platform. |
| Governance | ✅ | Community-driven, multiple maintainers. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [qbittorrent.org](https://www.qbittorrent.org)
- **Repository:** [github.com/qbittorrent/qBittorrent](https://github.com/qbittorrent/qBittorrent)
- **Docker image:** `linuxserver/qbittorrent`
