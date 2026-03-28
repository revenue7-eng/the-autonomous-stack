---
title: "Home Office"
parent: Recipes
nav_order: 8
---

# Home Office

Replace Google Workspace, ChatGPT, and Google Search with a self-hosted office stack. Files, notes, AI assistant, private search, and news — all on your hardware, all yours.

---

## Goal

Create a home office that:

- Syncs files, calendar, and contacts across all devices (replacing Google Workspace)
- Provides a local AI assistant for writing, research, and coding (replacing ChatGPT)
- Searches the web privately without tracking (replacing Google Search)
- Aggregates news and articles without algorithms (replacing Google News)
- Saves articles for later reading without ads (replacing Pocket)
- Manages passwords securely (replacing LastPass)
- All runs locally — your work stays on your machine

---

## Components

| Component | Catalog Card | Role |
|-----------|--------------|------|
| **Debian** | [`compute/os`](../catalog/debian.md) | Base operating system. [Ubuntu Server](../catalog/ubuntu-server.md) also works. |
| **Docker** | [`compute/container`](../catalog/docker.md) | Container runtime |
| **Nextcloud** | [`applications/cloud`](../catalog/nextcloud.md) | Files, calendar, contacts, office docs |
| **Joplin** | [`applications/notes`](../catalog/joplin.md) | Markdown notes with E2E encryption |
| **Ollama** | [`compute/inference`](../catalog/ollama.md) | Local LLM runtime |
| **SearXNG** | [`applications/search`](../catalog/searxng.md) | Private metasearch engine |
| **FreshRSS** | [`applications/news`](../catalog/freshrss.md) | RSS feed reader |
| **Wallabag** | [`applications/reading`](../catalog/wallabag.md) | Read-it-later service |
| **Vaultwarden** | [`security/passwords`](../catalog/vaultwarden.md) | Password manager |
| **Caddy** | [`network/proxy`](../catalog/caddy.md) | Reverse proxy with HTTPS |
| **PostgreSQL** | [`storage/database`](../catalog/postgresql.md) | Database for Nextcloud |

*All are A3/T2.*

---


> **Running Proxmox?** Create a VM (Debian, 4+ GB RAM), install Docker inside it, then follow this recipe. Benefit: VM-level snapshots before updates, isolation from other stacks, easy backup via vzdump. See [Proxmox VE](../catalog/proxmox.md).

## Who is this for?

- Remote workers who want control over their data
- Freelancers who don't want to pay for Google Workspace
- Anyone who uses ChatGPT daily and wants a private alternative
- Developers who want local AI for code assistance
- Privacy-conscious professionals

**Estimated setup time:** 2–3 hours.
**Minimum hardware:** 8 GB RAM minimum. 16 GB recommended if running Ollama with larger models. GPU optional but significantly improves LLM speed.

---

## Step-by-Step Instructions

### 1. Create Project Directory

```bash
mkdir -p /opt/home-office && cd /opt/home-office
```

