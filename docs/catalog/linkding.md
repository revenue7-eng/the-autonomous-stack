---
nav_exclude: false
title: "Linkding"
category: "applications/bookmarks"
status: "stable"
license: "MIT"
source: "https://github.com/sissbruecker/linkding"
repository: "https://github.com/sissbruecker/linkding"
documentation: "https://github.com/sissbruecker/linkding#readme"
docker_image: "sissbruecker/linkding"
community: "https://github.com/sissbruecker/linkding/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: []
depended_by: []
critical_criteria: ["Exit", "Pause"]
trajectory: "stable"
parent: Technology Catalog
nav_order: 99
---

# Linkding

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Minimal self-hosted bookmark manager. Fast, clean UI, tag-based organization, full-text search, bulk editing, and browser extensions. Does one thing — manages bookmarks — and does it well. No bloat, no complexity.

## Architectural Role

Applications layer: replaces browser bookmark sync (Chrome/Firefox), Raindrop, Pinboard, and del.icio.us. Centralizes bookmarks across all browsers and devices in a self-hosted instance.

## Technical Autonomy

- ✅ Works without internet (browse saved bookmarks offline)
- ✅ Stores data locally (SQLite database)
- ✅ Does not require external accounts
- ✅ Allows data export (Netscape HTML format — universal bookmark standard)
- ✅ Import from any browser or bookmark service

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅ | Stop container, bookmarks stay. |
| Exit                  | ✅ | Export as Netscape HTML — importable into any browser or service. |
| Recoverability        | ✅ | SQLite file. Copy and restore. |
| Visibility            | ✅ | MIT license. Simple Python/Django codebase. |
| External Dependencies | ✅ | Fully self-contained. Optional background archiving (wayback). |

## Configuration (Minimal)

```yaml
services:
  linkding:
    image: sissbruecker/linkding:latest
    container_name: linkding
    ports:
      - "9091:9090"
    volumes:
      - ./data/linkding:/etc/linkding/data
    restart: unless-stopped
```

## Related Recipes

- [Privacy-First Homelab](../recipes/privacy-first-homelab.md)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Wallabag](wallabag.md) | A3 / T2 | Full article archiver, not just bookmarks. More complex. |
| Raindrop.io | A0 / T0 | Cloud-only, freemium. Polished UI but proprietary. |
| Pinboard | A0 / T0 | Cloud-only, paid. Minimal but not self-hosted. |
| Shaarli | A3 / T2 | PHP-based, older. Single-file bookmark manager. |

---

## Trajectory

**Direction: stable.**

Linkding is a mature, focused tool. Regular releases, active maintainer, no feature bloat. MIT licensed. The simplicity is the feature.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | MIT, unchanged. |
| Feature gating | ✅ | No paid tier. |
| Self-hosting | ✅ | Docker-first, minimal resource usage. |
| Governance | ⚠️ | Single maintainer (sissbruecker). Bus factor = 1. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Repository:** [github.com/sissbruecker/linkding](https://github.com/sissbruecker/linkding)
- **Docker image:** `sissbruecker/linkding`
