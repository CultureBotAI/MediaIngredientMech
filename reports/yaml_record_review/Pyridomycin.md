# `data/ingredients/mapped/Pyridomycin.yaml`

**Verdict**: pass.

**Identity**: `Pyridomycin` is mapped exactly to active `CHEBI:221765` / `Pyridomycin`. OLS4 CHEBI resolves the same term, and PubChem name lookup confirms the stored formula and InChI for pyridomycin.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pyridomycin.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Pyridomycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The MicrobeDecoder import grounded pyridomycin through an OLS label-exact CHEBI match, then `review-ingredients` promoted the row after local OAK label verification. Final SSSOM row 2454 maps `MIM:Pyridomycin` exactly to `CHEBI:221765` and exports no unsupported synonym tokens.

**Completeness**: The record has no role assertions, components, CAS number, or extra synonyms.

**Recommended Edits**: None.
