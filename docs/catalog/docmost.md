---
nav_exclude: false
title: "Docmost"
parent: "Technology Catalog"
nav_order: 99
category: "applications/wiki"
status: "stable"
license: "AGPL-3.0"
source: "https://github.com/docmost/docmost"
repository: "https://github.com/docmost/docmost"
documentation: "https://docmost.com/docs"
docker_image: "docmost/docmost"
community: "https://github.com/docmost/docmost/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: []
depended_by: []
critical_criteria: ["Trajectory"]
---

# Docmost

> **TAS Score: S3/3 — D4/5** — A3 / T2
> D4 not D5: young project (launched 2024) — trajectory needs more time to evaluate; sustainability depends on continued maintainer commitment (Q8).

## Brief Description

Open-source, self-hosted documentation and wiki platform. Real-time collaborative editor with simultaneous editing. Hierarchical page structure with workspaces. AGPL-3.0 licensed. Often described as the selfhosted Notion/Confluence alternative. One of the most popular new selfhosted projects of 2025.

## Architectural Role

Knowledge management layer: team documentation, wikis, knowledge bases. Real-time collaboration. Modern alternative to Confluence and Notion.

## Technical Autonomy

- [x] Works without internet — fully functional on local network
- [x] Stores data locally — PostgreSQL database, all content on your server
- [x] Does not require external accounts
- [x] Allows data export — pages exportable as Markdown and HTML
- [x] Provides offline updates — Docker image, updated manually

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Stop the container. Data persists in PostgreSQL. Resume without loss. |
| Exit                  | ✅     | Export as Markdown. PostgreSQL database directly accessible. Standard formats. |
| Recoverability        | ✅     | PostgreSQL backup + file storage. Docker-based deployment. Straightforward restore. |
| Visibility            | ✅     | Fully open source (AGPL-3.0). Source available on GitHub. |
| External Dependencies | ✅     | Requires PostgreSQL and Redis — both open source. No external service calls. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

```yaml
services:
  docmost:
    image: docmost/docmost:latest
    environment:
      - DATABASE_URL=postgresql://docmost:secret@db:5432/docmost
      - REDIS_URL=redis://redis:6379
      - APP_SECRET=change-me-to-random-string
    ports:
      - 3000:3000
    depends_on:
      - db
      - redis

  db:
    image: postgres:16
    environment:
      - POSTGRES_DB=docmost
      - POSTGRES_USER=docmost
      - POSTGRES_PASSWORD=secret
    volumes:
      - ./pgdata:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
```

## Related Recipes

- [Developer Workstation](../recipes/developer-workstation.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [BookStack](bookstack.html) | A3 / T2 | More mature (10 years), MIT, no real-time collab, simpler |
| [Confluence](confluence.html) | A0 / T0 | Enterprise standard, proprietary lock-in, expensive |
| [Notion](notion.html) | A0 / T0 | Polished UI, cloud-only |

---

## Trajectory

**Direction: opening (early stage)**

Active development with strong community momentum. AGPL license protects openness. No enterprise split so far. Young project — sustainability depends on continued maintainer commitment and potential business model development. Worth watching.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | AGPL-3.0. Open source. |
| Feature gating | ✅ | All features free currently. No paid tier announced. |
| Self-hosting | ✅ | Self-hosting is the primary deployment model. |
| Governance | ➖ | Small team. Open source but early — governance not yet formalized. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** https://docmost.com
- **Documentation:** https://docmost.com/docs
- **Repository:** https://github.com/docmost/docmost
- **Docker image:** docmost/docmost
- **Community:** https://github.com/docmost/docmost/discussions
