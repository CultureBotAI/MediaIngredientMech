# `data/ingredients/mapped/Pyrocatechol.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Pyrocatechol` is mapped exactly to active `CHEBI:18135` / `catechol` through a synonym match. OLS4 CHEBI confirms `Pyrocatechol`, `1,2-Benzenediol`, and the other stored aliases on the same catechol term, and PubChem lookup by CAS `120-80-9` confirms the stored formula and InChI.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pyrocatechol.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Pyrocatechol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The CultureMech import, PubChem CAS lookup, KG-Microbe synonyms, and OAK/OLS row review support the same CHEBI identity. Final SSSOM row 2465 exports only catechol-specific synonyms and `CAS:120-80-9`; the raw `Role: Carbon source` import text is correctly filtered out.

**Completeness**: The active `nutritional_roles.CARBON_SOURCE` assertion is still only a `COMPUTATIONAL_PREDICTION` from in-session Claude reasoning with no external API, source table, or recipe evidence. The CultureMech raw role hints at carbon-source usage, but the active role facet is not supported by source-backed evidence.

**Recommended Edits**: Replace `nutritional_roles.CARBON_SOURCE` with source-backed CultureMech occurrence evidence scoped to recipes that use pyrocatechol as a carbon source, or remove the role if the source table cannot support it. Then synchronize `data/curated/mapped_ingredients.yaml` and rerun strict validation plus `scripts/validate_sssom_invariants.py`.
