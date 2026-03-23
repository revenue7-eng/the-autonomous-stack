---
title: "Infrastructure Audit"
nav_order: 3
---

# Infrastructure Audit

Eight questions for evaluating any technology вЂ” or your entire stack.

Three of them are structural: can you stop, leave, and recover? Five are diagnostic: what holds you inside, and where is the system heading?

Together they form a complete assessment derived from the [whose.world](https://whose.world) framework. The first three are necessary conditions for autonomy. The next five reveal the forces that erode it.

---

## How to use this

Pick one service from your stack. Answer all eight questions. It takes ten minutes.

Then do the next service. And the next. By the end you'll have a map вЂ” not just of what you use, but of what uses you.

---

## The three structural questions

These determine whether the system is an openвЂ‘mode or closedвЂ‘mode architecture. A system that fails all three is a system you don't control.

### 1. Pause

**Can you stop this service right now вЂ” and nothing breaks permanently?**

Can you shut it down, inspect it, and restart it? Does it have a safe shutdown procedure? Does stopping it cascade into failures elsewhere? Is there an "off switch" вЂ” or is it always running because it has to be?

A system without pause is a system that doesn't let you look around. It needs your continuous motion.

If stopping the service causes irreversible damage or data loss: **Pause = No.**

### 2. Exit

**Can you leave this service and take everything with you?**

Can you export all your data in a standard, portable format? Can you migrate to an alternative without rebuilding from scratch? What do you lose if you stop using it tomorrow вЂ” data, configuration, identity, integrations? Is there a "delete my account" that actually deletes?

A system without exit is a system that profits from your inability to leave. The higher the cost of leaving, the less free you are вЂ” regardless of how good the service is.

If leaving costs more than it should вЂ” socially, technically, or financially: **Exit = No.**

### 3. Recoverability

**If something goes wrong, can you go back?**

Are there backups? Are they yours вЂ” or the vendor's? Can you restore to a specific point in time? If an update breaks things, can you roll back? If the company behind it disappears, does your data survive?

A system without recoverability makes every action a oneвЂ‘way door. You move forward because you can't go back.

If a failure or a bad update means permanent loss: **Recoverability = No.**

---

## The five diagnostic questions

These reveal forces that are harder to see. A system can pass the three structural questions and still erode your autonomy вЂ” through data collection, artificial pressure, hidden costs, dependence on your ignorance, or a trajectory toward closure.

### 4. Personalisation

**Does this service collect data about you to shape your experience вЂ” or someone else's?**

Telemetry. Usage analytics. Behavioural models. "Recommended for you." "Based on your activity." Every piece of data collected is a model of you that belongs to someone else.

Not all data collection is malicious. Crash reports help fix bugs. Usage metrics help prioritise features. The question is: can you see what's collected? Can you turn it off? And does the service work the same way when you do?

If the service collects behavioural data you can't inspect or disable вЂ” it's building a model of you that you don't own.

*This maps to the personalisation tactic in whose.world: making a designed flow look like your own choice.*

### 5. Urgency

**Does this service pressure you to act before you're ready?**

Forced updates with countdown timers. Expiring trials. "Update now or lose access." "Your plan expires in 3 days." Deprecation notices with tight deadlines.

Urgency disables evaluation. When you feel you must act now, you can't stop to ask whether you should act at all. Legitimate urgency exists вЂ” security patches matter. But manufactured urgency is a design choice that benefits the vendor, not you.

If the service regularly creates time pressure that serves its interests more than yours вЂ” it's using urgency as a retention mechanism.

*This maps to the urgency tactic: artificial scarcity of time that disables reflection.*

### 6. Hidden cost

**What do you pay for this service besides money?**

Time spent learning proprietary workflows that don't transfer. Attention consumed by notifications you didn't ask for. Habits formed around the tool's logic rather than yours. Data that feeds the vendor's AI, advertising, or analytics pipeline. Cognitive load of managing yet another account, yet another password, yet another set of terms you didn't read.

Every service has a visible price and an invisible price. The visible price is on the pricing page. The invisible price is everything else.

List what you pay. Then mark what the vendor never told you about.

*This maps to hidden cost from whose.world's audit of built environments: the price that is paid silently.*

### 7. Transparency fragility

**If you could see everything about how this service works вЂ” would you still use it?**

Imagine full transparency. You see every algorithm, every data flow, every business decision behind the product. Every metric they optimise for. Every tradeвЂ‘off they made. Every way they monetise your presence.

Does the service survive this? Or does its value depend on you not knowing?

A service that survives full transparency is built on genuine value. A service that breaks under transparency is built on your ignorance. The first is openвЂ‘mode. The second is closedвЂ‘mode вЂ” regardless of its license.

This is the hardest question. It separates tools from traps.

*This maps to whose.world's fragility test and dependence on blindness: if your architecture needs someone's ignorance to work, it's structurally unstable.*

### 8. Trajectory

**Where is this project heading вЂ” toward openness or away from it?**

Today's rating is a snapshot. What matters is the direction. A project that's A3/T2 today but trending toward closed licensing is more dangerous than one that's A2/T1 and moving toward openness.

Signs of closing trajectory: license changes from permissive to restrictive (MIT в†’ BSL, Apache в†’ SSPL). Features moving from community to enterprise edition. New cloud dependencies introduced in updates. API restrictions tightening. Community governance giving way to corporate control.

Signs of opening trajectory: code being openвЂ‘sourced. SelfвЂ‘hosting becoming easier. Export tools improving. Community governance strengthening. Vendor lockвЂ‘in being actively reduced.

Read the changelog. Read the license history. Read the community forums. The trajectory tells you where you'll be in two years вЂ” not where you are today.

*This maps to whose.world's two modes of the Architect: every builder is either moving toward open mode (their architecture survives scrutiny) or toward closed mode (their architecture depends on others not seeing). The direction is more important than the current position.*

---

## Scoring

The first three questions give you the Autonomy Level:

| Answers to 1вЂ“3 | Level | Meaning |
|----------------|-------|---------|
| All three = No | **A0** | CloudвЂ‘bound. You're renting. |
| One or two = Yes | **A1вЂ“A2** | Partially autonomous. Dependencies remain. |
| All three = Yes | **A3** | Fully autonomous. You're in control. |

Questions 4вЂ“8 don't change the AвЂ‘level вЂ” they reveal what the AвЂ‘level doesn't show. A service can be A3 and still have aggressive telemetry (4), manufactured urgency (5), hidden costs (6), a fragile transparency model (7), or a closing trajectory (8).

The full picture is: **AвЂ‘level tells you where you stand. Questions 4вЂ“8 tell you what's pulling at you and where you're headed.**

---

## Reading the map

After auditing your stack, you'll see one of these patterns.

**Mostly A3, clean diagnostics.** Your stack is autonomous and the forces acting on it are visible. Maintain it вЂ” backups, updates, monitoring. The risk is not dependency but neglect.

**Mostly A3, but red flags in 4вЂ“8.** Your tools are technically autonomous, but some have aggressive telemetry, closing trajectories, or hidden costs. Watch the trajectory. Have a migration plan for the ones that are moving toward closure.

**Mixed AвЂ‘levels, conscious choice.** Some services are A0/A1, and you know why. You evaluated the tradeвЂ‘off and accepted it. This is fine. The goal is not maximum autonomy вЂ” it's conscious choice.

**Mixed AвЂ‘levels, default choice.** Some services are A0/A1 because nobody asked. This is the most common pattern вЂ” and the most valuable to discover. Not because you need to change everything, but because now you can choose.

---

## AntiвЂ‘patterns

**Hidden dependencies.** Your selfвЂ‘hosted service uses a container image that calls home on startup. Your "offline" tool requires license validation every 30 days. Your "local" database syncs metadata to the vendor's cloud. Audit not just the service вЂ” but what the service depends on.

**Convenience lockвЂ‘in.** The tool is easy to set up but impossible to leave. Data is in a proprietary format. Configuration is tied to the vendor's ecosystem. Migration would take weeks. This is not autonomy вЂ” it's comfort with a lock on the door.

**Security theatre.** EndвЂ‘toвЂ‘end encryption marketed as privacy вЂ” but the vendor holds the keys. "Your data stays on your device" вЂ” but telemetry goes to the cloud. Read the source, not the marketing.

**OpenвЂ‘source theatre.** The code is on GitHub вЂ” but the build requires proprietary tooling. The license is permissive вЂ” but the coordination server is closed. The project accepts PRs вЂ” but core decisions are made behind closed doors. T2 on paper is not T2 in practice.

---

## Next steps

- Browse the [Technology Catalog](catalog/) to find alternatives for services that scored poorly
- Deploy the [Minimal Autonomous Server](recipes/minimal-server.md) as a starting point
- Read the [Assessment Scale](catalog/assessment-scale.md) for detailed level definitions
- Understand the [Philosophy](philosophy.md) behind the eight questions

---

*This audit is itself a designed environment. It has a pause (you can stop at any question), an exit (you don't have to use TAS), and recoverability (you can reвЂ‘evaluate at any time). If it didn't вЂ” it would contradict its own criteria. And if full transparency about how it works would make you stop using it вЂ” it would fail its own seventh question.*

