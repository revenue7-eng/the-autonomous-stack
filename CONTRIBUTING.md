# Contributing to TAS

Thank you for your interest. TAS is a community‑driven project. All contributions are welcome — from fixing typos to adding technology cards, recipes, or translations.

---

## How to contribute

1. **Fork** the repository.
2. **Create a branch** with a descriptive name (`add-card-nextcloud`, `fix-syncthing-config`, `recipe-homelab-nas`).
3. **Make your changes** following the guidelines below.
4. **Submit a pull request** and describe what you changed.

---

## Adding a technology card

1. Copy `docs/catalog/template-card.md` to `docs/catalog/your-technology.md`.
2. Fill in all sections.
3. Assign an **Autonomy Level** (A0–A3) based on the three structural questions from the [Infrastructure Audit](docs/how-to-choose.md): Pause, Exit, Recoverability.
4. Assign a **Transparency Level** (T0–T2) based on source code availability.
5. For the **Philosophical Assessment**, be honest. If a criterion is ambiguous, explain in the Comments column.
6. Include a **Trajectory** section if the project has a meaningful history — license changes, acquisitions, shifts toward or away from openness. Rate as: opening, stable, mixed, or closing. If there's nothing notable to say, omit the section.
7. Add a link to the official documentation or source code.
8. Update `docs/catalog/index.md` to include your card in the appropriate category table.

### Anti‑examples welcome

TAS includes cards for closed‑mode technologies (Google Drive, Notion, Plex) alongside autonomous alternatives. The contrast is the point. If you want to add a card for a mainstream service with an honest assessment, that's valuable.

For anti‑example cards, include a **"Why it's in the catalog"** section explaining the trade‑offs, and an **"Autonomous alternatives"** section pointing to open‑mode options.

---

## Adding a recipe

1. Create a new file in `docs/recipes/` (e.g., `homelab-nas.md`).
2. Follow this structure:
   - **Title** and brief description
   - **Goal**: what problem it solves
   - **Components**: list of technologies used (link to their catalog cards)
   - **Step‑by‑step instructions**
   - **Verification**: how to test it works — including Pause, Exit, and Recoverability checks
   - **Links to related cards**
3. If you include code (docker‑compose, scripts), place them in `code/your-recipe/` and reference them from the recipe. Don't embed large code blocks in Markdown — link to the real files.

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
- Scripts should be executable (`chmod +x`) and use `set -euo pipefail`.
- Test that `docker compose up -d` works from a clean clone.

---

## The eight questions

When evaluating a technology, use the eight questions from the [Infrastructure Audit](docs/how-to-choose.md):

**Structural (determine A‑level):**
1. **Pause** — can the user stop?
2. **Exit** — can the user leave with their data?
3. **Recoverability** — can the system be restored?

**Diagnostic (reveal hidden forces):**
4. **Personalisation** — does it build a model of the user?
5. **Urgency** — does it manufacture time pressure?
6. **Hidden cost** — what does the user pay besides money?
7. **Transparency fragility** — does its value depend on user ignorance?
8. **Trajectory** — is the project moving toward openness or closure?

For catalog cards, the three structural questions and the Philosophical Assessment table are required. The diagnostic questions inform the Trajectory section and the overall assessment — but don't need to be answered formally in every card.

---

## Style

- Use clear, simple language. Avoid marketing hype.
- British or American English — be consistent within a document.
- Include links to primary sources when possible.
- When making claims about a technology's behaviour (telemetry, data collection, licensing), cite a source.

---

## Questions?

Open an issue or reach out via the project's communication channels.

Thank you for helping build a more autonomous digital world.
