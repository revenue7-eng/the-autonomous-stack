# Contributing to TAS

Thank you for your interest! TAS is a community‑driven project. All contributions are welcome – from fixing typos to adding new technology cards or recipes.

## How to Contribute

1. **Fork** the repository.
2. **Create a branch** with a descriptive name (`add-card-jellyfin`, `fix-typo-philosophy`).
3. **Make your changes** following the guidelines below.
4. **Submit a pull request** and describe what you changed.

## Adding a Technology Card

1. Copy `docs/catalog/template-card.md` to `docs/catalog/your-technology.md`.
2. Fill in all sections.
3. For the **Philosophical Assessment**, be honest and cite sources if possible. If a criterion is ambiguous, explain in the Comments column.
4. Add a link to the official documentation or source code.

## Adding a Recipe

1. Create a new file in `docs/recipes/` (e.g., `my-recipe.md`).
2. Follow the structure:
   - **Title** and brief description
   - **Goal**: what problem it solves
   - **Components**: list of technologies used (link to their cards)
   - **Step‑by‑step instructions**
   - **Verification**: how to test it works
   - **Links to related cards**
3. If you include code (docker‑compose, scripts), place them in `code/` and reference them.

## Philosophy Alignment

When evaluating a technology, use the three ethical criteria from whose.world:
- **Pause**: can the user stop?
- **Exit**: can the user leave with their data?
- **Recoverability**: can the system be restored?

These are not absolute judgments – they help architects make informed choices.

## Style

- Use British English (or consistent American) – we are flexible, but keep the same style within a document.
- Use clear, simple language; avoid marketing hype.
- Include links to primary sources when possible.

## Questions?

Open an issue or reach out via the project's communication channels.

Thank you for helping build a more autonomous digital world!