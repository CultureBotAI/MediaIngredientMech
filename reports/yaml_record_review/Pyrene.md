# `data/ingredients/mapped/Pyrene.yaml`

**Verdict**: pass.

**Identity**: `Pyrene` is mapped exactly to active `CHEBI:39106` / `pyrene`. OLS4 CHEBI resolves the same term, and the record stores the expected `C16H10` structure for pyrene.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pyrene.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Pyrene.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The MicrobeDecoder import grounded pyrene through an OLS label-exact CHEBI match, then `review-ingredients` promoted the row after local OAK label verification. Final SSSOM row 2453 maps `MIM:Pyrene` exactly to `CHEBI:39106` and exports no unsupported synonym tokens.

**Completeness**: The record has no role assertions, components, CAS number, or extra synonyms.

**Recommended Edits**: None.
