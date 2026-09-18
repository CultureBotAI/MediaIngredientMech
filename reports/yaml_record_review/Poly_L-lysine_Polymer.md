# `data/ingredients/mapped/Poly_L-lysine_Polymer.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `poly(L-lysine) polymer` maps exactly to `CHEBI:61490` / `poly(L-lysine) polymer`. The CHEBI identifier, canonical label, `SINGLE_INGREDIENT` classification, and final SSSOM row 2361 agree; a fresh CHEBI OLS exact lookup also resolved this label to `CHEBI:61490`.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Poly_L-lysine_Polymer.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Poly_L-lysine_Polymer.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: `Poly L Lysine Polymer` and `poly(L-lysine)` are valid surface forms for the CHEBI subject after the duplicate record merge. The active `produces: poly(L-lysine) polymer` synonym, recovered from previous SSSOM `other` content, is process-qualified trait text rather than a name for the substance. It still reaches final SSSOM row 2361 in `other`, so the published synonym surface is over-broad. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the active row, the rejected duplicate, the known cross-record `other` baseline entry, and the final SSSOM row exporting the process phrase.

**Completeness**: The exact CHEBI identity itself is complete enough for a zero-occurrence KG-Microbe special-chemical import, and no component or role assertions are active.

**Recommended Edits**: In `data/ingredients/mapped/Poly_L-lysine_Polymer.yaml`, either remove `produces: poly(L-lysine) polymer` as an active synonym or move it to provenance that the final SSSOM builder filters. Synchronize `data/curated/mapped_ingredients.yaml`, regenerate the SSSOM, and rerun `scripts/validate_sssom_invariants.py` to confirm `other` no longer publishes the process-qualified phrase.
