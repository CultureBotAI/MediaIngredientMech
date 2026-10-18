# `data/ingredients/mapped/Sodium_Acetate.yaml`

**Verdict**: pass with minor issues.

**Identity**: `Sodium acetate` is a rejected duplicate of the active anhydrous
acetate salt record. Fresh OLS4 lookup resolved active, defining `CHEBI:32954`
with label `sodium acetate`, CAS RN `127-09-3`, formula `C2H3O2.Na`, and an
InChI matching the tombstone.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Acetate.yaml
data/ingredients/mapped/Sodium_Acetate3h2o.yaml
data/ingredients/mapped/Sodium_Acetate_Trihydrate.yaml
data/ingredients/mapped/Sodium_Adipate.yaml
data/ingredients/mapped/Sodium_Alginate.yaml` passed for the 5-file batch with
0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for all 5 OBO-grounded files.

**Evidence**: The per-record YAML agrees with the regenerated aggregate row
when keyed by `(preferred_term, mapping_status)`. Hidden/ignored search of
final `mappings/ingredient_mappings.sssom.tsv` found no
`MIM:Sodium_Acetate` subject row, so the rejected vendor-flavored raw label and
provisional carbon/energy-source roles are contained in the tombstone.

**Completeness**: The rejected status and zero occurrence count agree with the
2026-08-20 merge into `Na-acetate`. The stale roles would be unsupported on an
active record, but they do not publish to final SSSOM while this file remains a
rejected tombstone.

**Recommended Edits**: Optionally strip the provisional nutritional roles from
this rejected tombstone during a dedicated tombstone-normalization pass; no
active YAML or SSSOM row needs repair for this file.
