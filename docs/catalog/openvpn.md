---
nav_exclude: false
parent: "Technology Catalog"
nav_order: 99
title: "OpenVPN"
category: "network/vpn"
status: "stable"
license: "GPL-2.0"
source: "https://github.com/OpenVPN/openvpn"
repository: "https://github.com/OpenVPN/openvpn"
documentation: "https://openvpn.net/community-resources"
docker_image: "kylemanna/openvpn"
community: "https://forums.openvpn.net"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: []
depended_by: []
critical_criteria: ["Exit", "External Dependencies"]
---

# OpenVPN

> **TAS Score: S3/3 — D4/5 · A3 / T2**
> _(D4 not D5: OpenVPN Inc. is pushing CloudConnexa (SaaS VPN) — commercial focus shifting away from self-hosted.)_

## Brief Description

Battle-tested open-source VPN protocol and implementation. SSL/TLS-based, highly configurable, runs on all platforms. The reference implementation for site-to-site and remote access VPN since 2001.

## Architectural Role

Network layer. Provides encrypted tunnels between clients and servers. Older and more complex than WireGuard but more widely supported in enterprise environments and legacy hardware.

## Technical Autonomy

- [x] Works without internet (LAN only)
- [x] Stores data locally
- [x] Does not require external accounts
- [x] Allows data export (config files)
- [ ] Provides offline updates

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Clean stop, no permanent damage |
| Exit                  | ✅     | Config files are portable; no lock-in |
| Recoverability        | ✅     | PKI and config backup is straightforward |
| Visibility            | ✅     | GPL-2.0, fully auditable |
| External Dependencies | ✅     | Runs fully self-contained; no cloud required |

## Configuration (Minimal)

```yaml
services:
  openvpn:
    image: kylemanna/openvpn:latest
    cap_add:
      - NET_ADMIN
    volumes:
      - ./openvpn-data:/etc/openvpn
    ports:
      - "1194:1194/udp"
```

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [WireGuard](wireguard.md) | A3 / T2 | Faster, simpler, kernel-level — preferred for new deployments |
| [Tailscale](tailscale.md) | A2 / T1 | Easier setup, proprietary coordination server |
| [Headscale](headscale.md) | A3 / T2 | Self-hosted Tailscale coordination server |

---

## Trajectory

**Direction: stable**

OpenVPN protocol and the open-source implementation have been stable since 2001 with no license changes. However, OpenVPN Inc. is increasingly focused on CloudConnexa, their SaaS VPN product. The community edition receives less attention than the commercial products. For new deployments, WireGuard is generally preferred — simpler, faster, and with stronger governance.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | GPL-2.0 since launch; no changes |
| Feature gating | ➖ | Community edition unchanged; commercial focus on CloudConnexa |
| Self-hosting | ➖ | Still works well; but new features go to commercial products first |
| Governance | ⚠️ | OpenVPN Inc. drives direction; community edition is maintenance mode |

---

## Sources

- **Website:** https://openvpn.net
- **Documentation:** https://openvpn.net/community-resources/how-to
- **Repository:** https://github.com/OpenVPN/openvpn
- **Docker image:** kylemanna/openvpn
- **Community:** https://forums.openvpn.net
