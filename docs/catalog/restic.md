---
nav_exclude: false
title: "Restic"
category: "storage/backup"
status: "stable"
license: "BSD-2-Clause"
source: "https://restic.net"
repository: "https://github.com/restic/restic"
documentation: "https://restic.readthedocs.io"
docker_image: "restic/restic"
community: "https://forum.restic.net"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: ["docker"]
depended_by: []
critical_criteria: ["Recoverability", "Exit"]
trajectory: "stable"
parent: Technology Catalog
nav_order: 99
---

# Restic

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Fast, secure, and efficient backup program. Encrypts backups client-side, deduplicates data across snapshots, and supports multiple backends: local disk, SFTP, S3, MinIO, Backblaze B2, and more. Single binary, no server component needed.

## Architectural Role

Storage/backup layer: CLI backup tool. Unlike Kopia which has a web UI and server mode, Restic is purely command-line. Excellent for scripted backups, cron jobs, and automation. Often paired with a scheduling wrapper like Autorestic or Runrestic.

## Technical Autonomy

- ✅ Works without internet (with local or LAN backup targets)
- ✅ Stores data locally (encrypted repository on any filesystem)
- ✅ Does not require external accounts
- ✅ Repository format is documented and stable
- ✅ Single binary, no dependencies

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅ | No running daemon. Run when you want, skip when you don't. |
| Exit                  | ✅ | Restore from any Restic binary. Repository format is stable and documented. |
| Recoverability        | ✅ | Built-in integrity checking. Restore individual files or full snapshots. |
| Visibility            | ✅ | BSD-2-Clause. Simple Go codebase. |
| External Dependencies | ✅ | Fully standalone. Backend choice is yours. |

## Configuration (Minimal)

```bash
# Initialize a local backup repository
restic init --repo /mnt/backup/restic-repo

# Create a snapshot
restic -r /mnt/backup/restic-repo backup /opt/my-data

# List snapshots
restic -r /mnt/backup/restic-repo snapshots

# Restore
restic -r /mnt/backup/restic-repo restore latest --target /tmp/restore
```

Automated with cron:

```bash
0 3 * * * RESTIC_PASSWORD_FILE=/etc/restic-password restic -r /mnt/backup/restic-repo backup /opt/my-data --exclude-caches
```

## Related Recipes

- [Minimal Autonomous Server](../recipes/minimal-server.md) — alternative to Kopia for backups

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Kopia](kopia.md) | A3 / T2 | Web UI, server mode, snapshots. More user-friendly. TAS recommended. |
| BorgBackup | A3 / T2 | Similar to Restic. Compression-first, slightly older. Python-based. |
| Duplicati | A3 / T2 | GUI-based, more backends. .NET-based. Less efficient dedup. |

---

## Trajectory

**Direction: stable.**

Restic has been one of the most trusted backup tools since 2015. BSD-2-Clause, single maintainer with community contributors. Steady development, no commercial pressure. The repository format stability guarantee is a strong autonomy signal.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | BSD-2-Clause, unchanged. Maximally permissive. |
| Feature gating | ✅ | No paid tier. |
| Self-hosting | ✅ | Single binary. No server component. |
| Governance | ⚠️ | Primary maintainer (fd0). Bus factor risk, but well-documented format ensures long-term viability. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [restic.net](https://restic.net)
- **Repository:** [github.com/restic/restic](https://github.com/restic/restic)
- **Docker image:** `restic/restic`
