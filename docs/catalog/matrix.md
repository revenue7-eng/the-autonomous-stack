---
nav_exclude: false
title: "Matrix / Element"
trajectory: "stable"
parent: "Technology Catalog"
nav_order: 99
category: "communication/messaging"
status: "stable"
license: "Apache-2.0 (Synapse), AGPL-3.0 (Element)"
source: "https://github.com/element-hq/synapse"
repository: "https://github.com/element-hq/synapse"
documentation: "https://element-hq.github.io/synapse/latest/"
docker_image: "matrixdotorg/synapse"
community: "https://matrix.to/#/#synapse:matrix.org"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: ["postgresql"]
depended_by: []
critical_criteria: ["Recoverability"]
---

# Matrix / Element

> **TAS Score: S3/3 — D4/5** — A3 / T2
> D4 not D5: Element (the company) is moving toward enterprise features with ESS Pro — some advanced features gated behind paid tiers (Q8). Core protocol and Synapse remain fully open.

## Brief Description

Matrix is an open standard for decentralized, end-to-end encrypted communication. Synapse is the reference homeserver (Python). Element is the primary client (web, iOS, Android). Supports federation — your server talks to any other Matrix server. E2EE enabled by default in private chats.

## Architectural Role

Communication layer: messaging, voice/video calls, file sharing, bridges to other platforms (Slack, Telegram, WhatsApp, Signal). Federated — no single point of control.

## Technical Autonomy

- [x] Works without internet — functions on local network; federation requires internet
- [x] Stores data locally — all messages and media on your server
- [x] Does not require external accounts — register on your own server
- [x] Allows data export — messages stored in PostgreSQL; standard database export; IMAP-like portability via federation
- [x] Provides offline updates — Docker image or package manager, updated manually

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅     | Stop Synapse. Messages queued by federated servers. Resume without loss. |
| Exit                  | ✅     | Your server, your data. PostgreSQL export. Domain-based identity (@user:yourdomain.com) — change server, keep identity via DNS. |
| Recoverability        | ✅     | PostgreSQL backup + media storage. Standard restore. Federation means room history exists on other servers too. |
| Visibility            | ✅     | Open standard (Matrix spec). Synapse: Apache-2.0. Element clients: AGPL-3.0. Full source available. |
| External Dependencies | ✅     | Requires PostgreSQL (selfhosted). Optional: coturn for VoIP NAT traversal. No mandatory external services. |

**Rating key:** ✅ fully meets · ⚠️ partially meets or requires configuration · ❌ does not meet

## Configuration (Minimal)

```yaml
services:
  synapse:
    image: matrixdotorg/synapse:latest
    volumes:
      - ./synapse:/data
    environment:
      - SYNAPSE_SERVER_NAME=matrix.example.com
      - SYNAPSE_REPORT_STATS=no
    ports:
      - 8008:8008
      - 8448:8448
    depends_on:
      - postgres

  postgres:
    image: postgres:15
    environment:
      - POSTGRES_DB=synapse
      - POSTGRES_USER=synapse
      - POSTGRES_PASSWORD=secret
    volumes:
      - ./pgdata:/var/lib/postgresql/data
```

Generate config first: `docker run --rm -v ./synapse:/data -e SYNAPSE_SERVER_NAME=matrix.example.com matrixdotorg/synapse:latest generate`. Requires reverse proxy for TLS. ~350 MB RAM for single-user server.

## Related Recipes

- [Privacy-First Homelab](../recipes/privacy-first-homelab.html)

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Slack](slack.html) | A0 / T0 | Polished team UX, fully proprietary, no federation |
| [Telegram](telegram.html) | A1 / T0 | Open client, proprietary server, centralized, phone-number required |
| Signal | A1 / T2 | E2EE, open source, but centralized and phone-number required |

---

## Trajectory

**Direction: opening (with caveats)**

Matrix protocol is an open standard governed by the Matrix.org Foundation. Synapse development is led by Element (the company). Element is introducing enterprise products (ESS Pro) with features behind paid tiers. However, the core protocol, Synapse server, and Element clients remain open source. Alternative homeservers exist (Conduit, Dendrite). The open standard means no single entity controls the ecosystem.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | Synapse: Apache-2.0. Element: AGPL-3.0. Protocol: open standard. |
| Feature gating | ⚠️ | ESS Pro has enterprise features. Core Synapse and Element remain fully featured and free. |
| Self-hosting | ✅ | Self-hosting is a core design principle of the protocol. Getting easier with each release. |
| Governance | ✅ | Matrix.org Foundation governs the protocol. Element governs Synapse development. Multiple independent implementations exist. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** https://matrix.org
- **Documentation:** https://element-hq.github.io/synapse/latest/
- **Repository:** https://github.com/element-hq/synapse
- **Docker image:** matrixdotorg/synapse
- **Community:** https://matrix.to/#/#synapse:matrix.org
