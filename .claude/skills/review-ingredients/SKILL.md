---
name: review-ingredients
description: Use this skill to quality-check ontology-mapped MediaIngredientMech ingredient records — verify CHEBI/FOODON/ENVO terms exist and labels match (OAK), enrich chemical properties and synonyms (OLS/OWL), and catch dual-identifier, purity-merge, and kg-microbe-dictionary disagreements. Use after a curation batch, before a KG export, or for periodic maintenance. Issues are graded P1 (blocking) → P4 (optional); P3/P4 can be auto-corrected.
version: 1.1.0
tags: [validation, quality-assurance, ontology, oak, ols, owl, chebi, foodon, envo]
author: MediaIngredientMech Team
created: 2026-03-15
---

# Review Ingredients Skill

## Overview

The **Review Ingredients** skill provides quality assurance for ontology-mapped
ingredients in MediaIngredientMech. It verifies that:

1. **Ontology mappings are correct** — term exists, label matches, definition appropriate
2. **Identifiers are valid** — proper CURIE format, dual identifier system consistency
3. **Synonyms are accurate** — chemical variants preserved, no duplicates
4. **Chemical properties are enriched** — SMILES, InChI, molecular formulas populated
5. **Merge integrity is maintained** — purity-aware merge rules followed

**Technology stack:** OAK (term existence/metadata in CHEBI/FOODON/ENVO), EBI OLS v4
API (formulas, SMILES, InChI, definitions), local OWL files (offline validation +
reasoning), LinkML (YAML structure/constraints).

**Dataset:** ~1,102 ingredients; ~1,034 mapped (93.8%), ~68 intentionally unmappable.

---

## When to Use This Skill

| Scenario | Workflow | Priority |
|----------|----------|----------|
| **Post-curation QA** | Validate newly mapped ingredients before committing | High |
| **Batch validation** | Review all mapped ingredients | High |
| **Pre-export check** | Ensure KG export quality before KG-Microbe ingestion | Critical |
| **Periodic maintenance** | Monthly validation after CultureMech updates | Medium |
| **Synonym verification** | Cross-check synonyms with ontology data | Medium |
| **Chemical enrichment** | Populate SMILES, InChI, formulas from OLS | Low |
| **Duplicate detection** | Find potential merge candidates | Low |

```
IF newly mapped batch → interactive review
IF full dataset check → batch review
IF enrichment needed  → auto-correct (P3/P4)
IF critical errors    → batch review with P1 filter
IF synonym issues     → validate_synonyms.py
```

---

## Review Workflows

### 1. Interactive Review (single ingredient)

Verify a specific ingredient after manual curation.

```bash
# By preferred term / by ontology ID / with fix suggestions
PYTHONPATH=src python scripts/review_ingredient.py "sodium chloride"
PYTHONPATH=src python scripts/review_ingredient.py --id CHEBI:26710
PYTHONPATH=src python scripts/review_ingredient.py "glucose" --suggest-fixes
```

Output: Rich panel with current mapping, P1–P4 validation results, suggested
corrections (apply/skip), and an ontology-metadata comparison.

### 2. Batch Review (all ingredients)

Validate the whole dataset and generate reports.

```bash
PYTHONPATH=src python scripts/batch_review.py \
  --output reports/validation_$(date +%Y%m%d) --format md,json,html --threads 4

PYTHONPATH=src python scripts/batch_review.py --priority P1,P2   # filter by priority
PYTHONPATH=src python scripts/batch_review.py --source CHEBI     # filter by source
PYTHONPATH=src python scripts/batch_review.py --limit 10 --dry-run
```

Output: `validation_report.md`, `validation_data.json`, `dashboard.html`. See
[`reference/api-reference.md`](reference/api-reference.md) for the report formats.

### 3. Automated Correction (P3/P4 safe issues)

Auto-fix issues that don't require human review.

```bash
PYTHONPATH=src python scripts/auto_correct.py --dry-run                          # preview
PYTHONPATH=src python scripts/auto_correct.py --apply                            # all safe
PYTHONPATH=src python scripts/auto_correct.py --apply --types chemical_properties
PYTHONPATH=src python scripts/auto_correct.py --apply --types synonyms
```

**Safe (auto-applied):** enrich chemical properties from OLS, add ontology synonyms,
normalize CURIE formats, fix label whitespace/case.
**Unsafe (manual review):** change ontology ID, modify preferred_term, merge duplicates,
change mapping quality level.

### 4. Claude Code-Assisted Review

```bash
/review-ingredients                              # interactive
/review-ingredients "calcium chloride dihydrate" # specific ingredient
```

Claude loads the YAML record, runs validation via `IngredientReviewer`, explains issues
in plain language, proposes corrections with rationale, applies on approval, and updates
`curation_history`.

