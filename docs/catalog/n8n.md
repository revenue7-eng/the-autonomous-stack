---
nav_exclude: false
title: "n8n"
parent: "Technology Catalog"
category: "applications/automation"
status: "stable"
license: "Sustainable-Use-1.0"
source: "https://github.com/n8n-io/n8n"
repository: "https://github.com/n8n-io/n8n"
documentation: "https://docs.n8n.io"
docker_image: "n8nio/n8n"
community: "https://community.n8n.io"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: ["postgresql"]
depended_by: []
critical_criteria: ["Trajectory"]
---

# n8n

> **TAS Score: S3/3 — D4/5** — A3 / T2
> D4 not D5: "Sustainable Use License" is source-available but not OSI-approved — commercial use restricted without paid license (Q7, Q8). Self-hosting for personal/internal use is free.

## Brief Description

Source-available workflow automation platform. Visual node-based editor with 400+ integrations. Selfhosted or cloud. Supports code nodes (JavaScript/Python) for custom logic. 106,000+ GitHub stars. Licensed under Sustainable Use License (free for personal and internal use).

## Architectural Role

Integration/automation layer: connects services, automates workflows, API orchestration. Direct alternative to Zapier with selfhosted option.

## Technical Autonomy

- [x] Works without internet — workflows execute locally; external integrations require internet
- [x] Stores data locally — SQLite or PostgreSQL, all on your server
- [x] Does not require external accounts
- [x] Allows data export — workflows exportable as JSON; fully portable between n8n instances
- [x] Provides offline updates — Docker image, updated manually

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Stop the container. Workflows pause. Resume without loss. |
| Exit                  | ✅     | Workflows export as JSON. Credentials stored locally. Database is standard SQLite/PostgreSQL. |
| Recoverability        | ✅     | Database backup + workflow JSON export. Straightforward restore. |
| Visibility            | ✅     | Source code fully available on GitHub. Audit possible. |
| External Dependencies | ✅     | Requires only Node.js runtime. Optional: PostgreSQL. No mandatory external services. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

```yaml
services:
  n8n:
    image: n8nio/n8n:latest
    environment:
      - N8N_BASIC_AUTH_ACTIVE=true
      - N8N_BASIC_AUTH_USER=admin
      - N8N_BASIC_AUTH_PASSWORD=changeme
    ports:
      - 5678:5678
    volumes:
      - ./n8n_data:/home/node/.n8n
    restart: unless-stopped
```

Runs on ~256 MB RAM for basic workflows. PostgreSQL recommended for production.

## Related Recipes

- [Developer Workstation](../recipes/developer-workstation.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Node-RED](node-red.html) | A3 / T2 | Apache-2.0, lighter, IoT-focused, fewer SaaS integrations |
| [Zapier](zapier.html) | A0 / T0 | No-code, 7000+ apps, fully proprietary, no export |

---

## Trajectory

**Direction: mixed**

n8n changed from Apache-2.0 to Sustainable Use License in 2022 — a significant closing signal. However: source remains fully available, selfhosting for personal/internal use is free, and development is very active (106K+ stars, regular releases). The company offers n8n Cloud as paid SaaS. Commercial selfhosting requires paid license. The license change is worth noting but hasn't affected the selfhosted experience for most users.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ⚠️ | Changed from Apache-2.0 to Sustainable Use License (2022). Source-available but not OSI-approved. |
| Feature gating | ➖ | All features available in selfhosted. Cloud version is paid alternative, not gated features. |
| Self-hosting | ✅ | Selfhosting is fully supported and documented. Primary deployment model for community. |
| Governance | ➖ | VC-backed company (n8n GmbH, Berlin). Active community. License change was controversial but stable since. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** https://n8n.io
- **Documentation:** https://docs.n8n.io
- **Repository:** https://github.com/n8n-io/n8n
- **Docker image:** n8nio/n8n
- **Community:** https://community.n8n.io
