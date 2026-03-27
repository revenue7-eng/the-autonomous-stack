---
nav_exclude: false
title: "Node-RED"
parent: "Technology Catalog"
category: "applications/automation"
status: "stable"
license: "Apache-2.0"
source: "https://github.com/node-red/node-red"
repository: "https://github.com/node-red/node-red"
documentation: "https://nodered.org/docs"
docker_image: "nodered/node-red"
community: "https://discourse.nodered.org"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: ["docker"]
depended_by: []
critical_criteria: []
---

# Node-RED

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Flow-based visual automation tool built on Node.js. Originally created by IBM, now a JS Foundation / OpenJS Foundation project. Drag-and-drop editor for wiring together APIs, hardware, and services. Strong in IoT and home automation. Apache-2.0 licensed. 22,000+ GitHub stars.

## Architectural Role

Integration/automation layer: flow-based programming for event-driven applications. Strong in IoT, home automation, and API orchestration. Lighter and more flexible than n8n, but fewer pre-built SaaS integrations.

## Technical Autonomy

- [x] Works without internet — flows execute locally; external integrations require internet
- [x] Stores data locally — flows stored as JSON files on disk
- [x] Does not require external accounts
- [x] Allows data export — flows are JSON files, fully portable between any Node-RED instance
- [x] Provides offline updates — npm package or Docker image, updated manually

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Stop the process. Flows stop. Resume without loss. |
| Exit                  | ✅     | Flows are JSON files. Copy them anywhere. Zero lock-in. |
| Recoverability        | ✅     | JSON flow files + any connected databases. Trivial backup and restore. |
| Visibility            | ✅     | Fully open source (Apache-2.0). OpenJS Foundation governance. |
| External Dependencies | ✅     | Requires Node.js only. No external services. Runs on anything from Raspberry Pi to cloud. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

```yaml
services:
  node-red:
    image: nodered/node-red:latest
    ports:
      - 1880:1880
    volumes:
      - ./node-red-data:/data
    restart: unless-stopped
```

Runs on ~128 MB RAM. Works on Raspberry Pi. No database required — flows stored as flat JSON files.

## Related Recipes

- [Minimal Autonomous Server](../recipes/minimal-server.html)
- [Privacy-First Homelab](../recipes/privacy-first-homelab.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [n8n](n8n.html) | A3 / T2 | More SaaS integrations, Zapier-like UX, source-available license |
| [Zapier](zapier.html) | A0 / T0 | No-code, 7000+ apps, fully proprietary, no selfhosting |

---

## Trajectory

**Direction: stable/opening**

Originally IBM project, now under OpenJS Foundation. Apache-2.0 license since inception — no changes. Active community with 4,000+ contributed node packages. No corporate pressure to monetize. Foundation governance provides long-term stability. One of the most mature selfhosted automation tools.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | Apache-2.0. No changes. Foundation-governed. |
| Feature gating | ✅ | All features free. No paid tier. Community nodes are free. |
| Self-hosting | ✅ | Selfhosting is the only deployment model. Runs on anything. |
| Governance | ✅ | OpenJS Foundation. Community-driven. No single-company control. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** https://nodered.org
- **Documentation:** https://nodered.org/docs
- **Repository:** https://github.com/node-red/node-red
- **Docker image:** nodered/node-red
- **Community:** https://discourse.nodered.org
