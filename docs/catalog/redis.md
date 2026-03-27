---
nav_exclude: false
parent: "Technology Catalog"
nav_order: 99
title: "Redis"
category: "storage/cache"
status: "stable"
license: "RSALv2 / SSPLv1"
source: "https://github.com/redis/redis"
repository: "https://github.com/redis/redis"
documentation: "https://redis.io/docs"
docker_image: "redis"
community: "https://discord.gg/redis"
autonomy_level: "A2"
transparency_level: "T1"
depends_on: ["docker"]
optional_deps: ["prometheus"]
depended_by: []
critical_criteria: ["Exit", "External Dependencies"]
---

# Redis

> **TAS Score: S3/3 — D2/5 · A2 / T1**
> _(T1 not T2: RSALv2 and SSPLv1 are NOT OSI-approved licenses — license changed from BSD in 2024. D2: license change ⚠️, governance ⚠️, trajectory closing.)_

## Why the score changed

Redis was BSD-3-Clause (A3/T2, opening) until March 2024 when Redis Ltd. changed the license to RSALv2 / SSPLv1 — neither of which is OSI-approved. This is a textbook trajectory event: a project that was in Lux (A3/T2) moved to Vigil/Stella zone overnight. The community responded with Valkey (Linux Foundation fork, BSD-3-Clause).

## Brief Description

In-memory data structure store. Used as cache, message broker, and session store. Extremely fast. Redis is no longer open source as of March 2024. **Valkey** is the community fork that preserved the open-source license.

## Architectural Role

Storage layer. In-memory cache and message broker. Used by many applications for session storage, rate limiting, pub/sub. Often a dependency rather than a standalone service.

## Technical Autonomy

- [x] Works without internet
- [x] Stores data locally (optional persistence)
- [x] Does not require external accounts
- [x] Allows data export (RDB snapshot, AOF log)
- [ ] Provides offline updates

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Clean stop; optional persistence |
| Exit                  | ✅     | RDB/AOF export; Valkey is wire-compatible |
| Recoverability        | ✅     | RDB snapshot backup |
| Visibility            | ⚠️     | Source available but not OSI-approved license |
| External Dependencies | ✅     | Runs fully self-contained |

## Autonomous Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| Valkey | A3 / T2 | Linux Foundation fork; BSD-3-Clause; wire-compatible drop-in |
| KeyDB | A3 / T2 | BSD-3-Clause fork; multithreaded |

---

## Trajectory

**Direction: closing**

Redis Ltd. changed the license from BSD-3-Clause to RSALv2/SSPLv1 in March 2024 — restricting commercial use of Redis as a managed service. This is not OSI-approved open source. The Linux Foundation immediately forked Redis as Valkey. For new deployments, **Valkey is recommended over Redis**.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ⚠️ | BSD-3-Clause → RSALv2/SSPLv1 in March 2024; not OSI-approved |
| Feature gating | ⚠️ | Redis Stack features (search, JSON) commercial-first |
| Self-hosting | ✅ | Self-hosting still works; license change affects service providers |
| Governance | ⚠️ | Redis Ltd. controls direction; community forked to Valkey in response |

---

## Sources

- **Website:** https://redis.io
- **Documentation:** https://redis.io/docs
- **Repository:** https://github.com/redis/redis
- **Docker image:** redis
- **Valkey fork:** https://github.com/valkey-io/valkey
