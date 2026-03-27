---
nav_exclude: false
parent: "Technology Catalog"
nav_order: 99
title: "SQLite"
category: "storage/database"
status: "stable"
license: "Public Domain"
source: "https://sqlite.org/src"
repository: "https://sqlite.org/src"
documentation: "https://sqlite.org/docs.html"
docker_image: "-"
community: "https://sqlite.org/forum/forum"
autonomy_level: "A3"
transparency_level: "T1"
depends_on: []
optional_deps: []
depended_by: ["uptime-kuma", "headscale", "joplin", "woodpecker"]
critical_criteria: ["Exit", "Recoverability"]
---

# SQLite

> **TAS Score: S3/3 — D5/5 · A3 / T1**
> _(T1 not T2: Public Domain is not an OSI-approved license — it predates the OSI framework. Functionally more open than any OSI license, but T2 requires OSI-approved license by definition.)_

## Brief Description

The most widely deployed database engine in the world — embedded in every smartphone, browser, and operating system. A single file. Zero configuration. No server process. The right choice for single-user apps, edge devices, and development environments.

## Architectural Role

Storage layer. Embedded database — runs inside the application process, not as a separate service. The database is a single `.db` file on disk. Used by Uptime Kuma, Headscale, and many other catalog entries for lightweight storage.

## Technical Autonomy

- [x] Works without internet
- [x] Stores data locally (single file)
- [x] Does not require external accounts
- [x] Allows data export (.dump SQL, direct file copy)
- [x] Provides offline updates (library bundled with app)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | No server process to stop |
| Exit                  | ✅     | Single .db file; .dump produces standard SQL |
| Recoverability        | ✅     | Copy the .db file — that is the backup |
| Visibility            | ✅     | Public Domain — no restrictions whatsoever |
| External Dependencies | ✅     | Zero external dependencies; bundled in app |

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [PostgreSQL](postgresql.md) | A3 / T2 | Multi-user, network, production scale |
| [MariaDB](mariadb.md) | A3 / T2 | MySQL-compatible, multi-user |

---

## Trajectory

**Direction: stable**

SQLite has been in Public Domain since its creation by D. Richard Hipp in 2000. It is maintained by a small core team at Hwaci. No corporate ownership, no commercial pressure, no license to change. SQLite is embedded in billions of devices — it will outlast every other technology in this catalog. The Public Domain dedication is irrevocable.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | Public Domain since 2000; irrevocable |
| Feature gating | ✅ | No paid tier; no commercial entity |
| Self-hosting | ✅ | Embedded library; no server |
| Governance | ➖ | Small core team (Hwaci); single maintainer risk; but Public Domain protects forever |

---

## Sources

- **Website:** https://sqlite.org
- **Documentation:** https://sqlite.org/docs.html
- **Repository:** https://sqlite.org/src
- **Community:** https://sqlite.org/forum/forum
