---
tags: [cloud, files, calendar, contacts, google-alternative]
title: "Nextcloud"
category: "applications/cloud"
status: "stable"
license: "AGPL-3.0"
source: "https://nextcloud.com"
repository: "https://github.com/nextcloud/server"
documentation: "https://docs.nextcloud.com"
docker_image: "https://hub.docker.com/_/nextcloud"
community: "https://help.nextcloud.com"
autonomy_level: "A3"
transparency_level: "T2"
parent: Technology Catalog
nav_order: 16
---

# Nextcloud

## Brief Description

Self-hosted cloud platform providing file sync, calendar, contacts, email, office documents, video calls, and more -- all under your control. The most comprehensive open-source alternative to Google Workspace and Microsoft 365.

## Architectural Role

Applications layer: central hub for personal and team productivity. Replaces multiple cloud services with a single self-hosted platform.

## Technical Autonomy

- ✅ Works without internet (after initial setup; all data local)
- ✅ Stores data locally (files, database, configuration)
- ✅ Does not require external accounts
- ✅ Allows data export (files are ordinary files; database can be dumped; CalDAV/CardDAV are open standards)
- ✅ Provides offline updates (manual upgrade via packages or Docker)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status  | Comments |
| --------------------- | ------- | -------- |
| Pause                 | Yes     | Services can be stopped; data remains on disk. |
| Exit                  | Yes     | Files are ordinary files. Calendar and contacts use open standards (CalDAV, CardDAV). Database can be exported. |
| Recoverability        | Yes     | Database and file backups; versioning built in for files. |
| Visibility            | Yes     | Open source (AGPL-3.0), fully auditable. |
| External Dependencies | Yes     | No mandatory external services. Push notifications use Nextcloud's server by default but can be self-hosted. |

## Configuration (Minimal)

Example `docker-compose.yml` snippet:

```yaml
services:
  nextcloud:
    image: nextcloud:latest
    ports:
      - "8080:80"
    volumes:
      - ./nextcloud-data:/var/www/html
    environment:
      SQLITE_DATABASE: nextcloud
    restart: unless-stopped
```

For production, use PostgreSQL or MariaDB instead of SQLite.

## Related Recipes

* [Minimal Autonomous Server](../recipes/minimal-server.md) -- can be extended with Nextcloud for full cloud replacement.

## Alternatives

* Syncthing -- lighter, P2P only, no calendar/contacts/office
* Seafile -- file sync focused, less feature-rich
* Google Workspace -- cloud-only, A0/T0

## Trajectory

**Direction: stable.**

Nextcloud has consistently maintained its open-source commitment since forking from ownCloud in 2016. The AGPL license ensures that modifications must be shared. The company monetises through enterprise support, not by closing features. Community governance is active. No license changes or concerning trends.

## Sources

* [Website](https://nextcloud.com)
* [Documentation](https://docs.nextcloud.com)
* [Repository](https://github.com/nextcloud/server)
* [Docker image](https://hub.docker.com/_/nextcloud)
* [Community](https://help.nextcloud.com)
