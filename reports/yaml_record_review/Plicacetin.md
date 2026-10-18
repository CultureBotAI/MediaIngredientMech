# `data/ingredients/mapped/Plicacetin.yaml`

**Verdict**: pass.

**Identity**: `Plicacetin` is mapped exactly to MeSH `mesh:C000633628` / `plicacetin` after promotion from the kg-microbe placeholder namespace. The identifier, preferred term, `SINGLE_INGREDIENT` classification, MeSH exact mapping, and final SSSOM row 2349 agree.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Plicacetin.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Plicacetin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: A fresh MeSH OLS exact lookup resolved `plicacetin` to `mesh:C000633628`, matching the stored ontology ID and label. The row-review manifest already classifies the older `UNKNOWN_TERM` stamp as a missing-prefix validator coverage issue, not a mapping defect. Final SSSOM row 2349 uses the expected `registry:mesh` object source and has no `other` synonyms to triage. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected curated, generated, row-review, and final SSSOM references.

**Completeness**: The record has a stable exact MeSH identity and no unsupported active roles, components, or synonyms. The zero occurrence count is consistent with a kg-microbe metatraits placeholder import rather than a medium occurrence.

**Recommended Edits**: None.
