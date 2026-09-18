# `data/ingredients/mapped/Sandramycin.yaml`

**Verdict**: pass.

**Identity**: `Sandramycin` maps exactly to active, defining `CHEBI:221703` /
`Sandramycin`. Fresh OLS4 lookup resolved the ChEBI term with the same formula,
InChI, and SMILES as the record.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Salt_Solution_II.yaml
data/ingredients/mapped/Salt_Water.yaml
data/ingredients/mapped/Salts_Solution.yaml
data/ingredients/mapped/Salvinorin_A.yaml
data/ingredients/mapped/Sandramycin.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the OBO-resolvable subset, `Salt_Water`, `Salvinorin_A`, and
`Sandramycin`; the two `kgmicrobe.ingredient` fallback-registry records in
this batch are outside Engine A coverage.

**Evidence**: The MicrobeDecoder exact-label import, review promotion, and
single-ingredient classification all point at the same exact CHEBI identity.
The per-record YAML agrees with the regenerated aggregate row when keyed by
`(identifier, preferred_term)`. Final SSSOM row 2558 maps exactly to
`CHEBI:221703` and exports an empty `other` field.

**Completeness**: The exact CHEBI identity, structure, MicrobeDecoder source
occurrence count, and final SSSOM row agree. No roles, components, CAS, or
curated synonyms are asserted.

**Recommended Edits**: None.
