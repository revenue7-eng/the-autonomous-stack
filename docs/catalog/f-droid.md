---
nav_exclude: true
title: "F-Droid"
category: "mobile/app-store"
status: "stable"
license: "GPL-3.0"
source: "https://f-droid.org"
repository: "https://gitlab.com/fdroid"
documentation: "https://f-droid.org/docs"
docker_image: "-"
community: "https://forum.f-droid.org"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["External Dependencies", "Visibility"]
---

# F-Droid

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Catalogue of free and open-source Android applications. All apps are built from source by F-Droid's build infrastructure. No tracking, no accounts, no proprietary dependencies. The gateway to autonomous mobile.

## Architectural Role

Application distribution layer — mobile. Replaces Google Play Store. Can host custom repositories.

## Technical Autonomy

- [x] Works without internet (cached catalog, downloaded APKs)
- [x] Stores data locally (no cloud sync)
- [x] Does not require external accounts (no login needed)
- [x] Allows data export (APK files are standard Android packages)
- [x] Provides offline updates (repos can be mirrored locally)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Installed apps keep working without F-Droid. |
| Exit                  | ✅     | Apps are standard APKs. Switch to manual installs anytime. |
| Recoverability        | ✅     | Reinstall from any mirror. |
| Visibility            | ✅     | All apps built from source. Build metadata public. |
| External Dependencies | ✅     | Can self-host repos. Multiple mirrors available. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

Install from https://f-droid.org — download APK directly. No server needed.

For self-hosted F-Droid repository:
```bash
pip install fdroidserver
fdroid init
fdroid update
# Serve the repo directory via any web server
```

## Related Recipes

- [Mobile Apps](../mobile.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Neo Store](neo-store.md) | A3 / T2 | Modern F-Droid client. Same repos, better UX. |
| [Aurora Store](aurora-store.md) | A3 / T2 | Access Play Store without Google account. |

---

## Trajectory

**Direction: stable**

Long-running project. Reproducible builds initiative. Growing catalog. Client app UX improvements ongoing.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | GPL-3.0, unchanged. |
| Feature gating | ✅ | Everything free. |
| Self-hosting | ✅ | fdroidserver makes custom repos easy. |
| Governance | ✅ | F-Droid Limited (nonprofit). Community-governed. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** https://f-droid.org
- **Documentation:** https://f-droid.org/docs
- **Repository:** https://gitlab.com/fdroid
- **Docker image:** —
- **Community:** https://forum.f-droid.org
