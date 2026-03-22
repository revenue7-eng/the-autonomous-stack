# How to Choose Tools

TAS is not just a catalog.

It is a decision framework for selecting technologies based on autonomy and transparency.

---

## Autonomy Level (A)

- **A0** — requires cloud to function
- **A1** — partially dependent on external services
- **A2** — mostly local, but with some dependencies
- **A3** — fully autonomous, works offline

---

## Transparency Level (T)

- **T0** — closed system, not auditable
- **T1** — partially inspectable
- **T2** — fully open and auditable

---

## Core Rules

### 1. If your system must work offline → use A3

Do not rely on tools that require:
- external APIs
- cloud authentication
- постоянное интернет-соединение

---

### 2. If you care about control → prefer T2

Transparent systems allow:
- auditing
- modification
- long-term reliability

---

### 3. Avoid hidden dependencies

Be careful with tools that require:
- mandatory accounts
- SaaS backends
- telemetry that cannot be disabled

---

## Example

Instead of:

- Google Drive (A0)

Use:

- Syncthing (A3)

---

## Trade-offs

Higher autonomy usually means:
- more manual setup
- less convenience
- fewer “plug-and-play” features

TAS makes these trade-offs explicit so you can choose consciously.

---

## Guiding Principle

If you cannot run it, stop it, or recover it — you do not control it.
