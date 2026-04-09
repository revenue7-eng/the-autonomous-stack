---
title: "ComfyUI"
parent: "Technology Catalog"
category: "compute/inference"
status: "stable"
license: "GPL-3.0"
source: "https://github.com/comfyanonymous/ComfyUI"
repository: "https://github.com/comfyanonymous/ComfyUI"
documentation: "https://github.com/comfyanonymous/ComfyUI/wiki"
docker_image: "-"
community: "https://github.com/comfyanonymous/ComfyUI/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: ["docker"]
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
nav_order: 99
---

# ComfyUI

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Node-based web interface for Stable Diffusion and other image generation models. Visual workflow editor for generating, editing, upscaling, and compositing images. Fully local — no cloud, no API keys.

## Architectural Role

Applications layer: local image generation workflow. Replaces Midjourney, DALL-E, and other cloud image services. Node-based interface allows complex multi-step pipelines (generate → upscale → face-fix → composit).

## Technical Autonomy

- [x] Works without internet (after model download)
- [x] Stores data locally — all generated images on disk
- [x] Does not require external accounts
- [x] Allows data export — standard image files, exportable workflows
- [x] GPL-3.0, fully auditable

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
| --- | --- | --- |
| Pause | ✅ | Stop the server. Models and images stay on disk. |
| Exit | ✅ | Standard model files (safetensors). Images are standard files. Workflows exportable as JSON. |
| Recoverability | ✅ | Reinstall, reload models and workflows. |
| Visibility | ✅ | GPL-3.0. Full source on GitHub. |
| External Dependencies | ✅ | None. Requires GPU for practical use. |

## Configuration (Minimal)

```bash
git clone https://github.com/comfyanonymous/ComfyUI
cd ComfyUI
pip install -r requirements.txt
python main.py
# Open http://localhost:8188
```

## Alternatives

| Alternative | Autonomy | Notes |
| --- | --- | --- |
| [AUTOMATIC1111](automatic1111.md) | A3 / T2 | Form-based UI. Simpler. Larger extension ecosystem. |
| Midjourney | A0 / T0 | Cloud-only. Discord-based. No self-hosted option. |
| DALL-E | A0 / T0 | Cloud-only. OpenAI API. |

---

## Trajectory

**Direction: opening**

GPL-3.0 licensed. Rapidly growing as the standard for local image generation workflows. Huge custom node ecosystem. Community-driven.

**Signal assessment:**

| Signal | Status | Evidence |
| --- | --- | --- |
| License | ✅ | GPL-3.0. Strong copyleft. |
| Feature gating | ✅ | No paid tier. |
| Self-hosting | ✅ | Git clone and run. Active development. |
| Governance | ✅ | Community-driven. Active contributor base. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Repository:** [github.com/comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI)
