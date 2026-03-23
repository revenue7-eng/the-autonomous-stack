---
title: "Technology Name"
category: "category/subcategory"
status: "stable | experimental"
license: "-"
source: "-"
repository: "-"
documentation: "-"
docker_image: "-"
community: "-"
autonomy_level: "A0"
transparency_level: "T0"
---

# Technology Name

## Brief Description

One or two sentences explaining what the technology does.

## Architectural Role

Where does it fit in the autonomous stack? (e.g., operating system, VPN, media server, backup, identity provider)

## Technical Autonomy

- [ ] Works without internet
- [ ] Stores data locally
- [ ] Does not require external accounts
- [ ] Allows data export
- [ ] Provides offline updates

## Philosophical Assessment (whose.world criteria)

| Criterion             | Status        | Comments                                                                 |
|-----------------------|--------------|--------------------------------------------------------------------------|
| Pause                 | ✅ / ⚠️ / ❌ | Does the system offer built‑in stopping mechanisms or safe shutdown?     |
| Exit                  | ✅ / ⚠️ / ❌ | Can the user leave with all data (export, deletion, migration)?          |
| Recoverability        | ✅ / ⚠️ / ❌ | Are backups and rollbacks supported and documented?                      |
| Visibility            | ✅ / ⚠️ / ❌ | Is the architecture/code/docs open enough to inspect how it works?       |
| External Dependencies | ✅ / ⚠️ / ❌ | Can it run without mandatory third‑party cloud services or accounts?     |

**Explanation of ratings**

- ✅ fully meets the criterion  
- ⚠️ partially meets or requires configuration  
- ❌ does not meet

## Configuration (Minimal)

A minimal configuration example (e.g., `docker run` or `docker-compose.yml` snippet) or link to a code sample.

## Related Recipes

Links to recipes that use this technology, for example:

* [Minimal Autonomous Server](../recipes/minimal-server.md)

## Alternatives

List other technologies that serve a similar purpose.

## Trajectory *(optional — include when there's a meaningful story)*

Where is this project heading? Toward openness (better export, community governance, permissive licensing) or toward closure (license restrictions, cloud dependencies, corporate control)?

Signs to look for: license changes, acquisition, feature gating (community vs enterprise), API restrictions, community governance changes.

Rate as: **opening**, **stable**, **mixed**, **closing**.

## Sources

* Website  
* Documentation  
* Repository  
* Docker image  
* Community  
