---
title: "Recommended Stack"
nav_order: 2
---

# Recommended Stack

4 ready-to-deploy recipes and 39 individual recommendations out of 88 technologies evaluated.

---

## Start Here: Recommended Recipes

Complete stacks you can deploy in one afternoon. Docker Compose, step-by-step instructions, failure modes, and cost comparison included.

| Recipe | What it solves | What it replaces | Key components |
|--------|---------------|-----------------|----------------|
| [Minimal Server](recipes/minimal-server.md) | Foundation for everything else | Cloud VPS + basic services | WireGuard, AdGuard Home, Syncthing, Kopia, Forgejo |
| [Family Cloud](recipes/family-cloud.md) | Family photos, files, passwords | Google Photos + Drive + iCloud + LastPass | Immich, Nextcloud, Vaultwarden, Syncthing |
| [Media Server](recipes/media-server.md) | Movies and TV, automated | Netflix + Disney+ + HBO ($63/mo) | Jellyfin, Radarr, Sonarr, Prowlarr, qBittorrent |
| [Home Office](recipes/home-office.md) | Remote work tools | Google Workspace + ChatGPT ($35/mo) | Nextcloud, Ollama, SearXNG, Joplin, FreshRSS |

All 8 recipes (including Monitoring, Communication, Privacy Homelab, Developer Workstation) are in the [Recipes](recipes/) section.

---

## Individual Recommendations

