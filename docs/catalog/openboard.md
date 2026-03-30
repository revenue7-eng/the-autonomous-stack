---
nav_exclude: true
title: "OpenBoard"
category: "mobile/keyboard"
status: "stable"
license: "GPL-3.0"
source: "https://github.com/openboard-team/openboard"
repository: "https://github.com/openboard-team/openboard"
documentation: "-"
docker_image: "-"
community: "-"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["External Dependencies"]
---

# OpenBoard

> **TAS Score: S3/3 — D4/5** — A3 / T2
> _D4 not D5: development has stalled — HeliBoard is the actively maintained successor (Q8)._

## Brief Description

Open-source Android keyboard based on AOSP keyboard. No internet permission, no data collection. Simple and lightweight. Largely superseded by HeliBoard, which continues active development.

## Architectural Role

Client-side input layer — keyboard. No network access.

## Technical Autonomy

- [x] Works without internet (no network permission)
- [x] Stores data locally
- [x] Does not require external accounts
- [x] Allows data export (settings)
- [x] Provides offline updates (F-Droid)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Switch anytime. |
| Exit                  | ✅     | Standard Android keyboard. |
| Recoverability        | ✅     | Reinstall from F-Droid. |
| Visibility            | ✅     | Fully open-source. |
| External Dependencies | ✅     | Zero. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

Install from F-Droid. Select as default keyboard. Consider migrating to HeliBoard for active development.

## Related Recipes

- [Mobile Apps](../mobile.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [HeliBoard](heliboard.md) | A3 / T2 | Actively maintained fork. More features. Recommended. |

---

## Trajectory

**Direction: closing**

Development has largely stopped. HeliBoard has taken over as the maintained fork. Use HeliBoard for new installations.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | GPL-3.0. |
| Feature gating | ✅ | All features free. |
| Self-hosting | ✅ | Client app. |
| Governance | ⚠️ | Unmaintained. HeliBoard is the successor. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** https://github.com/openboard-team/openboard
- **Repository:** https://github.com/openboard-team/openboard
- **Docker image:** —
