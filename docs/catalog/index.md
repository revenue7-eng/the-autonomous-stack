---
title: "Technology Catalog"
nav_order: 7
has_children: true
---

# Technology Catalog

Each technology is evaluated on two axes:

- **Autonomy Level** (A0–A3): operational independence from cloud and internet.
- **Transparency Level** (T0–T2): architectural openness and auditability.

Cards also include a **Philosophical Assessment** — Pause, Exit, Recoverability, Visibility — based on the [whose.world](https://whose.world) criteria.

The catalog includes both autonomous alternatives and the mainstream services they replace. The contrast makes the trade-offs visible.

See [Assessment Scale](assessment-scale.md) for detailed definitions.

*122 technologies evaluated.*

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
| [MySQL](mysql.md) | **A3** | **T2** | The world's most widely deployed open-source relational database. |
| [PostgreSQL](postgresql.md) | **A3** | **T2** | The world's most advanced open-source relational database. |
| [SQLite](sqlite.md) | **A3** | **T1** | The most widely deployed database engine in the world — embedded in every smartphone, browser, and operating system. |

### Sync

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Syncthing](syncthing.md) | **A3** | **T2** | Peer-to-peer file synchronisation tool that keeps folders in sync across multiple devices — without a central server, wi... |
| [Google Drive](google-drive.md) | **A0** | **T0** | Cloud file storage and synchronisation service by Google. |

---

## Compute

### Containers

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Docker](docker.md) | **A3** | **T2** | Platform for developing, shipping, and running applications in lightweight containers. |
| [Dockge](dockge.md) | **A3** | **T2** | Simple, reactive Docker Compose manager with a web UI. |
| [Podman](podman.md) | **A3** | **T2** | Daemonless, rootless container engine compatible with Docker CLI. |
| [Portainer](portainer.md) | **A3** | **T2** | Web-based GUI for managing Docker, Kubernetes, and Swarm environments. |
| [Watchtower](watchtower.md) | **A3** | **T2** | Automated Docker container updater. |

### Inference

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Ollama](ollama.md) | **A3** | **T2** | Local large language model runtime. |

### Operating System

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [CalyxOS](calyxos.md) | **A3** | **T2** | Privacy-focused Android OS with microG for basic Google service compatibility. |
| [Debian](debian.md) | **A3** | **T2** | The universal operating system. |
| [GrapheneOS](grapheneos.md) | **A3** | **T2** | Hardened Android-based mobile OS focused on privacy and security. |
| [LineageOS](lineageos.md) | **A3** | **T2** | The longest-running custom Android distribution. |
| [Ubuntu Server](ubuntu-server.md) | **A3** | **T2** | The most widely deployed Linux server distribution. |

### Orchestration

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [K3s](k3s.md) | **A3** | **T2** | Lightweight certified Kubernetes distribution built for edge, IoT, and resource‑constrained environments. |

### Virtualization

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Proxmox VE](proxmox.md) | **A3** | **T2** | Open-source server virtualization platform. |

---

## Security

### 2FA

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Aegis Authenticator](aegis.md) | **A3** | **T2** | Open-source 2FA authenticator for Android. |
| [ente Auth](ente-auth.md) | **A3** | **T2** | Cross-platform 2FA authenticator with end-to-end encrypted cloud backup. |

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

## Communication

### Email

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [FairEmail](fairemail.md) | **A3** | **T2** | Full-featured Android email client. |
| [K-9 Mail / Thunderbird](k9-mail.md) | **A3** | **T2** | Open-source Android email client, now part of the Thunderbird project (Mozilla). |
| [Mailcow](mailcow.md) | **A3** | **T2** | Open-source, Docker-based email server suite. |
| [Stalwart](stalwart.md) | **A3** | **T2** | All-in-one mail and collaboration server written in Rust. |
| [Gmail](gmail.md) | **A0** | **T0** | Google's cloud email service. |
| [Proton Mail](protonmail.md) | **A0** | **T1** | Encrypted email service with zero-knowledge architecture. |
| [Tuta (Tutanota)](tuta.md) | **A0** | **T2** | End-to-end encrypted email and calendar. |

### General

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Ntfy](ntfy.md) | **A3** | **T2** | Simple HTTP-based pub-sub notification service. |

### Messaging

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Matrix / Element](matrix.md) | **A3** | **T2** | Matrix is an open standard for decentralized, end-to-end encrypted communication. |
| [SimpleX Chat](simplex-chat.md) | **A3** | **T2** | Decentralized messenger with no user identifiers — no phone number, no username, no account. |
| [Signal](signal.md) | **A2** | **T2** | End-to-end encrypted messenger with voice and video calls. |
| [Telegram](telegram.md) | **A1** | **T0** | Cloud-based messaging platform. |
| [Briar](briar.md) | **A0** | **T2** | Peer-to-peer encrypted messenger that works over Tor, Wi-Fi, or Bluetooth. |
| [Slack](slack.md) | **A0** | **T0** | Cloud-based team messaging platform. |

---

## Mobile

