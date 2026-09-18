# `data/ingredients/mapped/Protocatechuate.yaml`

**Verdict**: pass.

**Identity**: `Protocatechuate` is mapped to active `CHEBI:36241` / `3,4-dihydroxybenzoate`, the anion form. OLS4 CHEBI confirms `protocatechuate` as a synonym and the stored anion formula, SMILES, and InChI.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Protocatechuate.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Protocatechuate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The #213 promotion note explicitly distinguishes the anion from protocatechuic acid, and final SSSOM row 2435 publishes only the exact anion row with no acid CAS or synonym leakage.

**Completeness**: The record has the expected MicrobeDecoder provenance plus one refreshed CultureMech occurrence, and no CAS, roles, components, or extra final synonyms that need additional support.

**Recommended Edits**: None.
