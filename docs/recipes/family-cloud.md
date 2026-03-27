---
title: "Family Cloud"
parent: Recipes
nav_order: 4
---

# Family Cloud

Replace Google Photos, Google Drive, iCloud, and LastPass with a self-hosted family cloud that you own. All data stays on your hardware. No subscriptions, no storage limits, no one scanning your photos.

This recipe combines technologies from the TAS catalog — all evaluated at **Autonomy Level A3** and **Transparency Level T2** (open source).

---

## Goal

Create a family cloud that:

- Stores and syncs photos automatically from every family phone (replacing Google Photos / iCloud)
- Syncs files and documents across all family devices (replacing Google Drive / iCloud Drive / Dropbox)
- Manages passwords for the whole family with shared vaults (replacing LastPass / 1Password)
- Provides a shared family cloud with calendar, contacts, and notes (replacing Google Workspace)
- Backs up everything automatically to a second location
- Runs behind a reverse proxy with automatic HTTPS
- Is accessible remotely via VPN
- Has a dashboard so everyone can find their apps

All of this on a single machine. No cloud accounts required after initial setup.

---

## Components

| Component | Catalog Card | Role |
|-----------|--------------|------|
| **Debian 12** | (OS) | Base operating system |
| **Docker** | [`compute/container`](../catalog/docker.md) | Container runtime |
| **Caddy** | [`network/proxy`](../catalog/caddy.md) | Reverse proxy with automatic HTTPS |
| **WireGuard** | [`network/vpn`](../catalog/wireguard.md) | Secure remote access |
| **Immich** | [`applications/photos`](../catalog/immich.md) | Photo & video backup (Google Photos replacement) |
| **Nextcloud** | [`applications/cloud`](../catalog/nextcloud.md) | Files, calendar, contacts, notes |
| **Syncthing** | [`storage/sync`](../catalog/syncthing.md) | P2P file sync between devices |
| **Vaultwarden** | [`security/passwords`](../catalog/vaultwarden.md) | Password manager (Bitwarden-compatible) |
| **PostgreSQL** | [`storage/database`](../catalog/postgresql.md) | Database for Immich and Nextcloud |
| **Redis** | [`storage/cache`](../catalog/redis.md) | Cache for Nextcloud |
| **Kopia** | [`storage/backup`](../catalog/kopia.md) | Encrypted backups |
| **Homepage** | [`applications/cloud`](../catalog/homepage.md) | Family dashboard |

*All are A3/T2.*

---

## Who is this for?

- A family that wants to stop paying Google/Apple for cloud storage
- Parents who want their children's photos on hardware they control
- Anyone who has been told "your iCloud storage is full" one too many times
- Families already running a NAS or old PC that could do more

**Estimated setup time:** 2–3 hours.
**Minimum hardware:** Any x86 machine with 8 GB RAM and 500 GB+ storage. An old laptop, a mini PC, or a NAS with Docker support.

---

## Step-by-Step Instructions

### 1. Install Base OS and Docker

Install Debian 12. Set up firewall:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y curl git ufw
sudo ufw allow ssh
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 51820/udp
sudo ufw enable
```

Install Docker:

```bash
curl -fsSL https://get.docker.com | sudo sh
sudo usermod -aG docker $USER
```

Log out and back in. Create the project directory:

```bash
mkdir -p /opt/family-cloud && cd /opt/family-cloud
```

### 2. Create Environment File

```bash
cat > .env << 'EOF'
# Domain (use a real domain pointed at your server, or .local for LAN-only)
DOMAIN=family.local

# PostgreSQL
POSTGRES_PASSWORD=CHANGE_ME_STRONG_PASSWORD_1

# Nextcloud
NEXTCLOUD_ADMIN_USER=admin
NEXTCLOUD_ADMIN_PASSWORD=CHANGE_ME_STRONG_PASSWORD_2

# Vaultwarden
VAULTWARDEN_ADMIN_TOKEN=CHANGE_ME_STRONG_PASSWORD_3

