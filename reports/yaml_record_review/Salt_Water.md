# `data/ingredients/mapped/Salt_Water.yaml`

**Verdict**: pass.

**Identity**: `Salt water` maps exactly to active, defining `ENVO:00002010` /
`saline water`. Fresh OLS4 lookup resolved the ENVO term and still lists
`salt water` as an exact synonym.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Salt_Solution_II.yaml
data/ingredients/mapped/Salt_Water.yaml
data/ingredients/mapped/Salts_Solution.yaml
data/ingredients/mapped/Salvinorin_A.yaml
data/ingredients/mapped/Sandramycin.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the OBO-resolvable subset, `Salt_Water`, `Salvinorin_A`, and
`Sandramycin`; the two `kgmicrobe.ingredient` fallback-registry records in
this batch are outside Engine A coverage.

**Evidence**: The curated OAK/OLS exact audit evidence matches the live OLS4
exact synonym on `ENVO:00002010`. The per-record YAML agrees with the
regenerated aggregate row when keyed by `(identifier, preferred_term)`. Final
SSSOM row 2555 maps exactly to `ENVO:00002010` and exports an empty `other`
field.

**Completeness**: The ENVO exact-synonym identity, raw synonym, undefined-
mixture type, occurrence count, and final SSSOM row agree. No roles,
components, CAS, or chemical structure fields are asserted.

**Recommended Edits**: None.
