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

## Relationship with whose.world Criteria

The whose.world framework defines four operational rights:

- **Pause** – ability to stop the system at any moment.  
- **Exit** – ability to leave with all your data.  
- **Recoverability** – ability to roll back to a previous state.  
- **Visibility** – ability to inspect how the system works.  

These criteria feed into the Autonomy and Transparency levels:

- **Autonomy** is directly influenced by Pause, Exit, and Recoverability.  
- **Transparency** is closely linked to Visibility.  

Together, they form a holistic picture of technological sovereignty.

