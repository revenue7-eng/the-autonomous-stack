---
title: "Organic Maps"
category: "mobile/navigation"
status: "stable"
license: "Apache-2.0"
source: "https://organicmaps.app"
repository: "https://github.com/organicmaps/organicmaps"
documentation: "https://organicmaps.app/faq"
docker_image: "-"
community: "https://github.com/organicmaps/organicmaps/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["External Dependencies"]
---

# Organic Maps

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Fast, lightweight offline maps. Fork of Maps.me without ads, tracking, or data collection. Clean interface, quick map downloads. Ideal for walking, cycling, and hiking.

## Architectural Role

Client-side application layer — navigation and mapping. OpenStreetMap data. Fully offline.

## Technical Autonomy

- [x] Works without internet (offline maps and routing)
- [x] Stores data locally (maps on device)
- [x] Does not require external accounts
- [x] Allows data export (KML/KMZ bookmarks)
- [x] Provides offline updates (F-Droid)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Maps work forever offline. |
| Exit                  | ✅     | KML export. Standard formats. |
| Recoverability        | ✅     | Re-download maps anytime. |
| Visibility            | ✅     | Fully open-source. |
| External Dependencies | ✅     | Internet only for map downloads. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

Install from F-Droid, App Store, or Play Store. Download maps. Navigate.

## Related Recipes

- [Mobile Apps](../mobile.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [OsmAnd](osmand.md) | A3 / T2 | More features (hiking profiles, nautical). Steeper learning curve. |

---
## Trajectory
**Direction: opening**
Active development. Growing community. Clean fork of Maps.me with ethical foundation. No ads, no tracking. Funded by donations.
**Signal assessment:**
| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | Apache-2.0, unchanged. |
| Feature gating | ✅ | All features free on all platforms. |
| Self-hosting | ✅ | Client app. |
| Governance | ✅ | Community-governed. Multiple core contributors. |
**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing
---

## Sources

- **Website:** https://organicmaps.app
- **Documentation:** https://organicmaps.app/faq
- **Repository:** https://github.com/organicmaps/organicmaps
- **Docker image:** —
- **Community:** https://github.com/organicmaps/organicmaps/discussions
