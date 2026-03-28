---
nav_exclude: false
title: "Piped"
category: "applications/media"
status: "stable"
license: "AGPL-3.0"
source: "https://piped.video"
repository: "https://github.com/TeamPiped/Piped"
documentation: "https://docs.piped.video"
docker_image: "1337kavin/piped"
community: "https://github.com/TeamPiped/Piped/discussions"
autonomy_level: "A2"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: []
depended_by: []
critical_criteria: ["Exit", "Pause"]
trajectory: "opening"
parent: Technology Catalog
nav_order: 99
---

# Piped

> **TAS Score: S2/3 — D5/5** — A2 / T2
> S2 not S3: content depends on YouTube's servers — if YouTube blocks your instance or changes API, content becomes unavailable (Q2, Q3). Your subscriptions and watch history are local, but the content is not.

## Brief Description

Privacy-friendly YouTube frontend. Watch YouTube videos without ads, tracking, or a Google account. Self-hosted proxy that fetches content from YouTube on your behalf. Subscriptions, playlists, and watch history stored locally.

## Architectural Role

Media/privacy layer: sits between you and YouTube. Strips tracking, removes ads, provides a clean interface. Your viewing habits stay on your server, not in Google's profile of you. SponsorBlock integration skips sponsor segments automatically.

## Technical Autonomy

- ⚠️ Requires internet (proxies YouTube content)
- ✅ Stores subscriptions and history locally
- ✅ Does not require Google account
- ✅ Export subscriptions as OPML
- ⚠️ Depends on YouTube as content source — no content without YouTube

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅ | Stop instance, subscriptions stay in database. |
| Exit                  | ⚠️ | Subscriptions exportable. But content is YouTube's — no local copies. |
| Recoverability        | ⚠️ | Instance is rebuildable. But YouTube can block your IP. |
| Visibility            | ✅ | AGPL-3.0, fully auditable. |
| External Dependencies | ⚠️ | Entirely dependent on YouTube for content. Privacy layer, not autonomy layer. |

## Configuration (Minimal)

```yaml
services:
  piped:
    image: 1337kavin/piped
    container_name: piped
    ports:
      - "8080:8080"
    restart: unless-stopped
```

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| Invidious | A2 / T2 | Older YouTube frontend. Ruby-based. Similar concept. |
| FreeTube | A2 / T2 | Desktop app, not self-hosted. Local subscriptions. |
| NewPipe | A2 / T2 | Android only. No server needed. |
| YouTube | A0 / T0 | Google account required, full tracking, ads. |

---

## Trajectory

**Direction: opening.**

Active development, growing instance network, AGPL-3.0. Community-driven alternative to YouTube's frontend. Main risk: YouTube actively blocks alternative frontends.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | AGPL-3.0, unchanged. |
| Feature gating | ✅ | No paid tier. |
| Self-hosting | ✅ | Docker, well documented. |
| Governance | ✅ | Community-driven, multiple contributors. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [piped.video](https://piped.video)
- **Repository:** [github.com/TeamPiped/Piped](https://github.com/TeamPiped/Piped)
