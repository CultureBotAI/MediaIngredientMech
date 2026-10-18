# `data/ingredients/mapped/Quercetin.yaml`

**Verdict**: pass.

**Identity**: `Quercetin` is mapped exactly to active `CHEBI:16243` / `quercetin`. OLS4 CHEBI confirms the same term, and PubChem lookup by CAS `117-39-5` confirms the stored formula and InChI.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Quercetin.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Quercetin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The CultureBotHT CAS import and OAK/OLS row review support the exact CHEBI identity. Final SSSOM row 2475 keeps only `2-(3,4-dihydroxyphenyl)-3,5,7-trihydroxy-4H-chromen-4-one` plus `CAS:117-39-5`; both are scoped to quercetin.

**Completeness**: The record has no role assertions, components, or unsupported final synonyms.

**Recommended Edits**: None.
