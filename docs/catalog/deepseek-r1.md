---
title: "DeepSeek-R1"
parent: "Technology Catalog"
category: "compute/inference"
status: "stable"
license: "MIT"
source: "https://huggingface.co/deepseek-ai/DeepSeek-R1"
repository: "https://github.com/deepseek-ai/DeepSeek-R1"
documentation: "https://github.com/deepseek-ai/DeepSeek-R1"
docker_image: "-"
community: "https://github.com/deepseek-ai/DeepSeek-R1/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: ["vllm", "sglang"]
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
nav_order: 99
---

# DeepSeek-R1

> **TAS Score: S3/3 — D4/5** — A3 / T2
> _(D4 not D5: hosted API (api.deepseek.com) collects usage data and requires account — trajectory mixed due to Chinese regulatory environment.)_

**Family:** [DeepSeek-R1 (full)](deepseek-r1.md) · [R1-Distill-Qwen](deepseek-r1-distill-qwen.md) · [R1-Distill-Llama](deepseek-r1-distill-llama.md)
_This card scores the **full 671B model only.** The distilled variants are separate objects with different base licenses — see the family links above._

**⚠️ Two-mode tool.** Self-hosted: A3/T2. Hosted API (api.deepseek.com): A1/T1. This card scores the self-hosted open-weight variant.

## Brief Description

Full-size open-weight reasoning model from DeepSeek — 671B parameters (Mixture-of-Experts). Trained on DeepSeek-V3-Base (DeepSeek's own base model). Chain-of-thought reasoning is visible in output. MIT licensed — weights and base are both under a permissive, OSI-approved license, so transparency is uncontested.

Running the full model requires server-class hardware (multi-GPU cluster). For consumer-hardware deployment, use the distilled variants — but note they are **different models** with **different base licenses**, scored on their own cards.

## Architectural Role

Compute/inference layer: frontier-class reasoning model for complex analysis, run on your own infrastructure. Local alternative to cloud reasoning APIs when you have the hardware to host the full model.

## Technical Autonomy

- [x] Works without internet (after model download)
- [x] Stores data locally
- [x] Does not require external accounts (self-hosted)
- [x] Allows data export — MIT licensed, standard HuggingFace format
- [ ] Hosted API requires account and sends data to DeepSeek servers

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
| --- | --- | --- |
| Pause | ✅ | Stop inference. Model weights stay on disk. |
| Exit | ✅ | Standard model format. MIT licensed — no restrictions on use. |
| Recoverability | ✅ | Re-download from HuggingFace or restore from backup. |
| Visibility | ✅ | MIT license (weights + DeepSeek-V3 base). Open weights. Training methodology published. |
| External Dependencies | ⚠️ | Self-hosted: none. Hosted API: DeepSeek infrastructure (China-based). |

## Configuration (Minimal)

```bash
# Full 671B model — requires a multi-GPU cluster
vllm serve deepseek-ai/DeepSeek-R1 --tensor-parallel-size 8

# Or via SGLang
python -m sglang.launch_server --model deepseek-ai/DeepSeek-R1 --tp 8
```

_For consumer hardware, see [R1-Distill-Qwen](deepseek-r1-distill-qwen.md) (Apache base) or [R1-Distill-Llama](deepseek-r1-distill-llama.md) (Llama base — lower transparency)._

## Alternatives

| Alternative | Autonomy | Notes |
| --- | --- | --- |
| [MiroThinker](mirothinker.md) | A3 / T2 | Verification-centric reasoning. Apache-2.0. |
| [R1-Distill-Qwen](deepseek-r1-distill-qwen.md) | A3 / T2 | Same reasoning, consumer hardware, Apache base. |
| OpenAI o1 | A0 / T0 | Cloud-only. Proprietary. |

---

## Trajectory

**Direction: mixed**

MIT licensed — maximally permissive. Groundbreaking open release that challenged frontier labs. But: DeepSeek is a Chinese company subject to regulatory environment. Hosted API subject to content filtering. Future open releases not guaranteed.

**Signal assessment:**

| Signal | Status | Evidence |
| --- | --- | --- |
| License | ✅ | MIT. Maximally permissive. |
| Feature gating | ✅ | Open weights for all variants including full 671B. |
| Self-hosting | ✅ | Standard formats. vLLM, SGLang compatible. |
| Governance | ⚠️ | Corporate (DeepSeek/High-Flyer). Chinese regulatory environment. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [deepseek.com](https://deepseek.com)
- **Repository:** [github.com/deepseek-ai/DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1)
- **Models:** [huggingface.co/deepseek-ai](https://huggingface.co/deepseek-ai)
