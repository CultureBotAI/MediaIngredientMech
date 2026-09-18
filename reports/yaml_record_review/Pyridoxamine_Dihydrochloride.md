# `data/ingredients/mapped/Pyridoxamine_Dihydrochloride.yaml`

**Verdict**: pass.

**Identity**: `Pyridoxamine Dihydrochloride` is mapped exactly to active `CHEBI:131532` / `pyridoxamine dihydrochloride`. OLS4 CHEBI confirms the same two-HCl salt term and salt-scoped aliases, and PubChem lookup by CAS `524-36-7` confirms the stored formula, SMILES, and InChI.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pyridoxamine_Dihydrochloride.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Pyridoxamine_Dihydrochloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The CultureMech import, CultureBotHT CAS confirmation, KG-Microbe synonyms, and row-review manifest support the exact CHEBI salt identity. Final SSSOM row 2458 preserves salt-specific two-HCl aliases and `CAS:524-36-7`; it does not leak monohydrochloride or free-base synonyms from the adjacent pyridoxamine records.

**Completeness**: The `VITAMIN_SOURCE` role is backed by `DATABASE_ENTRY` evidence imported from CultureMech with the original `Vitamin Source` role text. The record has no components or unsupported final synonyms.

**Recommended Edits**: None.
