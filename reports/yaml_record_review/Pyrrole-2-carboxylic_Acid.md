# `data/ingredients/mapped/Pyrrole-2-carboxylic_Acid.yaml`

**Verdict**: pass.

**Identity**: `Pyrrole-2-carboxylic acid` is mapped exactly to active `CHEBI:36751` / `pyrrole-2-carboxylic acid`. OLS4 CHEBI resolves the same term, and PubChem lookup by CAS `634-97-9` confirms the stored formula and InChI.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pyrrole-2-carboxylic_Acid.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Pyrrole-2-carboxylic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The CultureBotHT CAS import and OAK/OLS row review support the exact CHEBI identity. Final SSSOM row 2468 keeps only `1H-pyrrole-2-carboxylic acid` plus `CAS:634-97-9`; both are scoped to pyrrole-2-carboxylic acid.

**Completeness**: The record has no role assertions, components, or unsupported final synonyms.

**Recommended Edits**: None.
