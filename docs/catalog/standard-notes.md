---
nav_exclude: true
title: "Standard Notes"
category: "applications/notes"
status: "stable"
license: "AGPL-3.0"
source: "https://standardnotes.com"
repository: "https://github.com/standardnotes"
documentation: "https://docs.standardnotes.com"
docker_image: "standardnotes/server"
community: "https://community.standardnotes.com"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: ["docker"]
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
---

# Standard Notes

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

End-to-end encrypted notes app. Cross-platform (Android, iOS, desktop, web). Self-hostable sync server. Plain text notes with optional rich editors. Longevity-focused — designed to last 100 years.

## Architectural Role

Application layer — notes and documents. E2E encrypted sync between devices.

## Technical Autonomy

- [x] Works without internet (local notes cached)
- [x] Stores data locally (on-device, encrypted)
- [x] Does not require external accounts (self-host option)
- [x] Allows data export (plain text, JSON, encrypted backup)
- [x] Provides offline updates (F-Droid, GitHub APK)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Notes stay on device. |
| Exit                  | ✅     | Export to plain text or JSON. |
| Recoverability        | ✅     | Encrypted backups. Version history. |
| Visibility            | ✅     | Fully open-source. |
| External Dependencies | ✅     | Self-hostable server. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

Client: install from F-Droid, App Store, or standardnotes.com.

Self-hosted server:
```yaml
services:
  standardnotes:
    image: standardnotes/server:latest
    ports:
      - "3000:3000"
    environment:
      - DB_HOST=db
```

## Related Recipes

- [Mobile Apps](../mobile.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Joplin](joplin.md) | A3 / T2 | Markdown notes. More features. Sync via Nextcloud/WebDAV. |
| [Obsidian](obsidian.md) | A3 / T1 | Knowledge graph. Proprietary but local-first. |

---

## Trajectory

**Direction: stable**

Sustainable business model (paid hosted plans). All code open-source. Acquired by Proton in 2024 — future direction to watch.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | AGPL-3.0, unchanged. |
| Feature gating | ✅ | Self-hosted has all features. |
| Self-hosting | ✅ | Server fully self-hostable. |
| Governance | ⚠️ | Acquired by Proton. Watch for changes. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** https://standardnotes.com
- **Documentation:** https://docs.standardnotes.com
- **Repository:** https://github.com/standardnotes
- **Docker image:** standardnotes/server
- **Community:** https://community.standardnotes.com
