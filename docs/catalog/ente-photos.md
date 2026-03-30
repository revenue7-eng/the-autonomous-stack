---
nav_exclude: true
title: "Ente Photos"
category: "media/photos"
status: "stable"
license: "AGPL-3.0"
source: "https://ente.io"
repository: "https://github.com/ente-io/ente"
documentation: "https://help.ente.io"
docker_image: "-"
community: "https://ente.io/community"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
---

# Ente Photos

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

End-to-end encrypted photo storage and backup. Cross-platform (Android, iOS, web, desktop). Self-hostable server — or use Ente's hosted service with zero-knowledge encryption. Family plans available.

## Architectural Role

Application layer — photo management. Can be self-hosted or used as a service with E2E encryption.

## Technical Autonomy

- [x] Works without internet (cached photos available offline)
- [x] Stores data locally (on-device + encrypted cloud backup)
- [x] Does not require external accounts (self-host option)
- [x] Allows data export (bulk export, standard formats)
- [x] Provides offline updates (F-Droid, GitHub APK)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Photos stay on device and in encrypted backup. |
| Exit                  | ✅     | Full export in original formats. CLI export tool. |
| Recoverability        | ✅     | E2E encrypted backups. Recovery key system. |
| Visibility            | ✅     | Fully open-source. Server and clients. |
| External Dependencies | ✅     | Self-hostable. Or hosted with E2E — they can't see your photos. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

Client: install from F-Droid, App Store, or GitHub releases.

Self-hosted server: see https://github.com/ente-io/ente/tree/main/server

## Related Recipes

- [Mobile Apps](../mobile.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Immich](immich.md) | A3 / T2 | More Google Photos-like. Requires self-hosting. |
| [Simple Gallery](simple-gallery.md) | A3 / T2 | Offline only. No cloud backup. |

---

## Trajectory

**Direction: opening**

Fully open-sourced server in 2024. Active development. Sustainable business model (paid hosted plans fund open-source development). Growing community.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | AGPL-3.0, all components. |
| Feature gating | ✅ | Self-hosted has all features. |
| Self-hosting | ✅ | Server fully open-source and self-hostable. |
| Governance | ✅ | Ente Technologies. Open development. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** https://ente.io
- **Documentation:** https://help.ente.io
- **Repository:** https://github.com/ente-io/ente
- **Docker image:** —
- **Community:** https://ente.io/community
