---
title: "Llama"
parent: "Technology Catalog"
category: "compute/inference"
status: "stable"
license: "Llama Community License"
source: "https://huggingface.co/meta-llama"
repository: "https://github.com/meta-llama/llama-models"
documentation: "https://www.llama.com/docs"
docker_image: "-"
community: "-"
autonomy_level: "A3"
transparency_level: "T1"
depends_on: []
optional_deps: ["ollama", "vllm", "llama-cpp", "sglang"]
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
nav_order: 99
---

# Llama

> **TAS Score: S3/3 — D4/5** — A3 / T1
> _(T1 not T2: the Llama Community License is not OSI-approved — it adds a 700M-MAU commercial threshold, a competitor restriction, a ban on using Llama to train other models, and (since 3.2) an EU multimodal exclusion. Weights are downloadable and self-hostable, so autonomy stays A3; license transparency is capped at T1.)_
> _(D4 not D5: Meta grants the >700M-MAU license at its "sole discretion," and the Acceptable Use Policy is incorporated by reference — a standing conditionality on continued use at scale.)_

**Note:** Meta publishes open weights (Llama 3.x / 4) but has signalled a pivot toward closed models ("Muse Spark"). This card covers the open-weight Llama family.

## Brief Description

Meta's open-weight model family — Llama 3.1 (8B/70B/405B), 3.2 (small on-device + multimodal), 3.3 (70B), and Llama 4 (Scout, Maverick — MoE, natively multimodal, released April 2025). Weights are downloadable from HuggingFace and self-hostable via Ollama, vLLM, llama.cpp, SGLang.

The catch is the license. Every Llama release ships under the **Llama Community License**, a bespoke commercial license the OSI has explicitly found fails the Open Source Definition: it caps free commercial use at 700M monthly active users, bans building competing models, prohibits using Llama or its outputs to train other models, and (from 3.2) excludes EU-domiciled parties from the multimodal models. Fully runnable offline, but not OSI-open — hence T1.

## Architectural Role

Compute/inference layer: one of the most widely deployed open-weight bases, with a large ecosystem of derivatives and fine-tunes. Local alternative to cloud chat / multimodal APIs across the full size range.

## Technical Autonomy

- [x] Works without internet (after model download)
- [x] Stores data locally
- [x] Does not require external accounts (self-hosted)
- [x] Allows data export — weights downloadable (Llama Community License; MAU / competitor / training restrictions apply)
- [ ] Commercial use conditional on Meta's terms; EU multimodal excluded

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
| --- | --- | --- |
| Pause | ✅ | Stop inference. Model weights stay on disk. |
| Exit | ✅ | Standard model format, downloadable. |
| Recoverability | ✅ | Re-download from HuggingFace or restore from backup. |
| Visibility | ⚠️ | Open weights, but non-OSI Community License (MAU cap, competitor & training bans, EU exclusion) → T1. Training data not published. |
| External Dependencies | ⚠️ | Self-hosted: none at runtime. License: conditional on Meta's terms at scale. |

## Configuration (Minimal)

```bash
# Consumer hardware via Ollama
ollama run llama3.3      # 70B
ollama run llama3.2      # small / multimodal

# Server — Llama 4 via vLLM
vllm serve meta-llama/Llama-4-Scout-17B-16E-Instruct --tensor-parallel-size 8
```

## Alternatives

| Alternative | Autonomy | Notes |
| --- | --- | --- |
| [Qwen3](qwen3.md) | A3 / T2 | Apache open weights — no MAU cap, no competitor ban. |
| [Gemma 4](gemma-4.md) | A3 / T2 | Apache — Google's OSI-clean open family. |
| [DeepSeek-R1-Distill-Llama](deepseek-r1-distill-llama.md) | A3 / T1 | Llama-based distill — inherits the same T1. |

---

## Trajectory

**Direction: closing**

Llama popularized open weights, but the license has tightened over time (the EU multimodal exclusion arrived in 3.2), and Meta has signalled a strategic pivot toward closed "Muse Spark" models, casting doubt on long-term open releases. The weights you already hold stay usable, but the direction of travel is toward more restriction, not less — the mirror image of Gemma.

**Signal assessment:**

| Signal | Status | Evidence |
| --- | --- | --- |
| License | ⚠️ | Llama Community License — non-OSI; MAU cap, competitor & training bans. |
| Feature gating | ⚠️ | EU-domiciled parties excluded from multimodal models (since 3.2). |
| Self-hosting | ✅ | Standard formats. Ollama, vLLM, llama.cpp, SGLang. |
| Governance | ⚠️ | Meta controls terms; reported pivot toward closed models. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [llama.com](https://www.llama.com)
- **Repository:** [github.com/meta-llama/llama-models](https://github.com/meta-llama/llama-models)
- **Models:** [huggingface.co/meta-llama](https://huggingface.co/meta-llama)
