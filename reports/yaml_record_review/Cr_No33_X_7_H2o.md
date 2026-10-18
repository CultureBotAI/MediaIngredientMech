# `data/ingredients/mapped/Cr_No33_X_7_H2o.yaml`

## Verdict

Pass. The CultureMech hydrate record is grounded to active `CHEBI:86206`
chromium trinitrate heptahydrate, the formula, InChI, SMILES, exact synonyms,
2/2 CultureMech occurrence count, final SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Cr_No33_X_7_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:86206`,
  `ontology_mapping.ontology_id: CHEBI:86206`,
  `ontology_label: chromium trinitrate heptahydrate`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Live OLS lookup by `CHEBI:86206` returns active `CHEBI:86206` labelled
  `chromium trinitrate heptahydrate` with heptahydrate-specific synonyms.
- The record stores formula `Cr.7H2O.3NO3` with InChI and SMILES values that
  explicitly include the chromium ion, three nitrate ions, and seven waters.

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
  `reports` found the active `MIM:Cr_No33_X_7_H2o` final SSSOM row, the
  OAK/OLS row-review confirmation, and matching aggregate/docs rows.
- Hidden/ignored-inclusive exact identity search under `data/ingredients` found
  no second active record using `CHEBI:86206`.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found 2 rows for `CHEBI:86206`
  whose occurrence weights sum to 2, matching the explicit 2/2
  `occurrence_statistics`.
- The final SSSOM `other` column contains Cr(NO3)3 heptahydrate surface forms
  and hydrate-specific chromium nitrate synonyms, with no anhydrous or
  malformed hydrate residue.

## Completeness

- The ChEBI hydrate identifier, formula, InChI, SMILES, exact synonyms, SSSOM
  row, aggregate copy, docs row, and occurrence count are populated and agree.
- No recommended edits.

## Recommended Edits

- None.
