# `data/ingredients/mapped/Salicylate.yaml`

**Verdict**: pass.

**Identity**: `Salicylate` maps exactly to active, defining `CHEBI:30762` /
`salicylate`. Fresh OLS4 lookup resolved the ChEBI term and agreed with the
record's CultureMech-restored `EXACT_MATCH` grounding.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Salicylate.yaml
data/ingredients/mapped/Salicylic_Acid.yaml
data/ingredients/mapped/Salidroside.yaml
data/ingredients/mapped/Salinomycin.yaml
data/ingredients/mapped/Salsoline.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the same 5 files.

**Evidence**: The occurrence-table evidence in `ontology_mapping.evidence`
matches the restored creation history and points at the same exact CHEBI
identity. The per-record YAML agrees with the regenerated aggregate row when
keyed by `(identifier, preferred_term)`. Final SSSOM row 2549 maps exactly to
`CHEBI:30762` and exports an empty `other` field.

**Completeness**: The exact CHEBI identity and final SSSOM row agree. No
roles, components, CAS, or local structure fields are asserted.

**Recommended Edits**: None.
