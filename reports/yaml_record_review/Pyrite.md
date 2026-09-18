# `data/ingredients/mapped/Pyrite.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Pyrite` is mapped exactly to active `CHEBI:86471` / `pyrite`. OLS4 CHEBI resolves the same mineral term with `iron(2+) disulfide` as an exact synonym, and the stored OAK/CHEBI formula and structure fields are appropriate for pyrite.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pyrite.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Pyrite.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The kgm-metatraits import and OAK/OLS row review support the exact CHEBI identity. Final SSSOM row 2464 keeps the real `iron(2+) disulfide` synonym, but also exports `oxidation: pyrite`, a process-qualified source label that is not a synonym for the chemical entity.

**Completeness**: The record has no role assertions or components to fix. The active issue is the recovered raw process label in final `other`.

**Recommended Edits**: Delete the `oxidation: pyrite` `RAW_TEXT` synonym from `data/ingredients/mapped/Pyrite.yaml` or filter process-qualified raw labels during SSSOM construction. Then regenerate SSSOM and rerun `scripts/validate_sssom_invariants.py` plus the final `other` synonym review.
