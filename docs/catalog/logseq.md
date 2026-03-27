---
nav_exclude: false
trajectory: "mixed"
parent: "Technology Catalog"
nav_order: 99
title: "Logseq"
category: "applications/notes"
status: "experimental"
license: "AGPL-3.0"
source: "https://github.com/logseq/logseq"
repository: "https://github.com/logseq/logseq"
documentation: "https://docs.logseq.com"
docker_image: "-"
community: "https://discuss.logseq.com"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: ["syncthing"]
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
---

# Logseq

> **TAS Score: S3/3 — D3/5 · A3 / T2**
> _(D3 not D5: Trajectory ⚠️ — announced DB version with closed sync backend. Hidden cost ⚠️ — community split over direction creates migration uncertainty.)_

## Brief Description

Local-first outliner and knowledge graph. Bidirectional links, Markdown files, graph visualization. No server required — works entirely on local files. Strong community plugin ecosystem.

## Architectural Role

Applications layer. Personal knowledge management with graph structure. Fully local — no Docker, no server. Files stored as plain Markdown/EDN — readable without Logseq itself.

## Technical Autonomy

- [x] Works without internet
- [x] Stores data locally
- [x] Does not require external accounts
- [x] Allows data export (Markdown files, direct filesystem access)
- [ ] Provides offline updates

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Desktop app — no server, stop anytime |
| Exit                  | ✅     | Plain Markdown files on disk; readable without Logseq |
| Recoverability        | ✅     | Files are the backup; standard filesystem backup applies |
| Visibility            | ✅     | AGPL-3.0, fully auditable |
| External Dependencies | ✅     | Fully offline; sync via any file sync tool |

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Joplin](joplin.md) | A3 / T2 | More traditional notes, self-hosted sync server |
| [Obsidian](obsidian.md) | A2 / T0 | Proprietary but local-first; larger plugin ecosystem |

---

## Trajectory

**Direction: mixed**

In 2023–2024 Logseq announced a major architectural shift — a new "DB version" moving from plain Markdown files to a proprietary database format. This split the community: the DB version offers better performance but breaks the plain-file philosophy that made Logseq attractive. The sync backend for DB version is not self-hostable. The current file-based version remains AGPL-3.0 and functional, but its long-term maintenance status is uncertain as development focus shifts to DB.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | AGPL-3.0; no changes to current version |
| Feature gating | ⚠️ | DB version introduces closed sync; new features going to DB version only |
| Self-hosting | ➖ | Current file version: fully self-hosted. DB version sync: not self-hostable |
| Governance | ⚠️ | VC-backed; DB version direction driven by commercial interests; community split |

---

## Sources

- **Website:** https://logseq.com
- **Documentation:** https://docs.logseq.com
- **Repository:** https://github.com/logseq/logseq
- **Docker image:** — (desktop app only)
- **Community:** https://discuss.logseq.com
