---
title: "Claude API"
parent: "Technology Catalog"
category: "compute/inference"
status: "stable"
license: "Proprietary"
source: "-"
repository: "-"
documentation: "https://docs.anthropic.com"
docker_image: "-"
community: "https://docs.anthropic.com"
autonomy_level: "A0"
transparency_level: "T0"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Pause", "Exit", "Recoverability"]
nav_order: 99
---

# Claude API

> **TAS Score: S0/3 — D2/5** — A0 / T0
> _(S0: Pause ❌ — service controlled by Anthropic. Exit ❌ — no model export. Recoverability ❌ — no rollback.)_
> _(D2: Personalisation ⚠️ conversation data processed. Hidden cost ⚠️ data retention policies. Transparency fragility ⚠️ proprietary model.)_

## Brief Description

Cloud-based AI API by Anthropic. Claude models (Opus, Sonnet, Haiku) accessible via API and web interface (claude.ai). Known for strong reasoning and safety alignment. No self-hosted option.

## Why it's in the catalog

Claude is one of the leading AI assistants. Including it makes the autonomy trade-off visible against self-hosted alternatives. This card exists for comparison, not recommendation.

## Architectural Role

Cloud-hosted compute/inference. All processing on Anthropic/cloud infrastructure. API requires authentication and payment. Web interface requires account.

## Technical Autonomy

- [ ] Works without internet — **no, cloud-only**
- [ ] Stores data locally — **no, data on Anthropic servers**
- [x] Does not require external accounts — **requires Anthropic account**
- [ ] Allows data export — **conversation export exists, model cannot be exported**
- [ ] Provides offline updates — **no**

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
| --- | --- | --- |
| Pause | ❌ | Cannot pause the service. Anthropic controls availability. |
| Exit | ❌ | Conversation export possible. Model and capabilities cannot be taken. |
| Recoverability | ❌ | No rollback. Model versions change without user control. |
| Visibility | ❌ | Proprietary. No source code. No model weights. |
| External Dependencies | ❌ | Entirely dependent on Anthropic infrastructure. |

## Configuration (Minimal)

```bash
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "content-type: application/json" \
  -H "anthropic-version: 2023-06-01" \
  -d '{"model":"claude-sonnet-4-20250514","max_tokens":1024,"messages":[{"role":"user","content":"Hello"}]}'
```

No self-hosted option exists.

## Autonomous Alternatives

| Alternative | Autonomy | Notes |
| --- | --- | --- |
| [Ollama](ollama.md) + [Open WebUI](open-webui.md) | A3 / T2 | Self-hosted chat. Free, private, offline. |
| [MiroThinker](mirothinker.md) | A3 / T2 | Open-weight reasoning model. |
| [DeepSeek-R1](deepseek-r1.md) | A3 / T2 | Open-weight reasoning. MIT licensed. |

---

## Trajectory

**Direction: stable**

Anthropic positions itself as a safety-focused AI lab. No open-weight models. API-only access. Pricing competitive but cloud-locked. Constitutional AI approach is documented but model weights are proprietary.

**Signal assessment:**

| Signal | Status | Evidence |
| --- | --- | --- |
| License | ⚠️ | Proprietary. No open-weight models. |
| Feature gating | ⚠️ | Free tier limited. Best models behind paid API. |
| Self-hosting | ⚠️ | No self-hosted option. API-only. |
| Governance | ➖ | Corporate. Safety-focused research published, but models closed. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [anthropic.com](https://www.anthropic.com)
- **Documentation:** [docs.anthropic.com](https://docs.anthropic.com)
