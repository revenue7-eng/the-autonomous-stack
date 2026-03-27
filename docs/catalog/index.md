---
title: "Technology Catalog"
nav_order: 5
has_children: true
---

# Technology Catalog

Each technology is evaluated on two axes:

- **Autonomy Level** (A0–A3): operational independence from cloud and internet.
- **Transparency Level** (T0–T2): architectural openness and auditability.

Cards also include a **Trajectory** — is the project moving toward openness or closure?

The catalog includes both autonomous alternatives and the mainstream services they replace. The contrast makes the trade-offs visible.

See [Assessment Scale](assessment-scale.md) for detailed definitions.

*65 technologies evaluated.*

---

## Network

### DNS

| Technology | Autonomy | Transparency | Trajectory | Description |
|------------|----------|--------------|------------|-------------|
| [AdGuard Home](adguard-home.md) | **A3** | **T2** | stable | Network-wide DNS filtering and ad blocking. |
| [Pi-hole](pi-hole.md) | **A3** | **T2** | stable | Network-wide ad blocker and DNS sinkhole. |

### Proxy

| Technology | Autonomy | Transparency | Trajectory | Description |
|------------|----------|--------------|------------|-------------|
| [Nginx Proxy Manager](nginx-proxy-manager.md) | **A3** | **T2** | stable | GUI-based reverse proxy built on Nginx. |
| [Traefik](traefik.md) | **A3** | **T2** | mixed | Modern reverse proxy and load balancer. |

### VPN

| Technology | Autonomy | Transparency | Trajectory | Description |
|------------|----------|--------------|------------|-------------|
| [WireGuard](wireguard.md) | **A3** | **T2** | stable | Fast, modern VPN using state-of-the-art cryptography. |
| [Headscale](headscale.md) | **A3** | **T2** | opening | Self-hosted Tailscale coordination server. |
| [OpenVPN](openvpn.md) | **A3** | **T2** | stable | Battle-tested open-source VPN protocol. |
| [Tailscale](tailscale.md) | **A2** | **T1** | mixed | Mesh VPN built on WireGuard. Proprietary coordination server. |

---

## Storage

### Backup

| Technology | Autonomy | Transparency | Trajectory | Description |
|------------|----------|--------------|------------|-------------|
| [Kopia](kopia.md) | **A3** | **T2** | mixed | Fast encrypted backups with deduplication. Acquired by Veeam. |

### Sync & Cloud

| Technology | Autonomy | Transparency | Trajectory | Description |
|------------|----------|--------------|------------|-------------|
| [Nextcloud](nextcloud.md) | **A3** | **T2** | stable | Self-hosted cloud platform: files, calendar, contacts, collaboration. |
| [Syncthing](syncthing.md) | **A3** | **T2** | stable | Peer-to-peer file synchronisation, no central server. |
| [Google Drive](google-drive.md) | **A0** | **T0** | closing | Cloud file storage by Google. No self-hosting path. |

### Database

| Technology | Autonomy | Transparency | Trajectory | Description |
|------------|----------|--------------|------------|-------------|
| [PostgreSQL](postgresql.md) | **A3** | **T2** | opening | The most advanced open-source relational database. |
| [MariaDB](mariadb.md) | **A3** | **T2** | mixed | Community fork of MySQL. Drop-in replacement. |
| [SQLite](sqlite.md) | **A3** | **T1** | stable | Embedded database. Single file. Zero configuration. |
| [MySQL](mysql.md) | **A3** | **T1** | mixed | Widely deployed relational database. Oracle-owned. |
| [Redis](redis.md) | **A2** | **T1** | closing | In-memory cache and message broker. License changed to non-OSI in 2024. |

---

## Security

### Identity & Auth

| Technology | Autonomy | Transparency | Trajectory | Description |
|------------|----------|--------------|------------|-------------|
| [Authentik](authentik.md) | **A3** | **T2** | stable | Self-hosted identity provider and SSO. |

### Password Managers

| Technology | Autonomy | Transparency | Trajectory | Description |
|------------|----------|--------------|------------|-------------|
| [KeePass](keepass.md) | **A3** | **T2** | stable | Local password manager. GPL-2.0, no cloud component. |
| [Vaultwarden](vaultwarden.md) | **A3** | **T2** | stable | Unofficial Bitwarden-compatible server. MIT license. |
| [Bitwarden](bitwarden.md) | **A3** | **T2** | stable | Official self-hosted password manager. AGPL-3.0. |
| [1Password](1password.md) | **A0** | **T0** | closing | Cloud-only password manager. No self-hosting. |

### Secrets

| Technology | Autonomy | Transparency | Trajectory | Description |
|------------|----------|--------------|------------|-------------|
| [Vault](vault.md) | **A3** | **T1** | closing | Secrets management. License changed from MPL to BSL in 2023. |

---

## Observability

### Metrics & Monitoring

| Technology | Autonomy | Transparency | Trajectory | Description |
|------------|----------|--------------|------------|-------------|
| [Prometheus](prometheus.md) | **A3** | **T2** | opening | CNCF metrics system. Apache-2.0, community governed. |
| [Zabbix](zabbix.md) | **A3** | **T2** | stable | Enterprise-grade open-source monitoring platform. |
| [Netdata](netdata.md) | **A3** | **T2** | mixed | Real-time monitoring. Cloud opt-out required. |
| [Uptime Kuma](uptime-kuma.md) | **A3** | **T2** | stable | Self-hosted uptime and availability monitoring. |

### Dashboards

| Technology | Autonomy | Transparency | Trajectory | Description |
|------------|----------|--------------|------------|-------------|
| [Grafana](grafana.md) | **A3** | **T2** | mixed | Dashboards and alerting. License changed to AGPL in 2021. |

### Logs