### 2. Create Docker Compose

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
    restart: unless-stopped

  # ── Database ───────────────────────────────────────
  postgres:
    image: postgres:16
    container_name: postgres
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - ./data/postgres:/var/lib/postgresql/data
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 30s
      timeout: 5s
      retries: 3

  # ── Files + Calendar + Contacts ────────────────────
  nextcloud:
    image: nextcloud:stable
    container_name: nextcloud
    environment:
      POSTGRES_HOST: postgres
      POSTGRES_DB: nextcloud
      POSTGRES_USER: nextcloud
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      NEXTCLOUD_ADMIN_USER: ${NEXTCLOUD_ADMIN_USER}
      NEXTCLOUD_ADMIN_PASSWORD: ${NEXTCLOUD_ADMIN_PASSWORD}
    volumes:
      - ./data/nextcloud:/var/www/html
    depends_on:
      postgres:
        condition: service_healthy
    restart: unless-stopped

  # ── Notes ──────────────────────────────────────────
  joplin:
    image: joplin/server:latest
    container_name: joplin
    ports:
      - "22300:22300"
    environment:
      APP_BASE_URL: https://notes.${DOMAIN}
      DB_CLIENT: pg
      POSTGRES_HOST: postgres
      POSTGRES_PORT: 5432
      POSTGRES_DATABASE: joplin
      POSTGRES_USER: joplin
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    depends_on:
      postgres:
        condition: service_healthy
    restart: unless-stopped

  # ── AI Assistant ───────────────────────────────────
  ollama:
    image: ollama/ollama
    container_name: ollama
    ports:
      - "11434:11434"
    volumes:
      - ./data/ollama:/root/.ollama
    restart: unless-stopped

  # ── Private Search ─────────────────────────────────
  searxng:
    image: searxng/searxng
    container_name: searxng
    ports:
      - "8888:8080"
    volumes:
      - ./data/searxng:/etc/searxng
    environment:
      - SEARXNG_BASE_URL=https://search.${DOMAIN}
    restart: unless-stopped

  # ── RSS Reader ─────────────────────────────────────
  freshrss:
    image: freshrss/freshrss
    container_name: freshrss
    ports:
      - "8082:80"
    volumes:
      - ./data/freshrss/data:/var/www/FreshRSS/data
      - ./data/freshrss/extensions:/var/www/FreshRSS/extensions
    environment:
      - TZ=UTC
      - CRON_MIN=2,32
    restart: unless-stopped

  # ── Read Later ─────────────────────────────────────
  wallabag:
    image: wallabag/wallabag
    container_name: wallabag
    ports:
      - "8090:80"
    volumes:
      - ./data/wallabag/images:/var/www/wallabag/web/assets/images
      - ./data/wallabag/data:/var/www/wallabag/data
    environment:
      - SYMFONY__ENV__DOMAIN_NAME=https://read.${DOMAIN}
      - SYMFONY__ENV__DATABASE_DRIVER=pdo_sqlite
    restart: unless-stopped

  # ── Passwords ──────────────────────────────────────
  vaultwarden:
    image: vaultwarden/server:latest
    container_name: vaultwarden
    environment:
      DOMAIN: https://vault.${DOMAIN}
      ADMIN_TOKEN: ${VAULTWARDEN_ADMIN_TOKEN}
    volumes:
      - ./data/vaultwarden:/data
    restart: unless-stopped

volumes:
  caddy_data:
YAMLEOF
```

### 3. Create Environment File

```bash
cat > .env << 'EOF'
DOMAIN=office.local
POSTGRES_PASSWORD=CHANGE_ME_1
NEXTCLOUD_ADMIN_USER=admin
NEXTCLOUD_ADMIN_PASSWORD=CHANGE_ME_2
VAULTWARDEN_ADMIN_TOKEN=CHANGE_ME_3
EOF
```

### 4. Configure Caddy

```bash
mkdir -p config/caddy
cat > config/caddy/Caddyfile << 'EOF'
cloud.{$DOMAIN} {
    reverse_proxy nextcloud:80
}
notes.{$DOMAIN} {
    reverse_proxy joplin:22300
}
search.{$DOMAIN} {
    reverse_proxy searxng:8080
}
news.{$DOMAIN} {
    reverse_proxy freshrss:80
}
read.{$DOMAIN} {
    reverse_proxy wallabag:80
}
vault.{$DOMAIN} {
    reverse_proxy vaultwarden:80
}
ai.{$DOMAIN} {
    reverse_proxy ollama:11434
}
EOF
```

### 5. Initialize PostgreSQL Databases

```bash
mkdir -p config/postgres
cat > config/postgres/init-databases.sql << 'EOF'
CREATE USER nextcloud WITH PASSWORD 'CHANGE_ME_1';
CREATE DATABASE nextcloud OWNER nextcloud;

