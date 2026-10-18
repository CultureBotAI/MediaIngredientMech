# `data/ingredients/mapped/CrKSO42_X_12_H2O.yaml`

## Verdict

Pass. The chrome alum record is intentionally CAS-primary at
`cas:7788-99-0`, uses active `CHEBI:53471` chromium(III) sulfate only as a
close parent because ChEBI lacks the potassium dodecahydrate, has a 0/0
occurrence count, and exports the expected close ChEBI row plus exact CAS
registry companion row.

## Identity

- Reviewed record: `data/ingredients/mapped/CrKSO42_X_12_H2O.yaml`.
- Identifier and grounding: `identifier: cas:7788-99-0`,
  `ontology_mapping.ontology_id: CHEBI:53471`,
  `ontology_label: chromium(III) sulfate`, `ontology_source: CHEBI`,
  `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live OLS lookup by `CHEBI:53471` returns active `CHEBI:53471` labelled
  `chromium(III) sulfate`; the curated evidence records that this parent lacks
  both potassium and the twelve waters.
- The CAS RN `7788-99-0` is the record's own identity, and the final SSSOM
  preserves it as an exact CAS registry row alongside the close ChEBI parent.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/CrKSO42_X_12_H2O.yaml data/ingredients/mapped/Cr_No33_X_7_H2o.yaml data/ingredients/mapped/Creatine.yaml data/ingredients/mapped/Creatinine.yaml data/ingredients/mapped/Cresol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cr_No33_X_7_H2o.yaml data/ingredients/mapped/Creatine.yaml data/ingredients/mapped/Creatinine.yaml data/ingredients/mapped/Cresol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI-exact records in this batch.
  `CrKSO42_X_12_H2O` was intentionally skipped because its CAS primary
  identifier and close ChEBI parent are outside this CHEBI-focused exact-label
  validation pass.
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
  `reports` found the active `MIM:CrKSO42_X_12_H2O` final SSSOM close-match and
  exact-CAS rows, the no-exact-OLS audit for the original unmapped record, the
  Edison CAS enrichment, and matching generated docs rows.
- Hidden/ignored-inclusive exact identity search under `data/ingredients` found
  no second active record using `cas:7788-99-0`.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no `cas:7788-99-0` rows,
  matching the explicit 0/0 `occurrence_statistics`.
- The final SSSOM `other` column contains only `CAS:7788-99-0`, which is
  expected for the CAS primary identity.

## Completeness

- The CAS identity, close ChEBI parent, SSSOM rows, aggregate copy, docs row,
  and zero occurrence count are populated and agree.
- No recommended edits.

## Recommended Edits

- None.
