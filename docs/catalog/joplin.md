---
nav_exclude: false
parent: "Technology Catalog"
nav_order: 99
title: "Joplin"
category: "applications/notes"
status: "stable"
license: "AGPL-3.0"
source: "https://github.com/laurent22/joplin"
repository: "https://github.com/laurent22/joplin"
documentation: "https://joplinapp.org/help"
docker_image: "joplin/server"
community: "https://discourse.joplinapp.org"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: ["syncthing", "nextcloud"]
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
---

# Joplin

> **TAS Score: S3/3 — D4/5 · A3 / T2**
> _(D4 not D5: Joplin Cloud exists as a paid sync option — commercial focus growing alongside self-hosted.)_

## Brief Description

Open-source note-taking app with end-to-end encryption. Supports Markdown, notebooks, tags, attachments. Sync via self-hosted Joplin Server, Nextcloud, WebDAV, or local filesystem. Available on all platforms.

## Architectural Role

Applications layer. Personal knowledge management and note-taking. Can run fully local without any server — sync is optional. Self-hosted Joplin Server adds multi-user sharing.

## Technical Autonomy

- [x] Works without internet
- [x] Stores data locally
- [x] Does not require external accounts
- [x] Allows data export (JEX, Markdown, PDF, HTML)
- [ ] Provides offline updates

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Local app — no server required for basic use |
| Exit                  | ✅     | Full export to JEX, Markdown, or raw files |
| Recoverability        | ✅     | Notes stored as files; standard backup applies |
| Visibility            | ✅     | AGPL-3.0, fully auditable |
| External Dependencies | ✅     | Works fully offline; sync is optional |

## Configuration (Minimal)

```yaml
services:
  joplin-db:
    image: postgres:16
    environment:
      POSTGRES_DB: joplin
      POSTGRES_USER: joplin
      POSTGRES_PASSWORD: changeme
    volumes:
      - joplin_db:/var/lib/postgresql/data

  joplin:
    image: joplin/server:latest
    depends_on: [joplin-db]
    environment:
      APP_PORT: 22300
      APP_BASE_URL: https://joplin.yourdomain.com
      DB_CLIENT: pg
      POSTGRES_HOST: joplin-db
      POSTGRES_DATABASE: joplin
      POSTGRES_USER: joplin
      POSTGRES_PASSWORD: changeme
    ports:
      - "22300:22300"

volumes:
  joplin_db:
```

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Logseq](logseq.md) | A3 / T2 | Graph-based, local-first, no server needed |
| [Obsidian](obsidian.md) | A2 / T0 | Proprietary app, local files |

---

## Trajectory

**Direction: stable**

Joplin has been AGPL-3.0 since launch. Joplin Cloud launched as an optional paid sync service — it does not affect self-hosted functionality. The app works completely without any server. Core development has been consistent for 7+ years. Main risk: single primary maintainer.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | AGPL-3.0 since launch; no changes |
| Feature gating | ➖ | Joplin Cloud is optional; no local features gated |
| Self-hosting | ✅ | Self-hosted server actively maintained; sync alternatives supported |
| Governance | ➖ | Single primary maintainer (laurent22); large community; no foundation |

---

## Sources

- **Website:** https://joplinapp.org
- **Documentation:** https://joplinapp.org/help/apps/sync
- **Repository:** https://github.com/laurent22/joplin
- **Docker image:** joplin/server
- **Community:** https://discourse.joplinapp.org
