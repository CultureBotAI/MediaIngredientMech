# `data/ingredients/mapped/Potassium_Tellurite.yaml`

**Verdict**: pass.

**Identity**: `potassium tellurite` is an exact `CHEBI:75248` record. The September #455 repair corrected the CultureBotHT typo from `potassium tellurate` to `potassium tellurite`, while leaving the already-correct CAS `7790-58-1` and CHEBI mapping in place.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Potassium_Tellurite.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Potassium_Tellurite.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: OLS4 CHEBI resolves `CHEBI:75248` to `potassium tellurite`, with CAS xref `7790-58-1`, formula `2K.O3Te`, and `dipotassium tellurite` as an exact synonym. Those values agree with the stored CAS RN, chemistry, curated synonym, and final SSSOM row 2407.

**Completeness**: The record has no active role assertions or components, and the final `other` values are true synonyms for anhydrous potassium tellurite.

**Recommended Edits**: None.
