# `data/ingredients/mapped/Potassium_Aspartate.yaml`

**Verdict**: pass.

**Identity**: `Potassium Aspartate` maps exactly to `NCIT:C87343` / `Potassium Aspartate`. The CultureMech residual source, NCIT exact label, restored structured evidence, and final SSSOM row 2391 agree.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Potassium_Aspartate.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Potassium_Aspartate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The creation history and structured evidence both point to CultureMech occurrence-table rows that were grounded to `NCIT:C87343` on an exact canonical-label match for `Potassium Aspartate`. Final SSSOM row 2391 has no `other` synonyms to triage. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected curated, generated, and final SSSOM references.

**Completeness**: The exact NCIT identity and three CultureMech occurrences are present. No role, component, or chemical-property claims require further evidence.

**Recommended Edits**: None.
