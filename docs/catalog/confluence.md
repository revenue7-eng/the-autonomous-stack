---
nav_exclude: false
title: "Confluence"
trajectory: "closing"
parent: "Technology Catalog"
nav_order: 99
category: "applications/wiki"
status: "stable"
license: "Proprietary"
source: "-"
repository: "-"
documentation: "https://support.atlassian.com/confluence-cloud/"
docker_image: "-"
community: "https://community.atlassian.com"
autonomy_level: "A0"
transparency_level: "T0"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Exit", "Trajectory"]
---

# Confluence

> **TAS Score: S1/3 — D1/5** — A0 / T0
> S1 not S3: pause is partial — subscription continues (Q1); exit is lossy — proprietary format, macros and app content lost on export (Q2); recoverability depends on Atlassian infrastructure or valid license for Data Center (Q3). D1 not D5: data on Atlassian servers subject to US CLOUD Act (Q6); value depends on ecosystem lock-in — marketplace apps create exit barriers (Q7); server edition discontinued 2024, cloud-forcing strategy is closing trajectory (Q8).

## Brief Description

Proprietary wiki and collaboration platform by Atlassian. Cloud-first since February 2024 — server edition discontinued. Data Center edition available for large enterprises at significantly higher cost. Tightly integrated with Jira.

## Architectural Role

Knowledge management layer: team documentation, project wikis, internal knowledge bases. Part of Atlassian ecosystem (Jira, Trello, Bitbucket).

## Technical Autonomy

- [ ] Works without internet — cloud requires constant internet; Data Center requires license validation
- [ ] Stores data locally — cloud stores on Atlassian servers (US/Ireland); Data Center stores locally but needs license
- [ ] Does not require external accounts — requires Atlassian account
- [x] Allows data export — XML or PDF export available, but proprietary format; macros and marketplace app content often lost
- [ ] Provides offline updates — cloud managed by Atlassian; Data Center updates require license

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ⚠️     | Can stop using it, but subscription continues. Data accessible but export is lossy. |
| Exit                  | ❌     | Proprietary format. Macros, templates, marketplace app content do not export cleanly. Years of structured knowledge become difficult to move. |
| Recoverability        | ❌     | Cloud: depends on Atlassian. Data Center: requires valid license to operate. No license = no access to your data. |
| Visibility            | ❌     | Proprietary. Closed source. No visibility into data processing or storage implementation. |
| External Dependencies | ❌     | Fully dependent on Atlassian cloud infrastructure and licensing. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Why it's in the catalog

Confluence is the enterprise standard — and a clear example of why trajectory matters. It started as a self-hosted server product. Atlassian discontinued server licenses in 2024, forcing customers to cloud (losing data sovereignty) or expensive Data Center ($27,000+/year for 500 users). This is exactly the pattern TAS detects: a product moving from openness toward closure.

## Autonomous Alternatives

- [BookStack](bookstack.html) (A3/T2) — MIT-licensed, simple, self-hosted wiki
- [Docmost](docmost.html) (A3/T2) — modern Notion/Confluence alternative with real-time collaboration

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [BookStack](bookstack.html) | A3 / T2 | MIT, simple hierarchy, mature (10 years), no real-time collab |
| [Docmost](docmost.html) | A3 / T2 | AGPL, real-time collaboration, Notion-like UI, newer project |
| [Notion](notion.html) | A0 / T0 | More polished UI but same cloud lock-in pattern |

---

## Trajectory

**Direction: closing**

Server edition discontinued February 2024. Cloud is the default. Data Center exists at enterprise pricing. The trend is clear: less user control, higher costs, deeper lock-in. Marketplace apps create additional exit barriers that compound over time.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ⚠️ | Proprietary. Server edition discontinued. |
| Feature gating | ⚠️ | Per-user pricing. Advanced features behind premium tiers. Marketplace apps add recurring costs. |
| Self-hosting | ⚠️ | Data Center available but expensive. Cloud strongly pushed. Server no longer an option. |
| Governance | ⚠️ | Public company (Atlassian). Decisions driven by revenue optimization. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** https://www.atlassian.com/software/confluence
- **Documentation:** https://support.atlassian.com/confluence-cloud/
- **Repository:** -
- **Docker image:** -
- **Community:** https://community.atlassian.com
