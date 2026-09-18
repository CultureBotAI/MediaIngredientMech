# `data/ingredients/mapped/Potato_Flour.yaml`

**Verdict**: pass.

**Identity**: `Potato flour` is mapped exactly to `FOODON:03302378` / `potato flour`. The exact FOODON identity and `UNDEFINED_MIXTURE` ingredient type agree with a food-derived flour ingredient.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Potato_Flour.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Potato_Flour.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The `resolve_unmapped` OLS evidence records a label-exact FOODON upgrade from the original MediaDive queue entry, and final SSSOM row 2412 keeps an exact FOODON row without exporting any non-synonym `other` payload. The only active synonym is the raw same-label source text.

**Completeness**: A flour can be treated as an undefined mixture here, and the seven refreshed CultureMech occurrences are traceable through the #337 occurrence table. No component or role assertions are present that would need narrower evidence.

**Recommended Edits**: None.
