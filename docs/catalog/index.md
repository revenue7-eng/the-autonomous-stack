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

The catalog includes both autonomous alternatives and the mainstream services they replace. The contrast makes the trade‑offs visible.

See [Assessment Scale](assessment-scale.md) for detailed definitions.

---

## Network

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [WireGuard](wireguard.md) | **A3** | **T2** | Simple, fast VPN without central servers. |
| [AdGuard Home](adguard-home.md) | **A3** | **T2** | Network-wide ad blocking and DNS filtering. |
| [Pi-hole](pi-hole.md) | **A3** | **T2** | DNS sinkhole for network-wide ad blocking. |
| [Traefik](traefik.md) | **A3** | **T2** | Modern reverse proxy with auto-discovery and auto-HTTPS. |
| [Nginx Proxy Manager](nginx-proxy-manager.md) | **A3** | **T2** | GUI-based reverse proxy built on Nginx. |
| [Tailscale](tailscale.md) | **A2** | **T1** | Mesh VPN built on WireGuard. Convenient, but depends on central coordination server. |

---

## Identity

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Authentik](authentik.md) | **A3** | **T2** | Open‑source identity provider with SSO, MFA, LDAP. |

---

## Storage

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Syncthing](syncthing.md) | **A3** | **T2** | P2P file synchronisation without cloud. |
| [Kopia](kopia.md) | **A3** | **T2** | Fast, encrypted backups with snapshots. |
| [Google Drive](google-drive.md) | **A0** | **T0** | Cloud file storage. Seamless, but you don't own it. |

---

## Observability

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Uptime Kuma](uptime-kuma.md) | **A3** | **T2** | Self‑hosted monitoring dashboard. |
| [Prometheus](prometheus.md) | **A3** | **T2** | Metrics collection, storage, and alerting. |
| [Grafana](grafana.md) | **A3** | **T2** | Dashboards and visualisation for metrics, logs, traces. |

---

## Compute

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Docker](docker.md) | **A3** | **T2** | Container runtime and platform. |
| [K3s](k3s.md) | **A3** | **T2** | Lightweight Kubernetes distribution. |

---

## Security

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Vault](vault.md) | **A3** | **T2** | Secure secrets management and encryption. |
| [Vaultwarden](vaultwarden.md) | **A3** | **T2** | Self-hosted Bitwarden-compatible password manager. |

---

## Applications

### Media

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Jellyfin](jellyfin.md) | **A3** | **T2** | Self‑hosted media server without cloud. |
| [Plex](plex.md) | **A1** | **T0** | Popular media server, but requires cloud account for auth. |

### Version Control

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Forgejo](forgejo.md) | **A3** | **T2** | Lightweight self‑hosted Git with Actions. |

### Photos

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Immich](immich.md) | **A3** | **T2** | Self‑hosted photo and video backup solution. |

### Documents

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Paperless‑ngx](paperless-ngx.md) | **A3** | **T2** | Document management system with OCR. |
| [Notion](notion.md) | **A0** | **T0** | All‑in‑one workspace. Powerful, but cloud‑only with lossy export. |

### Notes

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Obsidian](obsidian.md) | **A2** | **T0** | Local-first Markdown notes. Data is yours, app is proprietary. |

### Cloud Platform

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Nextcloud](nextcloud.md) | **A3** | **T2** | Self-hosted cloud: files, calendar, contacts, office, video calls. |

### Automation

| Technology | Autonomy | Transparency | Description |
|------------|----------|--------------|-------------|
| [Home Assistant](home-assistant.md) | **A3** | **T2** | Local-first smart home automation with 2000+ integrations. |

---

*The catalog grows. Contributions welcome — see [CONTRIBUTING](../../CONTRIBUTING.md).*
