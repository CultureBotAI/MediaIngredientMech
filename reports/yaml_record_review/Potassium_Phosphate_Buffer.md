# `data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Potassium phosphate buffer` is preserved as the local exact identity `kgmicrobe.ingredient:potassium_phosphate_buffer` with a `CLOSE_MATCH` parent row to `NCIT:C29321` / `Phosphate Buffer`. That row shape correctly avoids equating a potassium-buffer formulation family with the generic NCIT phosphate-buffer class.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Potassium_Phosphate_Buffer.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The 2026-05-05 curation event supports keeping the local exact identity plus NCIT close row, and final SSSOM rows 2401 and 2402 preserve both surfaces. However, row 2401 still exports concentration- and pH-qualified recipe text, plus `Potassium phosphate buffer* (see below)`, as `other` synonyms. Those labels are formulation-specific recipe surfaces, not general names for the exact local registry subject. The active `physicochemical_roles.BUFFER` assertion is still only a `COMPUTATIONAL_PREDICTION` from the `infer_roles_from_name_lists` rule with the curator note `Provisional role from a curated name-pattern rule; review recommended.`

**Completeness**: The record has 44 source occurrences and the correct local identity shape, but it has no component or concentration model that can represent the distinct 0.01 M, 0.02 M, and 1 M pH-specific formulations now living as raw synonyms. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected final NCIT close row, local exact row, and corresponding Sodium_Potassium_Phosphate_Buffer sibling pattern.

**Recommended Edits**: In `data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml`, move the pH- and molarity-qualified labels out of active synonyms or teach the SSSOM builder to filter them from `other`. Replace the provisional `BUFFER` role with source-backed evidence or remove it, and add component/concentration recipes if a source can define each buffer formulation. Synchronize `data/curated/mapped_ingredients.yaml`, regenerate SSSOM, and rerun strict validation plus `scripts/validate_sssom_invariants.py`.
