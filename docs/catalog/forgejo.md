---
nav_exclude: false
title: "Forgejo"
category: "applications/version-control"
status: "stable"
license: "MIT"
source: "https://forgejo.org"
repository: "https://codeberg.org/forgejo/forgejo"
documentation: "https://forgejo.org/docs/"
docker_image: "https://hub.docker.com/r/codebergorg/forgejo"
community: "https://matrix.to/#/#forgejo:matrix.org"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: ["postgresql"]
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
parent: Technology Catalog
nav_order: 99
---

# Forgejo

> **TAS Score: S3/3 -- D5/5** -- A3 / T2
> **Critical criteria for this category:** Exit, Recoverability.


## Brief Description

Self-hosted Git service with a focus on lightweight operation, open governance, and built-in CI/CD via Actions. A fork of Gitea.

## Architectural Role

Core service: provides version control, code hosting, issue tracking, and CI/CD pipelines for autonomous infrastructure.

## Technical Autonomy

* Works without internet (after initial setup)
* Stores data locally (SQLite, PostgreSQL, or filesystem)
* Does not require external accounts
* Allows data export (full database and repository dumps)
* Provides offline updates (manual upgrade, can be air-gapped)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments                                                         |
| --------------------- | ------ | ---------------------------------------------------------------- |
| Pause                 | Yes    | No auto-refresh or infinite feeds; user-controlled interaction.  |
| Exit                  | Yes    | Full data export (repos, issues, wiki). No vendor lock-in.       |
| Recoverability        | Yes    | Regular backups of repositories and database; rollback possible. |
| Visibility            | Yes    | Open source, fully transparent architecture.                     |
| External Dependencies | Yes    | None; can run completely offline.                                |

## Configuration (Minimal)

Example docker-compose.yml snippet:

```yaml
services:
  forgejo:
    image: codeberg.org/forgejo/forgejo:1.21
    ports:
      - "3000:3000"
      - "222:22"
    volumes:
      - ./forgejo-data:/data
    environment:
      - FORGEJO__server__DOMAIN=git.local
      - FORGEJO__server__SSH_PORT=222
```

## Related Recipes

*  [Minimal Autonomous Server](../recipes/minimal-server.md)  – uses Forgejo as version control component.

## Alternatives

* Gitea – similar, but Forgejo offers a more community-governed fork.
* GitLab – more features but heavier, requires more resources.
* Gogs – lighter but fewer features.

---

## Trajectory

**Direction: opening.**

Forgejo was created in 2022 as a community fork of Gitea after governance concerns arose when the Gitea organisation moved toward corporate control. Forgejo is governed by the Codeberg e.V. non-profit, uses MIT licence, and explicitly positions itself as a community-first alternative. The trajectory since inception has been consistently toward openness.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | MIT licence; forked explicitly to preserve open governance. |
| Feature gating | ✅ | No enterprise tier; all features available to all users. |
| Self-hosting | ✅ | Self-hosting is the only deployment model; improving with each release. |
| Governance | ✅ | Governed by Codeberg e.V. non-profit; community-driven decisions. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

* [Website](https://forgejo.org)

* [Documentation](https://forgejo.org/docs/)

* [Repository (Codeberg)](https://codeberg.org/forgejo/forgejo)

* [Docker image](https://hub.docker.com/r/codebergorg/forgejo)

* [Community (Matrix)](https://matrix.to/#/#forgejo:matrix.org)
