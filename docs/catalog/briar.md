---
nav_exclude: true
title: "Briar"
category: "communication/messaging"
status: "stable"
license: "GPL-3.0"
source: "https://briarproject.org"
repository: "https://code.briarproject.org/briar/briar"
documentation: "https://briarproject.org/manual"
docker_image: "-"
community: "https://briarproject.org/get-involved"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["External Dependencies"]
---

# Briar

> **TAS Score: S3/3 — D4/5** — A3 / T2
> _D4 not D5: Android only, limiting platform reach (Q8 — trajectory concern)._

## Brief Description

Peer-to-peer encrypted messenger that works over Tor, Wi-Fi, or Bluetooth. No servers at all — messages sync directly between devices. Designed for journalists, activists, and anyone who needs communication that survives infrastructure outages.

## Architectural Role

Client-side application layer — messaging. Fully peer-to-peer. No server component. Can operate without internet via local Wi-Fi or Bluetooth.

## Technical Autonomy

- [x] Works without internet (Bluetooth, Wi-Fi direct)
- [x] Stores data locally (on-device only)
- [x] Does not require external accounts (no identifiers)
- [ ] Allows data export (no export feature — by design for security)
- [x] Provides offline updates (F-Droid, APK)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Stop anytime. No server to maintain. |
| Exit                  | ⚠️     | No data export — messages exist only on device. Security feature, not a limitation. |
| Recoverability        | ⚠️     | No backup/restore. Lose device = lose messages. |
| Visibility            | ✅     | Fully open-source. Audited. |
| External Dependencies | ✅     | Zero. Works without internet entirely. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

No server deployment. Install from:
- **Android**: F-Droid or briarproject.org
- **iOS**: not available
- **Desktop**: Briar Desktop (beta, Linux/Windows/macOS)

## Related Recipes

- [Mobile Apps](../mobile.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [SimpleX Chat](simplex-chat.md) | A3 / T2 | Cross-platform. Uses relay servers (self-hostable). |
| [Signal](signal.md) | A3 / T2 | More features. Requires phone number and internet. |

---

## Trajectory

**Direction: stable**

Mature project backed by academic research. Desktop client expanding platform reach. Development pace is slow but steady.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | GPL-3.0, unchanged. |
| Feature gating | ✅ | All features free. |
| Self-hosting | ✅ | Nothing to host — fully P2P. |
| Governance | ✅ | Briar Project, community-governed. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** https://briarproject.org
- **Documentation:** https://briarproject.org/manual
- **Repository:** https://code.briarproject.org/briar/briar
- **Docker image:** —
- **Community:** https://briarproject.org/get-involved
