---
nav_exclude: true
title: "Technology Name"
category: "category/subcategory"      # e.g. network/vpn, storage/backup, security/passwords
status: "stable | experimental"
license: "SPDX identifier"            # e.g. MIT, Apache-2.0, GPL-2.0, AGPL-3.0, Proprietary
source: "-"
repository: "-"
documentation: "-"
docker_image: "-"
community: "-"
autonomy_level: "A0"                  # A0 | A1 | A2 | A3
transparency_level: "T0"              # T0 | T1 | T2
depends_on: []                        # required runtime deps — use catalog slugs e.g. ["docker", "postgresql"]
optional_deps: []                     # optional integrations e.g. ["prometheus"]
depended_by: []                       # what uses this — populated by other cards e.g. ["nextcloud", "authentik"]
critical_criteria: []                 # highest-stakes criteria for this category e.g. ["Exit", "Recoverability"]
---

# Technology Name

> **TAS Score: S_/3 — D_/5** — A_ / T_
> _(explain any deduction: e.g. "D4 not D5: optional telemetry enabled by default (Q4).")_
> _(if S=3 and D=5, remove the explanation line)_

## Brief Description

One or two sentences explaining what the technology does.

## Architectural Role

Where does it fit in the autonomous stack? Which layer: network / identity / storage / compute / security / observability / applications?

## Technical Autonomy

- [ ] Works without internet
- [ ] Stores data locally
- [ ] Does not require external accounts
- [ ] Allows data export
- [ ] Provides offline updates

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status        | Comments |
|-----------------------|---------------|----------|
| Pause                 | ✅ / ⚠️ / ❌ | Can the service be stopped without permanent damage? |
| Exit                  | ✅ / ⚠️ / ❌ | Can the user leave with all data in a portable format? |
| Recoverability        | ✅ / ⚠️ / ❌ | Are backups and rollbacks supported and user-controlled? |
| Visibility            | ✅ / ⚠️ / ❌ | Is the architecture/code open enough to inspect? |
| External Dependencies | ✅ / ⚠️ / ❌ | Can it run without mandatory third-party cloud services? |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

A minimal working example (`docker-compose.yml` snippet or `docker run` command).

```yaml
# example
services:
  app:
    image: example/app:latest
    volumes:
      - ./data:/data
```

## Related Recipes

- [Minimal Autonomous Server](../recipes/minimal-server.md)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Tool Name](tool-name.md) | A_ / T_ | Brief comparison |

---

## Trajectory

**Direction: opening / stable / mixed / closing**

_One paragraph describing where this project is heading and why._

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ / ➖ / ⚠️ | Has the license changed in the last 3 years? More or less restrictive? |
| Feature gating | ✅ / ➖ / ⚠️ | Are key features moving to enterprise/paid tier? |
| Self-hosting | ✅ / ➖ / ⚠️ | Is self-hosting becoming easier or harder with new versions? |
| Governance | ✅ / ➖ / ⚠️ | Is community contribution growing or declining? Single maintainer risk? |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** 
- **Documentation:** 
- **Repository:** 
- **Docker image:** 
- **Community:** 

---
<!--
CONTRIBUTOR CHECKLIST — remove before submitting PR

Required:
[ ] frontmatter complete (all fields filled, depends_on populated)
[ ] TAS Score filled with gap explanation if S<3 or D<5
[ ] Trajectory section with all 4 signal rows filled
[ ] at least one configuration example
[ ] Alternatives table has at least one entry
[ ] card added to docs/catalog/index.md in correct category

For anti-example cards (A0/T0):
[ ] "Why it's in the catalog" section added
[ ] "Autonomous Alternatives" section added
-->
