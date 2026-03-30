---
nav_exclude: false
title: "Nextcloud"
category: "applications/cloud"
status: "stable"
license: "AGPL-3.0"
source: "https://nextcloud.com"
repository: "https://github.com/nextcloud/server"
documentation: "https://docs.nextcloud.com"
docker_image: "https://hub.docker.com/_/nextcloud"
community: "https://help.nextcloud.com"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker", "postgresql"]
optional_deps: ["redis"]
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
trajectory: "stable"
parent: Technology Catalog
nav_order: 99
---

# Nextcloud

> **TAS Score: S3/3 — D4/5** — A3 / T2
> _D4 not D5: push notification server is centralized by default (D3 — hidden infrastructure cost)._
>
> _Assessment criteria: [v1.0](assessment-criteria.md). Last verified: 2025-05._

## Brief Description

Self-hosted cloud platform providing file sync, calendar, contacts, email, office documents, video calls, and more — all under your control. The most comprehensive open-source alternative to Google Workspace and Microsoft 365.

## Architectural Role

Applications layer: central hub for personal and team productivity. Replaces multiple cloud services with a single self-hosted platform.

---

## Formal Assessment

### S1: Pause

| Test | Result | Evidence |
|------|--------|----------|
| Can you stop the process without a special shutdown procedure? | ✅ Yes | `docker stop nextcloud` — clean shutdown. |
| After stopping, is all data still on disk in a readable state? | ✅ Yes | Files in volume. Database in PostgreSQL/MariaDB volume. All on disk. |
| Can you restart and continue where you left off? | ✅ Yes | `docker start` → all files, calendar, contacts intact. |

**S1 = Yes**

### S2: Exit

| Test | Result | Evidence |
|------|--------|----------|
| Is there a documented export mechanism? | ✅ Yes | Files: copy from volume. Calendar: CalDAV export (`.ics`). Contacts: CardDAV export (`.vcf`). Database: `pg_dump`. |
| Does the export include ALL user data? | ✅ Yes | Files, calendar events, contacts, notes, bookmarks — all exportable. App-specific data via database dump. |
| Is the export in a standard, reusable format? | ✅ Yes | Files are ordinary files. Calendar uses iCalendar (`.ics`). Contacts use vCard (`.vcf`). All open standards. |
| Can another tool import the exported data? | ✅ Yes | Any CalDAV/CardDAV client reads the exports. Files are files. |

**S2 = Yes**

### S3: Recoverability

| Test | Result | Evidence |
|------|--------|----------|
| Does the service support backups? | ✅ Yes | File volume + database dump. Documented procedure in admin manual. |
| Can you restore from backup to a working state? | ✅ Yes | Restore volume + import database → working instance. Documented step-by-step. |
| Does a restore give you back the SAME state? | ✅ Yes | All files, all metadata, all calendar/contacts data restored. User sessions regenerated (expected). |

**S3 = Yes**

### Autonomy Level

| S1 | S2 | S3 | Level |
|----|----|----|-------|
| Yes | Yes | Yes | **A3** |

### Transparency Level

| Test | Result | Evidence |
|------|--------|----------|
| Source code publicly available? | ✅ Yes | github.com/nextcloud/server + all official apps |
| License OSI-approved? | ✅ Yes | AGPL-3.0 |

**T = T2**

### Diagnostic Score

| # | Question | Result | Evidence |
|---|----------|--------|----------|
| D1 | Personalisation | ✅ Clean | No analytics sent externally. No behavioural profiling. Usage stats are local admin dashboard only. |
| D2 | Urgency | ✅ Clean | No forced updates. No countdown timers. Update notifications are informational. |
| D3 | Hidden cost | ⚠️ Concern | **Push notification server** (`push-notifications.nextcloud.com`) is operated by Nextcloud GmbH. Default setup routes through their infrastructure. Self-hosting the push proxy is possible but underdocumented. |
| D4 | Transparency fragility | ✅ Clean | Business model is enterprise support contracts. Community edition is fully functional. No dark patterns. |
| D5 | Trajectory | ✅ Clean | AGPL-3.0 since fork from ownCloud (2016). Enterprise apps exist but core features are fully open. Self-hosting is the primary use case. |

**D-score: D4/5** (1 concern: D3)

---

## Counterarguments

| Claim | Challenge | Resolution |
|-------|-----------|------------|
| **A3: fully autonomous** | Depends on Docker and PostgreSQL — multi-layer dependency | Docker and PostgreSQL are both A3/T2. The dependency is on open-source infrastructure, not on a vendor. Noted in `depends_on`. |
| **A3: fully autonomous** | Push notifications route through Nextcloud GmbH server by default | Self-hosting the push proxy is possible. Without push, all features work — only mobile notifications are delayed. Captured as D3 concern. |
| **D4: not D5** | Enterprise apps are closed source | Enterprise apps are separate products. The core Nextcloud server and all community apps are AGPL-3.0. No core feature has moved to enterprise-only. |
| **T2: open source** | Some Nextcloud apps developed by Nextcloud GmbH have contributor license agreements | CLA exists for Nextcloud GmbH-developed apps. Community apps do not require CLA. The CLA allows dual-licensing but the AGPL code remains AGPL. |

---

## Configuration (Minimal)

```yaml
services:
  nextcloud:
    image: nextcloud:latest
    ports:
      - "8080:80"
    volumes:
      - ./nextcloud-data:/var/www/html
    environment:
      SQLITE_DATABASE: nextcloud
    restart: unless-stopped
```

For production, use PostgreSQL or MariaDB instead of SQLite.

## Related Recipes

- [Minimal Autonomous Server](../recipes/minimal-server.md)
- [Family Cloud](../recipes/family-cloud.md)
- [Home Office](../recipes/home-office.md)
- [GrapheneOS Mobile Stack](../recipes/grapheneos-mobile.md)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Syncthing](syncthing.md) | A3 / T2 | Lighter, P2P only. No calendar/contacts/office. |
| Seafile | A3 / T2 | File sync focused, less feature-rich. |
| Google Workspace | A0 / T0 | Cloud-only. Full vendor dependency. |

---

## Trajectory

**Direction: stable.**

Nextcloud has consistently maintained its open-source commitment since forking from ownCloud in 2016. AGPL-3.0 ensures modifications must be shared. Nextcloud GmbH monetises through enterprise support contracts, not by closing features.

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | AGPL-3.0 since fork in 2016; no changes. |
| Feature gating | ➖ | Enterprise apps exist but core functionality is fully open. No regression. |
| Self-hosting | ✅ | Self-hosting is the primary use case; documentation improving. |
| Governance | ✅ | Active community; Nextcloud GmbH supports but doesn't gate community edition. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** https://nextcloud.com
- **Documentation:** https://docs.nextcloud.com
- **Repository:** https://github.com/nextcloud/server
- **Docker image:** https://hub.docker.com/_/nextcloud
- **Community:** https://help.nextcloud.com
