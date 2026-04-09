---
title: "Midjourney"
parent: "Technology Catalog"
category: "compute/inference"
status: "stable"
license: "Proprietary"
source: "-"
repository: "-"
documentation: "https://docs.midjourney.com"
docker_image: "-"
community: "https://discord.gg/midjourney"
autonomy_level: "A0"
transparency_level: "T0"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Pause", "Exit", "Recoverability"]
nav_order: 99
---

# Midjourney

> **TAS Score: S0/3 — D1/5** — A0 / T0
> _(S0: Pause ❌ — subscription service. Exit ❌ — no model export, generated images have usage restrictions. Recoverability ❌ — no rollback.)_
> _(D1: Personalisation ⚠️ builds style profiles. Urgency ⚠️ subscription pressure, limited free generations. Hidden cost ⚠️ content used for training. Transparency fragility ⚠️ proprietary model.)_

## Brief Description

Cloud-based AI image generation. Known for high-quality artistic output. Originally Discord-only interface, now has web app. Subscription required. No open model, no self-hosted option.

## Why it's in the catalog

Midjourney is the most popular AI image generator. Including it shows the autonomy contrast: every capability Midjourney offers has a self-hosted equivalent (Stable Diffusion via ComfyUI or AUTOMATIC1111), with radically different autonomy scores.

## Architectural Role

Cloud-hosted compute/inference: image generation. All processing on Midjourney servers. Subscription model ($10-60/month).

## Technical Autonomy

- [ ] Works without internet — **no**
- [ ] Stores data locally — **no, images on Midjourney servers**
- [x] Does not require external accounts — **requires Midjourney account**
- [ ] Allows data export — **can download generated images, cannot export model**
- [ ] Provides offline updates — **no**

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
| --- | --- | --- |
| Pause | ❌ | Subscription service. Cancel = lose access. |
| Exit | ❌ | Can download images. Cannot take the model or generation capability. |
| Recoverability | ❌ | No rollback. Model versions change without user control. |
| Visibility | ❌ | Proprietary. No source, no weights, no architecture disclosure. |
| External Dependencies | ❌ | Entirely dependent on Midjourney Inc. |

## Autonomous Alternatives

| Alternative | Autonomy | Notes |
| --- | --- | --- |
| [ComfyUI](comfyui.md) | A3 / T2 | Node-based local image generation. Full control. |
| [AUTOMATIC1111](automatic1111.md) | A3 / T2 | Form-based UI. Huge extension ecosystem. |
| Stable Diffusion (models) | A3 / T2 | Open-weight models. Run anywhere. |

---

## Trajectory

**Direction: closing**

Started Discord-only, now web app — but still cloud-locked. Subscription price increasing. Content policies tightening. No open model. No API for third-party integration. Increasingly walled garden.

**Signal assessment:**

| Signal | Status | Evidence |
| --- | --- | --- |
| License | ⚠️ | Proprietary. No open alternative from Midjourney. |
| Feature gating | ⚠️ | Free tier effectively eliminated. Paid tiers increasing. |
| Self-hosting | ⚠️ | No self-hosted option. No API. |
| Governance | ⚠️ | Single company. No community input on direction. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [midjourney.com](https://midjourney.com)
- **Documentation:** [docs.midjourney.com](https://docs.midjourney.com)
