---
title: "Assessment Scale"
parent: Technology Catalog
nav_order: 1
---

# Assessment Scale

All technologies in the catalog are evaluated along two independent dimensions.

---

## Autonomy Level (A0--A3)

Measures **operational independence** from the cloud and the internet.

| Level | Description |
|-------|-------------|
| **A0** | **Cloud-bound** -- requires constant internet connection and external accounts to function. |
| **A1** | **Online-dependent** -- can work offline partially, but still needs occasional external services or authentication. |
| **A2** | **Offline-capable** -- works completely without internet; data stored locally, but may lack built-in data export or recovery mechanisms. |
| **A3** | **Fully autonomous** -- offline-first, local data storage, full data export, and built-in pause/exit/recoverability. |

---

## Transparency Level (T0--T2)

Measures **architectural openness** and auditability.

| Level | Description |
|-------|-------------|
| **T0** | **Closed** -- no public documentation of internals; source code not available. |
| **T1** | **Documented** -- architecture is described in public documents (whitepapers, security guides), but source code may be closed. |
| **T2** | **Open-source** -- source code is publicly available under an OSI-approved license; fully auditable. |

---

## Relationship with whose.world criteria

The [whose.world](https://whose.world) framework provides the philosophical foundation for TAS. The full [Infrastructure Audit](../how-to-choose.md) applies eight questions to any technology. They map to the scales as follows:

### Three structural questions -- Autonomy Level

- **Pause** -- can you stop the system at any moment?
- **Exit** -- can you leave with all your data?
- **Recoverability** -- can you roll back to a previous state?

These three directly determine the A-level. A system where all three are "yes" is A3. A system where all three are "no" is A0.

### Visibility -- Transparency Level

- **Visibility** -- can you inspect how the system works?

This determines the T-level. Open source with an OSI license = T2. Documented but closed = T1. Opaque = T0.

### Five diagnostic questions -- beyond A/T

The A/T rating is necessary but not sufficient. Five additional questions reveal forces that the rating alone doesn't capture:

- **Personalisation** -- does it build a behavioural model of you?
- **Urgency** -- does it manufacture time pressure?
- **Hidden cost** -- what do you pay besides money?
- **Transparency fragility** -- does its value depend on your ignorance?
- **Trajectory** -- is the project moving toward openness or closure?

A tool can be A3/T2 today and still have aggressive telemetry, hidden costs, or a closing trajectory. The A/T rating tells you where the tool stands. The diagnostic questions tell you what's pulling at it -- and where it's headed.

Together, they form a complete picture of technological sovereignty.

---

## How to score — step by step

### Step 1: Determine A level (structural questions)

Answer the three structural questions. Use this table:

| Pause | Exit | Recoverability | A level |
|-------|------|----------------|---------|
| ✅ yes | ✅ yes | ✅ yes | **A3** |
| ✅ yes | ✅ yes | ⚠️ partial | **A2** |
| ✅ yes | ⚠️ partial | ⚠️ partial | **A2** |
| ✅ yes | ❌ no | any | **A1** |
| ⚠️ partial | any | any | **A1** |
| ❌ no | any | any | **A0** |

**Rule:** the weakest answer dominates. If Exit is ❌, the tool is A0 or A1 regardless of the other answers.

---

### Step 2: Determine T level (transparency)

| Source code | License | T level |
|-------------|---------|---------|
| Public, OSI-approved license | MIT, Apache, GPL, AGPL, MPL... | **T2** |
| Architecture documented, code closed | Whitepaper, security audits published | **T1** |
| Closed, no public documentation | Proprietary, no auditable information | **T0** |

**Note:** BSL (Business Source License) is NOT OSI-approved → T1, not T2.

---

### Step 3: Determine D score (diagnostic questions)

Each of the five diagnostic questions is answered ✅ (clean) or ⚠️ (concern):

| Question | ✅ clean | ⚠️ concern |
|----------|----------|------------|
| Personalisation | No behavioural profiling | Builds user model, telemetry |
| Urgency | No artificial pressure | Countdown timers, forced upgrades |
| Hidden cost | No non-monetary costs | Privacy, attention, lock-in |
| Transparency fragility | Value survives full visibility | Value depends on user ignorance |
| Trajectory | Moving toward openness | License changes, feature gating, cloud push |

Count the ⚠️ concerns:

| ⚠️ concerns | D score | Trajectory |
|-------------|---------|------------|
| 0 | D5 | opening |
| 1 | D4 | stable |
| 2 | D3 | mixed |
| 3 | D2 | closing |
| 4–5 | D1 | closing |

---

### Step 4: Write the TAS Score

Format: **S_/3 — D_/5 · A_ / T_**

Example: `S3/3 — D4/5 · A3 / T2`

- **S** = structural score = number of ✅ among the 3 structural questions
- **D** = diagnostic score = 5 minus number of ⚠️ concerns
- **A** = autonomy level from Step 1
- **T** = transparency level from Step 2

If S=3 and D=5 — no explanation needed.
If S<3 or D<5 — always explain which question caused the deduction.

---

### Worked example: PhotoPrism

**Structural:**
- Pause ✅ — can be stopped cleanly
- Exit ✅ — original files remain untouched
- Recoverability ✅ — standard backup applies

→ S3/3 · **A3**

**Transparency:**
- AGPL-3.0, fully open source

→ **T2**

**Diagnostic:**
- Personalisation ✅ — no behavioural profiling
- Urgency ✅ — no artificial pressure
- Hidden cost ✅ — no non-monetary costs
- Transparency fragility ✅ — value survives full visibility
- Trajectory ⚠️ — PhotoPrism+ is a paid closed tier; some features gated

→ D4/5 · **mixed**

**Final: S3/3 — D4/5 · A3 / T2 · trajectory: mixed**
