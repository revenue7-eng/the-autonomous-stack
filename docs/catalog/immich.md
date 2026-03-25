---
tags: [photos, backup, google-photos-alternative]
title: "Immich"
category: "applications/photos"
status: "stable"
license: "MIT"
source: "https://immich.app"
repository: "https://github.com/immich-app/immich"
documentation: "https://docs.immich.app/overview/quick-start"
docker_image: "https://hub.docker.com/r/immich-app/immich-server"
community: "https://github.com/immich-app/immich/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker", "postgresql"]
optional_deps: []
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
parent: Technology Catalog
nav_order: 13
---

# Immich

> **TAS Score: S3/3 -- D5/5** -- A3 / T2
> **Critical criteria for this category:** Exit, Recoverability.


## Brief Description

Self-hosted photo and video backup solution with a focus on user
experience, automatic organisation, and machine learning features ---
all without cloud dependencies.

## Architectural Role

User application layer: provides a Google Photos alternative that runs
entirely on your own infrastructure, preserving ownership and privacy.

## Technical Autonomy

-   Works without internet (after initial setup)
-   Stores data locally (media files, thumbnails, database)
-   Does not require external accounts
-   Allows data export (media files are ordinary files; database can be
    dumped)
-   Provides offline updates (manual upgrade via Docker)

## Philosophical Assessment (whose.world criteria)

  -----------------------------------------------------------------------
  Criterion                  Status              Comments
  -------------------------- ------------------- ------------------------
  Pause                      Yes                 User controls upload and
                                                 viewing; can pause sync
                                                 at any time.

  Exit                       Yes                 Media files are stored
                                                 as ordinary files; you
                                                 can stop using Immich
                                                 and keep all originals.

  Recoverability             Yes                 Database and uploads can
                                                 be backed up and
                                                 restored.

  Visibility                 Yes                 Open source, fully
                                                 documented.

  External Dependencies      Yes                 No external services
                                                 required; can run
                                                 completely offline.
  -----------------------------------------------------------------------

## Configuration (Minimal)

Example `docker-compose.yml` snippet:

``` yaml
services:
  immich-server:
    image: ghcr.io/immich-app/immich-server:release
    ports:
      - "2283:2283"
    volumes:
      - ./immich-upload:/usr/src/app/upload
    environment:
      DB_HOSTNAME: immich-db
      DB_USERNAME: postgres
      DB_PASSWORD: change-me
    depends_on:
      - immich-db

  immich-db:
    image: postgres:14
    environment:
      POSTGRES_PASSWORD: change-me
    volumes:
      - ./immich-db:/var/lib/postgresql/data
```

## Related Recipes

- [Minimal Autonomous Server](../recipes/minimal-server.md) -- can be extended with Immich for photo
backup.

## Alternatives

-   Photoprism -- more advanced AI features, but less user-friendly
-   Nextcloud Memories -- part of Nextcloud, heavier
-   Piwigo -- older, less modern UI

## Sources

- [Website](https://immich.app)

- [Documentation](https://docs.immich.app/overview/quick-start)

- [Repository](https://github.com/immich-app/immich)

- [Docker image](https://hub.docker.com/r/immich-app/immich-server)

- [Community](https://github.com/immich-app/immich/discussions)

## Trajectory

**Direction: stable.**

Immich is a relatively new project (2022) that has grown rapidly. It uses AGPL-3.0 and is self-hosting-first. The maintainers have been transparent about the project direction and have rejected suggestions to add cloud services. No concerning trends, but the project is young enough that governance structures are still maturing.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ➖ | AGPL-3.0 since launch; no changes. |
| Feature gating | ✅ | No paid tier; all features available to self-hosters. |
| Self-hosting | ✅ | Self-hosting is the only supported deployment model. |
| Governance | ➖ | Small core team; community active on GitHub; governance structures still maturing. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing
