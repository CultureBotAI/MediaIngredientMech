# `data/ingredients/mapped/Sodium_Citrate.yaml`

**Verdict**: pass with minor issues.

**Identity**: `Sodium Citrate` is a rejected duplicate merged into the active
`Na3-citrate_X_2_H2o` dihydrate record. Fresh OLS4 lookup confirmed that
`CHEBI:32142` is `sodium citrate dihydrate`, and PubChem resolves the
hydrate-specific CAS RN `6132-04-3` to the same dihydrate InChIKey.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Carbonate_Solution.yaml
data/ingredients/mapped/Sodium_Chlorite.yaml
data/ingredients/mapped/Sodium_Cholate_Hydrate.yaml
data/ingredients/mapped/Sodium_Chromate.yaml
data/ingredients/mapped/Sodium_Citrate.yaml` passed for the 5-file batch with
0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed.

**Evidence**: The tombstone pointer to `CHEBI:32142` is current, and the
per-record YAML agrees with the regenerated aggregate row when keyed by
`(preferred_term, mapping_status)`. Hidden/ignored search of final
`mappings/ingredient_mappings.sssom.tsv` found no `MIM:Sodium_Citrate`
subject row, so the stale anhydrous formula and mixed anhydrous/dihydrate
kg-microbe synonyms are contained in the rejected tombstone.

**Completeness**: The active dihydrate sibling holds the publishing identity
for CAS RN `6132-04-3`. The stale chemical properties and synonyms here are
only tombstone cleanup.

**Recommended Edits**: Optionally remove the stale anhydrous formula and
ambiguous kg-microbe synonyms during a tombstone-normalization pass; no final
SSSOM row is emitted for this slug.
