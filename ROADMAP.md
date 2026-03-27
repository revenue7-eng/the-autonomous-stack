---
layout: default
title: "TAS Roadmap"
nav_order: 10
---

**Version:** 1.0  
**Date:** March 2026  
**Status:** Active

This roadmap is organized by priority, not by timeline. The core must be solid before scale makes sense.

---

## Principle: Core First, Scale Second

Features that make TAS bigger are only valuable if the core is trustworthy.  
The core is: the test, the cards, the recipes — and the consistency between them.

**Core = unassailable.** Every card must have a complete TAS Score. Every recipe must document failure modes. Trajectory must be a signal, not an opinion.

**Scale = multiplier.** Community contributions, dependency graphs, /test as viral artifact — these amplify a strong core. They cannot fix a weak one.

---

## Priority 1 — Strengthen the Core

*These make TAS credible at any scale.*

### 1.1 Formalize Trajectory Signals

**Current state:** Trajectory is rated as opening / stable / mixed / closing — but based on intuition.  
**Problem:** Subjective ratings can't be audited or disputed.  
**Solution:** Define 4 measurable signals for Trajectory assessment:

1. **License change** — has the license become more restrictive in the last 3 years? (MIT→BSL, Apache→SSPL, etc.)
2. **Feature gating** — have significant features moved from community to enterprise/paid tier?
3. **Self-hosting friction** — have new versions introduced cloud dependencies or made self-hosting harder?
4. **Governance concentration** — is community contribution declining relative to corporate commits? Is there a single maintainer point of failure?

Each signal: ✅ (opening signal) / ➖ (neutral) / ⚠️ (closing signal).  
Trajectory rating = sum of signals. Auditable, disputable, updatable.

**Effort:** Medium. Update template-card.md + retroactively apply to existing cards.

---

### 1.2 Complete TAS Score Across All Cards

**Current state:** Score format S_/3 — D_/5 exists but not consistently explained.  
**Problem:** Reader sees "S3/3 — D4/5" but doesn't know why D is 4 and not 5. The gap is invisible.  
**Solution:** Add one line to every card explaining the score gap:

```
> **TAS Score: S3/3 — D4/5** — A3 / T2
> D4 (not D5): Grafana Labs collects optional telemetry enabled by default (Q4).
```

**Effort:** Low. One line per card. High signal value.

---

### 1.3 Add Failure Modes to Recipes

**Current state:** Recipes show how to build. They don't show what breaks.  
**Problem:** A recipe without failure modes is an instruction, not an architecture document.  
**Solution:** Add a `## Failure Modes` section to every recipe:

```markdown
## Failure Modes

| Component | Failure | Impact | Recovery |
|-----------|---------|--------|----------|
| Vaultwarden | Database corruption | All passwords inaccessible | Restore from Kopia backup |
| Traefik | Config error | All services unreachable via domain | Access directly via IP:PORT |
| AdGuard Home | Service down | DNS resolution fails for all devices | Switch clients to 1.1.1.1 temporarily |
| WireGuard | Key rotation failure | Remote access lost | Physical/local access to regenerate keys |
```

**Effort:** Medium. Requires thinking through each recipe's critical path.

---

### 1.4 Add Dependency Fields to Card Frontmatter

**Current state:** Cards are isolated islands. Dependencies are mentioned in prose, not structured.  
**Problem:** No way to auto-generate dependency relationships or validate recipe completeness.  
**Solution:** Add to frontmatter:

```yaml
depends_on: ["docker", "postgresql"]   # required runtime dependencies
optional_deps: ["prometheus"]           # optional integrations
depended_by: ["nextcloud", "authentik"] # what uses this
```

**Effort:** Low per card, medium total. Unlocks dependency graph visualization later.

---

### 1.5 Context Weights by Category

**Current state:** All 8 questions treated equally across all technologies.  
**Problem:** Pause is more critical for a security camera than a media server. Exit is more critical for a password manager than a DNS filter.  
**Solution:** Add one line to each card: `Critical criteria: Pause, Exit` — marking which structural questions are highest-stakes for this specific category. Does not change the score. Adds context.

**Effort:** Very low. One line in template.

---

## Priority 2 — Create the Viral Entry Point

*This is how TAS spreads beyond its current audience.*

