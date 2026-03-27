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

*57 technologies evaluated.*

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
| [Nginx Proxy Manager](nginx-proxy-manager.md) | **A3** | **T2** | GUI-based reverse proxy built on Nginx. |
| [Traefik](traefik.md) | **A3** | **T2** | Modern reverse proxy and load balancer designed for microservices and container environments. |

### VPN

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [WireGuard](wireguard.md) | **A3** | **T2** | Extremely simple yet fast and modern VPN that utilizes state‑of‑the‑art cryptography. |
| [OpenVPN](openvpn.md) | **A3** | **T2** | Battle-tested open-source VPN protocol and implementation. |
| [Headscale](headscale.md) | **A3** | **T2** | Self-hosted implementation of the Tailscale coordination server. |
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
| [Zabbix](zabbix.md) | **A3** | **T2** | Enterprise-grade open-source monitoring platform. |
| [Netdata](netdata.md) | **A3** | **T2** | Real-time performance monitoring with zero configuration. |
| [Uptime Kuma](uptime-kuma.md) | **A3** | **T2** | Self-hosted monitoring tool that tracks the availability of websites, services, and network endpoints. |

---

## Compute

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Docker](docker.md) | **A3** | **T2** | Platform for developing, shipping, and running applications in lightweight containers. |
| [K3s](k3s.md) | **A3** | **T2** | Lightweight certified Kubernetes distribution built for edge, IoT, and resource‑constrained environments. |

---

## Security

### Password Manager

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [KeePass](keepass.md) | **A3** | **T2** | Free, open source password manager that stores credentials in a locally encrypted database file (`.kdbx`). |
| [Bitwarden](bitwarden.md) | **A3** | **T2** | Open-source password manager with end-to-end encryption. |
| [Vaultwarden](vaultwarden.md) | **A3** | **T2** | Lightweight, self-hosted implementation of the Bitwarden password manager API. |
| [1Password](1password.md) | **A0** | **T0** | Cloud-based password manager with polished clients for all platforms. |

### Secrets

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Vault](vault.md) | **A3** | **T2** | Secure, encrypted storage for secrets, API keys, certificates, and other sensitive data. |

---

## Applications

### Automation

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Home Assistant](home-assistant.md) | **A3** | **T2** | Open-source home automation platform that puts local control and privacy first. |
| [Node-RED](node-red.md) | **A3** | **T2** | Flow-based visual automation tool built on Node.js. |
| [n8n](n8n.md) | **A3** | **T2** | Source-available workflow automation platform. |
| [Zapier](zapier.md) | **A0** | **T0** | Cloud-based workflow automation platform. |

### Cloud Platform

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Nextcloud](nextcloud.md) | **A3** | **T2** | Self-hosted cloud platform providing file sync, calendar, contacts, email, office documents, video calls, and more -- al... |

### Documents

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Paperless-ngx](paperless-ngx.md) | **A3** | **T2** | Document management system that transforms your physical and digital documents into a searchable, organized archive. |
| [Notion](notion.md) | **A0** | **T0** | All‑in‑one workspace for notes, documents, databases, wikis, and project management. |

### General

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Jenkins](jenkins.md) | **A3** | **T2** | The most widely deployed open-source CI/CD server. |
| [Docmost](docmost.md) | **A3** | **T2** | Open-source, self-hosted documentation and wiki platform. |
| [Gitea Actions](gitea-actions.md) | **A3** | **T2** | Built-in CI/CD for Gitea and Forgejo. |
| [Forgejo](forgejo.md) | **A3** | **T2** | Self-hosted Git service with a focus on lightweight operation, open governance, and built-in CI/CD via Actions. |
| [Woodpecker CI](woodpecker.md) | **A3** | **T2** | Community fork of Drone CI after Harness acquired it and moved it toward a commercial model. |
| [BookStack](bookstack.md) | **A3** | **T2** | Open-source, self-hosted wiki platform built with PHP and Laravel. |
| [Confluence](confluence.md) | **A0** | **T0** | Proprietary wiki and collaboration platform by Atlassian. |

### Media

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Jellyfin](jellyfin.md) | **A3** | **T2** | Free software media server that streams your personal media collection without cloud dependencies. |
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
| [PhotoPrism](photoprism.md) | **A3** | **T2** | AI-powered self-hosted photo management. |
| [Immich](immich.md) | **A3** | **T2** | Self-hosted photo and video backup solution with a focus on user experience, automatic organisation, and machine learnin... |

---

## Other

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Matrix / Element](matrix.md) | **A3** | **T2** | Matrix is an open standard for decentralized, end-to-end encrypted communication. |
| [Umami](umami.md) | **A3** | **T2** | Simple, fast, privacy-focused web analytics. |
| [Mailcow](mailcow.md) | **A3** | **T2** | Open-source, Docker-based email server suite. |
| [Plausible Analytics](plausible.md) | **A3** | **T2** | Lightweight, privacy-friendly web analytics. |
| [Stalwart](stalwart.md) | **A3** | **T2** | All-in-one mail and collaboration server written in Rust. |
| [Telegram](telegram.md) | **A1** | **T0** | Cloud-based messaging platform. |
| [Tuta (Tutanota)](tuta.md) | **A0** | **T1** | End-to-end encrypted email and calendar. |
| [Proton Mail](protonmail.md) | **A0** | **T1** | Encrypted email service with zero-knowledge architecture. |
| [Google Analytics](google-analytics.md) | **A0** | **T0** | Cloud-only web analytics platform by Google. |
| [Gmail](gmail.md) | **A0** | **T0** | Google's cloud email service. |
| [Slack](slack.md) | **A0** | **T0** | Cloud-based team messaging platform. |

---

*The catalog grows. Contributions welcome — see [CONTRIBUTING](../../CONTRIBUTING.md).*
