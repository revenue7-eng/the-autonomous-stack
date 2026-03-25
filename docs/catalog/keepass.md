---
tags: [passwords, security, offline, encrypted]
title: "KeePass"
category: "security/password-manager"
status: "stable"
license: "GPL-2.0"
source: "https://keepass.info/"
repository: "https://sourceforge.net/projects/keepass/"
documentation: "https://keepass.info/help/base/index.html"
docker_image: "-"
community: "https://sourceforge.net/p/keepass/discussion/"
autonomy_level: "A3"
transparency_level: "T2"
parent: Technology Catalog
nav_order: 1
---

# KeePass

> **TAS Score: S3/3 -- D5/5** -- A3 / T2


## Brief Description
Free, open source password manager that stores credentials in a locally encrypted database file (`.kdbx`). No server, no account, no internet required.

## Architectural Role
Local password vault. Replaces cloud-based password managers (1Password, LastPass, Bitwarden cloud) in the autonomous stack. The `.kdbx` file can be synced via Syncthing or stored on any local drive.

## Technical Autonomy
- ✅ Works without internet
- ✅ Stores data locally (`.kdbx` encrypted file)
- ✅ Does not require external accounts
- ✅ Allows data export (CSV, XML, `.kdbx`)
- ✅ Provides offline updates (manual via installer)

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
|-----------|--------|----------|
| **Pause** | ✅ | Local process, stop anytime, nothing is lost. |
| **Exit** | ✅ | `.kdbx` is an open format, readable by any compatible client. |
| **Recoverability** | ✅ | Database is a plain file — backup = file copy. |
| **Visibility** | ✅ | Open source since 2003, independently audited multiple times. |
| **External Dependencies** | ✅ | Zero cloud dependencies, runs fully offline. |

## Configuration (Minimal)

KeePass is a desktop application — no Docker required. Download and run:

```
https://keepass.info/download.html
```

To sync the database across devices, add the `.kdbx` file to Syncthing:

```ini
# No special config needed — just point Syncthing
# at the folder containing your .kdbx file
```

## Related Recipes
- [Minimal Autonomous Server](../recipes/minimal-server.md)
- [Privacy Homelab](../recipes/privacy-homelab.md)

## Alternatives
- **KeePassXC** – modern cross-platform fork, same A3 level.
- **Vaultwarden** – self-hosted Bitwarden server, A2, requires Docker.
- **Bitwarden** – cloud by default, self-host possible, A1.
- **1Password** – cloud-only, proprietary, A0.

## Trajectory
**Stable — opening.** Maintained by a single developer since 2003, no VC funding, no acquisition, no enterprise tier. The `.kdbx` format has become an open standard adopted by multiple independent clients (KeePassXC, KeePassDX, Strongbox). No license changes in 20+ years.

## Sources
- [Website](https://keepass.info/)
- [Documentation](https://keepass.info/help/base/index.html)
- [Repository](https://sourceforge.net/projects/keepass/)
- [Community](https://sourceforge.net/p/keepass/discussion/)
