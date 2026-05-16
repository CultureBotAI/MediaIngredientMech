# Schema / instance / process gap analysis

**Date**: 2026-05-16
**Tool**: `linkml-validate` (linkml 1.9.3, linkml-runtime pinned to 1.9.x)
**Schema**: `src/mediaingredientmech/schema/mediaingredientmech.yaml`
**Data**: 1870 mapped + 398 unmapped + 2268 individual records (`data/curated/` + `data/ingredients/`)

This is a snapshot of the divergences `linkml-validate` finds when run against
the current schema and curated data. The methodology lives in
`.claude/skills/schema-gap-analysis/SKILL.md`; this file records what it
turned up this session so we don't rediscover the same gaps next time.

## Findings ranked by blast radius

| # | Error | Axis | Records affected | Fix sketch |
|---|---|---|---:|---|
| 1 | `'ontology_id' is a required property` and `Additional properties are not allowed ('identifier')` | Schema | 2268 (all) | Alias or rename: data uses `identifier`; schema slot is `ontology_id`. Either add `aliases: [identifier]` on the schema slot OR rename it. See [[identifier_system_dual]] memory for context. |
| 2 | `does not match '^[A-Z]+:[0-9]+$'` on `ontology_mapping.ontology_id` | Schema | 311 | The custom validator was broadened to `^[A-Za-z][A-Za-z0-9.]*:[A-Za-z0-9][A-Za-z0-9._-]*$`. Apply the same broadening to the schema `pattern:` on `OntologyMapping.ontology_id`. |
| 3 | `is not a 'date-time'` (naive timestamps without offset) | Process | 1537 | `accept_mapping()`, `ingredient_reviewer.py`, several `scripts/*` use `datetime.now()` instead of `datetime.now(timezone.utc)`. Fix the generators; one-shot rewrite of affected records is optional. |
| 4 | `Additional properties are not allowed ('pubchem_cid')` on `chemical_properties` | Schema | 185 | Add `pubchem_cid` to `ChemicalProperties` (range: string, pattern `^[0-9]+$`). |
| 5 | `does not match '^CHEBI:[0-9]+$'` on `kg_microbe_node_id` | Schema | 31 | Pattern too narrow; current data has non-CHEBI prefixes here too. Broaden similarly to (2). |
| 6 | `Additional properties are not allowed ('cas_rn')` on `ontology_mapping.evidence[]` | Schema | 44 | Add `cas_rn` to `MappingEvidence` (range: string, pattern `^\d+-\d+-\d+$`) — already defined on `ChemicalProperties`; promote to a reusable slot. |

Total error count: ~5848 across 2275 files (every issue above is systematic — none are isolated record bugs).

## Process-axis hot spots

`grep -rn 'datetime.now()' src/ scripts/ --include='*.py' | grep -v timezone`
turns up these generators writing naive timestamps:

- `src/mediaingredientmech/validation/ingredient_reviewer.py` (3 sites)
- `src/mediaingredientmech/export/report_generator.py`
- `scripts/download_ontologies.py`
- `scripts/batch_curate.py` (2 sites)
- `scripts/batch_curate_unmapped.py` (2 sites)
- and ~10 more under `scripts/`

The collection-level `generation_date` written by `scripts/aggregate_records.py`
is already timezone-aware; only record-level / event-level timestamps are
affected.

## Suggested remediation order

1. **Schema first (no migration risk)**: items 2, 4, 5, 6 — broaden patterns
   and add missing slots. After this, the only remaining errors are #1 and #3.
2. **Identifier slot alias (item 1)**: add `aliases: [identifier]` to the
   `IngredientRecord.ontology_id` slot rather than renaming, so old callers
   keep working. Re-run validation: residual errors should be zero except
   the timestamps.
3. **Generator fixes (item 3)**: switch `datetime.now()` → `datetime.now(timezone.utc)`
   in every site grep finds. Optional follow-up: a one-shot pass over
   `data/curated/` + `data/ingredients/` to retrofit the existing naive
   timestamps with `+00:00` so historical records also validate.

## Not addressed yet

- The `OntologyMapping.ontology_label` field is required by the schema but
  several records have `ontology_label: null` in the source YAML. Run a
  separate `grep "ontology_label: null"` pass before fixing #1, because
  those will become visible once the slot-name issue stops dominating the
  error output.
