# `data/ingredients/mapped/Pterin-6-Carboxylic_Acid.yaml`

**Verdict**: pass.

**Identity**: `Pterin-6-Carboxylic Acid` is a CAS-backed exact mapping to `CHEBI:88937` / `2-Amino-4-hydroxy-6-pteridinecarboxylic acid`. OLS4 CHEBI confirms CAS `948-60-7`, the stored formula, SMILES, InChI, and `Pterin-6-carboxylic acid` as a synonym.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pterin-6-Carboxylic_Acid.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Pterin-6-Carboxylic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The #317 `CAS_RN_LOOKUP` grade matches the CAS-to-CHEBI provenance. Final SSSOM row 2438 keeps the correct `skos:exactMatch` predicate for the record's own CHEBI identifier and a valid `CAS:948-60-7` token.

**Completeness**: The record has no active roles, components, or noisy synonyms.

**Recommended Edits**: None.
