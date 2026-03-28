---
title: "Technology Catalog"
nav_order: 5
has_children: true
---

# Technology Catalog

Each technology is evaluated on two axes:

- **Autonomy Level** (A0–A3): operational independence from cloud and internet.
- **Transparency Level** (T0–T2): architectural openness and auditability.

Cards also include a **Philosophical Assessment** — Pause, Exit, Recoverability, Visibility — based on the [whose.world](https://whose.world) criteria.

The catalog includes both autonomous alternatives and the mainstream services they replace. The contrast makes the trade-offs visible.

See [Assessment Scale](assessment-scale.md) for detailed definitions.

*88 technologies evaluated.*

---

## Network

### DNS

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [AdGuard Home](adguard-home.md) | **A3** | **T2** | Network-wide software for blocking ads, trackers, and malware. |
| [Pi-hole](pi-hole.md) | **A3** | **T2** | Network-wide ad blocker and DNS sinkhole. |

### Proxy

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Caddy](caddy.md) | **A3** | **T2** | Fast, extensible, cross-platform web server with automatic HTTPS. |
| [Nginx Proxy Manager](nginx-proxy-manager.md) | **A3** | **T2** | GUI-based reverse proxy built on Nginx. |
| [Traefik](traefik.md) | **A3** | **T2** | Modern reverse proxy and load balancer designed for microservices and container environments. |

### VPN

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Headscale](headscale.md) | **A3** | **T2** | Self-hosted implementation of the Tailscale coordination server. |
| [OpenVPN](openvpn.md) | **A3** | **T2** | Battle-tested open-source VPN protocol and implementation. |
| [WireGuard](wireguard.md) | **A3** | **T2** | Extremely simple yet fast and modern VPN that utilizes state‑of‑the‑art cryptography. |
| [Tailscale](tailscale.md) | **A2** | **T1** | Mesh VPN built on WireGuard. |

---

## Identity

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Authentik](authentik.md) | **A3** | **T2** | Open-source identity provider focused on flexibility and security. |

---

## Storage

### Backup

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Kopia](kopia.md) | **A3** | **T2** | Fast and secure open-source backup/restore tool with snapshots, deduplication, compression, and client-side encryption. |
| [Restic](restic.md) | **A3** | **T2** | Fast, secure, and efficient backup program. |

### Cache

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Redis](redis.md) | **A2** | **T1** | In-memory data structure store. |

### Cloud

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [MinIO](minio.md) | **A3** | **T2** | High-performance, S3-compatible object storage. |

### Database

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [MariaDB](mariadb.md) | **A3** | **T2** | Community-developed fork of MySQL created by MySQL's original author (Monty Widenius) after Oracle's acquisition. |
| [MySQL](mysql.md) | **A3** | **T1** | The world's most widely deployed open-source relational database. |
| [PostgreSQL](postgresql.md) | **A3** | **T2** | The world's most advanced open-source relational database. |
| [SQLite](sqlite.md) | **A3** | **T1** | The most widely deployed database engine in the world — embedded in every smartphone, browser, and operating system. |

### Sync

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Syncthing](syncthing.md) | **A3** | **T2** | Peer‑to‑peer file synchronisation tool that keeps folders in sync across multiple devices — without a central server, wi... |
| [Google Drive](google-drive.md) | **A0** | **T0** | Cloud file storage and synchronisation service by Google. |

---

## Observability

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Loki](loki.md) | **A3** | **T2** | Log aggregation system by Grafana Labs. |

### Dashboards

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Grafana](grafana.md) | **A3** | **T2** | Open-source observability and data visualisation platform. |

### Metrics

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Prometheus](prometheus.md) | **A3** | **T2** | Open‑source monitoring system that collects metrics from targets, stores them locally, and enables powerful querying, al... |

### Monitoring

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Netdata](netdata.md) | **A3** | **T2** | Real-time performance monitoring with zero configuration. |
| [Uptime Kuma](uptime-kuma.md) | **A3** | **T2** | Self-hosted monitoring tool that tracks the availability of websites, services, and network endpoints. |
| [Zabbix](zabbix.md) | **A3** | **T2** | Enterprise-grade open-source monitoring platform. |

