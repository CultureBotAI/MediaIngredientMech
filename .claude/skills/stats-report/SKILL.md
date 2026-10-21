---
name: stats-report
description: "Generate reproducible corpus, source, grounding, and data-quality statistics from the current MediaIngredientMech corpus."
category: reporting
requires_database: false
requires_internet: false
version: 1.0.0
tags: [reporting, statistics, metrics, corpus]
---

# Statistics report

Use this skill for current MediaIngredientMech repository counts, README statistics,
publication summaries, or before/after measurements for an import or curation
batch.

## Commands

```bash
just sync-curated
just export-indexes
just export-lists
just export-browser
just validate-strict
just qc
```

- Run `just sync-curated` (`scripts/aggregate_records.py` + `scripts/export_individual_records.py`) first so `data/curated/mapped_ingredients.yaml` and `data/curated/unmapped_ingredients.yaml` match `data/ingredients/mapped/` and `data/ingredients/unmapped/`.
- Run `just export-indexes` (`uv run python scripts/generate_index_files.py`) to compute and write current mapped/unmapped record totals, ontology namespace breakdowns, and occurrence summaries into `data/curated/MAPPED_INGREDIENTS.md`, `data/curated/UNMAPPED_INGREDIENTS.md`, `data/curated/ALL_INGREDIENTS.md`, and `data/curated/all_ingredients_index.json`.
- Run `just export-lists` (`uv run python scripts/export_lists.py`) and `just export-browser` (`uv run python scripts/browser_export.py`) to refresh `docs/data/all_ingredients.csv`, `docs/data/label_index.csv`, and `docs/data/ingredients.json`.
- Note: `just report` (`uv run python scripts/generate_report.py`) invokes `src/mediaingredientmech/export/report_generator.py`, which reads legacy pre-migration collection keys (`mapped_ingredients` / `unmapped_ingredients`) rather than the current `ingredients:` key in `data/curated/` and writes untracked `docs/curation_report.md` / `docs/curation_report.json` (`<!-- refcheck: ignore -->`). Use `just export-indexes`, `just export-lists`, and `just qc` for live corpus statistics.

Never copy a hardcoded record count from skill prose: always derive counts at
run time because the corpus changes continuously.

## Verification

- Record the exact command and git commit used for published figures.
- Do not hand-edit generated statistics tables or JSON/Markdown reports and present them as a fresh run.
- Run `just validate-strict` and `just qc` alongside reporting commands when summarizing corpus health.