| Technology | Autonomy | Transparency | Trajectory | Description |
|------------|----------|--------------|------------|-------------|
| [Loki](loki.md) | **A3** | **T2** | mixed | Log aggregation system by Grafana Labs. |

---

## Compute

| Technology | Autonomy | Transparency | Trajectory | Description |
|------------|----------|--------------|------------|-------------|
| [Docker](docker.md) | **A3** | **T2** | mixed | Container platform. Desktop requires paid license for large orgs. |
| [K3s](k3s.md) | **A3** | **T2** | stable | Lightweight Kubernetes. CNCF project, edge-first. |

---

## Communication

### Messaging

| Technology | Autonomy | Transparency | Trajectory | Description |
|------------|----------|--------------|------------|-------------|
| [Matrix / Element](matrix.md) | **A3** | **T2** | opening | Open standard for decentralised encrypted communication. |
| [Slack](slack.md) | **A0** | **T0** | closing | Cloud-based team messaging. No self-hosting. |
| [Telegram](telegram.md) | **A1** | **T0** | closing | Cloud-based messaging. Server code closed. |

### Email

| Technology | Autonomy | Transparency | Trajectory | Description |
|------------|----------|--------------|------------|-------------|
| [Mailcow](mailcow.md) | **A3** | **T2** | stable | Docker-based self-hosted email server suite. |
| [Stalwart](stalwart.md) | **A3** | **T2** | opening | Modern all-in-one mail server written in Rust. |
| [Proton Mail](protonmail.md) | **A0** | **T1** | closing | Encrypted cloud email. No self-hosting. |
| [Tuta](tuta.md) | **A0** | **T1** | mixed | Encrypted cloud email. Client is GPL-3.0. |
| [Gmail](gmail.md) | **A0** | **T0** | closing | Google cloud email. No self-hosting. |

---

## Applications

### Analytics

| Technology | Autonomy | Transparency | Trajectory | Description |
|------------|----------|--------------|------------|-------------|
| [Plausible Analytics](plausible.md) | **A3** | **T2** | stable | Lightweight, privacy-friendly web analytics. |
| [Umami](umami.md) | **A3** | **T2** | mixed | Simple self-hosted web analytics. MIT license. |
| [Google Analytics](google-analytics.md) | **A0** | **T0** | closing | Cloud-only analytics by Google. |

### Automation

| Technology | Autonomy | Transparency | Trajectory | Description |
|------------|----------|--------------|------------|-------------|
| [Home Assistant](home-assistant.md) | **A3** | **T2** | opening | Local-first home automation. Open Home Foundation. |
| [Node-RED](node-red.md) | **A3** | **T2** | stable | Flow-based visual automation tool. |
| [n8n](n8n.md) | **A3** | **T2** | mixed | Workflow automation. Source-available license. |
| [Zapier](zapier.md) | **A0** | **T0** | closing | Cloud-only workflow automation. |

### CI/CD

| Technology | Autonomy | Transparency | Trajectory | Description |
|------------|----------|--------------|------------|-------------|
| [Woodpecker CI](woodpecker.md) | **A3** | **T2** | opening | Community fork of Drone CI. Apache-2.0. |
| [Gitea Actions](gitea-actions.md) | **A3** | **T2** | opening | Built-in CI/CD for Forgejo/Gitea. GitHub Actions compatible. |
| [Jenkins](jenkins.md) | **A3** | **T2** | stable | The most widely deployed open-source CI/CD server. |

### Documents & Wiki

| Technology | Autonomy | Transparency | Trajectory | Description |
|------------|----------|--------------|------------|-------------|
| [Paperless-ngx](paperless-ngx.md) | **A3** | **T2** | opening | Document management with OCR and search. |
| [BookStack](bookstack.md) | **A3** | **T2** | stable | Self-hosted wiki platform. |
| [Docmost](docmost.md) | **A3** | **T2** | opening | Self-hosted documentation and wiki platform. |
| [Confluence](confluence.md) | **A0** | **T0** | closing | Proprietary wiki by Atlassian. |
| [Notion](notion.md) | **A0** | **T0** | closing | Cloud-only workspace. No self-hosting. |

### Media

| Technology | Autonomy | Transparency | Trajectory | Description |
|------------|----------|--------------|------------|-------------|
| [Jellyfin](jellyfin.md) | **A3** | **T2** | opening | Community fork of Emby. GPL-2.0, no cloud. |
| [Plex](plex.md) | **A1** | **T0** | closing | Media server moving toward platform. Requires Plex servers. |

### Notes

| Technology | Autonomy | Transparency | Trajectory | Description |
|------------|----------|--------------|------------|-------------|
| [Joplin](joplin.md) | **A3** | **T2** | stable | Open-source note-taking with E2E encryption. |
| [Logseq](logseq.md) | **A3** | **T2** | mixed | Local-first knowledge graph. DB version adds uncertainty. |
| [Obsidian](obsidian.md) | **A2** | **T0** | mixed | Local Markdown notes. Proprietary app. |

### Photos

| Technology | Autonomy | Transparency | Trajectory | Description |
|------------|----------|--------------|------------|-------------|
| [Immich](immich.md) | **A3** | **T2** | stable | Self-hosted photo and video backup. AGPL-3.0. |
| [PhotoPrism](photoprism.md) | **A3** | **T2** | mixed | AI-powered photo management. PhotoPrism+ is paid. |

### Version Control

| Technology | Autonomy | Transparency | Trajectory | Description |
|------------|----------|--------------|------------|-------------|
| [Forgejo](forgejo.md) | **A3** | **T2** | opening | Community fork of Gitea. Governed by Codeberg e.V. |

---

*The catalog grows. Contributions welcome — see [CONTRIBUTING](../../CONTRIBUTING.md).*
