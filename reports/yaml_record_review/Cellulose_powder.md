# `data/ingredients/mapped/Cellulose_powder.yaml`

## Verdict

Pass. The CultureMech residual `Cellulose powder` record is exactly grounded to
active `FOODON:03310367`, and its restored CultureMech occurrence-table
provenance, 1/1 occurrence count, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Cellulose_powder.yaml`.
- Identifier and grounding: `identifier: FOODON:03310367`,
  `ontology_mapping.ontology_id: FOODON:03310367`,
  `ontology_label: cellulose powder`, `ontology_source: FOODON`,
  `mapping_quality: EXACT_MATCH`, `match_level: EXACT`, and
  `mapping_status: MAPPED`.
- The focused LinkML label validator resolves `FOODON:03310367` and accepts the
  stored `cellulose powder` ontology label.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cellulose.yaml data/ingredients/mapped/Cellulose_powder.yaml data/ingredients/mapped/Cephalexin.yaml data/ingredients/mapped/Cephalosporin.yaml data/ingredients/mapped/Cephalothin.yaml`:
  passed.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cellulose.yaml data/ingredients/mapped/Cellulose_powder.yaml data/ingredients/mapped/Cephalexin.yaml data/ingredients/mapped/Cephalosporin.yaml data/ingredients/mapped/Cephalothin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 external-ontology records in this batch.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding generated review reports and curated
  backups, found the active exact `MIM:Cellulose_powder` SSSOM row, the
  `mappings/culturemech_residual_groundings.tsv` `NEW_RECORD` decision, the
  `mappings/culturemech_residual_triage.tsv` row with 1/1 mentions, and
  matching aggregate/docs rows for `FOODON:03310367`.
- The SSSOM row includes the restored
  `MIM:culturemech:output/ingredient_occurrences.tsv` provenance expected by
  the September 2026 `claude_restore_culturemech_evidence` correction.
- The record carries no chemical property, role, component, synonym, or
  environment claims.

## Completeness

- The exact FoodOn identifier, structured grounding evidence, SSSOM row,
  aggregate copy, docs row, and CultureMech residual 1/1 occurrence count are
  populated and agree.
- No additional exact synonym or rejected label is needed for this one-label
  residual grounding.

## Recommended Edits

- None for this record.
