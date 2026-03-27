---
nav_exclude: false
title: "Home Assistant"
category: "applications/automation"
status: "stable"
license: "Apache-2.0"
source: "https://www.home-assistant.io"
repository: "https://github.com/home-assistant/core"
documentation: "https://www.home-assistant.io/docs/"
docker_image: "https://hub.docker.com/r/homeassistant/home-assistant"
community: "https://community.home-assistant.io"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: []
depended_by: []
critical_criteria: ["Recoverability"]
trajectory: "stable"
parent: Technology Catalog
nav_order: 99
---

# Home Assistant

> **TAS Score: S3/3 -- D5/5** -- A3 / T2
> **Critical criteria for this category:** Recoverability.


## Brief Description

Open-source home automation platform that puts local control and privacy first. Supports 2000+ integrations for smart home devices -- lights, sensors, locks, cameras, climate -- all managed from a single dashboard without cloud dependencies.

## Architectural Role

Applications layer: central hub for smart home automation. Replaces Google Home, Amazon Alexa, and Apple HomeKit as the control plane for IoT devices. Runs locally, processes automations locally.

## Technical Autonomy

- ✅ Works without internet (local automations, local device control, local dashboard)
- ✅ Stores data locally (configuration, history, recorder database)
- ✅ Does not require external accounts (some integrations may require vendor accounts for their devices)
- ✅ Allows data export (configuration is YAML, database is SQLite/PostgreSQL, full backup built in)
- ✅ Provides offline updates (manual upgrade via Docker or OS image)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status  | Comments |
| --------------------- | ------- | -------- |
| Pause                 | Yes     | Service can be stopped; devices continue in their last state. |
| Exit                  | Yes     | Configuration is YAML files. Database is standard. No vendor lock-in at the platform level. |
| Recoverability        | Yes     | Built-in snapshots and backups. Configuration versioning via Git. |
| Visibility            | Yes     | Open source (Apache-2.0), fully auditable. Automations are transparent YAML. |
| External Dependencies | Partial | Home Assistant itself needs no cloud. But individual device integrations may depend on vendor clouds (Nest, Ring, etc). Choose local-protocol devices (Zigbee, Z-Wave, Matter) for full autonomy. |

## Configuration (Minimal)

Example `docker-compose.yml` snippet:

```yaml
services:
  homeassistant:
    image: homeassistant/home-assistant:latest
    container_name: homeassistant
    network_mode: host
    volumes:
      - ./ha-config:/config
    restart: unless-stopped
```

## Related Recipes

* [Minimal Autonomous Server](../recipes/minimal-server.md) -- can be extended with Home Assistant for home automation.

## Alternatives

* OpenHAB -- similar, Java-based, steeper learning curve
* Domoticz -- lighter, fewer integrations
* Google Home / Amazon Alexa -- cloud-dependent, A0/T0

## Trajectory

**Direction: opening.**

Home Assistant has consistently moved toward local control and away from cloud dependencies. Matter protocol integration strengthens local-first device communication. The project rejected acquisition offers and remains community-governed under the Open Home Foundation. Nabu Casa monetises through optional cloud subscription — no features are gated.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | Apache-2.0; no changes. Open Home Foundation holds the project. |
| Feature gating | ✅ | Nabu Casa Cloud is optional; no local features require subscription. |
| Self-hosting | ✅ | Local-first is the stated mission; Matter/Thread improve offline capability. |
| Governance | ✅ | Open Home Foundation (non-profit) governs the project; community-driven. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

## Sources

* [Website](https://www.home-assistant.io)
* [Documentation](https://www.home-assistant.io/docs/)
* [Repository](https://github.com/home-assistant/core)
* [Docker image](https://hub.docker.com/r/homeassistant/home-assistant)
* [Community](https://community.home-assistant.io)
