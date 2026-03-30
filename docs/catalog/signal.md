---
title: "Signal"
category: "communication/messaging"
status: "stable"
license: "AGPL-3.0"
source: "https://signal.org"
repository: "https://github.com/signalapp"
documentation: "https://support.signal.org"
docker_image: "-"
community: "https://community.signalusers.org"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Exit", "Visibility"]
---

# Signal

> **TAS Score: S3/3 — D4/5** — A3 / T2
> _D4 not D5: requires phone number for registration (Q6 — hidden cost: identity linkage)._

## Brief Description

End-to-end encrypted messenger with voice and video calls. No ads, no trackers, no data collection. The Signal Protocol is the gold standard for messaging encryption — adopted by WhatsApp, Google Messages, and others.

## Architectural Role

Client-side application layer — messaging. Server component is open-source but centralized (run by Signal Foundation). All encryption happens on-device.

## Technical Autonomy

- [x] Works without internet (queues messages, delivers when reconnected)
- [x] Stores data locally (messages never stored on server after delivery)
- [ ] Does not require external accounts (requires phone number)
- [x] Allows data export (local backup with encryption)
- [ ] Provides offline updates (requires Play Store, APK from signal.org, or F-Droid via Molly)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Can stop using without data loss. Messages stay on device. |
| Exit                  | ✅     | Local encrypted backups. Transfer to new device supported. |
| Recoverability        | ✅     | Backup/restore built in. |
| Visibility            | ✅     | Fully open-source — client, server, and protocol. |
| External Dependencies | ⚠️     | Centralized server infrastructure run by Signal Foundation. Cannot self-host. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

No server deployment — Signal is a client application. Install from:
- **Android**: signal.org/android (APK direct download)
- **iOS**: App Store
- **Desktop**: signal.org/download
- **F-Droid**: via Molly (Signal-compatible fork)

## Related Recipes

- [Mobile Apps](../mobile.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [SimpleX Chat](simplex-chat.md) | A3 / T2 | No phone number required. Fully decentralized. |
| [Briar](briar.md) | A3 / T2 | Peer-to-peer over Tor. No servers at all. |
| [Element (Matrix)](../catalog/matrix.md) | A3 / T2 | Federated. Self-hostable server. |

---
## Trajectory
**Direction: stable**
Signal Foundation is a nonprofit. The protocol is widely adopted and audited. No signs of commercial pressure or feature gating. Centralization remains the main philosophical concern.
**Signal assessment:**
| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | AGPL-3.0, unchanged. |
| Feature gating | ✅ | All features free for all users. |
| Self-hosting | ⚠️ | Server is open-source but not designed for self-hosting. |
| Governance | ✅ | Signal Foundation (501c3). Meredith Whittaker as president. |
**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing
---

## Sources

- **Website:** https://signal.org
- **Documentation:** https://support.signal.org
- **Repository:** https://github.com/signalapp
- **Docker image:** —
- **Community:** https://community.signalusers.org
