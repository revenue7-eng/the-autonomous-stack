---
nav_exclude: false
title: "Mealie"
category: "applications/household"
status: "stable"
license: "AGPL-3.0"
source: "https://mealie.io"
repository: "https://github.com/mealie-recipes/mealie"
documentation: "https://docs.mealie.io"
docker_image: "ghcr.io/mealie-recipes/mealie"
community: "https://github.com/mealie-recipes/mealie/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: []
depended_by: []
critical_criteria: ["Exit", "Pause"]
trajectory: "opening"
parent: Technology Catalog
nav_order: 99
---

# Mealie

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Self-hosted recipe manager and meal planner. Import recipes from any URL with automatic ingredient parsing, plan weekly meals, generate shopping lists, and manage a family cookbook — all without ads or subscriptions.

## Architectural Role

Household layer: replaces recipe apps (Paprika, Whisk, Yummly) and bookmarked recipe websites. Centralizes family cooking knowledge in a searchable, shareable, self-hosted application.

## Technical Autonomy

- ✅ Works without internet (all recipes stored locally)
- ✅ Stores all data locally (SQLite or PostgreSQL)
- ✅ Does not require external accounts
- ✅ Full data export (JSON, ZIP backup with images)
- ✅ Recipe import from URLs via scraping

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅ | Stop container, all recipes stay. Resume anytime. |
| Exit                  | ✅ | Full JSON export with images. Portable data. |
| Recoverability        | ✅ | Built-in backup/restore. SQLite file or PostgreSQL dump. |
| Visibility            | ✅ | AGPL-3.0, fully auditable. |
| External Dependencies | ✅ | Fully self-hosted. URL import scrapes directly, no API dependency. |

## Configuration (Minimal)

```yaml
services:
  mealie:
    image: ghcr.io/mealie-recipes/mealie:latest
    container_name: mealie
    ports:
      - "9925:9000"
    volumes:
      - ./data/mealie:/app/data
    environment:
      - TZ=UTC
      - BASE_URL=https://meals.example.com
    restart: unless-stopped
```

## Related Recipes

- [Family Cloud](../recipes/family-cloud.md) — add Mealie for family meal planning

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| Tandoor Recipes | A3 / T2 | More complex, more features. Django-based. PostgreSQL required. |
| Grocy | A3 / T2 | Broader scope — grocery management, not just recipes. |
| Paprika | A1 / T0 | Paid app, cloud sync, proprietary. Good UI but no self-hosting. |

---

## Trajectory

**Direction: opening.**

Mealie v1 was a complete rewrite from v0, showing active development and architectural investment. Growing community, regular releases, expanding feature set without feature gating.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | AGPL-3.0, unchanged. |
| Feature gating | ✅ | No paid tier. Everything is free. |
| Self-hosting | ✅ | Docker-first, good documentation, active Docker Hub presence. |
| Governance | ✅ | Multiple contributors. Healthy issue/PR activity. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [mealie.io](https://mealie.io)
- **Repository:** [github.com/mealie-recipes/mealie](https://github.com/mealie-recipes/mealie)
- **Docker image:** `ghcr.io/mealie-recipes/mealie`
