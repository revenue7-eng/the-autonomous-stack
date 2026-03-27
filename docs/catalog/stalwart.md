---
nav_exclude: false
title: "Stalwart"
parent: "Technology Catalog"
category: "communication/email"
status: "stable"
license: "AGPL-3.0"
source: "https://github.com/stalwartlabs/stalwart"
repository: "https://github.com/stalwartlabs/stalwart"
documentation: "https://stalw.art/docs/get-started"
docker_image: "stalwartlabs/mail-server"
community: "https://discord.gg/stalwart"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Trajectory"]
---

# Stalwart

> **TAS Score: S3/3 — D4/5** — A3 / T2
> D4 not D5: dual licensing (AGPL-3.0 + proprietary SELv1) — enterprise features gated behind paid license (Q8).

## Brief Description

All-in-one mail and collaboration server written in Rust. Supports JMAP, IMAP4, POP3, SMTP, CalDAV, CardDAV, and WebDAV. Single binary — no external databases required. Dual-licensed: AGPL-3.0 (community) and SELv1 (enterprise). 8,400+ GitHub stars. Funded by European NGI programs.

## Architectural Role

Communication layer: complete self-hosted email and collaboration infrastructure in a single server. Mail, calendars, contacts, and file storage.

## Technical Autonomy

- [x] Works without internet — receives and stores mail locally; sending requires internet
- [x] Stores data locally — SQLite or FoundationDB, all on your server
- [x] Does not require external accounts
- [x] Allows data export — standard protocols (IMAP, CalDAV, CardDAV) for migration
- [x] Provides offline updates — binary or Docker image, updated manually

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Stop the process or container. Mail queued by senders per RFC 5321. Resume without data loss. |
| Exit                  | ✅     | Standard protocols (IMAP, CalDAV, CardDAV). Migrate to any server. |
| Recoverability        | ✅     | Single data directory. SQLite backend. Straightforward backup and restore. |
| Visibility            | ✅     | Open source (AGPL-3.0). Full source available. Enterprise features visible in code but license-gated. |
| External Dependencies | ✅     | No external databases, no external services. Single binary. Optional: Let's Encrypt. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

```yaml
services:
  stalwart-mail:
    image: stalwartlabs/mail-server:latest
    volumes:
      - ./stalwart-mail:/opt/stalwart-mail
    ports:
      - 443:443
      - 25:25
      - 587:587
      - 465:465
      - 143:143
      - 993:993
      - 4190:4190
    restart: unless-stopped
```

Admin password logged on first run. Requires DNS configuration (MX, SPF, DKIM, DMARC). Runs comfortably on 512 MB RAM.

## Related Recipes

- [Privacy-First Homelab](../recipes/privacy-first-homelab.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Mailcow](mailcow.html) | A3 / T2 | More established, larger community, Docker-based, higher resources (4-6 GB RAM) |
| [Gmail](gmail.html) | A0 / T0 | Zero maintenance, zero ownership |

---

## Trajectory

**Direction: opening (with caveats)**

Actively developed with EU funding (NGI0 Entrust, NGI Zero Core). Approaching v1.0 — feature complete, focusing on performance. AGPL protects community edition. Dual licensing means enterprise features may diverge over time. Worth monitoring.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ➖ | AGPL-3.0 (open) + SELv1 (proprietary enterprise). Community edition fully functional. |
| Feature gating | ⚠️ | Some features enterprise-only. Sponsors at $5/month get enterprise license. |
| Self-hosting | ✅ | Self-hosting is the primary deployment model. |
| Governance | ➖ | Stalwart Labs LLC. Open source but corporate-governed. EU funding is positive signal. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** https://stalw.art
- **Documentation:** https://stalw.art/docs/get-started
- **Repository:** https://github.com/stalwartlabs/stalwart
- **Docker image:** stalwartlabs/mail-server
- **Community:** https://discord.gg/stalwart
