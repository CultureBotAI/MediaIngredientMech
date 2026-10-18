# `data/ingredients/mapped/Catalase.yaml`

## Verdict

Pass with minor issues. The live record is exactly grounded to active
`NCIT:C61062`, and its Sigma catalog variant, occurrence count, SSSOM row, and
aggregate copy agree, but the active SSSOM row still carries a stale
`UNKNOWN_TERM` validation marker.

## Identity

- Reviewed record: `data/ingredients/mapped/Catalase.yaml`.
- Identifier and grounding: `identifier: NCIT:C61062`,
  `ontology_mapping.ontology_id: NCIT:C61062`,
  `ontology_label: Catalase`, `ontology_source: NCIT`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `NCIT:C61062` returns one active NCIT term labelled
  `Catalase`.
- The record was correctly repaired from removed `CHEBI:3463` to
  `NCIT:C61062`; the older row-review files still name `CHEBI:3463`, but the
  maintained YAML, aggregate copy, docs rows, and live SSSOM row all now use
  the NCIT identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Caso42h2osaturated_Solution.yaml data/ingredients/mapped/Caso4_X_2_H2o.yaml data/ingredients/mapped/Caso4_X_7_H2o.yaml data/ingredients/mapped/Catalase.yaml data/ingredients/mapped/Cd_No32_X_4_H2o.yaml`:
  passed.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Caso4_X_2_H2o.yaml data/ingredients/mapped/Caso4_X_7_H2o.yaml data/ingredients/mapped/Catalase.yaml data/ingredients/mapped/Cd_No32_X_4_H2o.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 4 external-ontology records in this batch.
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
  backups, found the active `MIM:Catalase` SSSOM row with `NCIT:C61062`, the
  CultureMech alias-backfill triage row for `Catalase (Sigma C--10)`, and
  matching aggregate/docs rows.
- The current `mappings/culturemech_recipe_membership.tsv` rows contain 34
  distinct recipes and 34 total occurrences for `NCIT:C61062`, matching
  `occurrence_statistics`.
- No role, component, or chemical-property claims are present.

## Completeness

- The NCIT identifier, raw CultureMech property strings, Sigma catalog variant,
  34/34 occurrence count, SSSOM row, aggregate copy, and docs row are
  populated.
- Minor gap: `mappings/ingredient_mappings.sssom.tsv` still labels the
  validation method for the active NCIT row as `none|UNKNOWN_TERM|2026-07-07`
  even though direct NCIT OLS lookup resolves the exact CURIE.

## Recommended Edits

- Minor: refresh the synonym/unknown-term review metadata for the
  `MIM:Catalase` SSSOM row so `validation_method` no longer reports the
  pre-migration `UNKNOWN_TERM` state.