# Immich
IMMICH_DB_PASSWORD=CHANGE_ME_STRONG_PASSWORD_4

# WireGuard
WG_SERVER_PORT=51820
EOF
```

**Important:** Replace every `CHANGE_ME` with a real random password. Generate them:

```bash
openssl rand -hex 24
```

### 3. Create Docker Compose

```bash
cat > docker-compose.yml << 'YAMLEOF'
services:

  # ── Reverse Proxy ──────────────────────────────────
  caddy:
    image: caddy:latest
    container_name: caddy
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./config/caddy/Caddyfile:/etc/caddy/Caddyfile
      - caddy_data:/data
      - caddy_config:/config
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "wget", "--spider", "-q", "http://localhost:80"]
      interval: 30s
      timeout: 5s
      retries: 3

  # ── Database ───────────────────────────────────────
  postgres:
    image: postgres:16
    container_name: postgres
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - ./data/postgres:/var/lib/postgresql/data
      - ./config/postgres/init:/docker-entrypoint-initdb.d
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 30s
      timeout: 5s
      retries: 3
      start_period: 15s

  redis:
    image: redis:alpine
    container_name: redis
    command: --save 60 1
    volumes:
      - ./data/redis:/data
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 30s
      timeout: 5s
      retries: 3

  # ── Photos (Google Photos replacement) ─────────────
  immich-server:
    image: ghcr.io/immich-app/immich-server:release
    container_name: immich-server
    environment:
      DB_HOSTNAME: postgres
      DB_USERNAME: immich
      DB_PASSWORD: ${IMMICH_DB_PASSWORD}
      DB_DATABASE_NAME: immich
      REDIS_HOSTNAME: redis
    volumes:
      - ./data/immich/upload:/usr/src/app/upload
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    restart: unless-stopped

  immich-machine-learning:
    image: ghcr.io/immich-app/immich-machine-learning:release
    container_name: immich-ml
    volumes:
      - ./data/immich/model-cache:/cache
    restart: unless-stopped

  # ── Files, Calendar, Contacts (Google Drive replacement) ──
  nextcloud:
    image: nextcloud:stable
    container_name: nextcloud
    environment:
      POSTGRES_HOST: postgres
      POSTGRES_DB: nextcloud
      POSTGRES_USER: nextcloud
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      REDIS_HOST: redis
      NEXTCLOUD_ADMIN_USER: ${NEXTCLOUD_ADMIN_USER}
      NEXTCLOUD_ADMIN_PASSWORD: ${NEXTCLOUD_ADMIN_PASSWORD}
      NEXTCLOUD_TRUSTED_DOMAINS: cloud.${DOMAIN}
    volumes:
      - ./data/nextcloud:/var/www/html
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    restart: unless-stopped

  # ── Passwords (LastPass / 1Password replacement) ───
  vaultwarden:
    image: vaultwarden/server:latest
    container_name: vaultwarden
    environment:
      ADMIN_TOKEN: ${VAULTWARDEN_ADMIN_TOKEN}
      DOMAIN: https://vault.${DOMAIN}
    volumes:
      - ./data/vaultwarden:/data
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "wget", "--spider", "-q", "http://localhost:80/alive"]
      interval: 30s
      timeout: 5s
      retries: 3

  # ── File Sync (cross-device sync) ──────────────────
  syncthing:
    image: syncthing/syncthing:latest
    container_name: syncthing
    ports:
      - "22000:22000"
    volumes:
      - ./config/syncthing:/var/syncthing/config
      - ./data/syncthing:/var/syncthing/data
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "wget", "--spider", "-q", "http://localhost:8384"]
      interval: 30s
      timeout: 5s
      retries: 3

  # ── Dashboard ──────────────────────────────────────
  homepage:
    image: ghcr.io/gethomepage/homepage:latest
    container_name: homepage
    environment:
      HOMEPAGE_ALLOWED_HOSTS: home.${DOMAIN}
    volumes:
      - ./config/homepage:/app/config
      - /var/run/docker.sock:/var/run/docker.sock:ro
    restart: unless-stopped

  # ── Backup ─────────────────────────────────────────
  kopia:
    image: kopia/kopia:latest
    container_name: kopia
    volumes:
      - ./data:/source:ro
      - /mnt/backup:/backup
      - ./config/kopia:/app/config
    command: server start --insecure --address=0.0.0.0:51515
    restart: unless-stopped

