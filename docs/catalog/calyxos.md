---
nav_exclude: true
title: "CalyxOS"
category: "compute/os"
status: "stable"
license: "Apache-2.0"
source: "https://calyxos.org"
repository: "https://gitlab.com/CalyxOS"
documentation: "https://calyxos.org/docs"
docker_image: "-"
community: "https://calyxos.org/community"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Exit", "External Dependencies"]
---

# CalyxOS

> **TAS Score: S3/3 — D4/5** — A3 / T2
> _D4 not D5: microG provides partial Google compatibility — some telemetry possible (Q4)._

## Brief Description

Privacy-focused Android OS with microG for basic Google service compatibility. Easier transition from stock Android than GrapheneOS — F-Droid and Aurora Store pre-installed. Supports Pixel and select Fairphone/Motorola devices.

## Architectural Role

Base operating system layer — mobile. Includes microG for push notifications and location services without full Google Play Services.

## Technical Autonomy

- [x] Works without internet (fully functional offline)
- [x] Stores data locally (on-device, encrypted)
- [x] Does not require external accounts (no Google account needed)
- [x] Allows data export (standard Android backup, file access)
- [x] Provides offline updates (OTA or sideload)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Your device, your OS. |
| Exit                  | ✅     | Flash stock or another OS. |
| Recoverability        | ✅     | Standard Android recovery. |
| Visibility            | ✅     | Fully open-source. |
| External Dependencies | ⚠️     | Pixel/Fairphone/Motorola only. microG connects to some Google endpoints. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

Install via:
1. Unlock bootloader
2. Use CalyxOS flasher tool (calyxos.org/install)
3. Follow guided installation

No server deployment required.

## Related Recipes

- [Mobile Apps](../mobile.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [GrapheneOS](grapheneos.md) | A3 / T2 | More security hardening. No microG (sandboxed Play instead). |
| [LineageOS](lineageos.md) | A3 / T2 | Widest device support. No microG by default. |

---
## Trajectory
**Direction: stable**
Calyx Institute is a nonprofit. Steady development, expanding device support. microG dependency adds complexity but improves usability.
**Signal assessment:**
| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | Apache-2.0 and various open-source licenses. |
| Feature gating | ✅ | All features free. |
| Self-hosting | ✅ | Nothing to host. |
| Governance | ✅ | Calyx Institute (501c3 nonprofit). |
**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing
---

## Sources

- **Website:** https://calyxos.org
- **Documentation:** https://calyxos.org/docs
- **Repository:** https://gitlab.com/CalyxOS
- **Docker image:** —
- **Community:** https://calyxos.org/community
