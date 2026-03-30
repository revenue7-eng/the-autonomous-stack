---
title: "Firefox"
category: "mobile/browser"
status: "stable"
license: "MPL-2.0"
source: "https://www.mozilla.org/firefox"
repository: "https://hg.mozilla.org/mozilla-central"
documentation: "https://support.mozilla.org"
docker_image: "-"
community: "https://connect.mozilla.org"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Visibility", "External Dependencies"]
---

# Firefox

> **TAS Score: S3/3 — D4/5** — A3 / T2
> _D4 not D5: some telemetry enabled by default — opt-out available (Q4)._

## Brief Description

Open-source web browser by Mozilla. Independent rendering engine (Gecko). Enhanced Tracking Protection built in. Supports extensions on Android. The only major browser not based on Chromium.

## Architectural Role

Client-side application layer — web browsing. Independent from Google's Blink/Chromium ecosystem.

## Technical Autonomy

- [ ] Works without internet (browser needs internet for its purpose)
- [x] Stores data locally (bookmarks, history, passwords on-device)
- [x] Does not require external accounts (sync is optional)
- [x] Allows data export (bookmarks, passwords export)
- [x] Provides offline updates (F-Droid via Fennec, APK)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Stop anytime. Data stays local. |
| Exit                  | ✅     | Export bookmarks, passwords. Standard formats. |
| Recoverability        | ✅     | Sync optional. Local profile backup. |
| Visibility            | ✅     | Fully open-source. MPL-2.0. |
| External Dependencies | ⚠️     | Default search deal with Google. Telemetry opt-out. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

Install from F-Droid (Fennec build), Play Store, or mozilla.org.

Recommended hardening:
- Disable telemetry in Settings → Data collection
- Set search engine to DuckDuckGo or SearXNG
- Enable strict Enhanced Tracking Protection

## Related Recipes

- [Mobile Apps](../mobile.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Mull](mull.md) | A3 / T2 | Firefox fork with telemetry removed. Android only. |
| [Brave](brave.md) | A3 / T1 | Chromium-based. Built-in ad blocking. |

---
## Trajectory
**Direction: stable**
Mozilla Foundation is a nonprofit. Market share declining but development active. Google search deal provides funding — a structural tension.
**Signal assessment:**
| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | MPL-2.0, unchanged. |
| Feature gating | ✅ | All features free. |
| Self-hosting | ✅ | Client app. Sync server (Firefox Sync) is self-hostable. |
| Governance | ⚠️ | Mozilla Foundation/Corporation. Google revenue dependency. |
**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing
---

## Sources

- **Website:** https://www.mozilla.org/firefox
- **Documentation:** https://support.mozilla.org
- **Repository:** https://hg.mozilla.org/mozilla-central
- **Docker image:** —
- **Community:** https://connect.mozilla.org
