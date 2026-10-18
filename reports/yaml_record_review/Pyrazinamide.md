# `data/ingredients/mapped/Pyrazinamide.yaml`

**Verdict**: pass.

**Identity**: `Pyrazinamide` is mapped to active `CHEBI:45285` / `pyrazinecarboxamide` through CAS `98-96-4`. OLS4 CHEBI confirms `Pyrazinamide` and `PYRAZINE-2-CARBOXAMIDE` on the same term, and PubChem lookup by CAS confirms the stored formula and InChI.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pyrazinamide.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Pyrazinamide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The CultureBotHT CAS lookup, later CAS_RN_LOOKUP regrade, and OAK/OLS row review all support `CHEBI:45285`. Final SSSOM row 2452 maps the subject exactly to `CHEBI:45285` and keeps only `PYRAZINE-2-CARBOXAMIDE` plus `CAS:98-96-4` in `other`.

**Completeness**: The record has no role assertions, components, or unsupported final synonyms.

**Recommended Edits**: None.
