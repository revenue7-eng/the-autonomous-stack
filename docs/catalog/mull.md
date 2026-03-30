---
nav_exclude: true
title: "Mull"
category: "mobile/browser"
status: "stable"
license: "MPL-2.0"
source: "https://divestos.org/pages/our_apps#mull"
repository: "https://codeberg.org/nicucalcea/nicuca"
documentation: "https://divestos.org/pages/our_apps#mull"
docker_image: "-"
community: "-"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Visibility"]
---

# Mull

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Firefox fork with telemetry removed and privacy hardened. Applies arkenfox user.js settings by default. Available on F-Droid. Android only. The most private Firefox-based mobile browser.

## Architectural Role

Client-side application layer — web browsing. Hardened Firefox without Mozilla telemetry.

## Technical Autonomy

- [ ] Works without internet (browser needs internet)
- [x] Stores data locally
- [x] Does not require external accounts
- [x] Allows data export (bookmarks, passwords)
- [x] Provides offline updates (F-Droid)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Stop anytime. Local data. |
| Exit                  | ✅     | Standard Firefox profile. |
| Recoverability        | ✅     | Reinstall from F-Droid. |
| Visibility            | ✅     | Open-source. Patches public. |
| External Dependencies | ✅     | No telemetry, no default Google endpoints. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

Install from F-Droid (DivestOS repo). Works out of the box with hardened defaults.

## Related Recipes

- [Mobile Apps](../mobile.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Firefox](firefox.md) | A3 / T2 | Mainstream. More extensions. Some telemetry by default. |
| [Brave](brave.md) | A3 / T1 | Chromium-based. Built-in ad blocking. |

---
## Trajectory
**Direction: stable**
Maintained by DivestOS project. Follows Firefox ESR releases. Small team but consistent updates.
**Signal assessment:**
| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | MPL-2.0 (inherits from Firefox). |
| Feature gating | ✅ | All features free. |
| Self-hosting | ✅ | Client app. |
| Governance | ⚠️ | Small team (DivestOS). Bus factor risk. |
**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing
---

## Sources

- **Website:** https://divestos.org/pages/our_apps#mull
- **Repository:** https://codeberg.org/nicucalcea/nicuca
- **Docker image:** —
