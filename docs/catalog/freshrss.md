---
nav_exclude: false
title: "FreshRSS"
category: "applications/news"
status: "stable"
license: "AGPL-3.0"
source: "https://freshrss.org"
repository: "https://github.com/FreshRSS/FreshRSS"
documentation: "https://freshrss.github.io/FreshRSS/"
docker_image: "freshrss/freshrss"
community: "https://github.com/FreshRSS/FreshRSS/discussions"
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

# FreshRSS

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Self-hosted RSS/Atom feed aggregator. Subscribe to websites, blogs, and news sources without algorithms deciding what you see. Supports OPML import/export, full-text extraction, and mobile apps via Google Reader API.

## Architectural Role

Information layer: replaces Google News, Twitter feeds, and algorithmic timelines with a chronological, user-controlled feed. You choose what to read, in what order, with no tracking or engagement optimization.

## Technical Autonomy

- ✅ Works without internet (reads cached articles offline)
- ✅ Stores all data locally (articles, subscriptions, read status)
- ✅ Does not require external accounts
- ✅ OPML export — portable subscription list
- ⚠️ Needs internet to fetch new articles from RSS feeds

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅ | Stop container, articles stay. Resume fetching when ready. |
| Exit                  | ✅ | OPML export gives you all subscriptions. Import into any RSS reader. |
| Recoverability        | ✅ | SQLite database, simple backup/restore. |
| Visibility            | ✅ | AGPL-3.0, fully auditable. |
| External Dependencies | ✅ | Fully self-hosted. No cloud dependency. |

## Configuration (Minimal)

```yaml
services:
  freshrss:
    image: freshrss/freshrss
    container_name: freshrss
    ports:
      - "8082:80"
    volumes:
      - ./data/freshrss/data:/var/www/FreshRSS/data
      - ./data/freshrss/extensions:/var/www/FreshRSS/extensions
    environment:
      - TZ=UTC
      - CRON_MIN=2,32
    restart: unless-stopped
```

## Related Recipes

- [Privacy-First Homelab](../recipes/privacy-first-homelab.md)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| Miniflux | A3 / T2 | Minimalist RSS reader in Go. PostgreSQL-backed. Faster, fewer features. |
| Tiny Tiny RSS | A3 / T2 | Older, feature-rich. PHP-based. More complex setup. |
| Feedly | A0 / T0 | Cloud-only, freemium. Tracks reading habits. |

---

## Trajectory

**Direction: stable.**

FreshRSS has been consistently maintained since 2013. Active development, regular releases, growing extension ecosystem. No signs of commercialization or feature gating.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | AGPL-3.0, unchanged since inception. |
| Feature gating | ✅ | No paid tier. Everything is free. |
| Self-hosting | ✅ | Docker, native PHP, extensive docs. |
| Governance | ✅ | Multiple active maintainers. Healthy community contributions. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [freshrss.org](https://freshrss.org)
- **Repository:** [github.com/FreshRSS/FreshRSS](https://github.com/FreshRSS/FreshRSS)
- **Docker image:** `freshrss/freshrss`
