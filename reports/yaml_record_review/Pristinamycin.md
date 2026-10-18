# `data/ingredients/mapped/Pristinamycin.yaml`

**Verdict**: pass.

**Identity**: `Pristinamycin` is mapped exactly to active `CHEBI:85274` / `pristinamycin`. OLS4 CHEBI resolves that term as a pristinamycin mixture, which matches the MicrobeDecoder antibiotic label rather than a single component.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pristinamycin.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Pristinamycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The MicrobeDecoder OLS exact import, pending-review hold, and `review-ingredients` promotion are internally consistent. Final SSSOM row 2421 is an exact CHEBI row and has an empty `other` column.

**Completeness**: The record has the expected MicrobeDecoder source occurrence and no active synonyms, roles, components, or structure fields that need additional support.

**Recommended Edits**: None.
