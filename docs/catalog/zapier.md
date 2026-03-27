---
nav_exclude: false
title: "Zapier"
parent: "Technology Catalog"
nav_order: 99
category: "applications/automation"
status: "stable"
license: "Proprietary"
source: "-"
repository: "-"
documentation: "https://zapier.com/help"
docker_image: "-"
community: "https://community.zapier.com"
autonomy_level: "A0"
transparency_level: "T0"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Exit", "Hidden cost"]
---

# Zapier

> **TAS Score: S0/3 — D1/5** — A0 / T0
> S0 not S3: cannot pause without breaking active workflows (Q1); exit loses all Zaps — no portable export format (Q2); no self-recovery (Q3). D1 not D5: tracks usage patterns across connected services (Q4); free tier limits create artificial urgency to upgrade (Q5); you pay with workflow data — Zapier sees credentials and data flowing through every Zap (Q6); closed platform, no audit possible (Q7). D1 for trajectory: pricing increases, AI features requiring cloud processing (Q8).

## Brief Description

Cloud-based workflow automation platform. Connects 7,000+ apps via triggers and actions ("Zaps"). No-code interface. Free tier limited to 100 tasks/month with single-step Zaps only.

## Architectural Role

Integration/automation layer: connects services, automates workflows between applications. Sits between other tools as a data bridge.

## Technical Autonomy

- [ ] Works without internet
- [ ] Stores data locally
- [ ] Does not require external accounts — requires Zapier account plus credentials for every connected service
- [ ] Allows data export — Zaps not exportable in any reusable format
- [ ] Provides offline updates

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ❌     | Pausing breaks active automations. Dependent workflows may fail silently. |
| Exit                  | ❌     | No export of Zaps. Workflows must be manually recreated on any alternative. |
| Recoverability        | ❌     | No local backup. If Zapier changes pricing or suspends account — all automations stop. |
| Visibility            | ❌     | Closed source. No visibility into data processing or retention. |
| External Dependencies | ❌     | Fully dependent on Zapier infrastructure plus every connected service's API. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Why it's in the catalog

Zapier is the default automation tool — and the deepest form of lock-in in this category. Your automation logic is not exportable. Your credentials pass through their servers. The more Zaps you build, the harder it becomes to leave.

## Autonomous Alternatives

- [n8n](n8n.html) (A3/T2) — selfhosted workflow automation, visual editor, 400+ integrations
- [Node-RED](node-red.html) (A3/T2) — flow-based automation, IoT-focused, lightweight

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [n8n](n8n.html) | A3 / T2 | Closest Zapier alternative in UX, selfhosted, 400+ integrations |
| [Node-RED](node-red.html) | A3 / T2 | Flow-based, lightweight, IoT-strong, steeper learning curve |

---

## Trajectory

**Direction: closing**

Pricing increasing consistently. Free tier more limited. AI features require cloud processing. Enterprise tier growing. Business model depends on users building more Zaps — which increases lock-in.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ⚠️ | Proprietary. No change. |
| Feature gating | ⚠️ | Free: 100 tasks, single-step. Multi-step, filters behind paid plans. |
| Self-hosting | ⚠️ | No self-hosting. Never offered. |
| Governance | ⚠️ | VC-backed. Revenue-driven. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** https://zapier.com
- **Documentation:** https://zapier.com/help
- **Repository:** -
- **Docker image:** -
- **Community:** https://community.zapier.com
