---
nav_exclude: false
trajectory: "opening"
parent: "Technology Catalog"
nav_order: 99
title: "PostgreSQL"
category: "storage/database"
status: "stable"
license: "PostgreSQL License"
source: "https://github.com/postgres/postgres"
repository: "https://github.com/postgres/postgres"
documentation: "https://www.postgresql.org/docs"
docker_image: "postgres"
community: "https://www.postgresql.org/community"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: ["prometheus"]
depended_by: ["nextcloud", "vaultwarden", "authentik", "forgejo", "immich", "plausible", "umami", "joplin", "woodpecker"]
critical_criteria: ["Exit", "Recoverability"]
---

# PostgreSQL

> **TAS Score: S3/3 — D5/5 · A3 / T2**

## Brief Description

The world's most advanced open-source relational database. ACID-compliant, full SQL support, JSON, full-text search, extensions. The default database choice for serious self-hosted deployments. Used by Nextcloud, Authentik, Immich, Forgejo, Plausible, and most other catalog entries.

## Architectural Role

Storage layer. The foundational database for most self-hosted applications. Runs as a separate service that other applications connect to. Paired with pgAdmin or similar for management.

## Technical Autonomy

- [x] Works without internet
- [x] Stores data locally
- [x] Does not require external accounts
- [x] Allows data export (pg_dump, COPY, logical replication)
- [ ] Provides offline updates

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Clean stop; no permanent damage |
| Exit                  | ✅     | pg_dump produces standard SQL; portable to any PostgreSQL instance |
| Recoverability        | ✅     | pg_dump, WAL archiving, PITR — industry-standard recovery |
| Visibility            | ✅     | PostgreSQL License (OSI-approved), fully auditable |
| External Dependencies | ✅     | Runs fully self-contained |

## Configuration (Minimal)

```yaml
services:
  postgres:
    image: postgres:16
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: myapp
      POSTGRES_PASSWORD: changeme
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  postgres_data:
```

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [MariaDB](mariadb.md) | A3 / T2 | MySQL-compatible; good for apps requiring MySQL |
| [SQLite](sqlite.md) | A3 / T1 | Embedded, zero-config; not for multi-user apps |

---

## Trajectory

**Direction: opening**

PostgreSQL has been developed by the PostgreSQL Global Development Group (PGDG) since 1996 — a community of volunteers and companies with no single corporate controller. The PostgreSQL License is OSI-approved and permissive. No commercial entity can change the license or gate features. Development is active, with major releases annually. The gold standard for autonomous database infrastructure.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | PostgreSQL License (OSI-approved); unchanged since 1996 |
| Feature gating | ✅ | No paid tier; all features in community edition |
| Self-hosting | ✅ | Self-hosting is the only deployment model |
| Governance | ✅ | PGDG community governance; no corporate control |

---

## Sources

- **Website:** https://www.postgresql.org
- **Documentation:** https://www.postgresql.org/docs/current
- **Repository:** https://github.com/postgres/postgres
- **Docker image:** postgres
- **Community:** https://www.postgresql.org/community
