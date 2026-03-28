---
nav_exclude: false
title: "Proxmox VE"
category: "compute/virtualization"
status: "stable"
license: "AGPL-3.0"
source: "https://www.proxmox.com/en/proxmox-virtual-environment"
repository: "https://git.proxmox.com"
documentation: "https://pve.proxmox.com/wiki/Main_Page"
docker_image: "-"
community: "https://forum.proxmox.com"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Recoverability", "Exit"]
trajectory: "stable"
parent: Technology Catalog
nav_order: 99
---

# Proxmox VE

> **TAS Score: S3/3 — D4/5** — A3 / T2
> D4 not D5: subscription nag popup on every login for users without a paid subscription (Q5 urgency). Functionally identical with or without subscription — the popup is the only difference.

## Brief Description

Open-source server virtualization platform. Run multiple virtual machines and Linux containers (LXC) on a single physical server with a web-based management interface. Based on Debian. The self-hosted alternative to VMware ESXi and cloud VM providers.

## Architectural Role

Compute/virtualization layer: sits between hardware and everything else. Instead of installing Debian + Docker directly on hardware, install Proxmox → create VMs → run Docker inside VMs. Isolation, snapshots, live migration, backup — all at the hypervisor level. One physical server becomes multiple independent servers.

## Technical Autonomy

- ✅ Works without internet (fully offline after installation)
- ✅ Stores data locally (VMs, containers, backups all on local storage)
- ✅ Does not require external accounts
- ✅ VM images are standard QCOW2/raw — portable to any KVM hypervisor
- ✅ Built-in backup and snapshot system
- ⚠️ Subscription nag popup on login (cosmetic, not functional)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅ | VMs can be paused, suspended, snapshotted. Full state preservation. |
| Exit                  | ✅ | VMs are standard KVM images. Export and run on any KVM host. |
| Recoverability        | ✅ | Built-in backup (vzdump), snapshots, replication. Best-in-class for self-hosted recovery. |
| Visibility            | ✅ | AGPL-3.0. Full source available. Debian-based. |
| External Dependencies | ✅ | No cloud dependency. Subscription is optional. |

## Configuration (Minimal)

Download ISO from [proxmox.com](https://www.proxmox.com/en/downloads), install on bare metal.

Remove subscription nag (optional):

```bash
# After install, access web UI at https://your-ip:8006
# To remove the nag without subscription:
sed -Ei.bak "s/NotFound/Active/g" /usr/share/javascript/proxmox-widget-toolkit/proxmoxlib.js
systemctl restart pveproxy.service
```

Create your first VM:

```
Web UI → Create VM → select ISO → allocate RAM/CPU/disk → Start
```

## Related Recipes

- [Minimal Autonomous Server](../recipes/minimal-server.md) — run inside a Proxmox VM for isolation and snapshots

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Debian](debian.md) + KVM | A3 / T2 | Manual setup. No web UI. Full control. |
| XCP-ng | A3 / T2 | Xen-based. Alternative to Proxmox with different hypervisor. |
| VMware ESXi | A1 / T0 | Proprietary. Broadcom acquisition made free tier uncertain. |
| Unraid | A2 / T0 | Proprietary. Popular for NAS + VMs. Paid license. |

---

## Trajectory

**Direction: stable.**

Proxmox Server Solutions GmbH (Austrian company) has maintained Proxmox VE since 2008. AGPL-3.0, consistent releases, growing community. The business model (support subscriptions) funds development without restricting features. VMware's Broadcom acquisition has driven significant migration to Proxmox.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | AGPL-3.0, unchanged. No license rug-pull risk. |
| Feature gating | ✅ | Zero functional difference between free and subscribed. Enterprise repo is slightly faster updates. |
| Self-hosting | ✅ | The entire point of the product. |
| Governance | ➖ | Proxmox GmbH controls development. Small company, aligned incentives. Not community-governed like Debian. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [proxmox.com](https://www.proxmox.com/en/proxmox-virtual-environment)
- **Documentation:** [pve.proxmox.com/wiki](https://pve.proxmox.com/wiki/Main_Page)
- **Repository:** [git.proxmox.com](https://git.proxmox.com)
- **Community:** [forum.proxmox.com](https://forum.proxmox.com)
