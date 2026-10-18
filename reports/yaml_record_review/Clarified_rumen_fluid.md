# `data/ingredients/mapped/Clarified_rumen_fluid.yaml`

## Verdict

Pass with minor issues. The CultureMech residual `Clarified rumen fluid` record
is exactly grounded to active `MICRO:0000520`; its primary 6/6 residual
occurrence row, restored structured evidence, SSSOM row, and aggregate copy
agree. A second lower-case 3/3 residual row still targets the same term and
should be reconciled with this record or marked stale.

## Identity

- Reviewed record: `data/ingredients/mapped/Clarified_rumen_fluid.yaml`.
- Identifier and grounding: `identifier: MICRO:0000520`,
  `ontology_mapping.ontology_id: MICRO:0000520`,
  `ontology_label: clarified rumen fluid`, `ontology_source: MICRO`,
  `mapping_quality: EXACT_MATCH`, `match_level: EXACT`, and
  `mapping_status: MAPPED`.
- Live exact OLS lookup against MICRO for `clarified rumen fluid` returns
  active `MICRO:0000520` labelled `clarified rumen fluid`, plus the narrower
  DSMZ Medium 1310 clarified-rumen-fluid term.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Citric_Acid_X_H2o.yaml data/ingredients/mapped/Citric_Acidh2o.yaml data/ingredients/mapped/Cl.yaml data/ingredients/mapped/Cladomycin.yaml data/ingredients/mapped/Clarified_rumen_fluid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Citric_Acid_X_H2o.yaml data/ingredients/mapped/Citric_Acidh2o.yaml data/ingredients/mapped/Cl.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-scoped records in this batch. This MICRO record
  was skipped because `MICRO:0000520` is outside the Engine A OAK/OLS
  term-validation scope used by this repository.
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
  `reports` found the active exact `MIM:Clarified_rumen_fluid` SSSOM row, the
  CultureMech residual grounding/triage rows, its use as a component in the
  existing PYG or rumen-fluid blend records, and matching aggregate/docs rows.
- Hidden/ignored-inclusive exact CURIE search under `data/ingredients` found
  `MICRO:0000520` as the identifier only in this active record; three existing
  decomposed media records refer to it as a component.
- `mappings/culturemech_residual_groundings.tsv` records `Clarified rumen
  fluid` as a 6-occurrence, 6-recipe `NEW_RECORD` exact grounding to
  `MICRO:0000520`, matching the explicit 6/6 `occurrence_statistics`.
- The same hidden/ignored-inclusive residual search found another
  `clarified rumen fluid` row with count 3/3 that also targets `MICRO:0000520`.
  It is casefold-equivalent to the preferred label but is not reflected in the
  current occurrence count.
- The record carries no chemical-property, component, role, or environment
  claim that would require additional evidence.

## Completeness

- The residual-created identity, restored structured mapping evidence, primary
  residual occurrence count, SSSOM row, aggregate copy, and docs row are
  populated and agree.
- The 3/3 lower-case residual row is the only unresolved count/provenance gap.

## Recommended Edits

- Minor: fold the lower-case `clarified rumen fluid` residual row into this
  record's occurrence count or mark that row stale if those mentions are
  already included in the 6/6 creating row.
