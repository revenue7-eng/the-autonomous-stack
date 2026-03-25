---
title: "Privacy-First Homelab"
parent: Recipes
nav_order: 2
---

# Privacy-First Homelab

A complete self-hosted stack focused on privacy, ad blocking, and replacing cloud services with local alternatives. Every component is A3/T2 -- fully autonomous and open source.

This recipe extends the [Minimal Autonomous Server](minimal-server.md) with password management, reverse proxy, cloud platform, and smart home automation.

---

## Goal

Create a homelab that:

- Blocks ads and trackers for every device on your network
- Manages passwords without cloud dependency
- Replaces Google Drive / Dropbox with self-hosted file sync and cloud platform
- Provides HTTPS access to all services through a single reverse proxy
- Automates your home locally -- no Alexa, no Google Home
- Backs up everything automatically

---

## Components

| Component | Catalog Card | Role |
|-----------|--------------|------|
| **Debian 12** | (OS) | Base operating system |
| **Docker** | [compute/container](../catalog/docker.md) | Container runtime |
| **WireGuard** | [network/vpn](../catalog/wireguard.md) | Secure remote access |
| **Pi-hole** | [network/dns](../catalog/pi-hole.md) | Network-wide ad blocking |
| **Nginx Proxy Manager** | [network/proxy](../catalog/nginx-proxy-manager.md) | Reverse proxy with GUI |
| **Vaultwarden** | [security/passwords](../catalog/vaultwarden.md) | Password manager |
| **Syncthing** | [storage/sync](../catalog/syncthing.md) | P2P file sync |
| **Nextcloud** | [applications/cloud](../catalog/nextcloud.md) | Cloud platform (files, calendar, contacts) |
| **Kopia** | [storage/backup](../catalog/kopia.md) | Encrypted backups |
| **Home Assistant** | [applications/automation](../catalog/home-assistant.md) | Smart home automation |
| **Uptime Kuma** | [observability/monitoring](../catalog/uptime-kuma.md) | Monitoring dashboard |

All components are A3/T2.

---

## Prerequisites

- A server or mini PC (Intel NUC, old laptop, Raspberry Pi 4+ with 4GB RAM minimum)
- Debian 12 installed
- Docker and Docker Compose installed (see [Minimal Server recipe](minimal-server.md), steps 1-3)
- A local domain or IP address for accessing services
- External USB drive or NAS for backups (recommended)

---

## Step 1: Directory structure

```bash
mkdir -p /opt/homelab/{config,data,backups}
cd /opt/homelab
```

---

## Step 2: Docker Compose

Create `docker-compose.yml` in `/opt/homelab/`:

```yaml
services:

  # --- Network ---

  pihole:
    image: pihole/pihole:latest
    container_name: pihole
    ports:
      - "53:53/tcp"
      - "53:53/udp"
      - "8053:80/tcp"
    volumes:
      - ./config/pihole/etc:/etc/pihole
      - ./config/pihole/dnsmasq:/etc/dnsmasq.d
    environment:
      WEBPASSWORD: ${PIHOLE_PASSWORD}
    restart: unless-stopped

  npm:
    image: jc21/nginx-proxy-manager:latest
    container_name: nginx-proxy-manager
    ports:
      - "80:80"
      - "443:443"
      - "81:81"
    volumes:
      - ./data/npm:/data
      - ./data/npm-letsencrypt:/etc/letsencrypt
    restart: unless-stopped

  # --- Security ---

  vaultwarden:
    image: vaultwarden/server:latest
    container_name: vaultwarden
    ports:
      - "8222:80"
    volumes:
      - ./data/vaultwarden:/data
    environment:
      SIGNUPS_ALLOWED: "false"
      ADMIN_TOKEN: ${VW_ADMIN_TOKEN}
    restart: unless-stopped

  # --- Storage ---

  syncthing:
    image: syncthing/syncthing:latest
    container_name: syncthing
    ports:
      - "8384:8384"
      - "22000:22000"
    volumes:
      - ./config/syncthing:/var/syncthing/config
      - ./data/syncthing:/var/syncthing/data
    restart: unless-stopped

  nextcloud-db:
    image: postgres:15
    container_name: nextcloud-db
    environment:
      POSTGRES_DB: nextcloud
      POSTGRES_USER: nextcloud
      POSTGRES_PASSWORD: ${NC_DB_PASSWORD}
    volumes:
      - ./data/nextcloud-db:/var/lib/postgresql/data
    restart: unless-stopped

  nextcloud:
    image: nextcloud:latest
    container_name: nextcloud
    ports:
      - "8080:80"
    volumes:
      - ./data/nextcloud:/var/www/html
    environment:
      POSTGRES_HOST: nextcloud-db
      POSTGRES_DB: nextcloud
      POSTGRES_USER: nextcloud
      POSTGRES_PASSWORD: ${NC_DB_PASSWORD}
      NEXTCLOUD_ADMIN_USER: ${NC_ADMIN_USER}
      NEXTCLOUD_ADMIN_PASSWORD: ${NC_ADMIN_PASSWORD}
    depends_on:
      - nextcloud-db
    restart: unless-stopped

  # --- Automation ---

  homeassistant:
    image: homeassistant/home-assistant:latest
    container_name: homeassistant
    network_mode: host
    volumes:
      - ./config/homeassistant:/config
    restart: unless-stopped

  # --- Monitoring ---

  uptime-kuma:
    image: louislam/uptime-kuma:1
    container_name: uptime-kuma
    ports:
      - "3001:3001"
    volumes:
      - ./data/uptime-kuma:/app/data
    restart: unless-stopped
```

