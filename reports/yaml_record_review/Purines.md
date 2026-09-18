# `data/ingredients/mapped/Purines.yaml`

**Verdict**: pass.

**Identity**: `Purines` is mapped exactly to active `CHEBI:26401` / `purines`. The record intentionally points at a generic CHEBI purines class with formula `C5N4R7` and a generic R-group SMILES.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Purines.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Purines.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The MicrobeDecoder row was imported through an OLS label-exact CHEBI match, then manually promoted by the `review-ingredients` pass. Final SSSOM row 2441 maps `MIM:Purines` exactly to `CHEBI:26401` with no leaked raw text in `other`.

**Completeness**: The record has no role assertions, components, CAS number, or extra synonyms that need final SSSOM scrutiny beyond the exact CHEBI class row.

**Recommended Edits**: None.
