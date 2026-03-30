---
nav_exclude: false
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
depends_on: ["docker"]
optional_deps: []
depended_by: ["keepass", "obsidian"]
critical_criteria: ["Exit", "Recoverability"]
trajectory: "stable"
parent: Technology Catalog
nav_order: 99
---

# Syncthing

> **TAS Score: S3/3 — D5/5** — A3 / T2
>
> _Assessment criteria: [v1.0](assessment-criteria.md). Last verified: 2025-05._

## Brief Description

Peer-to-peer file synchronisation tool that keeps folders in sync across multiple devices — without a central server, without cloud accounts, without trusting a third party.

## Architectural Role

Storage layer: provides continuous, encrypted file sync between devices over the local network or via relay. Replaces Dropbox, Google Drive, and similar cloud sync services.

---

## Formal Assessment

### S1: Pause

| Test | Result | Evidence |
|------|--------|----------|
| Can you stop the process without a special shutdown procedure? | ✅ Yes | `docker stop syncthing` or close the app. Clean shutdown. |
| After stopping, is all data still on disk in a readable state? | ✅ Yes | Files are ordinary files on your filesystem. Nothing changes when Syncthing stops. |
| Can you restart and continue where you left off? | ✅ Yes | Restart → resumes sync from where it left off. No re-registration. |

**S1 = Yes**

### S2: Exit

| Test | Result | Evidence |
|------|--------|----------|
| Is there a documented export mechanism? | ✅ Yes | No export needed. Files ARE your data — they live on your filesystem as regular files. |
| Does the export include ALL user data? | ✅ Yes | All data is always on disk. Syncthing adds only a `.stfolder` marker and `.stversions` for versioning. |
| Is the export in a standard, reusable format? | ✅ Yes | Files are in their original format. Stop Syncthing → files remain exactly as they are. |
| Can another tool import the exported data? | ✅ Yes | Any tool can read the files. No import step needed. |

**S2 = Yes**

### S3: Recoverability

| Test | Result | Evidence |
|------|--------|----------|
| Does the service support backups? | ✅ Yes | Files are regular files — any backup tool works. Built-in file versioning (`.stversions`). |
| Can you restore from backup to a working state? | ✅ Yes | Copy files back. Reinstall Syncthing. Add folder. Done. |
| Does a restore give you back the SAME state? | ✅ Yes | All data restored. Device IDs regenerated (expected), but no data loss. |

**S3 = Yes**

### Autonomy Level

| S1 | S2 | S3 | Level |
|----|----|----|-------|
| Yes | Yes | Yes | **A3** |

### Transparency Level

| Test | Result | Evidence |
|------|--------|----------|
| Source code publicly available? | ✅ Yes | github.com/syncthing/syncthing |
| License OSI-approved? | ✅ Yes | MPL-2.0 |

**T = T2**

### Diagnostic Score

| # | Question | Result | Evidence |
|---|----------|--------|----------|
| D1 | Personalisation | ✅ Clean | No analytics. No user tracking. No recommendation engine. Usage reporting is opt-in and anonymous. |
| D2 | Urgency | ✅ Clean | No notifications beyond sync status. No forced updates. No deadlines. |
| D3 | Hidden cost | ✅ Clean | No ads. No data sharing. No identity requirements. No lock-in. |
| D4 | Transparency fragility | ✅ Clean | Value comes from file sync, not from information asymmetry. Fully transparent operation. |
| D5 | Trajectory | ✅ Clean | MPL-2.0 since launch (2014). Syncthing Foundation governs the project. No paid tier. No corporate owner. Discovery/relay servers are self-hostable. |

**D-score: D5/5** (0 concerns)

---

## Counterarguments

| Claim | Challenge | Resolution |
|-------|-----------|------------|
| **A3: fully autonomous** | Relies on discovery servers to find peers over the internet | Discovery servers are operated by the Foundation but fully self-hostable. LAN sync works without them entirely. |
| **A3: fully autonomous** | Relay servers needed when direct connection fails (NAT) | Relay servers are optional, self-hostable, and only carry encrypted data. LAN sync never uses them. |
| **D5: no concerns** | Usage reporting exists | Opt-in, anonymous, aggregated. Disabled by default in Docker deployments. Not a concern. |

---

## Configuration (Minimal)

```yaml
services:
  syncthing:
    image: syncthing/syncthing:latest
    container_name: syncthing
    ports:
      - "8384:8384"
      - "22000:22000"
    volumes:
      - ./syncthing-config:/var/syncthing/config
      - ./syncthing-data:/var/syncthing/data
    restart: unless-stopped
```

## Related Recipes

- [Minimal Autonomous Server](../recipes/minimal-server.md)
- [GrapheneOS Mobile Stack](../recipes/grapheneos-mobile.md)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| Nextcloud | A3 / T2 | Heavier, server-centric, but offers calendar/contacts/office. |
| Resilio Sync | A2 / T0 | Similar P2P model but proprietary and closed source. |

---

## Trajectory

**Direction: stable.**

Syncthing is MPL-2.0 licensed and community-governed by the Syncthing Foundation. Development has been active and consistent since 2014. No corporate ownership, no paid tier, no cloud lock-in.

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | MPL-2.0; no changes since launch. |
| Feature gating | ✅ | No paid tier; all features free. |
| Self-hosting | ✅ | Discovery and relay servers are self-hostable. |
| Governance | ✅ | Syncthing Foundation; community-driven. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** https://syncthing.net
- **Documentation:** https://docs.syncthing.net
- **Repository:** https://github.com/syncthing/syncthing
- **Docker image:** https://hub.docker.com/r/syncthing/syncthing
- **Community:** https://forum.syncthing.net
