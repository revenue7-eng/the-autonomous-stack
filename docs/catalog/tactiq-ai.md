---
title: "TactiQ AI Platform"
category: "applications/edge-ai"
status: "stable"
license: "Proprietary (Perpetual)"
source: "https://tactiqedge.com"
repository: "-"
documentation: "https://tactiqedge.com/docs"
docker_image: "https://hub.docker.com/r/tactiqedge/tactiq-ai"
community: "-"
autonomy_level: "A2"
transparency_level: "T1"
parent: Catalog
nav_order: 14
---

# TactiQ AI Platform

## Brief Description

A hardened edge‑AI platform that operates completely offline, with zero‑value‑on‑capture security. Designed for critical infrastructure, defence, and remote sites.  

## Architectural Role

Edge AI layer: provides autonomous video analytics, anomaly detection, and sensor fusion without cloud connectivity.

## Technical Autonomy

- Works without internet (12+ months)
- Stores data locally (encrypted, TPM-protected)
- Does not require external accounts
- Allows data export (via escrow keys in Enterprise config)
- Provides offline updates (RAUC A/B, USB/SD)

## Philosophical Assessment (whose.world criteria)

| Criterion              | Status  | Comments                                                                |
|-----------------------|---------|-------------------------------------------------------------------------|
| Pause                 | Yes     | The system implements fail-closed: any anomaly triggers immediate halt. |
| Exit                  | Yes     | Zero-Value-on-Capture: if compromised, keys are destroyed.              |
| Recoverability        | Yes     | RAUC A/B updates with automatic rollback.                               |
| Visibility            | Partial | Proprietary, but documented; supports remote attestation.               |
| External Dependencies | Yes     | No cloud dependencies; fully offline capable.                           |

## Configuration (Minimal)

Example deployment (simplified):

    services:
      tactiq-agent:
        image: tactiq/agent:latest
        environment:
          - VERIFIER_URL=https://verifier.local
          - DEVICE_ID=unit-001
        volumes:
          - /dev/tpm0:/dev/tpm0

Full hardware deployment requires a TactiQ Box or Edge module.

## Related Recipes

- [Minimal Autonomous Server](../recipes/minimal-server.md) – includes basic edge-AI integration.

## Alternatives

- Siemens MindSphere – cloud-dependent, SaaS model
- Hikvision Edge AI – limited offline capability
- NVIDIA Jetson + Balena – less hardened, no built-in zero-value protection

## Sources

- Website
https://tactiqedge.com

- Documentation
https://tactiqedge.com/docs

- Repository

- Docker image
https://hub.docker.com/r/tactiqedge/tactiq-ai

- Community
