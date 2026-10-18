# `data/ingredients/mapped/Pradimicin.yaml`

**Verdict**: pass.

**Identity**: `Pradimicin` is mapped exactly to `CHEBI:83230` / `pradimicin`. OLS4 CHEBI resolves the term as an active 3-star class for pradimicins, matching the MicrobeDecoder metabolite label.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pradimicin.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Pradimicin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The MicrobeDecoder import, pending-review hold, and later `review-ingredients` promotion are consistent with an OLS label-exact CHEBI import. Final SSSOM row 2413 is an exact CHEBI row with no noisy `other` tokens.

**Completeness**: The record has the expected MicrobeDecoder source occurrence and no active synonyms, roles, components, or structure fields that need additional curation.

**Recommended Edits**: None.
