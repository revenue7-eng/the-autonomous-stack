---
tags: [git, version-control, code, gitea-alternative]
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
parent: Technology Catalog
nav_order: 12
---

# Forgejo

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

## Sources

* [Website](https://forgejo.org)

* [Documentation](https://forgejo.org/docs/)

* [Repository (Codeberg)](https://codeberg.org/forgejo/forgejo)

* [Docker image](https://hub.docker.com/r/codebergorg/forgejo)

* [Community (Matrix)](https://matrix.to/#/#forgejo:matrix.org)

## Trajectory
**Opening — community governance.**

Forgejo was created in 2022 as a community fork of Gitea after concerns that Gitea Ltd was moving toward a more corporate model. It is hosted on Codeberg, governed by a non-profit, and has no commercial entity behind it. The fork was a direct response to trajectory concerns about Gitea.

This makes Forgejo one of the clearest examples of a project born from a closing trajectory being replaced by an opening one. Direction: **stable opening**. The main risk is sustainability — small community, no commercial backing.
