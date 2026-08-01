---
title: "Mistral Medium"
parent: "Technology Catalog"
category: "compute/inference"
status: "stable"
license: "Modified-MIT"
source: "https://huggingface.co/mistralai"
repository: "-"
documentation: "https://docs.mistral.ai"
docker_image: "-"
community: "-"
autonomy_level: "A3"
transparency_level: "T1"
depends_on: []
optional_deps: ["vllm", "ollama", "llama-cpp"]
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
nav_order: 99
---

# Mistral Medium

> **TAS Score: S3/3 — D4/5** — A3 / T1
> _(T1 not T2: the "Modified MIT" license adds a revenue clause — no rights if your company's consolidated monthly revenue exceeds $20M — which is not OSI-approved. Weights are downloadable and self-hostable, so autonomy stays A3; only license transparency drops.)_
> _(D4 not D5: the hosted La Plateforme API collects usage data and requires an account.)_

**Family:** [Mistral (Apache open)](mistral.md) · [Mistral Medium (Modified MIT)](mistral-medium.md)
_This card scores the **Modified-MIT tier** — Mistral Medium 3.5 and Devstral 2. The Apache-2.0 core lineup is a separate object — see the family link._

**⚠️ Two-mode tool.** Self-hosted open weights: A3/T1. Hosted La Plateforme API: A1/T1. This card scores the self-hosted open-weight variant.

## Brief Description

Mistral's Modified-MIT tier — Mistral Medium 3.5 (128B dense, 256K context, multimodal, released April 2026) and Devstral 2 (agentic coding). The weights are published on HuggingFace and fully self-hostable, but under a "Modified MIT" license that reads like MIT with one added condition: organizations whose consolidated monthly revenue exceeds $20M get no rights and must obtain a commercial license or use Mistral AI Studio. Because that revenue clause is not OSI-approved, transparency lands at T1 even though the weights are open.

This is the "looks open, isn't OSI" case — the same shape as Meta's Llama Community License (a scale-based usage restriction), and the reason [DeepSeek-R1-Distill-Llama](deepseek-r1-distill-llama.md) also sits at T1.

## Architectural Role

Compute/inference layer: a frontier-class open-weight model (Medium 3.5) and an agentic coder (Devstral 2), self-hostable on multi-GPU hardware. Medium 3.5's Q4 is roughly 75–80 GB — dual high-end GPUs, an H100/H200, or a 192 GB+ Mac.

## Technical Autonomy

- [x] Works without internet (after model download)
- [x] Stores data locally
- [x] Does not require external accounts (self-hosted)
- [x] Allows data export — weights downloadable (Modified-MIT; restricted only for orgs with >$20M monthly revenue)
- [ ] Hosted La Plateforme API requires an account and sends data to Mistral servers

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
| --- | --- | --- |
| Pause | ✅ | Stop inference. Model weights stay on disk. |
| Exit | ✅ | Standard model format, downloadable. Modified-MIT restricts only >$20M-revenue orgs. |
| Recoverability | ✅ | Re-download from HuggingFace or restore from backup. |
| Visibility | ⚠️ | Open weights, but the Modified-MIT revenue clause is not OSI-approved → T1. Training data not published. |
| External Dependencies | ⚠️ | Self-hosted: none. Hosted API: Mistral infrastructure (EU-based). |

## Configuration (Minimal)

```bash
# Devstral 2 (123B, agentic coding) via vLLM
vllm serve mistralai/Devstral-2-123B-Instruct-2512 --tensor-parallel-size 4

# Mistral Medium 3.5 — see the HuggingFace model card for the current checkpoint id
```

## Alternatives

| Alternative | Autonomy | Notes |
| --- | --- | --- |
| [Mistral](mistral.md) (Apache) | A3 / T2 | Same lab — OSI-permissive core lineup, no revenue clause. |
| [Qwen3](qwen3.md) | A3 / T2 | Apache-2.0 open weights, no revenue clause. |
| [DeepSeek-R1-Distill-Llama](deepseek-r1-distill-llama.md) | A3 / T1 | Same "open weights, non-OSI license" shape. |

---

## Trajectory

**Direction: mixed**

Modified MIT keeps the weights open and self-hostable for nearly everyone, but the >$20M revenue clause is a deliberate monetization gate that OSI would not accept — a small step back from Mistral's otherwise Apache-first stance. Whether future flagships stay Apache or drift into this tier is the signal to watch.

**Signal assessment:**

| Signal | Status | Evidence |
| --- | --- | --- |
| License | ⚠️ | Modified MIT — revenue clause, not OSI-approved. |
| Feature gating | ⚠️ | Merged flagship (Medium 3.5) placed in the restricted tier rather than Apache. |
| Self-hosting | ✅ | Weights downloadable; standard formats, vLLM / Ollama compatible. |
| Governance | ✅ | Independent EU company; license terms documented openly. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [mistral.ai](https://mistral.ai)
- **Documentation:** [docs.mistral.ai](https://docs.mistral.ai)
- **Models:** [huggingface.co/mistralai](https://huggingface.co/mistralai)
