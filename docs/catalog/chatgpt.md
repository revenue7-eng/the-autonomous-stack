---
title: "ChatGPT"
parent: "Technology Catalog"
category: "compute/inference"
status: "stable"
license: "Proprietary"
source: "-"
repository: "-"
documentation: "https://platform.openai.com/docs"
docker_image: "-"
community: "https://community.openai.com"
autonomy_level: "A0"
transparency_level: "T0"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Pause", "Exit", "Recoverability"]
nav_order: 99
---

# ChatGPT

> **TAS Score: S0/3 — D1/5** — A0 / T0
> _(S0: Pause ❌ — service controlled by OpenAI, can be discontinued or modified at any time. Exit ❌ — no way to export the model or fully replicate the service. Recoverability ❌ — no rollback, no local backup of model capabilities.)_
> _(D1: Personalisation ⚠️ builds user profiles. Urgency ⚠️ subscription pressure. Hidden cost ⚠️ data used for training. Transparency fragility ⚠️ value depends on proprietary model.)_

## Brief Description

Cloud-based AI assistant by OpenAI. GPT-4o, o1, and other proprietary models accessible via web interface, mobile apps, and API. The most widely used AI chatbot — and the benchmark against which self-hosted alternatives are measured.

## Why it's in the catalog

ChatGPT is the default AI tool for most people. Including it makes the autonomy trade-off visible: every feature ChatGPT offers has a self-hosted equivalent, but at a different point on the autonomy spectrum. This card exists for comparison, not recommendation.

## Architectural Role

Cloud-hosted compute/inference. All processing happens on OpenAI's infrastructure. No local component. API requires authentication and payment. Web interface requires account.

## Technical Autonomy

- [ ] Works without internet — **no, cloud-only**
- [ ] Stores data locally — **no, all data on OpenAI servers**
- [x] Does not require external accounts — **requires OpenAI account**
- [ ] Allows data export — **conversation export exists, model cannot be exported**
- [ ] Provides offline updates — **no**

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
| --- | --- | --- |
| Pause | ❌ | Cannot pause the service. OpenAI can modify, rate-limit, or discontinue at any time. |
| Exit | ❌ | Conversation history exportable. Model, capabilities, and fine-tuning cannot be taken. |
| Recoverability | ❌ | No rollback. Model versions change without user control. |
| Visibility | ❌ | Proprietary. No source code. No model weights. Architecture not disclosed. |
| External Dependencies | ❌ | Entirely dependent on OpenAI infrastructure and business decisions. |

## Configuration (Minimal)

```bash
# API usage (requires API key and payment)
curl https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-4o","messages":[{"role":"user","content":"Hello"}]}'
```

No self-hosted option exists.

## Autonomous Alternatives

| Alternative | Autonomy | Notes |
| --- | --- | --- |
| [Ollama](ollama.md) + [Open WebUI](open-webui.md) | A3 / T2 | Self-hosted ChatGPT-like experience. Free, private, offline. |
| [llama.cpp](llama-cpp.md) | A3 / T2 | Low-level inference. Maximum control. |
| [MiroThinker](mirothinker.md) | A3 / T2 | Open-weight reasoning model for research tasks. |

---

## Trajectory

**Direction: closing**

OpenAI started as a non-profit research lab committed to open AI. GPT-2 was released with open weights. Since then: GPT-3, GPT-4, o1, o3 — all proprietary. Corporate restructuring from non-profit to capped-profit. Increasing prices, feature gating behind Plus/Pro/Team/Enterprise tiers.

**Signal assessment:**

| Signal | Status | Evidence |
| --- | --- | --- |
| License | ⚠️ | Proprietary. Moved from open (GPT-2) to fully closed. |
| Feature gating | ⚠️ | Free tier increasingly limited. Best models behind $20+/month subscription. |
| Self-hosting | ⚠️ | No self-hosted option. API-only access with rate limits and content policies. |
| Governance | ⚠️ | Corporate-controlled. Board drama. No community governance. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [openai.com](https://openai.com)
- **Documentation:** [platform.openai.com/docs](https://platform.openai.com/docs)
- **Community:** [community.openai.com](https://community.openai.com)
