---
title: "Minimal Autonomous Server"
parent: Recipes
nav_order: 1
---

# Minimal Autonomous Server

Build a fully autonomous server that operates offline, gives you full control over your data, and respects the three ethical principles: **Pause**, **Exit**, and **Recoverability**.

This recipe combines technologies from the TAS catalog — all evaluated at **Autonomy Level A3** (fully autonomous) and **Transparency Level T2** (open source), except where noted.

---

## Goal

Create a server that:

- Runs without internet after initial setup (A3 autonomy)
- Stores all data locally
- Provides secure remote access (VPN)
- Filters network traffic (ad blocking, DNS)
- Manages user identity (SSO)
- Synchronises files across devices (P2P)
- Backs up data automatically
- Monitors services
- Hosts media and Git repositories

You will end up with a solid foundation for your autonomous digital infrastructure.

---

## Components

| Component | Catalog Card | Role |
|-----------|--------------|------|
| **Debian 12** | (OS) | Base operating system |
| **Docker** | [`compute/container`](../catalog/docker.md) | Container runtime |
| **WireGuard** | [`network/vpn`](../catalog/wireguard.md) | Secure remote access |
| **AdGuard Home** | [`network/dns`](../catalog/adguard-home.md) | DNS filtering and ad blocking |
| **Authentik** | [`identity/auth`](../catalog/authentik.md) | Central authentication |
| **Syncthing** | [`storage/sync`](../catalog/syncthing.md) | P2P file sync |
| **Kopia** | [`storage/backup`](../catalog/kopia.md) | Encrypted backups |
| **Uptime Kuma** | [`observability/monitoring`](../catalog/uptime-kuma.md) | Monitoring |
| **Jellyfin** | [`applications/media`](../catalog/jellyfin.md) | Media server |
| **Forgejo** | [`applications/version-control`](../catalog/forgejo.md) | Self‑hosted Git |

*All are A3/T2 unless specified.*

---

## Step‑by‑Step Instructions

### 1. Install Base OS

- Install Debian 12 on your hardware (or use a VM for testing).
- Disable unnecessary services. Set up a firewall (`ufw`) to allow SSH (22), VPN port (51820/udp), and later Web UI ports.
- Update the system:
 ```bash
  sudo apt update && sudo apt upgrade -y
 ```

### 2. Install Docker & Docker Compose
 ```bash
sudo apt install docker.io docker-compose -y
sudo systemctl enable docker
 ```

### 3. Prepare Directory Structure

 ```bash
mkdir -p /opt/autonomous-stack/{config,data,backups}
cd /opt/autonomous-stack
 ```

### 4. Deploy Core Services with Docker Compose

The complete `docker-compose.yml` and environment template are in [`code/minimal-server/`](../../code/minimal-server/).

```bash
# Copy the deployment files
cp -r /path/to/tas/code/minimal-server/* /opt/autonomous-stack/

# Create your .env from the template
cp .env.example .env

# Edit .env with real secrets:
# AUTHENTIK_SECRET_KEY — generate with: openssl rand -hex 32
# AUTHENTIK_DB_PASSWORD — generate with: openssl rand -hex 16
nano .env

# Start everything
docker compose up -d
```

→ [`docker-compose.yml`](../../code/minimal-server/docker-compose.yml) — all services  
→ [`.env.example`](../../code/minimal-server/.env.example) — environment template

### 5. Configure WireGuard (VPN)

Install WireGuard:

 ```bash
sudo apt install wireguard -y
 ```

Generate keys:

 ```bash
cd /etc/wireguard
umask 077
wg genkey | tee server_private.key | wg pubkey > server_public.key
 ```

Create /etc/wireguard/wg0.conf:

 ```ini
[Interface]
Address = 10.0.0.1/24
PrivateKey = <server-private-key>
ListenPort = 51820

[Peer]
PublicKey = <client-public-key>
AllowedIPs = 10.0.0.2/32
 ```

Enable and start:

 ```bash
sudo systemctl enable wg-quick@wg0
sudo systemctl start wg-quick@wg0
 ```

### 6. Configure Kopia for Backups

Install Kopia:

 ```bash
wget https://github.com/kopia/kopia/releases/latest/download/kopia-linux-amd64.tar.gz
tar -xzf kopia-linux-amd64.tar.gz
sudo mv kopia /usr/local/bin/
 ```

Create a backup repository on an external drive:

 ```bash
sudo kopia repository create filesystem --path /mnt/backup
 ```

Create a snapshot of your stack:

 ```bash
sudo kopia snapshot create /opt/autonomous-stack
 ```

Set up a daily cron job:

 ```bash
sudo crontab -e
# добавить строку:
0 2 * * * /usr/local/bin/kopia snapshot create /opt/autonomous-stack
```

### 7. Enable Pause (Manual Stop)

Pause and resume scripts are included in [`code/minimal-server/scripts/`](../../code/minimal-server/scripts/).

```bash
# Pause — stops all containers, data stays on disk
./scripts/pause-stack.sh

# Resume — starts all containers
./scripts/resume-stack.sh
```

This implements the **Pause** principle: you can stop the entire stack at any time and resume without loss.

### 8. Verification


Pause: Run sudo pause-stack.sh and verify all containers stop. Resume with docker-compose start.

Exit: All data is stored in local directories (config/, data/, backups/). You can copy these to another machine and recreate the stack. No cloud lock‑in.

Recoverability: Test restoring a Kopia snapshot to a new directory.

Network isolation: Ensure the server can function with internet disconnected (except for initial image pulls).


### Philosophical Reflection

This stack achieves A3 Autonomy (fully autonomous) and T2 Transparency (open source) for most components. It respects the whose.world ethical criteria:

Pause: The stop script gives you control.

Exit: Data is stored locally; you can stop the server and leave.

Recoverability: Kopia snapshots ensure you can go back in time.

Visibility: All components are open source and auditable.

By building this, you become an Architect in open mode, creating a digital flow that returns control to the user.


### Next Steps


Explore other technologies in the catalog (e.g., add Immich for photos, Paperless‑ngx for documents, or Vault for secrets).

Customise the stack with your own domain, certificates, and automation.

Share your experience with the community.

This recipe is a living document. Contributions are welcome!
