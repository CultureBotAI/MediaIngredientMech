# `data/ingredients/mapped/Sheep_blood.yaml`

**Verdict**: pass.

**Identity**: `Sheep blood` maps exactly to active, defining
`MICRO:0001230` / `sheep blood`. Fresh OLS4 lookup resolved the MICRO term by
exact CURIE and exact label, matching the restored CultureMech occurrence-table
grounding.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sheep_blood.yaml
data/ingredients/mapped/Shikimic_Acid.yaml
data/ingredients/mapped/Showdomycin.yaml
data/ingredients/mapped/Sialyllacto-N-tetraose_A.yaml
data/ingredients/mapped/Sialyllacto-N-tetraose_C.yaml` passed for the 5-file
batch with 0 ERROR rows. Direct `linkml-term-validator validate-data` with
`--labels` passed for the 4 CHEBI files; `Sheep_blood` was skipped because
`MICRO` is outside the Engine A CHEBI/OBO term-validation subset.

**Evidence**: The exact MICRO identity and final SSSOM row pass. The per-record
YAML agrees with the regenerated aggregate row when keyed by `(identifier,
preferred_term)`. Final SSSOM row 2575 maps exactly to `MICRO:0001230` and
exports an empty `other` field.

**Completeness**: The exact MICRO identity and final SSSOM row agree. No roles,
components, CAS, or chemical structure fields are asserted for this biological
ingredient record.

**Recommended Edits**: None.
