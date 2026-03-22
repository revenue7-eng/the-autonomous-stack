---
title: "The Autonomous Stack (TAS)"
nav_order: 1
---

# The Autonomous Stack (TAS)
*Architectural Guide for Designing Digital Flows*

TAS is a practical guide for architects who build autonomous digital systems.  
It provides a **catalog of technologies**, **tested recipes**, and a **philosophical framework** — all grounded in the ethics of [whose.world](https://whose.world).

---

## Why TAS?

Modern digital environments are often designed as **seamless flows** with hidden costs: you lose the ability to pause, exit, or recover your own data.  
TAS helps you build **sovereign digital flows** — systems that respect three fundamental principles:

- **Pause** – you can stop and reflect at any moment.
- **Exit** – you can leave without losing what is yours.
- **Recoverability** – mistakes can be undone; systems can be restored.

These principles come from the philosophy of *whose.world*, which asks: *Whose flow are you in?*

---

## Who Is This For?

- **Architects** designing edge, cloud‑agnostic, or self‑hosted infrastructures.
- **DevOps engineers** who want to understand the ethical implications of their choices.
- **Security professionals** looking for “zero‑value‑on‑capture” solutions.
- **Self‑hosting enthusiasts** seeking full data sovereignty.

---

## How to Use This Guide

- **To understand the philosophy** → read [Philosophy](philosophy.md).
- **To pick a technology** → browse the [Technology Catalog](catalog/).
- **To build a complete system** → follow a [Recipe](recipes/).
- **To contribute** → see [Contributing](../CONTRIBUTING.md).

---

## Structure

tas/
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── docs/
│ ├── index.md (this page)
│ ├── philosophy.md
│ ├── catalog/
│ │ ├── index.md
│ │ └── ... (technology cards)
│ ├── recipes/
│ │ ├── index.md
│ │ └── minimal-server.md
│ └── community/
│ ├── index.md
│ └── glossary.md (coming soon)
└── code/

---

## License

- **Code** (scripts, Dockerfiles, etc.): [MIT](../LICENSE)
- **Documentation** (text, diagrams, etc.): [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

---

## Credits

TAS is built on the philosophy of [whose.world](https://whose.world) and is maintained by the TAS community.  
If you use TAS in your work, please link back to both projects.
