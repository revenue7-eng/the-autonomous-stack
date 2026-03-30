---
title: "Neo Store"
category: "mobile/app-store"
status: "stable"
license: "GPL-3.0"
source: "https://github.com/NeoApplications/Neo-Store"
repository: "https://github.com/NeoApplications/Neo-Store"
documentation: "https://github.com/NeoApplications/Neo-Store/wiki"
docker_image: "-"
community: "https://github.com/NeoApplications/Neo-Store/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["External Dependencies"]
---

# Neo Store

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Modern F-Droid client with Material Design 3 UI. Same repositories as F-Droid but with faster, cleaner interface. Background updates, repository management, and better search.

## Architectural Role

Application distribution layer — mobile. Alternative frontend for F-Droid repositories.

## Technical Autonomy

- [x] Works without internet (cached catalog, installed APKs)
- [x] Stores data locally
- [x] Does not require external accounts
- [x] Allows data export (APKs are standard packages)
- [x] Provides offline updates (self-updates from F-Droid repos)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Installed apps keep working. |
| Exit                  | ✅     | Switch to F-Droid client anytime. Same repos. |
| Recoverability        | ✅     | Reinstall from any F-Droid repo. |
| Visibility            | ✅     | Fully open-source. |
| External Dependencies | ✅     | Uses same repos as F-Droid. Can add custom repos. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

Install from F-Droid. Comes pre-configured with default F-Droid repository. Add additional repos as needed.

## Related Recipes

- [Mobile Apps](../mobile.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [F-Droid](f-droid.md) | A3 / T2 | Official client. More established. Slower UI. |
| [Aurora Store](aurora-store.md) | A3 / T2 | For Play Store apps without Google account. |

---
## Trajectory
**Direction: opening**
Active development. Growing as the preferred F-Droid client for users who want a modern UI. Community-driven.
**Signal assessment:**
| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | GPL-3.0. |
| Feature gating | ✅ | All features free. |
| Self-hosting | ✅ | Client app. |
| Governance | ✅ | NeoApplications community. Open development. |
**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing
---

## Sources

- **Website:** https://github.com/NeoApplications/Neo-Store
- **Documentation:** https://github.com/NeoApplications/Neo-Store/wiki
- **Repository:** https://github.com/NeoApplications/Neo-Store
- **Docker image:** —
- **Community:** https://github.com/NeoApplications/Neo-Store/discussions
