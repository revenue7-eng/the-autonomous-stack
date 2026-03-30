---
title: "Assessment Criteria (Formal)"
parent: Technology Catalog
nav_order: 2
---

# Assessment Criteria — Formal Specification

This document defines the **testable criteria** behind every TAS score. Two independent evaluators following this checklist should arrive at the same rating.

If they don't — the checklist needs fixing, not the evaluators.

---

## Design Principle

Every criterion is a **yes/no question about an observable fact**, not an opinion. "Can you stop it?" is vague. "Does the service continue to function after `docker stop`?" is testable.

---

## Autonomy Level (A0–A3)

### Structural Criteria

Each criterion is answered **Yes**, **No**, or **Partial** (with mandatory explanation).

#### S1: Pause

> If you stop the software right now, is your data intact and the service resumable?

| Test | Yes | No |
|------|-----|----|
| Can you stop the process/container without a special shutdown procedure? | Ctrl+C / docker stop works | Requires graceful shutdown sequence or data is lost |
| After stopping, is all data still on disk in a readable state? | Files/DB intact | Data in memory only, or cloud-only |
| Can you restart and continue where you left off? | Works after restart | Requires re-registration, re-sync, or data is gone |

**Score Yes** if all three tests pass. **Partial** if restart works but requires re-sync. **No** if stopping causes data loss or permanent breakage.

#### S2: Exit

> Can you leave this service and take all your data with you?

| Test | Yes | No |
|------|-----|----|
| Is there a documented export mechanism? | CLI export, API, or standard file format | No export, or "contact support" |
| Does the export include ALL user data? | Messages, settings, history, media — everything | Only partial (e.g., can export contacts but not messages) |
| Is the export in a standard, reusable format? | JSON, CSV, SQL dump, standard media files, OPML, VCF, CalDAV | Proprietary format that only this service can read |
| Can another tool import the exported data? | At least one alternative exists that can use the export | Export exists but nothing can consume it |

**Score Yes** if all four tests pass. **Partial** if export exists but is incomplete or proprietary format. **No** if no export mechanism exists.

#### S3: Recoverability

> If something goes wrong, can you go back to a previous state?

| Test | Yes | No |
|------|-----|----|
| Does the service support backups (built-in or standard tools)? | Built-in backup, or data stored as files that standard backup tools can copy | No backup mechanism; requires vendor intervention |
| Can you restore from backup to a working state? | Documented restore procedure that has been tested | Backup exists but restore is undocumented or untested |
| Does a restore give you back the SAME state? | All data, settings, and configuration restored | Some data lost (e.g., encryption keys, sessions) |

**Score Yes** if all three pass. **Partial** if backup exists but restore loses some state. **No** if no backup/restore path exists.

### Autonomy Level Determination

| S1 Pause | S2 Exit | S3 Recovery | Level |
|----------|---------|-------------|-------|
| Yes | Yes | Yes | **A3** |
| Yes | Yes | Partial | **A2** |
| Yes | Partial | any | **A2** |
| Partial | any | any | **A1** |
| No | any | any | **A0** |
| any | No | any | **A0** |

**Rule:** No overrides weakest link. If Exit is No, the service is A0 regardless of other answers.

---

## Transparency Level (T0–T2)

| Test | T2 | T1 | T0 |
|------|----|----|-----|
| Is the source code publicly available? | Yes | No | No |
| Is the license OSI-approved? (MIT, Apache-2.0, GPL, AGPL, MPL) | Yes | N/A | N/A |
| Is the architecture publicly documented? | Yes | Yes | No |
| Are there published security audits or whitepapers? | Optional bonus | Yes | No |

**T2** = source code public + OSI-approved license.
**T1** = architecture documented but code closed, OR code available under non-OSI license (BSL, SSPL, Sustainable Use).
**T0** = neither code nor architecture publicly documented.

