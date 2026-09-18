# `data/ingredients/mapped/Pyruvic_Acid.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Pyruvic acid` is mapped exactly to active `CHEBI:32816` / `pyruvic acid`, not to the pyruvate anion or the sodium salt. OLS4 CHEBI confirms the acid term and its acid-specific aliases, and PubChem lookup by CAS `127-17-3` confirms the stored neutral-acid formula, SMILES, and InChI.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pyruvic_Acid.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Pyruvic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The CultureMech import, KG-Microbe synonyms, PubChem CAS lookup, and row-review manifest support the exact acid identity. Final SSSOM row 2472 keeps acid-scoped aliases and `CAS:127-17-3`; the raw `(sodium salt)` string remains YAML provenance and is not exported as `other`.

**Completeness**: The active `CARBON_SOURCE` and `ENERGY_SOURCE` roles are still `COMPUTATIONAL_PREDICTION` assertions from name-list and energy-source inference, both with provisional curator notes and no source-backed CultureMech recipe evidence.

**Recommended Edits**: Replace `nutritional_roles.CARBON_SOURCE` and `nutritional_roles.ENERGY_SOURCE` with source-backed evidence scoped to recipes that use pyruvic acid in those roles, or remove either role if the source table cannot support it. Then synchronize `data/curated/mapped_ingredients.yaml` and rerun strict validation plus `scripts/validate_sssom_invariants.py`.
