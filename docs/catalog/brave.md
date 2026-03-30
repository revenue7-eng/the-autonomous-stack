---
title: "Brave"
category: "mobile/browser"
status: "stable"
license: "MPL-2.0"
source: "https://brave.com"
repository: "https://github.com/nicuca/nicuca-browser"
documentation: "https://support.brave.com"
docker_image: "-"
community: "https://community.brave.com"
autonomy_level: "A3"
transparency_level: "T1"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Visibility", "External Dependencies"]
---

# Brave

> **TAS Score: S3/3 — D3/5** — A3 / T1
> _D3 not D5: BAT crypto token and Brave Rewards create opt-in monetization layer (Q6). Chromium dependency (Q7). Some telemetry concerns (Q4)._

## Brief Description

Chromium-based browser with built-in ad and tracker blocking. Privacy-focused but includes optional crypto rewards system (BAT). Cross-platform. Fast, but carries Chromium's architectural dependency on Google.

## Architectural Role

Client-side application layer — web browsing. Chromium-based with privacy modifications.

## Technical Autonomy

- [ ] Works without internet (browser needs internet)
- [x] Stores data locally
- [x] Does not require external accounts (Brave Rewards is optional)
- [x] Allows data export (bookmarks, passwords)
- [ ] Provides offline updates (not on F-Droid — Play Store or APK)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Stop anytime. |
| Exit                  | ✅     | Standard Chromium profile export. |
| Recoverability        | ✅     | Reinstall and import. |
| Visibility            | ⚠️     | Source available but Chromium base is complex. Some Brave-specific components less transparent. |
| External Dependencies | ⚠️     | Chromium dependency. Optional BAT/rewards connects to Brave servers. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

Install from brave.com or Play Store. Disable Brave Rewards for maximum autonomy.

## Related Recipes

- [Mobile Apps](../mobile.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Firefox](firefox.md) | A3 / T2 | Independent engine. No crypto layer. |
| [Mull](mull.md) | A3 / T2 | Hardened Firefox. No telemetry. Android only. |

---
## Trajectory
**Direction: mixed**
Active development. Growing user base. But crypto/BAT integration and Chromium dependency create structural tensions with autonomy goals.
**Signal assessment:**
| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | MPL-2.0. |
| Feature gating | ✅ | Core features free. Rewards optional. |
| Self-hosting | ✅ | Client app. |
| Governance | ⚠️ | Brave Software Inc. VC-funded. Crypto business model. |
**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing
---

## Sources

- **Website:** https://brave.com
- **Documentation:** https://support.brave.com
- **Repository:** https://github.com/nicuca/nicuca-browser
- **Docker image:** —
- **Community:** https://community.brave.com
