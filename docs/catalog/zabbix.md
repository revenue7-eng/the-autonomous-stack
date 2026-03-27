---
title: "Zabbix"
category: "observability/monitoring"
status: "stable"
license: "AGPL-3.0"
source: "https://github.com/zabbix/zabbix"
repository: "https://github.com/zabbix/zabbix"
documentation: "https://www.zabbix.com/documentation"
docker_image: "zabbix/zabbix-server-pgsql"
community: "https://www.zabbix.com/forum"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: ["prometheus", "grafana"]
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
---

# Zabbix

> **TAS Score: S3/3 — D4/5 · A3 / T2**
> _(D4 not D5: Zabbix LLC sells enterprise support and certified training — commercial focus exists but does not gate features.)_

## Brief Description

Enterprise-grade open-source monitoring platform. Monitors servers, networks, applications, cloud resources. Agent-based and agentless. Highly configurable alerting, dashboards, and auto-discovery. Battle-tested at scale since 2001.

## Architectural Role

Observability layer. Full-stack monitoring — infrastructure, network, applications. Heavier than Prometheus/Grafana stack but more self-contained. Good fit for environments that need a single monitoring platform with built-in alerting.

## Technical Autonomy

- [x] Works without internet
- [x] Stores data locally (PostgreSQL or MySQL)
- [x] Does not require external accounts
- [x] Allows data export (XML, CSV, API)
- [ ] Provides offline updates

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Clean stop, no permanent damage |
| Exit                  | ✅     | Full XML export; PostgreSQL database directly accessible |
| Recoverability        | ✅     | Standard database backup and restore |
| Visibility            | ✅     | AGPL-3.0, fully auditable |
| External Dependencies | ✅     | Fully self-contained; no cloud required |

## Configuration (Minimal)

```yaml
services:
  zabbix-db:
    image: postgres:16
    environment:
      POSTGRES_DB: zabbix
      POSTGRES_USER: zabbix
      POSTGRES_PASSWORD: changeme
    volumes:
      - zabbix_db:/var/lib/postgresql/data

  zabbix-server:
    image: zabbix/zabbix-server-pgsql:latest
    depends_on: [zabbix-db]
    environment:
      DB_SERVER_HOST: zabbix-db
      POSTGRES_DB: zabbix
      POSTGRES_USER: zabbix
      POSTGRES_PASSWORD: changeme
    ports:
      - "10051:10051"

  zabbix-web:
    image: zabbix/zabbix-web-nginx-pgsql:latest
    depends_on: [zabbix-server]
    environment:
      DB_SERVER_HOST: zabbix-db
      POSTGRES_DB: zabbix
      POSTGRES_USER: zabbix
      POSTGRES_PASSWORD: changeme
      ZBX_SERVER_HOST: zabbix-server
    ports:
      - "8080:8080"

volumes:
  zabbix_db:
```

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Prometheus](prometheus.md) | A3 / T2 | Metrics-focused, lighter, better ecosystem |
| [Netdata](netdata.md) | A3 / T2 | Easier setup, real-time focus |
| [Grafana](grafana.md) | A3 / T2 | Dashboards only — needs separate metrics source |

---

## Trajectory

**Direction: stable**

Zabbix has been AGPL-3.0 since launch with no license changes. Zabbix LLC monetises through enterprise support contracts and certified training — not by gating features. The open-source version and the enterprise version are identical in functionality. Development is active and consistent.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | AGPL-3.0 since launch; no changes |
| Feature gating | ➖ | No feature gating; enterprise = support contract only |
| Self-hosting | ✅ | Self-hosting is the only deployment model |
| Governance | ➖ | Zabbix LLC controls direction; community contributions accepted |

---

## Sources

- **Website:** https://www.zabbix.com
- **Documentation:** https://www.zabbix.com/documentation/current
- **Repository:** https://github.com/zabbix/zabbix
- **Docker image:** zabbix/zabbix-server-pgsql
- **Community:** https://www.zabbix.com/forum
