# `data/ingredients/mapped/Sarcidin.yaml`

**Verdict**: pass.

**Identity**: `Sarcidin` is intentionally retained on the local
`kgmicrobe.compound:sarcidin` placeholder. Fresh OLS4 search across CHEBI and
NCIT found no exact external replacement, consistent with the 2026-05-10
placeholder review and row-review triage.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sarcidin.yaml data/ingredients/mapped/Sarcosine.yaml
data/ingredients/mapped/Sclareolide.yaml
data/ingredients/mapped/Scopoletin.yaml
data/ingredients/mapped/Sea_Salts.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the OBO-resolvable subset, `Sarcosine`, `Sclareolide`,
`Scopoletin`, and `Sea_Salts`; the `kgmicrobe.compound` placeholder is outside
Engine A coverage.

**Evidence**: The kg-microbe placeholder import and the later UNKNOWN_TERM
review both document that no exact OLS candidate or normalized local duplicate
supported promotion. The per-record YAML agrees with the regenerated aggregate
row when keyed by `(identifier, preferred_term)`. Final SSSOM row 2559 maps
exactly to `kgmicrobe.compound:sarcidin` and exports an empty `other` field.

**Completeness**: The placeholder identity, single-ingredient type, and final
SSSOM row agree. No roles, components, CAS, or chemical structure fields are
asserted.

**Recommended Edits**: None.
