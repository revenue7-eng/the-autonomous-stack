---
title: "Developer Workstation"
parent: Recipes
nav_order: 3
---

# Developer Workstation

A self-hosted development environment where your code, secrets, CI/CD, and collaboration tools belong to you. No GitHub dependency, no cloud IDE, no SaaS lock-in.

---

## Goal

Create a development setup that:

- Hosts Git repositories with CI/CD pipelines locally
- Manages secrets and credentials without cloud vaults
- Syncs code and dotfiles across machines without cloud accounts
- Provides a private container registry
- Monitors build health and service uptime
- Backs up everything -- code, configs, databases
- Works offline for days or weeks at a time

---

## Components

| Component | Catalog Card | Role |
|-----------|--------------|------|
| **Debian 12** | (OS) | Base operating system |
| **Docker** | [compute/container](../catalog/docker.md) | Container runtime |
| **Forgejo** | [applications/version-control](../catalog/forgejo.md) | Git hosting + CI/CD (Actions) |
| **Vaultwarden** | [security/passwords](../catalog/vaultwarden.md) | Credentials and API keys |
| **Vault** | [security/secrets](../catalog/vault.md) | Infrastructure secrets and encryption |
| **Traefik** | [network/proxy](../catalog/traefik.md) | Reverse proxy with auto-HTTPS |
| **WireGuard** | [network/vpn](../catalog/wireguard.md) | Secure remote access |
| **Syncthing** | [storage/sync](../catalog/syncthing.md) | Dotfiles and config sync across machines |
| **Kopia** | [storage/backup](../catalog/kopia.md) | Encrypted backups |
| **Prometheus** | [observability/metrics](../catalog/prometheus.md) | Metrics collection |
| **Grafana** | [observability/dashboards](../catalog/grafana.md) | Dashboards |
| **Uptime Kuma** | [observability/monitoring](../catalog/uptime-kuma.md) | Service health monitoring |

All components are A3/T2.

---

## Prerequisites

- A server, workstation, or powerful mini PC (8GB RAM minimum, 16GB recommended)
- Debian 12 installed
- Docker and Docker Compose installed
- A domain or local DNS (optional but recommended for Traefik)

---

## Step 1: Directory structure

```bash
mkdir -p /opt/devstack/{config,data,backups}
cd /opt/devstack
```

---

## Step 2: Docker Compose

Create `docker-compose.yml` in `/opt/devstack/`:

```yaml
services:

  # --- Network ---

  traefik:
    image: traefik:latest
    container_name: traefik
    ports:
      - "80:80"
      - "443:443"
      - "8080:8080"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - ./config/traefik:/etc/traefik
      - ./data/letsencrypt:/letsencrypt
    command:
      - "--api.dashboard=true"
      - "--api.insecure=true"
      - "--providers.docker=true"
      - "--providers.docker.exposedByDefault=false"
      - "--entrypoints.web.address=:80"
      - "--entrypoints.websecure.address=:443"
    restart: unless-stopped

  # --- Version Control + CI/CD ---

  forgejo:
    image: codeberg.org/forgejo/forgejo:1.21
    container_name: forgejo
    ports:
      - "3000:3000"
      - "222:22"
    volumes:
      - ./data/forgejo:/data
    environment:
      - FORGEJO__server__DOMAIN=${FORGEJO_DOMAIN:-git.local}
      - FORGEJO__server__SSH_PORT=222
      - FORGEJO__server__ROOT_URL=http://${FORGEJO_DOMAIN:-git.local}:3000
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.forgejo.rule=Host(`${FORGEJO_DOMAIN:-git.local}`)"
      - "traefik.http.services.forgejo.loadbalancer.server.port=3000"
    restart: unless-stopped

  # --- Container Registry ---

  registry:
    image: registry:2
    container_name: registry
    ports:
      - "5000:5000"
    volumes:
      - ./data/registry:/var/lib/registry
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
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.vault.rule=Host(`vault.local`)"
      - "traefik.http.services.vault.loadbalancer.server.port=80"
    restart: unless-stopped

  # --- File Sync ---

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

  # --- Observability ---

  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./config/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml
      - ./data/prometheus:/prometheus
    restart: unless-stopped

  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    ports:
      - "3100:3000"
    volumes:
      - ./data/grafana:/var/lib/grafana
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.grafana.rule=Host(`grafana.local`)"
      - "traefik.http.services.grafana.loadbalancer.server.port=3000"
    restart: unless-stopped

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

## Step 3: Prometheus config

Create `config/prometheus/prometheus.yml`:

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'traefik'
    static_configs:
      - targets: ['traefik:8080']

  - job_name: 'node'
    static_configs:
      - targets: ['localhost:9100']
```

