---
title: "Mistral"
parent: "Technology Catalog"
category: "compute/inference"
status: "stable"
license: "Apache-2.0"
source: "https://huggingface.co/mistralai"
repository: "https://github.com/mistralai/mistral-inference"
documentation: "https://docs.mistral.ai"
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

# Mistral

> **TAS Score: S3/3 — D4/5** — A3 / T2
> _(D4 not D5: the hosted La Plateforme API collects usage data and requires an account. The self-hosted open-weight variant scored here carries none of this.)_

**Family:** [Mistral (Apache open)](mistral.md) · [Mistral Medium (Modified MIT)](mistral-medium.md)
_This card scores the **Apache-2.0 open-weight models**. The Modified-MIT tier (Mistral Medium 3.5, Devstral 2) carries a non-OSI revenue clause and is a separate object — see the family link._

**⚠️ Two-mode tool.** Self-hosted open weights: A3/T2. Hosted La Plateforme API: A1/T1. This card scores the self-hosted open-weight variant.

## Brief Description

Open-weight model family from Mistral AI (Paris) under the Apache-2.0 license — Mistral 7B, Mixtral 8x7B/8x22B, Mistral Nemo, Pixtral 12B, Mathstral, Ministral 3, Mistral Small / Small 4, Magistral Small, Devstral Small, and the flagship Mistral Large 3 (41B active / 675B total MoE, released Apache in December 2025). All fully downloadable and self-hostable; sizes span a laptop-friendly 7B up to a multi-GPU 675B MoE, with EU data-residency positioning.

Scope note: a few Mistral models sit under more restrictive licenses — Modified MIT (Medium 3.5, Devstral 2), the Mistral Research License (Ministral 8B, Mistral Large 2, Pixtral Large), and the non-production MNPL (classic Codestral). Those are not Apache; the Modified-MIT tier is scored on the family card, and MRL/MNPL models are noted there.

## Architectural Role

Compute/inference layer: general-purpose open-weight LLMs run on your own hardware, with an OpenAI-compatible API for drop-in self-hosting. Local alternative to cloud chat, coding, and reasoning APIs across the full size range.

## Technical Autonomy

- [x] Works without internet (after model download)
- [x] Stores data locally
- [x] Does not require external accounts (self-hosted)
- [x] Allows data export — Apache-2.0, standard HuggingFace format
- [ ] Hosted La Plateforme API requires an account and sends data to Mistral servers

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
| --- | --- | --- |
| Pause | ✅ | Stop inference. Model weights stay on disk. |
| Exit | ✅ | Standard model format. Apache-2.0 — no restrictions on use or redistribution. |
| Recoverability | ✅ | Re-download from HuggingFace or restore from backup. |
| Visibility | ✅ | Apache-2.0 across the core lineup. Open weights. Training data not published. |
| External Dependencies | ⚠️ | Self-hosted: none. Hosted API: Mistral infrastructure (EU-based). |

## Configuration (Minimal)

```bash
# Consumer hardware — via Ollama
ollama run mistral-nemo      # 12B, Apache-2.0
ollama run mixtral           # 8x7B MoE, Apache-2.0

# Server — via vLLM (Apache-licensed checkpoint)
vllm serve mistralai/Mixtral-8x22B-Instruct-v0.1 --tensor-parallel-size 4
```

## Alternatives

| Alternative | Autonomy | Notes |
| --- | --- | --- |
| [Qwen3](qwen3.md) | A3 / T2 | Apache-2.0 open-weight family. |
| [DeepSeek-R1](deepseek-r1.md) | A3 / T2 | Open-weight reasoning, MIT. |
| [Mistral Medium](mistral-medium.md) | A3 / T1 | Same lab — Modified-MIT revenue-clause tier. |

---

## Trajectory

**Direction: opening**

Mistral is the clearest permissive-open bet among major labs — Large 3, Small 4, Ministral, Mixtral, and Nemo all ship under Apache-2.0, with EU data residency. The caveats are a Modified-MIT tier (Medium 3.5, Devstral 2) with a revenue clause and a few research / non-production licenses; the core lineup stays Apache.

**Signal assessment:**

| Signal | Status | Evidence |
| --- | --- | --- |
| License | ✅ | Core lineup Apache-2.0; Mistral Large 3 released Apache (Dec 2025). |
| Feature gating | ➖ | Some flagship / coding models under restrictive licenses, but the Apache core is broad. |
| Self-hosting | ✅ | Standard formats. Ollama, vLLM, SGLang, llama.cpp; OpenAI-compatible API. |
| Governance | ✅ | Independent EU company. Active, frequent open releases. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [mistral.ai](https://mistral.ai)
- **Repository:** [github.com/mistralai/mistral-inference](https://github.com/mistralai/mistral-inference)
- **Models:** [huggingface.co/mistralai](https://huggingface.co/mistralai)
