# The Autonomous Stack — Vision

**Version:** 1.0  
**Date:** March 2026  
**Status:** Active

---

## What TAS Is

The Autonomous Stack is a **framework for infrastructure decision-making** — not a catalog of tools, not a platform, not a product.

Its core is a universal test: three questions that reveal whether you control your infrastructure, or your infrastructure controls you.

> **Pause.** Can you stop this system right now without permanent damage?  
> **Exit.** Can you leave and take everything with you?  
> **Recoverability.** If something breaks, can you go back?

These three questions work for any technology: cloud services, self-hosted tools, SaaS, AI products, APIs. They produce a number (0–3), they're understandable by non-engineers, and they're applicable in 10 minutes per service.

The catalog and recipes exist to demonstrate the test in action — not the other way around.

---

## The Problem TAS Solves

Modern infrastructure is full of hidden dependencies. Software running on your hardware may depend on external services for licensing, authentication, updates, or core features. The boundary between "self-hosted" and "cloud-dependent" is blurred.

Engineers discover these dependencies at the worst moment: when a vendor changes a license, when a service goes down, when a DNS misconfiguration silently disables security camera recording during a break-in, when an API is deprecated, or when a company is acquired.

Existing approaches to tool evaluation are fragmented: read reviews, check GitHub stars, ask on Reddit. None of them answer the central question: **if I build on this, will I still be in control in two years?**

TAS gives a systematic answer to that question.

---

## Core Concept: The TAS Test

The test has two layers.

**Structural (determines Autonomy Level A0–A3):**

| # | Question | Tests |
|---|----------|-------|
| 1 | Pause | Can you stop it without permanent damage? |
| 2 | Exit | Can you leave with all your data? |
| 3 | Recoverability | Can you roll back if something breaks? |

**Diagnostic (reveals what the A-level doesn't show):**

| # | Question | Tests |
|---|----------|-------|
| 4 | Personalisation | Does it build a behavioural model of you? |
| 5 | Urgency | Does it manufacture time pressure? |
| 6 | Hidden cost | What do you pay besides money? |
| 7 | Transparency fragility | Does its value depend on your ignorance? |
| 8 | Trajectory | Is it moving toward openness — or away from it? |

The TAS Score for any technology is expressed as **S_/3 — D_/5** (e.g., S3/3 — D4/5). The two-part score matters: a technology can be fully autonomous structurally (S3/3) but have a closing trajectory or aggressive telemetry (D2/5). One number would hide this.

---

## Three Layers

TAS has three layers. Each works independently. Together they form a decision pipeline.

**1. The Test** — the Infrastructure Audit. Eight questions. Apply to any technology. Takes 10 minutes. Produces an A-level (A0–A3), a T-level (T0–T2), and a profile of forces acting on you.

**2. The Catalog** — 27+ technology cards, each evaluated against the test. Includes both autonomous alternatives and the mainstream services they replace. The contrast makes trade-offs visible. Each card shows: TAS Score, Philosophical Assessment, Configuration, Trajectory, Dependencies.

**3. Recipes** — tested configurations combining catalog components into deployable stacks. Every recipe: uses only catalog components with known autonomy ratings, includes a full docker-compose.yml, documents failure modes for each critical component, and is verified against all three structural criteria.

---

## Philosophical Foundation

TAS is built on the [whose.world](https://whose.world) framework.

The key insight: every technology creates a flow. You are either the architect of that flow or a tenant inside someone else's architecture. There is no neutral position.

This is not an argument against cloud services. It is an argument for **conscious choice**. A technology rated A0/T0 is not wrong — it may be the right trade-off. TAS makes the trade-off visible so the choice is intentional.

Two roles define every relationship with infrastructure:

- **Architect** — you see how the system works, you can stop it, you can leave it, you can rebuild it.
- **Tenant** — you operate inside someone else's rules, on someone else's timeline, with someone else's exit terms.

Neither role is absolute. The goal of TAS is not maximum autonomy — it is conscious positioning.

---

## Who TAS Is For

**Primary audience:**
- DevOps engineers evaluating tools for production infrastructure
- CTOs and architects making build-vs-buy decisions
- Self-hosting enthusiasts building their first or tenth stack

**Secondary audience:**
- Open-source maintainers positioning their projects on the autonomy spectrum
- Anyone who has been burned by a vendor: license change, API deprecation, acquisition, paywall

**Not the primary audience (yet):**
- Non-technical users
- Enterprise compliance teams (though the framework applies)

---

## Strategic Direction

**Near-term (Q2 2026):** Strengthen the core. Formalize Trajectory signals. Complete TAS Score across all cards. Add failure modes to recipes. Add dependency fields to card frontmatter. Launch /test as a standalone shareable artifact.

**Medium-term (2026):** Build the network effect. Community card contributions with peer review. Dependency graph visualization. Case studies of real deployments. Integration with awesome-selfhosted and similar indexes.

**Long-term:** Become a reference framework. The goal is for "does this pass the TAS test?" to enter the vocabulary of infrastructure decisions — the same way "is this 12-factor?" or "is this OWASP-compliant?" became standard questions.

---

## What TAS Is Not

- **Not a product.** Nothing to buy. No SaaS. No premium tier.
- **Not a platform.** Does not manage your infrastructure; helps you decide how to build it.
- **Not prescriptive.** Does not tell you what to choose; gives you tools for conscious choice.
- **Not anti-cloud.** Includes cloud services as A0 examples to make contrast visible.
- **Not awesome-selfhosted.** awesome-selfhosted has no position. TAS has one.

---

## The Differentiator

Dozens of "self-hosted tools" lists exist. TAS is not one of them.

The differentiator is the test. A catalog without a test is a list. A test without a catalog is abstract. Together they form something that doesn't exist elsewhere: a systematic, auditable method for evaluating infrastructure autonomy — applied to real tools, producing real numbers, generating deployable configurations.

The catalog is proof that the test works.  
The recipes are proof that the catalog is actionable.  
The test is the thing that travels.

---

*The Autonomous Stack — a foundation for architects of open digital flows.*  
*Each card is a brick. Each recipe is a blueprint. The audit is quality control.*

MIT + CC BY-SA 4.0 · [revenue7-eng.github.io/the-autonomous-stack](https://revenue7-eng.github.io/the-autonomous-stack) · [whose.world](https://whose.world)
