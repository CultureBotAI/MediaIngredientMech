# `data/ingredients/mapped/Propan-1-ol.yaml`

**Verdict**: pass.

**Identity**: `Propan-1-ol` is mapped exactly to active `CHEBI:28831` / `propan-1-ol`, with CAS `71-23-8`. The stored formula, SMILES, and InChI match the CHEBI term.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Propan-1-ol.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Propan-1-ol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: OLS4 CHEBI lists `Propane-1-ol` and `Propanol` as related synonyms of `CHEBI:28831`, supporting the curated raw aliases from the #213 merge and CultureMech alias backfill. Final SSSOM row 2424 keeps those same aliases plus `CAS:71-23-8`, which matches `chemical_properties.cas_rn`.

**Completeness**: The record has no role assertions or components and no final synonym that crosses into propan-2-ol.

**Recommended Edits**: None.
