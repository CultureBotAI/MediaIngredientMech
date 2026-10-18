# `data/ingredients/mapped/Protocatechuic_Acid.yaml`

**Verdict**: pass.

**Identity**: `Protocatechuic Acid` is a CAS-backed exact mapping to `CHEBI:36062` / `3,4-dihydroxybenzoic acid`, separate from the `CHEBI:36241` anion. OLS4 CHEBI confirms CAS `99-50-3`, the stored formula, SMILES, InChI, and `Protocatechuic acid` as a synonym.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Protocatechuic_Acid.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Protocatechuic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The #317 regrade to `CAS_RN_LOOKUP` accurately records that the CultureBotHT CAS established the CHEBI target. Final SSSOM row 2436 remains `skos:exactMatch` under Rule D and publishes only the matching `CAS:99-50-3` token in `other`.

**Completeness**: The record has no roles, components, or active synonyms requiring further evidence.

**Recommended Edits**: None.
