---
title: "Gemma"
parent: "Technology Catalog"
category: "compute/inference"
status: "stable"
license: "Gemma Terms of Use"
source: "https://huggingface.co/google"
repository: "-"
documentation: "https://ai.google.dev/gemma"
docker_image: "-"
community: "-"
autonomy_level: "A3"
transparency_level: "T1"
depends_on: []
optional_deps: ["ollama", "vllm", "llama-cpp"]
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
nav_order: 99
---

# Gemma

> **TAS Score: S3/3 — D4/5** — A3 / T1
> _(T1 not T2: Gemma 2 and 3 ship under the custom "Gemma Terms of Use" — a source-available license with a prohibited-use policy that Google may revise and enforce remotely. Not OSI-approved. Weights are downloadable and self-hostable, so autonomy stays A3; license transparency is capped at T1.)_
> _(D4 not D5: the Gemma Terms are revisable by Google and include a remote-restriction clause — a standing diagnostic concern.)_

**Family:** [Gemma 2 / 3 (Gemma Terms)](gemma.md) · [Gemma 4 (Apache 2.0)](gemma-4.md)
_This card scores **Gemma 2 and 3**, under the custom Gemma Terms of Use. Gemma 4 moved to Apache-2.0 — a separate object, see the family link._

## Brief Description

Google DeepMind's open-weight model family, built on the same research as Gemini. Gemma 2 (June 2024) and Gemma 3 (March 2025) span roughly 2B to 27B parameters, run on consumer hardware, and are widely supported (Ollama, vLLM, llama.cpp). The weights are downloadable and self-hostable — but the license is the custom **Gemma Terms of Use**, a source-available license with a prohibited-use policy that Google can update and enforce remotely. That is not OSI-approved, which is why these versions land at T1 despite running fully offline.

Gemma 4 (April 2026) changed this — see the family card. Gemma 3 and everything earlier remain under the original terms.

## Architectural Role

Compute/inference layer: general-purpose open-weight LLM run on your own hardware. Local alternative to cloud chat APIs on modest hardware.

## Technical Autonomy

- [x] Works without internet (after model download)
- [x] Stores data locally
- [x] Does not require external accounts (self-hosted)
- [x] Allows data export — weights downloadable (Gemma Terms of Use; prohibited-use policy applies)
- [ ] Subject to Google's revisable usage policy

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
| --- | --- | --- |
| Pause | ✅ | Stop inference. Model weights stay on disk. |
| Exit | ✅ | Standard model format, downloadable. |
| Recoverability | ✅ | Re-download from HuggingFace / Kaggle or restore from backup. |
| Visibility | ⚠️ | Open weights, but custom Gemma Terms (non-OSI, revisable) → T1. Training data not published. |
| External Dependencies | ⚠️ | Self-hosted: none at runtime. License: Google's revisable terms. |

## Configuration (Minimal)

```bash
# Consumer hardware via Ollama
ollama run gemma2      # 9B / 27B, Gemma Terms of Use
ollama run gemma3      # multimodal, Gemma Terms of Use
```

## Alternatives

| Alternative | Autonomy | Notes |
| --- | --- | --- |
| [Gemma 4](gemma-4.md) | A3 / T2 | Same family — Apache-2.0, OSI-clean. |
| [Qwen3](qwen3.md) | A3 / T2 | Apache open weights, no custom terms. |
| [DeepSeek-R1-Distill-Llama](deepseek-r1-distill-llama.md) | A3 / T1 | Same "open weights, non-OSI license" shape. |

---

## Trajectory

**Direction: opening**

The story here is motion. Gemma launched in 2024 under a restrictive custom license and stayed there through Gemma 3 — but Gemma 4 (April 2026) became the first Gemma under OSI-approved Apache 2.0. These earlier versions remain T1, yet the family's direction is one of the few genuinely *opening* trajectories in the catalog: a major lab relaxing its license rather than tightening it.

**Signal assessment:**

| Signal | Status | Evidence |
| --- | --- | --- |
| License | ⚠️ | Gemma Terms of Use — custom, non-OSI, revisable. (Gemma 4 fixed this.) |
| Feature gating | ➖ | All sizes released as weights; no capability withheld. |
| Self-hosting | ✅ | Standard formats. Ollama, vLLM, llama.cpp. |
| Governance | ⚠️ | Google may update the usage policy and restrict use remotely. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [ai.google.dev/gemma](https://ai.google.dev/gemma)
- **Documentation:** [ai.google.dev/gemma/docs](https://ai.google.dev/gemma/docs)
- **Models:** [huggingface.co/google](https://huggingface.co/google)
