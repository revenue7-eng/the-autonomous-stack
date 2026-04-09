---
title: "AUTOMATIC1111"
parent: "Technology Catalog"
category: "compute/inference"
status: "stable"
license: "AGPL-3.0"
source: "https://github.com/AUTOMATIC1111/stable-diffusion-webui"
repository: "https://github.com/AUTOMATIC1111/stable-diffusion-webui"
documentation: "https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki"
docker_image: "-"
community: "https://github.com/AUTOMATIC1111/stable-diffusion-webui/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: ["docker"]
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
nav_order: 99
---

# AUTOMATIC1111

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Web UI for Stable Diffusion image generation. The original and most widely used self-hosted image generation interface. Form-based UI with txt2img, img2img, inpainting, upscaling. Huge extension ecosystem.

## Architectural Role

Applications layer: local image generation. Replaces Midjourney and DALL-E. Simpler interface than ComfyUI (forms vs nodes). Massive extension library for specialized workflows.

## Technical Autonomy

- [x] Works without internet (after model download)
- [x] Stores data locally
- [x] Does not require external accounts
- [x] Allows data export — standard image files, standard model files
- [x] AGPL-3.0, fully auditable

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
| --- | --- | --- |
| Pause | ✅ | Stop the server. Everything stays local. |
| Exit | ✅ | Standard safetensors models. Standard image files. |
| Recoverability | ✅ | Reinstall, reload models. |
| Visibility | ✅ | AGPL-3.0. Full source on GitHub. |
| External Dependencies | ✅ | None. Requires GPU for practical use. |

## Configuration (Minimal)

```bash
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui
cd stable-diffusion-webui
./webui.sh
# Open http://localhost:7860
```

## Alternatives

| Alternative | Autonomy | Notes |
| --- | --- | --- |
| [ComfyUI](comfyui.md) | A3 / T2 | Node-based. More flexible, steeper learning curve. |
| Midjourney | A0 / T0 | Cloud-only. Discord-based. |
| DALL-E | A0 / T0 | Cloud-only. OpenAI API. |

---

## Trajectory

**Direction: stable**

AGPL-3.0. Mature project. Development has slowed compared to ComfyUI, but stable and well-tested. Enormous extension ecosystem maintained by community.

**Signal assessment:**

| Signal | Status | Evidence |
| --- | --- | --- |
| License | ✅ | AGPL-3.0. No changes. |
| Feature gating | ✅ | No paid tier. |
| Self-hosting | ✅ | One-click installer scripts. |
| Governance | ⚠️ | Single maintainer. Community extensions are separate projects. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Repository:** [github.com/AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
