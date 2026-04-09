---
title: "Whisper.cpp"
parent: "Technology Catalog"
category: "compute/inference"
status: "stable"
license: "MIT"
source: "https://github.com/ggerganov/whisper.cpp"
repository: "https://github.com/ggerganov/whisper.cpp"
documentation: "https://github.com/ggerganov/whisper.cpp/blob/master/README.md"
docker_image: "-"
community: "https://github.com/ggerganov/whisper.cpp/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: ["docker"]
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
nav_order: 99
---

# Whisper.cpp

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

C/C++ port of OpenAI's Whisper speech-to-text model. Transcribes audio locally on CPU — no cloud, no API keys, no data leaves your machine. Supports 99 languages. From the same author as llama.cpp (Georgi Gerganov).

## Architectural Role

Compute/inference layer: local speech-to-text. Replaces cloud transcription services (Google Speech-to-Text, Otter.ai, OpenAI Whisper API). Pairs with Piper (text-to-speech) for a complete local voice pipeline. Can be integrated into Home Assistant, Jellyfin, and other self-hosted tools.

## Technical Autonomy

- [x] Works completely offline (after model download)
- [x] Stores data locally — audio never leaves the machine
- [x] Does not require external accounts
- [x] Allows data export — standard text/SRT/VTT output
- [x] Compiles from source with no external dependencies

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
| --- | --- | --- |
| Pause | ✅ | Stop the process. Models stay on disk. |
| Exit | ✅ | Models are standard GGML files. Output is plain text. |
| Recoverability | ✅ | Recompile, re-download model. Nothing to lose. |
| Visibility | ✅ | MIT license. Full source on GitHub. |
| External Dependencies | ✅ | None. Compiles standalone. Models downloadable from HuggingFace. |

## Configuration (Minimal)

```bash
# Build from source
git clone https://github.com/ggerganov/whisper.cpp
cd whisper.cpp && make

# Download a model
bash models/download-ggml-model.sh base.en

# Transcribe an audio file
./main -m models/ggml-base.en.bin -f audio.wav

# Real-time microphone transcription
./stream -m models/ggml-base.en.bin
```

## Related Recipes

- [Home Office](../recipes/home-office.md) — local transcription for meetings

## Alternatives

| Alternative | Autonomy | Notes |
| --- | --- | --- |
| OpenAI Whisper API | A0 / T0 | Cloud-only. Audio sent to OpenAI servers. Pay per minute. |
| Google Speech-to-Text | A0 / T0 | Cloud-only. Audio sent to Google. |
| Otter.ai | A0 / T0 | Cloud-only. Requires account. Stores all transcriptions on their servers. |

---

## Trajectory

**Direction: opening**

MIT licensed, same author as llama.cpp, active community. Expanding hardware support (CoreML, CUDA, Vulkan). GGML model format widely adopted. No commercial entity behind it — pure open-source.

**Signal assessment:**

| Signal | Status | Evidence |
| --- | --- | --- |
| License | ✅ | MIT. No changes. |
| Feature gating | ✅ | No paid tier. Everything free and open. |
| Self-hosting | ✅ | Single compilation. Runs on anything from Raspberry Pi to server GPUs. |
| Governance | ✅ | Community-driven. Healthy contributor base. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Website:** [github.com/ggerganov/whisper.cpp](https://github.com/ggerganov/whisper.cpp)
- **Repository:** [github.com/ggerganov/whisper.cpp](https://github.com/ggerganov/whisper.cpp)
- **Original model:** [github.com/openai/whisper](https://github.com/openai/whisper)
