---
nav_exclude: false
trajectory: "mixed"
parent: "Technology Catalog"
nav_order: 99
title: "MySQL"
category: "storage/database"
status: "stable"
license: "GPL-2.0"
source: "https://github.com/mysql/mysql-server"
repository: "https://github.com/mysql/mysql-server"
documentation: "https://dev.mysql.com/doc"
docker_image: "mysql"
community: "https://forums.mysql.com"
autonomy_level: "A3"
transparency_level: "T1"
depends_on: ["docker"]
optional_deps: ["prometheus"]
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
---

# MySQL

> **TAS Score: S3/3 — D3/5 · A3 / T1**
> _(T1 not T2: dual GPL/commercial license — GPL is OSI-approved but Oracle's commercial license adds restrictions. D3: Oracle ownership ⚠️, dual license ⚠️, trajectory mixed.)_

## Brief Description

The world's most widely deployed open-source relational database. LAMP stack staple. MySQL is owned by Oracle since 2010 — the community edition is GPL-2.0 but Oracle also sells a commercial license with additional features. MariaDB is a community fork created in response.

## Architectural Role

Storage layer. Relational database for web applications. Many legacy self-hosted apps (WordPress, Nextcloud, Gitea) support MySQL/MariaDB. For new deployments, PostgreSQL or MariaDB are generally preferred.

## Technical Autonomy

- [x] Works without internet
- [x] Stores data locally
- [x] Does not require external accounts
- [x] Allows data export (mysqldump, SELECT INTO OUTFILE)
- [ ] Provides offline updates

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Clean stop; no permanent damage |
| Exit                  | ✅     | mysqldump produces standard SQL; portable |
| Recoverability        | ✅     | mysqldump, binary logs, PITR supported |
| Visibility            | ⚠️     | GPL-2.0 community edition; some features in commercial edition only |
| External Dependencies | ✅     | Runs fully self-contained |

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [MariaDB](mariadb.md) | A3 / T2 | Community fork; fully open; drop-in replacement |
| [PostgreSQL](postgresql.md) | A3 / T2 | More powerful; preferred for new deployments |

---

## Trajectory

**Direction: mixed**

Oracle acquired MySQL in 2010 via Sun Microsystems. The community edition remains GPL-2.0 but Oracle controls the roadmap and licenses key features (thread pool, audit log) only in the commercial edition. The MySQL community forked to MariaDB precisely because of Oracle ownership concerns. Oracle has not changed the GPL license but the governance structure creates ongoing uncertainty.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ⚠️ | Dual GPL/commercial; Oracle controls; some features commercial-only |
| Feature gating | ⚠️ | Thread pool, audit log, enterprise encryption — commercial only |
| Self-hosting | ✅ | Community edition self-hosting unchanged |
| Governance | ⚠️ | Oracle-controlled; community has no input into direction |

---

## Sources

- **Website:** https://www.mysql.com
- **Documentation:** https://dev.mysql.com/doc/refman/8.0/en
- **Repository:** https://github.com/mysql/mysql-server
- **Docker image:** mysql
- **Community:** https://forums.mysql.com
