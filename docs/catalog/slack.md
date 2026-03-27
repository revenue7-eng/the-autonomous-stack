---
nav_exclude: false
title: "Slack"
trajectory: "closing"
parent: "Technology Catalog"
nav_order: 99
category: "communication/messaging"
status: "stable"
license: "Proprietary"
source: "-"
repository: "-"
documentation: "https://api.slack.com"
docker_image: "-"
community: "-"
autonomy_level: "A0"
transparency_level: "T0"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Exit", "Hidden cost"]
---

# Slack

> **TAS Score: S0/3 — D1/5** — A0 / T0
> S0 not S3: cannot pause without losing workspace access (Q1); exit loses message history, integrations, and channel structure (Q2); no self-recovery — depends on Salesforce/Slack infrastructure (Q3). D1 not D5: builds usage profiles and analytics on team behaviour (Q4); notification design creates urgency (Q5); free tier limits message history to 90 days — you pay with data loss (Q6); closed platform, no audit possible (Q7). D1 for trajectory only: acquired by Salesforce, enterprise features growing (Q8).

## Brief Description

Cloud-based team messaging platform. Channels, threads, integrations, file sharing. Free tier with 90-day message history limit. Owned by Salesforce since 2021.

## Architectural Role

Communication layer: team messaging, integrations hub, notification system. Central to many organisations' daily workflows.

## Technical Autonomy

- [ ] Works without internet
- [ ] Stores data locally
- [ ] Does not require external accounts — requires Slack account
- [x] Allows data export — workspace export available for admins (JSON format); free tier limited; DMs require Corporate Export (paid)
- [ ] Provides offline updates

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ❌     | Pausing means losing access to all channels and history. No clean pause. |
| Exit                  | ❌     | Export is JSON — not importable to alternatives. Integrations, bots, and workflows do not transfer. Channel structure and context lost. |
| Recoverability        | ❌     | No local backup. If Slack suspends workspace or changes terms, no self-recovery. |
| Visibility            | ❌     | Closed source. No visibility into data processing or retention beyond stated policies. |
| External Dependencies | ❌     | Fully dependent on Slack/Salesforce infrastructure. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Why it's in the catalog

Slack is the de facto standard for team communication — and a textbook example of convenience lock-in. The more integrations you build, the harder it becomes to leave. The 90-day message history limit on free tier means your team's knowledge disappears unless you pay. Export format (JSON) is not importable anywhere else.

## Autonomous Alternatives

- [Matrix/Element](matrix.html) (A3/T2) — federated, E2EE, selfhosted, open protocol
- [Mattermost](https://mattermost.com) (A3/T2) — Slack-like UI, selfhosted, open source

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Matrix/Element](matrix.html) | A3 / T2 | Federated protocol, E2EE, selfhosted server, different UX |
| Mattermost | A3 / T2 | Closest Slack alternative in UX, selfhosted, MIT (community) |
| [Telegram](telegram.html) | A1 / T0 | Easier UX, partially open client, server is proprietary |

---

## Trajectory

**Direction: closing**

Acquired by Salesforce in 2021. Enterprise features expanding. Free tier increasingly limited (90-day history introduced 2022). Pricing increases. Deeper Salesforce integration. The trend is toward enterprise monetization, not user independence.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ⚠️ | Proprietary. No change. |
| Feature gating | ⚠️ | 90-day history limit on free. DM export requires Corporate plan. Enterprise features growing. |
| Self-hosting | ⚠️ | No self-hosting option. Never offered. |
| Governance | ⚠️ | Salesforce subsidiary. Decisions driven by enterprise revenue. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** https://slack.com
- **Documentation:** https://api.slack.com
- **Repository:** -
- **Docker image:** -
- **Community:** -
