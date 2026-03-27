---
nav_exclude: false
parent: "Technology Catalog"
nav_order: 99
title: "Google Analytics"
category: "analytics/web"
status: "stable"
license: "Proprietary"
source: "-"
repository: "-"
documentation: "https://developers.google.com/analytics"
docker_image: "-"
community: "-"
autonomy_level: "A0"
transparency_level: "T0"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Exit", "External Dependencies", "Pause"]
---

# Google Analytics

> **TAS Score: S0/3 — D1/5** — A0 / T0
> _(S0: cannot pause, exit, or recover independently. D1: fully proprietary, behavioural profiling by design, no self-hosting path, trajectory is closing as GA4 migration forced data loss.)_

## Why it's in the catalog

Google Analytics is the default choice for web analytics — installed on the majority of websites globally. It is included here as an anti-example to make the trade-offs visible when compared to self-hosted alternatives.

## Brief Description

Cloud-only web analytics platform by Google. Free to use, but your visitor data is processed by Google, used to build advertising profiles, and subject to Google's data retention and deletion policies.

## Architectural Role

Cannot be self-hosted. Operates entirely on Google's infrastructure. Data is sent to Google servers on every page load via a JavaScript snippet.

## Technical Autonomy

- [ ] Works without internet
- [ ] Stores data locally
- [ ] Does not require external accounts
- [ ] Allows data export (limited — no raw event export on free tier)
- [ ] Provides offline updates

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ❌     | Stopping means losing access to all historical data |
| Exit                  | ❌     | No raw data export on free tier; GA4 dropped Universal Analytics data without migration path |
| Recoverability        | ❌     | Data is on Google's servers; no user-controlled backup |
| Visibility            | ❌     | Fully proprietary; no code to inspect |
| External Dependencies | ❌     | 100% dependent on Google infrastructure |

## Autonomous Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Plausible](plausible.md) | A3 / T2 | Privacy-first, AGPL-3.0, self-hosted |
| [Umami](umami.md) | A3 / T2 | MIT license, lightest stack |

---

## Trajectory

**Direction: closing**

Google forced migration from Universal Analytics to GA4 in 2023 — with no data migration path, causing permanent loss of historical data for users who didn't manually export. The free tier has reduced data retention limits. GA4 introduced more aggressive behavioural modelling. The direction is consistently toward more data collection and less user control.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ⚠️ | Proprietary; terms of service changed repeatedly |
| Feature gating | ⚠️ | Raw data export and longer retention require GA360 (paid, enterprise) |
| Self-hosting | ⚠️ | No self-hosting path exists or is planned |
| Governance | ⚠️ | Fully controlled by Google; UA→GA4 forced migration with data loss |

---

## Sources

- **Website:** https://analytics.google.com
- **Documentation:** https://developers.google.com/analytics
- **Community:** https://support.google.com/analytics
