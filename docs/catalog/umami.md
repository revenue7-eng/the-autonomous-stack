---
parent: "Technology Catalog"
nav_order: 99
title: "Umami"
category: "analytics/web"
status: "stable"
license: "MIT"
source: "https://github.com/umami-software/umami"
repository: "https://github.com/umami-software/umami"
documentation: "https://umami.is/docs"
docker_image: "ghcr.io/umami-software/umami"
community: "https://github.com/umami-software/umami/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: ["prometheus"]
depended_by: []
critical_criteria: ["Exit", "External Dependencies"]
---

# Umami

> **TAS Score: S3/3 — D4/5** — A3 / T2
> _(D4 not D5: Umami Cloud launched in 2023 — commercial focus is growing alongside the self-hosted version. Watch for feature divergence.)_

## Brief Description

Simple, fast, privacy-focused web analytics. Single database (PostgreSQL or MySQL), minimal setup. No cookies, GDPR compliant. MIT licensed — the most permissive of the self-hosted analytics options.

## Architectural Role

Applications layer. Lightest self-hosted analytics option — single container + single database. Good fit for small to medium sites where Plausible's ClickHouse requirement is overkill.

## Technical Autonomy

- [x] Works without internet
- [x] Stores data locally
- [x] Does not require external accounts
- [x] Allows data export (CSV)
- [ ] Provides offline updates

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Clean stop, no permanent damage |
| Exit                  | ✅     | CSV export; direct database access |
| Recoverability        | ✅     | Standard PostgreSQL/MySQL backup |
| Visibility            | ✅     | MIT license, fully auditable |
| External Dependencies | ✅     | Runs fully offline |

## Configuration (Minimal)

```yaml
services:
  umami-db:
    image: postgres:16
    environment:
      POSTGRES_DB: umami
      POSTGRES_USER: umami
      POSTGRES_PASSWORD: changeme
    volumes:
      - umami_db:/var/lib/postgresql/data

  umami:
    image: ghcr.io/umami-software/umami:postgresql-latest
    depends_on: [umami-db]
    environment:
      DATABASE_URL: postgresql://umami:changeme@umami-db:5432/umami
      APP_SECRET: changeme_random_string
    ports:
      - "3000:3000"

volumes:
  umami_db:
```

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Plausible](plausible.md) | A3 / T2 | More features, heavier stack (ClickHouse required) |
| [Google Analytics](google-analytics.md) | A0 / T0 | Cloud-only, full data collection |

---

## Trajectory

**Direction: mixed**

Umami launched Umami Cloud in 2023, shifting some development focus toward the commercial offering. MIT license ensures the self-hosted version remains fully open. Watch for features appearing in Cloud before making it to self-hosted, or self-hosted setup becoming more complex as Cloud features diverge.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | MIT since launch; no changes |
| Feature gating | ➖ | No gating yet; Cloud launched 2023 — trend to watch |
| Self-hosting | ➖ | Still well-supported; Cloud launch adds some uncertainty |
| Governance | ⚠️ | VC-backed (raised funding in 2022); commercial pressure increasing |

---

## Sources

- **Website:** https://umami.is
- **Documentation:** https://umami.is/docs/install
- **Repository:** https://github.com/umami-software/umami
- **Docker image:** ghcr.io/umami-software/umami
- **Community:** https://github.com/umami-software/umami/discussions
