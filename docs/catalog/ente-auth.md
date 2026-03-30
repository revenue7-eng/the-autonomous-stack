---
nav_exclude: true
title: "ente Auth"
category: "security/2fa"
status: "stable"
license: "AGPL-3.0"
source: "https://ente.io/auth"
repository: "https://github.com/ente-io/ente/tree/main/auth"
documentation: "https://help.ente.io"
docker_image: "-"
community: "https://ente.io/community"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Recoverability", "Exit"]
---

# ente Auth

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Cross-platform 2FA authenticator with end-to-end encrypted cloud backup. Works on Android, iOS, desktop, and web. By the same team as Ente Photos. Never lose your 2FA codes again — encrypted sync across all devices.

## Architectural Role

Client-side security layer — two-factor authentication. E2E encrypted cloud sync optional.

## Technical Autonomy

- [x] Works without internet (TOTP generates offline)
- [x] Stores data locally (on-device)
- [x] Does not require external accounts (works offline-only, sync optional)
- [x] Allows data export (plain text, encrypted backup)
- [x] Provides offline updates (F-Droid, GitHub APK)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Codes work offline forever. |
| Exit                  | ✅     | Export in standard formats. |
| Recoverability        | ✅     | E2E encrypted cloud backup. Recovery key. |
| Visibility            | ✅     | Fully open-source. Part of Ente monorepo. |
| External Dependencies | ✅     | Cloud sync optional. Works fully offline. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

Install from F-Droid, App Store, or GitHub. Use standalone or create Ente account for encrypted sync.

## Related Recipes

- [Mobile Apps](../mobile.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Aegis](aegis.md) | A3 / T2 | Android only. No cloud sync. Encrypted local vault. |

---

## Trajectory

**Direction: opening**

Part of the Ente ecosystem. Active development. Cross-platform advantage over Aegis. Sustainable business model via Ente Photos subscriptions.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | AGPL-3.0. |
| Feature gating | ✅ | All features free. |
| Self-hosting | ✅ | Server is self-hostable (shared with Ente Photos). |
| Governance | ✅ | Ente Technologies. Open development. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** https://ente.io/auth
- **Documentation:** https://help.ente.io
- **Repository:** https://github.com/ente-io/ente/tree/main/auth
- **Docker image:** —
- **Community:** https://ente.io/community
