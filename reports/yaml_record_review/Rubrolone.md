# `data/ingredients/mapped/Rubrolone.yaml`

**Verdict**: pass.

**Identity**: `Rubrolone` maps exactly to active, defining `CHEBI:140148` /
`rubrolone`. Fresh OLS4 lookup resolved the ChEBI term with the same formula,
InChI, and SMILES as the record.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Roxithromycin.yaml
data/ingredients/mapped/Rubidium_Chloride.yaml
data/ingredients/mapped/Rubradirin.yaml
data/ingredients/mapped/Rubrolone.yaml
data/ingredients/mapped/Rumen_Fluid.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels` passed
for the same 5 files.

**Evidence**: The MicrobeDecoder import, review promotion, and
single-ingredient classification all point at the same exact ChEBI identity.
The per-record YAML agrees with the regenerated aggregate row when keyed by
`(identifier, preferred_term)`. Final SSSOM row 2537 maps exactly to
`CHEBI:140148` and exports an empty `other` field.

**Completeness**: The exact ChEBI identity, structure, MicrobeDecoder source
occurrence count, and final SSSOM row agree. No roles, components, or CAS
payload are asserted.

**Recommended Edits**: None.
