---
tags: [passwords, security, bitwarden, selfhosted]
title: "Vaultwarden"
category: "security/passwords"
status: "stable"
license: "AGPL-3.0"
source: "https://github.com/dani-garcia/vaultwarden"
repository: "https://github.com/dani-garcia/vaultwarden"
documentation: "https://github.com/dani-garcia/vaultwarden/wiki"
docker_image: "https://hub.docker.com/r/vaultwarden/server"
community: "https://github.com/dani-garcia/vaultwarden/discussions"
autonomy_level: "A3"
transparency_level: "T2"
parent: Technology Catalog
nav_order: 19
---

# Vaultwarden

## Brief Description

Lightweight, self-hosted implementation of the Bitwarden password manager API. Compatible with all official Bitwarden clients (browser, mobile, desktop, CLI) but runs entirely on your hardware with minimal resources.

## Architectural Role

Security layer: centralised password and secrets management for individuals and teams. Replaces Bitwarden Cloud, LastPass, 1Password -- with full data ownership.

## Technical Autonomy

- ✅ Works without internet (after initial setup; clients sync when server is reachable)
- ✅ Stores data locally (SQLite or PostgreSQL, encrypted vault)
- ✅ Does not require external accounts
- ✅ Allows data export (Bitwarden-compatible JSON/CSV export from clients)
- ✅ Provides offline updates (manual upgrade via Docker)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
| --------------------- | ------ | -------- |
| Pause                 | Yes    | Server can be stopped; clients retain cached vault offline. |
| Exit                  | Yes    | Standard Bitwarden export format. Can migrate to official Bitwarden or any compatible server. |
| Recoverability        | Yes    | Database backups. Vault is encrypted; backup the SQLite file and you have everything. |
| Visibility            | Yes    | Open source (AGPL-3.0), fully auditable. |
| External Dependencies | Yes    | No mandatory external services. Push notifications to mobile require Bitwarden's push relay, but this is optional. |

## Configuration (Minimal)

Example `docker-compose.yml` snippet:

```yaml
services:
  vaultwarden:
    image: vaultwarden/server:latest
    container_name: vaultwarden
    ports:
      - "8222:80"
    volumes:
      - ./vw-data:/data
    environment:
      SIGNUPS_ALLOWED: "false"
    restart: unless-stopped
```

Important: put behind a reverse proxy with HTTPS for production use.

## Related Recipes

* [Minimal Autonomous Server](../recipes/minimal-server.md) -- can be extended with Vaultwarden for password management.

## Alternatives

* Bitwarden (official server) -- heavier, requires more resources, but officially supported
* KeePass/KeePassXC -- local-only, no sync built in (pair with Syncthing)
* 1Password / LastPass -- cloud-dependent, A0/T0

## Sources

* [Repository](https://github.com/dani-garcia/vaultwarden)
* [Documentation](https://github.com/dani-garcia/vaultwarden/wiki)
* [Docker image](https://hub.docker.com/r/vaultwarden/server)
* [Community](https://github.com/dani-garcia/vaultwarden/discussions)

## Trajectory
**Stable, but structurally dependent.**

Vaultwarden is an unofficial reimplementation of the Bitwarden server API. It is not affiliated with Bitwarden Inc. and exists in a grey zone: it depends on Bitwarden's clients remaining compatible with its API.

The risk is not Vaultwarden itself — the project is clean, well-maintained, and open source. The risk is Bitwarden. If Bitwarden changes its API in a way that breaks compatibility (intentionally or not), Vaultwarden users are affected. Bitwarden has not moved against Vaultwarden, but the dependency is structural.

Rate: **stable**, but watch Bitwarden's trajectory, not Vaultwarden's.
