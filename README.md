# The Autonomous Stack (TAS)

**Eight questions that reveal who controls your infrastructure.**

You switched from Google Drive to Syncthing. Good. But your DNS still goes through Cloudflare, your containers pull from Docker Hub, and your reverse proxy renews certs from Let's Encrypt. The dependency didn't disappear — it moved.

TAS gives you a way to see this clearly.

---

## The test

Three structural questions — can you control it?

| # | Question | What it tests |
|---|----------|---------------|
| 1 | **Pause** | Can you stop it without losing anything? |
| 2 | **Exit** | Can you leave and take all your data? |
| 3 | **Recover** | If something breaks, can you go back? |

If all three are "yes" — you're in control. If not — you know exactly where the dependency is.

Five more diagnostic questions reveal what's pulling at you: personalisation, urgency, hidden costs, transparency fragility, and trajectory.

**→ [Take the test (30 seconds)](https://revenue7-eng.github.io/the-autonomous-stack/test.html)**

---

## What's inside

**[Recommended Stack](https://revenue7-eng.github.io/the-autonomous-stack/docs/recommended-stack.html)** — one recommendation per need. VPN, passwords, photos, email, monitoring — 27 best-in-class picks, all A3/T2.

**[Technology Catalog](https://revenue7-eng.github.io/the-autonomous-stack/docs/catalog/)** — 73 technologies evaluated on two axes: Autonomy (A0–A3) and Transparency (T0–T2). Includes both autonomous alternatives and the mainstream services they replace.

**[Recipes](https://revenue7-eng.github.io/the-autonomous-stack/docs/recipes/)** — six deployment guides:
- [Minimal Autonomous Server](https://revenue7-eng.github.io/the-autonomous-stack/docs/recipes/minimal-server.html) — the foundation
- [Family Cloud](https://revenue7-eng.github.io/the-autonomous-stack/docs/recipes/family-cloud.html) — replace Google Photos + Drive + passwords
- [Monitoring Stack](https://revenue7-eng.github.io/the-autonomous-stack/docs/recipes/monitoring-stack.html) — Prometheus + Grafana + Loki + Uptime Kuma
- [Communication Server](https://revenue7-eng.github.io/the-autonomous-stack/docs/recipes/communication-server.html) — self-hosted email + Matrix messaging
- [Privacy-First Homelab](https://revenue7-eng.github.io/the-autonomous-stack/docs/recipes/privacy-first-homelab.html)
- [Developer Workstation](https://revenue7-eng.github.io/the-autonomous-stack/docs/recipes/developer-workstation.html)

**[Dependency Graph](https://revenue7-eng.github.io/the-autonomous-stack/docs/dependency-graph.html)** — interactive map of how 73 technologies depend on each other.

**[Autonomy Map](https://revenue7-eng.github.io/the-autonomous-stack/docs/autonomy-map.html)** — star chart: every technology plotted by autonomy × transparency.

---

## Quick example

Instead of:

| Need | Closed (A0) | Autonomous (A3) |
|------|------------|-----------------|
| File sync | Google Drive | **Syncthing** |
| Photos | Google Photos | **Immich** |
| Passwords | 1Password | **Vaultwarden** |
| Email | Gmail | **Stalwart** |
| Messaging | Slack | **Matrix / Element** |
| DNS filtering | NextDNS | **AdGuard Home** |
| VPN | Tailscale | **WireGuard** |

Every switch: A0 → A3. Full pause, exit, and recoverability.

---

## Quick deploy

```bash
cd code/minimal-server
cp .env.example .env
# Edit .env with your secrets
docker compose up -d
```

---

## How it works

Adding a technology to the catalog is one file:

```yaml
# docs/catalog/example.md
title: "Example"
category: "network/vpn"
autonomy_level: "A3"
transparency_level: "T2"
trajectory: "stable"
```

Push → GitHub Action automatically updates the catalog index, audit page, visual map, dependency graph, and all technology counts. Zero manual maintenance.

---

## Self-assessment

TAS evaluates itself: **A2/T2**. Code and content are fully open (MIT + CC BY-SA 4.0). But the site depends on GitHub Pages and the CI/CD runs on GitHub Actions. [Our own card](https://revenue7-eng.github.io/the-autonomous-stack/docs/catalog/the-autonomous-stack.html) documents this honestly and outlines a path to A3.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

- **Code**: [MIT](LICENSE)
- **Documentation**: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
