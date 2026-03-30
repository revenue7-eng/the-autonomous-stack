---
nav_exclude: false
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
depends_on: []
optional_deps: ["syncthing"]
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
trajectory: "stable"
parent: Technology Catalog
nav_order: 99
---

# KeePass

> **TAS Score: S3/3 — D5/5** — A3 / T2
>
> _Assessment criteria: [v1.1](assessment-criteria.md). Context: desktop app · single-user. Last verified: 2025-05._

## Brief Description

Free, open source password manager that stores credentials in a locally encrypted database file (`.kdbx`). No server, no account, no internet required.

## Architectural Role

Local password vault. Replaces cloud-based password managers (1Password, LastPass, Bitwarden cloud). The `.kdbx` file can be synced via Syncthing or stored on any local drive.

---

## Formal Assessment

### S1: Pause

| Test | Result | Evidence |
|------|--------|----------|
| Can you stop the process without a special shutdown procedure? | ✅ Yes | Close the application. Local process, no daemon. |
| After stopping, is all data still on disk in a readable state? | ✅ Yes | `.kdbx` file on disk, encrypted. Unchanged when app closes. |
| Can you restart and continue where you left off? | ✅ Yes | Open app → open `.kdbx` file → all entries present. |

**S1 = Yes**

### S2: Exit

| Test | Result | Evidence |
|------|--------|----------|
| Is there a documented export mechanism? | ✅ Yes | Export to CSV, XML, HTML. Or just copy the `.kdbx` file. |
| Does the export include ALL user data? | ✅ Yes | All entries, groups, custom fields, attachments, history. |
| Is the export in a standard, reusable format? | ✅ Yes | `.kdbx` is an open format with published specification. CSV/XML are universal. |
| Can another tool import the exported data? | ✅ Yes | KeePassXC, KeePassDX (Android), KeeWeb, Bitwarden — all read `.kdbx`. |

**S2 = Yes**

### S3: Recoverability

| Test | Result | Evidence |
|------|--------|----------|
| Does the service support backups? | ✅ Yes | Database is a single file — any backup tool works. KeePass auto-creates `.kdbx.bak` on save. |
| Can you restore from backup to a working state? | ✅ Yes | Copy `.kdbx` back → open in KeePass. Done. |
| Does a restore give you back the SAME state? | ✅ Yes | File is self-contained. All data, all history, all attachments. |

**S3 = Yes**

### Autonomy Level

| S1 | S2 | S3 | Level |
|----|----|----|-------|
| Yes | Yes | Yes | **A3** |

### Transparency Level

| Test | Result | Evidence |
|------|--------|----------|
| Source code publicly available? | ✅ Yes | sourceforge.net/projects/keepass/ |
| License OSI-approved? | ✅ Yes | GPL-2.0 |

**T = T2**

### Diagnostic Score

| # | Question | Result | Evidence |
|---|----------|--------|----------|
| D1 | Personalisation | ✅ Clean | No analytics. No network access. No user tracking. |
| D2 | Urgency | ✅ Clean | No notifications. No forced updates. No deadlines. |
| D3 | Hidden cost | ✅ Clean | No ads. No identity requirements. No lock-in. Open format. |
| D4 | Transparency fragility | ✅ Clean | Value is password storage. Fully transparent. No dark patterns. |
| D5 | Trajectory | ✅ Clean | GPL-2.0 since 2003. No paid tier ever. KDBX is an open standard with 10+ independent implementations. |

**D-score: D5/5** (0 concerns)

---

## Counterarguments

| Claim | Challenge | Resolution |
|-------|-----------|------------|
| **A3: fully autonomous** | No built-in sync — needs external tool to share across devices | By design. KeePass is a vault, not a sync service. Sync is delegated to Syncthing, USB, or any file transfer method. This is a feature, not a limitation. |
| **D5: no concerns** | Single maintainer (Dominik Reichl) since 2003 — bus factor risk | The KDBX format is open and implemented by 10+ independent projects (KeePassXC, KeePassDX, KeeWeb). If KeePass development stops, the ecosystem survives. Noted in Trajectory. |
| **D5: no concerns** | Windows-only (KeePass 2.x uses .NET/Mono) | KeePassXC is a cross-platform fork with same A3/T2 rating. Ecosystem diversity compensates. |

---

## Configuration (Minimal)

Desktop application — no Docker required.

```
Download: https://keepass.info/download.html
```

Sync database across devices with Syncthing:

```
# Add the folder containing your .kdbx file to Syncthing
# No special configuration needed
```

## Related Recipes

- [Minimal Autonomous Server](../recipes/minimal-server.md)
- [GrapheneOS Mobile Stack](../recipes/grapheneos-mobile.md) (via KeePassDX)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| KeePassXC | A3 / T2 | Cross-platform C++ fork. Same `.kdbx` format. Recommended for Linux/macOS. |
| [Vaultwarden](vaultwarden.md) | A3 / T2 | Self-hosted Bitwarden server. Browser integration. Requires Docker. |
| 1Password | A0 / T0 | Cloud-only, proprietary. |

---

## Trajectory

**Direction: stable.**

KeePass is one of the oldest password managers (2003) with an unchanged GPL-2.0 licence. The KDBX format is an open standard with 10+ independent implementations. No corporate ownership, no cloud service, no monetisation pressure.

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | GPL-2.0 since 2003; never changed. |
| Feature gating | ✅ | No paid tier exists and never has. |
| Self-hosting | ✅ | Local-only by design; no cloud component. |
| Governance | ⚠️ | Single maintainer. KDBX format is independent, mitigating risk. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** https://keepass.info
- **Documentation:** https://keepass.info/help/base/index.html
- **Repository:** https://sourceforge.net/projects/keepass/
- **Community:** https://sourceforge.net/p/keepass/discussion/
