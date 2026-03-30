---
title: "Aegis Authenticator"
category: "security/2fa"
status: "stable"
license: "GPL-3.0"
source: "https://getaegis.app"
repository: "https://github.com/beemdevelopment/Aegis"
documentation: "https://github.com/beemdevelopment/Aegis/wiki"
docker_image: "-"
community: "https://github.com/beemdevelopment/Aegis/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Recoverability", "Exit"]
---

# Aegis Authenticator

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Open-source 2FA authenticator for Android. Encrypted vault with biometric unlock. Supports TOTP and HOTP. Import from Google Authenticator, Authy, and others. Encrypted backups.

## Architectural Role

Client-side security layer — two-factor authentication. Purely local, no cloud component.

## Technical Autonomy

- [x] Works without internet (TOTP is offline by design)
- [x] Stores data locally (encrypted vault on device)
- [x] Does not require external accounts
- [x] Allows data export (encrypted/plain JSON, Google Authenticator format)
- [x] Provides offline updates (F-Droid)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Codes generate offline forever. |
| Exit                  | ✅     | Full export in multiple formats. |
| Recoverability        | ✅     | Encrypted backup/restore. |
| Visibility            | ✅     | Fully open-source. |
| External Dependencies | ✅     | Zero. Completely offline. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

Install from F-Droid. Set up vault password. Import existing 2FA codes or scan new QR codes. Enable automatic encrypted backups.

## Related Recipes

- [Mobile Apps](../mobile.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [ente Auth](ente-auth.md) | A3 / T2 | Cross-platform with E2E encrypted cloud backup. |

---
## Trajectory
**Direction: stable**
Mature, well-maintained. Android only (no iOS). Active development with regular releases.
**Signal assessment:**
| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | GPL-3.0, unchanged. |
| Feature gating | ✅ | All features free. |
| Self-hosting | ✅ | Nothing to host. |
| Governance | ✅ | Beem Development. Open community. |
**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing
---

## Sources

- **Website:** https://getaegis.app
- **Documentation:** https://github.com/beemdevelopment/Aegis/wiki
- **Repository:** https://github.com/beemdevelopment/Aegis
- **Docker image:** —
- **Community:** https://github.com/beemdevelopment/Aegis/discussions
