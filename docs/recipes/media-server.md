---
title: "Media Server"
parent: Recipes
nav_order: 7
---

# Media Server

Build a self-hosted media center that automatically finds, downloads, organizes, and streams your movies and TV shows. No subscriptions, no content restrictions, no algorithms deciding what you watch.

---

## Goal

Create a media server that:

- Streams your movie and TV library to any device (TV, phone, tablet, browser)
- Automatically monitors for new movies and TV episodes you want
- Searches and downloads content through your configured indexers
- Organizes files with proper naming, metadata, and artwork
- Routes download traffic through VPN for privacy
- Runs entirely self-hosted — no accounts, no cloud

---

## Components

| Component | Catalog Card | Role |
|-----------|--------------|------|
| **Docker** | [`compute/container`](../catalog/docker.md) | Container runtime |
| **Jellyfin** | [`applications/media`](../catalog/jellyfin.md) | Media server — stream to all devices |
| **Radarr** | [`applications/media`](../catalog/radarr.md) | Movie collection manager |
| **Sonarr** | [`applications/media`](../catalog/sonarr.md) | TV series collection manager |
| **Prowlarr** | [`applications/media`](../catalog/prowlarr.md) | Indexer manager for Radarr and Sonarr |
| **qBittorrent** | [`applications/downloads`](../catalog/qbittorrent.md) | Download client |
| **WireGuard** | [`network/vpn`](../catalog/wireguard.md) | VPN for download traffic |
| **Caddy** | [`network/proxy`](../catalog/caddy.md) | Reverse proxy with HTTPS |

*All are A3/T2.*

---

## Who is this for?

- Anyone paying for multiple streaming services and tired of content disappearing
- People who already have a media collection and want to stream it properly
- Families who want one place for all their movies and shows
- Anyone who wants automated library management instead of manual downloads

**Estimated setup time:** 2–3 hours.
**Minimum hardware:** Any x86 machine with 4 GB RAM. Storage depends on your library — plan for 1–4 TB. A dedicated HDD or NAS is recommended for media storage.

---

## Architecture

```
              ┌──────────┐
              │ Prowlarr │ ← manages indexers
              └────┬─────┘
                   │ syncs indexers to
          ┌────────┴────────┐
          ▼                 ▼
     ┌─────────┐      ┌─────────┐
     │ Radarr  │      │ Sonarr  │ ← monitor for wanted content
     │ (movies)│      │  (TV)   │
     └────┬────┘      └────┬────┘
          │                │
          └───────┬────────┘
                  ▼ sends downloads to
          ┌──────────────┐
          │ qBittorrent  │ ← downloads via VPN
          │  (WireGuard) │
          └──────┬───────┘
                 │ completed files
                 ▼
          ┌──────────┐
          │ Jellyfin │ ← streams to devices
          └──────────┘
```

---

## Step-by-Step Instructions

### 1. Create Project Directory

```bash
mkdir -p /opt/media-server && cd /opt/media-server
mkdir -p data/{jellyfin,radarr,sonarr,prowlarr,qbittorrent}
mkdir -p media/{movies,tv}
mkdir -p downloads/{complete,incomplete}
```

### 2. Set Up WireGuard VPN

Get a VPN provider that supports WireGuard (Mullvad, IVPN, AirVPN, etc.). Download the WireGuard configuration file.

Create `config/wg0.conf` with your provider's settings:

```ini
[Interface]
PrivateKey = YOUR_PRIVATE_KEY
Address = 10.x.x.x/32
DNS = 10.x.x.x

[Peer]
PublicKey = PROVIDER_PUBLIC_KEY
AllowedIPs = 0.0.0.0/0
Endpoint = PROVIDER_SERVER:51820
```

### 3. Create Docker Compose

```bash
cat > docker-compose.yml << 'YAMLEOF'
services:

  # ── VPN Container ──────────────────────────────────
  # qBittorrent routes ALL traffic through this VPN
  wireguard:
    image: linuxserver/wireguard
    container_name: wireguard
    cap_add:
      - NET_ADMIN
      - SYS_MODULE
    environment:
      - TZ=UTC
    volumes:
      - ./config/wg0.conf:/config/wg_confs/wg0.conf
    sysctls:
      - net.ipv4.conf.all.src_valid_mark=1
    ports:
      # qBittorrent WebUI (routed through VPN)
      - "8080:8080"
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "ping", "-c", "1", "1.1.1.1"]
      interval: 30s
      timeout: 5s
      retries: 3

  # ── Download Client (behind VPN) ───────────────────
  qbittorrent:
    image: linuxserver/qbittorrent
    container_name: qbittorrent
    network_mode: "service:wireguard"
    environment:
      - TZ=UTC
      - WEBUI_PORT=8080
    volumes:
      - ./data/qbittorrent:/config
      - ./downloads:/downloads
    depends_on:
      wireguard:
        condition: service_healthy
    restart: unless-stopped

  # ── Media Server ───────────────────────────────────
  jellyfin:
    image: jellyfin/jellyfin
    container_name: jellyfin
    ports:
      - "8096:8096"
    volumes:
      - ./data/jellyfin:/config
      - ./media/movies:/data/movies
      - ./media/tv:/data/tvshows
    environment:
      - TZ=UTC
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8096/health"]
      interval: 30s
      timeout: 5s
      retries: 3

  # ── Movie Manager ──────────────────────────────────
  radarr:
    image: linuxserver/radarr
    container_name: radarr
    ports:
      - "7878:7878"
    volumes:
      - ./data/radarr:/config
      - ./media/movies:/movies
      - ./downloads:/downloads
    environment:
      - TZ=UTC
    restart: unless-stopped

  # ── TV Manager ─────────────────────────────────────
  sonarr:
    image: linuxserver/sonarr
    container_name: sonarr
    ports:
      - "8989:8989"
    volumes:
      - ./data/sonarr:/config
      - ./media/tv:/tv
      - ./downloads:/downloads
    environment:
      - TZ=UTC
    restart: unless-stopped

  # ── Indexer Manager ────────────────────────────────
  prowlarr:
    image: linuxserver/prowlarr
    container_name: prowlarr
    ports:
      - "9696:9696"
    volumes:
      - ./data/prowlarr:/config
    environment:
      - TZ=UTC
    restart: unless-stopped

  # ── Reverse Proxy ──────────────────────────────────
  caddy:
    image: caddy:latest
    container_name: caddy
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./config/Caddyfile:/etc/caddy/Caddyfile
      - caddy_data:/data
    restart: unless-stopped

volumes:
  caddy_data:
YAMLEOF
```

