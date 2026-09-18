# `data/ingredients/mapped/Propionic_Acid.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Propionic acid` is mapped exactly to active `CHEBI:30768` / `propionic acid`, not to `CHEBI:17272` / `propionate`. OLS4 CHEBI confirms CAS `79-09-4`, the stored formula, SMILES, InChI, and the KG-Microbe synonym set.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Propionic_Acid.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Propionic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: Final SSSOM row 2429 preserves only acid synonyms and `CAS:79-09-4`, so it does not leak the `Propanoate` anion alias from the separate propionate record. The `CARBON_SOURCE` role is supported by the original CultureMech role text and stored as `DATABASE_ENTRY` evidence. The `ENERGY_SOURCE` role, however, is only a `COMPUTATIONAL_PREDICTION` from `infer_energy_source` with the note `Provisional ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.`

**Completeness**: The identity, structure, CAS, synonyms, carbon-source role, and occurrence counts are complete enough. The remaining unsupported claim is the energy-source role.

**Recommended Edits**: In `data/ingredients/mapped/Propionic_Acid.yaml`, replace `nutritional_roles.ENERGY_SOURCE` with source-backed evidence or remove that role. Synchronize `data/curated/mapped_ingredients.yaml`, regenerate SSSOM if role-derived products change, and rerun strict validation plus `scripts/validate_sssom_invariants.py`.
