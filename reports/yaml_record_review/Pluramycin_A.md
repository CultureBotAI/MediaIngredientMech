# `data/ingredients/mapped/Pluramycin_A.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Pluramycin A` is preserved as the local exact identity `kgmicrobe.compound:pluramycin_a` with a `NARROW_MATCH` parent mapping to MeSH `mesh:C003169` / `pluramycin`. Final SSSOM rows 2353 and 2354 correctly publish both the MeSH parent `skos:narrowMatch` row and the sibling local `skos:exactMatch` identity row.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pluramycin_A.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Pluramycin_A.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: A fresh MeSH OLS exact lookup resolved `pluramycin` to `mesh:C003169`, matching the stored broader parent term; an exact `pluramycin A` OLS lookup still found that broader `pluramycin` hit rather than a specific Pluramycin A target. The row-review manifest classifies both final rows as expected: missing-prefix validator coverage for the MeSH parent and an expected local registry identity row for `kgmicrobe.compound:pluramycin_a`. The final SSSOM rows have no `other` synonyms to triage. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected curated, generated, row-review, and final SSSOM references.

**Completeness**: The active `physicochemical_roles.SELECTIVE_AGENT` assertion is still only a `COMPUTATIONAL_PREDICTION` from the `infer_roles_from_name_lists` rule with the curator note `Provisional role from a curated name-pattern rule; review recommended.` That is not source evidence that this record functions as a selective agent in a medium.

**Recommended Edits**: In `data/ingredients/mapped/Pluramycin_A.yaml`, either replace the provisional `SELECTIVE_AGENT` evidence with source-backed evidence scoped to Pluramycin A or remove the role if no such medium-use source exists. Then synchronize `data/curated/mapped_ingredients.yaml` and re-run strict validation plus the SSSOM invariant check.
