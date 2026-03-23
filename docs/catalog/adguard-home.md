---
title: "AdGuard Home"
category: "network/dns"
status: "stable"
license: "GPL-3.0"
source: "https://adguard.com/en/home/overview.html"
repository: "https://github.com/AdguardTeam/AdGuardHome"
documentation: "https://github.com/AdguardTeam/AdGuardHome/wiki"
docker_image: "https://hub.docker.com/r/adguard/adguardhome"
community: "https://github.com/AdguardTeam/AdGuardHome/discussions"
autonomy_level: "A3"
transparency_level: "T2"
parent: Technology Catalog
nav_order: 2
---

# AdGuard Home

## Brief Description

Network-wide software for blocking ads, trackers, and malware. Works as a DNS server with filtering and parental control, entirely self‑hosted.

## Architectural Role

Network layer: provides DNS resolution with content filtering, can also act as DHCP server. A core component for maintaining a clean, private network.

## Technical Autonomy

- ✅ Works without internet (after initial setup; caching and local filtering continue)
- ✅ Stores data locally (configuration, statistics, filter lists)
- ✅ Does not require external accounts
- ✅ Allows data export (config export, statistics can be backed up)
- ✅ Provides offline updates (manual upgrade via packages or Docker)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
| --------------------- | ------ | -------- |
| Pause                 | Yes    | DNS service can be stopped/started manually; filtering can be disabled per client. |
| Exit                  | Yes    | No vendor lock‑in; all configuration and logs are local, can be migrated. |
| Recoverability        | Yes    | Configuration backups, statistics export. |
| Visibility            | Yes    | Open source, full documentation, query logs visible to admin. |
| External Dependencies | Yes    | No required external services; can run completely offline. |

## Configuration (Minimal)

Example `docker-compose.yml` snippet:

```yaml
services:
  adguard-home:
    image: adguard/adguardhome:latest
    container_name: adguard-home
    ports:
      - "53:53/tcp"
      - "53:53/udp"
      - "80:80/tcp"          # Web UI
      - "443:443/tcp"        # HTTPS
      - "784:784/udp"        # DNS-over-QUIC
    volumes:
      - ./adguard-work:/opt/adguardhome/work
      - ./adguard-conf:/opt/adguardhome/conf
    restart: unless-stopped
```

## Related Recipes

* [Minimal Autonomous Server](../recipes/minimal-server.md) – can be extended with AdGuard Home for network‑wide ad blocking.

## Alternatives

* Pi‑hole – similar, but AdGuard Home offers native DoT/DoQ and more advanced features.
* NextDNS – cloud‑based, not fully autonomous.
* Unbound – recursive DNS resolver without filtering.

## Sources

* [Website](https://adguard.com/en/adguard-home/overview.html)

* [Documentation](https://github.com/AdguardTeam/AdGuardHome/wiki)

* [Repository](https://github.com/AdguardTeam/AdGuardHome)

* [Docker image](https://hub.docker.com/r/adguard/adguardhome)

* [Community](https://github.com/AdguardTeam/AdGuardHome/discussions)