volumes:
  caddy_data:
  caddy_config:
YAMLEOF
```

### 4. Create PostgreSQL Init Script

Multiple databases in one PostgreSQL instance:

```bash
mkdir -p config/postgres/init
cat > config/postgres/init/init-databases.sql << 'EOF'
CREATE USER immich WITH PASSWORD 'CHANGE_ME_STRONG_PASSWORD_4';
CREATE DATABASE immich OWNER immich;

CREATE USER nextcloud WITH PASSWORD 'CHANGE_ME_STRONG_PASSWORD_1';
CREATE DATABASE nextcloud OWNER nextcloud;
EOF
```

Replace passwords to match your `.env`.

### 5. Create Caddyfile

```bash
mkdir -p config/caddy
cat > config/caddy/Caddyfile << 'EOF'
photos.{$DOMAIN} {
    reverse_proxy immich-server:2283
}

cloud.{$DOMAIN} {
    reverse_proxy nextcloud:80
}

vault.{$DOMAIN} {
    reverse_proxy vaultwarden:80
}

sync.{$DOMAIN} {
    reverse_proxy syncthing:8384
}

home.{$DOMAIN} {
    reverse_proxy homepage:3000
}

backup.{$DOMAIN} {
    reverse_proxy kopia:51515
}
EOF
```

### 6. Create Homepage Dashboard Config

```bash
mkdir -p config/homepage
cat > config/homepage/services.yaml << 'EOF'
- Family Cloud:
    - Photos:
        icon: immich.png
        href: https://photos.family.local
        description: Photo & video backup
    - Files:
        icon: nextcloud.png
        href: https://cloud.family.local
        description: Files, calendar, contacts
    - Passwords:
        icon: vaultwarden.png
        href: https://vault.family.local
        description: Family password vault
    - Sync:
        icon: syncthing.png
        href: https://sync.family.local
        description: Cross-device file sync
    - Backups:
        icon: kopia.png
        href: https://backup.family.local
        description: Backup management
EOF
```

### 7. Deploy

```bash
cd /opt/family-cloud
docker compose up -d
```

Watch the logs:

```bash
docker compose logs -f
```

All services should be healthy within 2–3 minutes.

### 8. Set Up WireGuard for Remote Access

```bash
sudo apt install -y wireguard
wg genkey | tee /etc/wireguard/server_private.key | wg pubkey > /etc/wireguard/server_public.key
```

Create `/etc/wireguard/wg0.conf`:

```ini
[Interface]
PrivateKey = <server_private_key>
Address = 10.0.0.1/24
ListenPort = 51820

[Peer]
# Mom's phone
PublicKey = <peer_public_key>
AllowedIPs = 10.0.0.2/32

[Peer]
# Dad's phone
PublicKey = <peer_public_key>
AllowedIPs = 10.0.0.3/32
```

Enable:

```bash
sudo systemctl enable --now wg-quick@wg0
```

### 9. Set Up Backups

Mount an external drive or NAS share at `/mnt/backup`. Then:

```bash
docker exec kopia kopia repository create filesystem --path /backup
docker exec kopia kopia snapshot create /source
```

Set up a daily cron:

```bash
sudo crontab -e
# Add:
0 3 * * * docker exec kopia kopia snapshot create /source
```

### 10. Onboard Family Members

**Photos (Immich):**
- Install the Immich app on every family phone (iOS and Android)
- Point it at `https://photos.family.local`
- Enable auto-backup — all photos sync automatically

**Files (Nextcloud):**
- Install the Nextcloud app on phones and desktops
- Create user accounts for each family member
- Enable Calendar and Contacts sync in phone settings

