---
title: "The Autonomous Stack"
layout: home
nav_order: 1
---

# The Autonomous Stack

**A decision framework for engineers who build systems they actually control.**

If your infrastructure requires an external account to function — you don't control it.
If it can't be stopped, exited, or recovered — you're renting, not owning.

TAS gives you three things: a way to **evaluate** any technology, a **catalog** of evaluated tools, and **recipes** to deploy them.

---

## Three criteria

Every technology in TAS is evaluated against three questions — derived from the [whose.world](https://whose.world) philosophical framework:

**Pause** — Can you stop the system at any moment? Is there a structural place to halt, inspect, and decide whether to continue?

**Exit** — Can you leave with all your data? Is the cost of leaving proportional, or does the system punish departure?

**Recoverability** — Can you roll back to a previous state? If something breaks, can you undo it?

A system with all three is an **open-mode architecture** — it respects the autonomy of whoever uses it. A system without them is a **closed-mode architecture** — it depends on your inability to leave.

---

## What do you need?

### → I need to evaluate my current stack

Start with the [Infrastructure Audit](how-to-choose.md). Eight questions — three structural (can you stop, leave, recover?) and five diagnostic (what holds you inside, where is it heading?). Takes 15 minutes per service. You'll know where you stand.

### → I need to choose a specific tool

Browse the [Technology Catalog](catalog/). Each card shows Autonomy Level (A0–A3), Transparency Level (T0–T2), and a detailed assessment against the three criteria.

### → I need to build from scratch

Follow the [Minimal Autonomous Server](recipes/minimal-server.md) recipe. A complete stack — VPN, DNS filtering, identity, file sync, backups, monitoring, media, Git hosting — deployed in a few hours.

### → I want to understand the philosophy behind this

Read [whose.world](https://whose.world). TAS is a practical application of its framework. The short version: every digital environment is an architecture built by someone. The question is whether that architecture contains pauses, exits, and recoverability — or whether it's designed to keep you inside without noticing.

---

## Autonomy × Transparency

TAS evaluates technologies along two independent axes:

**Autonomy Level** — how dependent is it on the cloud?

| Level | Meaning |
|-------|---------|
| **A0** | Cloud‑bound — requires constant internet and external accounts |
| **A1** | Online‑dependent — partially offline, but needs external services |
| **A2** | Offline‑capable — works without internet, but may lack full data export |
| **A3** | Fully autonomous — offline‑first, local data, full pause/exit/recoverability |

**Transparency Level** — can you see how it works?

| Level | Meaning |
|-------|---------|
| **T0** | Closed — no public documentation, no source code |
| **T1** | Documented — architecture described publicly, source may be closed |
| **T2** | Open‑source — source code available under an OSI‑approved license |

See the full [Assessment Scale](catalog/assessment-scale.md) for details.

---

## Quick example

Instead of:

| Need | Closed option | Autonomous option |
|------|--------------|-------------------|
| File sync | Google Drive (A0/T0) | Syncthing (A3/T2) |
| Media server | Plex (A1/T0) | Jellyfin (A3/T2) |
| DNS filtering | NextDNS (A0/T1) | AdGuard Home (A3/T2) |
| VPN | Tailscale (A2/T1) | WireGuard (A3/T2) |
| Notes | Notion (A0/T0) | Paperless‑ngx (A3/T2) |

Higher autonomy usually means more manual setup and less convenience. TAS makes these trade‑offs explicit so you can choose consciously.

---

## Structure

```
tas/
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── docs/
│   ├── index.md              ← you are here
│   ├── how-to-choose.md      # infrastructure audit + decision framework
│   ├── philosophy.md          # link to whose.world concepts
│   ├── catalog/               # technology cards (A3 to A0)
│   ├── recipes/               # tested deployments
│   └── community/             # glossary, case studies
└── code/                      # docker-compose files, scripts
    └── minimal-server/
```

---

## License

- **Code**: [MIT](../LICENSE)
- **Documentation**: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

---

## Credits

TAS applies the philosophical framework of [whose.world](https://whose.world) to infrastructure decisions.

The three criteria (Pause, Exit, Recoverability) come from whose.world's ethics of open‑mode architecture. If you use TAS, please link back to both projects.
