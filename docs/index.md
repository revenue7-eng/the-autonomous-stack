---
title: "The Autonomous Stack (TAS)"
nav_order: 1
---

# The Autonomous Stack (TAS)

**A decision framework for building cloud-independent systems.**

TAS helps engineers design infrastructure that:
- works without constant internet access
- avoids vendor lock-in
- preserves control over data and execution

---

## What you can do with TAS

- Build a fully local-first stack in a few hours
- Choose tools based on autonomy (A0–A3) and transparency (T0–T2)
- Deploy reproducible infrastructure using recipes

---

## Start here

[Recipes](recipes/) — ready-to-deploy stacks
[Catalog](catalog/) — technologies with ratings
[How to choose tools](how-to-choose/)

---

## Example: Minimal Autonomous Stack

- WireGuard — secure network
- Syncthing — file sync
- Kopia — backups
- Forgejo — git hosting
- Uptime Kuma — monitoring

---

## Core principle

If your system requires an external account to function — you don’t control it.

---

## Structure

```
tas/
├── README.md # this file
├── CONTRIBUTING.md # guidelines for contributors
├── LICENSE # MIT (code) + CC BY-SA 4.0 (docs)
├── docs/
│ ├── index.md # this file
│ ├── getting-started.md # quick start guide
│ ├── philosophy.md # core concepts from whose.world
│ ├── catalog/ # technology cards
│ │ ├── index.md
│ │ └── ...
│ ├── recipes/ # tested builds
│ │ ├── index.md
│ │ └── minimal-server.md
│ └── community/ # case studies, glossary
│ ├── glossary.md
│ └── ...
└── code/ # example scripts & docker-compose files
```

---

## License

- **Code** (scripts, Dockerfiles, etc.): [MIT](../LICENSE)
- **Documentation** (text, diagrams, etc.): [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

---

## Credits

TAS is built on the philosophy of [whose.world](https://whose.world) and is maintained by the TAS community.  

If you use TAS in your work, please link back to both projects.
