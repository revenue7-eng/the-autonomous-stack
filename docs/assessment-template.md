---
nav_exclude: true
title: "Assessment Template"
---

# TAS Assessment Template

Use this template to evaluate any technology against [TAS Assessment Criteria v1.1](catalog/assessment-criteria.md). Copy, fill in, and submit as a PR or GitHub Issue.

---

**Technology:** _[name]_
**Evaluated by:** _[your name or handle]_
**Date:** _[YYYY-MM]_
**Criteria version:** v1.1

---

## S1: Pause

| Test | Result | Evidence |
|------|--------|----------|
| Can you stop the process without a special shutdown procedure? | _Yes / No_ | _[how?]_ |
| After stopping, is all data still on disk in a readable state? | _Yes / No_ | _[where?]_ |
| Can you restart and continue where you left off? | _Yes / No_ | _[any caveats?]_ |

**S1 = _Yes / Partial / No_**

## S2: Exit

| Test | Result | Evidence |
|------|--------|----------|
| Is there a documented export mechanism? | _Yes / No_ | _[what tool/command?]_ |
| Does the export include ALL user data? | _Yes / Partial / No_ | _[what's missing?]_ |
| Is the export in a standard, reusable format? | _Yes / No_ | _[which format?]_ |
| Can another tool import the exported data? | _Yes / No_ | _[which tool?]_ |

**S2 = _Yes / Partial / No_**

## S3: Recoverability

| Test | Result | Evidence |
|------|--------|----------|
| Does the service support backups? | _Yes / No_ | _[built-in or external?]_ |
| Can you restore from backup to a working state? | _Yes / No_ | _[documented?]_ |
| Does a restore give you back the SAME state? | _Yes / Partial / No_ | _[what's lost?]_ |

**S3 = _Yes / Partial / No_**

## Autonomy Level

| S1 | S2 | S3 | Level |
|----|----|----|-------|
| _?_ | _?_ | _?_ | **A_** |

## Transparency Level

| Test | Result | Evidence |
|------|--------|----------|
| Source code publicly available? | _Yes / No_ | _[URL]_ |
| License OSI-approved? | _Yes / No_ | _[which license?]_ |

**T = _T0 / T1 / T2_**

## Diagnostic Score

| # | Question | Result | Evidence |
|---|----------|--------|----------|
| D1 | Personalisation | _✅ / ⚠️_ | _[evidence]_ |
| D2 | Urgency | _✅ / ⚠️_ | _[evidence]_ |
| D3 | Hidden cost | _✅ / ⚠️_ | _[evidence]_ |
| D4 | Transparency fragility | _✅ / ⚠️_ | _[evidence]_ |
| D5 | Trajectory | _✅ / ⚠️_ | _[evidence]_ |

**D-score: D_/5** (_N_ concerns)

## Counterarguments

| Claim | Challenge | Resolution |
|-------|-----------|------------|
| _[your rating]_ | _[why it might be wrong]_ | _[why you chose this rating anyway]_ |

## Final Score

**S_/3 — D_/5 — A_ / T_**

---

_Submit this assessment as a [GitHub Issue](https://github.com/revenue7-eng/the-autonomous-stack/issues/new?labels=independent-assessment) or [Pull Request](https://github.com/revenue7-eng/the-autonomous-stack/pulls)._
