---
tags: [vpn, network, mesh, wireguard]
title: "Tailscale"
category: "network/vpn"
status: "stable"
license: "BSD-3-Clause (client) / Proprietary (coordination server)"
source: "https://tailscale.com"
repository: "https://github.com/tailscale/tailscale"
documentation: "https://tailscale.com/kb"
docker_image: "-"
community: "https://github.com/tailscale/tailscale/discussions"
autonomy_level: "A2"
transparency_level: "T1"
parent: Technology Catalog
nav_order: 53
---

# Tailscale

## Brief Description

Mesh VPN built on WireGuard. Zero‑config networking between devices. Uses a central coordination server for key exchange, NAT traversal, and access control — hosted by Tailscale.

## Architectural Role

Network layer: provides encrypted mesh connectivity between devices. Simplifies VPN setup dramatically compared to raw WireGuard.

## Technical Autonomy

- ⚠️ Works without internet — existing connections persist, but new device connections and key rotation require the coordination server
- ✅ Stores data locally — traffic flows directly between devices (peer‑to‑peer)
- ❌ Does not require external accounts — requires Tailscale account (via SSO providers)
- ⚠️ Allows data export — network configuration is partially exportable; ACL policies are stored on Tailscale's servers
- ✅ Provides offline updates — client can be updated manually

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status  | Comments |
| --------------------- | ------- | -------- |
| Pause                 | Yes     | VPN can be stopped on any device. |
| Exit                  | Partial | Traffic is yours (P2P), but network topology and ACL policies depend on Tailscale's coordination server. Migration to raw WireGuard requires reconfiguring every device. |
| Recoverability        | Partial | Device connections can be recreated. But if Tailscale changes terms or the coordination server is unreachable, new connections can't be established. |
| Visibility            | Partial | Client is open source. Coordination server is proprietary. You can audit what runs on your device, but not the control plane. |
| External Dependencies | No      | Depends on Tailscale's coordination server for key exchange and NAT traversal. Headscale exists as an open‑source alternative coordination server. |

## Why it's in the catalog

Tailscale is the best example of A2: it works mostly offline, data flows peer‑to‑peer, the client is open source — but the control plane is proprietary. You don't own your network topology. This is a deliberate trade‑off: massive convenience in exchange for a dependency on a single vendor's coordination server.

**What you gain:** Zero‑config VPN. NAT traversal that just works. MagicDNS. ACL policies. SSO integration. Minutes to set up vs. hours for raw WireGuard.

**What you give up:** Independence from Tailscale's coordination server. Full control over your network topology. The ability to operate if Tailscale is unreachable.

**The Headscale option:** [Headscale](https://github.com/jurassicpark/headscale) is an open‑source implementation of the Tailscale coordination server. Running it yourself moves Tailscale from A2/T1 to approximately A3/T2 — but you lose Tailscale's managed infrastructure and some features.

## Autonomous alternatives

* [WireGuard](wireguard.md) (A3/T2) — raw VPN, no coordination server, full control
* WireGuard + Headscale — Tailscale‑compatible mesh with self‑hosted control plane

## Trajectory

**Direction: stable with tension.**

Tailscale's client remains open source. The company is growing toward enterprise (SSO integration, audit logs, policy controls). The coordination server remains proprietary — but Headscale exists as a community alternative and Tailscale has not moved against it.

The tension: Tailscale's business model requires the coordination server to be valuable enough to pay for. If Headscale becomes good enough, the model is threatened. How Tailscale responds to that pressure will determine the trajectory. So far — neutral. Watch for changes to the client license or Headscale compatibility.

## Sources

* [Website](https://tailscale.com)

* [Documentation](https://tailscale.com/kb)

* [Repository (client)](https://github.com/tailscale/tailscale)

* [Headscale (open‑source coordination server)](https://github.com/jurassicpark/headscale)

* [Community](https://github.com/tailscale/tailscale/discussions)
