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
autonomy_level: "A2"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Exit", "Visibility"]
---

# Signal

> **TAS Score: S2/3 — D4/5** — A2 / T2
> _S2 not S3: Exit = Partial-E1 (proprietary backup format). D4 not D5: phone number required (D3)._
>
> _Assessment criteria: [v1.1](assessment-criteria.md). Context: mobile app · single-user · Android._

## Brief Description

End-to-end encrypted messenger with voice and video calls. No ads, no trackers, no data collection. The Signal Protocol is the gold standard for messaging encryption — adopted by WhatsApp, Google Messages, and others.

## Architectural Role

Client-side application layer — messaging. Server component is open-source but centralized (run by Signal Foundation). All encryption happens on-device.

---

## Formal Assessment

### Context

```
deployment: mobile app (not self-hosted — no server component for end users)
scale: single-user
platform: Android (APK from signal.org)
```

### S1: Pause

| # | Test | Result | Evidence |
|---|------|--------|----------|
| 1a | Can you stop the process without a special shutdown procedure? | ✅ Yes | Close the app. Force-stop in Android settings. No daemon required. |
| 1b | After stopping, is all user data still on disk? | ✅ Yes | Messages stored in local encrypted SQLite database on device storage. |
| 1c | Can you restart and continue with the same data? | ✅ Yes | Reopen app → all messages, contacts, settings intact. No re-registration. |

**S1 = Yes**

### S2: Exit

| # | Test | Result | Evidence |
|---|------|--------|----------|
| 2a | Is there a documented export mechanism? | ✅ Yes | Settings → Chats → Chat backups. Creates encrypted backup file on local storage. |
| 2b | Does the export include ALL user-generated data? | ✅ Yes | Messages, media, stickers, group info included. Call history partially excluded. |
| 2c | Is the export format documented and non-proprietary? | ❌ No | Proprietary encrypted format. Only Signal can decrypt and restore it. Format is not publicly documented. |
| 2d | Can at least one other tool consume the export? | ❌ No | No third-party tool can read Signal backups. |

**S2 = Partial-E1** (export exists, data is complete, but format is proprietary)

### S3: Recoverability

| # | Test | Result | Evidence |
|---|------|--------|----------|
| 3a | Can the data be backed up? | ✅ Yes | Built-in encrypted backup to local storage. File can be copied by standard tools. |
| 3b | Can you restore from backup to a working state? | ✅ Yes | New device → install Signal → restore from backup file → working. |
| 3c | Does restore give back ALL user data? | ✅ Yes | Messages, media restored. Session keys regenerated (inherent to E2E, not a data loss). |

**S3 = Yes**

### Autonomy Level

| S1 | S2 | S3 | Table lookup | Level |
|----|----|----|-------------|-------|
| Yes | Partial-E1 | Yes | "Yes / Partial-E1 / any → A2" | **A2** |

### Transparency Level

| Test | Result | Evidence |
|------|--------|----------|
| Source code publicly available? | ✅ Yes | Client: github.com/signalapp/Signal-Android, Signal-iOS, Signal-Desktop. Server: github.com/signalapp/Signal-Server |
| License OSI-approved? | ✅ Yes | AGPL-3.0 (client and server) |

**T = T2**

### Diagnostic Score

| # | Question | Result | Evidence |
|---|----------|--------|----------|
| D1 | Personalisation | ✅ Clean | No analytics, no recommendation engine, no behavioural tracking. Sealed sender hides metadata from server. |
| D2 | Urgency | ✅ Clean | No unsolicited notifications beyond message delivery. No countdown timers. No forced updates. |
| D3 | Hidden cost | ⚠️ Concern | **Requires phone number for registration.** Links identity to telecom infrastructure. Cannot use pseudonymously. |
| D4 | Transparency fragility | ✅ Clean | Donation-funded nonprofit. No dark patterns. Straightforward ToS. |
| D5 | Trajectory | ✅ Clean | AGPL-3.0 unchanged. All features free. No feature gating. Signal Foundation (501c3). |

**D-score: D4/5** (1 concern: D3)

---

## Counterarguments

| Claim | Challenge | Resolution |
|-------|-----------|------------|
| **A2** | "But you CAN migrate to a new device with all your data" | Yes, but only to another Signal instance. Partial-E1 is clear: proprietary format. Under v1.1, this caps at A2. |
| **A2** | Most messaging apps are A0 — isn't A2 unfair? | A2 is not a penalty. It accurately describes: you can pause and recover, but you cannot exit to a non-Signal tool with your data. |
| **T2** | Server federation not supported | T2 measures code visibility. Code is public and auditable. Operational centralization is separate from transparency. |
| **T2** | Can't self-host the server practically | Same as above. T-level is about code access, not operational independence. |
| **D4** | Phone number is "just registration" | It's a real identity cost. You cannot use Signal without revealing a phone number to telecom infrastructure. D3 concern is correct. |

---

## What would make Signal A3?

Signal reaches A3 if either:

- Backup format is publicly documented and at least one third-party tool can parse it → S2 becomes Yes
- Signal adopts an open export format (e.g., JSON message archive) → S2 becomes Yes

This is not a criticism. It is a measurement. A2/T2 is a strong rating — it means you control everything except portability of message history.

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
| [SimpleX Chat](simplex-chat.md) | A3 / T2 | No phone number. Database export in documented format. |
| [Briar](briar.md) | A0 / T2 | P2P over Tor. Maximum security, but no export and no backup by design → A0. |
| [Element (Matrix)](matrix.md) | A3 / T2 | Federated. Self-hostable. Open export format. |

---

## Trajectory

**Direction: stable**

Signal Foundation is a nonprofit. The protocol is widely adopted and audited. No signs of commercial pressure or feature gating. Centralization and proprietary backup format remain the main concerns.

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