For full host metrics, add Node Exporter:

```bash
docker run -d --name node-exporter --net=host prom/node-exporter:latest
```

---

## Step 4: Environment file

Create `.env`:

```bash
# Forgejo
FORGEJO_DOMAIN=git.local

# Vaultwarden
VW_ADMIN_TOKEN=change-me-generate-with-openssl-rand-hex-32
```

---

## Step 5: Start everything

```bash
docker compose up -d
```

---

## Step 6: Configure WireGuard

Same as [Minimal Server recipe](minimal-server.md), step 5. Gives you secure access to your dev environment from anywhere.

---

## Step 7: Set up Forgejo

Open `http://git.local:3000` (or your server IP). Complete the initial setup wizard.

Then:

1. Create your user account.
2. Create your first repository.
3. Push an existing project: `git remote add origin ssh://git@your-server:222/you/project.git && git push -u origin main`
4. Enable Forgejo Actions for CI/CD (Settings > Actions > Enable).

---

## Step 8: Set up the container registry

Your private Docker registry is at `localhost:5000`. Use it in CI/CD:

```bash
# Tag and push an image
docker build -t localhost:5000/myapp:latest .
docker push localhost:5000/myapp:latest

# Pull from registry
docker pull localhost:5000/myapp:latest
```

For Forgejo Actions, reference your registry in workflow files.

---

## Step 9: Sync dotfiles with Syncthing

Open `http://your-server:8384`. Add a folder for your dotfiles (`.bashrc`, `.gitconfig`, `.ssh/config`, editor configs). Share it between your workstation and server. Changes propagate automatically -- no GitHub dotfiles repo needed.

---

## Step 10: Set up Grafana dashboards

Open `http://grafana.local:3100` (default: admin/admin).

1. Add Prometheus as data source: `http://prometheus:9090`
2. Import dashboard #1860 (Node Exporter Full) for host metrics.
3. Import dashboard #4475 (Traefik) for proxy metrics.
4. Add Uptime Kuma monitors for each service.

---

## Step 11: Configure backups

```bash
# Install Kopia
wget https://github.com/kopia/kopia/releases/latest/download/kopia-linux-amd64.tar.gz
tar -xzf kopia-linux-amd64.tar.gz
sudo mv kopia /usr/local/bin/

# Create repository
sudo kopia repository create filesystem --path /mnt/backup

# Backup everything
sudo kopia snapshot create /opt/devstack

# Daily cron
sudo crontab -e
# Add: 0 3 * * * /usr/local/bin/kopia snapshot create /opt/devstack
```

---

## Developer workflow

Your daily workflow now looks like this:

1. **Code** -- push to Forgejo. CI runs via Actions. Images go to your registry.
2. **Secrets** -- API keys in Vaultwarden (personal) or Vault (infrastructure). No plaintext `.env` files in repos.
3. **Sync** -- dotfiles and configs sync via Syncthing across all your machines.
4. **Monitor** -- Grafana shows host metrics, Traefik shows request rates, Uptime Kuma alerts if anything goes down.
5. **Access** -- WireGuard from anywhere. Traefik routes to the right service.
6. **Backup** -- Kopia snapshots every night. Restore any point in time.

---


---

## Failure Modes

What breaks, how badly, and how to recover.

