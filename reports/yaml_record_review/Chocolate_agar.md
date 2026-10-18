# `data/ingredients/mapped/Chocolate_agar.yaml`

## Verdict

Pass. The CultureMech residual record is exactly grounded to active
`MICRO:0000591` `chocolate agar`, carries a 2/2 occurrence count traceable to
the residual import, and its SSSOM row and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Chocolate_agar.yaml`.
- Identifier and grounding: `identifier: MICRO:0000591`,
  `ontology_mapping.ontology_id: MICRO:0000591`,
  `ontology_label: chocolate agar`, `ontology_source: MICRO`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Direct exact OLS lookup against MICRO for `chocolate agar` returned one
  active `MICRO:0000591` term labelled `chocolate agar`, matching the record's
  identifier and ontology mapping.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Chocolate_agar.yaml data/ingredients/mapped/Cholesterol_Lipid_Concentrate.yaml data/ingredients/mapped/Cholic_Acid.yaml data/ingredients/mapped/Cholin_Acetate.yaml data/ingredients/mapped/Choline.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data ... -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-scoped ontology records in this batch. This MICRO
  record was skipped because `MICRO:0000591` is outside the Engine A OAK/OLS
  term-validation scope used by this repository.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active `MIM:Chocolate_agar` SSSOM row as
  `skos:exactMatch MICRO:0000591` and matching aggregate/docs rows.
- Hidden/ignored-inclusive search found the CultureMech residual-review inputs:
  `mappings/culturemech_residual_groundings.tsv` records `chocolate agar` as a
  2-occurrence, 2-recipe `NEW_RECORD` exact grounding to `MICRO:0000591`, and
  the unified ingredient mapping retains the two raw CultureMech recipe ids.
- The record carries no chemical-property, component, role, or environment
  claim that would require non-MICRO evidence.

## Completeness

- The residual-created identity, structured mapping evidence restored for
  issue 541, occurrence count, SSSOM row, aggregate copy, and docs row are
  populated and agree.

## Recommended Edits

- None for this record.
