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
optional_deps: ["ollama", "docker"]
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
nav_order: 99
---

# DeepSeek-R1

> **TAS Score: S3/3 — D4/5** — A3 / T2
> _(D4 not D5: hosted API (api.deepseek.com) collects usage data and requires account — trajectory mixed due to Chinese regulatory environment.)_

**⚠️ Two-mode tool.** Self-hosted: A3/T2. Hosted API (api.deepseek.com): A1/T1. This card scores the self-hosted open-weight variant.

## Brief Description

Open-weight reasoning model from DeepSeek. Chain-of-thought reasoning is visible in output. MIT licensed. Full model (671B MoE) and distilled versions (1.5B to 70B) available. Distilled versions run via Ollama on consumer hardware.

## Architectural Role

Compute/inference layer: reasoning model for complex analysis. Replaces OpenAI o1/o3 and Claude reasoning modes when run locally. Distilled variants (7B, 14B) practical for self-hosted deployment.

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
| Visibility | ✅ | MIT license. Open weights. Training methodology published. |
| External Dependencies | ⚠️ | Self-hosted: none. Hosted API: DeepSeek infrastructure (China-based). |

## Configuration (Minimal)

```bash
# Via Ollama (distilled 7B — runs on consumer hardware)
ollama pull deepseek-r1:7b
ollama run deepseek-r1:7b

# Via vLLM (full or larger variants — requires GPU cluster)
vllm serve deepseek-ai/DeepSeek-R1-Distill-Llama-70B --tensor-parallel-size 4
```

## Alternatives

| Alternative | Autonomy | Notes |
| --- | --- | --- |
| [MiroThinker](mirothinker.md) | A3 / T2 | Verification-centric reasoning. Apache-2.0. |
| [Ollama](ollama.md) + Qwen3 | A3 / T2 | Simpler reasoning. Easier setup. |
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
| Self-hosting | ✅ | Standard formats. Ollama, vLLM, SGLang compatible. |
| Governance | ⚠️ | Corporate (DeepSeek/High-Flyer). Chinese regulatory environment. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [deepseek.com](https://deepseek.com)
- **Repository:** [github.com/deepseek-ai/DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1)
- **Models:** [huggingface.co/deepseek-ai](https://huggingface.co/deepseek-ai)