CREATE USER joplin WITH PASSWORD 'CHANGE_ME_1';
CREATE DATABASE joplin OWNER joplin;
EOF
```

Add the init script volume to the postgres service:

```yaml
    volumes:
      - ./data/postgres:/var/lib/postgresql/data
      - ./config/postgres:/docker-entrypoint-initdb.d
```

### 6. Deploy

```bash
docker compose up -d
```

### 7. Set Up Ollama

```bash
# Pull a model (choose based on your hardware)
# 8GB RAM: small model
docker exec ollama ollama pull phi3:mini

# 16GB RAM: medium model
docker exec ollama ollama pull llama3.2

# 32GB+ RAM or GPU: large model
docker exec ollama ollama pull llama3.1:70b

# Test
docker exec ollama ollama run llama3.2 "Summarize the key points of project management"
```

### 8. Set SearXNG as Default Search

In your browser: Settings → Search Engine → Add custom → `https://search.office.local/search?q=%s`

### 9. Connect Clients

**Nextcloud:** Install apps on phone and desktop. Sync calendar and contacts in phone settings (CalDAV/CardDAV).

**Joplin:** Install Joplin desktop and mobile apps. Settings → Sync → Joplin Server → enter your server URL.

**Vaultwarden:** Install Bitwarden apps. Settings → Self-hosted → enter vault URL.

**FreshRSS:** Add your favorite news sources, blogs, and YouTube channels as RSS feeds.

**Wallabag:** Install browser extension. One click saves any article.

---

## Failure Modes

| Component | Failure scenario | Impact | Recovery |
|-----------|-----------------|--------|----------|
| **PostgreSQL** | Database corruption | Nextcloud and Joplin lose metadata | Restore from backup. Files on disk are intact. |
| **Nextcloud** | PHP error | Files inaccessible via web | Files still on disk. Fix via `occ maintenance:repair` |
| **Ollama** | OOM (out of memory) | AI assistant crashes | Use a smaller model. Restart: `docker compose restart ollama` |
| **SearXNG** | Upstream engines blocked | Search returns no results | Switch engines in SearXNG settings. Self-hosted search still works. |
| **FreshRSS** | Feed fetch failure | New articles not appearing | Check feed URLs. Some sites block RSS scraping. |
| **Wallabag** | Disk full | Can't save new articles | Clean old articles or expand storage. |
| **Vaultwarden** | Database corruption | Passwords inaccessible online | Bitwarden apps have offline cache. Restore from backup. |

**Blast radius:** PostgreSQL is the highest-impact component — takes down Nextcloud and Joplin if it fails. Ollama, SearXNG, FreshRSS, and Wallabag are independent — each failure is isolated.

---

## What Replaces What

| Need | You used to use | Now you use | Autonomy gain |
|------|----------------|-------------|---------------|
| Files + calendar | Google Workspace | **Nextcloud** | A0 → A3 |
| Notes | Notion / Google Keep | **Joplin** | A0 → A3 |
| AI assistant | ChatGPT / Claude | **Ollama** | A0 → A3 |
| Web search | Google Search | **SearXNG** | A0 → A3 |
| News | Google News / Twitter | **FreshRSS** | A0 → A3 |
| Read later | Pocket / Instapaper | **Wallabag** | A0 → A3 |
| Passwords | LastPass / 1Password | **Vaultwarden** | A0 → A3 |

---

## Cost

| Item | One-time | Monthly |
|------|----------|---------|
| Mini PC (16 GB RAM recommended) | $200–400 | — |
| 1 TB SSD | $60–100 | — |
| Domain (optional) | — | $1/month |
| Electricity | — | ~$5/month |
| **Total** | **$260–500** | **~$6/month** |

Compare: Google Workspace ($7/mo) + ChatGPT Plus ($20/mo) + Pocket Premium ($5/mo) + 1Password ($3/mo) = **$35/month = $420/year**. Hardware pays for itself in under a year.
