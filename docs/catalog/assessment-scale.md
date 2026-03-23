# Assessment Scale

All technologies in the catalog are evaluated along two independent dimensions.

---

## Autonomy Level (A0–A3)

Measures **operational independence** from the cloud and the internet.

| Level | Description |
|-------|-------------|
| **A0** | **Cloud‑bound** – requires constant internet connection and external accounts to function. |
| **A1** | **Online‑dependent** – can work offline partially, but still needs occasional external services or authentication. |
| **A2** | **Offline‑capable** – works completely without internet; data stored locally, but may lack built‑in data export or recovery mechanisms. |
| **A3** | **Fully autonomous** – offline‑first, local data storage, full data export, and built‑in pause/exit/recoverability. |

---

## Transparency Level (T0–T2)

Measures **architectural openness** and auditability.

| Level | Description |
|-------|-------------|
| **T0** | **Closed** – no public documentation of internals; source code not available. |
| **T1** | **Documented** – architecture is described in public documents (whitepapers, security guides), but source code may be closed. |
| **T2** | **Open‑source** – source code is publicly available under an OSI‑approved license; fully auditable. |

---

## Relationship with whose.world criteria

The [whose.world](https://whose.world) framework provides the philosophical foundation for TAS. The full [Infrastructure Audit](../how-to-choose.md) applies eight questions to any technology. They map to the scales as follows:

### Three structural questions → Autonomy Level

- **Pause** – can you stop the system at any moment?
- **Exit** – can you leave with all your data?
- **Recoverability** – can you roll back to a previous state?

These three directly determine the A‑level. A system where all three are "yes" is A3. A system where all three are "no" is A0.

### Visibility → Transparency Level

- **Visibility** – can you inspect how the system works?

This determines the T‑level. Open source with an OSI license = T2. Documented but closed = T1. Opaque = T0.

### Five diagnostic questions → beyond A/T

The A/T rating is necessary but not sufficient. Five additional questions reveal forces that the rating alone doesn't capture:

- **Personalisation** – does it build a behavioural model of you?
- **Urgency** – does it manufacture time pressure?
- **Hidden cost** – what do you pay besides money?
- **Transparency fragility** – does its value depend on your ignorance?
- **Trajectory** – is the project moving toward openness or closure?

A tool can be A3/T2 today and still have aggressive telemetry, hidden costs, or a closing trajectory. The A/T rating tells you where the tool stands. The diagnostic questions tell you what's pulling at it — and where it's headed.

Together, they form a complete picture of technological sovereignty.

