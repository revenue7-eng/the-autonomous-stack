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
nav_order: 10
---

# Vault

> **TAS Score: S3/3 -- D3/5** -- A3 / T2
> D3 (not D5): license changed from MPL-2.0 to BSL 1.1 in 2023 — no longer OSI-approved (Q8 trajectory closing); IBM acquisition adds governance uncertainty (Q8). Community fork OpenBao (MPL-2.0) is the open alternative.


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

In August 2023, HashiCorp changed the license of Vault (and all its products) from MPL‑2.0 to the Business Source License (BSL 1.1). BSL is not an OSI‑approved open‑source license — it prohibits using the software to offer competing commercial services.

This moved Vault from T2 (open source) toward T1 (documented but restricted). The source code is still publicly readable, but the usage rights are narrower. The community responded with OpenBao — an MPL‑2.0 fork maintained by the Linux Foundation.

In 2024, IBM acquired HashiCorp. The long‑term trajectory is uncertain, but the direction — from community‑governed open source to corporate‑controlled source‑available — is clear.

If you choose Vault today, have a migration path to OpenBao. If you're starting fresh, evaluate OpenBao directly.

## Sources

- [Website](https://www.vaultproject.io)

- [Documentation](https://www.vaultproject.io/docs)

- [Repository](https://github.com/hashicorp/vault)

- [Docker image](https://hub.docker.com/r/hashicorp/vault)

- [Community](https://discuss.hashicorp.com/c/vault/)
