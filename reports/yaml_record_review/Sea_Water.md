# `data/ingredients/mapped/Sea_Water.yaml`

**Verdict**: pass.

**Identity**: `Sea water` is a rejected duplicate of active `Seawater`; both
records use active, defining `ENVO:00002149` / `sea water`. Fresh OLS4 lookup
resolved the ENVO term, and the tombstone correctly records that the duplicate
was merged into `Seawater`.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sea_Water.yaml data/ingredients/mapped/Seawater.yaml
data/ingredients/mapped/Sebacic_Acid.yaml data/ingredients/mapped/Selenate.yaml
data/ingredients/mapped/Selenite.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the same 5 files.

**Evidence**: The `MERGED_INTO` history explains that `Sea water` was folded
into `Seawater` under the same `ENVO:00002149` identifier. The per-record YAML
agrees with the regenerated aggregate row when keyed by `(identifier,
preferred_term)`. Final SSSOM has no `MIM:Sea_Water` row because the rejected
tombstone is excluded.

**Completeness**: The duplicate is tombstoned, occurrences are zeroed, and no
roles, components, CAS, or chemical structure fields are asserted.

**Recommended Edits**: None.
