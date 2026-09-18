# `data/ingredients/mapped/Sodium_Acetate3h2o.yaml`

**Verdict**: pass with minor issues.

**Identity**: `Sodium_Acetate3h2o` is a rejected hydrate duplicate merged into
`Sodium_Acetate_Trihydrate`. The tombstone points at active, defining
`CHEBI:32138` / `sodium acetate trihydrate`, and fresh OLS4 plus PubChem
lookups confirmed CAS RN `6131-90-4`, the hydrate-specific InChIKey, and the
trihydrate formula now used by the active record.

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
`MIM:Sodium_Acetate3h2o` subject row, so the tombstone's stale anhydrous CAS,
anhydrous structure, and anhydrous exact synonyms do not reach final SSSOM.

**Completeness**: The active `Sodium_Acetate_Trihydrate` record carries the
correct hydrate CAS RN, formula, and exact CHEBI identity. The stale anhydrous
payload left behind here is only a non-publishing tombstone cleanup issue.

**Recommended Edits**: Optionally remove the stale anhydrous CAS, structure,
and synonyms from this rejected tombstone during a tombstone-normalization
pass; no active SSSOM row is emitted for this slug.
