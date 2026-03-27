---
parent: "Technology Catalog"
nav_order: 99
title: "1Password"
category: "security/passwords"
status: "stable"
license: "Proprietary"
source: "-"
repository: "-"
documentation: "https://support.1password.com"
docker_image: "-"
community: "-"
autonomy_level: "A0"
transparency_level: "T0"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Pause", "Exit", "External Dependencies"]
---

# 1Password

> **TAS Score: S0/3 — D1/5 · A0 / T0**
> _(S0: cannot pause, exit cleanly, or recover independently — all data on 1Password servers. D1: fully proprietary, no self-hosting, trajectory closing, hidden cost of vendor lock-in.)_

## Why it's in the catalog

1Password is one of the most widely used password managers. It is included as an anti-example — to make the trade-offs visible when choosing between a convenient cloud service and a self-hosted alternative.

## Brief Description

Cloud-based password manager with polished clients for all platforms. Strong UX, team sharing, Travel Mode. No self-hosting option — all vault data is stored on 1Password's servers.

## Architectural Role

Cannot be self-hosted. Operates entirely on 1Password's infrastructure. Clients sync through 1Password's servers on every device.

## Technical Autonomy

- [ ] Works without internet (read-only cache only)
- [ ] Stores data locally
- [ ] Does not require external accounts
- [x] Allows data export (1PUX, CSV — limited)
- [ ] Provides offline updates

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status | Comments |
|-----------------------|--------|----------|
| Pause                 | ❌     | Stopping subscription locks vault access |
| Exit                  | ⚠️     | Export exists but 1PUX format requires conversion; attachments not exported |
| Recoverability        | ❌     | Recovery depends entirely on 1Password's infrastructure |
| Visibility            | ❌     | Fully proprietary; no code to inspect |
| External Dependencies | ❌     | 100% dependent on 1Password servers |

## Autonomous Alternatives

| Alternative | Autonomy | Notes |
|-------------|----------|-------|
| [Vaultwarden](vaultwarden.md) | A3 / T2 | Self-hosted Bitwarden-compatible server; MIT |
| [Bitwarden](bitwarden.md) | A3 / T2 | Official self-hosted server; AGPL-3.0 |
| [KeePass](keepass.md) | A3 / T2 | Local-only; no server needed |

---

## Trajectory

**Direction: closing**

1Password has moved steadily toward deeper cloud integration. The product requires an active subscription to access the vault — there is no perpetual license or local-only mode. The company raised $620M in 2021 and is focused on enterprise B2B growth. Individual users are a declining priority. The 1PUX export format is proprietary and requires tooling to convert.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ⚠️ | Proprietary; subscription required; no perpetual option |
| Feature gating | ⚠️ | Team/Business features behind higher-tier subscriptions |
| Self-hosting | ⚠️ | No self-hosting path exists or is planned |
| Governance | ⚠️ | VC-backed ($620M raised 2021); enterprise B2B pivot |

---

## Sources

- **Website:** https://1password.com
- **Documentation:** https://support.1password.com
- **Community:** https://1password.community
