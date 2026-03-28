---
nav_exclude: false
title: "Actual Budget"
category: "applications/finance"
status: "stable"
license: "MIT"
source: "https://actualbudget.org"
repository: "https://github.com/actualbudget/actual"
documentation: "https://actualbudget.org/docs/"
docker_image: "ghcr.io/actualbudget/actual-server"
community: "https://discord.gg/pRYNYr4W5A"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: []
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
trajectory: "opening"
parent: Technology Catalog
nav_order: 99
---

# Actual Budget

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Local-first personal finance and budgeting app. Envelope budgeting methodology with bank sync support, reports, and rule-based transaction management. Data stored locally as SQLite — syncs across devices through a lightweight server. Originally commercial, now fully open source.

## Architectural Role

Applications layer: replaces YNAB, Mint, and other cloud-based budgeting services. Financial data stays on your hardware. The server is optional — only needed for multi-device sync.

## Technical Autonomy

- ✅ Works without internet (local-first architecture, all data on device)
- ✅ Stores data locally (SQLite database)
- ✅ Does not require external accounts
- ✅ Allows data export (OFX, CSV, full database backup)
- ✅ Bank sync optional, not required

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅ | Stop the server, app continues working locally. |
| Exit                  | ✅ | SQLite file is portable. Export to CSV/OFX. |
| Recoverability        | ✅ | Copy the SQLite file. Built-in backup/restore. |
| Visibility            | ✅ | MIT license. Fully auditable. |
| External Dependencies | ✅ | Fully self-contained. Bank sync (GoCardless/SimpleFIN) is optional. |

## Configuration (Minimal)

```yaml
services:
  actual:
    image: ghcr.io/actualbudget/actual-server:latest
    container_name: actual
    ports:
      - "5006:5006"
    volumes:
      - ./data/actual:/data
    restart: unless-stopped
```

## Related Recipes

- [Family Cloud](../recipes/family-cloud.md) — add Actual for family finance management

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| YNAB | A0 / T0 | Cloud-only, subscription-based. The service Actual replaces. |
| Firefly III | A3 / T2 | More complex, double-entry accounting. PHP-based. |
| GnuCash | A3 / T2 | Desktop app, traditional accounting. Not web-based. |

---

## Trajectory

**Direction: opening.**

Actual was originally a paid SaaS product. The creator open-sourced it in 2022 under MIT license. Community-driven development has accelerated since. More features, more contributors, regular releases.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | MIT. Was proprietary, now fully open. Trajectory reversal. |
| Feature gating | ✅ | No paid tier. Everything is free. |
| Self-hosting | ✅ | Docker-first, local-first architecture. Self-hosting is the primary use case. |
| Governance | ✅ | Community-driven. Multiple active maintainers. Healthy contributor base. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [actualbudget.org](https://actualbudget.org)
- **Repository:** [github.com/actualbudget/actual](https://github.com/actualbudget/actual)
- **Docker image:** `ghcr.io/actualbudget/actual-server`
