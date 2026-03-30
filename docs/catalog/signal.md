---
nav_exclude: true
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
> _D4 not D5: requires phone number for registration (D3 — hidden cost: identity linkage)._
>
> _Assessment criteria: [v1.0](assessment-criteria.md). Last verified: 2025-05._

## Brief Description

End-to-end encrypted messenger with voice and video calls. No ads, no trackers, no data collection. The Signal Protocol is the gold standard for messaging encryption — adopted by WhatsApp, Google Messages, and others.

## Architectural Role

Client-side application layer — messaging. Server component is open-source but centralized (run by Signal Foundation). All encryption happens on-device.

---

## Formal Assessment

### S1: Pause

| Test | Result | Evidence |
|------|--------|----------|
| Can you stop the process without a special shutdown procedure? | ✅ Yes | Close the app. No background process required. |
| After stopping, is all data still on disk in a readable state? | ✅ Yes | Messages stored in local encrypted SQLite database. |
| Can you restart and continue where you left off? | ✅ Yes | Reopen app → all messages, contacts, settings intact. |

**S1 = Yes**

### S2: Exit

| Test | Result | Evidence |
|------|--------|----------|
| Is there a documented export mechanism? | ✅ Yes | Android: Settings → Chats → Chat backups. Encrypted local backup file. |
| Does the export include ALL user data? | ⚠️ Partial | Messages and media included. Call history and some metadata not exported. |
| Is the export in a standard, reusable format? | ❌ No | Proprietary encrypted backup format. Only Signal can restore it. |
| Can another tool import the exported data? | ❌ No | No third-party tool can read Signal backups. |

**S2 = Partial** — Export exists but format is proprietary and not all data included.

> **Why A3 and not A2:** The Exit criterion tests whether you can *leave with your data*. Signal's backup allows full migration to a new device running Signal. The data leaves the old device and arrives intact on the new one. The proprietary format is a limitation, but you are not locked into a specific *instance* — you control the backup file. This is a judgment call. A strict interpretation would give A2.

### S3: Recoverability

| Test | Result | Evidence |
|------|--------|----------|
| Does the service support backups? | ✅ Yes | Built-in encrypted backup to local storage. |
| Can you restore from backup to a working state? | ✅ Yes | New device → install Signal → restore from backup file. |
| Does a restore give you back the SAME state? | ⚠️ Partial | Messages and media restored. Session keys regenerated (expected for E2E). Some call metadata lost. |

**S3 = Yes** (session key regeneration is inherent to E2E encryption, not a limitation)

### Autonomy Level

| S1 | S2 | S3 | Level |
|----|----|----|-------|
| Yes | Partial | Yes | **A3** (see judgment note on S2) |

### Transparency Level

| Test | Result | Evidence |
|------|--------|----------|
| Source code publicly available? | ✅ Yes | Client: github.com/signalapp/Signal-Android, Signal-iOS, Signal-Desktop. Server: github.com/signalapp/Signal-Server |
| License OSI-approved? | ✅ Yes | AGPL-3.0 (client and server) |

**T = T2**

### Diagnostic Score

| # | Question | Result | Evidence |
|---|----------|--------|----------|
| D1 | Personalisation | ✅ Clean | No analytics, no recommendation engine, no behavioural tracking. Sealed sender prevents server-side metadata collection. |
| D2 | Urgency | ✅ Clean | No push notifications by default beyond message delivery. No countdown timers. No forced updates. |
| D3 | Hidden cost | ⚠️ Concern | **Requires phone number for registration.** This links your identity to telecom infrastructure. You cannot use Signal pseudonymously without a phone number. |
| D4 | Transparency fragility | ✅ Clean | Business model is donation-funded nonprofit. No dark patterns. ToS is straightforward. |
| D5 | Trajectory | ✅ Clean | AGPL-3.0 unchanged. All features free. No feature gating. Signal Foundation (501c3) governed by nonprofit board. |

**D-score: D4/5** (1 concern: D3)

---

## Counterarguments

| Claim | Challenge | Resolution |
|-------|-----------|------------|
| **A3: fully autonomous** | Requires phone number → identity dependency on telecom | Phone number is for registration only. Does not affect Pause/Exit/Recovery. Captured as D3 concern. |
| **A3: fully autonomous** | Cannot self-host the server → centralized infrastructure | Server code is open-source and auditable. Messages are E2E encrypted — server sees only encrypted blobs. Self-hosting is theoretically possible but not supported. Dependency is on Signal Foundation's uptime, not their access to your data. |
| **A3: fully autonomous** | Backup format is proprietary → Exit is not fully portable | Acknowledged in S2 assessment. You can leave with your data, but only to another Signal instance. This is the weakest point of the A3 rating. |
| **T2: open source** | Server federation not supported → you can't run your own Signal network | T2 measures code visibility, not operational independence. Code is public and auditable. Operational centralization is captured in A-level assessment. |
| **D4: clean trajectory** | Signal Foundation received $50M from Brian Acton → funding dependency? | Acton's donation was one-time with no governance strings. Foundation is self-sustaining through donations. No evidence of commercial pressure. |

---

## Configuration (Minimal)

No server deployment — Signal is a client application. Install from:
- **Android**: signal.org/android (APK direct download)
- **iOS**: App Store
- **Desktop**: signal.org/download
- **F-Droid**: via Molly (Signal-compatible fork)

## Related Recipes

- [GrapheneOS Mobile Stack](../recipes/grapheneos-mobile.md)
- [Mobile Apps](../mobile.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [SimpleX Chat](simplex-chat.md) | A3 / T2 | No phone number required. Fully decentralized. Resolves D3 concern. |
| [Briar](briar.md) | A3 / T2 | Peer-to-peer over Tor. No servers at all. But no data export (S2 = No). |
| [Element (Matrix)](matrix.md) | A3 / T2 | Federated. Self-hostable server. Resolves centralization concern. |

---

## Trajectory

**Direction: stable**

Signal Foundation is a nonprofit. The protocol is widely adopted and audited. No signs of commercial pressure or feature gating. Centralization remains the main philosophical concern.

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | AGPL-3.0, unchanged since project inception. |
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
