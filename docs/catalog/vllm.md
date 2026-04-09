---
title: "vLLM"
parent: "Technology Catalog"
category: "compute/inference"
status: "stable"
license: "Apache-2.0"
source: "https://github.com/vllm-project/vllm"
repository: "https://github.com/vllm-project/vllm"
documentation: "https://docs.vllm.ai"
docker_image: "vllm/vllm-openai"
community: "https://github.com/vllm-project/vllm/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: ["docker"]
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
nav_order: 99
---

# vLLM

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Production-grade GPU inference engine for large language models. Uses PagedAttention for high-throughput serving. OpenAI-compatible API. Designed for multi-user deployments where Ollama is too simple and llama.cpp too low-level.

## Architectural Role

Compute/inference layer: production serving engine for LLMs. Sits between llama.cpp (low-level) and Ollama (consumer-friendly). Primary choice for self-hosted teams serving models to multiple users. Replaces hosted inference APIs from OpenAI, Anthropic, Together.AI.

## Technical Autonomy

- [x] Works without internet (after model download)
- [x] Stores data locally
- [x] Does not require external accounts
- [x] Allows data export — standard HuggingFace model format
- [x] Full source on GitHub

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
| --- | --- | --- |
| Pause | ✅ | Stop the server. Models stay on disk. |
| Exit | ✅ | Standard HuggingFace models. Use with any compatible runtime. |
| Recoverability | ✅ | Reinstall, reload models. Stateless serving. |
| Visibility | ✅ | Apache-2.0. Full source on GitHub. |
| External Dependencies | ✅ | Requires NVIDIA GPU. No cloud dependencies. |

## Configuration (Minimal)

```bash
pip install vllm
vllm serve meta-llama/Llama-3.1-8B-Instruct --port 8000
```

Or with Docker:

```yaml
services:
  vllm:
    image: vllm/vllm-openai
    ports:
      - "8000:8000"
    volumes:
      - ./models:/root/.cache/huggingface
    deploy:
      resources:
        reservations:
          devices:
            - capabilities: [gpu]
    command: ["--model", "meta-llama/Llama-3.1-8B-Instruct"]
```

## Alternatives

| Alternative | Autonomy | Notes |
| --- | --- | --- |
| [Ollama](ollama.md) | A3 / T2 | Simpler. Better for single-user. No GPU required. |
| [llama.cpp](llama-cpp.md) | A3 / T2 | Lower-level. CPU-friendly. More control. |
| Together.AI | A0 / T0 | Hosted inference. Pay per token. |

---

## Trajectory

**Direction: opening**

Apache-2.0 licensed. Started at UC Berkeley, now backed by venture funding (vLLM Inc). Rapidly growing community. De facto standard for production self-hosted LLM serving.

**Signal assessment:**

| Signal | Status | Evidence |
| --- | --- | --- |
| License | ✅ | Apache-2.0. No changes. |
| Feature gating | ✅ | No paid tier. |
| Self-hosting | ✅ | Docker and pip install. Active documentation. |
| Governance | ⚠️ | Corporate-backed (vLLM Inc). Open source but venture-funded. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [docs.vllm.ai](https://docs.vllm.ai)
- **Repository:** [github.com/vllm-project/vllm](https://github.com/vllm-project/vllm)
- **Docker image:** `vllm/vllm-openai`
