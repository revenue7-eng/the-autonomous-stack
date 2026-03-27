---
parent: "Technology Catalog"
nav_order: 99
title: "MariaDB"
category: "storage/database"
status: "stable"
license: "GPL-2.0"
source: "https://github.com/MariaDB/server"
repository: "https://github.com/MariaDB/server"
documentation: "https://mariadb.com/kb/en"
docker_image: "mariadb"
community: "https://mariadb.zulipchat.com"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: ["prometheus"]
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
---

# MariaDB

> **TAS Score: S3/3 — D4/5 · A3 / T2**
> _(D4 not D5: MariaDB Corporation went through financial difficulties in 2023 — acquired by K1 Investment Management. Governance trajectory to watch.)_

## Brief Description

Community-developed fork of MySQL created by MySQL's original author (Monty Widenius) after Oracle's acquisition. Drop-in replacement for MySQL. GPL-2.0. MariaDB Foundation provides independent governance separate from MariaDB Corporation.

## Architectural Role

Storage layer. MySQL-compatible relational database. Drop-in replacement for MySQL in most self-hosted applications — Nextcloud, WordPress, Gitea, and others support MariaDB natively.

## Technical Autonomy

- [x] Works without internet
- [x] Stores data locally
- [x] Does not require external accounts
- [x] Allows data export (mysqldump compatible; mariadb-dump)
- [ ] Provides offline updates

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Clean stop; no permanent damage |
| Exit                  | ✅     | mysqldump compatible; standard SQL output |
| Recoverability        | ✅     | Standard backup and recovery; binary logs |
| Visibility            | ✅     | GPL-2.0, fully auditable |
| External Dependencies | ✅     | Runs fully self-contained |

## Configuration (Minimal)

```yaml
services:
  mariadb:
    image: mariadb:11
    environment:
      MARIADB_ROOT_PASSWORD: changeme
      MARIADB_DATABASE: myapp
      MARIADB_USER: myapp
      MARIADB_PASSWORD: changeme
    volumes:
      - mariadb_data:/var/lib/mysql
    ports:
      - "3306:3306"

volumes:
  mariadb_data:
```

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [PostgreSQL](postgresql.md) | A3 / T2 | More powerful; preferred for new deployments |
| [MySQL](mysql.md) | A3 / T1 | Oracle-owned original; commercial features gated |

---

## Trajectory

**Direction: mixed**

MariaDB was created to provide a community alternative to Oracle-controlled MySQL. The MariaDB Foundation provides independent governance. However, MariaDB Corporation (the commercial entity) went through financial difficulties in 2023 and was acquired by K1 Investment Management — a private equity firm. The Foundation remains independent but the corporate trajectory adds uncertainty.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | GPL-2.0; no changes |
| Feature gating | ➖ | Enterprise features exist but core is fully open |
| Self-hosting | ✅ | Self-hosting well-supported |
| Governance | ⚠️ | MariaDB Corp acquired by K1 (PE) in 2023; Foundation independent but watch |

---

## Sources

- **Website:** https://mariadb.org
- **Documentation:** https://mariadb.com/kb/en
- **Repository:** https://github.com/MariaDB/server
- **Docker image:** mariadb
- **Community:** https://mariadb.zulipchat.com