---

## Compute

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Docker](docker.md) | **A3** | **T2** | Platform for developing, shipping, and running applications in lightweight containers. |
| [Dockge](dockge.md) | **A3** | **T2** | Simple, reactive Docker Compose manager with a web UI. |
| [K3s](k3s.md) | **A3** | **T2** | Lightweight certified Kubernetes distribution built for edge, IoT, and resource‑constrained environments. |
| [Ollama](ollama.md) | **A3** | **T2** | Local large language model runtime. |
| [Portainer](portainer.md) | **A3** | **T2** | Web-based GUI for managing Docker, Kubernetes, and Swarm environments. |
| [Watchtower](watchtower.md) | **A3** | **T2** | Automated Docker container updater. |

---

## Security

### General

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [CrowdSec](crowdsec.md) | **A2** | **T2** | Open-source intrusion detection and prevention system with crowdsourced threat intelligence. |

### Password Manager

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Bitwarden](bitwarden.md) | **A3** | **T2** | Open-source password manager with end-to-end encryption. |
| [KeePass](keepass.md) | **A3** | **T2** | Free, open source password manager that stores credentials in a locally encrypted database file (`.kdbx`). |
| [Vaultwarden](vaultwarden.md) | **A3** | **T2** | Lightweight, self-hosted implementation of the Bitwarden password manager API. |
| [1Password](1password.md) | **A0** | **T0** | Cloud-based password manager with polished clients for all platforms. |

### Secrets

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Vault](vault.md) | **A3** | **T1** | Secure, encrypted storage for secrets, API keys, certificates, and other sensitive data. |

---

## Communication

### Email

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Mailcow](mailcow.md) | **A3** | **T2** | Open-source, Docker-based email server suite. |
| [Stalwart](stalwart.md) | **A3** | **T2** | All-in-one mail and collaboration server written in Rust. |
| [Gmail](gmail.md) | **A0** | **T0** | Google's cloud email service. |
| [Proton Mail](protonmail.md) | **A0** | **T1** | Encrypted email service with zero-knowledge architecture. |
| [Tuta (Tutanota)](tuta.md) | **A0** | **T1** | End-to-end encrypted email and calendar. |

### General

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Ntfy](ntfy.md) | **A3** | **T2** | Simple HTTP-based pub-sub notification service. |

### Messaging

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Matrix / Element](matrix.md) | **A3** | **T2** | Matrix is an open standard for decentralized, end-to-end encrypted communication. |
| [Telegram](telegram.md) | **A1** | **T0** | Cloud-based messaging platform. |
| [Slack](slack.md) | **A0** | **T0** | Cloud-based team messaging platform. |

---

## Analytics

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Plausible Analytics](plausible.md) | **A3** | **T2** | Lightweight, privacy-friendly web analytics. |
| [Umami](umami.md) | **A3** | **T2** | Simple, fast, privacy-focused web analytics. |
| [Google Analytics](google-analytics.md) | **A0** | **T0** | Cloud-only web analytics platform by Google. |

---

## Applications

### Automation

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Home Assistant](home-assistant.md) | **A3** | **T2** | Open-source home automation platform that puts local control and privacy first. |
| [n8n](n8n.md) | **A3** | **T1** | Source-available workflow automation platform. |
| [Node-RED](node-red.md) | **A3** | **T2** | Flow-based visual automation tool built on Node.js. |
| [Zapier](zapier.md) | **A0** | **T0** | Cloud-based workflow automation platform. |

### CI/CD

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Gitea Actions](gitea-actions.md) | **A3** | **T2** | Built-in CI/CD for Gitea and Forgejo. |
| [Jenkins](jenkins.md) | **A3** | **T2** | The most widely deployed open-source CI/CD server. |
| [Woodpecker CI](woodpecker.md) | **A3** | **T2** | Community fork of Drone CI after Harness acquired it and moved it toward a commercial model. |

