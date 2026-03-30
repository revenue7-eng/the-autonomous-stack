---
nav_exclude: true
title: "Open Camera"
category: "mobile/camera"
status: "stable"
license: "GPL-3.0"
source: "https://opencamera.org.uk"
repository: "https://sourceforge.net/p/opencamera/code"
documentation: "https://opencamera.org.uk/help.html"
docker_image: "-"
community: "https://sourceforge.net/p/opencamera/discussion"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["External Dependencies"]
---

# Open Camera

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Open-source camera app for Android. No internet access, no tracking. Full manual controls (ISO, shutter speed, focus), HDR, video recording, timelapse. Saves to standard JPEG/PNG/MP4.

## Architectural Role

Client-side application layer — camera. No network component. Purely on-device image capture.

## Technical Autonomy

- [x] Works without internet (no network permission)
- [x] Stores data locally (standard media files)
- [x] Does not require external accounts
- [x] Allows data export (standard photo/video formats)
- [x] Provides offline updates (F-Droid)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Nothing to pause. |
| Exit                  | ✅     | Standard file formats. Zero lock-in. |
| Recoverability        | ✅     | Settings export. Photos are standard files. |
| Visibility            | ✅     | Fully open-source. |
| External Dependencies | ✅     | Zero. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

Install from F-Droid. Use as default camera app.

## Related Recipes

- [Mobile Apps](../mobile.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| GrapheneOS built-in camera | A3 / T2 | Basic but privacy-respecting. |

---
## Trajectory
**Direction: stable**
Long-running project. Single developer but consistent updates. Feature-complete for most use cases.
**Signal assessment:**
| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | GPL-3.0, unchanged. |
| Feature gating | ✅ | All features free. |
| Self-hosting | ✅ | Client app. |
| Governance | ⚠️ | Single developer. Bus factor risk. |
**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing
---

## Sources

- **Website:** https://opencamera.org.uk
- **Documentation:** https://opencamera.org.uk/help.html
- **Repository:** https://sourceforge.net/p/opencamera/code
- **Docker image:** —
- **Community:** https://sourceforge.net/p/opencamera/discussion