| Component | Failure scenario | Impact | Recovery |
|-----------|-----------------|--------|----------|
| **Traefik** | Config syntax error or volume permission issue | All services unreachable via domain | Access directly via `http://server-ip:PORT` while fixing Traefik config; check logs with `docker compose logs traefik` |
| **Forgejo** | Data volume failure | All Git repositories and CI/CD history inaccessible | Restore `/opt/devstack/data/forgejo` from Kopia backup; Git repos are standard bare repos and can be re-pushed if backup fails |
| **Forgejo Actions runner** | Runner offline | CI/CD pipelines queue but don't run | Restart runner container; pipelines resume automatically |
| **Vaultwarden** | Service down | Developer credentials temporarily inaccessible | Restart container; data persists on volume. If volume corrupt: restore from Kopia backup |
| **Container Registry** | Service down or volume failure | `docker push/pull` fails; existing images on disk are intact | Restart registry container; images in `/opt/devstack/data/registry` survive restarts |
| **Syncthing** | Conflict on dotfiles | Dotfiles duplicated with conflict copies | Pause sync, resolve via Syncthing UI, resume; no data loss |
| **Prometheus** | Data volume full | Metrics collection stops; dashboards show gaps | Prune old data: `docker compose exec prometheus promtool tsdb list`; or reduce retention in prometheus.yml |
| **Grafana** | Database corruption | Dashboards inaccessible | Dashboards are JSON — export regularly. Restore from Kopia backup or re-import dashboard JSON files |
| **WireGuard** | Key rotation failure after server rebuild | Remote dev access lost | Regenerate server keys, redistribute peer configs; keep an SSH fallback |
| **Kopia** | Repository locked (crash during backup) | Subsequent backups fail | `sudo kopia repository unlock`; run `sudo kopia maintenance run` |

**Highest-impact failures:** Forgejo data loss = losing Git history. Vaultwarden failure = losing API keys and credentials. Both must have tested backup restore paths before you rely on this stack in production.

**Forgejo backup verification:**

```bash
# Verify Forgejo backup is restorable
sudo kopia snapshot list | grep forgejo
sudo kopia restore <snapshot-id> /tmp/forgejo-test
ls /tmp/forgejo-test/data/forgejo/repositories/
# You should see your repository directories
```

**Quick recovery commands:**

```bash
# Restart any failed service
docker compose restart <service-name>

# View recent logs
docker compose logs --tail=100 <service-name>

# Check all container statuses
docker compose ps -a

# Pause entire stack safely
docker compose stop

# Emergency rollback to previous image
docker compose pull <service>  # pulls latest; specify tag to pin version
```

## Verification

**Pause.** `docker compose stop`. All services halt. Code stays in Forgejo data directory. Secrets stay encrypted. Resume with `docker compose start`.

**Exit.** Clone your repos from Forgejo via standard Git. Export passwords from Vaultwarden via Bitwarden clients. Copy `/opt/devstack` to a new machine. No vendor involved.

**Recoverability.** Kopia snapshots. Forgejo keeps Git history. Grafana dashboards export as JSON. Everything can be restored.

---

## What you replaced

| Cloud service | What you had | What you have now | Autonomy change |
|--------------|-------------|-------------------|----------------|
| GitHub / GitLab.com | Cloud Git + CI | Forgejo + Actions -- local Git + CI | A0 to A3 |
| Docker Hub (builds) | Cloud registry | Private registry -- local images | A0 to A3 |
| 1Password / LastPass | Cloud passwords | Vaultwarden -- local passwords | A0 to A3 |
| Dropbox (dotfiles) | Cloud sync | Syncthing -- P2P sync | A0 to A3 |
| Datadog / New Relic | Cloud monitoring | Prometheus + Grafana -- local metrics | A0 to A3 |

---

## Next steps

- Add [Authentik](../catalog/authentik.md) for SSO across Forgejo, Grafana, and Nextcloud
- Add a Gitea/Forgejo runner for more complex CI/CD pipelines
- Add [Nextcloud](../catalog/nextcloud.md) for team collaboration (wiki, shared files, video calls)
- Set up Git mirroring to push to GitHub as a public mirror while keeping Forgejo as primary

---

*Every tool in this stack passes the transparency fragility test: if you could see exactly how each one works -- every line of code, every data flow, every design decision -- you would still use it. That is the definition of open-mode architecture.*
