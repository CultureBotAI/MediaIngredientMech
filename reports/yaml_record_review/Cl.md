# `data/ingredients/mapped/Cl.yaml`

## Verdict

Pass. The CultureMech residual `Cl-` record is correctly grounded to active
`CHEBI:17996` chloride on a ChEBI synonym match; its 5/5 residual occurrence
count, restored structured evidence, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Cl.yaml`.
- Identifier and grounding: `identifier: CHEBI:17996`,
  `ontology_mapping.ontology_id: CHEBI:17996`,
  `ontology_label: chloride`, `ontology_source: CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `match_level: NORMALIZED`, and
  `mapping_status: MAPPED`.
- Live OLS lookup for `CHEBI:17996` returns one active ChEBI term labelled
  `chloride` with `Cl-` as a related synonym.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Citric_Acid_X_H2o.yaml data/ingredients/mapped/Citric_Acidh2o.yaml data/ingredients/mapped/Cl.yaml data/ingredients/mapped/Cladomycin.yaml data/ingredients/mapped/Clarified_rumen_fluid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Citric_Acid_X_H2o.yaml data/ingredients/mapped/Citric_Acidh2o.yaml data/ingredients/mapped/Cl.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-scoped records in this batch. `Cladomycin` and
  `Clarified_rumen_fluid` were skipped because local `kgmicrobe.compound:` and
  `MICRO:` terms are outside the focused Engine A CHEBI/OBO validation scope.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only the expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active exact `MIM:Cl` SSSOM row, the CultureMech residual
  grounding/triage rows, and matching aggregate/docs rows.
- Hidden/ignored-inclusive exact CURIE search under `data/ingredients` found
  `CHEBI:17996` only in this active record.
- `mappings/culturemech_residual_groundings.tsv` records `Cl-` as a
  5-occurrence, 5-recipe `NEW_RECORD` exact grounding to `CHEBI:17996`,
  matching the explicit 5/5 `occurrence_statistics`.
- The record carries no chemical-property, component, role, or environment
  claim that would require additional evidence.

## Completeness

- The residual-created identity, restored structured mapping evidence,
  occurrence count, SSSOM row, aggregate copy, and docs row are populated and
  agree.

## Recommended Edits

- None for this record.
