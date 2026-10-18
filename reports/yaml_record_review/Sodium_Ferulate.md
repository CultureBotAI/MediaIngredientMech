# `data/ingredients/mapped/Sodium_Ferulate.yaml`

**Verdict**: pass.

**Identity**: `Sodium ferulate` maps exactly to active, defining
`CHEBI:114954` / `sodium ferulate`. Fresh OLS4 lookup confirmed the ChEBI
label, CAS RN `24276-84-4`, formula `C10H9O4.Na`, InChI, InChIKey, SMILES,
and exact IUPAC synonym. PubChem resolves the CAS RN to CID `23669636` with
the same formula, InChI, InChIKey, and structure.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Dodecyl_Sulfate.yaml
data/ingredients/mapped/Sodium_Ethyl_Sulfate.yaml
data/ingredients/mapped/Sodium_Ferric_EDTA.yaml
data/ingredients/mapped/Sodium_Ferulate.yaml
data/ingredients/mapped/Sodium_Fluoroacetate.yaml` passed for the 5-file batch
with 0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed.

**Evidence**: The exact CHEBI identity, CAS RN, formula, InChI, SMILES, and
exact IUPAC synonym pass. Final SSSOM row 2640 exports only the exact IUPAC
name plus `CAS:24276-84-4` in `other`, both valid same-substance tokens. The
per-record YAML agrees with the regenerated aggregate row when keyed by
identifier and preferred term.

**Completeness**: The record has refreshed 3-occurrence statistics, no roles
needing evidence review, and no stale broader or raw occurrence synonyms in
final SSSOM.

**Recommended Edits**: None.
