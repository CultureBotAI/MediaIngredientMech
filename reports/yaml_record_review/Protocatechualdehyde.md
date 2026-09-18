# `data/ingredients/mapped/Protocatechualdehyde.yaml`

**Verdict**: pass.

**Identity**: `Protocatechualdehyde` is a CAS-backed exact mapping to `CHEBI:50205` / `3,4-dihydroxybenzaldehyde`. OLS4 CHEBI confirms CAS `139-85-5`, the stored formula, SMILES, InChI, and `Protocatechualdehyde` as a related synonym.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Protocatechualdehyde.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Protocatechualdehyde.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The #317 regrade to `CAS_RN_LOOKUP` accurately records that the CultureBotHT CAS, not the preferred-term synonym, established the CHEBI target. Final SSSOM row 2434 remains `skos:exactMatch` under Rule D and publishes the matching `CAS:139-85-5` token.

**Completeness**: The record has no active roles, components, or synonyms that need additional support.

**Recommended Edits**: None.
