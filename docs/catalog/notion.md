---
tags: [notes, documents, workspace, cloud, alternative]
title: "Notion"
category: "applications/documents"
status: "stable"
license: "Proprietary"
source: "https://notion.so"
repository: "-"
documentation: "https://www.notion.so/help"
docker_image: "-"
community: "-"
autonomy_level: "A0"
transparency_level: "T0"
parent: Technology Catalog
nav_order: 51
---

# Notion

> **TAS Score: S0/3 -- D1/5** -- A0 / T0


## Brief Description

All‑in‑one workspace for notes, documents, databases, wikis, and project management. Cloud‑only. Requires an account and internet connection for full functionality.

## Architectural Role

Applications layer: replaces multiple tools (notes, wiki, task management, databases) with a single platform.

## Technical Autonomy

- ❌ Works without internet — limited offline mode; requires internet for sync, collaboration, and most features
- ❌ Stores data locally — all canonical data is on Notion's servers
- ❌ Does not require external accounts — requires Notion account
- ⚠️ Allows data export — exports to Markdown and CSV, but loses database relations, views, formulas, and rich formatting
- ❌ Provides offline updates — client updates controlled by Notion

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status  | Comments |
| --------------------- | ------- | -------- |
| Pause                 | No      | No structural pause. Always connected, always syncing. Notifications and updates are continuous. |
| Exit                  | Partial | Export exists but is lossy. Complex databases, relations, and views do not survive export. The more you invest in Notion's unique features, the harder it is to leave. |
| Recoverability        | Partial | Page history available on paid plans. No user‑controlled backups. If Notion has an outage or suspends your account, your data is inaccessible. |
| Visibility            | No      | Proprietary. No source code. No way to audit data handling. |
| External Dependencies | No      | Entirely dependent on Notion's cloud infrastructure. |

## Why it's in the catalog

Notion is one of the most popular productivity tools. Its power comes from flexibility — but that flexibility creates deep lock‑in. The more you build inside Notion, the harder it is to leave. This is the classic closed‑mode trade‑off: convenience in exchange for exit cost.

**What you gain:** Beautiful interface. Flexible databases. All‑in‑one workspace. Excellent collaboration.

**What you give up:** Data portability. Offline access. Control over your workspace if Notion changes pricing or terms.

## Autonomous alternatives

* [Paperless‑ngx](paperless-ngx.md) (A3/T2) — document management with OCR
* [Bookstack](https://www.bookstackapp.com) (A3/T2) — self‑hosted wiki
* [Obsidian](https://obsidian.md) + [Syncthing](syncthing.md) — local Markdown notes with P2P sync

## Sources

* [Website](https://notion.so)

* [Documentation](https://www.notion.so/help)

## Trajectory
**Mixed — VC-backed, pricing pressure.**

Notion has raised over $330M in funding. The free tier has been progressively restricted. Enterprise features are aggressively priced. The product is deeply integrated — the more you use Notion, the harder it is to leave, which is the mechanism that supports pricing power.

Direction: **closing**. Not in terms of the product disappearing, but in terms of the exit cost increasing over time. The export format remains lossy, which means the lock-in compounds.
