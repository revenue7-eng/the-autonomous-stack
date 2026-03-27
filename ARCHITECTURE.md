---
layout: default
title: "TAS Architecture"
nav_order: 11
---

**Version:** 1.0  
**Date:** March 2026  
**Status:** Active

This document describes how TAS is structured, how its components relate, and the principles that govern decisions about what to add and what to leave out.

---

## The Three-Layer Model

```
┌─────────────────────────────────────────────┐
│                  THE TEST                    │
│         8 questions · universal              │
│         applies to any technology            │
└──────────────────┬──────────────────────────┘
                   │ produces
┌──────────────────▼──────────────────────────┐
│                THE CATALOG                   │
│       65+ cards · evaluated technologies     │
│       TAS Score · Trajectory · Dependencies  │
└──────────────────┬──────────────────────────┘
                   │ assembles into
┌──────────────────▼──────────────────────────┐
│                 RECIPES                      │
│       tested stacks · deployable configs     │
│       failure modes · verified criteria      │
└─────────────────────────────────────────────┘
```

Each layer is independently useful. The Test works without the Catalog. The Catalog works without Recipes. Recipes reference the Catalog but can be followed without reading every card.

Together they form a decision pipeline: evaluate → choose → deploy.

---

## Layer 1: The Test

### Structure

Eight questions in two groups:

**Structural (→ Autonomy Level A0–A3)**

These are necessary conditions. A system that fails all three is a system you don't control.

| # | Name | Question |
|---|------|----------|
| 1 | Pause | Can you stop this service right now without permanent damage? |
| 2 | Exit | Can you leave and take everything with you? |
| 3 | Recoverability | If something breaks, can you go back? |

Scoring: each Yes = +1. Total → A-level (0=A0, 1=A1, 2=A2, 3=A3).

**Diagnostic (→ profile beyond A-level)**

These reveal forces that structural criteria don't capture. A system can be A3 and still erode autonomy through data collection, artificial urgency, hidden costs, or a closing trajectory.

| # | Name | Question |
|---|------|----------|
| 4 | Personalisation | Does it build a behavioural model of you? |
| 5 | Urgency | Does it manufacture time pressure? |
| 6 | Hidden cost | What do you pay besides money? |
| 7 | Transparency fragility | Does its value depend on your ignorance? |
| 8 | Trajectory | Is it moving toward openness or away from it? |

Scoring: each clean = +1. Total → D-level (0–5).

### TAS Score Format

```
S_/3 — D_/5    e.g. S3/3 — D4/5
```

The score is always two-part. A single number loses critical information:  
- S3/3 — D1/5: structurally autonomous, but aggressive telemetry + closing trajectory  
- S1/3 — D5/5: cloud-dependent, but fully transparent and opening trajectory (e.g. Tailscale)

**Score gap explanation** (required in every card):  
When S < 3 or D < 5, the card must include one sentence explaining the deduction.  
Example: `D4 (not D5): optional telemetry enabled by default (Q4).`

### Transparency Level (T0–T2)

Independent of the A-level. Determined by source code availability:

| Level | Meaning |
|-------|---------|
| T0 | Closed — no source code, no internal documentation |
| T1 | Documented — architecture public, source closed |
| T2 | Open-source — OSI-approved license, fully auditable |

The full card label is always: **S_/3 — D_/5 · A_ / T_**

---

## Layer 2: The Catalog

### Card Structure

Every card is a Markdown file with YAML frontmatter. Fields:

**Frontmatter (required):**
```yaml
title: "Technology Name"
category: "layer/subcategory"        # e.g. network/vpn, storage/backup
status: "stable | experimental"
license: "SPDX identifier"
autonomy_level: "A0 | A1 | A2 | A3"
transparency_level: "T0 | T1 | T2"
depends_on: []                        # runtime dependencies (catalog slugs)
optional_deps: []                     # optional integrations
depended_by: []                       # what uses this
```

**Frontmatter (optional but encouraged):**
```yaml
trajectory_history:
  - date: "YYYY-MM"
    event: "Description of change"
    signal: "opening | neutral | closing"
```

