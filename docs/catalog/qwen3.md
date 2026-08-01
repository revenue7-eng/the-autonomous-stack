---
title: "Qwen3"
parent: "Technology Catalog"
category: "compute/inference"
status: "stable"
license: "Apache-2.0"
source: "https://huggingface.co/Qwen"
repository: "https://github.com/QwenLM/Qwen3"
documentation: "https://github.com/QwenLM/Qwen3"
docker_image: "-"
community: "-"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: ["ollama", "vllm", "llama-cpp", "sglang"]
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
nav_order: 99
---

# Qwen3

> **TAS Score: S3/3 — D4/5** — A3 / T2
> _(D4 not D5: the hosted DashScope API collects usage data and requires an account, and Alibaba is subject to the Chinese regulatory environment. The self-hosted open-weight variant scored here carries none of this.)_

**⚠️ Two-mode tool.** Self-hosted open weights: A3/T2. Hosted DashScope API (Alibaba Cloud Model Studio): A1/T1. This card scores the self-hosted open-weight variant.

## Brief Description

Open-weight model family from Alibaba's Qwen team — dense models from 0.6B to 32B plus Mixture-of-Experts models (30B-A3B and 235B-A22B). Every open-weight size ships under the Apache-2.0 license, so both use and redistribution are uncontested. Switches between a "thinking" mode for reasoning and a "non-thinking" mode for general chat; strong at reasoning, coding, and multilingual tasks (100+ languages).

Small sizes run on consumer hardware; the 235B MoE needs a multi-GPU host. Training data is not published — as with nearly every open-weight model — but the **license on the weights** is fully OSI-approved. The transparency limit here is the training corpus, not usage rights.

## Architectural Role

Compute/inference layer: general-purpose open-weight LLM run on your own hardware. Local alternative to cloud chat and reasoning APIs across the full size range — a 0.6B model on a laptop up to a 235B MoE on a GPU server.

## Technical Autonomy

- [x] Works without internet (after model download)
- [x] Stores data locally
- [x] Does not require external accounts (self-hosted)
- [x] Allows data export — Apache-2.0, standard HuggingFace format
- [ ] Hosted DashScope API requires an account and sends data to Alibaba servers

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
| --- | --- | --- |
| Pause | ✅ | Stop inference. Model weights stay on disk. |
| Exit | ✅ | Standard model format. Apache-2.0 — no restrictions on use or redistribution. |
| Recoverability | ✅ | Re-download from HuggingFace / ModelScope or restore from backup. |
| Visibility | ✅ | Apache-2.0 across all open sizes. Open weights. Training data not published. |
| External Dependencies | ⚠️ | Self-hosted: none. Hosted API: Alibaba infrastructure (China-based). |

## Configuration (Minimal)

```bash
# Consumer hardware — dense model via Ollama
ollama run qwen3

# Server — 235B MoE via vLLM
vllm serve Qwen/Qwen3-235B-A22B --tensor-parallel-size 8

# Or via SGLang
python -m sglang.launch_server --model Qwen/Qwen3-32B
```

_The full range is Apache-2.0, so the same license applies whether you run the 0.6B model or the 235B MoE — only the hardware requirement changes._

## Alternatives

| Alternative | Autonomy | Notes |
| --- | --- | --- |
| [DeepSeek-R1-Distill-Qwen](deepseek-r1-distill-qwen.md) | A3 / T2 | Reasoning distill built on a Qwen base. Apache. |
| [MiroThinker](mirothinker.md) | A3 / T2 | Verification-centric reasoning. Apache-2.0. |
| Qwen-Max | A0 / T0 | API-only flagship. Proprietary, no weights. |

---

## Trajectory

**Direction: mixed**

Alibaba runs one of the most aggressive open-weight strategies of any major lab — every core Qwen3 size, including the 235B flagship MoE, is Apache-2.0. But Qwen is a corporate project from a Chinese company subject to its regulatory environment, and the top-tier Qwen-Max line is kept API-only and closed.

**Signal assessment:**

| Signal | Status | Evidence |
| --- | --- | --- |
| License | ✅ | Apache-2.0 across all open-weight sizes (0.6B–235B). |
| Feature gating | ⚠️ | Flagship Qwen-Max is API-only — not released as weights. |
| Self-hosting | ✅ | Standard formats. Ollama, vLLM, SGLang, llama.cpp compatible. |
| Governance | ⚠️ | Corporate (Alibaba). Chinese regulatory environment. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [qwen.ai](https://qwen.ai)
- **Repository:** [github.com/QwenLM/Qwen3](https://github.com/QwenLM/Qwen3)
- **Models:** [huggingface.co/Qwen](https://huggingface.co/Qwen)
