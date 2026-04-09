---
title: "LocalAI"
parent: "Technology Catalog"
category: "compute/inference"
status: "stable"
license: "MIT"
source: "https://github.com/mudler/LocalAI"
repository: "https://github.com/mudler/LocalAI"
documentation: "https://localai.io/docs"
docker_image: "localai/localai"
community: "https://github.com/mudler/LocalAI/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: ["docker"]
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
nav_order: 99
---

# LocalAI

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Drop-in replacement for the OpenAI API. Supports text generation, image generation, audio transcription, text-to-speech, and embeddings — all locally. Single binary or Docker container. No GPU required (but supported).

## Architectural Role

Compute/inference layer: multi-modal local inference server. Unlike Ollama (text-only focus), LocalAI covers text, images, audio, and embeddings in one API. Replaces multiple OpenAI API endpoints simultaneously.

## Technical Autonomy

- [x] Works without internet (after model download)
- [x] Stores data locally
- [x] Does not require external accounts
- [x] Allows data export — standard model formats
- [x] Single binary or Docker deployment

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
| --- | --- | --- |
| Pause | ✅ | Stop the process. Models stay on disk. |
| Exit | ✅ | Standard model files. Portable. |
| Recoverability | ✅ | Reinstall, reload models. |
| Visibility | ✅ | MIT license. Full source on GitHub. |
| External Dependencies | ✅ | None. Runs on CPU or GPU. |

## Configuration (Minimal)

```yaml
services:
  localai:
    image: localai/localai:latest-cpu
    ports:
      - "8080:8080"
    volumes:
      - ./models:/models
    restart: unless-stopped
```

## Alternatives

| Alternative | Autonomy | Notes |
| --- | --- | --- |
| [Ollama](ollama.md) | A3 / T2 | Simpler for text-only. Better UX. |
| [vLLM](vllm.md) | A3 / T2 | Higher throughput for text. GPU required. |
| OpenAI API | A0 / T0 | Cloud-only. Proprietary. |

---

## Trajectory

**Direction: opening**

MIT licensed, active community. Growing multi-modal support. No commercial entity — community-driven project by Ettore Di Giacinto.

**Signal assessment:**

| Signal | Status | Evidence |
| --- | --- | --- |
| License | ✅ | MIT. No changes. |
| Feature gating | ✅ | No paid tier. |
| Self-hosting | ✅ | Docker, binary, pip. Multiple deployment options. |
| Governance | ✅ | Community-driven. Active contributors. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [localai.io](https://localai.io)
- **Repository:** [github.com/mudler/LocalAI](https://github.com/mudler/LocalAI)
- **Docker image:** `localai/localai`
