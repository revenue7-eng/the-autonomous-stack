---
nav_exclude: false
title: "Ntfy"
category: "communication/notifications"
status: "stable"
license: "Apache-2.0 / GPL-2.0"
source: "https://ntfy.sh"
repository: "https://github.com/binwiederhier/ntfy"
documentation: "https://docs.ntfy.sh"
docker_image: "binwiederhier/ntfy"
community: "https://discord.gg/cT7ECsZj9w"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: []
depended_by: []
critical_criteria: ["Pause", "Exit"]
trajectory: "stable"
parent: Technology Catalog
nav_order: 99
---

# Ntfy

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Simple HTTP-based pub-sub notification service. Send push notifications to your phone or desktop from any script, cron job, or monitoring tool with a single `curl` command. No account, no API key, no app registration.

## Architectural Role

Notification layer: the glue between your infrastructure and your attention. Uptime Kuma detects downtime → ntfy pushes alert to your phone. Backup script finishes → ntfy notifies you. Any service that can make an HTTP request can send notifications through ntfy.

## Technical Autonomy

- ✅ Works without internet (LAN delivery to connected clients)
- ✅ Stores messages locally (configurable cache)
- ✅ Does not require external accounts
- ✅ Allows data export (messages are plain text over HTTP)
- ⚠️ iOS push requires upstream relay through ntfy.sh (Apple restriction)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅ | Stop the container, no data loss. Messages queue on sender side. |
| Exit                  | ✅ | Messages are ephemeral. Configuration is a single YAML file. |
| Recoverability        | ✅ | Stateless by design. Redeploy from config in minutes. |
| Visibility            | ✅ | Fully open source, dual-licensed Apache 2.0 / GPL 2.0. |
| External Dependencies | ✅ | Fully self-hosted. iOS push optionally uses ntfy.sh relay. |

## Configuration (Minimal)

```yaml
services:
  ntfy:
    image: binwiederhier/ntfy
    container_name: ntfy
    command: serve
    ports:
      - "2586:80"
    volumes:
      - ./data/ntfy/cache:/var/cache/ntfy
      - ./data/ntfy/etc:/etc/ntfy
    restart: unless-stopped
```

Send a notification:

```bash
curl -d "Backup complete" http://your-server:2586/alerts
```

## Related Recipes

- [Monitoring Stack](../recipes/monitoring-stack.md) — use ntfy as alert target for Uptime Kuma and Grafana

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| Gotify | A3 / T2 | Similar concept, WebSocket-based instead of HTTP pub-sub. No iOS app. |
| Pushover | A0 / T0 | Cloud-only, proprietary. One-time purchase. |
| Firebase Cloud Messaging | A0 / T0 | Google's push service. Required for iOS/Android background push. |

---

## Trajectory

**Direction: stable.**

ntfy has been consistently maintained by a single developer with a clear vision: simple, self-hostable notifications. The dual license (Apache 2.0 / GPL 2.0) is maximally permissive. Paid plans exist for the hosted service but do not gate any self-hosted features.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | Dual Apache 2.0 / GPL 2.0. No changes. |
| Feature gating | ✅ | All features available in self-hosted version. Paid plans are for hosted service only. |
| Self-hosting | ✅ | First-class self-hosting support. Single binary or Docker. |
| Governance | ⚠️ | Single maintainer (binwiederhier). Bus factor = 1. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [ntfy.sh](https://ntfy.sh)
- **Documentation:** [docs.ntfy.sh](https://docs.ntfy.sh)
- **Repository:** [github.com/binwiederhier/ntfy](https://github.com/binwiederhier/ntfy)
- **Docker image:** `binwiederhier/ntfy`
