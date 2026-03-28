---
nav_exclude: false
title: "Debian"
category: "compute/os"
status: "stable"
license: "DFSG (multiple free licenses)"
source: "https://www.debian.org"
repository: "https://salsa.debian.org/debian"
documentation: "https://www.debian.org/doc/"
docker_image: "-"
community: "https://www.debian.org/community/"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: ["docker"]
critical_criteria: ["Exit", "Recoverability"]
trajectory: "stable"
parent: Technology Catalog
nav_order: 99
---

# Debian

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

The universal operating system. Community-driven Linux distribution known for stability, security, and commitment to free software. The foundation of Ubuntu, Proxmox, and countless other distributions. The default choice for servers that need to run for years without surprises.

## Architectural Role

Compute/OS layer: the base operating system on which everything else runs. Docker, containers, services — all sit on top of the OS. Debian's stability means the foundation doesn't shift under your stack. Every TAS recipe assumes Debian as the base OS.

## Technical Autonomy

- ✅ Works without internet (fully functional offline after installation)
- ✅ Stores data locally (everything is local by default)
- ✅ Does not require external accounts (no login, no telemetry, no cloud tie-in)
- ✅ Allows data export (standard filesystem, no proprietary formats)
- ✅ Offline updates possible (via local mirror or USB)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅ | Shut down, boot up. No data loss, no state to maintain. |
| Exit                  | ✅ | Standard Linux — migrate to any other distribution. Data is filesystem-level portable. |
| Recoverability        | ✅ | Mature backup tools, snapshots, full disk cloning. Battle-tested recovery. |
| Visibility            | ✅ | 100% free software by default. DFSG (Debian Free Software Guidelines) enforced. |
| External Dependencies | ✅ | No mandatory cloud services. No telemetry. No accounts. |

## Configuration (Minimal)

Download ISO from [debian.org](https://www.debian.org/distrib/), install on hardware or VM.

Post-install server setup:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y curl git ufw
sudo ufw allow ssh
sudo ufw enable
```

## Related Recipes

- [Minimal Autonomous Server](../recipes/minimal-server.md) — starts with Debian
- [Family Cloud](../recipes/family-cloud.md) — Debian base
- [Media Server](../recipes/media-server.md) — Debian base
- [Home Office](../recipes/home-office.md) — Debian base

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Ubuntu Server](ubuntu-server.md) | A3 / T2 | Based on Debian. More packages, but Snap and Ubuntu Pro add commercial pressure. |
| [Proxmox VE](proxmox.md) | A3 / T2 | Debian-based virtualization platform. Run multiple VMs on one machine. |
| Fedora Server | A3 / T2 | Red Hat-based. Newer packages, shorter support cycles. |
| Alpine Linux | A3 / T2 | Minimal, musl-based. Popular for containers, unusual for servers. |

---

## Trajectory

**Direction: stable.**

Debian has been community-governed since 1993. No corporation controls it. The Debian Social Contract and DFSG (Debian Free Software Guidelines) are constitutional documents that bind the project to free software principles. This is the most stable trajectory in the entire TAS catalog.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | DFSG-compliant only. Non-free is separate repository, disabled by default. 30+ years unchanged. |
| Feature gating | ✅ | No paid tier. No commercial version. No enterprise edition. |
| Self-hosting | ✅ | The definition of self-hosted. |
| Governance | ✅ | Elected project leader. Constitutional governance. No corporate owner. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [debian.org](https://www.debian.org)
- **Documentation:** [debian.org/doc](https://www.debian.org/doc/)
- **Repository:** [salsa.debian.org](https://salsa.debian.org/debian)
