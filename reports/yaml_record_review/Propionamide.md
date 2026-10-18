# `data/ingredients/mapped/Propionamide.yaml`

**Verdict**: pass.

**Identity**: `Propionamide` is mapped exactly to active `CHEBI:45422` / `propionamide`. The stored formula, SMILES, InChI, and molecular weight match the CHEBI structure.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Propionamide.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Propionamide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The MicrobeDecoder exact import, pending-review hold, `review-ingredients` promotion, and #323 single-ingredient classification are aligned. Final SSSOM row 2427 publishes only the exact CHEBI row with no `other` payload.

**Completeness**: The record has no CAS, role, synonym, or component fields that need further support.

**Recommended Edits**: None.
