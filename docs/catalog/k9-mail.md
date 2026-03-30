---
nav_exclude: true
title: "K-9 Mail / Thunderbird"
category: "communication/email"
status: "stable"
license: "Apache-2.0"
source: "https://k9mail.app"
repository: "https://github.com/thunderbird/thunderbird-android"
documentation: "https://docs.k9mail.app"
docker_image: "-"
community: "https://github.com/thunderbird/thunderbird-android/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Exit"]
---

# K-9 Mail / Thunderbird

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Open-source Android email client, now part of the Thunderbird project (Mozilla). Works with any IMAP/POP3/Exchange provider. Being rebranded as Thunderbird for Android.

## Architectural Role

Client-side application layer — email. Standard protocol client, no proprietary backend.

## Technical Autonomy

- [x] Works without internet (cached emails offline)
- [x] Stores data locally (on-device)
- [x] Does not require external accounts (any email provider)
- [x] Allows data export (standard IMAP — switch freely)
- [x] Provides offline updates (F-Droid, GitHub APK)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Stop anytime. Emails stay on server. |
| Exit                  | ✅     | Standard protocols. Zero lock-in. |
| Recoverability        | ✅     | Settings export. Emails on server. |
| Visibility            | ✅     | Fully open-source. Part of Mozilla/MZLA. |
| External Dependencies | ✅     | Any email provider. No proprietary dependency. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

Android email client. Install from:
- **F-Droid**: available
- **Play Store**: available (free)
- **GitHub**: APK releases

## Related Recipes

- [Mobile Apps](../mobile.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [FairEmail](fairemail.md) | A3 / T2 | More privacy features. Single maintainer. |
| [Tuta](tuta.md) | A2 / T2 | E2E encrypted but provider-locked. |

---
## Trajectory
**Direction: opening**
Acquired by Thunderbird/MZLA. Rebranding to Thunderbird for Android underway. More resources, larger team, active development. Strong trajectory.
**Signal assessment:**
| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | Apache-2.0, unchanged. |
| Feature gating | ✅ | All features free. |
| Self-hosting | ✅ | Client app — nothing to host. |
| Governance | ✅ | MZLA Technologies (Mozilla subsidiary). |
**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing
---

## Sources

- **Website:** https://k9mail.app
- **Documentation:** https://docs.k9mail.app
- **Repository:** https://github.com/thunderbird/thunderbird-android
- **Docker image:** —
- **Community:** https://github.com/thunderbird/thunderbird-android/discussions
