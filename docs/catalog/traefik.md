---
nav_exclude: false
title: "Traefik"
category: "network/proxy"
status: "stable"
license: "MIT"
source: "https://traefik.io"
repository: "https://github.com/traefik/traefik"
documentation: "https://doc.traefik.io/traefik/"
docker_image: "https://hub.docker.com/_/traefik"
community: "https://community.traefik.io"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: []
depended_by: []
critical_criteria: ["Pause"]
trajectory: "mixed"
parent: Technology Catalog
nav_order: 99
---

# Traefik

> **TAS Score: S3/3 -- D5/5** -- A3 / T2
> **Critical criteria for this category:** Pause.


## Brief Description

Modern reverse proxy and load balancer designed for microservices and container environments. Auto-discovers services from Docker, Kubernetes, and other providers. Handles SSL certificates automatically via Let's Encrypt.

## Architectural Role

Network layer: edge router that sits in front of all your services, handles HTTPS termination, routing, and load balancing. The front door of your self-hosted stack.

## Technical Autonomy

- ✅ Works without internet (routing and proxying are local; Let's Encrypt requires internet for certificate renewal)
- ✅ Stores data locally (configuration, certificates, access logs)
- ✅ Does not require external accounts
- ✅ Allows data export (configuration is YAML/TOML files, portable)
- ✅ Provides offline updates (manual upgrade via Docker)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status  | Comments |
| --------------------- | ------- | -------- |
| Pause                 | Yes     | Service can be stopped; upstream services remain but become unreachable from outside. |
| Exit                  | Yes     | Configuration is standard files. Can migrate to Nginx, Caddy, or any reverse proxy. |
| Recoverability        | Yes     | Configuration files can be version-controlled. Certificates can be backed up. |
| Visibility            | Yes     | Open source (MIT), fully auditable. Dashboard shows real-time routing. |
| External Dependencies | Partial | Core routing is fully local. Automatic HTTPS via Let's Encrypt requires internet. For air-gapped use, bring your own certificates. |

## Configuration (Minimal)

Example `docker-compose.yml` snippet:

```yaml
services:
  traefik:
    image: traefik:latest
    container_name: traefik
    ports:
      - "80:80"
      - "443:443"
      - "8080:8080"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - ./traefik-config:/etc/traefik
      - ./letsencrypt:/letsencrypt
    command:
      - "--api.dashboard=true"
      - "--providers.docker=true"
      - "--entrypoints.web.address=:80"
      - "--entrypoints.websecure.address=:443"
    restart: unless-stopped
```

## Related Recipes

* [Minimal Autonomous Server](../recipes/minimal-server.md) -- can be extended with Traefik as reverse proxy.

## Alternatives

* Nginx Proxy Manager -- GUI-based, easier for beginners, less flexible
* Caddy -- simpler configuration, automatic HTTPS, single binary
* Nginx -- manual configuration, most flexible, steepest learning curve
* HAProxy -- enterprise-grade load balancer, more complex

---

## Trajectory

**Direction: mixed.**

Traefik is MIT licenced and widely adopted. Traefik Labs also develops Traefik Enterprise (closed-source) with advanced features. The open-source version remains functional and well-maintained. The risk is gradual migration of useful features to the enterprise edition — this has been a slow trend in recent releases.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ➖ | MIT for OSS edition; unchanged. Enterprise edition is separate and proprietary. |
| Feature gating | ⚠️ | Some advanced features (API management, OIDC, advanced routing) are enterprise-only. |
| Self-hosting | ✅ | OSS self-hosting remains well-supported; no cloud dependency. |
| Governance | ➖ | Traefik Labs controls direction; community contributions accepted but roadmap is corporate-driven. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

* [Website](https://traefik.io)
* [Documentation](https://doc.traefik.io/traefik/)
* [Repository](https://github.com/traefik/traefik)
* [Docker image](https://hub.docker.com/_/traefik)
* [Community](https://community.traefik.io)
-e
