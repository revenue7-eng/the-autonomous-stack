---
nav_exclude: false
trajectory: "opening"
parent: "Technology Catalog"
nav_order: 99
title: "Headscale"
category: "network/vpn"
status: "stable"
license: "BSD-3-Clause"
source: "https://github.com/juanfont/headscale"
repository: "https://github.com/juanfont/headscale"
documentation: "https://headscale.net"
docker_image: "headscale/headscale"
community: "https://github.com/juanfont/headscale/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker", "wireguard"]
optional_deps: ["prometheus"]
depended_by: []
critical_criteria: ["External Dependencies", "Exit"]
---

# Headscale

> **TAS Score: S3/3 — D5/5 · A3 / T2**

## Brief Description

Self-hosted implementation of the Tailscale coordination server. Use Tailscale clients (which are open source) with a server you control. Eliminates the only proprietary component of the Tailscale stack — the control plane.

## Architectural Role

Network layer. Replaces Tailscale's cloud coordination server with a self-hosted alternative. Clients connect to your Headscale instance instead of Tailscale's servers — full WireGuard mesh, zero cloud dependency.

## Technical Autonomy

- [x] Works without internet (after initial setup)
- [x] Stores data locally
- [x] Does not require external accounts
- [x] Allows data export (SQLite database)
- [ ] Provides offline updates

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Clean stop; clients fall back to direct WireGuard |
| Exit                  | ✅     | SQLite database is portable; WireGuard configs exportable |
| Recoverability        | ✅     | Standard SQLite backup; config is code |
| Visibility            | ✅     | BSD-3-Clause, fully auditable |
| External Dependencies | ✅     | No cloud dependency; fully self-contained |

## Configuration (Minimal)

```yaml
services:
  headscale:
    image: headscale/headscale:latest
    command: serve
    volumes:
      - ./config:/etc/headscale
      - ./data:/var/lib/headscale
    ports:
      - "8080:8080"
      - "9090:9090"
```

```yaml
# /etc/headscale/config.yaml (minimal)
server_url: https://headscale.yourdomain.com
listen_addr: 0.0.0.0:8080
private_key_path: /var/lib/headscale/private.key
db_type: sqlite3
db_path: /var/lib/headscale/db.sqlite
```

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Tailscale](tailscale.md) | A2 / T1 | Easier setup, proprietary coordination server |
| [WireGuard](wireguard.md) | A3 / T2 | Lower level, no mesh — manual peer management |

---

## Trajectory

**Direction: opening**

Headscale is a community project created specifically to provide a self-hosted alternative to Tailscale's proprietary control plane. BSD-3-Clause licensed, no commercial entity, growing contributor base. Tailscale has not moved against Headscale and has even acknowledged its existence positively. The project is maturing rapidly.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | BSD-3-Clause since launch; no changes |
| Feature gating | ✅ | No paid tier; all features available |
| Self-hosting | ✅ | Self-hosting is the only deployment model |
| Governance | ✅ | Community-governed; no corporate control; growing contributor base |

---

## Sources

- **Website:** https://headscale.net
- **Documentation:** https://headscale.net/running-headscale-linux
- **Repository:** https://github.com/juanfont/headscale
- **Docker image:** headscale/headscale
- **Community:** https://github.com/juanfont/headscale/discussions