**Body sections (required):**
- Brief Description
- Architectural Role
- Technical Autonomy (checklist)
- Philosophical Assessment (Pause / Exit / Recoverability / Visibility / External Dependencies)
- TAS Score with gap explanation
- Configuration (minimal example)
- Alternatives

**Body sections (required when applicable):**
- Trajectory — with 4 formal signals (see below)
- Why it's in the catalog — for anti-example cards (A0/T0)
- Autonomous Alternatives — for anti-example cards

**Body sections (optional):**
- Related Recipes
- Sources

### Trajectory: Formal Signals

Trajectory is assessed through 4 measurable signals:

| Signal | Opening indicator | Closing indicator |
|--------|-------------------|-------------------|
| **License** | License became more permissive in last 3 years | License became more restrictive (MIT→BSL, Apache→SSPL) |
| **Feature gating** | Community edition gaining features | Features moving to enterprise/paid tier |
| **Self-hosting** | Self-hosting becoming easier, better-documented | Cloud dependencies added, self-hosting made harder |
| **Governance** | Community contributions growing, independent governance | Single maintainer, corporate control increasing, community declining |

Each signal: ✅ opening / ➖ neutral / ⚠️ closing  
Overall rating: **opening** (3–4 opening) / **stable** (mostly neutral) / **mixed** (signals conflict) / **closing** (2+ closing signals)

### Category System

Categories follow a two-level hierarchy: `layer/subcategory`

**Infrastructure layers:**
- `network/` — vpn, dns, proxy
- `identity/` — auth, sso
- `storage/` — backup, sync
- `compute/` — container, orchestration
- `security/` — passwords, secrets
- `observability/` — metrics, dashboards, monitoring
- `applications/` — media, photos, documents, notes, vcs, cloud, automation

### Anti-Example Cards

The catalog deliberately includes closed-mode technologies (Notion, Google Drive, Plex) alongside autonomous alternatives. This is intentional: the contrast makes the trade-off visible and the choice conscious.

