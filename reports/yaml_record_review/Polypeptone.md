# `data/ingredients/mapped/Polypeptone.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Polypeptone` denotes a commercial peptone product family, including Polypeptone and Hipolypepton variants, but the record uses `FOODON:03315306` / `protein hydrolyzates` as both its identifier and ontology ID while also marking the mapping as `CLOSE_MATCH`. That collapses a narrower product-family identity onto its broader FOODON parent; final SSSOM row 2371 therefore publishes the parent FOODON term as an exact identity row.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Polypeptone.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Polypeptone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed, confirming the FOODON parent label even though the grounding is broader than the MIM subject.

**Evidence**: The FOODON promotion note itself says no exact FOODON term exists and that `protein hydrolyzates` is a parent. The manual synonyms and CultureMech aliases are scoped to the Polypeptone/Hipolypepton family, not every protein hydrolyzate. The active `nutritional_roles.PROTEIN_SOURCE` assertion is still only a `COMPUTATIONAL_PREDICTION` from the `infer_roles_from_name_lists` rule with the curator note `Provisional role from a curated name-pattern rule; review recommended.` An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected curated, generated, residual-alias, synonym-review, and final SSSOM references.

**Completeness**: The source-specific synonym set is rich, but the product-family identity needs a local exact registry ID with a non-exact FOODON parent row before the final SSSOM can express both the exact Polypeptone/Hipolypepton surface forms and the broader `protein hydrolyzates` grounding honestly.

**Recommended Edits**: Re-curate `data/ingredients/mapped/Polypeptone.yaml` to preserve the Polypeptone/Hipolypepton family with a `kgmicrobe.ingredient` exact identity and keep `FOODON:03315306` only as a non-exact parent mapping. Replace the provisional `PROTEIN_SOURCE` evidence with source-backed CultureMech occurrence evidence or remove the role. Then regenerate SSSOM and re-run strict validation plus `scripts/validate_sssom_invariants.py`.
