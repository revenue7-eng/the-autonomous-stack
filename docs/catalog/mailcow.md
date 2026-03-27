---
nav_exclude: false
title: "Mailcow"
parent: "Technology Catalog"
nav_order: 99
category: "communication/email"
status: "stable"
license: "GPL-3.0"
source: "https://github.com/mailcow/mailcow-dockerized"
repository: "https://github.com/mailcow/mailcow-dockerized"
documentation: "https://docs.mailcow.email"
docker_image: "ghcr.io/mailcow"
community: "https://t.me/mailcow"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: []
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
---

# Mailcow

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Open-source, Docker-based email server suite. Combines Postfix (SMTP), Dovecot (IMAP/POP3), SOGo (webmail/groupware), Rspamd (spam filtering), ClamAV (antivirus), and a web-based admin UI. GPLv3 licensed. 12,400+ GitHub stars.

## Architectural Role

Communication layer: complete self-hosted email infrastructure. Handles sending, receiving, filtering, webmail, and administration.

## Technical Autonomy

- [x] Works without internet — receives and stores mail locally; sending requires internet (SMTP)
- [x] Stores data locally — all emails, contacts, and calendars on your server
- [x] Does not require external accounts
- [x] Allows data export — standard mbox/Maildir formats; IMAP migration tools available
- [x] Provides offline updates — Docker images can be pulled and applied manually

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Stop Docker containers. Mail queued by sending servers per RFC 5321 (retried 3+ days). Resume without data loss. |
| Exit                  | ✅     | Standard email formats (mbox, Maildir). IMAP-based migration to any server. Your domain, your MX records. |
| Recoverability        | ✅     | Full control over backups. Database and mail storage are local. Docker-based architecture makes restoration straightforward. |
| Visibility            | ✅     | Fully open source (GPLv3). All components are established open-source projects. |
| External Dependencies | ✅     | Requires domain name and DNS. Optional: ClamAV definitions, Let's Encrypt. Core works independently. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

```bash
cd /opt
git clone https://github.com/mailcow/mailcow-dockerized
cd mailcow-dockerized
./generate_config.sh
docker compose pull
docker compose up -d
```

Requires DNS configuration (MX, SPF, DKIM, DMARC records) and a VPS with port 25 open. Minimum 4 GB RAM (6 GB recommended with ClamAV).

## Related Recipes

- [Privacy-First Homelab](../recipes/privacy-first-homelab.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Stalwart](stalwart.html) | A3 / T2 | Single binary (Rust), lower resources (~512 MB RAM), newer, JMAP support |
| [Gmail](gmail.html) | A0 / T0 | Zero maintenance, zero ownership |

---

## Trajectory

**Direction: opening**

Actively maintained with regular releases. Recently moved Docker images from Docker Hub to GitHub Container Registry — reducing external dependency. Community is active. No signs of license changes or feature gating.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | GPLv3. No changes. |
| Feature gating | ✅ | All features free. Optional SAL (Stay-Awesome License) is voluntary donation, not required. |
| Self-hosting | ✅ | Self-hosting is the only deployment model. |
| Governance | ✅ | Community-driven. Open issue tracker. Transparent development. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** https://mailcow.email
- **Documentation:** https://docs.mailcow.email
- **Repository:** https://github.com/mailcow/mailcow-dockerized
- **Docker image:** ghcr.io/mailcow
- **Community:** https://t.me/mailcow