---

## Validation Rules

Issues are graded by priority. Full definitions (checks, impact, fix, data sources,
known false-positive patterns) live in
[`reference/validation-rules.md`](reference/validation-rules.md).

| Level | Meaning | Action | Target |
|-------|---------|--------|--------|
| **P1** | Critical errors blocking KG export | Fix immediately | 0 |
| **P2** | High-priority warnings needing review | Manual review | < 5% |
| **P3** | Medium-priority enrichment opportunities | Auto-correct when possible | < 20% |
| **P4** | Low-priority info/suggestions | Optional | Any |

| Rule | Summary |
|------|---------|
| **P1.1** | Ontology term does not exist (404 from OAK/OLS) |
| **P1.2** | Invalid CURIE format (e.g. `CHEBI123` not `CHEBI:123`) |
| **P1.3** | Dual identifier mismatch (`id` vs `identifier`/ontology ID) |
| **P1.4** | Missing required fields (`ontology_id`, `preferred_term`) |
| **P2.1** | Label mismatch (ontology label vs `preferred_term`) |
| **P2.2** | Definition mismatch (semantic) |
| **P2.3** | Deprecated/obsolete ontology term |
| **P2.4** | Purity merge violation (pure/impure merged incorrectly) |
| **P2.5** | kg-microbe unified-dictionary disagreement on a CHEBI mapping |
| **P3.1** | Missing chemical properties (SMILES/InChI/formula) |
| **P3.2** | Missing synonyms present in the ontology |
| **P3.3** | Low-confidence mapping (< 0.7 or PROVISIONAL) |
| **P3.4** | Ambiguous quality level (CLOSE_MATCH without purity/catalog note) |
| **P4.1** | Additional ontology synonyms available |
| **P4.2** | Alternative ontology matches (score > 0.8 elsewhere) |
| **P4.3** | Enrichment opportunities (roles, pathways) |
| **P4.4** | kg-microbe synonyms this record lacks (enrichment candidates) |

> **kg-microbe rules (P2.5, P4.4):** the unified chemical dictionary has documented
> TSV-parse bugs (merged-row pollution, cation/anion contamination). Never treat it as
> authoritative — every proposal is human-verified via OAK round-trip. Loader pattern,
> guards, and known false positives are in
> [`reference/integrations.md`](reference/integrations.md).

---

## Best Practices

### DO ✅

1. **Run batch validation before KG export** — no P1 errors propagate; generates an audit trail.
2. **Use auto-correct for P3/P4 only** — properties enrichment and synonym addition are low-risk; review P1/P2 manually.
3. **Cache OWL files locally** — faster, offline-capable, reproducible.
4. **Track validation history** — add validation events to `curation_history`; monitor trends.
5. **Batch process with checkpoints** — resume on failure; 4–8 threads; rate-limit API calls (0.5–1 s).
6. **Verify corrections before applying** — `--dry-run` first, review the JSON plan, test on a subset.

### DON'T ❌

1. **Don't auto-correct P1/P2** — label mismatches, deprecated terms, and dual-ID issues need judgment.
2. **Don't skip validation for "trusted" sources** — CultureMech imports and expert curations still have errors; ontologies evolve.
3. **Don't over-enrich** — add only synonyms that improve search; avoid IUPAC clutter.
4. **Don't ignore P2 warnings** — they often signal semantic issues or data-integrity loss.
5. **Don't run a full batch without sampling** — test on 10–20 first; check format and performance.
6. **Don't hardcode API endpoints** — use config, support fallbacks, handle version changes.

---

## Reference Files

Deep material is bundled alongside this skill (progressive disclosure — read on demand):

| File | Contents |
|------|----------|
| [`reference/validation-rules.md`](reference/validation-rules.md) | Full P1–P4 rule definitions: checks, impact, fixes, data sources, false-positive patterns |
| [`reference/integrations.md`](reference/integrations.md) | KG-Microbe unified-dictionary integration (loader, guards), OAK lookup patterns, EBI OLS enrichment, OWL file management |
| [`reference/api-reference.md`](reference/api-reference.md) | `IngredientReviewer` class + supporting dataclasses, and the markdown/JSON/HTML report formats |
| [`reference/scripts.md`](reference/scripts.md) | The 7 supporting scripts (`review_ingredient`, `batch_review`, `auto_correct`, `apply_corrections`, `download_ontologies`, `validate_synonyms`, `enrich_from_ols`) with usage and options |
| [`reference/operations.md`](reference/operations.md) | Error handling & retry, troubleshooting, worked examples/scenarios, workflow integration points, quality metrics & trends, and the future-enhancements roadmap |
