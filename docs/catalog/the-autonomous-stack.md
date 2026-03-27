---
nav_exclude: false
title: "The Autonomous Stack (TAS)"
category: "applications/documents"
status: "stable"
license: "MIT / CC BY-SA 4.0"
source: "https://revenue7-eng.github.io/the-autonomous-stack/"
repository: "https://github.com/revenue7-eng/the-autonomous-stack"
documentation: "https://revenue7-eng.github.io/the-autonomous-stack/"
docker_image: "-"
community: "https://github.com/revenue7-eng/the-autonomous-stack/discussions"
autonomy_level: "A2"
transparency_level: "T2"
depends_on: []
optional_deps: []
depended_by: []
critical_criteria: ["Pause", "Exit"]
trajectory: "opening"
parent: Technology Catalog
nav_order: 99
---

# The Autonomous Stack (TAS)

> **TAS Score: S2/3 — D5/5** — A2 / T2
> S2 not S3: code and content are fully open and cloneable (Q1 partial); exit is clean — `git clone` gives you everything (Q2); but recoverability depends on GitHub — if the repo is suspended or GitHub Pages goes down, the live site disappears (Q3). The project cannot currently be paused and resumed independently of GitHub's infrastructure.
> **Critical criteria for this category:** Pause, Exit.

**Why it's in the catalog:** A framework for digital autonomy should evaluate itself by its own criteria. TAS currently depends on GitHub for hosting, CI/CD, and delivery. This card documents that dependency honestly and outlines a path toward A3.


## Brief Description

An open-source decision framework for evaluating and building infrastructure you control. Eight questions, a technology catalog, deployment recipes, and interactive visualizations — all generated from structured data in a single repository.

## Architectural Role

Meta-framework: TAS is not infrastructure you deploy — it is a tool for deciding what infrastructure to deploy. It produces assessments, comparisons, and deployment guides. The project itself runs as a static site on GitHub Pages with GitHub Actions for automation.

## Technical Autonomy

- ✅ All content is open source (MIT for code, CC BY-SA 4.0 for docs)
- ✅ Full data export — `git clone` captures 100% of the project
- ✅ No external accounts required to use the content (read-only)
- ⚠️ Site delivery depends on GitHub Pages — no self-hosted mirror
- ⚠️ CI/CD depends on GitHub Actions — automation breaks without GitHub
- ⚠️ Community interaction depends on GitHub Issues/Discussions

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status  | Comments |
| --------------------- | ------- | -------- |
| Pause                 | Partial | Repository can be cloned and preserved offline. But the live site cannot be paused and resumed independently — it is GitHub Pages or nothing. |
| Exit                  | Yes     | `git clone` gives you everything: content, automation scripts, generated pages. The project is fully portable to any Git host + static site generator. |
| Recoverability        | Partial | Content is recoverable from any clone. But GitHub Actions workflows, Pages configuration, and community history (Issues, Discussions) are not portable. |
| Visibility            | Yes     | Fully open source. Every line of code, every assessment, every automation script is public and auditable. |
| External Dependencies | Partial | GitHub (hosting, CI/CD, Pages, community). Jekyll (static site generator — but replaceable). D3.js via CDN (but could be vendored). |

## Current Dependencies on GitHub

| What | Depends on | Autonomous alternative |
|------|-----------|----------------------|
| Code hosting | GitHub repos | Forgejo, Gitea (self-hosted) |
| Site delivery | GitHub Pages | Self-hosted Caddy/Nginx + static files |
| CI/CD automation | GitHub Actions | Woodpecker CI, Gitea Actions |
| Community | GitHub Issues/Discussions | Matrix, Discourse (self-hosted) |
| Domain | github.io subdomain | Own domain with self-hosted DNS |

## Path to A3

The following steps would move TAS from A2 to A3 — full autonomy:

**Phase 1 — Reduce single point of failure**
- Register a custom domain (e.g. `theautonomousstack.org`)
- Point it at GitHub Pages initially — but the domain is portable
- This decouples identity from hosting

**Phase 2 — Mirror the site**
- Deploy a self-hosted mirror on a VPS (static files + Caddy)
- GitHub Pages remains primary, mirror is fallback
- If GitHub goes down, DNS switch restores the site

**Phase 3 — Self-hosted primary**
- Move CI/CD to Woodpecker CI or Gitea Actions on Forgejo
- Host the site on own infrastructure
- GitHub becomes a mirror, not the primary
- Community moves to self-hosted Discourse or Matrix

**Phase 4 — Full autonomy (A3)**
- All infrastructure self-hosted
- GitHub is one of many mirrors
- No single external dependency can take the project offline
- The framework practices what it preaches

## Alternatives

This is not a tool with alternatives — it is a framework. But alternative approaches to infrastructure evaluation exist:

* awesome-selfhosted — curated list without evaluation framework
* AlternativeTo — crowd-sourced recommendations without autonomy analysis
* PrivacyGuides — privacy-focused recommendations, different evaluation criteria

---

## Trajectory

**Direction: opening.**

TAS is moving toward greater autonomy. The project started on GitHub as a practical choice, and is incrementally reducing its GitHub dependency. Every automation added (generate_all.py, frontmatter-driven generation) makes the project more portable — the same scripts work on any CI system.

**Signal assessment:**

| Signal | Status | Evidence |
|--------|--------|----------|
| License | ✅ | MIT + CC BY-SA 4.0. Maximally permissive for code, copyleft for content. |
| Feature gating | ✅ | No paid tier. Everything is free and open. |
| Self-hosting | ⚠️ | Not yet self-hosted. But all prerequisites for self-hosting exist. |
| Governance | ✅ | Single maintainer (transparent). Community contributions welcome. No corporate control. |

**Signal key:** ✅ opening · ➖ neutral · ⚠️ closing

---

## Sources

* [Website](https://revenue7-eng.github.io/the-autonomous-stack/)
* [Repository](https://github.com/revenue7-eng/the-autonomous-stack)
* [Philosophy](https://whose.world)
