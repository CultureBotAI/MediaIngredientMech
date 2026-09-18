# `data/ingredients/mapped/Sodium_L-glutamate.yaml`

**Verdict**: pass.

**Identity**: `Sodium L-glutamate` maps to active, defining `CHEBI:64243` /
`monosodium L-glutamate` by synonym match. Fresh OLS4 lookup confirmed the
ChEBI label, `Sodium L-glutamate` synonym, CAS RN `142-47-2`, formula
`C5H8NO4.Na`, InChI, InChIKey, SMILES, and the stored anhydrous
same-substance synonym set.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Iodate.yaml
data/ingredients/mapped/Sodium_Iodide.yaml
data/ingredients/mapped/Sodium_Iodoacetate.yaml
data/ingredients/mapped/Sodium_Isethionate.yaml
data/ingredients/mapped/Sodium_L-glutamate.yaml` passed for the 5-file batch
with 0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed.

**Evidence**: The anhydrous monosodium L-glutamate identity, formula, InChI,
SMILES, MicrobeDecoder occurrence count, and `Na-glutamate` synonym pass. A
hidden and ignored-inclusive search found the old `Na-glutamate.yaml` record is
a rejected tombstone already reviewed as inert, and final SSSOM row 2652
properly carries `Na-glutamate` only as an `other` token on this live
`CHEBI:64243` row. The per-record YAML agrees with the regenerated aggregate
row when keyed by identifier and preferred term.

**Completeness**: The record has no roles needing evidence review, and no
hydrate, anion, or tombstone-only synonyms leak into final SSSOM.

**Recommended Edits**: None.
