---
nav_exclude: false
title: "CrowdSec"
category: "security"
status: "stable"
license: "MIT"
source: "https://crowdsec.net"
repository: "https://github.com/crowdsecurity/crowdsec"
documentation: "https://docs.crowdsec.net"
docker_image: "https://hub.docker.com/r/crowdsecurity/crowdsec"
community: "https://discord.gg/crowdsec"
autonomy_level: "A2"
transparency_level: "T2"
depends_on: []
optional_deps: ["docker"]
depended_by: []
critical_criteria: ["Exit", "External Dependencies"]
trajectory: "mixed"
parent: Technology Catalog
nav_order: 99
---

# CrowdSec

> **TAS Score: S2/3 — D4/5** — A2 / T2
> S2 not S3: fully autonomous local detection is possible, but the core value proposition — the crowdsourced IP reputation blocklist — requires internet connectivity and sharing data with CrowdSec's central API (Q3). D4 not D5: premium blocklists and console features are gated behind paid plans (Q8).
> **Critical criteria for this category:** Exit, External Dependencies.


## Brief Description

Open-source intrusion detection and prevention system with crowdsourced threat intelligence. Analyzes logs to detect malicious behavior (brute force, port scans, web attacks), blocks threats via remediation components, and shares intelligence with a global community network.

## Architectural Role

Security layer: sits alongside your services, reading their logs to detect attacks. Remediation components (bouncers) block threats at various levels — firewall, reverse proxy, or application. The optional cloud API provides a shared blocklist of known malicious IPs.

## Technical Autonomy

- ✅ Works without internet (local detection and blocking via LAPI mode)
- ✅ Stores data locally (decisions, alerts, configuration)
- ⚠️ Core value requires internet (crowdsourced blocklist needs connection to CrowdSec CAPI)
- ✅ Allows data export (configuration is YAML, decisions exportable)
- ✅ Provides offline updates (manual binary or Docker image replacement)

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status  | Comments |
| --------------------- | ------- | -------- |
| Pause                 | Yes     | Service can be stopped. Existing firewall rules persist until manually cleared. |
| Exit                  | Partial | Local detection rules are portable YAML. But the crowdsourced blocklist is proprietary — leaving CrowdSec means losing shared intelligence. |
| Recoverability        | Yes     | Configuration and local decisions can be backed up. |
| Visibility            | Yes     | Security Engine is MIT licensed, fully auditable. Scenarios on Hub are MIT. |
| External Dependencies | Partial | Local detection is fully autonomous. Crowdsourced blocklist and Console require CrowdSec's cloud infrastructure. |

## Configuration (Minimal)

```yaml
services:
  crowdsec:
    image: crowdsecurity/crowdsec:latest
    container_name: crowdsec
    ports:
      - "8080:8080"
      - "6060:6060"
    volumes:
      - ./config/crowdsec:/etc/crowdsec
      - ./data/crowdsec:/var/lib/crowdsec/data
      - /var/log:/var/log:ro
    environment:
      COLLECTIONS: "crowdsecurity/linux crowdsecurity/nginx"
    restart: unless-stopped
```

## Alternatives

* Fail2Ban — predecessor, Python-based, simpler but slower and less scalable
* OSSEC / Wazuh — full HIDS with log analysis, more complex
* Suricata — network-level IDS/IPS, different approach (packet inspection vs log analysis)
* pfSense / OPNsense — firewall-based IDS via Suricata/Snort integration

---

## Trajectory

**Direction: mixed.**

CrowdSec Security Engine is MIT licensed and actively developed. The core detection and local blocking are fully open source. However, the company is building a paid ecosystem around the open-source core: premium blocklists, Console features, and enterprise support tiers. The crowdsourced model inherently creates a dependency on CrowdSec's infrastructure.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | MIT for Security Engine and Hub scenarios; unchanged. |
| Feature gating | ⚠️ | Premium blocklists, advanced Console features, and priority support behind paid plans. |
| Self-hosting | ➖ | Engine is fully self-hostable. But full value requires CAPI connection — by design. |
| Governance | ➖ | Corporate-controlled; open source contributions accepted but roadmap is commercial. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

* [Website](https://crowdsec.net)
* [Documentation](https://docs.crowdsec.net)
* [Repository](https://github.com/crowdsecurity/crowdsec)
* [Docker image](https://hub.docker.com/r/crowdsecurity/crowdsec)
* [Community Discord](https://discord.gg/crowdsec)
