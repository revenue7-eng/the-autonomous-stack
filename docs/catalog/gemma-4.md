---
title: "Gemma 4"
parent: "Technology Catalog"
category: "compute/inference"
status: "stable"
license: "Apache-2.0"
source: "https://huggingface.co/google"
repository: "-"
documentation: "https://ai.google.dev/gemma"
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

# Gemma 4

> **TAS Score: S3/3 — D4/5** — A3 / T2
> _(D4 not D5: the hosted option via Google AI Studio / Vertex AI collects usage data and requires a Google account. The self-hosted Apache-2.0 weights scored here carry none of this.)_

**Family:** [Gemma 2 / 3 (Gemma Terms)](gemma.md) · [Gemma 4 (Apache 2.0)](gemma-4.md)
_This card scores **Gemma 4** — the first Gemma under Apache-2.0. Gemma 3 and earlier remain under the custom Gemma Terms of Use (T1) — see the family link._

**⚠️ Two-mode tool.** Self-hosted open weights: A3/T2. Hosted via Google AI Studio / Vertex AI: A1/T1. This card scores the self-hosted open-weight variant.

## Brief Description

Google DeepMind's fourth-generation open-weight family, released April 2, 2026 — four sizes (2B, 4B, 26B MoE, 31B dense), built on the same research as Gemini 3, natively multimodal, ~256K context. The 2B/4B edge variants run on phones and single-board computers; the 31B dense model runs 4-bit on a 24 GB consumer GPU and ranks near the top of open-model leaderboards.

The landmark change is licensing: **Gemma 4 is the first Gemma under OSI-approved Apache 2.0**, dropping the custom Gemma Terms that constrained earlier versions. That single change moves the family from T1 to T2.

## Architectural Role

Compute/inference layer, full range from edge to workstation. Local alternative to cloud chat and multimodal APIs — now legally clean for commercial deployment.

## Technical Autonomy

- [x] Works without internet (after model download)
- [x] Stores data locally
- [x] Does not require external accounts (self-hosted)
- [x] Allows data export — Apache-2.0, standard HuggingFace format
- [ ] Hosted AI Studio / Vertex option requires a Google account and sends data to Google

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
| --- | --- | --- |
| Pause | ✅ | Stop inference. Model weights stay on disk. |
| Exit | ✅ | Standard model format. Apache-2.0 — no restrictions on use or redistribution. |
| Recoverability | ✅ | Re-download from HuggingFace / Kaggle or restore from backup. |
| Visibility | ✅ | Apache-2.0. Open weights. Training data not published. |
| External Dependencies | ⚠️ | Self-hosted: none. Hosted option: Google infrastructure. |

## Configuration (Minimal)

```bash
# Edge — 4B on device via Ollama
ollama run gemma4:4b

# Workstation — 31B dense, 4-bit on a 24GB GPU
ollama run gemma4:31b
```

## Alternatives

| Alternative | Autonomy | Notes |
| --- | --- | --- |
| [Gemma](gemma.md) (2 / 3) | A3 / T1 | Earlier versions — custom Gemma Terms of Use. |
| [Qwen3](qwen3.md) | A3 / T2 | Apache open weights. |
| [Mistral](mistral.md) | A3 / T2 | Apache open-weight family. |

---

## Trajectory

**Direction: opening**

Gemma 4 is one of the clearest *opening* moves in the catalog: a major lab taking an established restrictive-license family and relicensing its newest generation under OSI Apache 2.0. Google's own open-source blog frames it as the first Gemma with a truly open license. The remaining caveats are that training data stays unpublished and the hosted path (AI Studio / Vertex) is a separate, data-collecting mode.

**Signal assessment:**

| Signal | Status | Evidence |
| --- | --- | --- |
| License | ✅ | Apache-2.0 — first Gemma under an OSI-approved license. |
| Feature gating | ✅ | All four sizes released as weights, edge to 31B. |
| Self-hosting | ✅ | Standard formats. Ollama, vLLM, llama.cpp. |
| Governance | ➖ | Google-controlled project, but Apache removes the revisable-terms risk. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [deepmind.google/models/gemma](https://deepmind.google/models/gemma)
- **Documentation:** [ai.google.dev/gemma](https://ai.google.dev/gemma)
- **Models:** [huggingface.co/google](https://huggingface.co/google)
