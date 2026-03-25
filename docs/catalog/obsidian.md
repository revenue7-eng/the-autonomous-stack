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
parent: Technology Catalog
nav_order: 54
---

# Obsidian

> **TAS Score: S2/3 -- D3/5** -- A2 / T0


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

**Direction: stable with tension.**

Obsidian's core promise -- local Markdown files, no lock-in -- has held since launch. But the company increasingly promotes Obsidian Sync and Publish as paid services, which are cloud-dependent. The app remains free for personal use, but commercial use requires a paid license. No concerning license changes, but the closed-source nature means the community has no recourse if priorities shift.

## Sources

* [Website](https://obsidian.md)
* [Documentation](https://help.obsidian.md)
* [Community](https://forum.obsidian.md)
