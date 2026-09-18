# `data/ingredients/mapped/Sodium_Fluorophosphate.yaml`

**Verdict**: pass.

**Identity**: `Sodium Fluorophosphate` maps exactly to active, defining
`CHEBI:86431` / `sodium fluorophosphate`. Fresh OLS4 lookup confirmed the
ChEBI label, formula `FO3P.2Na`, InChI, InChIKey, SMILES, and the exact
`disodium phosphorofluoridate` synonym. PubChem resolves the local CAS RN
`7631-97-2` to CID `24266` with the same InChI, InChIKey, and structure.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Fluorophosphate.yaml
data/ingredients/mapped/Sodium_Gluconate.yaml
data/ingredients/mapped/Sodium_Glutamate_Monohydrate.yaml
data/ingredients/mapped/Sodium_Hypochlorite.yaml
data/ingredients/mapped/Sodium_Hypophosphite_Monohydrate.yaml` passed for the
5-file batch with 0 ERROR rows. Direct `linkml-term-validator validate-data`
with `--labels` passed.

**Evidence**: The exact CHEBI identity, formula, InChI, SMILES, and local CAS
RN pass. Final SSSOM row 2642 exports only `Sodium monofluorophosphate`,
`disodium phosphorofluoridate`, and `CAS:7631-97-2` in `other`, all
same-substance tokens. The per-record YAML agrees with the regenerated
aggregate row when keyed by identifier and preferred term.

**Completeness**: The record has no roles needing evidence review, and no
stale broader or raw occurrence synonyms leak into final SSSOM.

**Recommended Edits**: None.
