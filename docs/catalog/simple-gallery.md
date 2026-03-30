---
title: "Simple Gallery"
category: "applications/photos"
status: "stable"
license: "GPL-3.0"
source: "https://github.com/SimpleMobileTools/Simple-Gallery"
repository: "https://github.com/SimpleMobileTools/Simple-Gallery"
documentation: "-"
docker_image: "-"
community: "https://github.com/SimpleMobileTools/Simple-Gallery/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["External Dependencies"]
---

# Simple Gallery

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Offline photo and video gallery for Android. No cloud, no tracking, no internet permission. Just view, organize, and edit your local media files. Part of the Simple Mobile Tools suite (now forked as Fossify after acquisition).

## Architectural Role

Client-side application layer — media viewer. Purely local, no network component.

## Technical Autonomy

- [x] Works without internet (no network access at all)
- [x] Stores data locally (views device storage only)
- [x] Does not require external accounts
- [x] Allows data export (standard file formats on device)
- [x] Provides offline updates (F-Droid)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Nothing to pause — purely local. |
| Exit                  | ✅     | Photos are standard files. No app lock-in. |
| Recoverability        | ✅     | Nothing stored in app — reads filesystem. |
| Visibility            | ✅     | Fully open-source. |
| External Dependencies | ✅     | Zero network dependencies. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

Install from F-Droid (search "Fossify Gallery" — the maintained fork).

## Related Recipes

- [Mobile Apps](../mobile.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Ente Photos](ente-photos.md) | A3 / T2 | Adds encrypted cloud backup. |
| [Immich](immich.md) | A3 / T2 | Google Photos replacement with server. |

---
## Trajectory
**Direction: mixed**
Original Simple Mobile Tools was acquired by ZipoApps in 2023. Community forked to Fossify. The Fossify fork is actively maintained under GPL-3.0.
**Signal assessment:**
| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | GPL-3.0. Fork preserved the license. |
| Feature gating | ✅ | All features free. |
| Self-hosting | ✅ | Client app — nothing to host. |
| Governance | ⚠️ | Original sold; Fossify fork is community-governed. Use Fossify. |
**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing
---

## Sources

- **Website:** https://github.com/FossifyOrg/Gallery
- **Repository:** https://github.com/FossifyOrg/Gallery
- **Docker image:** —
- **Community:** https://github.com/FossifyOrg/Gallery/discussions
