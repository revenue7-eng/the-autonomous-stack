---
title: "Google Gemini"
parent: "Technology Catalog"
category: "compute/inference"
status: "stable"
license: "Proprietary"
source: "-"
repository: "-"
documentation: "https://ai.google.dev/docs"
docker_image: "-"
community: "https://ai.google.dev/community"
autonomy_level: "A0"
transparency_level: "T0"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Pause", "Exit", "Recoverability"]
nav_order: 99
---

# Google Gemini

> **TAS Score: S0/3 — D1/5** — A0 / T0
> _(S0: Pause ❌ — Google controls the service. Exit ❌ — no model export. Recoverability ❌ — no rollback.)_
> _(D1: Personalisation ⚠️ deep user profiling. Urgency ⚠️ ecosystem lock-in pressure. Hidden cost ⚠️ data feeds Google's ecosystem. Transparency fragility ⚠️ proprietary.)_

**Note:** Google's open-weight models (Gemma) are a separate product and score A3/T2 when self-hosted. This card covers the Gemini API and web interface.

## Brief Description

Cloud-based AI by Google. Gemini models accessible via API, web interface (gemini.google.com), and integrated into Google Workspace. Proprietary. Part of Google's broader data ecosystem.

## Why it's in the catalog

Gemini is one of the most widely available AI services through Google integration. Including it shows the autonomy gap — especially notable because Google also publishes Gemma (open-weight, A3/T2). Same company, radically different autonomy.

## Architectural Role

Cloud-hosted compute/inference. All processing on Google infrastructure. Deep integration with Google ecosystem (Workspace, Search, Android).

## Technical Autonomy

- [ ] Works without internet — **no**
- [ ] Stores data locally — **no**
- [x] Does not require external accounts — **requires Google account**
- [ ] Allows data export — **limited conversation export**
- [ ] Provides offline updates — **no**

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
| --- | --- | --- |
| Pause | ❌ | Google controls the service. |
| Exit | ❌ | Cannot export model. Limited data export. |
| Recoverability | ❌ | No rollback. Model changes without notice. |
| Visibility | ❌ | Proprietary. No source, no weights. |
| External Dependencies | ❌ | Entirely Google-dependent. |

## Autonomous Alternatives

| Alternative | Autonomy | Notes |
| --- | --- | --- |
| Gemma (self-hosted) | A3 / T2 | Google's open-weight models. Run via Ollama. |
| [Ollama](ollama.md) + [Open WebUI](open-webui.md) | A3 / T2 | Self-hosted chat. |
| [DeepSeek-R1](deepseek-r1.md) | A3 / T2 | Open-weight reasoning. |

---

## Trajectory

**Direction: closing**

Gemini API is proprietary and cloud-locked. Pricing competitive but ecosystem-integrated — the more you use Google services, the deeper the lock-in. Gemma (open-weight) exists but is a separate, smaller product line.

**Signal assessment:**

| Signal | Status | Evidence |
| --- | --- | --- |
| License | ⚠️ | Proprietary. Gemma is open, Gemini is not. |
| Feature gating | ⚠️ | Free tier limited. Best models behind paid API/subscription. |
| Self-hosting | ⚠️ | No self-hosted option for Gemini. Gemma is self-hostable. |
| Governance | ⚠️ | Google controls everything. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [gemini.google.com](https://gemini.google.com)
- **Documentation:** [ai.google.dev](https://ai.google.dev)
