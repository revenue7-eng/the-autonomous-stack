---
title: "Open WebUI"
parent: "Technology Catalog"
category: "compute/inference"
status: "stable"
license: "BSD-3-Clause"
source: "https://github.com/open-webui/open-webui"
repository: "https://github.com/open-webui/open-webui"
documentation: "https://docs.openwebui.com"
docker_image: "ghcr.io/open-webui/open-webui"
community: "https://discord.gg/open-webui"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker", "ollama"]
optional_deps: ["postgresql"]
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
nav_order: 99
---

# Open WebUI

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Self-hosted web interface for local LLMs. Connects to Ollama or any OpenAI-compatible API. Provides a ChatGPT-like experience — conversations, RAG, web search, multi-user support, file uploads — entirely on your own infrastructure.

## Architectural Role

Applications layer: the user-facing frontend for local AI inference. Pairs with Ollama (inference engine) the same way a web browser pairs with a web server. Replaces ChatGPT, Claude, and other hosted AI chat interfaces.

## Technical Autonomy

- [x] Works without internet (when connected to local Ollama)
- [x] Stores all data locally (SQLite or PostgreSQL)
- [x] Does not require external accounts
- [x] Allows data export — conversations exportable as JSON
- [x] Docker-based deployment, fully self-contained

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
| --- | --- | --- |
| Pause | ✅ | Stop the container. Data persists in volumes. |
| Exit | ✅ | Export conversations. Switch to any other Ollama-compatible frontend. |
| Recoverability | ✅ | Redeploy container, restore volume. Standard Docker backup. |
| Visibility | ✅ | BSD-3-Clause. Full source on GitHub. |
| External Dependencies | ✅ | None required. Optional web search and RAG features work locally. |

## Configuration (Minimal)

```yaml
services:
  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    container_name: open-webui
    ports:
      - "3000:8080"
    volumes:
      - ./data/open-webui:/app/backend/data
    environment:
      - OLLAMA_BASE_URL=http://ollama:11434
    restart: unless-stopped
    depends_on:
      - ollama

  ollama:
    image: ollama/ollama
    container_name: ollama
    ports:
      - "11434:11434"
    volumes:
      - ./data/ollama:/root/.ollama
    restart: unless-stopped
```

## Related Recipes

- [Developer Workstation](../recipes/developer-workstation.md)

## Alternatives

| Alternative | Autonomy | Notes |
| --- | --- | --- |
| [LM Studio](lm-studio.md) | A3 / T1 | Desktop app. Easier setup, closed source. |
| ChatGPT | A0 / T0 | Cloud-only. All data on OpenAI servers. |
| [Jan](jan.md) | A3 / T2 | Desktop app. Open source, offline-first. |

---

## Trajectory

**Direction: opening**

One of the fastest-growing self-hosted AI projects. Active development, responsive maintainers, growing plugin ecosystem. BSD-3-Clause licensed. No paid tier — everything is free.

**Signal assessment:**

| Signal | Status | Evidence |
| --- | --- | --- |
| License | ✅ | BSD-3-Clause. Permissive, no changes. |
| Feature gating | ✅ | No paid tier. All features free. |
| Self-hosting | ✅ | Single Docker image. Improving documentation continuously. |
| Governance | ✅ | Active community. Hundreds of contributors. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [openwebui.com](https://openwebui.com)
- **Documentation:** [docs.openwebui.com](https://docs.openwebui.com)
- **Repository:** [github.com/open-webui/open-webui](https://github.com/open-webui/open-webui)
- **Docker image:** `ghcr.io/open-webui/open-webui`
