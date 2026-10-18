# `data/ingredients/mapped/Pravastatin.yaml`

**Verdict**: pass.

**Identity**: `Pravastatin` is mapped exactly to active `CHEBI:63618` / `pravastatin`. The stored formula, SMILES, InChI, and molecular weight match the structure fields on the CHEBI term.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pravastatin.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Pravastatin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The MicrobeDecoder source occurrence, OLS exact CHEBI import, `review-ingredients` promotion, and #323 single-ingredient classification are aligned. Final SSSOM row 2414 preserves the exact CHEBI mapping and does not publish extra synonyms in `other`.

**Completeness**: The record has no CAS, role, synonym, or component payload that would require further support. Its stored structure is specific to pravastatin rather than a salt or lactone sibling.

**Recommended Edits**: None.
