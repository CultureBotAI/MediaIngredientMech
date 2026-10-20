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
just report
just qc
```

Run `just report` (`uv run python scripts/generate_report.py`) to compute mapped/unmapped ingredient totals, ontology namespace breakdown, and quality metrics from `data/curated/` and `data/ingredients/`.

Never copy a hardcoded record count from skill prose: always derive counts at
run time because the corpus changes continuously.

## Verification

- Record the exact command and git commit used for published figures.
- Do not hand-edit generated statistics tables or JSON/Markdown reports and present them as a fresh run.
- Run `just validate-strict` alongside reporting commands when summarizing corpus health.
