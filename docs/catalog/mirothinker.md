---
title: "MiroThinker"
parent: "Technology Catalog"
category: "compute/inference"
status: "stable"
license: "Apache-2.0"
source: "https://huggingface.co/miromind-ai/MiroThinker-v1.5-30B"
repository: "https://github.com/MiroMindAI/MiroThinker"
documentation: "https://github.com/MiroMindAI/MiroThinker"
docker_image: "-"
community: "https://discord.gg/miromind"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: ["docker"]
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
nav_order: 99
---

# MiroThinker

> **TAS Score: S3/3 — D4/5** — A3 / T2
> _(D4 not D5: hosted app (dr.miromind.ai) builds user profiles and requires account — trajectory mixed due to commercial push alongside open weights.)_

**⚠️ Two-mode tool.** Self-hosted: A3/T2. Hosted app (dr.miromind.ai): A1/T1. This card scores the self-hosted open-weight variant.

## Brief Description

Open-weight reasoning model from MiroMind (30B and 235B parameter variants). Designed for deep research and multi-step verification — proposes hypotheses, searches for evidence, identifies mismatches, revises conclusions. Runs locally via vLLM or SGLang. Hosted version available but requires account.

## Architectural Role

Compute/inference layer: reasoning model for complex research and analysis tasks. Replaces hosted research agents (OpenAI Deep Research, Perplexity Pro) when run locally. The 30B variant runs on a single high-end GPU; the 235B MoE variant (22B active) requires multi-GPU setup.

## Technical Autonomy

- [x] Works without internet (after model download)
- [x] Stores data locally (model weights are standard files)
- [x] Does not require external accounts (self-hosted variant)
- [x] Allows data export — standard HuggingFace model format
- [ ] Hosted app requires account and sends data to MiroMind servers

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
| --- | --- | --- |
| Pause | ✅ | Stop inference server. Model weights stay on disk. |
| Exit | ✅ | Model weights are downloadable files. Use with any vLLM/SGLang compatible setup. |
| Recoverability | ✅ | Re-download weights from HuggingFace or restore from backup. |
| Visibility | ✅ | Apache-2.0. Open weights on HuggingFace. Training code on GitHub. |
| External Dependencies | ⚠️ | Self-hosted: none. Hosted app: depends on MiroMind infrastructure. |

## Configuration (Minimal)

```bash
# Using vLLM (requires NVIDIA GPU with sufficient VRAM)
pip install vllm
vllm serve miromind-ai/MiroThinker-v1.5-30B \
  --tensor-parallel-size 1 \
  --max-model-len 65536

# Using SGLang
pip install sglang
python -m sglang.launch_server \
  --model-path miromind-ai/MiroThinker-v1.5-30B \
  --tp 1 --host 0.0.0.0 --port 1234

# Via Ollama (if GGUF quantization available)
ollama pull mirothinker:30b
ollama run mirothinker:30b
```

## Related Recipes

- [Developer Workstation](../recipes/developer-workstation.md) — local AI coding and research

## Alternatives

| Alternative | Autonomy | Notes |
| --- | --- | --- |
| [DeepSeek-R1](deepseek-r1.md) | A3 / T2 | Open-weight reasoning. Distilled versions run via Ollama. |
| [Ollama](ollama.md) + Qwen3 | A3 / T2 | Simpler setup. Less specialized reasoning. |
| OpenAI Deep Research | A0 / T0 | Cloud-only. Proprietary. All data on OpenAI servers. |

---

## Trajectory

**Direction: mixed**

Open weights published on HuggingFace (Apache-2.0). Active research team. But commercial direction is visible: hosted app with account requirement, enterprise pitch for financial services. Classic pattern of open-core with closing commercial layer.

**Signal assessment:**

| Signal | Status | Evidence |
| --- | --- | --- |
| License | ✅ | Apache-2.0 for model weights. Open. |
| Feature gating | ⚠️ | Hosted app may get features not available in open weights. Enterprise tier emerging. |
| Self-hosting | ✅ | Standard HuggingFace distribution. vLLM/SGLang compatible. |
| Governance | ⚠️ | Corporate-led (MiroMind Inc). Small team, venture-backed. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [miromind.ai](https://www.miromind.ai)
- **Repository:** [github.com/MiroMindAI](https://github.com/MiroMindAI)
- **Models:** [huggingface.co/miromind-ai](https://huggingface.co/miromind-ai)
- **Hosted demo:** [dr.miromind.ai](https://dr.miromind.ai)
