---
title: "Home"
layout: home
nav_order: 1
---

# The Autonomous Stack (TAS)

**A decision framework for building infrastructure you actually control.**

If your system requires an external account to function --- you don't control it.
If it can't be stopped, exited, or recovered --- you're renting, not owning.

TAS provides:

- An **[Infrastructure Audit](docs/how-to-choose.md)** --- eight questions to evaluate any technology or your entire stack
- A **[Technology Catalog](docs/catalog/)** --- tools rated by Autonomy (A0--A3) and Transparency (T0--T2), from Google Drive to WireGuard
- **[Recipes](docs/recipes/)** --- tested deployments you can clone and run

---

## Quick start

**Evaluate your stack:**
→ [Infrastructure Audit](docs/how-to-choose.md) --- 8 questions, 15 minutes per service

**Choose a tool:**
→ [Technology Catalog](docs/catalog/) --- 20+ tools rated across the full A0--A3 spectrum

**Build from scratch:**
→ [Minimal Autonomous Server](docs/recipes/minimal-server.md) --- VPN, DNS, auth, sync, backups, monitoring, media, Git

**Deploy immediately:**
```bash
cd code/minimal-server
cp .env.example .env
# Edit .env with your secrets
docker compose up -d
```

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

The catalog includes both autonomous alternatives and the mainstream services they replace. The contrast makes the trade-offs visible.

→ Full catalog: [Technology Catalog](docs/catalog/)

---

## Philosophy

TAS is built on the [whose.world](https://whose.world) framework.

The core idea: every digital environment is an architecture built by someone. An **open-mode architecture** contains pauses, allows exit, and survives scrutiny. A **closed-mode architecture** removes pauses, punishes exit, and depends on your inability to see how it works.

The eight questions are a practical translation of this philosophy into infrastructure decisions.

→ [Philosophy](docs/philosophy.md)

---

## Contributing

We welcome contributions --- new technology cards, recipes, corrections, translations.

→ [Contributing guide](CONTRIBUTING.md)

---

## License

- **Code** (scripts, docker-compose, etc.): [MIT](LICENSE)
- **Documentation** (text, assessments, etc.): [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

---

## Credits

TAS applies the philosophical framework of [whose.world](https://whose.world) to infrastructure decisions. The eight audit questions are derived from whose.world's ethics of open-mode architecture.

If you use TAS, please link back to both projects.
