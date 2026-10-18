# `data/ingredients/mapped/Propandiamine.yaml`

**Verdict**: pass.

**Identity**: `Propandiamine` is a CAS-derived exact mapping to `CHEBI:15725` / `trimethylenediamine`. OLS4 CHEBI confirms CAS `109-76-2`, formula `C3H10N2`, and the `Propane-1,3-diamine` exact synonym.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Propandiamine.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Propandiamine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The #317 `CAS_RN_LOOKUP` regrade accurately preserves the CAS-to-CHEBI lookup method while final SSSOM row 2425 still emits the record's own CHEBI identifier as `skos:exactMatch`. The `Propane-1,3-diamine` and `CAS:109-76-2` final tokens are exact for the same substance.

**Completeness**: The stored CAS RN and structure agree with CHEBI, and there are no active roles or components requiring further evidence.

**Recommended Edits**: None.
