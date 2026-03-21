---
title: "Technology Name"
category: "category (os / core / storage / applications / evolution)"
status: "stable | experimental"
license: "license type"
source: "link to repository or website"
---

# Technology Name

## Brief Description
One or two sentences explaining what the technology does.

## Architectural Role
Where does it fit in the autonomous stack? (e.g., operating system, VPN, media server)

## Technical Autonomy
Check each that applies:

- [ ] Works without internet
- [ ] Stores data locally
- [ ] Does not require external accounts
- [ ] Allows data export
- [ ] Provides offline updates

## Philosophical Assessment (whose.world criteria)

| Criterion | Status | Comments |
|-----------|--------|----------|
| **Pause** | ✅ / ⚠️ / ❌ | Does the system offer built‑in stopping mechanisms? (e.g., time limits, end of session, user‑initiated pause). For fail‑closed systems, automatic stop on anomaly also qualifies. |
| **Exit** | ✅ / ⚠️ / ❌ | Can the user delete their account and data without loss? Are there documented export procedures? |
| **Recoverability** | ✅ / ⚠️ / ❌ | Can the system be rolled back to a previous state? Are backups supported? |
| **Visibility** | ✅ / ⚠️ / ❌ | Is the system architecture open (code, documentation)? Can users verify how it works? |
| **External Dependencies** | ✅ / ⚠️ / ❌ | Does the system rely on third‑party cloud services or mandatory external accounts? |

**Explanation of ratings**  
- ✅ fully meets the criterion  
- ⚠️ partially meets or requires configuration  
- ❌ does not meet

## Configuration (Minimal)
A minimal configuration example (e.g., Docker Compose snippet) or link to `/code/`.

## Related Recipes
Links to recipes that use this technology.

## Alternatives
List other technologies that serve a similar purpose.

## Sources
Links to official documentation, source code, etc.