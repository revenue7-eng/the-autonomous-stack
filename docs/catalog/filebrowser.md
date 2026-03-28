---
nav_exclude: false
title: "File Browser"
category: "applications/files"
status: "stable"
license: "Apache-2.0"
source: "https://filebrowser.org"
repository: "https://github.com/filebrowser/filebrowser"
documentation: "https://filebrowser.org"
docker_image: "filebrowser/filebrowser"
community: "https://github.com/filebrowser/filebrowser/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: []
depended_by: []
critical_criteria: ["Exit", "Pause"]
trajectory: "stable"
parent: Technology Catalog
nav_order: 99
---

# File Browser

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Web-based file manager. Browse, upload, download, edit, and share files on your server through a clean web interface. Single binary, zero configuration. Replaces the need to SSH into your server to manage files.

## Architectural Role

Applications/utility layer: web file manager for your server. Gives non-technical family members or team members access to files without SSH or SFTP knowledge. Useful alongside Nextcloud for direct server filesystem access.

## Technical Autonomy

- ✅ Works without internet
- ✅ Files are plain files on disk — no database, no abstraction
- ✅ Does not require external accounts
- ✅ Nothing to export — files are already on your filesystem
- ✅ Single binary, no dependencies

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅ | Stop it, files stay on disk. |
| Exit                  | ✅ | Files are plain files. No migration needed. |
| Recoverability        | ✅ | No state to lose. Config is one JSON file. |
| Visibility            | ✅ | Apache-2.0. Simple Go codebase. |
| External Dependencies | ✅ | Fully self-contained. |

## Configuration (Minimal)

```yaml
services:
  filebrowser:
    image: filebrowser/filebrowser
    container_name: filebrowser
    ports:
      - "8085:80"
    volumes:
      - /path/to/your/files:/srv
      - ./data/filebrowser/filebrowser.db:/database/filebrowser.db
    restart: unless-stopped
```

## Related Recipes

- [Family Cloud](../recipes/family-cloud.md) — add File Browser for direct file access

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Nextcloud](nextcloud.md) | A3 / T2 | Full cloud platform with file management. Much more complex. |
| [Syncthing](syncthing.md) | A3 / T2 | P2P sync, not web file manager. Different use case. |
| SFTP/SCP | A3 / T2 | Command line. No web UI. |

---

## Trajectory

**Direction: stable.**

Mature, focused tool. Apache-2.0 licensed. Does one thing well. Active community, regular releases.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | Apache-2.0, unchanged. |
| Feature gating | ✅ | No paid tier. |
| Self-hosting | ✅ | Single binary or Docker. Minimal resources. |
| Governance | ➖ | Community maintained. Multiple contributors. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [filebrowser.org](https://filebrowser.org)
- **Repository:** [github.com/filebrowser/filebrowser](https://github.com/filebrowser/filebrowser)
- **Docker image:** `filebrowser/filebrowser`
