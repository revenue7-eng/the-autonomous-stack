---
nav_exclude: true
title: "HeliBoard"
category: "mobile/keyboard"
status: "stable"
license: "Apache-2.0"
source: "https://github.com/Helium314/HeliBoard"
repository: "https://github.com/Helium314/HeliBoard"
documentation: "https://github.com/Helium314/HeliBoard/wiki"
docker_image: "-"
community: "https://github.com/Helium314/HeliBoard/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["External Dependencies", "Visibility"]
---

# HeliBoard

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Open-source keyboard for Android. No internet permission — your keystrokes never leave your device. Successor to OpenBoard with active development. Supports multilingual typing, themes, gesture typing (with library), and clipboard history.

## Architectural Role

Client-side input layer — keyboard. Zero network access. Your keyboard sees everything you type — this one keeps it local.

## Technical Autonomy

- [x] Works without internet (no network permission at all)
- [x] Stores data locally (dictionary, clipboard on-device)
- [x] Does not require external accounts
- [x] Allows data export (settings backup)
- [x] Provides offline updates (F-Droid)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Switch keyboard anytime. |
| Exit                  | ✅     | Standard Android keyboard. No lock-in. |
| Recoverability        | ✅     | Settings export/import. |
| Visibility            | ✅     | Fully open-source. No hidden network calls. |
| External Dependencies | ✅     | Zero. No network permission. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

Install from F-Droid. Go to Settings → System → Keyboard → select HeliBoard. Download offline dictionaries for your languages.

## Related Recipes

- [Mobile Apps](../mobile.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [OpenBoard](openboard.md) | A3 / T2 | Predecessor. Less actively maintained. |

---

## Trajectory

**Direction: opening**

Active development. Growing feature set. Maintained fork of OpenBoard with many improvements. Community contributions welcomed.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | Apache-2.0. |
| Feature gating | ✅ | All features free. |
| Self-hosting | ✅ | Client app. |
| Governance | ✅ | Community-maintained. Active contributor base. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** https://github.com/Helium314/HeliBoard
- **Documentation:** https://github.com/Helium314/HeliBoard/wiki
- **Repository:** https://github.com/Helium314/HeliBoard
- **Docker image:** —
- **Community:** https://github.com/Helium314/HeliBoard/discussions
