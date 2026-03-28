---
nav_exclude: false
title: "Wallabag"
category: "applications/reading"
status: "stable"
license: "MIT"
source: "https://wallabag.org"
repository: "https://github.com/wallabag/wallabag"
documentation: "https://doc.wallabag.org"
docker_image: "wallabag/wallabag"
community: "https://github.com/wallabag/wallabag/discussions"
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

# Wallabag

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Self-hosted read-it-later service. Save articles from the web, strip ads and clutter, read offline. Browser extensions, mobile apps, and RSS feed export. Replaces Pocket, Instapaper, and browser bookmarks for articles.

## Architectural Role

Applications layer: personal article archive. Save articles you want to read later, annotate, tag, and search. Content is extracted and stored permanently — articles survive even if the original website goes down.

## Technical Autonomy

- ✅ Works without internet (reads saved articles offline)
- ✅ Stores data locally (articles, tags, annotations in database)
- ✅ Does not require external accounts
- ✅ Allows data export (JSON, CSV, EPUB, PDF, plain text)
- ⚠️ Needs internet to save new articles from URLs

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅ | Stop container, all saved articles remain. |
| Exit                  | ✅ | Full export in multiple formats. Import into any other service. |
| Recoverability        | ✅ | Database backup. Articles stored as full text, not just links. |
| Visibility            | ✅ | MIT license, fully auditable. |
| External Dependencies | ✅ | Fully self-hosted. No third-party dependency. |

## Configuration (Minimal)

```yaml
services:
  wallabag:
    image: wallabag/wallabag
    container_name: wallabag
    ports:
      - "8090:80"
    volumes:
      - ./data/wallabag/images:/var/www/wallabag/web/assets/images
      - ./data/wallabag/data:/var/www/wallabag/data
    environment:
      - SYMFONY__ENV__DOMAIN_NAME=https://read.example.com
      - SYMFONY__ENV__DATABASE_DRIVER=pdo_sqlite
      - SYMFONY__ENV__DATABASE_NAME=wallabag
    restart: unless-stopped
```

## Related Recipes

- [Privacy-First Homelab](../recipes/privacy-first-homelab.md)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| Pocket | A0 / T0 | Cloud-only, owned by Mozilla/Fakespot. Tracks reading habits. |
| Instapaper | A0 / T0 | Cloud-only, proprietary. |
| Omnivore | A0 / T0 | Was open source, acquired and shut down in 2024. |
| Linkding | A3 / T2 | Bookmark manager, not full article archiver. Simpler. |

---

## Trajectory

**Direction: stable.**

Wallabag has been consistently maintained since 2013. French open-source project with steady development. No signs of commercialization. The hosted service (wallabag.it) funds development without restricting self-hosting.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | MIT, unchanged since inception. |
| Feature gating | ✅ | No paid tier for self-hosted. Hosted service is optional. |
| Self-hosting | ✅ | Docker, native PHP, well documented. |
| Governance | ✅ | Community-driven, multiple maintainers. Healthy project. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [wallabag.org](https://wallabag.org)
- **Repository:** [github.com/wallabag/wallabag](https://github.com/wallabag/wallabag)
- **Docker image:** `wallabag/wallabag`
