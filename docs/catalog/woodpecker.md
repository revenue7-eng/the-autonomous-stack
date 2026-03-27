---
parent: "Technology Catalog"
nav_order: 99
title: "Woodpecker CI"
category: "applications/ci-cd"
status: "stable"
license: "Apache-2.0"
source: "https://github.com/woodpecker-ci/woodpecker"
repository: "https://github.com/woodpecker-ci/woodpecker"
documentation: "https://woodpecker-ci.org/docs/intro"
docker_image: "woodpeckerci/woodpecker-server"
community: "https://matrix.to/#/#woodpecker:matrix.org"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker", "forgejo"]
optional_deps: ["prometheus"]
depended_by: []
critical_criteria: ["Exit", "External Dependencies"]
---

# Woodpecker CI

> **TAS Score: S3/3 — D5/5 · A3 / T2**

## Brief Description

Community fork of Drone CI after Harness acquired it and moved it toward a commercial model. Lightweight, pipeline-as-code CI/CD. Native integration with Forgejo, Gitea, GitHub, GitLab. Agent-based architecture — runs pipelines in Docker containers.

## Architectural Role

Applications layer. CI/CD pipeline execution. Works alongside Forgejo or any Git host. Pipelines defined in YAML files in the repository — no vendor lock-in on configuration format.

## Technical Autonomy

- [x] Works without internet
- [x] Stores data locally (SQLite or PostgreSQL)
- [x] Does not require external accounts
- [x] Allows data export (pipeline configs are plain YAML in repo)
- [ ] Provides offline updates

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Clean stop; no permanent damage |
| Exit                  | ✅     | Pipeline configs are YAML files in your repo — fully portable |
| Recoverability        | ✅     | Database backup; stateless agents |
| Visibility            | ✅     | Apache-2.0, fully auditable |
| External Dependencies | ✅     | Runs fully self-contained |

## Configuration (Minimal)

```yaml
services:
  woodpecker-server:
    image: woodpeckerci/woodpecker-server:latest
    environment:
      WOODPECKER_OPEN: "true"
      WOODPECKER_HOST: https://ci.yourdomain.com
      WOODPECKER_FORGEJO: "true"
      WOODPECKER_FORGEJO_URL: https://git.yourdomain.com
      WOODPECKER_FORGEJO_CLIENT: your-oauth-client-id
      WOODPECKER_FORGEJO_SECRET: your-oauth-secret
      WOODPECKER_AGENT_SECRET: changeme
    volumes:
      - woodpecker_data:/var/lib/woodpecker
    ports:
      - "8000:8000"

  woodpecker-agent:
    image: woodpeckerci/woodpecker-agent:latest
    environment:
      WOODPECKER_SERVER: woodpecker-server:9000
      WOODPECKER_AGENT_SECRET: changeme
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock

volumes:
  woodpecker_data:
```

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Jenkins](jenkins.md) | A3 / T2 | More powerful, heavier, larger ecosystem |
| [Forgejo](forgejo.md) | A3 / T2 | Includes built-in Actions CI/CD |
| GitHub Actions | A0 / T1 | Cloud-only; vendor lock-in on syntax |

---

## Trajectory

**Direction: opening**

Woodpecker was created as a community fork of Drone CI after Harness acquired it in 2021 and began moving it toward a commercial model. Apache-2.0 licensed, community-governed, no corporate control. The project has grown rapidly since its fork with an active contributor base. A clear example of the open-source ecosystem self-correcting after a vendor lock-in attempt.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | Apache-2.0; forked to preserve open governance |
| Feature gating | ✅ | No paid tier; all features available |
| Self-hosting | ✅ | Self-hosting is the only deployment model |
| Governance | ✅ | Community-governed; no corporate control; active contributors |

---

## Sources

- **Website:** https://woodpecker-ci.org
- **Documentation:** https://woodpecker-ci.org/docs/intro
- **Repository:** https://github.com/woodpecker-ci/woodpecker
- **Docker image:** woodpeckerci/woodpecker-server
- **Community:** https://matrix.to/#/#woodpecker:matrix.org
