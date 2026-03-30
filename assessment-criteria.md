---
title: "Assessment Criteria (Formal)"
parent: Technology Catalog
nav_order: 2
---

# Assessment Criteria — Formal Specification

This document defines the **testable criteria** behind every TAS score. Two independent evaluators following this checklist should arrive at the same rating.

If they don't — the checklist needs fixing, not the evaluators.

---

## Design Principles

1. Every criterion is a **yes/no question about an observable fact**, not an opinion.
2. "Partial" is not a judgment call — it is a **defined list of specific cases**.
3. The aggregation table is **mechanical** — no overrides, no "but in context…".
4. Every assessment declares its **evaluation context** — results are only comparable within the same context.

---

## Evaluation Context (Required)

Every assessment MUST declare its context. Assessments are only comparable within the same context.

```
Context:
  deployment: self-hosted / managed-hosted / SaaS
  scale: single-user / team / enterprise
  platform: Docker / bare metal / mobile app / desktop app
```

**Default context** (used when not specified): `self-hosted · single-user · Docker`.

A technology may have different ratings under different contexts. For example, Nextcloud self-hosted is A3; Nextcloud via a hosting provider may be A2 or A1 depending on what the provider controls.

---

## Autonomy Level (A0–A3)

### S1: Pause

> If you stop the software right now, is your data intact and the service resumable?

| # | Test | Yes | No |
|---|------|-----|----|
| 1a | Can you stop the process without a special shutdown procedure? | `Ctrl+C`, `docker stop`, close app — works cleanly | Requires multi-step graceful shutdown or data is corrupted |
| 1b | After stopping, is all user data still on disk? | Data persists in files or database on local storage | Data exists only in memory, or only on a remote server you don't control |
| 1c | Can you restart and continue with the same data? | Restart → same state, no re-registration, no re-download | Requires re-registration, re-authentication with external service, or data is gone |

**Scoring:**

| Result | When |
|--------|------|
| **Yes** | All three (1a, 1b, 1c) pass |
| **Partial-P1**: restart requires re-sync | 1a and 1b pass, but 1c requires re-syncing data from peers/server (data is not lost, but not immediately available) |
| **Partial-P2**: restart requires re-authentication | 1a and 1b pass, but 1c requires re-login to a local account (not an external service) |
| **No** | 1a fails (stopping corrupts data), OR 1b fails (data not on local disk) |

### S2: Exit

> Can you leave this service and take all your data with you?

