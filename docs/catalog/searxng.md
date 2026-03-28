---
nav_exclude: false
title: "SearXNG"
category: "applications/search"
status: "stable"
license: "AGPL-3.0"
source: "https://docs.searxng.org"
repository: "https://github.com/searxng/searxng"
documentation: "https://docs.searxng.org"
docker_image: "searxng/searxng"
community: "https://github.com/searxng/searxng/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: []
depended_by: []
critical_criteria: ["Pause", "Exit"]
trajectory: "opening"
parent: Technology Catalog
nav_order: 99
---

# SearXNG

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Privacy-respecting metasearch engine that aggregates results from 70+ search engines without tracking users. Self-hosted alternative to Google Search. No ads, no tracking, no profiling.

## Architectural Role

Search layer: replaces Google/Bing as your default search engine. Runs on your server, queries upstream engines on your behalf, strips tracking parameters, and returns clean results. Can be set as default search in any browser.

## Technical Autonomy

- ✅ Works without internet (returns cached results, but needs internet for live search)
- ✅ Stores no user data (stateless by design)
- ✅ Does not require external accounts
- ✅ No data to export (no user data stored)
- ✅ Configurable via single settings file

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅ | Stop container, no data loss. Stateless. |
| Exit                  | ✅ | Nothing to migrate — configuration is one YAML file. |
| Recoverability        | ✅ | Redeploy from config in seconds. |
| Visibility            | ✅ | AGPL-3.0, fully auditable. |
| External Dependencies | ⚠️ | Requires internet to query upstream search engines. The search itself is proxied, not local. |

## Configuration (Minimal)

```yaml
services:
  searxng:
    image: searxng/searxng
    container_name: searxng
    ports:
      - "8888:8080"
    volumes:
      - ./data/searxng:/etc/searxng
    environment:
      - SEARXNG_BASE_URL=https://search.example.com
    restart: unless-stopped
```

## Related Recipes

- [Privacy-First Homelab](../recipes/privacy-first-homelab.md)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Google Analytics](google-analytics.md) | A0 / T0 | Google Search itself — tracks everything, profiles users. |
| Whoogle | A3 / T2 | Google results without tracking. Single-engine, less versatile. |
| Presearch | A1 / T1 | Decentralized search with token incentives. Blockchain dependency. |

---

## Trajectory

**Direction: opening.**

SearXNG is a community fork of searx with more active development, better maintenance, and modern features. The project is growing in contributors and instances.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | AGPL-3.0, unchanged. Strong copyleft. |
| Feature gating | ✅ | No paid tier. Everything is free. |
| Self-hosting | ✅ | Docker-first, extensive documentation, many public instances. |
| Governance | ✅ | Community-driven fork with multiple active maintainers. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [searxng.org](https://docs.searxng.org)
- **Repository:** [github.com/searxng/searxng](https://github.com/searxng/searxng)
- **Docker image:** `searxng/searxng`
