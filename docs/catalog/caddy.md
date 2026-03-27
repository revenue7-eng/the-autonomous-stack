---
nav_exclude: false
title: "Caddy"
category: "network/proxy"
status: "stable"
license: "Apache-2.0"
source: "https://caddyserver.com"
repository: "https://github.com/caddyserver/caddy"
documentation: "https://caddyserver.com/docs/"
docker_image: "https://hub.docker.com/_/caddy"
community: "https://caddy.community"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Pause"]
trajectory: "opening"
parent: Technology Catalog
nav_order: 99
---

# Caddy

> **TAS Score: S3/3 — D5/5** — A3 / T2
> **Critical criteria for this category:** Pause.


## Brief Description

Fast, extensible, cross-platform web server with automatic HTTPS. Single binary, zero dependencies, automatic TLS certificates via Let's Encrypt or ZeroSSL. Simpler configuration than Nginx or Traefik through the Caddyfile format.

## Architectural Role

Network layer: reverse proxy and web server that handles HTTPS termination, routing, and static file serving. Sits in front of your self-hosted services with automatic certificate management.

## Technical Autonomy

- ✅ Works without internet (proxying and serving are local; Let's Encrypt requires internet for certificate renewal)
- ✅ Stores data locally (configuration, certificates, private keys)
- ✅ Does not require external accounts
- ✅ Allows data export (configuration is Caddyfile or JSON, fully portable)
- ✅ Provides offline updates (manual upgrade by replacing single binary)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status  | Comments |
| --------------------- | ------- | -------- |
| Pause                 | Yes     | Service can be stopped; upstream services remain but become unreachable from outside. |
| Exit                  | Yes     | Configuration is standard files. Can migrate to Nginx, Traefik, or any reverse proxy. |
| Recoverability        | Yes     | Single binary + config file. Certificates can be backed up from data directory. |
| Visibility            | Yes     | Open source (Apache-2.0), fully auditable. |
| External Dependencies | Partial | Core proxying is fully local. Automatic HTTPS via ACME requires internet. For air-gapped use, bring your own certificates. |

## Configuration (Minimal)

Example `Caddyfile`:

```
example.com {
    reverse_proxy localhost:8080
}

git.example.com {
    reverse_proxy localhost:3000
}
```

Docker deployment:

```yaml
services:
  caddy:
    image: caddy:latest
    container_name: caddy
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./Caddyfile:/etc/caddy/Caddyfile
      - caddy_data:/data
      - caddy_config:/config
    restart: unless-stopped
```

## Related Recipes

* [Minimal Autonomous Server](../recipes/minimal-server.md) — Caddy can replace Nginx Proxy Manager as the reverse proxy.

## Alternatives

* Nginx Proxy Manager — GUI-based, easier for beginners, less flexible
* Traefik — more complex, better Docker integration, auto-discovery
* Nginx — manual configuration, most flexible, steepest learning curve
* HAProxy — enterprise-grade load balancer, more complex

---

## Trajectory

**Direction: opening.**

Caddy is Apache-2.0 licensed with no enterprise-only gating of features. All features are free for everyone. The project is actively developed with strong focus on security (first server to support automatic ECH, post-quantum key exchange). No signs of feature gating or license changes.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | Apache-2.0; unchanged since v2. Previous EULA controversy (v1 era) fully resolved. |
| Feature gating | ✅ | No enterprise edition. All features are free. |
| Self-hosting | ✅ | Single binary, zero dependencies, designed for self-hosting. |
| Governance | ✅ | Open development on GitHub. Community contributions actively accepted. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

* [Website](https://caddyserver.com)
* [Documentation](https://caddyserver.com/docs/)
* [Repository](https://github.com/caddyserver/caddy)
* [Docker image](https://hub.docker.com/_/caddy)
* [Community](https://caddy.community)