| Need | We recommend | Why this one | Replaces |
|------|-------------|-------------|----------|
| **VPN** | [WireGuard](catalog/wireguard.md) | Fastest, simplest, most audited. Built into Linux kernel. | Tailscale, OpenVPN |
| **DNS filtering** | [AdGuard Home](catalog/adguard-home.md) | Blocks ads and trackers network-wide. Better UI than Pi-hole, DoH/DoT support. | Pi-hole, NextDNS |
| **Reverse proxy** | [Caddy](catalog/caddy.md) | Automatic HTTPS, zero-config. Single binary. | Nginx, Traefik, NPM |
| **Identity / SSO** | [Authentik](catalog/authentik.md) | Full identity provider. One login for all services. | Keycloak, Authelia |
| **File sync** | [Syncthing](catalog/syncthing.md) | Peer-to-peer, no server needed. Works offline. | Google Drive, Dropbox |
| **Backup** | [Kopia](catalog/kopia.md) | Encrypted, deduplicated, client-side. Fast. | Restic, Borg |
| **Database** | [PostgreSQL](catalog/postgresql.md) | The most advanced open-source database. Everything depends on it. | MySQL, MariaDB |
| **Passwords** | [Vaultwarden](catalog/vaultwarden.md) | Bitwarden-compatible, lightweight, self-hosted. Family sharing built in. | 1Password, LastPass |
| **Photos** | [Immich](catalog/immich.md) | Google Photos replacement. Auto-backup from phone, face recognition, maps. | Google Photos, iCloud |
| **Documents** | [Paperless-ngx](catalog/paperless-ngx.md) | Scan, OCR, tag, search all your documents. | Google Drive, filing cabinets |
| **Notes** | [Joplin](catalog/joplin.md) | Markdown notes with E2E encryption. Sync via Syncthing or Nextcloud. | Notion, Evernote |
| **Cloud platform** | [Nextcloud](catalog/nextcloud.md) | Files + calendar + contacts + office. The all-in-one. | Google Workspace |
| **Media server** | [Jellyfin](catalog/jellyfin.md) | Stream your media library. No account required, no telemetry. | Plex |
| **Email** | [Stalwart](catalog/stalwart.md) | All-in-one mail server in Rust. SMTP + IMAP + JMAP. Modern and fast. | Gmail, Proton Mail |
| **Messaging** | [Matrix / Element](catalog/matrix.md) | Decentralized, encrypted, federated. | Slack, Telegram |
| **Monitoring** | [Uptime Kuma](catalog/uptime-kuma.md) | Simple, beautiful uptime monitoring with alerts. | Pingdom, StatusCake |
| **Metrics** | [Prometheus](catalog/prometheus.md) + [Grafana](catalog/grafana.md) | Industry standard. Scrape, store, visualize. | Datadog, New Relic |
| **Logs** | [Loki](catalog/loki.md) | Log aggregation by Grafana Labs. Lightweight, pairs with Grafana. | Splunk, ELK |
| **Git hosting** | [Forgejo](catalog/forgejo.md) | Community fork of Gitea. Lightweight, self-hosted GitHub alternative. | GitHub, GitLab |
| **CI/CD** | [Woodpecker CI](catalog/woodpecker.md) | Simple, container-native CI. Pairs with Forgejo. | GitHub Actions, Jenkins |
| **Containers** | [Docker](catalog/docker.md) | The foundation. Everything else runs on it. | Podman |
| **Automation** | [n8n](catalog/n8n.md) | Visual workflow automation. Self-hosted Zapier alternative. | Zapier, Make |
| **Home automation** | [Home Assistant](catalog/home-assistant.md) | Local-first smart home. 2000+ integrations, no cloud required. | Google Home, Alexa |
| **Analytics** | [Plausible](catalog/plausible.md) | Privacy-friendly web analytics. No cookies, GDPR-compliant. | Google Analytics |
| **Dashboard** | [Homepage](catalog/homepage.md) | Landing page for all your services. Docker auto-discovery. | Dashy, Homer |
| **Security / IDS** | [CrowdSec](catalog/crowdsec.md) | Crowdsourced intrusion detection. Modern Fail2Ban. | Fail2Ban, OSSEC |
| **Object storage** | [MinIO](catalog/minio.md) | S3-compatible. For backups, media, data lakes. | AWS S3 |
| **Notifications** | [Ntfy](catalog/ntfy.md) | One curl command to push alerts to your phone. Dead simple. | Pushover, Firebase |
| **Search** | [SearXNG](catalog/searxng.md) | Privacy-respecting metasearch. No tracking, no profiling. | Google Search |
| **LLM runtime** | [Ollama](catalog/ollama.md) | Run open-weight models locally. OpenAI-compatible API. | ChatGPT, Claude API |
| **RSS reader** | [FreshRSS](catalog/freshrss.md) | Read what you choose, in order, no algorithm. | Google News, Feedly |
| **Recipes** | [Mealie](catalog/mealie.md) | Family cookbook, meal planner, shopping lists. | Yummly, Paprika |
| **Remote desktop** | [RustDesk](catalog/rustdesk.md) | Self-hosted TeamViewer. Peer-to-peer, works on all platforms. | TeamViewer, AnyDesk |
| **Budgeting** | [Actual Budget](catalog/actual-budget.md) | Local-first personal finance. Was paid SaaS, now open source. | YNAB, Mint |
| **Read later** | [Wallabag](catalog/wallabag.md) | Save articles, read offline, strip ads. Your personal archive. | Pocket, Instapaper |
| **Container updates** | [Watchtower](catalog/watchtower.md) | Auto-updates your Docker containers. Set and forget. | Manual docker pull |
| **Media automation** | [Radarr](catalog/radarr.md) + [Sonarr](catalog/sonarr.md) + [Prowlarr](catalog/prowlarr.md) | Automated movie and TV collection. Prowlarr manages indexers for both. | Manual downloads |
| **Download client** | [qBittorrent](catalog/qbittorrent.md) | Open-source, no ads, web UI. The engine behind the *arr stack. | uTorrent, Transmission |
| **Backup (CLI)** | [Restic](catalog/restic.md) | Encrypted, deduplicated, scriptable. For cron jobs and automation. | Duplicati, CrashPlan |

---

## How to read this

Every recommendation is **A3/T2** (fully autonomous, open source) unless noted. This means:

- You can **stop** it without losing data
- You can **leave** and take everything with you
- You can **recover** if something breaks
- You can **see** exactly how it works

The "Replaces" column shows what most people are switching from. It's not a judgment — it's a map of the migration path.

---

## Where to go next

**Ready to deploy?** Pick a recipe:

- [Minimal Autonomous Server](recipes/minimal-server.md) — the foundation
- [Family Cloud](recipes/family-cloud.md) — replace Google Photos + Drive + passwords
- [Monitoring Stack](recipes/monitoring-stack.md) — see what's happening
- [Communication Server](recipes/communication-server.md) — email + messaging
- [Privacy-First Homelab](recipes/privacy-first-homelab.md) — maximum privacy
- [Developer Workstation](recipes/developer-workstation.md) — Git + CI/CD + tools

**Want the full picture?** Browse the [Technology Catalog](catalog/) — 88 technologies with detailed assessments.

**Missing a technology?** [Add it yourself →](card-builder.html) — no GitHub account needed.

**Want to see relationships?** Open the [Dependency Graph](dependency-graph.html) — how everything connects.
