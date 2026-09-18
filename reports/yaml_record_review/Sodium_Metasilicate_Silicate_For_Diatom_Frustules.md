# `data/ingredients/mapped/Sodium_Metasilicate_Silicate_For_Diatom_Frustules.yaml`

**Verdict**: pass.

**Identity**: `Sodium metasilicate (silicate for diatom frustules)` is a
rejected tombstone merged into the live `Sodium Metasilicate` record on
`mesh:C025349` / `sodium metasilicate`. Fresh prefix-specific OLS4 lookup
confirmed the MeSH term.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Malonate.yaml
data/ingredients/mapped/Sodium_Metasilicate.yaml
data/ingredients/mapped/Sodium_Metasilicate_Silicate_For_Diatom_Frustules.yaml
data/ingredients/mapped/Sodium_Methanesulfonate.yaml
data/ingredients/mapped/Sodium_Nitrate_070_M_Stock.yaml` passed for the
5-file batch with 0 ERROR rows. Engine A term validation is skipped for this
record because `mesh:` is outside the OBO prefixes handled by the direct
LinkML term-validator recipe.

**Evidence**: The tombstone has zero occurrences, retains the MeSH pointer for
traceability, and names the live `Sodium Metasilicate` target in its
`MERGED_INTO` history. A hidden and ignored-inclusive search found no final
SSSOM subject row for this record. The per-record YAML agrees with the
regenerated aggregate row when keyed by identifier and preferred term.

**Completeness**: The rejected tombstone is inert. The old context label still
needs removal from the live record's final `other` output, but this tombstone
itself no longer publishes a mapping row.

**Recommended Edits**: None for the tombstone.
