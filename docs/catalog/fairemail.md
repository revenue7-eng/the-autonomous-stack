---
title: "FairEmail"
category: "communication/email"
status: "stable"
license: "GPL-3.0"
source: "https://email.faircode.eu"
repository: "https://github.com/M66B/FairEmail"
documentation: "https://github.com/M66B/FairEmail/blob/master/FAQ.md"
docker_image: "-"
community: "https://forum.xda-developers.com/t/app-5-0-fairemail-fully-featured-open-source-privacy-oriented-email-app.3stripping824168/"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Exit", "External Dependencies"]
---

# FairEmail

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Full-featured Android email client. No tracking, no ads, no cloud dependency. Works with any IMAP/POP3 provider. Privacy-focused with built-in encryption support (PGP, S/MIME).

## Architectural Role

Client-side application layer — email. Connects to any standard email server. No proprietary backend.

## Technical Autonomy

- [x] Works without internet (cached emails available offline)
- [x] Stores data locally (on-device database)
- [x] Does not require external accounts (works with any email provider)
- [x] Allows data export (standard email protocols — messages stay on server)
- [x] Provides offline updates (F-Droid, GitHub APK)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Stop using anytime. Emails remain on your server. |
| Exit                  | ✅     | Standard IMAP — switch clients freely. |
| Recoverability        | ✅     | Settings export/import. Emails on server. |
| Visibility            | ✅     | Fully open-source. |
| External Dependencies | ✅     | Works with any email provider. No proprietary dependency. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

No server deployment — Android email client. Install from:
- **F-Droid**: available
- **GitHub**: APK releases
- **Play Store**: available (pro features via purchase)

## Related Recipes

- [Mobile Apps](../mobile.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [K-9 Mail / Thunderbird](k9-mail.md) | A3 / T2 | Now part of Thunderbird. Similar philosophy. |
| [Tuta](tuta.md) | A2 / T2 | E2E encrypted but tied to Tuta servers. |

---
## Trajectory
**Direction: stable**
Maintained by single developer (M66B). Very active development. Some concern about bus factor, but codebase is clean and well-documented.
**Signal assessment:**
| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | GPL-3.0, unchanged. |
| Feature gating | ⚠️ | Some pro features require Play Store purchase, but F-Droid version is fully functional. |
| Self-hosting | ✅ | Client app — nothing to host. |
| Governance | ⚠️ | Single maintainer. Bus factor risk. |
**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing
---

## Sources

- **Website:** https://email.faircode.eu
- **Documentation:** https://github.com/M66B/FairEmail/blob/master/FAQ.md
- **Repository:** https://github.com/M66B/FairEmail
- **Docker image:** —
- **Community:** XDA Developers forum
