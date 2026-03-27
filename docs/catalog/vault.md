---
tags: [secrets, security, encryption, hashicorp]
title: "Vault"
category: "security/secrets"
status: "stable"
license: "MPL-2.0"
source: "https://www.vaultproject.io"
repository: "https://github.com/hashicorp/vault"
documentation: "https://www.vaultproject.io/docs"
docker_image: "https://hub.docker.com/r/hashicorp/vault"
community: "https://discuss.hashicorp.com/c/vault/"
autonomy_level: "A3"
transparency_level: "T2"
depends_on: ["docker"]
optional_deps: []
depended_by: []
critical_criteria: ["Exit", "Recoverability"]
parent: Technology Catalog
nav_order: 99
---

# Vault

> **TAS Score: S3/3 -- D3/5** -- A3 / T2
> D3 (not D5): license changed from MPL-2.0 to BSL 1.1 in 2023 — no longer OSI-approved (Q8 trajectory closing); IBM acquisition adds governance uncertainty (Q8). Community fork OpenBao (MPL-2.0) is the open alternative.
> **Critical criteria for this category:** Exit, Recoverability.


## Brief Description

Secure, encrypted storage for secrets, API keys, certificates, and other sensitive data. Provides fine‑grained access control, auditing, and dynamic secrets.

---

## Architectural Role

Security layer: centralised secrets management and encryption as a service. Protects infrastructure credentials and ensures secure authentication.

---

## Technical Autonomy

- ✅ Works without internet (after setup; can run in air‑gapped mode)
- ✅ Stores data locally (encrypted storage backend)
- ✅ Does not require external accounts
- ✅ Allows data export (backup of storage backend)
- ✅ Provides offline updates (manual via packages)

---

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
|-----------|--------|----------|
| Pause | Yes | Vault service can be stopped; secrets remain encrypted. |
| Exit | Yes | Storage backend can be copied; no lock‑in. |
| Recoverability | Yes | Full recovery from storage backend backup. |
| Visibility | Yes | Open source, auditable. |
| External Dependencies | Yes | No required cloud services; can run entirely offline. |

---

## Configuration (Minimal)

Development server (for testing):

```bash
vault server -dev
For production, configure file storage backend (example config.hcl):

hcl
storage "file" {
  path = "/opt/vault/data"
}

listener "tcp" {
  address     = "127.0.0.1:8200"
  tls_disable = true
}

api_addr = "http://127.0.0.1:8200"
Start with: vault server -config=config.hcl
```

## Related Recipes

- [Minimal Autonomous Server](../recipes/minimal-server.md) – can be extended with Vault for secrets management.

## Alternatives

- SOPS – simpler, file‑based, no API.

- Sealed Secrets – Kubernetes‑specific.

- Hashicorp Consul – includes key‑value store but not dedicated secrets.

## Trajectory

**Direction: closing.**

In August 2023, HashiCorp changed Vault's licence from MPL-2.0 to BSL 1.1 — not an OSI-approved open-source licence. In 2024, IBM acquired HashiCorp. The community responded with OpenBao (MPL-2.0 fork, Linux Foundation). If starting fresh, evaluate OpenBao directly.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ⚠️ | MPL-2.0 → BSL 1.1 in August 2023. BSL is not OSI-approved; restricts competing commercial use. |
| Feature gating | ⚠️ | Enterprise features (namespaces, HSM support, advanced auth) have always been gated; trend continues. |
| Self-hosting | ➖ | Self-hosting still works; no cloud dependency introduced. |
| Governance | ⚠️ | IBM acquired HashiCorp in 2024; community fork (OpenBao) created in response. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

## Sources

- [Website](https://www.vaultproject.io)

- [Documentation](https://www.vaultproject.io/docs)

- [Repository](https://github.com/hashicorp/vault)

- [Docker image](https://hub.docker.com/r/hashicorp/vault)

- [Community](https://discuss.hashicorp.com/c/vault/)
