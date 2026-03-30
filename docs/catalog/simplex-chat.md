---
nav_exclude: true
title: "SimpleX Chat"
category: "communication/messaging"
status: "stable"
license: "AGPL-3.0"
source: "https://simplex.chat"
repository: "https://github.com/simplex-chat/simplex-chat"
documentation: "https://simplex.chat/docs"
docker_image: "simplexchat/smp-server"
community: "https://simplex.chat/contact"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Exit", "External Dependencies"]
---

# SimpleX Chat

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Decentralized messenger with no user identifiers — no phone number, no username, no account. Uses double-ratchet encryption with pairwise connections. Self-hostable relay servers. The most private messaging option available.

## Architectural Role

Client-side application layer — messaging. Relay servers (SMP) are stateless and self-hostable. No central directory or identity system.

## Technical Autonomy

- [x] Works without internet (queues locally, delivers when reconnected)
- [x] Stores data locally (all messages stored on-device only)
- [x] Does not require external accounts (no identifiers at all)
- [x] Allows data export (database export/import)
- [x] Provides offline updates (APK available, F-Droid repo)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Stop anytime. Messages stay on device. |
| Exit                  | ✅     | Export database. Migrate to new device. |
| Recoverability        | ✅     | Local database backup. |
| Visibility            | ✅     | Fully open-source. Protocol documented and audited. |
| External Dependencies | ✅     | Can run own SMP/XFTP servers. No central dependency. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

Client: install from F-Droid, GitHub releases, or simplex.chat.

Self-hosted relay server:
```yaml
services:
  smp-server:
    image: simplexchat/smp-server:latest
    ports:
      - "5223:5223"
    volumes:
      - ./config:/etc/opt/simplex
      - ./logs:/var/opt/simplex
```

## Related Recipes

- [Mobile Apps](../mobile.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Signal](signal.md) | A3 / T2 | More mainstream. Requires phone number. Centralized servers. |
| [Briar](briar.md) | A3 / T2 | P2P over Tor. No servers at all, but Android only. |
| [Element (Matrix)](matrix.md) | A3 / T2 | Federated. Richer features (rooms, bridges). |

---

## Trajectory

**Direction: opening**

Active development, growing user base. Trail of Bits audit completed. Adding group features and file transfer. Fully funded without VC pressure.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | AGPL-3.0, unchanged. |
| Feature gating | ✅ | All features free. |
| Self-hosting | ✅ | SMP/XFTP servers easy to self-host. |
| Governance | ✅ | SimpleX Chat Ltd, open development. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** https://simplex.chat
- **Documentation:** https://simplex.chat/docs
- **Repository:** https://github.com/simplex-chat/simplex-chat
- **Docker image:** simplexchat/smp-server
- **Community:** https://simplex.chat/contact
