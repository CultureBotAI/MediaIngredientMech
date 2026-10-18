# `data/ingredients/mapped/Polymyxin_B_Sulfate.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Polymyxin B sulfate` maps exactly to `CHEBI:8310` / `Polymyxin B sulfate`. The CHEBI identifier, CAS RN `1405-20-5`, sulfate structure fields, occurrence count, and final SSSOM row 2370 agree.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Polymyxin_B_Sulfate.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Polymyxin_B_Sulfate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The CultureBotHT import supports the CHEBI identity and CAS-bearing source record, and the final SSSOM row exports only `CAS:1405-20-5` in `other`, matching `chemical_properties.cas_rn`. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected curated, generated, row-review, and final SSSOM references.

**Completeness**: The active `physicochemical_roles.SELECTIVE_AGENT` assertion is still only a `COMPUTATIONAL_PREDICTION` from the `infer_roles_from_name_lists` rule with the curator note `Provisional role from a curated name-pattern rule; review recommended.`

**Recommended Edits**: In `data/ingredients/mapped/Polymyxin_B_Sulfate.yaml`, either replace the provisional `SELECTIVE_AGENT` evidence with source-backed evidence scoped to Polymyxin B sulfate or remove the role if no such source exists. Then synchronize `data/curated/mapped_ingredients.yaml` and re-run strict validation plus the SSSOM invariant check.
