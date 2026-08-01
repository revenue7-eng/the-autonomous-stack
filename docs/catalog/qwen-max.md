---
title: "Qwen-Max"
parent: "Technology Catalog"
category: "compute/inference"
status: "stable"
license: "Proprietary"
source: "-"
repository: "-"
documentation: "https://www.alibabacloud.com/help/en/model-studio/"
docker_image: "-"
community: "-"
autonomy_level: "A0"
transparency_level: "T0"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Pause", "Exit", "Recoverability"]
nav_order: 99
---

# Qwen-Max

> **TAS Score: S0/3 — D1/5** — A0 / T0
> _(S0: Pause ❌ — Alibaba controls the service. Exit ❌ — no model export, weights never released. Recoverability ❌ — no rollback; the model changes without notice.)_
> _(D1: Personalisation ⚠️ account-bound API profiling. Urgency ⚠️ subscription/credit pressure. Hidden cost ⚠️ prompts processed on Alibaba servers. Transparency fragility ⚠️ proprietary, plus Chinese regulatory environment.)_

**Note:** Alibaba's open-weight models (Qwen3) are a separate product and score A3/T2 when self-hosted. This card covers the API-only Qwen-Max flagship.

## Brief Description

Alibaba's top-tier proprietary model, available only through the Alibaba Cloud Model Studio / DashScope API — never released as open weights. Positioned above the open Qwen3 line as the frontier commercial offering (Qwen-Max / Qwen3-Max).

## Why it's in the catalog

Qwen-Max shows the autonomy gap inside a single vendor: Alibaba publishes Qwen3 as open weights (A3/T2) but keeps its most capable model API-only and closed. Same company, radically different autonomy — the exact contrast the catalog exists to make visible. This card is for comparison, not recommendation.

## Architectural Role

Cloud-hosted compute/inference. All processing on Alibaba Cloud infrastructure (China-based). Requires an Alibaba Cloud account and API credits. No local component.

## Technical Autonomy

- [ ] Works without internet — **no**
- [ ] Stores data locally — **no**
- [ ] Does not require external accounts — **requires Alibaba Cloud account**
- [ ] Allows data export — **no model export; limited data export**
- [ ] Provides offline updates — **no**

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
| --- | --- | --- |
| Pause | ❌ | Alibaba controls the service. |
| Exit | ❌ | Cannot export the model. Weights never released. |
| Recoverability | ❌ | No rollback. Model changes without notice. |
| Visibility | ❌ | Proprietary. No source, no weights. |
| External Dependencies | ❌ | Entirely Alibaba-dependent. China-based infrastructure. |

## Autonomous Alternatives

| Alternative | Autonomy | Notes |
| --- | --- | --- |
| [Qwen3](qwen3.md) (self-hosted) | A3 / T2 | Alibaba's own open-weight models. Apache-2.0. |
| [Ollama](ollama.md) + [Open WebUI](open-webui.md) | A3 / T2 | Self-hosted chat. |
| [DeepSeek-R1](deepseek-r1.md) | A3 / T2 | Open-weight reasoning. |

---

## Trajectory

**Direction: closing**

Qwen-Max is proprietary and API-only. While Alibaba's open Qwen3 line is aggressively permissive, the flagship Max tier stays closed and, in recent releases, subscription-gated — the capability ceiling is kept behind the API.

**Signal assessment:**

| Signal | Status | Evidence |
| --- | --- | --- |
| License | ⚠️ | Proprietary. Qwen3 is open, Qwen-Max is not. |
| Feature gating | ⚠️ | Top capability API-only; newest Max tiers subscription-gated. |
| Self-hosting | ⚠️ | No self-hosted option for Qwen-Max. Qwen3 is self-hostable. |
| Governance | ⚠️ | Alibaba controls everything. Chinese regulatory environment. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [qwen.ai](https://qwen.ai)
- **Documentation:** [alibabacloud.com/help/en/model-studio](https://www.alibabacloud.com/help/en/model-studio/)
