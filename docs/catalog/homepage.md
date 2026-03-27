---
nav_exclude: false
title: "Homepage"
category: "applications/cloud"
status: "stable"
license: "GPL-3.0"
source: "https://gethomepage.dev"
repository: "https://github.com/gethomepage/homepage"
documentation: "https://gethomepage.dev"
docker_image: "ghcr.io/gethomepage/homepage"
community: "https://github.com/gethomepage/homepage/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: []
depended_by: []
critical_criteria: ["Pause"]
trajectory: "opening"
parent: Technology Catalog
nav_order: 99
---

# Homepage

> **TAS Score: S3/3 — D5/5** — A3 / T2
> **Critical criteria for this category:** Pause.


## Brief Description

Highly customizable, self-hosted application dashboard with Docker auto-discovery and over 100 service integrations. Fast, fully static frontend with YAML-based configuration. A single landing page for all your self-hosted services.

## Architectural Role

Presentation layer: a read-only dashboard that aggregates status and information from your other services. Does not store data itself — purely a visualization and navigation tool. Sits behind your reverse proxy as the entry point to your homelab.

## Technical Autonomy

- ✅ Works without internet (all rendering is local; some widgets like weather need internet)
- ✅ Stores data locally (configuration is YAML files on disk)
- ✅ Does not require external accounts
- ✅ Allows data export (configuration is plain YAML, fully portable)
- ✅ Provides offline updates (Docker image pull and replace)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status  | Comments |
| --------------------- | ------- | -------- |
| Pause                 | Yes     | Dashboard can be stopped. All underlying services continue running independently. |
| Exit                  | Yes     | Configuration is YAML files. Can migrate to Dashy, Homer, or any alternative. Services are unaffected. |
| Recoverability        | Yes     | Stateless — just config files. Backup is a single directory copy. |
| Visibility            | Yes     | Open source (GPL-3.0), fully auditable. |
| External Dependencies | None    | Core dashboard is fully local. Optional weather/search widgets use external APIs. |

## Configuration (Minimal)

```yaml
services:
  homepage:
    image: ghcr.io/gethomepage/homepage:latest
    container_name: homepage
    environment:
      HOMEPAGE_ALLOWED_HOSTS: homepage.local
    ports:
      - "3000:3000"
    volumes:
      - ./config/homepage:/app/config
      - /var/run/docker.sock:/var/run/docker.sock:ro
    restart: unless-stopped
```

Example `services.yaml`:

```yaml
- Infrastructure:
    - Traefik:
        icon: traefik.png
        href: https://traefik.local
        description: Reverse proxy
    - AdGuard Home:
        icon: adguard-home.png
        href: https://adguard.local
        description: DNS filtering

- Media:
    - Jellyfin:
        icon: jellyfin.png
        href: https://jellyfin.local
        description: Media server
```

## Alternatives

* Dashy — more feature-rich, heavier, MIT licensed
* Homer — simpler, static YAML-based, Apache-2.0
* Flame — easiest setup, GUI-based editing
* Heimdall — PHP-based, visual app organizer
* Homarr — modern UI, drag-and-drop editing

---

## Trajectory

**Direction: opening.**

Homepage is GPL-3.0 licensed with active development and a growing community. No enterprise edition, no paid features, no telemetry. The project accepts contributions and has a transparent roadmap. One of the fastest-growing self-hosted dashboard projects.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | GPL-3.0; unchanged. Strong copyleft ensures code stays open. |
| Feature gating | ✅ | No paid tier. All features are free. |
| Self-hosting | ✅ | Designed exclusively for self-hosting. No cloud version. |
| Governance | ✅ | Community-driven. Active GitHub discussions. Transparent development. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

* [Website](https://gethomepage.dev)
* [Documentation](https://gethomepage.dev)
* [Repository](https://github.com/gethomepage/homepage)
* [Docker image](https://ghcr.io/gethomepage/homepage)
* [Community](https://github.com/gethomepage/homepage/discussions)
