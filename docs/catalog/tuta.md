---
nav_exclude: false
trajectory: "mixed"
parent: "Technology Catalog"
nav_order: 99
title: "Tuta (Tutanota)"
category: "communication/email"
status: "stable"
license: "GPL-3.0"
source: "https://github.com/tutao/tutanota"
repository: "https://github.com/tutao/tutanota"
documentation: "https://tuta.com/support"
docker_image: "-"
community: "https://github.com/tutao/tutanota/discussions"
autonomy_level: "A0"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Pause", "Exit", "External Dependencies"]
---

# Tuta (Tutanota)

> **TAS Score: S0/3 — D3/5 · A0 / T1**
> _(S0: cloud-only, no self-hosting. T1 not T2: client is GPL-3.0 open source but server is closed — partial transparency. D3: trajectory mixed, client open but server direction unclear.)_

## Why it's in the catalog

Tuta is a privacy-focused encrypted email service. Like Proton Mail, it is included to distinguish privacy from autonomy — open-source clients do not make a cloud service self-hostable.

## Brief Description

End-to-end encrypted email and calendar. Client apps are GPL-3.0 open source — you can audit what runs on your device. The server is closed source. No IMAP/SMTP support — proprietary protocol only. No self-hosting option.

## Architectural Role

Cannot be self-hosted. All mail stored on Tuta's servers in Germany. The open-source client is a meaningful transparency signal — but the server controls delivery and storage.

## Technical Autonomy

- [ ] Works without internet
- [ ] Stores data locally
- [ ] Does not require external accounts
- [x] Allows data export (EML export available)
- [ ] Provides offline updates

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ❌     | Cancelling account = losing access to all mail |
| Exit                  | ⚠️     | EML export available; no IMAP so standard client migration is blocked |
| Recoverability        | ❌     | Recovery depends entirely on Tuta's infrastructure |
| Visibility            | ⚠️     | Client GPL-3.0 and auditable; server closed |
| External Dependencies | ❌     | 100% dependent on Tuta servers; no IMAP/SMTP |

## Autonomous Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Mailcow](mailcow.md) | A3 / T2 | Full self-hosted mail server |
| [Stalwart](stalwart.md) | A3 / T2 | Modern self-hosted mail server, Rust-based |

---

## Trajectory

**Direction: mixed**

Tuta's client being GPL-3.0 is a genuine positive signal — rare for a commercial email service. The company is bootstrapped with no VC funding, which reduces commercial pressure. However, the server remains closed and there is no self-hosting roadmap. The lack of IMAP/SMTP support is a deliberate lock-in decision. Renamed from Tutanota to Tuta in 2024.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | Client GPL-3.0; open source since launch |
| Feature gating | ➖ | Free tier functional; paid adds storage and custom domains |
| Self-hosting | ⚠️ | No self-hosting path; no IMAP/SMTP by design |
| Governance | ✅ | Bootstrapped, no VC; Tuta GmbH; community-responsive |

---

## Sources

- **Website:** https://tuta.com
- **Documentation:** https://tuta.com/support
- **Repository:** https://github.com/tutao/tutanota
- **Community:** https://github.com/tutao/tutanota/discussions
