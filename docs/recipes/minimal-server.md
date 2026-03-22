# Minimal Autonomous Server

Build a fully autonomous server that operates offline, gives you full control over your data, and respects the three ethical principles: **Pause**, **Exit**, and **Recoverability**.

This recipe combines technologies from the TAS catalog, all evaluated at Autonomy Level A3 (fully autonomous) and Transparency Level T2 (open source).

---

## Goal

Create a server that:

* Runs without internet after initial setup (A3 autonomy)
* Stores all data locally
* Allows you to pause services, export data, and restore from backups
* Gives you full ownership of your infrastructure
* Provides secure remote access via VPN (without cloud coordination)

---

## Components

| Component | Catalog Card                                            | Role                                         |
| --------- | ------------------------------------------------------- | -------------------------------------------- |
| WireGuard | [`network/vpn`](../catalog/wireguard.md)                | Secure remote access without central servers |
| Syncthing | [`storage/sync`](../catalog/syncthing.md)               | P2P file synchronization                     |
| Jellyfin  | [`applications/media`](../catalog/jellyfin.md)          | Offline media server                         |
| Forgejo   | [`applications/version-control`](../catalog/forgejo.md) | Self-hosted Git                              |
| Debian 12 | (OS)                                                    | Base system                                  |

---

## Step-by-Step Instructions

### 1. Install Base OS

* Install Debian 12
* Configure firewall (ufw)
* Update system:

  sudo apt update && sudo apt upgrade -y

---

### 2. Install Docker

```
sudo apt install docker.io docker-compose -y
sudo systemctl enable docker
```

---

### 3. Deploy Core Services

Create working directory:

```
mkdir -p /opt/autonomous-stack
cd /opt/autonomous-stack
```

Create docker-compose.yml:

```
version: '3.8'

services:
  forgejo:
    image: codeberg.org/forgejo/forgejo:1.21
    ports:
      - "3000:3000"
      - "222:22"
    volumes:
      - ./forgejo-data:/data
    environment:
      - FORGEJO__server__DOMAIN=git.local
      - FORGEJO__server__SSH_PORT=222

  syncthing:
    image: syncthing/syncthing:latest
    ports:
      - "8384:8384"
      - "22000:22000"
    volumes:
      - ./syncthing-config:/config
      - ./data:/data

  jellyfin:
    image: jellyfin/jellyfin:latest
    ports:
      - "8096:8096"
    volumes:
      - ./jellyfin-config:/config
      - ./media:/media
```

Start:

```
docker-compose up -d
```

---

### 4. Configure WireGuard

Install:

```
sudo apt install wireguard -y
```

Generate keys:

```
cd /etc/wireguard
umask 077
wg genkey | tee server_private.key | wg pubkey > server_public.key
```

---

### 5. Backup (Kopia)

```
kopia repository create filesystem --path /mnt/backup
kopia snapshot create /opt/autonomous-stack
```

---

### 6. Enable Pause

Create script:

```
sudo nano /usr/local/bin/pause-services.sh
```

Content:

```
#!/bin/bash
cd /opt/autonomous-stack
docker-compose stop
```

Make executable:

```
sudo chmod +x /usr/local/bin/pause-services.sh
```

---

### 7. Verification

Pause:

* run pause-services.sh

Exit:

* copy volumes and run on another machine

Recoverability:

* restore via Kopia or volume backup

---

## Philosophical Reflection

Pause:
Manual stop via script or Docker.

Exit:
All data stored locally in plain volumes.

Recoverability:
Backups allow full restoration.

---

## Next Steps

* Add Immich (photos)
* Add Paperless-ngx (documents)
* Add Uptime Kuma (monitoring)

Contributions are welcome.
