---
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
parent: Catalog
nav_order: 10
---

# Vault

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

## Sources

- Website
https://www.vaultproject.io

- Documentation
https://www.vaultproject.io/docs

- Repository
https://github.com/hashicorp/vault

- Docker image
https://hub.docker.com/r/hashicorp/vault

- Community
https://discuss.hashicorp.com/c/vault/