---

## Step 3: Environment file

Create `.env` in the same directory:

```bash
# Pi-hole
PIHOLE_PASSWORD=change-me

# Vaultwarden
VW_ADMIN_TOKEN=change-me-generate-with-openssl-rand-hex-32

# Nextcloud
NC_DB_PASSWORD=change-me-generate-random
NC_ADMIN_USER=admin
NC_ADMIN_PASSWORD=change-me-strong-password
```

Generate real secrets:

```bash
openssl rand -hex 32  # for VW_ADMIN_TOKEN
openssl rand -hex 16  # for NC_DB_PASSWORD
```

---

## Step 4: Start everything

```bash
docker compose up -d
```

---

## Step 5: Configure WireGuard

Follow the same WireGuard setup as the [Minimal Server recipe](minimal-server.md), step 5. This gives you secure remote access to all services.

---

## Step 6: Configure Nginx Proxy Manager

Open `http://your-server:81`. Default login: `admin@example.com` / `changeme`.

Add proxy hosts for each service:

| Service | Internal URL | Suggested subdomain |
|---------|-------------|-------------------|
| Pi-hole | `http://pihole:80` | pihole.home.local |
| Vaultwarden | `http://vaultwarden:80` | vault.home.local |
| Nextcloud | `http://nextcloud:80` | cloud.home.local |
| Syncthing | `http://syncthing:8384` | sync.home.local |
| Uptime Kuma | `http://uptime-kuma:3001` | status.home.local |
| Home Assistant | `http://localhost:8123` | ha.home.local |

For local-only access, use self-signed certificates or mkcert. For external access, enable Let's Encrypt in NPM.

---

## Step 7: Configure Pi-hole as network DNS

Point your router's DNS to your server's IP address. All devices on the network will now use Pi-hole for DNS resolution and ad blocking.

If you can't change router DNS, configure individual devices to use your server as DNS.

---

## Step 8: Set up Vaultwarden

Open `https://vault.home.local` (or the IP with port 8222).

1. Create your account (signups are disabled after first user by default).
2. Install the Bitwarden browser extension and mobile app.
3. Point them to your Vaultwarden URL.
4. Import existing passwords from your current password manager.

---

## Step 9: Set up Nextcloud

Open `https://cloud.home.local` (or the IP with port 8080). Log in with the admin credentials from `.env`.

Install recommended apps: Calendar, Contacts, Notes, Talk. Install the Nextcloud desktop and mobile sync clients and point them to your server.

---

## Step 10: Configure backups with Kopia

```bash
# Install Kopia
wget https://github.com/kopia/kopia/releases/latest/download/kopia-linux-amd64.tar.gz
tar -xzf kopia-linux-amd64.tar.gz
sudo mv kopia /usr/local/bin/

# Create repository on external drive
sudo kopia repository create filesystem --path /mnt/backup

# Backup everything
sudo kopia snapshot create /opt/homelab

# Set up daily cron
sudo crontab -e
# Add: 0 3 * * * /usr/local/bin/kopia snapshot create /opt/homelab
```

---

## Step 11: Pause and resume

```bash
# Pause everything
cd /opt/homelab
docker compose stop

# Resume
docker compose start
```

---


---

## Failure Modes

What breaks, how badly, and how to recover.

