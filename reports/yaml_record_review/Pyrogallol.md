# `data/ingredients/mapped/Pyrogallol.yaml`

**Verdict**: pass.

**Identity**: `Pyrogallol` is mapped exactly to active `CHEBI:16164` / `pyrogallol`. OLS4 CHEBI resolves the same term, and PubChem lookup by CAS `87-66-1` confirms the stored formula and InChI.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pyrogallol.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Pyrogallol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The CultureBotHT CAS import and OAK/OLS row review support the exact CHEBI identity. Final SSSOM row 2466 keeps only `benzene-1,2,3-triol` plus `CAS:87-66-1`; both are scoped to pyrogallol.

**Completeness**: The record has no role assertions, components, or unsupported final synonyms.

**Recommended Edits**: None.
