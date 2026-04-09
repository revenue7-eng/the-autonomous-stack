---
title: "Jan"
parent: "Technology Catalog"
category: "compute/inference"
status: "stable"
license: "AGPL-3.0"
source: "https://github.com/janhq/jan"
repository: "https://github.com/janhq/jan"
documentation: "https://jan.ai/docs"
docker_image: "-"
community: "https://discord.gg/jan"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
nav_order: 99
---

# Jan

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Open-source desktop AI assistant. Runs models locally, offline-first. Chat interface with conversation history, model management, and OpenAI-compatible local API. Available on macOS, Windows, Linux.

## Architectural Role

Applications layer: desktop client for local inference. Open-source alternative to LM Studio. Uses llama.cpp/ONNX internally. Replaces ChatGPT desktop.

## Technical Autonomy

- [x] Works without internet (after model download)
- [x] Stores data locally — conversations and models on disk
- [x] Does not require external accounts
- [x] Allows data export — standard model and chat formats
- [x] AGPL-3.0 — fully auditable

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
| --- | --- | --- |
| Pause | ✅ | Close the app. Everything persists locally. |
| Exit | ✅ | Models are standard GGUF. Conversations exportable. |
| Recoverability | ✅ | Reinstall, data remains in local directory. |
| Visibility | ✅ | AGPL-3.0. Full source on GitHub. |
| External Dependencies | ✅ | None required. Optional cloud model providers. |

## Configuration (Minimal)

```
1. Download from jan.ai
2. Open → Models → download a model
3. Chat
```

## Alternatives

| Alternative | Autonomy | Notes |
| --- | --- | --- |
| [LM Studio](lm-studio.md) | A3 / T1 | More polished UI. Closed source. |
| [Ollama](ollama.md) + [Open WebUI](open-webui.md) | A3 / T2 | Web-based. More setup. Multi-user. |
| [GPT4All](gpt4all.md) | A3 / T2 | Simpler. Document Q&A focus. |

---

## Trajectory

**Direction: opening**

AGPL-3.0 licensed. Active development by Homebrew Computer Company. Growing community. No paid tier. Edge computing focus.

**Signal assessment:**

| Signal | Status | Evidence |
| --- | --- | --- |
| License | ✅ | AGPL-3.0. Strong copyleft. |
| Feature gating | ✅ | No paid tier. |
| Self-hosting | ✅ | Desktop app, fully offline. |
| Governance | ⚠️ | Corporate-backed (Homebrew Computer Company). Open source. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [jan.ai](https://jan.ai)
- **Repository:** [github.com/janhq/jan](https://github.com/janhq/jan)