### 4. Create Caddyfile (optional — for domain access)

```bash
mkdir -p config
cat > config/Caddyfile << 'EOF'
media.{$DOMAIN} {
    reverse_proxy jellyfin:8096
}
EOF
```

### 5. Deploy

```bash
docker compose up -d
```

### 6. Configure the Stack

**Order matters. Configure in this sequence:**

**6a. Prowlarr** (`:9696`)
1. Add your indexers (Usenet or torrent indexers)
2. Settings → Apps → Add Radarr and Sonarr with their API keys

**6b. qBittorrent** (`:8080`)
1. Default login: admin / check container logs for generated password
2. Settings → Downloads → Set default save path to `/downloads/complete`
3. Verify VPN is working: Tools → Connection → your IP should be the VPN IP

**6c. Radarr** (`:7878`)
1. Settings → Media Management → Add root folder: `/movies`
2. Settings → Download Clients → Add qBittorrent (host: `wireguard`, port: 8080)
3. Movies → Add New → Search for a movie to test

**6d. Sonarr** (`:8989`)
1. Settings → Media Management → Add root folder: `/tv`
2. Settings → Download Clients → Add qBittorrent (host: `wireguard`, port: 8080)
3. Series → Add New → Search for a show to test

**6e. Jellyfin** (`:8096`)
1. Complete the setup wizard
2. Add library: Movies → `/data/movies`
3. Add library: TV Shows → `/data/tvshows`
4. Install mobile apps (iOS/Android) and point to your server

### 7. Verify VPN Protection

**Critical:** Ensure download traffic goes through VPN.

```bash
# Check qBittorrent's external IP (should be VPN, not your real IP)
docker exec wireguard curl -s ifconfig.me
```

If this shows your real IP, the VPN is not working. Do not proceed until fixed.

---

## Failure Modes

| Component | Failure scenario | Impact | Recovery |
|-----------|-----------------|--------|----------|
| **WireGuard** | VPN disconnects | qBittorrent loses internet (by design — kill switch). Downloads pause. | Check VPN config, restart: `docker compose restart wireguard` |
| **qBittorrent** | Crash | Downloads pause. Radarr/Sonarr queue items. | `docker compose restart qbittorrent`. Incomplete downloads resume. |
| **Radarr/Sonarr** | Database corruption | Collection metadata lost. Media files untouched. | Restore from backup. Movies/shows still playable in Jellyfin. |
| **Prowlarr** | Indexer sync fails | New searches fail. Existing library unaffected. | Check indexer status. Re-add indexers if needed. |
| **Jellyfin** | Database corruption | Library metadata lost. Rescan rebuilds from media files. | Delete Jellyfin DB, rescan. All media files are intact. |
| **Caddy** | Config error | Remote access lost | Access via LAN IP:PORT while fixing. |
| **Disk full** | Storage exhausted | Downloads fail, Jellyfin may stop indexing | Clear completed downloads, expand storage, prune old content. |

**Blast radius:** WireGuard failure is the most impactful — it stops all downloads immediately (kill switch by design). But this is a feature, not a bug. Jellyfin continues streaming existing content regardless of any other component failure.

**Quick recovery:**

```bash
# Restart a single service
docker compose restart <service-name>

# Check VPN status
docker exec wireguard wg show

# Full stack restart
docker compose down && docker compose up -d
```

---

## What Replaces What

| Need | You used to use | Now you use | Autonomy gain |
|------|----------------|-------------|---------------|
| Streaming | Netflix / Disney+ / HBO | **Jellyfin** | A0 → A3 |
| Finding movies | Browse streaming apps | **Radarr** | Manual → Automated |
| Finding TV shows | Browse streaming apps | **Sonarr** | Manual → Automated |
| Downloading | Manual search | **qBittorrent + Prowlarr** | Manual → Automated |
| Privacy | ISP sees everything | **WireGuard VPN** | Exposed → Protected |

---

## Maintenance

**Weekly:**
- Check qBittorrent — clear completed downloads
- Check disk usage: `du -sh media/* downloads/*`

**Monthly:**
- Update containers: `docker compose pull && docker compose up -d`
- Check Radarr/Sonarr activity — clean stuck queue items
- Verify VPN: `docker exec wireguard curl -s ifconfig.me`

**As needed:**
- Add new movies to Radarr watchlist
- Add new TV shows to Sonarr
- Update indexer credentials in Prowlarr

---

## Cost

| Item | One-time | Monthly |
|------|----------|---------|
| Server (mini PC or NAS) | $150–300 | — |
| Storage (4 TB HDD) | $80–120 | — |
| VPN service (Mullvad/IVPN) | — | $5/month |
| Electricity | — | ~$5/month |
| **Total** | **$230–420** | **~$10/month** |

Compare: Netflix ($15) + Disney+ ($14) + HBO Max ($16) + Hulu ($18) = **$63/month = $756/year**. Hardware pays for itself in 4–6 months.
