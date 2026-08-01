---
title: "gpt-oss"
parent: "Technology Catalog"
category: "compute/inference"
status: "stable"
license: "Apache-2.0"
source: "https://huggingface.co/openai"
repository: "https://github.com/openai/gpt-oss"
documentation: "https://github.com/openai/gpt-oss"
docker_image: "-"
community: "-"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: ["ollama", "vllm", "llama-cpp"]
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
nav_order: 99
---

# gpt-oss

> **TAS Score: S3/3 — D4/5** — A3 / T2
> _(D4 not D5: OpenAI attaches a short "gpt-oss usage policy" alongside the Apache-2.0 license — a minor overlay on otherwise OSI-clean weights. The license governing the weights is Apache-2.0, so transparency stays T2.)_

**Note:** gpt-oss is OpenAI's open-weight family (Apache-2.0), a separate object from OpenAI's proprietary hosted models — see [ChatGPT](chatgpt.md) (A0/T0) for the same company's closed offering.

## Brief Description

OpenAI's open-weight models — gpt-oss-120b and gpt-oss-20b, released August 2025 under Apache 2.0, the company's first open-weight release since GPT-2. The 20b runs on a single high-end consumer GPU; the 120b needs a data-center card (~80 GB) or multi-GPU. Both are reasoning-oriented (configurable effort) and tool-use capable, self-hostable via Ollama, vLLM, and llama.cpp.

OpenAI attaches a brief "gpt-oss usage policy" alongside the license, but the license governing the weights themselves is OSI-approved Apache 2.0 — a clean T2. Training data, as usual, is not published. The pairing is the point: the same company that keeps GPT / ChatGPT fully closed (A0/T0) also ships gpt-oss fully open (A3/T2).

## Architectural Role

Compute/inference layer: reasoning-capable open-weight models run on your own hardware. Local alternative to OpenAI's hosted API for many tasks.

## Technical Autonomy

- [x] Works without internet (after model download)
- [x] Stores data locally
- [x] Does not require external accounts (self-hosted)
- [x] Allows data export — Apache-2.0, standard HuggingFace format
- [ ] OpenAI's hosted GPT models are a separate paid API (not this card)

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
| --- | --- | --- |
| Pause | ✅ | Stop inference. Model weights stay on disk. |
| Exit | ✅ | Standard model format. Apache-2.0 — no restrictions on use or redistribution. |
| Recoverability | ✅ | Re-download from HuggingFace or restore from backup. |
| Visibility | ✅ | Apache-2.0 open weights. Brief usage-policy overlay. Training data not published. |
| External Dependencies | ✅ | Self-hosted: none. No first-party hosted dependency. |

## Configuration (Minimal)

```bash
# Consumer GPU — 20b via Ollama
ollama run gpt-oss:20b

# Data-center GPU — 120b via vLLM
vllm serve openai/gpt-oss-120b --tensor-parallel-size 2
```

## Alternatives

| Alternative | Autonomy | Notes |
| --- | --- | --- |
| [Qwen3](qwen3.md) | A3 / T2 | Apache open weights. |
| [DeepSeek-R1](deepseek-r1.md) | A3 / T2 | Open-weight reasoning, MIT. |
| [ChatGPT](chatgpt.md) | A0 / T0 | Same company — closed hosted models. |

---

## Trajectory

**Direction: opening**

gpt-oss is OpenAI's first open-weight release in years, under a clean Apache license — a notable opening from a company otherwise defined by closed APIs. Whether it becomes a sustained line or a one-off is the signal to watch; for now the released weights are permanently yours.

**Signal assessment:**

| Signal | Status | Evidence |
| --- | --- | --- |
| License | ✅ | Apache-2.0 on the weights (with a brief usage-policy overlay). |
| Feature gating | ➖ | Two sizes released; frontier hosted models remain separate and closed. |
| Self-hosting | ✅ | Standard formats. Ollama, vLLM, llama.cpp. |
| Governance | ➖ | OpenAI-controlled; open-weight commitment newly established, not yet proven durable. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Repository:** [github.com/openai/gpt-oss](https://github.com/openai/gpt-oss)
- **Models:** [huggingface.co/openai](https://huggingface.co/openai)
