---
nav_exclude: false
trajectory: "mixed"
parent: "Technology Catalog"
nav_order: 99
title: "Netdata"
category: "observability/monitoring"
status: "stable"
license: "GPL-3.0"
source: "https://github.com/netdata/netdata"
repository: "https://github.com/netdata/netdata"
documentation: "https://learn.netdata.cloud"
docker_image: "netdata/netdata"
community: "https://community.netdata.cloud"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: ["prometheus", "grafana"]
depended_by: []
critical_criteria: ["External Dependencies"]
---

# Netdata

> **TAS Score: S3/3 — D3/5 · A3 / T2**
> _(D3 not D5: Trajectory ⚠️ — agent increasingly configured for Netdata Cloud by default. Hidden cost ⚠️ — opt-out telemetry and cloud connectivity enabled by default.)_

## Brief Description

Real-time performance monitoring with zero configuration. Auto-detects hundreds of applications and services. 1-second granularity. Built-in dashboards, ML-based anomaly detection. Lightweight agent runs on any Linux system.

## Architectural Role

Observability layer. Real-time monitoring focused on individual nodes. Can run standalone (per-node dashboard) or feed into Prometheus/Grafana for fleet-wide visibility.

## Technical Autonomy

- [x] Works without internet
- [x] Stores data locally
- [x] Does not require external accounts
- [x] Allows data export (Prometheus endpoint, OpenMetrics)
- [ ] Provides offline updates

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Clean stop, no permanent damage |
| Exit                  | ✅     | Prometheus endpoint; data exportable |
| Recoverability        | ✅     | Agent is stateless; config-as-code |
| Visibility            | ✅     | GPL-3.0, fully auditable |
| External Dependencies | ⚠️     | Cloud connectivity and telemetry enabled by default; requires explicit opt-out |

## Configuration (Minimal)

```yaml
services:
  netdata:
    image: netdata/netdata:latest
    pid: host
    network_mode: host
    cap_add:
      - SYS_PTRACE
      - SYS_ADMIN
    security_opt:
      - apparmor:unconfined
    volumes:
      - ./netdataconfig:/etc/netdata
      - netdatalib:/var/lib/netdata
      - netdatacache:/var/cache/netdata
      - /:/host/root:ro,rslave
      - /etc/passwd:/host/etc/passwd:ro
      - /etc/group:/host/etc/group:ro
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
    environment:
      - DO_NOT_TRACK=1  # disable telemetry

volumes:
  netdatalib:
  netdatacache:
```

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Prometheus](prometheus.md) | A3 / T2 | Pull-based metrics, better for fleet monitoring |
| [Zabbix](zabbix.md) | A3 / T2 | Enterprise-grade, heavier, more configurable |
| [Uptime Kuma](uptime-kuma.md) | A3 / T2 | Simpler — uptime/availability only |

---

## Trajectory

**Direction: mixed**

Netdata launched Netdata Cloud in 2020 and has been increasingly integrating the agent with cloud features. Since 2022, the agent ships with cloud connectivity and telemetry enabled by default — requiring explicit opt-out. New features (alert notification routing, dashboards) are being developed cloud-first. The GPL-3.0 core remains open, but the default experience is pushing toward cloud dependency.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | GPL-3.0; no changes |
| Feature gating | ⚠️ | Alert routing, dashboards, ML features increasingly cloud-first |
| Self-hosting | ⚠️ | Cloud opt-out required; default config connects to Netdata Cloud |
| Governance | ⚠️ | VC-backed; commercial focus on Netdata Cloud growing |

---

## Sources

- **Website:** https://www.netdata.cloud
- **Documentation:** https://learn.netdata.cloud/docs/netdata-agent
- **Repository:** https://github.com/netdata/netdata
- **Docker image:** netdata/netdata
- **Community:** https://community.netdata.cloud
