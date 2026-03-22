---
title: "K3s"
category: "compute/orchestration"
status: "stable"
license: "Apache-2.0"
source: "https://k3s.io"
repository: "https://github.com/k3s-io/k3s"
documentation: "https://docs.k3s.io"
docker_image: "-"
community: "https://github.com/k3s-io/k3s/discussions"
autonomy_level: "A3"
transparency_level: "T2"
---

# K3s

## Brief Description

Lightweight certified Kubernetes distribution built for edge, IoT, and resource‑constrained environments. Single binary, low memory footprint, fully offline capable.

---

## Architectural Role

Compute orchestration layer: manages containers across a cluster. Provides scheduling, service discovery, secrets management, and declarative application deployment.

---

## Technical Autonomy

- ✅ Works without internet (after installation and image pull)
- ✅ Stores data locally (etcd, manifests, local storage)
- ✅ Does not require external accounts
- ✅ Allows data export (cluster state can be backed up)
- ✅ Provides offline updates (manual upgrade via script or package)

---

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
|-----------|--------|----------|
| Pause | Yes | Cluster can be stopped (stop the k3s service); workloads can be paused. |
| Exit | Yes | No vendor lock‑in; workloads can be exported or moved to other Kubernetes clusters. |
| Recoverability | Yes | Regular etcd snapshots allow full cluster recovery. |
| Visibility | Yes | Open source, fully transparent. |
| External Dependencies | Yes | No required cloud services; can run in air‑gapped mode. |

---

## Configuration (Minimal)

Single‑node server install (on Debian/Ubuntu):

```bash
curl -sfL https://get.k3s.io | sh -
```

Verify it works offline (after installation and pulling images):

```bash
sudo k3s kubectl get nodes
```

For air‑gapped environments, use the offline installation guide.

## Related Recipes

- [Minimal Autonomous Server](../recipes/minimal-server.md) – can be extended with K3s for full orchestration.

## Alternatives

- K0s – another lightweight Kubernetes distribution.
- MicroK8s – Canonical’s lightweight Kubernetes (requires snap).
- Nomad – HashiCorp orchestrator, simpler but less declarative.

## Sources

- Website
https://k3s.io

- Documentation
https://docs.k3s.io

- Repository
https://github.com/k3s-io/k3s

- Docker image

- Community
https://github.com/k3s-io/k3s/discussions
