# `data/ingredients/mapped/Selenate.yaml`

**Verdict**: pass.

**Identity**: `Selenate` maps exactly to active, defining `CHEBI:15075` /
`selenate`. Fresh OLS4 lookup resolved the ChEBI term with the same formula,
InChI, and SMILES as the record.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sea_Water.yaml data/ingredients/mapped/Seawater.yaml
data/ingredients/mapped/Sebacic_Acid.yaml data/ingredients/mapped/Selenate.yaml
data/ingredients/mapped/Selenite.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the same 5 files.

**Evidence**: The MicrobeDecoder exact-label import, review promotion, and
single-ingredient classification all point at the same exact CHEBI identity.
The per-record YAML agrees with the regenerated aggregate row when keyed by
`(identifier, preferred_term)`. Final SSSOM row 2568 maps exactly to
`CHEBI:15075` and exports an empty `other` field.

**Completeness**: The exact CHEBI identity, structure, MicrobeDecoder source
occurrence count, and final SSSOM row agree. No roles, components, CAS, or
curated synonyms are asserted.

**Recommended Edits**: None.
