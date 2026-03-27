---
nav_exclude: false
title: "Grafana"
category: "observability/dashboards"
status: "stable"
license: "AGPL-3.0"
source: "https://grafana.com"
repository: "https://github.com/grafana/grafana"
documentation: "https://grafana.com/docs/grafana/latest/"
docker_image: "https://hub.docker.com/r/grafana/grafana"
community: "https://community.grafana.com"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: ["prometheus"]
depended_by: []
critical_criteria: ["Recoverability"]
parent: Technology Catalog
nav_order: 99
---

# Grafana

> **TAS Score: S3/3 -- D4/5** -- A3 / T2
> D4 (not D5): optional telemetry is enabled by default and must be explicitly disabled (Q4 personalisation).
> **Critical criteria for this category:** Recoverability.


## Brief Description

Open-source observability and data visualisation platform. Dashboards for metrics, logs, and traces from Prometheus, InfluxDB, Loki, Elasticsearch, and dozens of other sources. The standard for infrastructure monitoring dashboards.

## Architectural Role

Observability layer: visualisation and alerting on top of metrics and log sources. Pairs with Prometheus for metrics, Loki for logs, Tempo for traces. Does not store data itself -- connects to data sources.

## Technical Autonomy

- ✅ Works without internet (after initial setup; connects to local data sources)
- ✅ Stores data locally (dashboards, users, alert rules in SQLite or PostgreSQL)
- ✅ Does not require external accounts
- ✅ Allows data export (dashboards exportable as JSON; provisioning via config files)
- ✅ Provides offline updates (manual upgrade via packages or Docker)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
| --------------------- | ------ | -------- |
| Pause                 | Yes    | Service can be stopped; dashboards and config persist on disk. |
| Exit                  | Yes    | Dashboards are JSON, exportable and portable. Data lives in external sources you control. |
| Recoverability        | Yes    | Database backups; dashboard versioning built in; provisioning from config files enables reproducible setup. |
| Visibility            | Yes    | Open source (AGPL-3.0), fully auditable. |
| External Dependencies | Yes    | No mandatory external services. Grafana Cloud exists but is optional. |

## Configuration (Minimal)

Example `docker-compose.yml` snippet:

```yaml
services:
  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    volumes:
      - ./grafana-data:/var/lib/grafana
    restart: unless-stopped
```

Add Prometheus as a data source after startup via the web UI or provisioning config.

## Related Recipes

* [Minimal Autonomous Server](../recipes/minimal-server.md) -- can be extended with Grafana + Prometheus for full observability.

## Alternatives

* Netdata -- real-time monitoring with built-in visualisation, less customisable
* Chronograf -- InfluxDB-specific dashboard
* Kibana -- Elasticsearch-specific, similar role but tied to Elastic stack

## Trajectory

**Direction: mixed.**

Grafana Labs changed the licence from Apache 2.0 to AGPL-3.0 in 2021. Core dashboarding and alerting remain open. Enterprise features (SSO, RBAC, reporting, advanced data source plugins) are not in the OSS edition and are moving further into the enterprise tier. Watch for features migrating from OSS to enterprise-only.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ⚠️ | Apache 2.0 → AGPL-3.0 in 2021; AGPL's copyleft requirements affect embedding in proprietary products. |
| Feature gating | ⚠️ | SSO, RBAC, reporting, and several plugins are enterprise-only and growing. |
| Self-hosting | ➖ | OSS self-hosting remains well-supported; Grafana Cloud is optional. |
| Governance | ➖ | Grafana Labs controls direction; community contributions accepted but roadmap is corporate-driven. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

## Sources

* [Website](https://grafana.com)
* [Documentation](https://grafana.com/docs/grafana/latest/)
* [Repository](https://github.com/grafana/grafana)
* [Docker image](https://hub.docker.com/r/grafana/grafana)
* [Community](https://community.grafana.com)
