# `data/ingredients/mapped/Pravastatin_Lactone.yaml`

**Verdict**: pass.

**Identity**: `Pravastatin lactone` is mapped exactly to active `CHEBI:145933` / `pravastatin lactone`, not to pravastatin acid or a sodium salt. The stored formula, SMILES, and InChI match the CHEBI term and PubChem's record for CAS `85956-22-5`.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pravastatin_Lactone.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Pravastatin_Lactone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The CultureBotHT CAS source, exact CHEBI mapping, and final SSSOM row 2415 agree. The final `CAS:85956-22-5` token is allowed because it matches `chemical_properties.cas_rn`.

**Completeness**: The record has no role assertions, no active synonyms, and no components; the exact lactone identity is represented without leaking labels from broader pravastatin.

**Recommended Edits**: None.
