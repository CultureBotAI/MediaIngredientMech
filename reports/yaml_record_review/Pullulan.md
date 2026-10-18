# `data/ingredients/mapped/Pullulan.yaml`

**Verdict**: pass.

**Identity**: `Pullulan` is mapped exactly to active `CHEBI:27941` / `pullulan`. OLS4 CHEBI confirms CAS `9057-02-7`, and the stored polymer formula and SMILES agree with the CHEBI pullulan entry.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pullulan.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Pullulan.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The CultureMech import, CAS backfill, and row-review manifest all support the same CHEBI identity. Final SSSOM row 2440 maps `MIM:Pullulan` to `CHEBI:27941` and keeps only the registry `CAS:9057-02-7` token in `other`; the raw CultureMech `Role:` / `Properties:` text remains YAML provenance and is filtered out of final SSSOM.

**Completeness**: The `CARBON_SOURCE` role is backed by `DATABASE_ENTRY` evidence imported from CultureMech with the original `Carbon Source` role text, so it is source-backed rather than a provisional name-pattern prediction.

**Recommended Edits**: None.
