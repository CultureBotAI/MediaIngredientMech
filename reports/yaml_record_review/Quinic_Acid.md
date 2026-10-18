# `data/ingredients/mapped/Quinic_Acid.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Quinic acid` is mapped exactly to active `CHEBI:26493` / `quinic acid`, the broad cyclitol carboxylic acid class, while the narrower `(-)-quinic acid` sibling remains separate. OLS4 CHEBI confirms both terms, and PubChem lookup by CAS `7729-33-1` confirms a quinic-acid formula and InChI compatible with the stored CAS.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Quinic_Acid.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Quinic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The CultureMech import, PubChem CAS lookup, and OAK/OLS row review support the broad CHEBI identity. Final SSSOM row 2477 exports only `CAS:7729-33-1`; the KG-Microbe `(-)-quinic acid` synonym was correctly rejected as narrower and does not appear in `other`.

**Completeness**: The active `nutritional_roles.CARBON_SOURCE` assertion is still only a `COMPUTATIONAL_PREDICTION` from `infer_roles_from_name_lists` with the curator note `Provisional role from a curated name-pattern rule; review recommended.`

**Recommended Edits**: Replace `nutritional_roles.CARBON_SOURCE` with source-backed CultureMech occurrence evidence scoped to recipes that use quinic acid as a carbon source, or remove the role if the source table cannot support it. Then synchronize `data/curated/mapped_ingredients.yaml` and rerun strict validation plus `scripts/validate_sssom_invariants.py`.
