# Contributing to TAS

Thank you for your interest. TAS is a community-driven project. All contributions are welcome — from fixing typos to adding technology cards, recipes, or translations.

---

## How to contribute

1. **Fork** the repository.
2. **Create a branch** with a descriptive name (`add-card-nextcloud`, `fix-syncthing-config`, `recipe-homelab-nas`).
3. **Make your changes** following the guidelines below.
4. **Submit a pull request** and describe what you changed.

---

## Adding a technology card

### Step-by-step

1. Copy `docs/catalog/template-card.md` to `docs/catalog/your-technology.md`.
2. Fill in the frontmatter — all fields are required. Pay special attention to:
   - `depends_on` — list runtime dependencies using catalog slugs (e.g. `["docker", "postgresql"]`)
   - `optional_deps` — list optional integrations
   - `critical_criteria` — which structural criteria matter most for this category (e.g. `["Exit", "Recoverability"]` for storage tools)
3. Assign an **Autonomy Level** (A0–A3) based on the three structural questions: Pause, Exit, Recoverability.
4. Assign a **Transparency Level** (T0–T2) based on source code availability.
5. Fill in the **TAS Score** (`S_/3 — D_/5`). If S < 3 or D < 5, add one sentence explaining the deduction directly under the score line.
6. Complete the **Philosophical Assessment** table honestly. If a criterion is ambiguous, explain in the Comments column.
7. Complete the **Trajectory** section with all four signal rows (License, Feature gating, Self-hosting, Governance). This is required, not optional.
8. Add your card to `docs/catalog/index.md` in the correct category table.

### Trajectory signals

Trajectory is assessed through four measurable signals. For each, mark:
- ✅ opening signal
- ➖ neutral
- ⚠️ closing signal

| Signal | What to look for |
|--------|-----------------|
| **License** | Has the license changed in the last 3 years? MIT→BSL or Apache→SSPL = closing. Proprietary→open = opening. |
| **Feature gating** | Are significant features moving to enterprise/paid tier? Community edition losing capabilities? |
| **Self-hosting** | Are new versions introducing cloud dependencies? Is self-hosting becoming harder or better documented? |
| **Governance** | Is community contribution declining relative to corporate commits? Single maintainer point of failure? |

Overall direction: **opening** (3–4 opening signals) / **stable** (mostly neutral) / **mixed** (signals conflict) / **closing** (2+ closing signals).

### PR checklist for new cards

Before submitting, verify:

- [ ] Frontmatter complete — all fields filled, `depends_on` populated
- [ ] TAS Score filled with gap explanation if S < 3 or D < 5
- [ ] Trajectory section present with all 4 signal rows completed
- [ ] At least one configuration example (docker-compose snippet or equivalent)
- [ ] Alternatives table has at least one entry
- [ ] Card added to `docs/catalog/index.md` in correct category

For anti-example cards (A0/T0 technologies):
- [ ] `## Why it's in the catalog` section included
- [ ] `## Autonomous Alternatives` section included

### Anti-examples welcome

TAS includes cards for closed-mode technologies (Google Drive, Notion, Plex) alongside autonomous alternatives. The contrast is the point. Honest assessments of mainstream services are valuable.

For anti-example cards, include a **"Why it's in the catalog"** section explaining the trade-offs, and an **"Autonomous Alternatives"** section pointing to open-mode options.

---

## Disputing an A/T level rating

If you believe a technology's Autonomy or Transparency level is incorrect, open an issue using the **"Dispute rating"** template and include:

1. Technology name and current rating
2. Proposed rating
3. Evidence — specific signals from the 8 questions that support your assessment
4. Sources (changelogs, license history, documentation)

Cards with active disputes are labeled `rating-disputed` until resolved. If the dispute is accepted, submit a PR updating the card and adding an entry to `trajectory_history` in the frontmatter.

---

## Adding a recipe

1. Create a new file in `docs/recipes/` (e.g., `homelab-nas.md`).
2. Follow this structure:
   - **Title** and brief description
   - **Goal** — what problem it solves
   - **Components** — list of technologies used (link to their catalog cards)
   - **Step-by-step instructions**
   - **Failure Modes** — required section (see below)
   - **Verification** — how to test Pause, Exit, and Recoverability at the stack level
3. Place code in `code/your-recipe/` and reference it from the recipe.

### Failure Modes section (required)

Every recipe must document what happens when critical components fail:

```markdown
## Failure Modes

| Component | Failure scenario | Impact | Recovery procedure |
|-----------|-----------------|--------|--------------------|
| Vaultwarden | Database corruption | All passwords inaccessible | Restore from Kopia backup — see Recoverability section |
| Traefik | Config syntax error | All services unreachable via domain | Access directly via IP:PORT while fixing config |
| WireGuard | Key mismatch after update | Remote access lost | Requires local/physical access to regenerate peer config |
```

Think through the critical path: what is the blast radius of each component failing? What cascades?

### Recipe autonomy level

A recipe's overall A-level = the lowest A-level of any **required** component. Optional components don't affect the overall level.

---

## Adding or updating code

All deployable code lives in `code/`. Each recipe has its own subdirectory:

```
code/
└── minimal-server/
    ├── docker-compose.yml
    ├── .env.example
    └── scripts/
        ├── pause-stack.sh
        └── resume-stack.sh
```

When adding code:
- Include a `.env.example` with comments explaining each variable.
- Scripts must be executable and use `set -euo pipefail`.
- Test that `docker compose up -d` works from a clean clone.
- Include a `pause-stack.sh` — Pause is a structural criterion, it must be testable.

---

## The eight questions

When evaluating a technology, apply the eight questions from the [Infrastructure Audit](docs/how-to-choose.md):

**Structural (determine A-level):**
1. **Pause** — can you stop it without permanent damage?
2. **Exit** — can you leave with all your data?
3. **Recoverability** — can you restore to a known state?

**Diagnostic (inform TAS Score D-level and Trajectory):**
4. **Personalisation** — does it build a behavioural model of you?
5. **Urgency** — does it manufacture time pressure?
6. **Hidden cost** — what do you pay besides money?
7. **Transparency fragility** — does its value depend on your ignorance?
8. **Trajectory** — is the project moving toward openness or closure?

---

## Style

- Clear, direct language. No marketing hype. No hedging.
- When making claims about a technology's behaviour (telemetry, data collection, licensing), cite a source.
- British or American English — be consistent within a document.
- Honesty over promotion. A partial ⚠️ is more useful than a false ✅.

---

## Questions?

Open an issue. All questions are welcome.

Thank you for helping build a more autonomous digital world.
