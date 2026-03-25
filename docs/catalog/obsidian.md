---
tags: [notes, markdown, knowledge, local-first]
title: "Obsidian"
category: "applications/notes"
status: "stable"
license: "Proprietary (free for personal use)"
source: "https://obsidian.md"
repository: "-"
documentation: "https://help.obsidian.md"
docker_image: "-"
community: "https://forum.obsidian.md"
autonomy_level: "A2"
transparency_level: "T0"
depends_on: []
optional_deps: ["syncthing"]
depended_by: []
critical_criteria: ["Exit"]
parent: Technology Catalog
nav_order: 54
---

# Obsidian

> **TAS Score: S2/3 -- D3/5** -- A2 / T0
> S2 (not S3): Recoverability is partial — no built-in backup, depends on external tools (Q3). D3 (not D5): closed-source application (Q7 transparency fragility); Obsidian Sync is a cloud service (Q6 hidden cost); no telemetry audit possible.
> **Critical criteria for this category:** Exit.


## Brief Description

Local-first knowledge management app based on plain Markdown files stored on your device. Rich plugin ecosystem. Free for personal use, paid for commercial and sync.

## Architectural Role

Applications layer: personal knowledge base, note-taking, writing, and research tool. Files live on your filesystem -- Obsidian is a viewer and editor, not a storage service.

## Technical Autonomy

- ✅ Works without internet (fully offline; all files are local Markdown)
- ✅ Stores data locally (plain .md files in a folder you choose)
- ❌ Does not require external accounts -- no account needed for local use, but Obsidian Sync and Publish require an account
- ✅ Allows data export (files are plain Markdown -- nothing to export, they're already yours)
- ❌ Provides offline updates -- updates are pushed by Obsidian; app itself is proprietary

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status  | Comments |
| --------------------- | ------- | -------- |
| Pause                 | Yes     | Close the app; files remain. No background sync unless you enabled Obsidian Sync. |
| Exit                  | Yes     | Files are plain Markdown in a regular folder. Stop using Obsidian and keep everything. Open them in any text editor. |
| Recoverability        | Partial | Local file versioning via plugins. No built-in backup. Depends on your filesystem and external backup tools. |
| Visibility            | No      | Proprietary application. Source code not available. Plugins are open source, but the core is closed. |
| External Dependencies | Partial | Core app works fully offline. Obsidian Sync and Publish are cloud services tied to Obsidian accounts. |

## Why A2 and not A3

Obsidian scores well on Pause and Exit -- your data is plain Markdown, fully portable, no lock-in. But the application itself is proprietary (T0), updates are controlled by the company, and there's no way to audit what the app does. If Obsidian disappears, your files survive -- but you need a new editor.

This is the A2 pattern: your data is autonomous, your tool is not.

## Configuration (Minimal)

Download from [obsidian.md](https://obsidian.md). Open a folder. Start writing. No server, no Docker, no configuration.

For sync without Obsidian Sync, use [Syncthing](syncthing.md) to sync the vault folder between devices.

## Related Recipes

* [Minimal Autonomous Server](../recipes/minimal-server.md) -- use Syncthing to sync Obsidian vaults across devices without cloud.

## Alternatives

* Logseq -- open source (AGPL), similar local-first approach, but outliner-based
* Joplin -- open source, Markdown notes with sync
* Notion -- cloud-only, A0/T0 -- more features, less autonomy

## Trajectory

**Direction: stable.**

Obsidian's core promise — local Markdown files, no lock-in — has held since launch. The company promotes Obsidian Sync and Publish as paid cloud services, but these are opt-in additions, not replacements for local functionality. The closed-source nature means the community has no recourse if priorities shift.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ➖ | Proprietary app; free for personal use, paid for commercial use. No change since launch. |
| Feature gating | ➖ | Sync and Publish are paid cloud services, but local functionality is complete without them. |
| Self-hosting | ➖ | Local-first by design; no self-hosted server component (Sync uses Obsidian's cloud). |
| Governance | ⚠️ | Privately held; no community governance; direction opaque. No open-source recourse if app is discontinued. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

## Sources

* [Website](https://obsidian.md)
* [Documentation](https://help.obsidian.md)
* [Community](https://forum.obsidian.md)
