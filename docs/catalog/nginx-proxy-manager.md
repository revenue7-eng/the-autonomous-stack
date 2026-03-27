---
tags: [proxy, network, https, gui]
title: "Nginx Proxy Manager"
category: "network/proxy"
status: "stable"
license: "MIT"
source: "https://nginxproxymanager.com"
repository: "https://github.com/NginxProxyManager/nginx-proxy-manager"
documentation: "https://nginxproxymanager.com/guide/"
docker_image: "https://hub.docker.com/r/jc21/nginx-proxy-manager"
community: "https://github.com/NginxProxyManager/nginx-proxy-manager/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: []
depended_by: []
critical_criteria: ["Pause"]
parent: Technology Catalog
nav_order: 99
---

# Nginx Proxy Manager

> **TAS Score: S3/3 -- D5/5** -- A3 / T2
> **Critical criteria for this category:** Pause.


## Brief Description

GUI-based reverse proxy built on Nginx. Manage proxy hosts, SSL certificates, redirects, and access lists through a clean web interface -- no manual Nginx config files needed.

## Architectural Role

Network layer: reverse proxy with a visual management interface. Ideal for homelabs and small deployments where simplicity matters more than advanced routing.

## Technical Autonomy

- ✅ Works without internet (proxying is local; Let's Encrypt needs internet for certificate renewal)
- ✅ Stores data locally (SQLite database, certificates, Nginx configs)
- ✅ Does not require external accounts
- ✅ Allows data export (database and config files can be backed up)
- ✅ Provides offline updates (manual upgrade via Docker)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status  | Comments |
| --------------------- | ------- | -------- |
| Pause                 | Yes     | Service can be stopped; upstream services remain but become unreachable from outside. |
| Exit                  | Yes     | Generated Nginx configs are standard. Can migrate to raw Nginx or Traefik. |
| Recoverability        | Yes     | SQLite database and certificate files can be backed up and restored. |
| Visibility            | Yes     | Open source (MIT), fully auditable. |
| External Dependencies | Partial | Core proxying is local. Let's Encrypt certificate renewal requires internet. |

## Configuration (Minimal)

Example `docker-compose.yml` snippet:

```yaml
services:
  npm:
    image: jc21/nginx-proxy-manager:latest
    container_name: nginx-proxy-manager
    ports:
      - "80:80"
      - "443:443"
      - "81:81"
    volumes:
      - ./npm-data:/data
      - ./npm-letsencrypt:/etc/letsencrypt
    restart: unless-stopped
```

Default login: admin@example.com / changeme

## Related Recipes

* [Minimal Autonomous Server](../recipes/minimal-server.md) -- can be extended with Nginx Proxy Manager for easy HTTPS.

## Alternatives

* Traefik -- more powerful, auto-discovery, no GUI by default
* Caddy -- simpler config, automatic HTTPS, no GUI
* Nginx (raw) -- maximum flexibility, manual configuration

---

## Trajectory

**Direction: stable.**

Nginx Proxy Manager is MIT licenced, community-maintained, and has no commercial entity behind it. Development is active. No monetisation pressure, no enterprise tier. The main risk is dependency on a small maintainer team.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | MIT licence; no changes. |
| Feature gating | ✅ | No paid tier; all features are free. |
| Self-hosting | ✅ | Self-hosting only; no cloud service. |
| Governance | ➖ | Small maintainer team; active but no formal governance structure. Single-maintainer risk is moderate. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

* [Website](https://nginxproxymanager.com)
* [Documentation](https://nginxproxymanager.com/guide/)
* [Repository](https://github.com/NginxProxyManager/nginx-proxy-manager)
* [Docker image](https://hub.docker.com/r/jc21/nginx-proxy-manager)
* [Community](https://github.com/NginxProxyManager/nginx-proxy-manager/discussions)
-e
