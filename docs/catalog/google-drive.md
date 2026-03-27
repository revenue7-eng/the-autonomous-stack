---
nav_exclude: false
title: "Google Drive"
category: "storage/sync"
status: "stable"
license: "Proprietary"
source: "https://drive.google.com"
repository: "-"
documentation: "https://support.google.com/drive"
docker_image: "-"
community: "-"
autonomy_level: "A0"
transparency_level: "T0"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
trajectory: "closing"
parent: Technology Catalog
nav_order: 99
---

# Google Drive

> **TAS Score: S0/3 -- D1/5** -- A0 / T0
> S0 (not S3): Pause, Exit, and Recoverability all fail — continuous sync, lossy export, no user-controlled backup (Q1–Q3). D1 (not D5): closed proprietary system with full cloud dependency; only partial export credit (Q4–Q8).
> **Critical criteria for this category:** Exit, Recoverability.


## Brief Description

Cloud file storage and synchronisation service by Google. Integrated with Google Workspace (Docs, Sheets, Slides). Requires a Google account and internet connection.

## Architectural Role

Storage layer: provides file sync, sharing, and collaboration. Central to many teams' workflows.

## Technical Autonomy

- ❌ Works without internet — requires constant connection for sync and access
- ❌ Stores data locally — local cache exists, but canonical copy is in the cloud
- ❌ Does not require external accounts — requires Google account
- ⚠️ Allows data export — Google Takeout provides bulk export, but Google‑native formats (Docs, Sheets) are converted on export with potential fidelity loss
- ❌ Provides offline updates — client updates are pushed by Google

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status  | Comments |
| --------------------- | ------- | -------- |
| Pause                 | No      | Sync is continuous and automatic. No structural moment to stop and inspect what's happening. |
| Exit                  | Partial | Google Takeout exports data, but Google‑native documents lose formatting. Sharing links, permissions, and collaboration history are not portable. |
| Recoverability        | Partial | 30‑day trash for deleted files. Version history exists but is not exportable. If Google suspends your account, recovery depends on Google's processes. |
| Visibility            | No      | Proprietary. No public source code. No way to audit what the sync client does. |
| External Dependencies | No      | Entirely dependent on Google's infrastructure and account system. |

## Why it's in the catalog

Google Drive is the de facto standard for file sync. Most people use it without evaluating the trade‑offs. This card makes those trade‑offs visible.

**What you gain:** Zero setup. Seamless collaboration. Deep integration with Google Workspace. Reliable uptime. Generous free tier.

**What you give up:** Data sovereignty. Offline independence. Portability of Google‑native formats. Control over your account. Visibility into how the system works.

## Autonomous alternatives

* [Syncthing](syncthing.md) (A3/T2) — P2P file sync, no cloud, no account
* [Nextcloud](https://nextcloud.com) (A3/T2) — self‑hosted cloud with file sync, calendar, contacts
* [Kopia](kopia.md) (A3/T2) — for backup specifically

---

## Trajectory

**Direction: closing.**

Google Drive has no meaningful trajectory toward openness. Google has reduced free storage (15GB shared across services), changed pricing multiple times, and maintains full proprietary control. The service is valuable because of network effects, not architectural openness. Direction is stable-to-closing.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ⚠️ | Proprietary — no change and no expectation of change. |
| Feature gating | ⚠️ | Free tier has been reduced; features tied to Google Workspace subscription. |
| Self-hosting | ⚠️ | No self-hosting path exists or is planned. |
| Governance | ⚠️ | Fully controlled by Google; no community input into direction. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

* [Website](https://drive.google.com)

* [Documentation](https://support.google.com/drive)
