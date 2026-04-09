---
title: "Piper"
parent: "Technology Catalog"
category: "compute/inference"
status: "stable"
license: "MIT"
source: "https://github.com/rhasspy/piper"
repository: "https://github.com/rhasspy/piper"
documentation: "https://github.com/rhasspy/piper/blob/master/README.md"
docker_image: "-"
community: "https://github.com/rhasspy/piper/discussions"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: []
optional_deps: ["home-assistant"]
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
nav_order: 99
---

# Piper

> **TAS Score: S3/3 — D5/5** — A3 / T2

## Brief Description

Fast local text-to-speech engine. Multiple languages, natural-sounding voices. Runs on Raspberry Pi. Used by Home Assistant for local voice control. No cloud, no API keys.

## Architectural Role

Compute/inference layer: local text-to-speech. Replaces Google TTS, Amazon Polly, ElevenLabs. Pairs with Whisper.cpp (speech-to-text) for a complete local voice pipeline.

## Technical Autonomy

- [x] Works completely offline
- [x] Stores data locally — voice models are local files
- [x] Does not require external accounts
- [x] Allows data export — standard audio output
- [x] Runs on minimal hardware (Raspberry Pi)

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
| --- | --- | --- |
| Pause | ✅ | Stop the process. Models stay on disk. |
| Exit | ✅ | Standard ONNX voice models. Portable. |
| Recoverability | ✅ | Re-download models. Nothing to lose. |
| Visibility | ✅ | MIT license. Full source on GitHub. |
| External Dependencies | ✅ | None. |

## Configuration (Minimal)

```bash
# Install
pip install piper-tts

# Generate speech
echo "Hello, world" | piper --model en_US-lessac-medium --output_file hello.wav

# Or download binary
wget https://github.com/rhasspy/piper/releases/latest/download/piper_linux_x86_64.tar.gz
```

## Alternatives

| Alternative | Autonomy | Notes |
| --- | --- | --- |
| Google TTS | A0 / T0 | Cloud-only. Audio sent to Google. |
| ElevenLabs | A0 / T0 | Cloud-only. Subscription required. |
| Coqui TTS | A3 / T2 | More voices, heavier. Project discontinued. |

---

## Trajectory

**Direction: opening**

MIT licensed. Part of the Rhasspy voice assistant ecosystem. Growing voice model library. Integrated into Home Assistant. Active development.

**Signal assessment:**

| Signal | Status | Evidence |
| --- | --- | --- |
| License | ✅ | MIT. No changes. |
| Feature gating | ✅ | No paid tier. |
| Self-hosting | ✅ | Single binary. Runs on Raspberry Pi. |
| Governance | ✅ | Community-driven. Part of Rhasspy ecosystem. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

- **Repository:** [github.com/rhasspy/piper](https://github.com/rhasspy/piper)
- **Voice models:** [huggingface.co/rhasspy/piper-voices](https://huggingface.co/rhasspy/piper-voices)
