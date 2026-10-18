# `data/ingredients/mapped/Serum.yaml`

**Verdict**: pass.

**Identity**: `Serum` maps exactly to active, defining `UBERON:0001977` /
`blood serum`. Fresh OLS4 lookup resolved the UBERON term and still lists
`serum` as an exact synonym.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Serine.yaml
data/ingredients/mapped/Serine_Hydroxamate.yaml
data/ingredients/mapped/Serotonin.yaml data/ingredients/mapped/Serum.yaml
data/ingredients/mapped/Setamycin.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the same 5 files.

**Evidence**: The kgm-metatraits source-preset import and the later
`ontology_source` correction both point at `UBERON:0001977`. The per-record
YAML agrees with the regenerated aggregate row when keyed by `(identifier,
preferred_term)`. Final SSSOM row 2573 maps exactly to `UBERON:0001977` and
exports an empty `other` field.

**Completeness**: The exact UBERON identity, undefined-mixture classification,
and final SSSOM row agree. No roles, components, CAS, or chemical structure
fields are asserted.

**Recommended Edits**: None.
