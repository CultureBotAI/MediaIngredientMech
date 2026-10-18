# `data/ingredients/mapped/Polygalacturonic_Acid.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `polygalacturonic acid` maps exactly to `CHEBI:62969` / `polygalacturonic acid`. The CHEBI identity and CultureBotHT CAS `25990-10-7` agree with final SSSOM row 2364.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Polygalacturonic_Acid.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Polygalacturonic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The exact CHEBI mapping is sound, but the final SSSOM row still exports `filtered, polygalacturonic acid (ultrapure)` and `autoclaved, polygalacturonic acid` in `other`. Those are process-qualified source labels, not true synonyms of the polymer. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the active raw process labels, synonym-enrichment review, and final SSSOM row that still emits them.

**Completeness**: The active `nutritional_roles.CARBON_SOURCE` assertion is still only a `COMPUTATIONAL_PREDICTION` from CHEBI carbohydrate ancestry with the curator note `Provisional role inferred from CHEBI is_a/has_role closure; review recommended.`

**Recommended Edits**: In `data/ingredients/mapped/Polygalacturonic_Acid.yaml`, keep the process-qualified raw labels as provenance only or move them to a filtered field so final SSSOM `other` emits only real synonyms. Replace the provisional `CARBON_SOURCE` evidence with source-backed evidence scoped to polygalacturonic acid medium use, or remove the role. Then synchronize `data/curated/mapped_ingredients.yaml`, regenerate the SSSOM, and rerun strict validation plus `scripts/validate_sssom_invariants.py`.
