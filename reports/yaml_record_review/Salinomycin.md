# `data/ingredients/mapped/Salinomycin.yaml`

**Verdict**: pass.

**Identity**: `Salinomycin` maps exactly to active, defining `CHEBI:80025` /
`Salinomycin`. Fresh OLS4 lookup resolved the ChEBI term with the same formula,
InChI, and SMILES as the record.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Salicylate.yaml
data/ingredients/mapped/Salicylic_Acid.yaml
data/ingredients/mapped/Salidroside.yaml
data/ingredients/mapped/Salinomycin.yaml
data/ingredients/mapped/Salsoline.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the same 5 files.

**Evidence**: The MicrobeDecoder exact-label import, review promotion, and
single-ingredient classification all point at the same exact CHEBI identity.
The per-record YAML agrees with the regenerated aggregate row when keyed by
`(identifier, preferred_term)`. Final SSSOM row 2552 maps exactly to
`CHEBI:80025` and exports an empty `other` field.

**Completeness**: The exact CHEBI identity, structure, MicrobeDecoder source
occurrence count, and final SSSOM row agree. No roles, components, CAS, or
curated synonyms are asserted.

**Recommended Edits**: None.
