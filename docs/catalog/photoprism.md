---
nav_exclude: false
parent: "Technology Catalog"
nav_order: 99
title: "PhotoPrism"
category: "applications/photos"
status: "stable"
license: "AGPL-3.0"
source: "https://github.com/photoprism/photoprism"
repository: "https://github.com/photoprism/photoprism"
documentation: "https://docs.photoprism.app"
docker_image: "photoprism/photoprism"
community: "https://github.com/photoprism/photoprism/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: ["prometheus"]
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
---

# PhotoPrism

> **TAS Score: S3/3 — D4/5 · A3 / T2**
> _(D4 not D5: PhotoPrism+ is a paid closed tier with additional features — trajectory is mixed.)_

## Brief Description

AI-powered self-hosted photo management. Automatic tagging, face recognition, geo-mapping, duplicate detection. Works with your existing folder structure — original files are never modified.

## Architectural Role

Applications layer. Photo management and browsing. Pairs naturally with Immich (which focuses on mobile backup) — PhotoPrism is stronger on library organisation and search.

## Technical Autonomy

- [x] Works without internet
- [x] Stores data locally
- [x] Does not require external accounts
- [x] Allows data export (original files always accessible)
- [ ] Provides offline updates

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Clean stop, no permanent damage |
| Exit                  | ✅     | Original files untouched; sidecar metadata exportable |
| Recoverability        | ✅     | Standard backup of data directory and database |
| Visibility            | ✅     | AGPL-3.0, fully auditable |
| External Dependencies | ✅     | Runs fully offline; optional maps tile server |

## Configuration (Minimal)

```yaml
services:
  photoprism:
    image: photoprism/photoprism:latest
    environment:
      PHOTOPRISM_AUTH_MODE: "password"
      PHOTOPRISM_SITE_URL: "https://photos.yourdomain.com"
      PHOTOPRISM_ORIGINALS_LIMIT: 5000
      PHOTOPRISM_HTTP_COMPRESSION: "gzip"
      PHOTOPRISM_DATABASE_DRIVER: "sqlite"
      PHOTOPRISM_ADMIN_USER: "admin"
      PHOTOPRISM_ADMIN_PASSWORD: "changeme"
    volumes:
      - ./originals:/photoprism/originals
      - ./storage:/photoprism/storage
    ports:
      - "2342:2342"
```

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Immich](immich.md) | A3 / T2 | Better mobile backup; weaker library organisation |

---

## Trajectory

**Direction: mixed**

PhotoPrism is AGPL-3.0 and self-hosting is a first-class use case. However, the project introduced PhotoPrism+ in 2022 — a paid tier with additional features (expandable library limit, priority support). The core remains open. Watch for more features migrating to the paid tier over time.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | AGPL-3.0 since launch; no changes |
| Feature gating | ⚠️ | PhotoPrism+ introduced 2022; some features require paid activation |
| Self-hosting | ✅ | Self-hosting is the primary use case; docs actively maintained |
| Governance | ➖ | Small team; primary maintainer drives direction; no foundation |

---

## Sources

- **Website:** https://photoprism.app
- **Documentation:** https://docs.photoprism.app
- **Repository:** https://github.com/photoprism/photoprism
- **Docker image:** photoprism/photoprism
- **Community:** https://github.com/photoprism/photoprism/discussions
