---
nav_exclude: true
title: "OsmAnd"
category: "mobile/navigation"
status: "stable"
license: "GPL-3.0"
source: "https://osmand.net"
repository: "https://github.com/osmandapp/OsmAnd"
documentation: "https://osmand.net/docs"
docker_image: "-"
community: "https://github.com/osmandapp/OsmAnd/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["External Dependencies"]
---

# OsmAnd

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Offline maps and navigation based on OpenStreetMap. Detailed maps for hiking, cycling, skiing, nautical. Fully offline — download region maps and navigate without internet. Extremely feature-rich.

## Architectural Role

Client-side application layer — navigation and mapping. Uses OpenStreetMap data. Fully offline-capable.

## Technical Autonomy

- [x] Works without internet (offline maps and navigation)
- [x] Stores data locally (downloaded maps on device)
- [x] Does not require external accounts
- [x] Allows data export (GPX tracks, favorites, OSM format)
- [x] Provides offline updates (F-Droid)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Downloaded maps work forever. |
| Exit                  | ✅     | GPX export. Standard formats. |
| Recoverability        | ✅     | Re-download maps. Export/import profiles. |
| Visibility            | ✅     | Fully open-source. |
| External Dependencies | ✅     | Needs internet only for initial map download. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

Install from F-Droid (free, all features) or Play Store (free version limited to 7 map downloads). Download maps for your region. Navigate offline.

## Related Recipes

- [Mobile Apps](../mobile.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Organic Maps](organic-maps.md) | A3 / T2 | Simpler, faster. Fewer features. Fork of Maps.me. |

---
## Trajectory
**Direction: stable**
Long-running project. Active development. F-Droid version has all features for free. Sustainable via Play Store purchases.
**Signal assessment:**
| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | GPL-3.0, unchanged. |
| Feature gating | ⚠️ | Play Store version has download limits. F-Droid version is unlimited. |
| Self-hosting | ✅ | Client app. Map data is OpenStreetMap (public). |
| Governance | ✅ | OsmAnd B.V. Open development. |
**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing
---

## Sources

- **Website:** https://osmand.net
- **Documentation:** https://osmand.net/docs
- **Repository:** https://github.com/osmandapp/OsmAnd
- **Docker image:** —
- **Community:** https://github.com/osmandapp/OsmAnd/discussions
