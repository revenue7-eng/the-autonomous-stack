---
title: "llama.cpp"
parent: "Technology Catalog"
category: "compute/inference"
status: "stable"
license: "MIT"
source: "https://github.com/ggerganov/llama.cpp"
repository: "https://github.com/ggerganov/llama.cpp"
documentation: "https://github.com/ggerganov/llama.cpp/blob/master/README.md"
docker_image: "-"
community: "https://github.com/ggerganov/llama.cpp/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: ["docker"]
depended_by: ["ollama"]
critical_criteria: ["Exit", "Recoverability"]
nav_order: 99
---

# llama.cpp

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

C/C++ inference engine for large language models. The foundational project that made local LLM inference practical on consumer hardware — CPU, Apple Silicon, NVIDIA, AMD, and Intel GPUs. No cloud, no API keys, no external dependencies.

## Architectural Role

Compute/inference layer: the lowest-level runtime for local LLM inference. Ollama, LM Studio, GPT4All, and most local AI tools are built on top of llama.cpp. Introduced the GGUF format — now the industry standard for local model distribution.

## Technical Autonomy

- [x] Works without internet (after model download)
- [x] Stores data locally
- [x] Does not require external accounts
- [x] Allows data export — models are standard GGUF files
- [x] Compiles from source with no external dependencies

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
| --- | --- | --- |
| Pause | ✅ | Stop the process. Models stay on disk. |
| Exit | ✅ | GGUF files are portable. Use with any compatible runtime. |
| Recoverability | ✅ | Recompile from source, reload models. Nothing to lose. |
| Visibility | ✅ | MIT license. Full source on GitHub. |
| External Dependencies | ✅ | None. Compiles standalone. Models downloadable from HuggingFace. |

## Configuration (Minimal)

```bash
# Build from source
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp && cmake -B build && cmake --build build --config Release

# Run a model
./build/bin/llama-cli -m model.gguf -p "Hello, world"

# Start an OpenAI-compatible server
./build/bin/llama-server -m model.gguf --port 8080
```

## Related Recipes

- [Developer Workstation](../recipes/developer-workstation.md) — local AI coding assistant

## Alternatives

| Alternative | Autonomy | Notes |
| --- | --- | --- |
| [Ollama](ollama.md) | A3 / T2 | Higher-level wrapper. Easier to use, less control. |
| [vLLM](vllm.md) | A3 / T2 | GPU-focused production serving. Better throughput, requires NVIDIA. |
| ChatGPT | A0 / T0 | Cloud-only. All data sent to OpenAI servers. |

---

## Trajectory

**Direction: opening**

The most active open-source LLM infrastructure project. Created by Georgi Gerganov, MIT licensed, massive contributor community. GGUF format became the de facto standard. Continuously expanding hardware support.

**Signal assessment:**

| Signal | Status | Evidence |
| --- | --- | --- |
| License | ✅ | MIT. Maximally permissive. No changes. |
| Feature gating | ✅ | No paid tier. Everything is free and open. |
| Self-hosting | ✅ | Single compilation, no Docker needed. Runs on Raspberry Pi to datacenter GPUs. |
| Governance | ✅ | Hundreds of contributors. Healthy community governance. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [github.com/ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp)
- **Repository:** [github.com/ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp)
