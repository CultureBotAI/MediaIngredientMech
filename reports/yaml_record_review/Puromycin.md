# `data/ingredients/mapped/Puromycin.yaml`

**Verdict**: pass.

**Identity**: `Puromycin` is mapped exactly to active `CHEBI:17939` / `puromycin`. OLS4 CHEBI confirms the stored formula, SMILES, and InChI for the free-base antibiotic.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Puromycin.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Puromycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The MicrobeDecoder import grounded the same antibiotic through an OLS label-exact CHEBI match, and `review-ingredients` promoted the row after local OAK label verification. Final SSSOM row 2442 maps `MIM:Puromycin` exactly to `CHEBI:17939` and exports no unsupported synonym tokens.

**Completeness**: The record has no role assertions, components, CAS number, or extra synonyms.

**Recommended Edits**: None.
