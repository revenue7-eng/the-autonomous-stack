---
nav_exclude: false
title: "Authelia"
category: "identity/auth"
status: "stable"
license: "Apache-2.0"
source: "https://www.authelia.com"
repository: "https://github.com/authelia/authelia"
documentation: "https://www.authelia.com/docs/"
docker_image: "authelia/authelia"
community: "https://discord.authelia.com"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: ["redis"]
depended_by: []
critical_criteria: ["Pause", "Recoverability"]
trajectory: "opening"
parent: Technology Catalog
nav_order: 99
---

# Authelia

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Lightweight authentication and authorization server. Provides SSO (single sign-on), two-factor authentication, and access control for your self-hosted services via reverse proxy integration. Simpler and lighter than Authentik — single binary, no database required for basic setup.

## Architectural Role

Identity layer: sits behind your reverse proxy (Caddy, Traefik, Nginx) and protects services with authentication. One login for all your apps. Supports TOTP, WebAuthn, push notifications for 2FA. LDAP and file-based user backends.

## Technical Autonomy

- ✅ Works without internet
- ✅ Stores data locally (YAML config + SQLite or file-based)
- ✅ Does not require external accounts
- ✅ Configuration is YAML files — version-controllable, portable
- ✅ No database required for basic setup (file-based users)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅ | Stop Authelia, services become unprotected (pass-through) or blocked, depending on proxy config. |
| Exit                  | ✅ | User config is YAML. Remove Authelia, reconfigure proxy. |
| Recoverability        | ✅ | Config files + optional SQLite. Simple backup. |
| Visibility            | ✅ | Apache-2.0. Clean Go codebase. |
| External Dependencies | ✅ | Fully self-contained. Redis optional for HA. |

## Configuration (Minimal)

```yaml
services:
  authelia:
    image: authelia/authelia
    container_name: authelia
    ports:
      - "9091:9091"
    volumes:
      - ./config/authelia:/config
    environment:
      - TZ=UTC
    restart: unless-stopped
```

## Related Recipes

- [Minimal Autonomous Server](../recipes/minimal-server.md) — lighter alternative to Authentik

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Authentik](authentik.md) | A3 / T2 | Full identity provider. More features, more complex. PostgreSQL required. TAS recommended. |
| Keycloak | A3 / T2 | Enterprise-grade. Java-based. Very heavy for homelab use. |
| Caddy Security | A3 / T2 | Auth plugin for Caddy. Simpler but less flexible. |

---

## Trajectory

**Direction: opening.**

Authelia has grown significantly as the lightweight alternative to heavy identity providers. Apache-2.0, active development, growing feature set without complexity bloat. OpenID Connect support added, making it a viable SSO provider.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | Apache-2.0, unchanged. |
| Feature gating | ✅ | No paid tier. |
| Self-hosting | ✅ | Single binary or Docker. Minimal resource usage. |
| Governance | ✅ | Community-driven, multiple maintainers. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [authelia.com](https://www.authelia.com)
- **Repository:** [github.com/authelia/authelia](https://github.com/authelia/authelia)
- **Docker image:** `authelia/authelia`
