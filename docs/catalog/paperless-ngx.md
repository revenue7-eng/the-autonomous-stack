---
tags: [documents, ocr, archive, notion-alternative]
title: "Paperless-ngx"
category: "applications/documents"
status: "stable"
license: "GPL-3.0"
source: "https://paperless-ngx.readthedocs.io"
repository: "https://github.com/paperless-ngx/paperless-ngx"
documentation: "https://paperless-ngx.readthedocs.io"
docker_image: "https://hub.docker.com/r/paperlessngx/paperless-ngx"
community: "https://github.com/paperless-ngx/paperless-ngx/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker", "postgresql"]
optional_deps: ["redis"]
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
parent: Technology Catalog
nav_order: 15
---

# Paperless-ngx

> **TAS Score: S3/3 -- D5/5** -- A3 / T2
> **Critical criteria for this category:** Exit, Recoverability.


## Brief Description

Document management system that transforms your physical and digital documents into a searchable, organized archive. OCR, tagging, and full‑text search — all self‑hosted.

## Architectural Role

Applications layer: central repository for documents, invoices, receipts, and correspondence. Acts as a digital filing cabinet.

## Technical Autonomy

- ✅ Works without internet (after initial setup; OCR and processing local)
- ✅ Stores data locally (media files, database, index)
- ✅ Does not require external accounts
- ✅ Allows data export (files and database can be backed up)
- ✅ Provides offline updates (manual upgrade via Docker)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
| --------------------- | ------ | -------- |
| Pause                 | Yes    | Services can be stopped; documents remain accessible via filesystem. |
| Exit                  | Yes    | All documents stored as ordinary files; you can export the database and take your data elsewhere. |
| Recoverability        | Yes    | Database and media backups; built‑in export tools. |
| Visibility            | Yes    | Open source, fully documented, auditable. |
| External Dependencies | Yes    | No mandatory external services; can run fully offline. |

## Configuration (Minimal)

Example `docker-compose.yml` snippet:

```yaml
services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: paperless
      POSTGRES_USER: paperless
      POSTGRES_PASSWORD: change-me
    volumes:
      - ./postgres-data:/var/lib/postgresql/data

  redis:
    image: redis:7

  paperless:
    image: ghcr.io/paperless-ngx/paperless-ngx:latest
    ports:
      - "8000:8000"
    volumes:
      - ./paperless-data:/usr/src/paperless/data
      - ./paperless-media:/usr/src/paperless/media
      - ./consume:/usr/src/paperless/consume
      - ./export:/usr/src/paperless/export
    environment:
      PAPERLESS_SECRET_KEY: change-me
      PAPERLESS_DBENGINE: postgresql
      PAPERLESS_DBHOST: postgres
      PAPERLESS_DBNAME: paperless
      PAPERLESS_DBUSER: paperless
      PAPERLESS_DBPASS: change-me
      PAPERLESS_REDIS: redis://redis:6379
    depends_on:
      - postgres
      - redis
```

## Related Recipes

* [Minimal Autonomous Server](../recipes/minimal-server.md) – can be extended with Paperless for document archiving.

## Alternatives

* Mayan EDMS – more complex, enterprise‑oriented.
* Teedy – lighter but less feature‑rich.
* Nextcloud – can store documents but lacks dedicated OCR and metadata extraction.

---

## Trajectory

**Direction: opening.**

Paperless-ngx was created as a community fork of paperless-ng after the original maintainer abandoned the project. It is GPL-3.0, community-governed, and actively developed. No corporate ownership, no monetisation pressure, no enterprise tier.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | GPL-3.0; forked to preserve community development after upstream abandonment. |
| Feature gating | ✅ | No paid tier; all features available to all users. |
| Self-hosting | ✅ | Self-hosting is the only deployment model. |
| Governance | ✅ | Community-governed; active maintainer team; transparent roadmap. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

* [Website](https://paperless-ngx.readthedocs.io)

* [Documentation](https://paperless-ngx.readthedocs.io)

* [Repository](https://github.com/paperless-ngx/paperless-ngx)

* [Docker image](https://hub.docker.com/r/paperlessngx/paperless-ngx)

* [Community](https://github.com/paperless-ngx/paperless-ngx/discussions)
