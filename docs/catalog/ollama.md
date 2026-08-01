---
nav_exclude: false
title: "Ollama"
category: "compute/inference"
status: "stable"
license: "MIT"
source: "https://ollama.com"
repository: "https://github.com/ollama/ollama"
documentation: "https://github.com/ollama/ollama/blob/main/docs/README.md"
docker_image: "ollama/ollama"
community: "https://discord.gg/ollama"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: ["docker"]
depended_by: []
critical_criteria: ["Pause", "Exit"]
trajectory: "opening"
parent: Technology Catalog
nav_order: 99
---

# Ollama

> **TAS Score: S3/3 — D4/5** — A3 / T2
> D4 not D5: model downloads require internet and come from Ollama's registry — no built-in way to verify model integrity or provenance beyond SHA checksums (Q6). Once downloaded, models run fully offline.

## Brief Description

Local large language model runtime. Run Llama, Mistral, Gemma, Phi, and dozens of other open-weight models on your own hardware. Provides an OpenAI-compatible API server. Ollama is not a model — it is the engine that downloads, manages, and serves models locally. No cloud, no API keys, no data leaves your machine.

## Architectural Role

Compute/inference layer: runtime for local LLM inference. Like Docker is to containers, Ollama is to language models — it manages downloads, versioning, and serving. Replaces cloud LLM API dependencies (ChatGPT, Claude API, Gemini) for tasks where data privacy matters or internet is unavailable. Provides a REST API compatible with the OpenAI format.

## Technical Autonomy

- ✅ Works without internet (after model download)
- ✅ Stores all data locally (models + conversations)
- ✅ Does not require external accounts
- ✅ Models are downloadable files — portable to any machine
- ⚠️ Initial model download from ollama.com registry (one-time)

## The registry problem

The Ollama runtime is autonomous. Its default model registry is not. Same distinction as Docker:

| Component | Autonomy | Transparency | Notes |
|-----------|----------|-------------|-------|
| Ollama runtime | A3 | T2 | Open source (MIT), runs anywhere, fully offline after download |
| Ollama CLI / API | A3 | T2 | Open source, OpenAI-compatible local server |
| ollama.com registry | A0 | T0 | Centralized default registry, proprietary. Provenance not verifiable beyond SHA checksums |
| Models (GGUF) | A3 | T2 | Standard GGUF files. Portable to llama.cpp or any compatible runtime |

When you run `ollama pull`, the runtime is A3 but the default model source is A0. Same as Docker: the dependency didn't disappear — it moved.

**Mitigation:** Import from HuggingFace, build from a local GGUF with `ollama create`, or point Ollama at a self-hosted/mirror registry. Pull once, keep the file — this moves model distribution from A0 to A3.

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ✅ | Stop the process, models stay on disk. Resume instantly. |
| Exit                  | ✅ | Models are standard GGUF files. Copy and use with llama.cpp or any compatible runtime. |
| Recoverability        | ✅ | Reinstall Ollama, re-pull models (or copy from backup). No state to lose. |
| Visibility            | ✅ | MIT license. Full source code on GitHub. |
| External Dependencies | ⚠️ | Model registry is centralized (ollama.com). But models can be imported from HuggingFace or local files. |

## Configuration (Minimal)

```bash
# Install (no Docker needed)
curl -fsSL https://ollama.com/install.sh | sh

# Pull a model
ollama pull llama3.2

# Chat
ollama run llama3.2
```

Or with Docker:

```yaml
services:
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

- [Developer Workstation](../recipes/developer-workstation.md) — local AI coding assistant

## Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| llama.cpp | A3 / T2 | Lower-level C++ runtime. More control, less convenience. |
| LocalAI | A3 / T2 | OpenAI-compatible API server. Supports more model formats. |
| ChatGPT | A0 / T0 | Cloud-only, proprietary. All data sent to OpenAI. |

---

## Trajectory

**Direction: opening.**

Ollama is one of the fastest-growing open-source projects in the AI space. MIT licensed, single binary, rapidly expanding model support. The project makes local LLM inference accessible to non-ML-engineers.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | MIT. Maximally permissive. |
| Feature gating | ✅ | No paid tier. Everything is free and local. |
| Self-hosting | ✅ | Single binary install, Docker support, offline after first download. |
| Governance | ⚠️ | Backed by Ollama Inc. (venture-funded). Open source but corporate-led. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [ollama.com](https://ollama.com)
- **Repository:** [github.com/ollama/ollama](https://github.com/ollama/ollama)
- **Docker image:** `ollama/ollama`
