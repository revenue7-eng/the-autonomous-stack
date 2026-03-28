---
nav_exclude: false
title: "Gitea"
category: "applications/version-control"
status: "stable"
license: "MIT"
source: "https://gitea.com"
repository: "https://github.com/go-gitea/gitea"
documentation: "https://docs.gitea.com"
docker_image: "gitea/gitea"
community: "https://discourse.gitea.io"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: ["postgresql"]
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
trajectory: "mixed"
parent: Technology Catalog
nav_order: 99
---

# Gitea

> **TAS Score: S3/3 — D4/5** — A3 / T2
> D4 not D5: Gitea Ltd. (for-profit company) controls development direction. The community forked to Forgejo over governance concerns (Q8). Commercial features (Gitea Actions cloud runners) are being developed for the hosted offering.

## Brief Description

Lightweight self-hosted Git service. Fork of Gogs, written in Go. Provides Git hosting, issue tracking, pull requests, wikis, and CI/CD (Gitea Actions). Fast, low resource usage, easy to deploy. Gitea is the upstream of Forgejo.

## Architectural Role

Applications/dev layer: self-hosted GitHub alternative. Hosts Git repositories, manages code review, tracks issues. Gitea Actions provides CI/CD. Lighter than GitLab, more features than bare Git.

## Technical Autonomy

- ✅ Works without internet (all Git operations are local after clone)
- ✅ Stores data locally (Git repos + SQLite/PostgreSQL)
- ✅ Does not require external accounts
- ✅ Allows data export (Git repos are standard, dump command for metadata)
- ✅ Mirrors and federation support

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅ | Stop container, repos stay on disk. |
| Exit                  | ✅ | Git repos are standard. `gitea dump` exports everything. Migrate to Forgejo, GitLab, or bare Git. |
| Recoverability        | ✅ | Database + repo directory backup. |
| Visibility            | ✅ | MIT license. Full source on GitHub. |
| External Dependencies | ✅ | Fully self-contained. |

## Configuration (Minimal)

```yaml
services:
  gitea:
    image: gitea/gitea:latest
    container_name: gitea
    ports:
      - "3000:3000"
      - "2222:22"
    volumes:
      - ./data/gitea:/data
    environment:
      - USER_UID=1000
      - USER_GID=1000
    restart: unless-stopped
```

## Related Recipes

- [Developer Workstation](../recipes/developer-workstation.md)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Forgejo](forgejo.md) | A3 / T2 | Community fork of Gitea. Non-profit governance. Recommended over Gitea for new deployments. |
| GitLab CE | A3 / T2 | Full DevOps platform. Much heavier, more features. |
| GitHub | A0 / T0 | Cloud-only, proprietary. The service Gitea replaces. |

---

## Trajectory

**Direction: mixed.**

Gitea was community-driven until 2022 when Gitea Ltd. was created as a for-profit company, transferring the domain and trademark from the community. This triggered the Forgejo fork (under Codeberg e.V., a non-profit). Gitea remains MIT-licensed and functional, but governance is now corporate. For new deployments, Forgejo is recommended due to its non-profit governance model.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | MIT, unchanged. |
| Feature gating | ⚠️ | Gitea Ltd. developing commercial cloud features. Self-hosted version still full-featured. |
| Self-hosting | ✅ | Easy to deploy, lightweight, well documented. |
| Governance | ⚠️ | For-profit company (Gitea Ltd.) controls direction. Community forked to Forgejo in response. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [gitea.com](https://gitea.com)
- **Repository:** [github.com/go-gitea/gitea](https://github.com/go-gitea/gitea)
- **Docker image:** `gitea/gitea`
