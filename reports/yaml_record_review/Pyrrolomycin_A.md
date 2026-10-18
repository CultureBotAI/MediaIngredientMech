# `data/ingredients/mapped/Pyrrolomycin_A.yaml`

**Verdict**: pass.

**Identity**: `Pyrrolomycin A` is mapped exactly to active `CHEBI:156550` / `pyrrolomycin A`. OLS4 CHEBI resolves the same term, and PubChem name lookup confirms the stored formula and InChI.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pyrrolomycin_A.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Pyrrolomycin_A.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The MicrobeDecoder import grounded pyrrolomycin A through an OLS label-exact CHEBI match, then `review-ingredients` promoted the row after local OAK label verification. Final SSSOM row 2469 maps `MIM:Pyrrolomycin_A` exactly to `CHEBI:156550` and exports no unsupported synonym tokens.

**Completeness**: The record has no role assertions, components, CAS number, or extra synonyms.

**Recommended Edits**: None.
