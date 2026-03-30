---
nav_exclude: true
title: "LineageOS"
category: "compute/os"
status: "stable"
license: "Apache-2.0"
source: "https://lineageos.org"
repository: "https://github.com/LineageOS"
documentation: "https://wiki.lineageos.org"
docker_image: "-"
community: "https://reddit.com/r/LineageOS"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Exit"]
---

# LineageOS

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

The longest-running custom Android distribution. Successor to CyanogenMod. Supports 200+ devices. No Google services by default — clean AOSP-based experience with quality-of-life improvements.

## Architectural Role

Base operating system layer — mobile. Widest device support of any custom Android OS.

## Technical Autonomy

- [x] Works without internet
- [x] Stores data locally
- [x] Does not require external accounts
- [x] Allows data export (standard Android)
- [x] Provides offline updates (sideload ZIP)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Your device, your OS. |
| Exit                  | ✅     | Flash stock or another ROM. |
| Recoverability        | ✅     | TWRP/recovery, nandroid backups. |
| Visibility            | ✅     | Fully open-source. Massive contributor base. |
| External Dependencies | ✅     | No mandatory external services. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

Install via:
1. Unlock bootloader
2. Flash custom recovery (TWRP or Lineage Recovery)
3. Flash LineageOS ZIP
4. Optionally flash GApps (not recommended for autonomy)

## Related Recipes

- [Mobile Apps](../mobile.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [GrapheneOS](grapheneos.md) | A3 / T2 | Stronger security. Pixel only. |
| [CalyxOS](calyxos.md) | A3 / T2 | microG included. Fewer devices. |

---
## Trajectory
**Direction: stable**
Over a decade of continuous development. Largest custom ROM community. Volunteer-maintained — no commercial pressure. Steady device support.
**Signal assessment:**
| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | Apache-2.0, unchanged since CyanogenMod. |
| Feature gating | ✅ | All features free. |
| Self-hosting | ✅ | Nothing to host. |
| Governance | ✅ | Community-governed. Multiple maintainers per device. |
**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing
---

## Sources

- **Website:** https://lineageos.org
- **Documentation:** https://wiki.lineageos.org
- **Repository:** https://github.com/LineageOS
- **Docker image:** —
- **Community:** https://reddit.com/r/LineageOS