**Edge cases:**
- BSL-1.1 (HashiCorp Vault, MariaDB BSL fork) → **T1** (not OSI-approved)
- SSPL (MongoDB) → **T1**
- Source-available but "no production use" → **T1**
- AGPL-3.0 → **T2** (it IS OSI-approved)

---

## Diagnostic Score (D1–D5)

Each diagnostic question has **specific observable indicators**. Answer ⚠️ (concern) if ANY indicator is present.

### D1: Personalisation

> Does this service build a behavioural model of you?

| ⚠️ Concern present if: | ✅ Clean if: |
|-------------------------|-------------|
| Collects usage analytics beyond crash reports | No analytics, or opt-in only with no default |
| Has recommendation engine based on behaviour | No recommendations, or purely local |
| Tracks browsing, reading, or viewing patterns | No tracking |
| Requires identity verification (phone number, ID) | Anonymous usage possible |

### D2: Urgency

> Does this service pressure you to act before you're ready?

| ⚠️ Concern present if: | ✅ Clean if: |
|-------------------------|-------------|
| Sends push notifications you didn't explicitly request | Silent by default |
| Has countdown timers or expiring offers | No time pressure |
| Auto-updates without user consent | User controls update timing |
| Requires action within a deadline or data is lost | No deadlines |

### D3: Hidden cost

> What do you pay besides money?

| ⚠️ Concern present if: | ✅ Clean if: |
|-------------------------|-------------|
| Free tier subsidized by advertising | No ads |
| Requires sharing data with third parties | No third-party data sharing |
| Lock-in via proprietary formats or protocols | Standard formats |
| Identity cost: requires real name, phone number, or credit card | Anonymous or pseudonymous use possible |

### D4: Transparency fragility

> Would you still use it if you saw exactly how it works?

| ⚠️ Concern present if: | ✅ Clean if: |
|-------------------------|-------------|
| Business model depends on user not understanding data collection | Business model transparent |
| Dark patterns in UI (e.g., hard-to-find unsubscribe) | UI is straightforward |
| Terms of service contain surprising clauses | ToS is readable and unsurprising |
| Default settings favour the vendor, not the user | Defaults favour user privacy |

### D5: Trajectory

> Is this project moving toward openness — or away from it?

| ⚠️ Concern present if: | ✅ Clean if: |
|-------------------------|-------------|
| License changed to more restrictive in last 3 years | License unchanged or became more permissive |
| Features moved from free to paid tier | All features remain available |
| Self-hosting became harder in recent versions | Self-hosting maintained or improved |
| Governance concentrated (single company, single maintainer) | Community-governed or foundation-backed |

### D-score calculation

Count the number of ⚠️ concerns across D1–D5:

| ⚠️ count | D-score |
|-----------|---------|
| 0 | **D5** |
| 1 | **D4** |
| 2 | **D3** |
| 3 | **D2** |
| 4–5 | **D1** |

---

## Counterarguments (Required)

Every card in the catalog MUST include a **Counterarguments** section listing known challenges to the assigned rating. This is not optional — it is what makes the rating trustworthy.

Format:

```
## Counterarguments

| Claim | Challenge | Resolution |
|-------|-----------|------------|
| A3: fully autonomous | Requires phone number for registration → identity dependency | Accepted limitation. Does not affect Pause/Exit/Recovery. Noted in D3 (hidden cost). |
| T2: open source | Server federation not practically possible | Server code is open source and auditable. Self-hosting is documented but not encouraged. |
```

If there are no counterarguments, the evaluator hasn't looked hard enough.

---

## Reproducibility Test

A TAS rating passes the reproducibility test if:

1. A second evaluator, using only this document and the technology's public documentation, arrives at the **same A-level and T-level**.
2. The D-score may differ by ±1 due to judgment calls on diagnostic questions — this is acceptable.
3. If A or T differs, the **counterarguments section must explain why** the rating was chosen over the alternative.

---

## Version

This is **TAS Assessment Criteria v1.0**.

Changes to this document MUST be versioned. A rating made under v1.0 criteria is valid under v1.0 — it does not automatically change if criteria are updated.
