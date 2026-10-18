# `data/ingredients/mapped/Sake.yaml`

**Verdict**: pass.

**Identity**: `Sake` maps exactly to active, defining `FOODON:03301670` /
`sake`. Fresh OLS4 lookup resolved the FOODON term with the same canonical
label.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/S-isocorydine.yaml
data/ingredients/mapped/Saccharin.yaml data/ingredients/mapped/Safrole.yaml
data/ingredients/mapped/Sake.yaml data/ingredients/mapped/Salicin.yaml` passed
for the 5-file batch with 0 ERROR rows. Direct `linkml-term-validator
validate-data` with `--labels` passed for the same 5 files.

**Evidence**: The CultureMech residual grounding records three `Sake` mentions
mapped by exact label to `FOODON:03301670`, and the later evidence-restoration
pass put the same source into the structured mapping evidence read by the SSSOM
builder. The per-record YAML agrees with the regenerated aggregate row when
keyed by `(identifier, preferred_term)`. Final SSSOM row 2547 maps exactly to
`FOODON:03301670` and exports an empty `other` field.

**Completeness**: The FOODON identity, CultureMech evidence restoration,
occurrence count, and final SSSOM row agree. No roles, components, or chemical
properties are asserted.

**Recommended Edits**: None.
