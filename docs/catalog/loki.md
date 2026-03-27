---
parent: "Technology Catalog"
nav_order: 99
title: "Loki"
category: "observability/logs"
status: "stable"
license: "AGPL-3.0"
source: "https://github.com/grafana/loki"
repository: "https://github.com/grafana/loki"
documentation: "https://grafana.com/docs/loki/latest"
docker_image: "grafana/loki"
community: "https://github.com/grafana/loki/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker", "grafana"]
optional_deps: ["prometheus"]
depended_by: ["grafana"]
critical_criteria: ["Exit", "Recoverability"]
---

# Loki

> **TAS Score: S3/3 — D4/5 · A3 / T2**
> _(D4 not D5: Grafana Labs changed Loki's license from Apache-2.0 to AGPL-3.0 in 2023 — trajectory signal.)_

## Brief Description

Log aggregation system by Grafana Labs. Designed to work alongside Prometheus — same labels, same query patterns. Indexes only metadata (labels), not log content — making it lightweight compared to Elasticsearch. Visualised through Grafana.

## Architectural Role

Observability layer. Log storage and querying. Part of the PLG stack (Prometheus + Loki + Grafana). Promtail or Alloy collect logs from containers and systems and ship them to Loki.

## Technical Autonomy

- [x] Works without internet
- [x] Stores data locally (filesystem or S3-compatible)
- [x] Does not require external accounts
- [x] Allows data export (LogQL queries, direct filesystem access)
- [ ] Provides offline updates

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Clean stop; no permanent damage |
| Exit                  | ✅     | Log chunks stored on filesystem; queryable directly |
| Recoverability        | ✅     | Filesystem backup; stateless query layer |
| Visibility            | ✅     | AGPL-3.0, fully auditable |
| External Dependencies | ✅     | Runs fully self-contained |

## Configuration (Minimal)

```yaml
services:
  loki:
    image: grafana/loki:latest
    command: -config.file=/etc/loki/loki-config.yaml
    volumes:
      - ./loki-config.yaml:/etc/loki/loki-config.yaml
      - loki_data:/loki
    ports:
      - "3100:3100"

  promtail:
    image: grafana/promtail:latest
    command: -config.file=/etc/promtail/promtail-config.yaml
    volumes:
      - ./promtail-config.yaml:/etc/promtail/promtail-config.yaml
      - /var/log:/var/log:ro
      - /var/lib/docker/containers:/var/lib/docker/containers:ro

volumes:
  loki_data:
```

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Prometheus](prometheus.md) | A3 / T2 | Metrics not logs — complementary, not alternative |
| Elasticsearch | A3 / T1 | Full-text search, heavier, SSPL license (not OSI) |

---

## Trajectory

**Direction: mixed**

Loki was Apache-2.0 until 2023 when Grafana Labs changed it to AGPL-3.0 — the same move made for Grafana itself in 2021. The self-hosted version remains fully functional. Enterprise features (multi-tenancy at scale, SSO) are available in Grafana Cloud. Watch for further migration of features to the enterprise tier, consistent with the broader Grafana Labs pattern.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ⚠️ | Apache-2.0 → AGPL-3.0 in 2023; AGPL restricts embedding in proprietary products |
| Feature gating | ➖ | Core logging features remain open; enterprise = scale + SSO |
| Self-hosting | ✅ | Self-hosting well-supported; actively developed |
| Governance | ➖ | Grafana Labs controls direction; community contributions accepted |

---

## Sources

- **Website:** https://grafana.com/oss/loki
- **Documentation:** https://grafana.com/docs/loki/latest
- **Repository:** https://github.com/grafana/loki
- **Docker image:** grafana/loki
- **Community:** https://github.com/grafana/loki/discussions
