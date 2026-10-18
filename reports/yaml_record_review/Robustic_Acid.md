# `data/ingredients/mapped/Robustic_Acid.yaml`

**Verdict**: pass.

**Identity**: `Robustic Acid` uses exact local `cas:5307-59-5` identity rows
plus a narrow parent to active `mesh:C105206` / `robustic acid`. Fresh OLS4
lookup resolved the MeSH parent, and fresh PubChem lookup by the stored CAS
resolved CID 54677407 for a defined `C22H20O6` compound.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Ristocetin_B.yaml data/ingredients/mapped/Rna.yaml
data/ingredients/mapped/Robustic_Acid.yaml
data/ingredients/mapped/Roccellic_Acid.yaml
data/ingredients/mapped/Rolled_Oats.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels` passed
for the same 5 files.

**Evidence**: The per-record YAML agrees with the regenerated aggregate row
when keyed by `(identifier, preferred_term)`. Final SSSOM rows 2524-2526 publish
the MeSH `skos:narrowMatch` plus the required exact CAS and kg-microbe registry
rows. The old `UNKNOWN_TERM` results for the MeSH, CAS, and kg-microbe rows are
already triaged as prefix coverage or expected registry identifiers.

**Completeness**: The CAS-backed local identity, broad MeSH parent, CAS
registry rows, and final SSSOM rows agree. No unsafe synonyms, roles, or
structure-derived values are asserted.

**Recommended Edits**: None.
