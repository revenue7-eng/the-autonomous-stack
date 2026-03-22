---
title: "Kopia"
category: "storage/backup"
status: "stable"
license: "Apache-2.0"
source: "https://kopia.io"
autonomy_level: "A3"
transparency_level: "T2"
---

# Kopia

## Brief Description
Fast and secure open-source backup/restore tool with snapshots, deduplication, compression, and client-side encryption. Works with local storage, network shares, or any S3-compatible backend.

## Architectural Role
Data protection layer: creates versioned, encrypted backups of your data, ensuring recoverability.

## Technical Autonomy
- ✅ Works without internet (if backing up to local storage)
- ✅ Stores data locally (can also use remote storage)
- ✅ Does not require external accounts
- ✅ Allows data export (snapshots are portable)
- ✅ Provides offline updates (manual via packages)

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
|-----------|--------|----------|
| **Pause** | ✅ | Backup can be paused/resumed at any time. |
| **Exit** | ✅ | Snapshots are ordinary files; you can stop using Kopia and keep your data. |
| **Recoverability** | ✅ | Core feature: snapshots allow restoration of previous states. |
| **Visibility** | ✅ | Open source, fully documented. |
| **External Dependencies** | ✅ | None if using local or self-hosted storage. |

## Configuration (Minimal)

Create a repository on an external USB drive:

```bash
kopia repository create filesystem --path /mnt/backup
