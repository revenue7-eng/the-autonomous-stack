---
nav_exclude: false
title: "Grocy"
category: "applications/household"
status: "stable"
license: "MIT"
source: "https://grocy.info"
repository: "https://github.com/grocy/grocy"
documentation: "https://grocy.info/documentation"
docker_image: "linuxserver/grocy"
community: "https://github.com/grocy/grocy/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: []
depended_by: []
critical_criteria: ["Exit", "Pause"]
trajectory: "stable"
parent: Technology Catalog
nav_order: 99
---

# Grocy

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Self-hosted grocery and household management. Track pantry inventory, manage shopping lists, plan meals, monitor expiration dates, manage chores, and track batteries/equipment. An ERP for your home.

## Architectural Role

Applications/household layer: replaces scattered shopping lists, fridge notes, and mental tracking of what you have and what you need. Barcode scanning support for quick inventory management.

## Technical Autonomy

- ✅ Works without internet (all data local)
- ✅ Stores data locally (SQLite)
- ✅ Does not require external accounts
- ✅ Allows data export (API, database backup)
- ✅ Barcode lookup works offline with local database

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅ | Stop container, all data stays. |
| Exit                  | ✅ | SQLite database. Full API for extraction. |
| Recoverability        | ✅ | Copy SQLite file. Simple backup. |
| Visibility            | ✅ | MIT license. PHP codebase. |
| External Dependencies | ✅ | Fully self-contained. |

## Configuration (Minimal)

```yaml
services:
  grocy:
    image: linuxserver/grocy
    container_name: grocy
    ports:
      - "9283:80"
    volumes:
      - ./data/grocy:/config
    environment:
      - TZ=UTC
    restart: unless-stopped
```

## Related Recipes

- [Family Cloud](../recipes/family-cloud.md) — add Grocy for household management

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Mealie](mealie.md) | A3 / T2 | Recipe-focused. Grocy is broader (inventory, chores, equipment). |
| Tandoor Recipes | A3 / T2 | Recipes only. More polished meal planning. |
| AnyList | A0 / T0 | Cloud-only, proprietary shopping list app. |
| OurGroceries | A0 / T0 | Cloud-only, proprietary. |

---

## Trajectory

**Direction: stable.**

Grocy has been consistently maintained since 2017 by a single dedicated developer. MIT licensed, regular releases, no commercialization. The household ERP niche has few competitors.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | MIT, unchanged. |
| Feature gating | ✅ | No paid tier. |
| Self-hosting | ✅ | Docker via linuxserver.io, native PHP. |
| Governance | ⚠️ | Single developer (berrnd). Bus factor = 1. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [grocy.info](https://grocy.info)
- **Repository:** [github.com/grocy/grocy](https://github.com/grocy/grocy)
- **Docker image:** `linuxserver/grocy`
