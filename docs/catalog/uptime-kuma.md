---
nav_exclude: false
title: "Uptime Kuma"
category: "observability/monitoring"
status: "stable"
license: "MIT"
source: "https://uptime.kuma.pet"
repository: "https://github.com/louislam/uptime-kuma"
documentation: "https://github.com/louislam/uptime-kuma/wiki"
docker_image: "https://hub.docker.com/r/louislam/uptime-kuma"
community: "https://github.com/louislam/uptime-kuma/issues"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: []
depended_by: []
critical_criteria: ["Pause"]
parent: Technology Catalog
nav_order: 99
---

# Uptime Kuma

> **TAS Score: S3/3 -- D5/5** -- A3 / T2
> **Critical criteria for this category:** Pause.


## Brief Description

Self-hosted monitoring tool that tracks the availability of websites,
services, and network endpoints. Provides a clean dashboard,
notifications, and status pages without cloud dependencies.

## Architectural Role

Observability layer: monitors your services and alerts you when
something goes wrong.

## Technical Autonomy

-   Works without internet (monitors local services)
-   Stores data locally (SQLite database)
-   Does not require external accounts
-   Allows data export (SQLite file, config export)
-   Provides offline updates (manual via Docker)

## Philosophical Assessment (whose.world criteria)

  -----------------------------------------------------------------------
  Criterion                  Status              Comments
  -------------------------- ------------------- ------------------------
  Pause                      Yes                 Monitoring can be
                                                 paused; alerts are
                                                 user-controlled.

  Exit                       Yes                 Data can be exported;
                                                 you can stop using it at
                                                 any time.

  Recoverability             Yes                 SQLite database can be
                                                 backed up and restored.

  Visibility                 Yes                 Open source, fully
                                                 transparent.

  External Dependencies      Yes                 None; runs entirely
                                                 offline.
  -----------------------------------------------------------------------

## Configuration (Minimal)

Example docker-compose.yml snippet:

``` yaml
services:
  uptime-kuma:
    image: louislam/uptime-kuma:1
    container_name: uptime-kuma
    ports:
      - "3001:3001"
    volumes:
      - ./kuma-data:/app/data
    restart: unless-stopped
```

## Related Recipes

- [Minimal Autonomous Server](../recipes/minimal-server.md) -- includes Uptime Kuma for monitoring.

## Alternatives

-   Grafana + Prometheus -- more complex and resource-heavy
-   Nagios -- older and harder to configure
-   Healthchecks.io -- cloud-based (not autonomous)

---

## Trajectory

**Direction: stable.**

Uptime Kuma is MIT licenced, maintained by a single primary author (louislam) with a large community of contributors. No commercial entity, no enterprise tier, no cloud service. Rapid development since 2021. Single-maintainer dependency is the main governance risk.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | MIT; no changes since launch. |
| Feature gating | ✅ | No paid tier; all features free. |
| Self-hosting | ✅ | Self-hosting only; no cloud component. |
| Governance | ➖ | Single primary maintainer (louislam); active community; no foundation backing. Bus-factor risk. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- [Website](https://uptime.kuma.pet)

- [Documentation](https://github.com/louislam/uptime-kuma/wiki)

- [Repository](https://github.com/louislam/uptime-kuma)

- [Docker image](https://hub.docker.com/r/louislam/uptime-kuma)

- [Community](https://github.com/louislam/uptime-kuma/issues)
-e