Anti-example cards require:
- `## Why it's in the catalog` section
- `## Autonomous Alternatives` section
- Honest assessment — partial credit where partial credit is due (e.g., Notion's export is partial, not absent)

### Critical Criteria by Category

Not all criteria matter equally for all categories. Each card should note which structural criteria are highest-stakes:

| Category | Critical criteria |
|----------|-------------------|
| security/ | Exit, Recoverability (losing passwords = critical failure) |
| storage/ | Exit, Recoverability (data portability is the entire point) |
| network/ | Pause (network disruption cascades to everything) |
| identity/ | Pause, Exit (SSO down = everything down) |
| observability/ | Recoverability (metrics are only valuable if you can audit history) |
| applications/ | Exit (content lock-in is the primary risk) |
| compute/ | Recoverability (container runtime failure cascades) |

This does not change the score. It adds context for decision-making.

---

## Layer 3: Recipes

### What a Recipe Is

A recipe is a tested, deployable configuration that combines catalog components into a working autonomous system. Every recipe:

1. Uses only catalog components with known A/T ratings
2. Documents the autonomy level of the combined stack
3. Includes a complete `docker-compose.yml` with environment variables
4. Provides step-by-step deployment instructions
5. Lists failure modes for each critical component
6. Verifies Pause, Exit, Recoverability at the stack level

### Failure Modes (required)

Every recipe must include a `## Failure Modes` section:

```markdown
## Failure Modes

| Component | Failure scenario | Impact | Recovery procedure |
|-----------|-----------------|--------|--------------------|
| Vaultwarden | DB corruption | All passwords inaccessible | Restore from Kopia backup |
| Traefik | Config syntax error | All services unreachable via domain | Direct IP:PORT access |
| WireGuard | Key mismatch after update | Remote access lost | Local access, regenerate peer config |
```

This section serves two purposes: it forces the recipe author to think through the critical path, and it gives the reader a recovery plan before they need one.

### Recipe Composition Rules

- Every component in a recipe must have a catalog card
- The recipe's overall A-level = the lowest A-level of any required component
- Optional components (e.g., monitoring) are marked as such and don't affect the overall A-level
- Recipes must pass the three structural criteria at the stack level:
  - **Pause:** a `pause-stack.sh` script or equivalent procedure must exist
  - **Exit:** a documented data export path for every stateful component
  - **Recoverability:** a documented restore path from the backup component

---

## Dependency Model

Dependencies between catalog components are tracked in frontmatter and used to:
1. Validate recipe completeness (all dependencies have cards)
2. Auto-generate dependency graph (via GitHub Actions)
3. Assess blast radius of a component failure

### Dependency Types

```yaml
depends_on: ["docker"]           # required at runtime — without this it doesn't work
optional_deps: ["prometheus"]     # integrates if present, works without
depended_by: ["nextcloud"]        # inverse relationship — populated by other cards
```

### Dependency Graph Generation

The `.github/scripts/generate_catalog.py` script is extended to:
1. Parse `depends_on` / `depended_by` from all cards
2. Validate that all referenced slugs exist in the catalog
3. Output a `dependency-graph.json` for visualization

---

## Governance

### Who Can Assess A/T Levels

Anyone. But ratings are:
- Auditable — based on documented criteria, not opinion
- Disputable — via GitHub Issue template "Dispute this A/T level assessment"
- Versioned — changes tracked in git history with rationale in commit message

### Dispute Process

1. Open issue with template: technology name, current rating, proposed rating, evidence (specific signals from the 8 questions)
2. Maintainer or community responds with counter-evidence or accepts
3. If accepted: PR with updated card + updated trajectory_history entry
4. Cards with active disputes are labeled `rating-disputed` until resolved

### Contribution Requirements (checklist for PRs)

New cards must have:
- [ ] Complete frontmatter including `depends_on`
- [ ] TAS Score with gap explanation if S < 3 or D < 5
- [ ] Trajectory with formal signals (4 indicators)
- [ ] At least one configuration example
- [ ] Autonomous alternatives (if anti-example card)
- [ ] Card added to `docs/catalog/index.md`

---

## Site Structure

```
/                       Homepage — entry by use case
/how-to-choose          Infrastructure Audit (8 questions, full text)
/audit.html             Interactive Audit (JavaScript implementation)
/test                   [planned] Standalone /test artifact — shareable
/catalog/               Technology Catalog index
/catalog/[slug]         Individual technology card
/recipes/               Recipes index
/recipes/[name]         Individual recipe
/philosophy             whose.world connection
/community/             Glossary, case studies [planned]
```

### Navigation Principles

- Entry points are use-case based ("I need to evaluate" / "I need to choose" / "I need to build")
- Recipes are first-level navigation — not buried under a parent
- The /test page is designed to work without any other page context — shareable standalone
- Philosophy is available but never mandatory for using the framework

---

## Automation

### GitHub Actions: Catalog Generation

`.github/workflows/generate-catalog.yml` regenerates `docs/catalog/index.md` on push to main.

On push:
1. Parses all `docs/catalog/*.md` frontmatter
2. Rebuilds `docs/catalog/index.md` with current ratings and counts
3. [planned] Validates `depends_on` references
4. [planned] Outputs `dependency-graph.json`

**Important:** This creates merge conflicts when pushing local changes to `index.md` simultaneously. Always `git pull --rebase` before pushing if you've touched catalog files.

---

## Design Principles

**1. The test travels, the catalog stays.**  
The three structural questions should be usable without the catalog or the site. They are the portable artifact. Design every piece of content so the test can be extracted and used independently.

**2. Contrast is the method.**  
The catalog includes closed-mode technologies deliberately. Google Drive next to Syncthing. Notion next to Paperless-ngx. Without the contrast, the test has no proof of concept.

**3. Scores must be auditable.**  
Any rating must be traceable to specific signals. "S2/3 because Exit is partial — export format is proprietary." Not "S2/3 because it feels like A2." Opinions that can't be disputed can't be trusted.

**4. Recipes are architecture documents, not installation guides.**  
The difference: installation guides tell you how to set up. Architecture documents tell you what breaks and why. Failure modes make recipes into architecture documents.

**5. The framework must pass its own test.**  
TAS has a Pause (you can stop using it), an Exit (the content is CC BY-SA 4.0, you can fork it), and Recoverability (git history, forkable). If it failed its own criteria, it would contradict itself.

---

*Architecture is a living document. Update it when structure changes, not when content changes.*
