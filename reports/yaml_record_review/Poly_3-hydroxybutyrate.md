# `data/ingredients/mapped/Poly_3-hydroxybutyrate.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Poly(3-hydroxybutyrate)` maps exactly to `CHEBI:53389` / `poly(3-hydroxybutyrate)`. The CHEBI identifier, canonical label, CultureMech source, polymer formula, KG-Microbe synonyms, and final SSSOM row 2357 agree.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Poly_3-hydroxybutyrate.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Poly_3-hydroxybutyrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The CHEBI mapping supports the exact polymer identity, and the row-review manifest shows that the candidate synonym-enrichment text was already represented. Final SSSOM row 2357 exports only real PHB synonyms; the raw `Role: Carbon source` synonym remains in YAML as CultureMech import provenance and is not emitted as `other`. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected curated, generated, row-review, and final SSSOM references.

**Completeness**: The active `nutritional_roles.CARBON_SOURCE` assertion is still only a `COMPUTATIONAL_PREDICTION` from the `infer_roles_from_name_lists` rule with the curator note `Provisional role from a curated name-pattern rule; review recommended.` The original CultureMech role text suggests the right role, but the active role facet is not supported at the narrowest claim with source evidence.

**Recommended Edits**: In `data/ingredients/mapped/Poly_3-hydroxybutyrate.yaml`, replace the provisional `CARBON_SOURCE` evidence with source-backed CultureMech occurrence evidence scoped to the recipes that use PHB as a carbon source, or remove the role if the source table cannot support it. Then synchronize `data/curated/mapped_ingredients.yaml` and re-run strict validation plus the SSSOM invariant check.
