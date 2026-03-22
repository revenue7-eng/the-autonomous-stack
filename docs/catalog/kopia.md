---
autonomy_level: A3
category: storage/backup
license: Apache-2.0
source: "https://kopia.io"
repository: "https://github.com/kopia/kopia"
documentation: "https://kopia.io/docs/"
docker_image: "https://hub.docker.com/r/kopia/kopia"
community: "https://github.com/kopia/kopia/discussions"
status: stable
title: Kopia
transparency_level: T2
---

# Kopia

## Brief Description

Fast and secure open-source backup/restore tool with snapshots,
deduplication, compression, and client-side encryption. Works with local
storage, network shares, or any S3-compatible backend.

## Architectural Role

Data protection layer: creates versioned, encrypted backups of your
data, ensuring recoverability.

## Technical Autonomy

-   ✅ Works without internet (if backing up to local storage)
-   ✅ Stores data locally (can also use remote storage)
-   ✅ Does not require external accounts
-   ✅ Allows data export (snapshots are portable)
-   ✅ Provides offline updates (manual via packages)

## Philosophical Assessment (whose.world criteria)

  -----------------------------------------------------------------------
  Criterion                  Status              Comments
  -------------------------- ------------------- ------------------------
  **Pause**                  ✅                  Backup can be
                                                 paused/resumed at any
                                                 time.

  **Exit**                   ✅                  Snapshots are ordinary
                                                 files; you can stop
                                                 using Kopia and keep
                                                 your data.

  **Recoverability**         ✅                  Core feature: snapshots
                                                 allow restoration of
                                                 previous states.

  **Visibility**             ✅                  Open source, fully
                                                 documented.

  **External Dependencies**  ✅                  None if using local or
                                                 self-hosted storage.
  -----------------------------------------------------------------------

## Configuration (Minimal)

Create a repository on an external USB drive:

``` bash
kopia repository create filesystem --path /mnt/backup
```

Create a snapshot of your Docker data:

``` bash
kopia snapshot create /opt/autonomous-stack
```

List snapshots:

``` bash
kopia snapshot list
```

Restore:

``` bash
kopia restore <snapshot-id> /tmp/restored
```

Set up a daily cron job to run snapshots:

``` bash
0 2 * * * /usr/local/bin/kopia snapshot create /opt/autonomous-stack
```

## Related Recipes

[Minimal Autonomous Server](../recipes/minimal-server.md) -- uses Kopia for backups.

## Alternatives

-   BorgBackup -- similar, but Kopia has a more modern UI and cloud
    support
-   Duplicati -- GUI-based, but less reliable for large datasets
-   Restic -- fast, but no built-in GUI

## Sources

-   Kopia Official Website
-   Kopia Documentation

