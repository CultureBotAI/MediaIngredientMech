# `data/ingredients/mapped/Cresol.yaml`

## Verdict

Needs curation; minor. The residual CultureMech record is grounded to active
`CHEBI:25399` cresol and exports a clean final SSSOM row, but its
`occurrence_statistics` were refreshed to 1/1 even though the residual grounding
artifact that created the row reports 3 Cresol mentions across 3 recipes and
the current `culturemech_recipe_membership.tsv` has no `CHEBI:25399` row.

## Identity

- Reviewed record: `data/ingredients/mapped/Cresol.yaml`.
- Identifier and grounding: `identifier: CHEBI:25399`,
  `ontology_mapping.ontology_id: CHEBI:25399`, `ontology_label: cresol`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `match_level: EXACT`.
- Live OLS lookup by `CHEBI:25399` returns active `CHEBI:25399` labelled
  `cresol`.
- The record is a generic cresol row distinct from the existing exact
  `4-Cresol` record at `CHEBI:17847`.

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
  `reports` found the active `MIM:Cresol` final SSSOM row, the residual
  grounding row that created it, the distinct active `MIM:4-Cresol` row, and
  matching generated docs rows.
- Hidden/ignored-inclusive exact identity search under `data/ingredients` found
  no second active record using `CHEBI:25399`.
- `mappings/culturemech_residual_groundings.tsv` reports `Cresol` with 3
  mentions across 3 recipes, but the record now stores 1/1 and
  hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no `CHEBI:25399` rows.
- The final SSSOM row has no `other` tokens to review.

## Completeness

- The ChEBI identifier, SSSOM row, aggregate copy, and docs row are populated
  and agree.
- The cleanup gap is the occurrence count provenance: current generated
  products publish 1/1 while the residual source artifact reports 3/3 and the
  membership table has not been populated for `CHEBI:25399`.

## Recommended Edits

- Minor: recompute `Cresol` occurrence statistics from the current CultureMech
  occurrence table or residual grounding source, update
  `mappings/culturemech_recipe_membership.tsv` so `CHEBI:25399` is represented,
  and preserve the distinct `4-Cresol` counts under `CHEBI:17847`.
- Regenerate synchronized products and rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
