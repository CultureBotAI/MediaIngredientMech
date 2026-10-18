# `data/ingredients/mapped/Quebrachitol.yaml`

**Verdict**: pass.

**Identity**: `Quebrachitol` is mapped to active `CHEBI:111` / `(-)-Quebrachitol` through CAS `642-38-6`. OLS4 CHEBI resolves the same stereospecific term, and PubChem lookup by the stored CAS confirms the stored formula.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Quebrachitol.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Quebrachitol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The CultureBotHT CAS lookup, later CAS_RN_LOOKUP regrade, and row-review manifest support `CHEBI:111`. Final SSSOM row 2474 maps the subject exactly to `CHEBI:111` and keeps only `CAS:642-38-6` in `other`.

**Completeness**: The record has no role assertions, components, or unsupported final synonyms.

**Recommended Edits**: None.
