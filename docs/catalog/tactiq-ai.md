---
title: "TactiQ AI Platform"
category: "applications/edge-ai"
status: "stable"
license: "Proprietary (Perpetual)"
source: "https://tactiq.ai"
---

# TactiQ AI Platform

## Brief Description
A hardened edge‑AI platform that operates completely offline, with zero‑value‑on‑capture security. Designed for critical infrastructure, defence, and remote sites.

## Architectural Role
Edge AI layer: provides autonomous video analytics, anomaly detection, and sensor fusion without cloud connectivity.

## Technical Autonomy
- ✅ Works without internet (12+ months)
- ✅ Stores data locally (encrypted, TPM‑protected)
- ✅ Does not require external accounts
- ✅ Allows data export (via escrow keys in Enterprise config)
- ✅ Provides offline updates (RAUC A/B, USB/SD)

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
|-----------|--------|----------|
| **Pause** | ✅ | The system implements **fail‑closed**: any anomaly triggers immediate halt. This is an extreme form of pause – the system stops itself to prevent damage. |
| **Exit** | ✅ | Zero‑Value‑on‑Capture: if the device is physically compromised, keys are destroyed (cryptographic erasure) or hardware is physically destroyed (thermite). In normal operation, authorised administrators can extract data via escrow keys. |
| **Recoverability** | ✅ | RAUC A/B updates with automatic rollback. Enterprise configuration includes key escrow for full recovery. |
| **Visibility** | ⚠️ | The platform is proprietary, but its architecture is documented in a Security Whitepaper; users can verify integrity via remote attestation (mTLS + TPM). |
| **External Dependencies** | ✅ | No cloud dependencies. All models are pre‑loaded, updates are offline. |

## Configuration (Minimal)
Example deployment (simplified):
```yaml
# docker-compose.yml (if using TactiQ OS in generic mode)
services:
  tactiq-agent:
    image: tactiq/agent:latest
    environment:
      - VERIFIER_URL=https://verifier.local
      - DEVICE_ID=unit-001
    volumes:
      - /dev/tpm0:/dev/tpm0
