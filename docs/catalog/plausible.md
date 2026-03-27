---
title: "Plausible Analytics"
category: "analytics/web"
status: "stable"
license: "AGPL-3.0"
source: "https://github.com/plausible/analytics"
repository: "https://github.com/plausible/analytics"
documentation: "https://plausible.io/docs"
docker_image: "plausible/analytics"
community: "https://github.com/plausible/analytics/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: ["prometheus"]
depended_by: []
critical_criteria: ["Exit", "External Dependencies"]
---

# Plausible Analytics

> **TAS Score: S3/3 — D4/5** — A3 / T2
> _(D4 not D5: Plausible Cloud is the primary commercial product — self-hosted is supported but not the main focus of the company's development effort.)_

## Brief Description

Lightweight, privacy-friendly web analytics. No cookies, no personal data collection, GDPR compliant by design. Self-hosted version is fully functional and identical to the cloud offering.

## Architectural Role

Applications layer. Replaces Google Analytics as a website traffic analytics tool. Runs as a standalone service with a PostgreSQL and ClickHouse backend.

## Technical Autonomy

- [x] Works without internet
- [x] Stores data locally
- [x] Does not require external accounts
- [x] Allows data export (CSV)
- [ ] Provides offline updates (requires internet for image pulls)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Can be stopped cleanly; no permanent damage |
| Exit                  | ✅     | Full CSV export of all stats |
| Recoverability        | ✅     | Standard PostgreSQL + ClickHouse backups |
| Visibility            | ✅     | AGPL-3.0, fully auditable |
| External Dependencies | ✅     | Runs fully offline after initial setup |

## Configuration (Minimal)

```yaml
services:
  plausible_db:
    image: postgres:16
    environment:
      POSTGRES_DB: plausible
      POSTGRES_USER: plausible
      POSTGRES_PASSWORD: changeme
    volumes:
      - plausible_db:/var/lib/postgresql/data

  plausible_events_db:
    image: clickhouse/clickhouse-server:24
    volumes:
      - plausible_events:/var/lib/clickhouse

  plausible:
    image: plausible/analytics:v2
    depends_on: [plausible_db, plausible_events_db]
    environment:
      DATABASE_URL: postgres://plausible:changeme@plausible_db/plausible
      CLICKHOUSE_DATABASE_URL: http://plausible_events_db:8123/plausible_events
      SECRET_KEY_BASE: changeme_generate_with_openssl
      BASE_URL: https://analytics.yourdomain.com
    ports:
      - "8000:8000"

volumes:
  plausible_db:
  plausible_events:
```

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Umami](umami.md) | A3 / T2 | Simpler stack, single PostgreSQL database |
| [Google Analytics](google-analytics.md) | A0 / T0 | Cloud-only, full data collection |

---

## Trajectory

**Direction: stable**

Plausible has been AGPL-3.0 since launch and has not changed its licensing or self-hosting policy. The team is small (bootstrapped, no VC funding) and explicitly committed to privacy-first analytics. The self-hosted version receives the same updates as the cloud product. Main risk: small team dependency.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | AGPL-3.0 since launch; no changes |
| Feature gating | ➖ | All features available in self-hosted; no enterprise tier |
| Self-hosting | ✅ | Self-hosted docs actively maintained; Docker images updated regularly |
| Governance | ➖ | Small bootstrapped team; no VC pressure; single-company risk |

---

## Sources

- **Website:** https://plausible.io
- **Documentation:** https://plausible.io/docs/self-hosting
- **Repository:** https://github.com/plausible/analytics
- **Docker image:** plausible/analytics
- **Community:** https://github.com/plausible/analytics/discussions