| Component | Failure scenario | Impact | Recovery |
|-----------|-----------------|--------|----------|
| **Pi-hole** | Service down | DNS resolution fails for every device using the server as DNS | Set router DNS back to ISP temporarily, or set `1.1.1.1` on individual devices; restart Pi-hole container |
| **Nginx Proxy Manager** | Config error or service crash | All services unreachable via domain names (HTTPS) | Access services directly via `http://server-ip:PORT` while fixing NPM config |
| **Vaultwarden** | Data volume failure | All passwords inaccessible | This is the highest-severity failure in this stack. Restore `/opt/homelab/data/vaultwarden` from Kopia backup immediately. **Test this restore path before you need it.** |
| **Nextcloud + PostgreSQL** | PostgreSQL crash | Nextcloud unavailable; files on disk are intact | Restart `nextcloud-db` container; if corrupt, restore DB from Kopia backup. Files in `/opt/homelab/data/nextcloud` remain accessible directly. |
| **Syncthing** | Device goes offline | Sync pauses until device reconnects — no data loss | No action needed; sync resumes automatically on reconnect |
| **Home Assistant** | Config error after update | Automation and device control unavailable | Roll back: `docker compose pull homeassistant` to previous tag; or restore config from Kopia backup |
| **Kopia** | Backup drive unmounted | Backups silently fail | Add a Kopia health check to Uptime Kuma: monitor the cron log or set up `kopia maintenance run` with alerting |
| **WireGuard** | Firewall rule change blocks UDP 51820 | Remote access lost | Requires local access to fix firewall; or keep an SSH fallback port open |
| **Uptime Kuma** | Service down | No monitoring alerts | Not critical — all other services continue; restart container |

**Cascade risk:** Pi-hole → Nginx Proxy Manager → all services. If Pi-hole fails, domain-based access via NPM also breaks (DNS doesn't resolve the domain). Direct IP:PORT access is always your fallback.

**Vaultwarden is your most critical service.** All your passwords live there. Verify the backup restore path:

```bash
# Test Vaultwarden backup restore
sudo kopia snapshot list | grep vaultwarden
sudo kopia restore <snapshot-id> /tmp/vaultwarden-test
ls /tmp/vaultwarden-test/data/vaultwarden/
# You should see: db.sqlite3, attachments/, config.json
```

**Quick recovery commands:**

```bash
# Restart any failed service
docker compose restart <service-name>

# View recent logs
docker compose logs --tail=100 <service-name>

# Check all container statuses
docker compose ps

# Emergency: stop everything safely
docker compose stop
```

## Verification

Run through the three structural criteria:

**Pause.** Stop all services with `docker compose stop`. Verify they stop cleanly. Resume with `docker compose start`. Nothing should be lost.

**Exit.** All data is in `/opt/homelab/config/` and `/opt/homelab/data/`. Copy these directories to another machine, run `docker compose up -d`, and you have the same stack. Passwords export via Bitwarden clients. Nextcloud files are ordinary files. No cloud lock-in anywhere.

**Recoverability.** Restore a Kopia snapshot to verify backups work:

```bash
sudo kopia snapshot list
sudo kopia restore <snapshot-id> /tmp/homelab-test
```

---

## What you replaced

| Cloud service | What you had | What you have now | Autonomy change |
|--------------|-------------|-------------------|----------------|
| Google DNS / ISP DNS | No filtering, tracked | Pi-hole -- filtered, private | A0 to A3 |
| LastPass / 1Password | Cloud passwords | Vaultwarden -- local passwords | A0 to A3 |
| Google Drive / Dropbox | Cloud files | Syncthing + Nextcloud -- local files | A0 to A3 |
| Google Home / Alexa | Cloud automation | Home Assistant -- local automation | A0 to A3 |
| No monitoring | Hope nothing breaks | Uptime Kuma -- you'll know | -- to A3 |

---

## Next steps

- Add [Immich](../catalog/immich.md) for photo backup (replace Google Photos)
- Add [Jellyfin](../catalog/jellyfin.md) for media streaming (replace Plex)
- Add [Paperless-ngx](../catalog/paperless-ngx.md) for document management
- Add [Forgejo](../catalog/forgejo.md) for Git hosting
- Add [Authentik](../catalog/authentik.md) for single sign-on across all services
- Set up [Grafana](../catalog/grafana.md) + [Prometheus](../catalog/prometheus.md) for advanced monitoring

---

*This stack achieves A3/T2 across all components. Every service can be paused, exited, and recovered. Every piece of data is yours. If full transparency about how any of these tools work would make you stop using them -- they would fail their own seventh question. They don't.*
