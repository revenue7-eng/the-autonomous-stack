---
nav_exclude: false
title: "Gmail"
trajectory: "closing"
parent: "Technology Catalog"
nav_order: 99
category: "communication/email"
status: "stable"
license: "Proprietary"
source: "-"
repository: "-"
documentation: "https://support.google.com/mail"
docker_image: "-"
community: "-"
autonomy_level: "A0"
transparency_level: "T0"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Exit", "Hidden cost"]
---

# Gmail

> **TAS Score: S0/3 — D1/5** — A0 / T0
> S0 not S3: cannot pause independently from Google account (Q1); exit loses your address and is lossy (Q2); no self-recovery — depends on Google support (Q3). D1 not D5: builds behavioural profile from email content (Q4); manufactures urgency via notifications and promotions tab (Q5); you pay with data — emails scanned for ad targeting (Q6); value depends on ignorance of data usage (Q7). D1 for trajectory only: stable but moving toward deeper AI integration requiring cloud processing (Q8).

## Brief Description

Google's cloud email service. Free tier with 15 GB shared storage across Google services. Part of Google Workspace for paid plans.

## Architectural Role

Communication layer: email sending, receiving, and storage. Tightly integrated with Google ecosystem (Drive, Calendar, Meet).

## Technical Autonomy

- [ ] Works without internet
- [ ] Stores data locally
- [ ] Does not require external accounts
- [x] Allows data export — Google Takeout provides mbox export; labels, filters, and contacts require separate export
- [ ] Provides offline updates

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ❌     | Disabling account risks losing access to all connected Google services. No clean way to pause email independently. |
| Exit                  | ⚠️     | Google Takeout exports emails as mbox. But labels, filters, forwarding rules, and the address itself cannot be transferred. |
| Recoverability        | ❌     | If Google suspends or deletes your account, recovery depends entirely on Google's support. No local backup by default. |
| Visibility            | ❌     | Closed source. No visibility into how emails are processed, filtered, or used for ad targeting. |
| External Dependencies | ❌     | Fully dependent on Google's infrastructure, terms of service, and account policies. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Why it's in the catalog

Gmail is the baseline A0/T0 in the email category. It works well, it's free, and it's deeply integrated — but you own nothing. Your email address belongs to Google. Your data lives on their servers. Your access depends on their terms. The hidden cost is not $0 — it's that your communications are scanned to build an advertising profile.

## Autonomous Alternatives

- [Mailcow](mailcow.html) (A3/T2) — full-featured selfhosted email suite, Docker-based
- [Stalwart](stalwart.html) (A3/T2) — modern all-in-one mail server written in Rust

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Mailcow](mailcow.html) | A3 / T2 | Docker-based, full email stack, higher resource requirements (4-6 GB RAM) |
| [Stalwart](stalwart.html) | A3 / T2 | Single binary, Rust, lower resource requirements, newer project |

---

## Trajectory

**Direction: closing**

Gmail's core functionality is stable, but Google increasingly integrates AI features that process email content on their servers. Workspace pricing has increased. Smart Compose, Smart Reply, and AI summarization require cloud processing of your email content. The trend is toward deeper integration, not user independence.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ⚠️ | Proprietary. Closed source. No change. |
| Feature gating | ⚠️ | AI features and increased storage behind paid tiers. Free tier storage shared across services. |
| Self-hosting | ⚠️ | No self-hosting option. Never offered. |
| Governance | ⚠️ | Corporate-governed. Terms of service can change unilaterally. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** https://mail.google.com
- **Documentation:** https://support.google.com/mail
- **Repository:** -
- **Docker image:** -
- **Community:** -
