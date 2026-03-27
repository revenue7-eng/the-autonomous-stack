---
tags: [identity, sso, auth, mfa, ldap]
title: "Authentik"
category: "identity/auth"
status: "stable"
license: "Apache-2.0"
source: "https://goauthentik.io"
repository: "https://github.com/goauthentik/authentik"
documentation: "https://docs.goauthentik.io"
docker_image: "https://hub.docker.com/r/goauthentik/authentik"
community: "https://github.com/goauthentik/authentik/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker", "postgresql"]
optional_deps: ["redis"]
depended_by: []
critical_criteria: ["Pause", "Exit"]
parent: Technology Catalog
nav_order: 99
---

# Authentik

> **TAS Score: S3/3 -- D5/5** -- A3 / T2
> **Critical criteria for this category:** Pause, Exit.


## Brief Description

Open-source identity provider focused on flexibility and security. Supports SSO, MFA, LDAP, OAuth2, OIDC, and more — all without external dependencies.

## Architectural Role

Identity layer: central authentication and authorization for your self-hosted services.

## Technical Autonomy

* Works without internet (after initial setup)
* Stores data locally (PostgreSQL, Redis, files)
* Does not require external accounts
* Allows data export (database and config backups)
* Provides offline updates (manual upgrade via packages or Docker)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments                                                          |
| --------------------- | ------ | ----------------------------------------------------------------- |
| Pause                 | Yes    | Services can be stopped; authentication requests fail gracefully. |
| Exit                  | Yes    | All user data can be exported; you can migrate to another IdP.    |
| Recoverability        | Yes    | Database and configuration can be backed up and restored.         |
| Visibility            | Yes    | Open source, full documentation.                                  |
| External Dependencies | Yes    | None; runs entirely offline.                                      |

## Configuration (Minimal)

Example docker-compose.yml snippet:

```yaml
services:
  postgresql:
    image: postgres:15
    volumes:
      - ./postgres-data:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: authentik
      POSTGRES_USER: authentik
      POSTGRES_PASSWORD: change-me

  redis:
    image: redis:alpine
    command: --save 60 1
    volumes:
      - ./redis-data:/data

  authentik:
    image: ghcr.io/goauthentik/server:latest
    ports:
      - "9000:9000"
      - "9443:9443"
    environment:
      AUTHENTIK_SECRET_KEY: change-me
      AUTHENTIK_POSTGRESQL__HOST: postgresql
      AUTHENTIK_POSTGRESQL__USER: authentik
      AUTHENTIK_POSTGRESQL__PASSWORD: change-me
      AUTHENTIK_REDIS__HOST: redis
    volumes:
      - ./authentik-media:/media
    depends_on:
      - postgresql
      - redis
```

## Related Recipes

* [Minimal Autonomous Server](../recipes/minimal-server.md) – can be extended with Authentik for unified auth.

## Alternatives

* Keycloak – more complex, heavier, still open source
* Authelia – lightweight, but less feature-rich
* Zitadel – cloud-native, requires external database

---

## Trajectory

**Direction: stable.**

Authentik uses a dual-license model: MIT for the core, and a separate enterprise license for advanced features (RBAC, support SLAs). The split is clean — enterprise features are additive, not replacements for community functionality. The project is actively developed and self-hosting is a first-class use case.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ➖ | MIT for core; enterprise license for additive features only. |
| Feature gating | ➖ | Enterprise tier adds features on top — does not remove community functionality. |
| Self-hosting | ✅ | Self-hosting is the primary deployment model; documentation is thorough. |
| Governance | ➖ | Maintained by Authentik Security Inc.; community PRs accepted actively. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

* [Website](https://goauthentik.io)

* [Documentation](https://docs.goauthentik.io)

* [Repository](https://github.com/goauthentik/authentik)

* [Docker image](https://hub.docker.com/r/goauthentik/authentik)

* [Community](https://github.com/goauthentik/authentik/discussions)
