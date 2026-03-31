---
title: TAS Roadmap
layout: default
---

**Version:** 2.0
**Date:** March 2026
**Status:** Active

---

## Where TAS stands now

TAS has 122 technology cards across 12 categories, 9 deployment recipes (from Minimal Server to GrapheneOS Mobile Stack), a formal assessment model (Assessment Criteria v1.1), a 30-second public test (/test.html), four pilot validations with counterarguments, a dependency graph, an autonomy map, and a card builder for community submissions.

The model works. Signal went from A3 to A2 when we tightened criteria. Nextcloud scores A3 with a D4 diagnostic flag. Every score has a one-line gap explanation. The scoring is reproducible — that was the goal.

---

## Principle: Core First, Scale Second

Features that make TAS bigger are only valuable if the core is trustworthy.

**Core = unassailable.** Every card has a complete TAS Score. Every assessment is reproducible. Trajectory is becoming a signal, not an opinion.

**Scale = multiplier.** Community contributions, external validations, distribution — these amplify a strong core. They cannot fix a weak one.

---

## What's done

These items from the original roadmap are complete:

| Item | Status | Notes |
|------|--------|-------|
| Catalog: 40+ technologies | ✅ Done | 122 cards, 12 categories |
| /test page (viral entry point) | ✅ Done | 30 seconds, 3 questions, share button |
| Assessment Criteria formalization | ✅ Done | v1.1 with 10 structural + 5 diagnostic checks |
| Dependency graph visualization | ✅ Done | Auto-generated from frontmatter |
| Autonomy Map | ✅ Done | Interactive SVG, 12 constellations, trajectory colors |
| Card Builder | ✅ Done | Community submissions without GitHub |
| Validate the Model page | ✅ Done | 4 pilot assessments, open invitation |
| Recipes expanded | ✅ Done | 9 recipes including Mobile Stack |
| TAS Score gap explanation | ✅ Done | One line per card |
| Dependency frontmatter | ✅ Done | `depends_on` / `depended_by` in cards |
| Recommended Stack page | ✅ Done | Visual landing with recipe cards |
| Mobile Apps page | ✅ Done | GrapheneOS + app recommendations |

---

## Priority 1 — Fix what's broken

*These create wrong impressions right now.*

### 1.1 Catalog Index vs. navigation mismatch

**Problem:** The sidebar navigation shows ~96 cards. The Autonomy Map and main page claim 122. The Catalog Index page shows a different subset. Three different numbers for the same catalog.

**Impact:** An attentive reader notices the mismatch and questions accuracy — exactly what TAS can't afford.

**Solution:** Ensure the GitHub Action that generates `catalog/index.md` also feeds the sidebar navigation data, or collapse navigation to point to Catalog Index only (instead of listing every card in the sidebar).

**Effort:** Low-medium. Debugging the Action + Jekyll nav config.

---

### 1.2 Sidebar navigation overload

**Problem:** 96+ card links in the sidebar make it unusable. The nav is longer than most pages.

**Solution:** Collapse the Technology Catalog sidebar to show only category groupings or top-level link to Catalog Index. Individual cards are discoverable through Catalog Index filters, Autonomy Map, and search.

**Effort:** Low. Jekyll `_data/navigation.yml` or frontmatter `nav_exclude`.

---

## Priority 2 — Strengthen the core

*These make TAS more credible.*

### 2.1 Formalize Trajectory Signals

**Current state:** Trajectory is rated as opening / stable / mixed / closing — but based on judgment.

**Solution:** Define 4 measurable signals:

1. **License change** — has the license become more restrictive in the last 3 years?
2. **Feature gating** — have features moved from community to paid tier?
3. **Self-hosting friction** — have new versions introduced cloud dependencies?
4. **Governance concentration** — single maintainer? declining community contribution?

Each signal: ✅ (opening) / ➖ (neutral) / ⚠️ (closing). Auditable, disputable.

**Effort:** Medium. Update template-card.md + retroactively apply.

---

### 2.2 Add Failure Modes to Recipes

**Problem:** Recipes show how to build but not what breaks.

**Solution:** Add a `## Failure Modes` section to every recipe — component, failure, impact, recovery.

**Effort:** Medium. Requires thinking through each recipe's critical path.

---

### 2.3 Context Weights by Category

**Problem:** Pause is more critical for a security camera than a media server.

**Solution:** One line per card: `Critical criteria: Pause, Exit` — marking which structural questions matter most for this category. Does not change the score. Adds context.

**Effort:** Very low.

---

## Priority 3 — Community and peer review

*These matter once external attention arrives.*

### 3.1 First external validation

The Validate the Model page invites independent assessments. Zero external submissions so far. The first one carries disproportionate weight.

**Action:** When publishing on HN or Reddit, frame the ask as "try to break our scores" — not "check out our project." Disagreement is more valuable than agreement.

---

### 3.2 Peer review process for contributions

**Mechanism:**

- Card Builder and GitHub Issues as contribution entry points (already exist)
- PR review checklist: complete TAS Score? Trajectory signals? Dependency fields?
- Every external assessment published — whether it agrees or not

**Why it matters:** At 122 cards, the catalog is large enough that unchecked growth turns assessments into opinions.

---

### 3.3 Trajectory tracking over time

**Mechanism:** `trajectory_history` array in frontmatter — date, event, signal direction. Turns Trajectory from a snapshot into a living record.

---

## Priority 4 — Distribution

*After Priority 1 is fixed.*

### 4.1 Hacker News

Post: "Show HN: Three questions that reveal who controls your infrastructure"
Entry point: /test.html → Validate the Model → Catalog.
Timing: After nav mismatch is fixed.

### 4.2 r/selfhosted

Different framing: practical, recipe-first.
Entry point: Minimal Autonomous Server recipe.
Post link in first comment (low karma account).

### 4.3 awesome-selfhosted

Submit TAS as a meta-resource. The catalog evaluates what awesome-selfhosted lists.

### 4.4 Хабр

Use existing Russian-language material. Practical tone, no philosophy in the headline.

---

## What we are not building (now)

| Item | Why not now |
|------|------------|
| 1-click deploy | Needs failure modes in recipes first |
| API for catalog data | Schema is stable enough, but audience isn't there yet |
| Localization (full RU) | After EN content is stable. Хабр post can use existing material |
| Mobile app | Not in scope. Web-first |
| Economic model / monetization | Premature. Need users first |
| TAS-specific domain | Reserved (miri.life purchased). Acquire when ready |

---

## Definition of Done for Priority 1

- [ ] Sidebar nav, Catalog Index, Autonomy Map, and main page all show the same card count
- [ ] Sidebar navigation is collapsed (cards not individually listed)
- [ ] ROADMAP.md reflects actual project state (this document)

---

*The goal is not a bigger catalog. The goal is a more trustworthy one.*
