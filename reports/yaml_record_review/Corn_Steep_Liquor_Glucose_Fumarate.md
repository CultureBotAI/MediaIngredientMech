# `data/ingredients/mapped/Corn_Steep_Liquor_Glucose_Fumarate.yaml`

## Verdict

Pass. The MicrobeDecoder residual blend is intentionally grounded to the local
`kgmicrobe.ingredient:corn_steep_liquor_glucose_fumarate` identity, the source
label is completely decomposed into corn steep liquor, glucose, and fumaric
acid, the one literature-substrate occurrence is preserved, and the final SSSOM
row is narrow.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Corn_Steep_Liquor_Glucose_Fumarate.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:corn_steep_liquor_glucose_fumarate`,
  `ontology_mapping.ontology_id: kgmicrobe.ingredient:corn_steep_liquor_glucose_fumarate`,
  `ontology_label: Corn Steep Liquor + Glucose + Fumarate`,
  `ontology_source: kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, and `ingredient_type: UNDEFINED_MIXTURE`.
- A fresh exact OLS search for `Corn Steep Liquor + Glucose + Fumarate`
  returned no class hits, matching the local-registry decision.
- `component_assertion` is `LABEL_ENUMERATION` and `COMPLETE`; the label names
  corn steep liquor, glucose, and fumaric acid, and those are the three retained
  components.

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
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed
  before this read-only report batch.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active
  `MIM:Corn_Steep_Liquor_Glucose_Fumarate` final SSSOM row, the residual blend
  queue row, the curated decomposition row, and matching generated docs rows.
- Hidden/ignored-inclusive exact identity search under `data/ingredients` found
  no second active record using
  `kgmicrobe.ingredient:corn_steep_liquor_glucose_fumarate`.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no local
  `kgmicrobe.ingredient` rows, matching the explicit 0/0 CultureMech
  `occurrence_statistics` for this MicrobeDecoder literature-substrate record.
- The final SSSOM row has no `other` tokens to review. The raw label synonym
  duplicates the preferred term and is filtered.

## Completeness

- The local ingredient identity, three-part complete decomposition, residual
  MicrobeDecoder occurrence, SSSOM row, aggregate copy, and docs row are
  populated and agree.
- No recommended edits.

## Recommended Edits

- None.
