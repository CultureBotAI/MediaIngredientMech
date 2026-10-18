# `data/ingredients/mapped/Sludge.yaml`

**Verdict**: pass.

**Identity**: `Sludge` maps exactly to active, defining `ENVO:00002044` /
`sludge`. Fresh OLS4 lookup resolved the ENVO term by exact CURIE and exact
label, matching the local label-exact ENVO upgrade.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sludge.yaml
data/ingredients/mapped/Sludge_fluid.yaml
data/ingredients/mapped/Sn-Glycerol_3-phosphate_Lithium_Salt.yaml
data/ingredients/mapped/Sn-glycero-3-phosphocholine.yaml
data/ingredients/mapped/Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt.yaml`
passed for the 5-file batch with 0 ERROR rows. Direct
`linkml-term-validator validate-data` with `--labels` passed for the ENVO and
3 CHEBI files; `Sludge_fluid` was skipped because `MICRO` is outside the Engine
A OBO term-validation subset.

**Evidence**: The exact ENVO identity, undefined-mixture classification, and
occurrence count refresh pass. The per-record YAML agrees with the regenerated
aggregate row when keyed by `(identifier, preferred_term)`. Final SSSOM row
2599 maps exactly to `ENVO:00002044` and exports an empty `other` field.

**Completeness**: The exact ENVO identity, undefined-mixture classification,
occurrence counts, and final SSSOM row agree. No roles, components, CAS, or
chemical structure fields are asserted.

**Recommended Edits**: None.
