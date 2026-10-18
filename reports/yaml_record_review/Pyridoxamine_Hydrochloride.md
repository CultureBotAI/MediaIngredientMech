# `data/ingredients/mapped/Pyridoxamine_Hydrochloride.yaml`

**Verdict**: pass.

**Identity**: `Pyridoxamine hydrochloride` is mapped exactly to active `CHEBI:131531` / `pyridoxamine hydrochloride`. OLS4 CHEBI confirms the same monohydrochloride term and salt-scoped aliases, and PubChem lookup by CAS `5103-96-8` confirms the stored formula, SMILES, and InChI.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pyridoxamine_Hydrochloride.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Pyridoxamine_Hydrochloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The CultureMech import, PubChem/CHEBI CAS lookups, KG-Microbe synonyms, and row-review manifest support the exact CHEBI salt identity. Final SSSOM row 2459 preserves monohydrochloride-specific aliases and `CAS:5103-96-8`; it does not leak free-base or dihydrochloride labels.

**Completeness**: The `VITAMIN_SOURCE` role is backed by CultureMech `DATABASE_ENTRY` evidence for use as `Vitamin`. The record has no components or unsupported final synonyms.

**Recommended Edits**: None.
