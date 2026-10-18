# `data/ingredients/mapped/Protoporphyrin.yaml`

**Verdict**: pass.

**Identity**: `Protoporphyrin` is mapped exactly to active `CHEBI:15430` / `protoporphyrin`. OLS4 CHEBI confirms CAS `553-12-8`, the stored structure, `Protoporphyrin IX`, and `7,12-diethenyl-3,8,13,17-tetramethylporphyrin-2,18-dipropanoic acid` as synonyms of the same term.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Protoporphyrin.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Protoporphyrin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The #310 CAS repair stripped the invalid leading zero from `0553-12-8`, leaving the valid CAS `553-12-8` that CHEBI and final SSSOM row 2437 both carry. The final `other` tokens are all true synonyms for CHEBI:15430.

**Completeness**: The record has no role or component assertions and no unsupported synonym payload.

**Recommended Edits**: None.
