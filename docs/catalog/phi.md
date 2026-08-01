---
title: "Phi"
parent: "Technology Catalog"
category: "compute/inference"
status: "stable"
license: "MIT"
source: "https://huggingface.co/microsoft"
repository: "-"
documentation: "https://huggingface.co/microsoft/phi-4"
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

# Phi

> **TAS Score: S3/3 — D4/5** — A3 / T2
> _(D4 not D5: a hosted option exists via Azure AI Foundry (account + per-token pricing). The self-hosted MIT weights scored here carry none of this.)_

## Brief Description

Microsoft Research's small-but-capable open-weight family — Phi-4 (14B) and its variants (Phi-4-mini, Phi-4-multimodal, Phi-4-reasoning). The Phi-4 weights are published on HuggingFace under the **MIT license**: no usage restrictions, with commercial use, fine-tuning, and redistribution all permitted without royalty. Trained heavily on synthetic data, Phi-4 punches well above its size on math and reasoning and runs comfortably on consumer hardware via Ollama, llama.cpp, and vLLM. MIT is fully OSI-approved → a clean T2; the training data itself is not released.

Small opening arc worth noting: Phi-4 first shipped on Azure under a Microsoft Research License (Dec 2024), then the weights were released MIT on HuggingFace (Jan 2025).

## Architectural Role

Compute/inference layer: efficient small models for local reasoning and coding on modest hardware. Local alternative to cloud APIs wherever a 14B-class model suffices.

## Technical Autonomy

- [x] Works without internet (after model download)
- [x] Stores data locally
- [x] Does not require external accounts (self-hosted)
- [x] Allows data export — MIT, standard HuggingFace format
- [ ] Hosted Azure AI Foundry option requires an account and per-token billing

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
| --- | --- | --- |
| Pause | ✅ | Stop inference. Model weights stay on disk. |
| Exit | ✅ | Standard model format. MIT — no restrictions on use or redistribution. |
| Recoverability | ✅ | Re-download from HuggingFace or restore from backup. |
| Visibility | ✅ | MIT-licensed open weights. Training data not published (synthetic-heavy). |
| External Dependencies | ⚠️ | Self-hosted: none. Hosted option: Azure. |

## Configuration (Minimal)

```bash
# Local via Ollama
ollama run phi4

# Server via vLLM
vllm serve microsoft/phi-4
```

## Alternatives

| Alternative | Autonomy | Notes |
| --- | --- | --- |
| [Qwen3](qwen3.md) | A3 / T2 | Apache open weights, broader size range. |
| [Gemma 4](gemma-4.md) | A3 / T2 | Apache — comparable small / edge sizes. |
| [Mistral](mistral.md) | A3 / T2 | Apache open-weight family. |

---

## Trajectory

**Direction: opening**

Microsoft moved Phi-4 from an Azure-only research license to fully MIT-released weights within weeks of launch — a clear opening step, and one of the most permissive licenses in the catalog. Continued MIT releases across the Phi-4 variants reinforce the direction.

**Signal assessment:**

| Signal | Status | Evidence |
| --- | --- | --- |
| License | ✅ | MIT — OSI-approved, no usage restrictions. |
| Feature gating | ✅ | Full weights released; variants (mini, multimodal, reasoning) also open. |
| Self-hosting | ✅ | Standard formats. Ollama, vLLM, llama.cpp, TGI. |
| Governance | ➖ | Microsoft-controlled project, but MIT removes license risk. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Documentation:** [huggingface.co/microsoft/phi-4](https://huggingface.co/microsoft/phi-4)
- **Models:** [huggingface.co/microsoft](https://huggingface.co/microsoft)
