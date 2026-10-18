# `data/ingredients/mapped/Quassin.yaml`

**Verdict**: pass.

**Identity**: `Quassin` is mapped exactly to active `CHEBI:8692` / `Quassin`. OLS4 CHEBI resolves `CHEBI:8692` by label, and PubChem lookup by CAS `76-78-8` confirms the stored formula, stereochemical SMILES, and InChI for quassin.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Quassin.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Quassin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The CultureBotHT CAS import and OAK/OLS row review support the exact CHEBI identity despite the broader OLS search also returning nigakilactone terms with `Quassin` as a related synonym. Final SSSOM row 2473 keeps only `CAS:76-78-8` in `other`.

**Completeness**: The record has no role assertions, components, or unsupported final synonyms.

**Recommended Edits**: None.
