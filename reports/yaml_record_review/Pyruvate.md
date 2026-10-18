# `data/ingredients/mapped/Pyruvate.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Pyruvate` is mapped exactly to active `CHEBI:15361` / `pyruvate`, the conjugate-base anion of pyruvic acid. OLS4 CHEBI confirms the anion term with `2-oxopropanoate` as an exact synonym, and PubChem lookup by CAS `57-60-3` confirms the stored anion formula, SMILES, and InChI.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pyruvate.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Pyruvate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The CultureMech import, KG-Microbe synonym, PubChem CAS lookup, and OAK/OLS row review support the exact CHEBI anion identity. Final SSSOM row 2471 exports only `2-oxopropanoate` and `CAS:57-60-3`, so it does not leak pyruvic acid or sodium pyruvate aliases from neighboring records.

**Completeness**: The active `CARBON_SOURCE` and `ENERGY_SOURCE` roles are still `COMPUTATIONAL_PREDICTION` assertions from name-list and energy-source inference, both with provisional curator notes and no source-backed CultureMech recipe evidence.

**Recommended Edits**: Replace `nutritional_roles.CARBON_SOURCE` and `nutritional_roles.ENERGY_SOURCE` with source-backed evidence scoped to recipes that use pyruvate in those roles, or remove either role if the source table cannot support it. Then synchronize `data/curated/mapped_ingredients.yaml` and rerun strict validation plus `scripts/validate_sssom_invariants.py`.