**Passwords (Vaultwarden):**
- Install the Bitwarden app on all devices
- Point it at `https://vault.family.local`
- Create family accounts, set up shared vault for WiFi passwords, streaming logins, etc.

**Sync (Syncthing):**
- Install Syncthing on devices that need direct P2P sync
- Great for documents, music libraries, or anything that needs to work offline

---

## Failure Modes

What breaks, how badly, and how to recover.

| Component | Failure scenario | Impact | Recovery |
|-----------|-----------------|--------|----------|
| **Caddy** | Config error or crash | All services unreachable via domain | Access services directly via IP:PORT. Fix Caddyfile, `docker compose restart caddy` |
| **PostgreSQL** | Database corruption | Immich and Nextcloud lose metadata (photos/files still on disk) | Restore from Kopia backup: `docker exec kopia kopia snapshot restore <id> /source/postgres` |
| **Redis** | Service down | Nextcloud slow, Immich queues paused | Non-critical — `docker compose restart redis`. Data regenerates. |
| **Immich** | Server crash | Photo upload paused, web UI down | Photos stay on phones. `docker compose restart immich-server`. Uploads resume automatically. |
| **Nextcloud** | PHP error or update failure | Files inaccessible via web | Files still on disk at `data/nextcloud/`. Fix via `docker exec nextcloud occ maintenance:repair` |
| **Vaultwarden** | Database corruption | Passwords inaccessible | Bitwarden apps have offline cache — passwords still accessible on devices. Restore Vaultwarden data from Kopia. |
| **Syncthing** | Conflict on shared folder | Duplicate files with `.sync-conflict` suffix | Resolve in Syncthing UI. No data loss — both versions kept. |
| **Kopia** | Backup disk full | New backups fail | Clean old snapshots: `kopia snapshot delete`. Add more storage. |
| **WireGuard** | Key mismatch after phone reset | Remote access lost for that device | Generate new peer key, update server config, restart WireGuard. |

**Blast radius:** PostgreSQL is the highest-impact single point of failure — it takes down both Immich and Nextcloud metadata. Ensure Kopia backups run daily and test restore periodically.

**Quick recovery:**

```bash
# Restart a single failed service
docker compose restart <service-name>

# Check logs
docker compose logs --tail=50 <service-name>

# Full stack restart
docker compose down && docker compose up -d

# Emergency: restore full backup
docker compose down
docker exec kopia kopia snapshot restore <snapshot-id> /source
docker compose up -d
```

---

## What Replaces What

| Need | You used to use | Now you use | Autonomy gain |
|------|----------------|-------------|---------------|
| Photo backup | Google Photos / iCloud | Immich | A0 → A3 |
| File storage | Google Drive / Dropbox | Nextcloud + Syncthing | A0 → A3 |
| Calendar & contacts | Google Calendar | Nextcloud | A0 → A3 |
| Passwords | LastPass / 1Password | Vaultwarden | A0 → A3 |
| Family sharing | iCloud Family | Nextcloud shared folders | A0 → A3 |

---

## Maintenance

**Weekly:**
- Check Kopia backup status — verify latest snapshot exists
- Check Immich — ensure photo upload queue is empty

**Monthly:**
- Update containers: `docker compose pull && docker compose up -d`
- Check disk usage: `df -h` and `du -sh data/*`
- Test restore: pick one Kopia snapshot and verify it works

**Quarterly:**
- Review Nextcloud security scan: Settings → Security
- Rotate WireGuard keys if any device was lost
- Review Vaultwarden admin panel for inactive accounts

---

## Cost

| Item | One-time | Monthly |
|------|----------|---------|
| Mini PC (e.g. Intel NUC, Beelink) | $150–300 | — |
| 2 TB SSD (main storage) | $100–150 | — |
| External HDD for backups | $50–80 | — |
| Domain name (optional) | — | $1/month |
| Electricity | — | ~$5/month |
| **Total** | **$300–530** | **~$6/month** |

Compare: Google One 2TB ($10/month) + iCloud 2TB ($10/month) + LastPass Family ($4/month) = **$24/month = $288/year**. The hardware pays for itself in 1–2 years.
