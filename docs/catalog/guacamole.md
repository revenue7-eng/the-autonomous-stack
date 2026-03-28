---
nav_exclude: false
title: "Apache Guacamole"
category: "applications/remote-access"
status: "stable"
license: "Apache-2.0"
source: "https://guacamole.apache.org"
repository: "https://github.com/apache/guacamole-server"
documentation: "https://guacamole.apache.org/doc/gug/"
docker_image: "guacamole/guacamole"
community: "https://lists.apache.org/list.html?user@guacamole.apache.org"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: ["postgresql"]
depended_by: []
critical_criteria: ["Pause", "Exit"]
trajectory: "stable"
parent: Technology Catalog
nav_order: 99
---

# Apache Guacamole

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Clientless remote desktop gateway. Access RDP, VNC, and SSH sessions through a web browser — no plugins, no client software. Apache Software Foundation project. Connect to any machine on your network from any device with a browser.

## Architectural Role

Remote access layer: browser-based gateway to all your machines. Unlike RustDesk which requires a client app on each device, Guacamole works from any browser. Ideal for accessing headless servers, Windows machines, and legacy systems.

## Technical Autonomy

- ✅ Works without internet (LAN access to internal machines)
- ✅ Stores data locally (connection configs, session recordings)
- ✅ Does not require external accounts
- ✅ Configuration exportable (database or XML)
- ✅ No external dependencies for core functionality

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅ | Stop container, active sessions end but no data lost. |
| Exit                  | ✅ | Connection configs in database or YAML. Portable. |
| Recoverability        | ✅ | Stateless gateway. Rebuild from config. |
| Visibility            | ✅ | Apache-2.0, ASF governance. |
| External Dependencies | ✅ | Fully self-contained. |

## Configuration (Minimal)

```yaml
services:
  guacd:
    image: guacamole/guacd
    container_name: guacd
    restart: unless-stopped

  guacamole:
    image: guacamole/guacamole
    container_name: guacamole
    ports:
      - "8080:8080"
    environment:
      GUACD_HOSTNAME: guacd
      GUACD_PORT: 4822
    depends_on:
      - guacd
    restart: unless-stopped
```

## Related Recipes

- [Minimal Autonomous Server](../recipes/minimal-server.md)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [RustDesk](rustdesk.md) | A3 / T2 | Native client, peer-to-peer. Better for desktop-to-desktop. |
| MeshCentral | A3 / T2 | Full remote management platform with web UI. More complex. |
| Chrome Remote Desktop | A0 / T0 | Google account required, cloud-dependent. |

---

## Trajectory

**Direction: stable.**

Apache Software Foundation project since 2016. ASF governance ensures community control. Steady development, no commercial pressure, no feature gating. The definition of stable open source.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | Apache-2.0, ASF project. Immutable. |
| Feature gating | ✅ | No paid tier. |
| Self-hosting | ✅ | Docker or manual install. Well documented. |
| Governance | ✅ | Apache Software Foundation. Community-governed. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [guacamole.apache.org](https://guacamole.apache.org)
- **Repository:** [github.com/apache/guacamole-server](https://github.com/apache/guacamole-server)
- **Docker image:** `guacamole/guacamole`
