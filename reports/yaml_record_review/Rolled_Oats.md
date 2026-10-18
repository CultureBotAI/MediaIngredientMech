# `data/ingredients/mapped/Rolled_Oats.yaml`

**Verdict**: pass.

**Identity**: `Rolled oats` maps exactly to active, defining
`FOODON:03307110` / `rolled oats`. Fresh OLS4 lookup resolved the FOODON CURIE
with the same canonical label.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Ristocetin_B.yaml data/ingredients/mapped/Rna.yaml
data/ingredients/mapped/Robustic_Acid.yaml
data/ingredients/mapped/Roccellic_Acid.yaml
data/ingredients/mapped/Rolled_Oats.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels` passed
for the same 5 files.

**Evidence**: The per-record YAML agrees with the regenerated aggregate row
when keyed by `(identifier, preferred_term)`. Final SSSOM row 2528 maps exactly
to `FOODON:03307110` and exports an empty `other` field.

**Completeness**: The FOODON identity, mim-queue provenance, undefined-mixture
classification, refreshed 9-occurrence count, and final SSSOM row agree. No
roles, components, or chemical properties are asserted.

**Recommended Edits**: None.