### App Store

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Aurora Store](aurora-store.md) | **A3** | **T2** | Open-source client for Google Play Store. |
| [F-Droid](f-droid.md) | **A3** | **T2** | Catalogue of free and open-source Android applications. |
| [Neo Store](neo-store.md) | **A3** | **T2** | Modern F-Droid client with Material Design 3 UI. |

### Browser

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Brave](brave.md) | **A3** | **T1** | Chromium-based browser with built-in ad and tracker blocking. |
| [Firefox](firefox.md) | **A3** | **T2** | Open-source web browser by Mozilla. |
| [Mull](mull.md) | **A3** | **T2** | Firefox fork with telemetry removed and privacy hardened. |

### Camera

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Open Camera](open-camera.md) | **A3** | **T2** | Open-source camera app for Android. |

### Keyboard

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [HeliBoard](heliboard.md) | **A3** | **T2** | Open-source keyboard for Android. |
| [OpenBoard](openboard.md) | **A3** | **T2** | Open-source Android keyboard based on AOSP keyboard. |

### Navigation

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Organic Maps](organic-maps.md) | **A3** | **T2** | Fast, lightweight offline maps. |
| [OsmAnd](osmand.md) | **A3** | **T2** | Offline maps and navigation based on OpenStreetMap. |

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

### Bookmarks

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Linkding](linkding.md) | **A3** | **T2** | Minimal self-hosted bookmark manager. |

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
| [Nextcloud](nextcloud.md) | **A3** | **T2** | Self-hosted cloud platform providing file sync, calendar, contacts, email, office documents, video calls, and more — all... |

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

### Downloads

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [qBittorrent](qbittorrent.md) | **A3** | **T2** | Open-source BitTorrent client with a web UI. |

### Files

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [File Browser](filebrowser.md) | **A3** | **T2** | Web-based file manager. |

### Finance

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Actual Budget](actual-budget.md) | **A3** | **T2** | Local-first personal finance and budgeting app. |

### Household

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Grocy](grocy.md) | **A3** | **T2** | Self-hosted grocery and household management. |
| [Mealie](mealie.md) | **A3** | **T2** | Self-hosted recipe manager and meal planner. |

### Media

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [AntennaPod](antennapod.md) | **A3** | **T2** | Open-source podcast player for Android. |
| [Bazarr](bazarr.md) | **A3** | **T2** | Automated subtitle manager for Radarr and Sonarr. |
| [Jellyfin](jellyfin.md) | **A3** | **T2** | Free software media server that streams your personal media collection without cloud dependencies. |
| [NewPipe](newpipe.md) | **A3** | **T2** | Lightweight YouTube frontend for Android. |
| [Overseerr](overseerr.md) | **A3** | **T2** | Media request and discovery tool. |
| [Prowlarr](prowlarr.md) | **A3** | **T2** | Indexer manager for the *arr stack. |
| [Radarr](radarr.md) | **A3** | **T2** | Automated movie collection manager. |
| [Sonarr](sonarr.md) | **A3** | **T2** | Automated TV series collection manager. |
| [Piped](piped.md) | **A2** | **T2** | Privacy-friendly YouTube frontend. |
| [Plex](plex.md) | **A1** | **T0** | Media server that organises and streams your personal media collection. |

### News & RSS

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [FreshRSS](freshrss.md) | **A3** | **T2** | Self-hosted RSS/Atom feed aggregator. |

### Notes

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Joplin](joplin.md) | **A3** | **T2** | Open-source note-taking app with end-to-end encryption. |
| [Logseq](logseq.md) | **A3** | **T2** | Local-first outliner and knowledge graph. |
| [Standard Notes](standard-notes.md) | **A3** | **T2** | End-to-end encrypted notes app. |
| [Obsidian](obsidian.md) | **A2** | **T0** | Local-first knowledge management app based on plain Markdown files stored on your device. |

### Photos

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Ente Photos](ente-photos.md) | **A3** | **T2** | End-to-end encrypted photo storage and backup. |
| [Immich](immich.md) | **A3** | **T2** | Self-hosted photo and video backup solution with a focus on user experience, automatic organisation, and machine learnin... |
| [PhotoPrism](photoprism.md) | **A3** | **T2** | AI-powered self-hosted photo management. |
| [Simple Gallery](simple-gallery.md) | **A3** | **T2** | Offline photo and video gallery for Android. |

### Reading

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Wallabag](wallabag.md) | **A3** | **T2** | Self-hosted read-it-later service. |

### Remote Access

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Apache Guacamole](guacamole.md) | **A3** | **T2** | Clientless remote desktop gateway. |
| [RustDesk](rustdesk.md) | **A3** | **T2** | Self-hosted remote desktop application written in Rust. |

### Search

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [SearXNG](searxng.md) | **A3** | **T2** | Privacy-respecting metasearch engine that aggregates results from 70+ search engines without tracking users. |

### Version Control

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Forgejo](forgejo.md) | **A3** | **T2** | Self-hosted Git service with a focus on lightweight operation, open governance, and built-in CI/CD via Actions. |
| [Gitea](gitea.md) | **A3** | **T2** | Lightweight self-hosted Git service. |

---

*The catalog grows. [Add a technology →](../card-builder.html) or see [CONTRIBUTING](../../CONTRIBUTING.md).*
