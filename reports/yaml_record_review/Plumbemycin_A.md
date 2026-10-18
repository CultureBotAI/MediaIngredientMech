# `data/ingredients/mapped/Plumbemycin_A.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Plumbemycin A` maps exactly to MeSH `mesh:C096638` / `plumbemycin A` after promotion from the kg-microbe placeholder namespace. The identifier, preferred term, MeSH exact mapping, and final SSSOM row 2351 agree.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Plumbemycin_A.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Plumbemycin_A.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: A fresh MeSH OLS exact lookup for `plumbemycin A` returned `mesh:C096638`, matching the stored ontology ID and label. The row-review manifest already classifies the older `UNKNOWN_TERM` stamp as a missing-prefix validator coverage issue. Final SSSOM row 2351 uses the expected `registry:mesh` object source and has no `other` synonyms to triage. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected curated, generated, row-review, and final SSSOM references.

**Completeness**: The active `physicochemical_roles.SELECTIVE_AGENT` assertion is still only a `COMPUTATIONAL_PREDICTION` from the `infer_roles_from_name_lists` rule with the curator note `Provisional role from a curated name-pattern rule; review recommended.` That is not source evidence that this record functions as a selective agent in a medium.

**Recommended Edits**: In `data/ingredients/mapped/Plumbemycin_A.yaml`, either replace the provisional `SELECTIVE_AGENT` evidence with source-backed evidence scoped to Plumbemycin A or remove the role if no such medium-use source exists. Then synchronize `data/curated/mapped_ingredients.yaml` and re-run strict validation plus the SSSOM invariant check.
