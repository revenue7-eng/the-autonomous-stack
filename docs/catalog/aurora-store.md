---
nav_exclude: true
title: "Aurora Store"
category: "mobile/app-store"
status: "stable"
license: "GPL-3.0"
source: "https://auroraoss.com"
repository: "https://gitlab.com/AuroraOSS/AuroraStore"
documentation: "https://gitlab.com/AuroraOSS/AuroraStore/-/wikis/home"
docker_image: "-"
community: "https://t.me/AuroraSupport"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["External Dependencies"]
---

# Aurora Store

> **TAS Score: S3/3 — D3/5** — A3 / T2
> _D3 not D5: depends on Google Play infrastructure for app delivery (Q7 — transparency fragility). Anonymous accounts shared and may break (Q6)._

## Brief Description

Open-source client for Google Play Store. Download apps without a Google account using anonymous shared credentials. Useful for apps not available on F-Droid.

## Architectural Role

Application distribution layer — mobile. Bridge between Google Play ecosystem and de-Googled devices.

## Technical Autonomy

- [ ] Works without internet (requires Google servers for downloads)
- [x] Stores data locally (downloaded APKs are standard)
- [x] Does not require external accounts (anonymous login available)
- [x] Allows data export (APKs are standard Android packages)
- [x] Provides offline updates (F-Droid)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Installed apps work without Aurora Store. |
| Exit                  | ✅     | Apps are standard APKs. |
| Recoverability        | ✅     | Reinstall from F-Droid. |
| Visibility            | ✅     | Open-source client. |
| External Dependencies | ❌     | Depends entirely on Google Play infrastructure. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

Install from F-Droid. Open, choose anonymous login, search and install apps.

## Related Recipes

- [Mobile Apps](../mobile.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [F-Droid](f-droid.md) | A3 / T2 | Open-source apps only. No Google dependency. |
| [Neo Store](neo-store.md) | A3 / T2 | Modern F-Droid client. |

---

## Trajectory

**Direction: stable**

Active development. Anonymous login may break periodically due to Google's anti-abuse measures. Necessary bridge tool for the foreseeable future.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | GPL-3.0, unchanged. |
| Feature gating | ✅ | All features free. |
| Self-hosting | ✅ | Client app — nothing to host. |
| Governance | ➖ | Small team. Community contributions. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** https://auroraoss.com
- **Documentation:** https://gitlab.com/AuroraOSS/AuroraStore/-/wikis/home
- **Repository:** https://gitlab.com/AuroraOSS/AuroraStore
- **Docker image:** —
- **Community:** https://t.me/AuroraSupport
