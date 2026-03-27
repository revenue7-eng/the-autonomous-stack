---
nav_exclude: false
parent: "Technology Catalog"
nav_order: 99
title: "Gitea Actions"
category: "applications/ci-cd"
status: "stable"
license: "MIT"
source: "https://github.com/go-gitea/gitea"
repository: "https://github.com/go-gitea/gitea"
documentation: "https://docs.gitea.com/usage/actions/overview"
docker_image: "gitea/gitea"
community: "https://discourse.gitea.io"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker", "forgejo"]
optional_deps: ["prometheus"]
depended_by: []
critical_criteria: ["Exit", "External Dependencies"]
---

# Gitea Actions

> **TAS Score: S3/3 — D5/5 · A3 / T2**

## Brief Description

Built-in CI/CD for Gitea and Forgejo. GitHub Actions-compatible syntax — pipelines defined in `.gitea/workflows/` YAML files. Act runner executes jobs in Docker containers. No separate CI server needed — CI/CD is part of your Git host.

## Architectural Role

Applications layer. CI/CD integrated directly into Forgejo/Gitea. The act runner can be deployed alongside the Git server or on separate nodes. GitHub Actions workflow syntax compatibility means migrating existing pipelines is straightforward.

## Technical Autonomy

- [x] Works without internet
- [x] Stores data locally
- [x] Does not require external accounts
- [x] Allows data export (pipeline configs are YAML in repo; GitHub Actions compatible)
- [ ] Provides offline updates

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Part of Forgejo/Gitea — clean stop |
| Exit                  | ✅     | Workflow YAML is GitHub Actions compatible — portable |
| Recoverability        | ✅     | Stateless runners; configs in repo |
| Visibility            | ✅     | MIT license, fully auditable |
| External Dependencies | ✅     | Runs fully self-contained |

## Configuration (Minimal)

```yaml
# Act runner — runs alongside Forgejo/Gitea
services:
  act-runner:
    image: gitea/act_runner:latest
    environment:
      GITEA_INSTANCE_URL: https://git.yourdomain.com
      GITEA_RUNNER_REGISTRATION_TOKEN: your-token
      GITEA_RUNNER_NAME: my-runner
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - act_runner_data:/data

volumes:
  act_runner_data:
```

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Woodpecker CI](woodpecker.md) | A3 / T2 | Dedicated CI server; more flexible |
| [Jenkins](jenkins.md) | A3 / T2 | More powerful, heavier |

---

## Trajectory

**Direction: opening**

Gitea Actions is part of both Gitea and Forgejo — both community-governed projects with MIT/MIT licensing. GitHub Actions syntax compatibility is a deliberate choice to reduce vendor lock-in: your pipelines are portable. The act runner is developed in the open with active contributions.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | MIT; no changes |
| Feature gating | ✅ | No paid tier; all features available |
| Self-hosting | ✅ | Self-hosting is the only deployment model |
| Governance | ✅ | Community-governed via Forgejo (Codeberg e.V.) and Gitea org |

---

## Sources

- **Website:** https://docs.gitea.com/usage/actions/overview
- **Documentation:** https://docs.gitea.com/usage/actions/act-runner
- **Repository:** https://github.com/go-gitea/gitea
- **Docker image:** gitea/act_runner
- **Community:** https://discourse.gitea.io
