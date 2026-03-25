---
title: "Home"
layout: home
nav_order: 1
---

# The Autonomous Stack (TAS)

**Three questions that reveal who controls your infrastructure.**

If your system requires an external account to function --- you don't control it.
If it can't be stopped, exited, or recovered --- you're renting, not owning.

**→ [Does your infrastructure pass the TAS test?](docs/test.html)** — 30 seconds, no account needed.

---

## Start here

→ [Infrastructure Audit](docs/how-to-choose.md) --- evaluate your stack. Eight questions, 15 minutes per service.

→ [Technology Catalog](docs/catalog/) --- choose a tool. 20+ technologies rated A0--A3.

→ [Minimal Autonomous Server](docs/recipes/minimal-server.md) --- build from scratch. VPN, DNS, auth, sync, backups, monitoring, media, Git.

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

→ Full framework: [Infrastructure Audit](docs/how-to-choose.md)

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

→ Full catalog: [Technology Catalog](docs/catalog/)

---

## Philosophy

TAS is built on the [whose.world](https://whose.world) framework.

Every digital environment is an architecture built by someone. An **open-mode architecture** contains pauses, allows exit, and survives scrutiny. A **closed-mode architecture** removes pauses, punishes exit, and depends on your inability to see how it works.

The eight questions are a practical translation of this philosophy into infrastructure decisions.

→ [Philosophy](docs/philosophy.md)

---

## License

- **Code**: [MIT](LICENSE)
- **Documentation**: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

TAS applies the philosophical framework of [whose.world](https://whose.world) to infrastructure decisions. If you use TAS, please link back to both projects.