### 2.1 The /test Page

A standalone page. No navigation. No catalog. No philosophy.

**Content:**
- The three questions, large
- Two worked examples (Google Docs: 0/3 vs Syncthing: 3/3)
- A simple form: "Enter a technology name → run the interactive audit"
- One link: "See the full catalog →"

**Why this matters:** This is what gets shared on HN and Reddit. The catalog is for people who stay. The /test page is for people who arrive. It must work without any prior context.

**Effort:** Medium. Design + implementation. Content already exists in how-to-choose.md.

---

### 2.2 One Shareable Tagline

**Current:** "A decision framework for engineers who build systems they actually control."  
**Problem:** Too long. Doesn't travel in a tweet or a Slack message.  
**Candidates:**
- *"Three questions that reveal who controls your infrastructure."*
- *"Pause. Exit. Recoverability. Does your stack pass?"*
- *"The TAS test: does your infrastructure control you?"*

**Decision needed.** Once chosen, apply consistently: README, site header, /test page, social sharing.

---

### 2.3 Recipes to First-Level Navigation

**Current state:** Recipes are buried under a parent nav item.  
**Problem:** The most actionable part of the project is hardest to find.  
**Solution:** Promote Recipes to first-level nav. Add a visual entry on the homepage: "Deploy a complete autonomous stack in 2 hours →".

---

## Priority 3 — Scale the Catalog

*Only after Priority 1 is complete.*

### 3.1 Community Card Contributions with Peer Review

**Mechanism:**
- Template-card.md as the contribution entry point (already exists)
- GitHub Issue template: "I disagree with this A/T level" — for disputing ratings
- PR review checklist: does the card have complete TAS Score explanation? Trajectory signals? Dependency fields?

**Why peer review matters:** Without it, at 200+ cards the catalog becomes opinions, not assessments.

---

### 3.2 Dependency Graph Visualization

**Prerequisite:** 1.4 (dependency frontmatter) must be complete.  
**Output:** Auto-generated graph showing how catalog components relate. Which recipes share components. What breaks if one component fails.

Built from frontmatter via GitHub Actions. No manual maintenance.

---

### 3.3 Trajectory Tracking Over Time

**Mechanism:** Each card stores a `trajectory_history` array in frontmatter:

```yaml
trajectory_history:
  - date: "2021-04"
    event: "License changed from Apache 2.0 to AGPL-3.0"
    signal: "closing"
  - date: "2024-01"
    event: "Grafana OnCall moved to Cloud-only"
    signal: "closing"
```

This turns Trajectory from a static snapshot into a living record.

---

## Priority 4 — Distribution

*After the core is solid and the entry point exists.*

### 4.1 Hacker News Launch

Post: "Show HN: TAS — a framework for evaluating infrastructure autonomy"  
Entry point: /test page, not the catalog.  
Timing: After Priority 1 and 2.1 are complete.

### 4.2 r/selfhosted Post

Different framing: practical, stack-focused, recipe-first.  
Entry point: Minimal Autonomous Server recipe.

### 4.3 awesome-selfhosted Integration

Submit TAS as a meta-resource. The catalog complements awesome-selfhosted — it evaluates what awesome-selfhosted lists.

---

## What We Are Not Building (Now)

| Item | Why not now |
|------|-------------|
| 1-click Deploy button | Needs stable recipes first. Failure modes section is prerequisite. |
| Interactive score calculator | /test page comes first. Calculator is a feature of /test, not standalone. |
| API for catalog data | Needs stable schema. Dependency frontmatter (1.4) must be in place. |
| Localisation (RU) | After EN content is complete and stable. Habrahabr post can use the existing RU vision doc. |
| Mobile app | Not in scope. Web-first. |

---

## Definition of Done for Priority 1

Priority 1 is complete when:
- [ ] All cards have formalized Trajectory signals (4 measurable indicators)
- [ ] All cards have TAS Score gap explanation (1 line per card)
- [ ] All 3 recipes have Failure Modes section
- [ ] All cards have `depends_on` / `depended_by` frontmatter
- [ ] template-card.md updated to reflect all new fields
- [ ] CONTRIBUTING.md updated with new requirements for contributions

---

*The goal is not a bigger catalog. The goal is a more trustworthy one.*
