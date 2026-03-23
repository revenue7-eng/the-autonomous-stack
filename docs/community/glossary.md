---
title: Glossary
parent: Community
nav_order: 100
---

# Glossary

Key terms used in The Autonomous Stack.

---

## A

**Autonomy Level**
A scale (A0–A3) measuring operational independence from cloud and internet.
- **A0** – Cloud‑bound (requires constant internet and external accounts).
- **A1** – Online‑dependent (needs occasional external services).
- **A2** – Offline‑capable (works without internet but may lack full data export or recovery).
- **A3** – Fully autonomous (offline‑first, local data, full pause/exit/recoverability).

---

## C

**Closed‑mode architecture**
A system that removes pauses, makes exit costly, and depends on the user not seeing how it works. If someone inside it gains full visibility, the system is threatened — because its value depends on ignorance. Contrast with *open‑mode architecture*.

---

## E

**Exit**
The ability to leave a system with all your data, identity, and history — without disproportionate cost. One of the three structural criteria. If leaving is punished or impractical, exit does not exist regardless of whether a "delete account" button is present.

---

## H

**Hidden cost**
What a user pays for a service besides money. Time, attention, behavioural data, habits, cognitive load, dependency. One of the five diagnostic questions in the Infrastructure Audit. A service may be free in price and expensive in hidden cost.

---

## I

**Infrastructure Audit**
The core evaluation tool of TAS. Eight questions applied to any technology or stack: three structural (Pause, Exit, Recoverability) and five diagnostic (Personalisation, Urgency, Hidden cost, Transparency fragility, Trajectory). See [Infrastructure Audit](../how-to-choose.md).

---

## O

**Open‑mode architecture**
A system that contains pauses, allows exit, and is recoverable. If someone inside it sees the full architecture, the system is not threatened — because its value does not depend on ignorance. Contrast with *closed‑mode architecture*.

---

## P

**Pause**
The ability to stop a system at any moment — a structural place where movement halts and the user can inspect, reflect, and decide whether to continue. One of the three structural criteria. Not the same as "turning it off" — pause implies the ability to resume without loss.

**Personalisation** *(diagnostic)*
When a service collects behavioural data to shape the user's experience — making a designed flow look like the user's own choice. One of the five diagnostic questions. Not inherently harmful, but becomes a problem when it can't be inspected or disabled.

---

## R

**Recoverability**
The ability to roll back to a previous state. If something breaks, if an update fails, if a mistake is made — can you undo it? One of the three structural criteria. Without recoverability, every action is a one‑way door.

---

## T

**Trajectory**
The direction a project is heading — toward openness (better export, community governance, permissive licensing) or toward closure (license restrictions, cloud dependencies, corporate control). One of the five diagnostic questions. Today's A/T rating is a snapshot; trajectory tells you where you'll be in two years.

**Transparency fragility**
A diagnostic test: if the user could see everything about how a service works — every algorithm, every data flow, every business decision — would they still use it? A service that survives full transparency is built on genuine value. A service that breaks under transparency is built on ignorance. One of the five diagnostic questions.

**Transparency Level**
A scale (T0–T2) measuring architectural openness.
- **T0** – Closed (no public documentation or source code).
- **T1** – Documented (architecture described publicly, source may be closed).
- **T2** – Open‑source (source code available under an OSI‑approved license; fully auditable).

---

## U

**Urgency** *(diagnostic)*
When a service creates artificial time pressure — forced updates, expiring trials, deprecation deadlines — that disables the user's ability to evaluate. One of the five diagnostic questions. Legitimate urgency (security patches) exists; manufactured urgency serves the vendor.

---

## V

**Visibility**
The ability to inspect how a system works. Closely linked to Transparency Level. Full visibility means you can audit the source code, understand the data flows, and verify the claims.

---

## W

**whose.world**
The philosophical framework that underpins TAS. It asks: *Whose flow are you in?* and provides the structural criteria (Pause, Exit, Recoverability, Visibility) and the concepts of open‑mode and closed‑mode architecture. TAS translates this framework into infrastructure decisions.

---

*This glossary expands as the project grows. Contributions welcome.*
