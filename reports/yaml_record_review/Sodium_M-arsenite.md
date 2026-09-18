# `data/ingredients/mapped/Sodium_M-arsenite.yaml`

**Verdict**: pass.

**Identity**: `Sodium m-arsenite` maps to active, defining `CHEBI:29678` /
`sodium arsenite` through an explicit CAS-to-ChEBI lookup. Fresh OLS4 lookup
confirmed the ChEBI label, CAS RN `7784-46-5`, formula `AsO2.Na`, InChI,
InChIKey, SMILES, and the exact `catena-poly[(oxidoarsenate-mu-oxido)]sodium`
IUPAC synonym, and PubChem resolves the CAS RN to CID `443495` with the same
formula, InChI, InChIKey, and structure.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_L-lactate.yaml
data/ingredients/mapped/Sodium_Lactate.yaml
data/ingredients/mapped/Sodium_M-arsenite.yaml
data/ingredients/mapped/Sodium_Malate.yaml
data/ingredients/mapped/Sodium_Maleate.yaml` passed for the 5-file batch with
0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed.

**Evidence**: The CAS-to-ChEBI identity, CAS RN, formula, InChI, SMILES, exact
IUPAC synonym, and final SSSOM row 2654 pass. The `other` column exports only
`catena-poly[(oxidoarsenate-mu-oxido)]sodium` and `CAS:7784-46-5`, both
same-substance tokens. The per-record YAML agrees with the regenerated
aggregate row when keyed by identifier and preferred term.

**Completeness**: The record has no roles needing evidence review, and no
unsafe synonyms are exported to final SSSOM.

**Recommended Edits**: None.
