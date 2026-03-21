# Minimal Autonomous Server

Build a small, fully self‑contained server that you control, with built‑in pauses, clear exit paths, and full recoverability.

## Goal
Create a server that:
- Runs without internet (after initial setup)
- Stores all data locally
- Allows you to pause services, export data, and restore from backups
- Gives you full ownership of your infrastructure

## Components
- **OS**: Debian 12 (or any Linux)
- **Version Control**: Forgejo
- **VPN**: WireGuard
- **Backup**: Kopia
- **Monitoring**: Uptime Kuma

## Steps (summary)
1. Install Debian 12.
2. Install Docker and Docker Compose.
3. Deploy Forgejo using docker-compose.
4. Deploy Uptime Kuma.
5. Set up WireGuard.
6. Configure Kopia backups.
7. Create a script to pause all services.

Full instructions will be expanded later.