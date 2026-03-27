---
title: "Home"
layout: home
nav_order: 1
---

# The Autonomous Stack

**Eight questions that reveal who controls your infrastructure.**

If your infrastructure requires an external account to function --- you don't control it.
If it can't be stopped, exited, or recovered --- you're renting, not owning.

TAS gives you three things: a way to **evaluate** any technology, a **catalog** of evaluated tools, and **recipes** to deploy them.

**→ [Does your infrastructure pass the TAS test?](https://revenue7-eng.github.io/the-autonomous-stack/test.html)** — 30 seconds, no account needed.

**→ [Explore the Autonomy Map](https://revenue7-eng.github.io/the-autonomous-stack/docs/autonomy-map.html)** — 62 technologies, 12 constellations.

---

## What do you need?

### I need to evaluate my current stack

Start with the [Infrastructure Audit](docs/how-to-choose.md). Eight questions --- three structural (can you stop, leave, recover?) and five diagnostic (what holds you inside, where is it heading?). Takes 15 minutes per service. You'll know where you stand.

### I need to choose a specific tool

Browse the [Technology Catalog](docs/catalog/). Each card shows Autonomy Level (A0--A3), Transparency Level (T0--T2), and a detailed assessment against the three criteria.

### I need to build from scratch

Follow the [Minimal Autonomous Server](docs/recipes/minimal-server.md) recipe. A complete stack --- VPN, DNS filtering, identity, file sync, backups, monitoring, media, Git hosting --- deployed in a few hours.

### I want to understand the philosophy behind this

Read [whose.world](https://whose.world). TAS is a practical application of its framework. Or see our [Philosophy](docs/philosophy.md) page for a short bridge.

---

## The eight questions

Three structural --- can you control it?

| # | Question | Tests |
|---|----------|-------|
| 1 | **Pause** | Can you stop it without permanent damage? |
| 2 | **Exit** | Can you leave with all your data? |
| 3 | **Recoverability** | Can you roll back if something breaks? |

Five diagnostic --- what's pulling at you?

| # | Question | Tests |
|---|----------|-------|
| 4 | **Personalisation** | Does it build a behavioural model of you? |
| 5 | **Urgency** | Does it manufacture time pressure? |
| 6 | **Hidden cost** | What do you pay besides money? |
| 7 | **Transparency fragility** | Does its value depend on your ignorance? |
| 8 | **Trajectory** | Is the project moving toward openness --- or closure? |

The first three determine the Autonomy Level. The next five reveal what the rating doesn't show.

Full framework: [Infrastructure Audit](docs/how-to-choose.md)

---

## Autonomy x Transparency

**Autonomy Level** --- how dependent is it on the cloud?

| Level | Meaning |
|-------|---------|
| **A0** | Cloud-bound --- requires constant internet and external accounts |
| **A1** | Online-dependent --- partially offline, but needs external services |
| **A2** | Offline-capable --- works without internet, but may lack full data export |
| **A3** | Fully autonomous --- offline-first, local data, full pause/exit/recoverability |

**Transparency Level** --- can you see how it works?

| Level | Meaning |
|-------|---------|
| **T0** | Closed --- no public documentation, no source code |
| **T1** | Documented --- architecture described publicly, source may be closed |
| **T2** | Open-source --- source code available under an OSI-approved license |

See the full [Assessment Scale](docs/catalog/assessment-scale.md) for details.

---

## Catalog sample

| Technology | Autonomy | Transparency | Category |
|------------|----------|--------------|----------|
| [WireGuard](docs/catalog/wireguard.md) | **A3** | **T2** | VPN |
| [Syncthing](docs/catalog/syncthing.md) | **A3** | **T2** | File sync |
| [Jellyfin](docs/catalog/jellyfin.md) | **A3** | **T2** | Media server |
| [Tailscale](docs/catalog/tailscale.md) | **A2** | **T1** | Mesh VPN |
| [Plex](docs/catalog/plex.md) | **A1** | **T0** | Media server |
| [Notion](docs/catalog/notion.md) | **A0** | **T0** | Documents |
| [Google Drive](docs/catalog/google-drive.md) | **A0** | **T0** | File storage |

Full catalog: [Technology Catalog](docs/catalog/)

---

## Quick deploy
```bash
cd code/minimal-server
cp .env.example .env
# Edit .env with your secrets
docker compose up -d
```

---

## Quick example

Instead of:

| Need | Closed option | Autonomous option |
|------|--------------|-------------------|
| File sync | Google Drive (A0/T0) | Syncthing (A3/T2) |
| Media server | Plex (A1/T0) | Jellyfin (A3/T2) |
| DNS filtering | NextDNS (A0/T1) | AdGuard Home (A3/T2) |
| VPN | Tailscale (A2/T1) | WireGuard (A3/T2) |
| Notes | Notion (A0/T0) | Paperless-ngx (A3/T2) |

Higher autonomy usually means more manual setup and less convenience. TAS makes these trade-offs explicit so you can choose consciously.

---

## Core principle

*If your system requires an external account to function --- you don't control it.*

This framework is built on the philosophy of [whose.world](https://whose.world). The three criteria (Pause, Exit, Recoverability) and five diagnostic questions come from whose.world's ethics of open-mode architecture.

---

## License

- **Code**: [MIT](LICENSE)
- **Documentation**: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
