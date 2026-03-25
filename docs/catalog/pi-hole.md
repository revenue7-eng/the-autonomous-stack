---
tags: [dns, network, privacy, ad-blocking]
title: "Pi-hole"
category: "network/dns"
status: "stable"
license: "EUPL-1.2"
source: "https://pi-hole.net"
repository: "https://github.com/pi-hole/pi-hole"
documentation: "https://docs.pi-hole.net"
docker_image: "https://hub.docker.com/r/pihole/pihole"
community: "https://discourse.pi-hole.net"
autonomy_level: "A3"
transparency_level: "T2"
parent: Technology Catalog
nav_order: 22
---

# Pi-hole

> **TAS Score: S3/3 -- D5/5** -- A3 / T2


## Brief Description

Network-wide ad blocker and DNS sinkhole. Blocks ads, trackers, and malware at the DNS level for every device on your network -- without installing anything on individual devices.

## Architectural Role

Network layer: DNS resolver with filtering. Sits between your devices and the internet, blocking unwanted domains before they load. Similar role to AdGuard Home.

## Technical Autonomy

- ✅ Works without internet (local DNS resolution and filtering continue; upstream DNS requires internet)
- ✅ Stores data locally (configuration, blocklists, query logs)
- ✅ Does not require external accounts
- ✅ Allows data export (configuration and teleporter backup built in)
- ✅ Provides offline updates (manual upgrade via packages or Docker)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
| --------------------- | ------ | -------- |
| Pause                 | Yes    | Service can be disabled temporarily via web UI; DNS falls back to upstream. |
| Exit                  | Yes    | No vendor lock-in. Teleporter exports full configuration. Point DNS elsewhere and you're done. |
| Recoverability        | Yes    | Teleporter backup/restore. Configuration files can be version-controlled. |
| Visibility            | Yes    | Open source (EUPL-1.2), fully auditable. Query log shows exactly what's blocked and why. |
| External Dependencies | Yes    | No mandatory external services. Gravity (blocklist) updates need internet but can be done manually. |

## Configuration (Minimal)

Example `docker-compose.yml` snippet:

```yaml
services:
  pihole:
    image: pihole/pihole:latest
    container_name: pihole
    ports:
      - "53:53/tcp"
      - "53:53/udp"
      - "8053:80/tcp"
    volumes:
      - ./pihole-etc:/etc/pihole
      - ./pihole-dnsmasq:/etc/dnsmasq.d
    environment:
      WEBPASSWORD: change-me
    restart: unless-stopped
```

## Related Recipes

* [Minimal Autonomous Server](../recipes/minimal-server.md) -- uses AdGuard Home for DNS filtering; Pi-hole is an alternative.

## Alternatives

* AdGuard Home -- more modern UI, native DNS-over-HTTPS/QUIC, more features out of the box
* Blocky -- lightweight DNS proxy with blocklists, config-file only
* NextDNS -- cloud-based, not self-hosted, A0/T1

## Sources

* [Website](https://pi-hole.net)
* [Documentation](https://docs.pi-hole.net)
* [Repository](https://github.com/pi-hole/pi-hole)
* [Docker image](https://hub.docker.com/r/pihole/pihole)
* [Community](https://discourse.pi-hole.net)
-e 
## Trajectory
**Stable — community project.**

Pi-hole is maintained by a small volunteer team with no commercial entity. It is one of the oldest and most established self-hosted tools. No enterprise tier, no cloud features. Direction: **stable**.
