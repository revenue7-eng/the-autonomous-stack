---
nav_exclude: false
title: "Ubuntu Server"
category: "compute/os"
status: "stable"
license: "Multiple (GPL, LGPL, etc.)"
source: "https://ubuntu.com/server"
repository: "https://launchpad.net/ubuntu"
documentation: "https://ubuntu.com/server/docs"
docker_image: "-"
community: "https://discourse.ubuntu.com"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: ["docker"]
critical_criteria: ["Exit", "Recoverability"]
trajectory: "mixed"
parent: Technology Catalog
nav_order: 99
---

# Ubuntu Server

> **TAS Score: S3/3 — D3/5** — A3 / T2
> D3 not D5: Ubuntu Pro nag messages on login and `apt upgrade` (Q5 urgency); Snap packages auto-update with no user control over timing, phone home to Canonical's Snap Store (Q4, Q6); `ubuntu-advantage-tools` installed by default collects system data (Q4). Ubuntu is free but increasingly pushes paid services.

## Brief Description

The most widely deployed Linux server distribution. Based on Debian with newer packages, longer commercial support (LTS), and extensive documentation. Backed by Canonical Ltd. Powerful and well-supported, but trending toward commercial lock-in through Snap and Ubuntu Pro.

## Architectural Role

Compute/OS layer: alternative to Debian as server base. Most cloud VPS providers default to Ubuntu. More tutorials and guides available than any other server OS. If something works on Linux, there's an Ubuntu guide for it.

## Technical Autonomy

- ✅ Works without internet
- ✅ Stores data locally
- ⚠️ Snap daemon phones home to Canonical's Snap Store by default
- ⚠️ Ubuntu Pro prompts on login and during upgrades
- ✅ Allows data export (standard Linux filesystem)
- ✅ Snap can be removed: `sudo apt remove snapd`

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅ | Standard Linux behavior. |
| Exit                  | ✅ | Standard Linux — migrate to Debian or any other distribution. |
| Recoverability        | ✅ | Standard backup tools. LTS has 5-year support. |
| Visibility            | ✅ | Open source. Snap client is open, Snap Store is proprietary. |
| External Dependencies | ⚠️ | Snap auto-updates from Canonical's store. Ubuntu Pro telemetry. Can be disabled but requires effort. |

## Configuration (Minimal)

Download from [ubuntu.com/server](https://ubuntu.com/server), install.

Remove Snap and Ubuntu Pro prompts (recommended for autonomous setup):

```bash
sudo apt remove -y snapd ubuntu-advantage-tools
sudo apt-mark hold snapd
```

## Related Recipes

- Any TAS recipe works on Ubuntu Server (replace Debian with Ubuntu)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Debian](debian.md) | A3 / T2 | TAS recommended. No commercial pressure, no Snap. |
| [Proxmox VE](proxmox.md) | A3 / T2 | Debian-based with built-in virtualization. |
| Fedora Server | A3 / T2 | Red Hat-based. Newer packages, shorter cycles. |

---

## Trajectory

**Direction: mixed.**

Ubuntu Server itself is open source and functional. But Canonical is increasingly adding commercial friction: Snap packages (forced for some core tools, auto-update, phone home), Ubuntu Pro nag messages, telemetry. The OS works perfectly without these — but removing them takes effort that shouldn't be necessary.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | Core OS remains open source. |
| Feature gating | ⚠️ | Ubuntu Pro gates extended security updates (ESM) behind subscription. Livepatch requires Pro. |
| Self-hosting | ⚠️ | Snap Store is centralized and proprietary. No self-hosted Snap Store. Firefox, Chromium, LXD forced to Snap. |
| Governance | ⚠️ | Canonical Ltd. controls direction. Community input limited. Snap decisions overrode community objections. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [ubuntu.com/server](https://ubuntu.com/server)
- **Documentation:** [ubuntu.com/server/docs](https://ubuntu.com/server/docs)
- **Repository:** [launchpad.net/ubuntu](https://launchpad.net/ubuntu)
