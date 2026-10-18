# `data/ingredients/mapped/Pyrimethamine.yaml`

**Verdict**: pass.

**Identity**: `Pyrimethamine` is mapped exactly to active `CHEBI:8673` / `pyrimethamine`. OLS4 CHEBI confirms the same term, and PubChem lookup by CAS `58-14-0` confirms the stored formula and InChI.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pyrimethamine.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Pyrimethamine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The CultureBotHT CAS import and OAK/OLS row review support the exact CHEBI identity. Final SSSOM row 2463 keeps only `5-(4-chlorophenyl)-6-ethylpyrimidine-2,4-diamine` plus `CAS:58-14-0`; both are scoped to pyrimethamine.

**Completeness**: The record has no role assertions, components, or unsupported final synonyms.

**Recommended Edits**: None.
