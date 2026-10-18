# `data/ingredients/mapped/Corn_Oil.yaml`

## Verdict

Pass. The MicrobeDecoder import is grounded to active `CHEBI:195250` corn oil,
the source occurrence count matches the residual BacDive trait count, the 0/0
CultureMech occurrence count is expected, the final SSSOM row is narrow, and no
unsupported roles or component claims are present.

## Identity

- Reviewed record: `data/ingredients/mapped/Corn_Oil.yaml`.
- Identifier and grounding: `identifier: CHEBI:195250`,
  `ontology_mapping.ontology_id: CHEBI:195250`, `ontology_label: corn oil`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`, and
  `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:195250` returns active `CHEBI:195250` labelled
  `corn oil`.
- The record has no ordinary CultureMech occurrences and retains the separate
  MicrobeDecoder provenance in `source_occurrences`.

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
  `reports` found the active `MIM:Corn_Oil` final SSSOM row, the
  MicrobeDecoder approval row, and matching generated docs rows.
- Hidden/ignored-inclusive exact identity search under `data/ingredients` found
  no second active record using `CHEBI:195250`.
- Hidden/ignored-inclusive search of
  `data/custom/microbedecoder/unmapped_labels.tsv` found
  `kgmicrobe.trait:corn_oil` in `BacDive_Metabolite_utilization` with count 5,
  matching `occurrence_statistics.source_occurrences`.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no `CHEBI:195250` rows,
  matching the explicit 0/0 CultureMech `occurrence_statistics`.
- The final SSSOM row has no `other` tokens to review.

## Completeness

- The ChEBI identifier, MicrobeDecoder source count, zero CultureMech count,
  SSSOM row, aggregate copy, and docs row are populated and agree.
- No recommended edits.

## Recommended Edits

- None.
