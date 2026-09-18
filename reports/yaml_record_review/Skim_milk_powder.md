# `data/ingredients/mapped/Skim_milk_powder.yaml`

**Verdict**: pass.

**Identity**: `Skim milk powder` maps exactly to active, defining
`MICRO:0001241` / `skim milk powder`. Fresh OLS4 lookup resolved the MICRO term
by exact CURIE and exact label, matching the restored CultureMech
occurrence-table grounding.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sio2.yaml
data/ingredients/mapped/Sisomicin_Sulfate_Salt.yaml
data/ingredients/mapped/Skim_milk_powder.yaml
data/ingredients/mapped/Skimmed_Milk.yaml
data/ingredients/mapped/Skirrow_Supplement.yaml` passed for the 5-file batch
with 0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for `Sio2`, `Sisomicin_Sulfate_Salt`, and `Skimmed_Milk`; the MICRO and
kgmicrobe.ingredient records were skipped because those prefixes are outside the
Engine A OBO term-validation subset.

**Evidence**: The exact MICRO identity and final SSSOM row pass. The per-record
YAML agrees with the regenerated aggregate row when keyed by `(identifier,
preferred_term)`. Final SSSOM row 2596 maps exactly to `MICRO:0001241` and
exports an empty `other` field.

**Completeness**: The exact MICRO identity, occurrence counts, and final SSSOM
row agree. No roles, components, CAS, or chemical structure fields are asserted
for this biological ingredient record.

**Recommended Edits**: None.