| # | Test | Yes | No |
|---|------|-----|----|
| 2a | Is there a documented export mechanism? | CLI command, API endpoint, or "copy the files" — documented | No export exists, or only "contact support" |
| 2b | Does the export include ALL user-generated data? | Messages, files, settings, history, media — everything the user created | Some user data is not exportable (e.g., messages exist but can't be exported) |
| 2c | Is the export format documented and non-proprietary? | JSON, CSV, SQL, standard media formats (JPEG, MP4), open standards (CalDAV, VCF, OPML) | Proprietary binary format, or encrypted format only this software can read |
| 2d | Can at least one other tool consume the export? | Another tool/service can import or read the exported data | Export exists but no other tool can use it |

**Scoring:**

| Result | When |
|--------|------|
| **Yes** | All four (2a, 2b, 2c, 2d) pass |
| **Partial-E1**: export exists but format is proprietary | 2a passes, 2b passes, but 2c fails — export is in a format only this software reads |
| **Partial-E2**: export exists but incomplete | 2a passes, but 2b fails — some user data cannot be exported |
| **Partial-E3**: export format is open but no importer exists | 2a, 2b, 2c pass, but 2d fails — format is standard but no alternative tool actually imports it yet |
| **No** | 2a fails — no export mechanism exists |

### S3: Recoverability

> If something goes wrong, can you go back to a previous state?

| # | Test | Yes | No |
|---|------|-----|----|
| 3a | Can the data be backed up with built-in tools or standard file copy? | Built-in backup command, or data is plain files that `cp`/`rsync` can copy | No backup mechanism; requires vendor; data is in opaque internal format |
| 3b | Can you restore from backup to a fully working state? | Documented restore procedure; tested and produces working instance | Backup exists but restore is undocumented, untested, or fails |
| 3c | Does restore give back ALL user data? | All data, settings, configuration. Sessions/tokens regenerated (expected and acceptable). | Some user-created data permanently lost after restore |

**Scoring:**

| Result | When |
|--------|------|
| **Yes** | All three (3a, 3b, 3c) pass |
| **Partial-R1**: backup works but restore loses some settings | 3a passes, 3b passes, but 3c fails — user data is intact but some configuration must be manually recreated |
| **Partial-R2**: backup requires downtime or special mode | 3a requires stopping the service first (not hot-backupable), 3b and 3c pass |
| **No** | 3a fails — no way to back up the data |

---

### Autonomy Level — Aggregation Table

This table is **mechanical**. No overrides. No judgment notes. No "but in context…".

| S1 Pause | S2 Exit | S3 Recovery | Level |
|----------|---------|-------------|-------|
| Yes | Yes | Yes | **A3** |
| Yes | Yes | Partial-R* | **A2** |
| Yes | Partial-E3 | Yes | **A3** |
| Yes | Partial-E3 | Partial-R* | **A2** |
| Yes | Partial-E1 | any | **A2** |
| Yes | Partial-E2 | any | **A2** |
| Partial-P* | Yes | Yes | **A2** |
| Partial-P* | Yes | Partial-R* | **A1** |
| Partial-P* | Partial-E* | any | **A1** |
| No | any | any | **A0** |
| any | No | any | **A0** |

**Reading the table:**

- `Partial-E3` (format is open but no importer) is the mildest Exit limitation — it preserves A3 when combined with Yes on the others, because the data is portable even if no tool imports it yet.
- `Partial-E1` (proprietary format) and `Partial-E2` (incomplete export) are harder limitations — they cap at A2.
- `No` on any criterion is A0. No exceptions.

---

## Transparency Level (T0–T2)

| Test | T2 | T1 | T0 |
|------|----|----|-----|
| Is the source code publicly available? | Yes | No | No |
| Is the license OSI-approved? (MIT, Apache-2.0, GPL, AGPL, MPL) | Yes | N/A | N/A |
| Is the architecture publicly documented? | Yes | Yes | No |

**T2** = source code public + OSI-approved license.
**T1** = architecture documented but code closed, OR code available under non-OSI license (BSL, SSPL, Sustainable Use).
**T0** = neither code nor architecture publicly documented.

**Edge cases:**

- BSL-1.1 → **T1** (not OSI-approved)
- SSPL → **T1**
- Source-available with "no production use" clause → **T1**
- AGPL-3.0 → **T2** (it IS OSI-approved)

---

## Diagnostic Score (D1–D5)

Each diagnostic question has **specific observable indicators**. Answer ⚠️ (concern) if ANY indicator in the list is present.

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

Every card in the catalog MUST include a **Counterarguments** section listing known challenges to the assigned rating. This is not optional.

Format:

```
| Claim | Challenge | Resolution |
|-------|-----------|------------|
| A3 | Requires phone number → identity dependency | Does not affect S1/S2/S3. Captured in D3. |
```

If there are no counterarguments, the evaluator hasn't looked hard enough.

---

## Reproducibility Test

A TAS rating passes the reproducibility test if:

1. A second evaluator, using only this document and the technology's public documentation, arrives at the **same A-level and T-level**.
2. The D-score may differ by ±1 due to judgment calls on diagnostic indicators — this is acceptable.
3. If A or T differs, the difference **must be traceable to a specific test** (e.g., "I scored 2c as No because format X is undocumented; you scored it Yes because parser Y exists").

---

## Changelog

**v1.1** (2025-05)

- Added **Evaluation Context** requirement — every assessment must declare deployment, scale, platform.
- Replaced vague "Partial" with **named sub-cases** (Partial-P1, P2, E1, E2, E3, R1, R2) — each has a specific definition and a deterministic effect on A-level.
- Made aggregation table **mechanical** — removed ability to override with judgment notes. Signal drops from A3 to A2 under v1.1 (S2 = Partial-E1: proprietary backup format).
- Numbered all sub-tests (1a, 1b, 1c, 2a–2d, 3a–3c) for precise reference in disagreements.

**v1.0** (2025-05)

- Initial formal specification.
