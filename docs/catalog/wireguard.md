---
nav_exclude: false
title: "WireGuard"
category: "network/vpn"
status: "stable"
license: "GPL-2.0"
source: "https://www.wireguard.com"
repository: "https://git.zx2c4.com/wireguard-linux-compat"
documentation: "https://www.wireguard.com/quickstart/"
docker_image: "https://hub.docker.com/r/linuxserver/wireguard"
community: "https://www.reddit.com/r/WireGuard/"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Pause"]
parent: Technology Catalog
nav_order: 99
---

# WireGuard

> **TAS Score: S3/3 -- D5/5** -- A3 / T2
> **Critical criteria for this category:** Pause.


## Brief Description
Extremely simple yet fast and modern VPN that utilizes state‑of‑the‑art cryptography. Designed for ease of use and minimal attack surface.

## Architectural Role
Network layer: provides secure, peer‑to‑peer VPN connections without a central server. Can be used to remotely access a private network.

## Technical Autonomy
- ✅ Works without internet (once configured, it can establish local peer‑to‑peer links)
- ✅ Stores data locally (configuration files, keys)
- ✅ Does not require external accounts
- ✅ Allows data export (config files can be copied)
- ✅ Provides offline updates (manual via package manager)

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
|-----------|--------|----------|
| **Pause** | ✅ | VPN can be stopped/started manually; no forced background activity. |
| **Exit** | ✅ | Disabling VPN leaves your network untouched; no lock‑in. |
| **Recoverability** | ✅ | Configurations and keys can be backed up and restored. |
| **Visibility** | ✅ | Open source, auditable, simple codebase. |
| **External Dependencies** | ✅ | No central servers; works entirely offline. |

## Configuration (Minimal)

Server side (example `/etc/wireguard/wg0.conf`):

```ini
[Interface]
Address = 10.0.0.1/24
PrivateKey = <server-private-key>
ListenPort = 51820

[Peer]
PublicKey = <client-public-key>
AllowedIPs = 10.0.0.2/32
AllowedIPs = 10.0.0.2/32
```

### Client side

```ini
[Interface]
Address = 10.0.0.2/24
PrivateKey = <client-private-key>

[Peer]
PublicKey = <server-public-key>
Endpoint = your-server-ip:51820
AllowedIPs = 0.0.0.0/0
```

## Related Recipes
- [Minimal Autonomous Server](../recipes/minimal-server.md) – uses WireGuard for secure remote access.

## Alternatives
- **OpenVPN** – more complex, heavier, slower.
- **IPsec** – powerful but difficult to configure.
- **Tailscale** – built on WireGuard but relies on central coordination servers.

---

## Trajectory

**Direction: stable.**

WireGuard is GPL-2.0 licenced and has been merged into the Linux kernel (5.6, 2020). Development is led by Jason Donenfeld with ZX2C4 LLC, but the protocol specification is public and there are multiple independent implementations. Kernel inclusion provides structural stability.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | GPL-2.0; merged into Linux kernel in 2020 — structural stability guaranteed. |
| Feature gating | ✅ | No paid tier; no commercial entity; protocol is a public standard. |
| Self-hosting | ✅ | Kernel-level integration; no external service dependencies. |
| Governance | ✅ | Linux kernel governance; multiple independent implementations (boringtun, wireguard-go, etc.). |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- [Website](https://www.wireguard.com)

- [Documentation](https://www.wireguard.com/quickstart/)

- [Repository](https://git.zx2c4.com/wireguard-linux-compat)

- [Docker image](https://hub.docker.com/r/linuxserver/wireguard)

- [Community](https://www.reddit.com/r/WireGuard/)
-e
