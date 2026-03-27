---
nav_exclude: false
title: "Telegram"
parent: "Technology Catalog"
nav_order: 99
category: "communication/messaging"
status: "stable"
license: "GPL-2.0 (client), Proprietary (server)"
source: "https://github.com/nicegram/nicegram-ios"
repository: "https://github.com/nicegram/nicegram-ios"
documentation: "https://core.telegram.org"
docker_image: "-"
community: "-"
autonomy_level: "A1"
transparency_level: "T0"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Exit", "Visibility"]
---

# Telegram

> **TAS Score: S1/3 — D2/5** — A1 / T0
> S1 not S3: pause is possible (Q1); exit loses channel subscribers, group history, and username — no portable format (Q2); no self-recovery — server is proprietary and centralized (Q3). D2 not D5: phone number required — identity tied to telecom (Q4); notification design creates urgency (Q5); server is proprietary — no audit of data handling possible (Q7). D2: client code is open, project is independent from big tech (Q6, Q8).

## Brief Description

Cloud-based messaging platform. Personal and group chats, channels, bots, file sharing. Client apps are open source (GPL-2.0). Server infrastructure is proprietary and centralized. Requires phone number for registration.

## Architectural Role

Communication layer: personal and group messaging, channels, bots. Used as both messaging app and content distribution platform.

## Technical Autonomy

- [ ] Works without internet — requires internet for all operations
- [ ] Stores data locally — messages stored on Telegram's servers; "Secret Chats" are device-to-device but not default
- [ ] Does not require external accounts — requires phone number
- [x] Allows data export — Telegram Desktop has built-in export (HTML/JSON); channel subscriber lists and group membership not exportable
- [ ] Provides offline updates — client updated via app stores

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Can stop using it without data loss. Account persists. |
| Exit                  | ❌     | Personal chat history exportable via desktop client. But channels, subscribers, group context, and username are not portable. No migration path to alternatives. |
| Recoverability        | ❌     | All data on Telegram's servers. If account is banned or servers are blocked in your country, no self-recovery. |
| Visibility            | ⚠️     | Client apps are open source (GPL-2.0). Server is completely proprietary. MTProto protocol is documented but server implementation is closed. |
| External Dependencies | ❌     | Fully dependent on Telegram's centralized infrastructure. No federation, no self-hosting. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Why it's in the catalog

Telegram is the interesting middle ground — A1, not A0. Clients are open source. The protocol is documented. It's not tied to a big tech company. But the server is proprietary and centralized. You cannot selfhost Telegram. You cannot federate. Your data lives on their servers, and your identity is tied to a phone number you don't fully control.

The open client code gives visibility into what runs on your device — but not into what happens on their servers. This is partial transparency without actual autonomy.

## Autonomous Alternatives

- [Matrix/Element](matrix.html) (A3/T2) — federated, E2EE by default, selfhosted, open protocol and server

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Matrix/Element](matrix.html) | A3 / T2 | Federated, E2EE, selfhosted server, open protocol |
| [Slack](slack.html) | A0 / T0 | Team-focused, fully proprietary, workspace model |
| Signal | A1 / T2 | E2EE by default, open source (client + server), but centralized and phone-number required |

---

## Trajectory

**Direction: mixed**

Telegram remains independent from big tech. Client code stays open source. However, the platform is increasingly monetized (Premium subscriptions, ads in channels). Server remains proprietary with no indication of change. Founder's legal situation (French arrest 2024) adds governance uncertainty. No self-hosting or federation roadmap.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ➖ | Client: GPL-2.0 (open). Server: proprietary. No changes. |
| Feature gating | ⚠️ | Telegram Premium introduces paid features. Ads in channels. Monetization increasing. |
| Self-hosting | ⚠️ | No self-hosting option. Not on roadmap. |
| Governance | ⚠️ | Single founder (Pavel Durov). No foundation or community governance. Legal uncertainty after 2024. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** https://telegram.org
- **Documentation:** https://core.telegram.org
- **Repository:** https://github.com/nicegram/nicegram-ios (client example)
- **Docker image:** -
- **Community:** -
