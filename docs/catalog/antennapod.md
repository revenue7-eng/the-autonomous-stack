---
title: "AntennaPod"
category: "applications/media"
status: "stable"
license: "GPL-3.0"
source: "https://antennapod.org"
repository: "https://github.com/AntennaPod/AntennaPod"
documentation: "https://antennapod.org/documentation"
docker_image: "-"
community: "https://forum.antennapod.org"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Exit", "External Dependencies"]
---

# AntennaPod

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Open-source podcast player for Android. No tracking, no account, no ads. Subscribe to any RSS feed. Download episodes for offline listening. Import/export OPML.

## Architectural Role

Client-side application layer — podcast playback. Uses standard RSS/Atom feeds. No proprietary backend.

## Technical Autonomy

- [x] Works without internet (downloaded episodes play offline)
- [x] Stores data locally (subscriptions, episodes on-device)
- [x] Does not require external accounts
- [x] Allows data export (OPML export of all subscriptions)
- [x] Provides offline updates (F-Droid)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Stop anytime. Downloads persist. |
| Exit                  | ✅     | OPML export. Switch to any other podcast app. |
| Recoverability        | ✅     | OPML import. Database backup. |
| Visibility            | ✅     | Fully open-source. |
| External Dependencies | ✅     | Standard RSS. Works with any podcast feed. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

Install from F-Droid. Search for podcasts or add RSS feed URLs. Download episodes for offline listening.

## Related Recipes

- [Mobile Apps](../mobile.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| No direct equivalent in catalog. Spotify Podcasts (A0/T0) is what most people use. |

---
## Trajectory
**Direction: stable**
Mature project. Active community. Regular releases. Well-established in the F-Droid ecosystem.
**Signal assessment:**
| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | GPL-3.0, unchanged. |
| Feature gating | ✅ | All features free. |
| Self-hosting | ✅ | Client app. |
| Governance | ✅ | Community-governed. Multiple maintainers. |
**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing
---

## Sources

- **Website:** https://antennapod.org
- **Documentation:** https://antennapod.org/documentation
- **Repository:** https://github.com/AntennaPod/AntennaPod
- **Docker image:** —
- **Community:** https://forum.antennapod.org
