---
nav_exclude: false
title: "RustDesk"
category: "applications/remote-access"
status: "stable"
license: "AGPL-3.0"
source: "https://rustdesk.com"
repository: "https://github.com/rustdesk/rustdesk"
documentation: "https://rustdesk.com/docs/"
docker_image: "rustdesk/rustdesk-server"
community: "https://discord.gg/nDceKgxnkV"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: []
depended_by: []
critical_criteria: ["Pause", "Exit"]
trajectory: "opening"
parent: Technology Catalog
nav_order: 99
---

# RustDesk

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Self-hosted remote desktop application written in Rust. Works out of the box with no configuration. Replace TeamViewer, AnyDesk, and Chrome Remote Desktop with a solution where the relay server is yours. Clients available for Windows, macOS, Linux, iOS, and Android.

## Architectural Role

Remote access layer: peer-to-peer remote desktop with optional self-hosted relay and rendezvous servers. Direct connections when possible, relay through your server when NAT traversal fails. No third-party infrastructure required.

## Technical Autonomy

- ✅ Works without internet (on LAN with direct IP)
- ✅ Stores data locally (connection history, settings on each client)
- ✅ Does not require external accounts (with self-hosted server)
- ✅ No data to export (stateless relay)
- ✅ Full offline capability on local network

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅ | Stop the server, direct connections still work on LAN. |
| Exit                  | ✅ | Nothing to migrate — clients connect to any RustDesk server. |
| Recoverability        | ✅ | Server is stateless. Redeploy in minutes. |
| Visibility            | ✅ | AGPL-3.0, fully auditable. Written in Rust. |
| External Dependencies | ✅ | Fully self-hosted. No cloud dependency. |

## Configuration (Minimal)

```yaml
services:
  rustdesk-hbbs:
    image: rustdesk/rustdesk-server:latest
    container_name: hbbs
    command: hbbs
    ports:
      - "21115:21115"
      - "21116:21116"
      - "21116:21116/udp"
      - "21118:21118"
    volumes:
      - ./data/rustdesk:/root
    restart: unless-stopped

  rustdesk-hbbr:
    image: rustdesk/rustdesk-server:latest
    container_name: hbbr
    command: hbbr
    ports:
      - "21117:21117"
      - "21119:21119"
    volumes:
      - ./data/rustdesk:/root
    restart: unless-stopped
```

On clients: enter your server's IP in Settings → Network → ID/Relay Server.

## Related Recipes

- [Minimal Autonomous Server](../recipes/minimal-server.md)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| TeamViewer | A0 / T0 | Cloud-only, proprietary, aggressive commercial detection. |
| AnyDesk | A0 / T0 | Cloud-only, proprietary. |
| Apache Guacamole | A3 / T2 | Browser-based, supports RDP/VNC/SSH. No native client. |
| MeshCentral | A3 / T2 | Full remote management platform. More complex. |

---

## Trajectory

**Direction: opening.**

RustDesk has grown rapidly as the self-hosted TeamViewer alternative. AGPL-3.0 licensed, written in Rust for performance and security. Active development, growing community, expanding platform support.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | AGPL-3.0, unchanged. Strong copyleft. |
| Feature gating | ✅ | Pro features exist but self-hosted version is fully functional. |
| Self-hosting | ✅ | Self-hosting is the primary value proposition. Excellent documentation. |
| Governance | ➖ | Company-backed (RustDesk GmbH). Open source but corporate-led. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [rustdesk.com](https://rustdesk.com)
- **Repository:** [github.com/rustdesk/rustdesk](https://github.com/rustdesk/rustdesk)
- **Docker image:** `rustdesk/rustdesk-server`
