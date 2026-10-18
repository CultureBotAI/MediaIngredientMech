# `data/ingredients/mapped/Corn_Meal.yaml`

## Verdict

Pass. The mim-queue record is grounded to active `FOODON:03310257` cornmeal
through the exact synonym `corn meal`, classified as an undefined mixture, has a
matching 6/6 CultureMech occurrence count, exports the valid `Maize meal`
synonym, and has no unsupported roles or component claims.

## Identity

- Reviewed record: `data/ingredients/mapped/Corn_Meal.yaml`.
- Identifier and grounding: `identifier: FOODON:03310257`,
  `ontology_mapping.ontology_id: FOODON:03310257`,
  `ontology_label: cornmeal`, `ontology_source: FOODON`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: FOODON:03310257`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Live OLS lookup by `FOODON:03310257` returns active `FOODON:03310257`
  labelled `cornmeal` with exact synonyms `corn meal` and `maize meal`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Corn_Meal.yaml data/ingredients/mapped/Corn_Oil.yaml data/ingredients/mapped/Corn_Steep_Liquor_Glucose_Fumarate.yaml data/ingredients/mapped/Coso4.yaml data/ingredients/mapped/Coso4_X_7_H2o.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Corn_Oil.yaml data/ingredients/mapped/Coso4.yaml data/ingredients/mapped/Coso4_X_7_H2o.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-identified records in this batch. `Corn_Meal` and
  `Corn_Steep_Liquor_Glucose_Fumarate` were intentionally skipped because their
  FOODON and local `kgmicrobe.ingredient` identifiers are outside this
  CHEBI-focused LinkML term-validation pass.
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
  `reports` found the active `MIM:Corn_Meal` final SSSOM row, the
  FOODON:03310257 exact-synonym audit for the previously unmapped record, and
  matching generated docs rows.
- Hidden/ignored-inclusive exact identity search under `data/ingredients` found
  no second active record using `FOODON:03310257`.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found 6 rows for
  `FOODON:03310257` whose occurrence weights sum to 6, matching the explicit
  6/6 `occurrence_statistics`.
- The final SSSOM `other` column contains `Maize meal`, an exact FoodOn synonym.

## Completeness

- The FoodOn identifier, undefined-mixture classification, final SSSOM row,
  aggregate copy, docs row, and occurrence count are populated and agree.
- No recommended edits.

## Recommended Edits

- None.
