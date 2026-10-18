# `data/ingredients/mapped/Pyrrolomycin_B.yaml`

**Verdict**: pass.

**Identity**: `Pyrrolomycin B` is mapped exactly to active `CHEBI:220052` / `Pyrrolomycin B`. OLS4 CHEBI resolves the same term, and PubChem name lookup confirms the stored formula and InChI.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pyrrolomycin_B.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Pyrrolomycin_B.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The MicrobeDecoder import grounded pyrrolomycin B through an OLS label-exact CHEBI match, then `review-ingredients` promoted the row after local OAK label verification. Final SSSOM row 2470 maps `MIM:Pyrrolomycin_B` exactly to `CHEBI:220052` and exports no unsupported synonym tokens.

**Completeness**: The record has no role assertions, components, CAS number, or extra synonyms.

**Recommended Edits**: None.
