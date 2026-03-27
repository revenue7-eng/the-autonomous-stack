---
parent: "Technology Catalog"
nav_order: 99
title: "Jenkins"
category: "applications/ci-cd"
status: "stable"
license: "MIT"
source: "https://github.com/jenkinsci/jenkins"
repository: "https://github.com/jenkinsci/jenkins"
documentation: "https://www.jenkins.io/doc"
docker_image: "jenkins/jenkins"
community: "https://community.jenkins.io"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: ["prometheus"]
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
---

# Jenkins

> **TAS Score: S3/3 — D4/5 · A3 / T2**
> _(D4 not D5: Jenkins is in maintenance mode for new features — development focus has shifted to the ecosystem. Trajectory is stable but not opening.)_

## Brief Description

The most widely deployed open-source CI/CD server. 1800+ plugins. Pipeline-as-code via Jenkinsfile. Java-based, runs anywhere. The reference implementation for self-hosted CI/CD — battle-tested at any scale since 2011 (originally Hudson, 2004).

## Architectural Role

Applications layer. CI/CD pipeline orchestration. Highly flexible — can build, test, deploy anything through its plugin ecosystem. Heavier than Woodpecker or Gitea Actions but more powerful for complex enterprise pipelines.

## Technical Autonomy

- [x] Works without internet
- [x] Stores data locally (filesystem)
- [x] Does not require external accounts
- [x] Allows data export (Jenkinsfile is plain Groovy in repo; job configs exportable)
- [ ] Provides offline updates

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Clean stop; no permanent damage |
| Exit                  | ✅     | Jenkinsfile is code in your repo; job configs exportable as XML |
| Recoverability        | ✅     | Filesystem backup of JENKINS_HOME |
| Visibility            | ✅     | MIT license, fully auditable |
| External Dependencies | ✅     | Runs fully self-contained |

## Configuration (Minimal)

```yaml
services:
  jenkins:
    image: jenkins/jenkins:lts
    user: root
    volumes:
      - jenkins_home:/var/jenkins_home
      - /var/run/docker.sock:/var/run/docker.sock
    ports:
      - "8080:8080"
      - "50000:50000"

volumes:
  jenkins_home:
```

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Woodpecker CI](woodpecker.md) | A3 / T2 | Lighter, modern, Docker-native |
| [Gitea Actions](gitea-actions.md) | A3 / T2 | Built into Forgejo/Gitea; GitHub Actions syntax |

---

## Trajectory

**Direction: stable**

Jenkins has been MIT licensed since its fork from Hudson in 2011. The Jenkins project is governed by the Continuous Delivery Foundation (Linux Foundation). Development has slowed — most innovation happens in the plugin ecosystem rather than the core. No commercial entity controls Jenkins. For new projects, lighter alternatives like Woodpecker may be preferable, but Jenkins remains the most battle-tested option for complex pipelines.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | MIT since 2011; no changes |
| Feature gating | ✅ | No paid tier; 1800+ free plugins |
| Self-hosting | ✅ | Self-hosting is the only deployment model |
| Governance | ➖ | CDF (Linux Foundation) governance; core in maintenance mode |

---

## Sources

- **Website:** https://www.jenkins.io
- **Documentation:** https://www.jenkins.io/doc
- **Repository:** https://github.com/jenkinsci/jenkins
- **Docker image:** jenkins/jenkins
- **Community:** https://community.jenkins.io
