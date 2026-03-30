---
nav_exclude: true
title: "NewPipe"
category: "media/video"
status: "stable"
license: "GPL-3.0"
source: "https://newpipe.net"
repository: "https://github.com/TeamNewPipe/NewPipe"
documentation: "https://github.com/TeamNewPipe/NewPipe/wiki"
docker_image: "-"
community: "https://github.com/TeamNewPipe/NewPipe/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["External Dependencies"]
---

# NewPipe

> **TAS Score: S3/3 — D4/5** — A3 / T2
> _D4 not D5: depends on YouTube/PeerTube/SoundCloud APIs which can break without notice (Q7 — transparency fragility)._

## Brief Description

Lightweight YouTube frontend for Android. No ads, no tracking, no Google account required. Background playback, downloads, subscriptions — all without Google Play Services. Also supports PeerTube, SoundCloud, Bandcamp, and media.ccc.de.

## Architectural Role

Client-side application layer — media streaming. Scrapes public APIs without authentication.

## Technical Autonomy

- [ ] Works without internet (streaming requires internet, but downloaded content works offline)
- [x] Stores data locally (subscriptions, history, downloads on-device)
- [x] Does not require external accounts (no login at all)
- [x] Allows data export (subscriptions as JSON, downloaded media files)
- [x] Provides offline updates (F-Droid)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Stop anytime. Downloaded content persists. |
| Exit                  | ✅     | Export subscriptions. Downloaded files are standard media. |
| Recoverability        | ✅     | Import subscriptions. Reinstall from F-Droid. |
| Visibility            | ✅     | Fully open-source. |
| External Dependencies | ⚠️     | Depends on YouTube's public-facing API. Google can break it. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

Install from F-Droid. Open and use — no account or setup needed.

## Related Recipes

- [Mobile Apps](../mobile.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Piped](../catalog/piped.md) | A3 / T2 | Web-based YouTube frontend. Self-hostable. |

---

## Trajectory

**Direction: stable**

Active development. Occasional breakage when YouTube changes its API — typically fixed within days. Large contributor community.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | GPL-3.0, unchanged. |
| Feature gating | ✅ | All features free. |
| Self-hosting | ✅ | Client app. |
| Governance | ✅ | TeamNewPipe. Community-governed. Multiple contributors. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** https://newpipe.net
- **Documentation:** https://github.com/TeamNewPipe/NewPipe/wiki
- **Repository:** https://github.com/TeamNewPipe/NewPipe
- **Docker image:** —
- **Community:** https://github.com/TeamNewPipe/NewPipe/discussions