### Cloud Platform

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Homepage](homepage.md) | **A3** | **T2** | Highly customizable, self-hosted application dashboard with Docker auto-discovery and over 100 service integrations. |
| [Nextcloud](nextcloud.md) | **A3** | **T2** | Self-hosted cloud platform providing file sync, calendar, contacts, email, office documents, video calls, and more -- al... |

### Documents

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Paperless-ngx](paperless-ngx.md) | **A3** | **T2** | Document management system that transforms your physical and digital documents into a searchable, organized archive. |
| [The Autonomous Stack (TAS)](the-autonomous-stack.md) | **A2** | **T2** | An open-source decision framework for evaluating and building infrastructure you control. |
| [Notion](notion.md) | **A0** | **T0** | All‑in‑one workspace for notes, documents, databases, wikis, and project management. |

### Documents & Wiki

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [BookStack](bookstack.md) | **A3** | **T2** | Open-source, self-hosted wiki platform built with PHP and Laravel. |
| [Docmost](docmost.md) | **A3** | **T2** | Open-source, self-hosted documentation and wiki platform. |
| [Confluence](confluence.md) | **A0** | **T0** | Proprietary wiki and collaboration platform by Atlassian. |

### General

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Actual Budget](actual-budget.md) | **A3** | **T2** | Local-first personal finance and budgeting app. |
| [File Browser](filebrowser.md) | **A3** | **T2** | Web-based file manager. |
| [FreshRSS](freshrss.md) | **A3** | **T2** | Self-hosted RSS/Atom feed aggregator. |
| [Grocy](grocy.md) | **A3** | **T2** | Self-hosted grocery and household management. |
| [Apache Guacamole](guacamole.md) | **A3** | **T2** | Clientless remote desktop gateway. |
| [Linkding](linkding.md) | **A3** | **T2** | Minimal self-hosted bookmark manager. |
| [Mealie](mealie.md) | **A3** | **T2** | Self-hosted recipe manager and meal planner. |
| [qBittorrent](qbittorrent.md) | **A3** | **T2** | Open-source BitTorrent client with a web UI. |
| [RustDesk](rustdesk.md) | **A3** | **T2** | Self-hosted remote desktop application written in Rust. |
| [SearXNG](searxng.md) | **A3** | **T2** | Privacy-respecting metasearch engine that aggregates results from 70+ search engines without tracking users. |
| [Wallabag](wallabag.md) | **A3** | **T2** | Self-hosted read-it-later service. |

### Media

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Jellyfin](jellyfin.md) | **A3** | **T2** | Free software media server that streams your personal media collection without cloud dependencies. |
| [Prowlarr](prowlarr.md) | **A3** | **T2** | Indexer manager for the *arr stack. |
| [Radarr](radarr.md) | **A3** | **T2** | Automated movie collection manager. |
| [Sonarr](sonarr.md) | **A3** | **T2** | Automated TV series collection manager. |
| [Plex](plex.md) | **A1** | **T0** | Media server that organises and streams your personal media collection. |

### Notes

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Joplin](joplin.md) | **A3** | **T2** | Open-source note-taking app with end-to-end encryption. |
| [Logseq](logseq.md) | **A3** | **T2** | Local-first outliner and knowledge graph. |
| [Obsidian](obsidian.md) | **A2** | **T0** | Local-first knowledge management app based on plain Markdown files stored on your device. |

### Photos

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Immich](immich.md) | **A3** | **T2** | Self-hosted photo and video backup solution with a focus on user experience, automatic organisation, and machine learnin... |
| [PhotoPrism](photoprism.md) | **A3** | **T2** | AI-powered self-hosted photo management. |

### Version Control

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Forgejo](forgejo.md) | **A3** | **T2** | Self-hosted Git service with a focus on lightweight operation, open governance, and built-in CI/CD via Actions. |
| [Gitea](gitea.md) | **A3** | **T2** | Lightweight self-hosted Git service. |

---

*The catalog grows. [Add a technology →](../card-builder.html) or see [CONTRIBUTING](../../CONTRIBUTING.md).*
