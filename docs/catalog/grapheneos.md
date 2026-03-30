---
nav_exclude: true
title: "GrapheneOS"
category: "compute/os"
status: "stable"
license: "MIT"
source: "https://grapheneos.org"
repository: "https://github.com/GrapheneOS"
documentation: "https://grapheneos.org/usage"
docker_image: "-"
community: "https://discuss.grapheneos.org"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Exit", "External Dependencies"]
---

# GrapheneOS

> **TAS Score: S3/3 — D4/5** — A3 / T2
> _D4 not D5: limited to Pixel devices only (Q8 — hardware dependency)._

## Brief Description

Hardened Android-based mobile OS focused on privacy and security. No Google services by default — optional sandboxed Google Play available for app compatibility. Verified boot, hardened memory allocator, network and sensor permissions per-app.

## Architectural Role

Base operating system layer — mobile. Foundation for the entire mobile autonomous stack.

## Technical Autonomy

- [x] Works without internet (fully functional offline)
- [x] Stores data locally (everything on-device, encrypted)
- [x] Does not require external accounts (no Google account needed)
- [x] Allows data export (standard Android backup, file access)
- [x] Provides offline updates (OTA or sideload)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Your device, your OS. |
| Exit                  | ✅     | Can relock bootloader, flash stock, or switch OS. |
| Recoverability        | ✅     | Factory reset, reflash. Standard Android recovery. |
| Visibility            | ✅     | Fully open-source. Security audited. |
| External Dependencies | ⚠️     | Pixel hardware dependency. Cannot install on other devices. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

Install via web installer:
1. Unlock bootloader on Pixel device
2. Visit https://grapheneos.org/install/web
3. Follow guided installation
4. Relock bootloader

No server deployment required.

## Related Recipes

- [Mobile Apps](../mobile.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [CalyxOS](calyxos.md) | A3 / T2 | Includes microG for easier Google compatibility. |
| [LineageOS](lineageos.md) | A3 / T2 | Supports 200+ devices. Less security hardening. |

---

## Trajectory

**Direction: opening**

Active development. Expanding Pixel device support with each release. Growing community. Funded by donations. No commercial pressure.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | MIT and various open-source licenses. |
| Feature gating | ✅ | All features free. |
| Self-hosting | ✅ | Nothing to host — it's an OS. |
| Governance | ✅ | GrapheneOS Foundation. Community-driven. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** https://grapheneos.org
- **Documentation:** https://grapheneos.org/usage
- **Repository:** https://github.com/GrapheneOS
- **Docker image:** —
- **Community:** https://discuss.grapheneos.org
