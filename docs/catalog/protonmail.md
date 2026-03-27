---
nav_exclude: false
trajectory: "closing"
parent: "Technology Catalog"
nav_order: 99
title: "Proton Mail"
category: "communication/email"
status: "stable"
license: "Proprietary"
source: "-"
repository: "-"
documentation: "https://proton.me/support/mail"
docker_image: "-"
community: "https://www.reddit.com/r/ProtonMail"
autonomy_level: "A0"
transparency_level: "T1"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Pause", "Exit", "External Dependencies"]
---

# Proton Mail

> **TAS Score: S0/3 — D2/5 · A0 / T1**
> _(S0: cannot pause, exit cleanly, or recover independently — all mail on Proton servers. D2: proprietary server, Bridge requires paid plan, trajectory closing for free tier.)_

## Why it's in the catalog

Proton Mail is widely used as a "privacy-respecting" alternative to Gmail. It is included to make the trade-offs visible — privacy from Google does not mean autonomy. You are still a tenant on someone else's infrastructure.

## Brief Description

Encrypted email service with zero-knowledge architecture. End-to-end encrypted between Proton users. Proton Bridge allows standard email clients (IMAP/SMTP) — but only on paid plans. No self-hosting option.

## Architectural Role

Cannot be self-hosted. All mail stored on Proton's servers in Switzerland. Encryption happens client-side — Proton cannot read your mail, but they control delivery, storage, and access.

## Technical Autonomy

- [ ] Works without internet
- [ ] Stores data locally
- [ ] Does not require external accounts
- [x] Allows data export (via Proton Mail export tool — MBOX/EML)
- [ ] Provides offline updates

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ❌     | Cancelling account = losing access to all mail |
| Exit                  | ⚠️     | Export tool exists but requires active account; attachments included |
| Recoverability        | ❌     | Recovery depends entirely on Proton's infrastructure |
| Visibility            | ⚠️     | Cryptographic architecture documented; server code closed |
| External Dependencies | ❌     | 100% dependent on Proton servers |

## Autonomous Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Mailcow](mailcow.md) | A3 / T2 | Full self-hosted mail server |
| [Stalwart](stalwart.md) | A3 / T2 | Modern self-hosted mail server, Rust-based |

---

## Trajectory

**Direction: closing**

Proton has progressively restricted the free tier — reducing storage, limiting Bridge to paid plans, and adding features only in paid tiers. The acquisition of SimpleLogin and Standard Notes signals a platform play. Privacy from surveillance is genuine, but the trajectory for self-hosting and autonomy is closing.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ⚠️ | Server proprietary; clients partially open source |
| Feature gating | ⚠️ | Bridge (IMAP/SMTP) requires paid plan; free tier progressively restricted |
| Self-hosting | ⚠️ | No self-hosting path exists or is planned |
| Governance | ⚠️ | Proton AG controls direction; VC-backed growth phase |

---

## Sources

- **Website:** https://proton.me/mail
- **Documentation:** https://proton.me/support/mail
- **Community:** https://www.reddit.com/r/ProtonMail
