---
nav_exclude: false
title: "BookStack"
trajectory: "stable"
parent: "Technology Catalog"
nav_order: 99
category: "applications/wiki"
status: "stable"
license: "MIT"
source: "https://github.com/BookStackApp/BookStack"
repository: "https://github.com/BookStackApp/BookStack"
documentation: "https://www.bookstackapp.com/docs"
docker_image: "lscr.io/linuxserver/bookstack"
community: "https://github.com/BookStackApp/BookStack/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: []
depended_by: []
critical_criteria: []
---

# BookStack

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Open-source, self-hosted wiki platform built with PHP and Laravel. Organizes content in a book-like hierarchy: Shelves → Books → Chapters → Pages. MIT licensed. WYSIWYG and Markdown editors. 17,800+ GitHub stars.

## Architectural Role

Knowledge management layer: internal documentation, team wikis, knowledge bases. Standalone — no ecosystem dependencies.

## Technical Autonomy

- [x] Works without internet — fully functional on local network
- [x] Stores data locally — MySQL/MariaDB, all content on your server
- [x] Does not require external accounts
- [x] Allows data export — pages exportable as HTML, PDF, plain text, Markdown; bulk export via API and CLI
- [x] Provides offline updates — Git-based updates or Docker image

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Stop the server. Data persists in MySQL. Resume without loss. |
| Exit                  | ✅     | Export in four formats per page. Bulk export available. Standard MySQL database — directly accessible. |
| Recoverability        | ✅     | MySQL backup + file storage. Standard restore process. Docker simplifies recovery. |
| Visibility            | ✅     | Fully open source (MIT). Single codebase, no enterprise split. All features available to all users. |
| External Dependencies | ✅     | Requires PHP and MySQL — both open source and self-hosted. No external service calls. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

```yaml
services:
  bookstack:
    image: lscr.io/linuxserver/bookstack
    environment:
      - APP_URL=http://localhost:8080
      - DB_HOST=db
      - DB_DATABASE=bookstack
      - DB_USERNAME=bookstack
      - DB_PASSWORD=secret
    ports:
      - 8080:80
    depends_on:
      - db

  db:
    image: mariadb:10
    environment:
      - MYSQL_ROOT_PASSWORD=secret
      - MYSQL_DATABASE=bookstack
      - MYSQL_USER=bookstack
      - MYSQL_PASSWORD=secret
    volumes:
      - ./db:/var/lib/mysql
```

## Related Recipes

- [Privacy-First Homelab](../recipes/privacy-first-homelab.html)
- [Developer Workstation](../recipes/developer-workstation.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Docmost](docmost.html) | A3 / T2 | Real-time collaboration, Notion-like UI, newer, AGPL |
| [Confluence](confluence.html) | A0 / T0 | Enterprise standard, deep Jira integration, proprietary lock-in |
| [Notion](notion.html) | A0 / T0 | Polished UI, cloud-only, no self-hosting |

---

## Trajectory

**Direction: stable/opening**

Consistently maintained since 2015 by single developer (Dan Brown). MIT license with no signs of change. No VC funding, no enterprise edition, no dual licensing. Development is slow but steady — the trajectory pattern that builds trust.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | MIT. No changes in 10 years. |
| Feature gating | ✅ | All features free. No paid tier. |
| Self-hosting | ✅ | Self-hosting is the only deployment model. |
| Governance | ✅ | Single maintainer with transparent development. Independent — no corporate backing. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** https://www.bookstackapp.com
- **Documentation:** https://www.bookstackapp.com/docs
- **Repository:** https://github.com/BookStackApp/BookStack
- **Docker image:** lscr.io/linuxserver/bookstack
- **Community:** https://github.com/BookStackApp/BookStack/discussions
