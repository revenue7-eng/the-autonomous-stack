---
title: "Prometheus"
category: "observability/metrics"
status: "stable"
license: "Apache-2.0"
source: "https://prometheus.io"
repository: "https://github.com/prometheus/prometheus"
documentation: "https://prometheus.io/docs/"
docker_image: "https://hub.docker.com/r/prom/prometheus"
community: "https://github.com/prometheus/prometheus/discussions"
autonomy_level: "A3"
transparency_level: "T2"
---

# Prometheus

## Brief Description

Open‑source monitoring system that collects metrics from targets, stores them locally, and enables powerful querying, alerting, and visualisation.

---

## Architectural Role

Observability layer: metrics collection, storage, and alerting for infrastructure and applications. Often paired with Grafana for dashboards.

---

## Technical Autonomy

- ✅ Works without internet (after setup)
- ✅ Stores data locally (TSDB)
- ✅ Does not require external accounts
- ✅ Allows data export (remote read/write, snapshot, backup)
- ✅ Provides offline updates (manual via packages)

---

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
|-----------|--------|----------|
| Pause | Yes | Service can be stopped; data remains on disk. |
| Exit | Yes | Data can be exported; no vendor lock‑in. |
| Recoverability | Yes | Backups of data directory can be restored. |
| Visibility | Yes | Open source, fully auditable. |
| External Dependencies | Yes | No required cloud services; can run offline. |

---

## Configuration (Minimal)

Basic `prometheus.yml` configuration:

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'node'
    static_configs:
      - targets: ['localhost:9100']
```

Start Prometheus:

``` bash
prometheus --config.file=prometheus.yml
```

For Docker:

```yaml
services:
  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus-data:/prometheus
```

## Related Recipes

- [Minimal Autonomous Server](../recipes/minimal-server.md) – can be extended with Prometheus and Grafana for full observability.

## Alternatives

- VictoriaMetrics – faster, more scalable, Prometheus‑compatible.

- InfluxDB – time‑series database, different query language.

- Netdata – real‑time monitoring, less emphasis on long‑term storage.

## Sources

- Website
https://prometheus.io

- Documentation
https://prometheus.io/docs/

- Repository
https://github.com/prometheus/prometheus

- Docker image
https://hub.docker.com/r/prom/prometheus

- Community
https://github.com/prometheus/prometheus/discussions
