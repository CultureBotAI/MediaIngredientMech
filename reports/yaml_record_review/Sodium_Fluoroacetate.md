# `data/ingredients/mapped/Sodium_Fluoroacetate.yaml`

**Verdict**: pass.

**Identity**: `Sodium Fluoroacetate` maps exactly to active, defining
`CHEBI:38699` / `sodium fluoroacetate`. Fresh OLS4 lookup confirmed the ChEBI
label, CAS RN `62-74-8`, formula `C2H2FO2.Na`, InChI, InChIKey, SMILES, and
same-substance synonyms. PubChem resolves the CAS RN to CID `16212360` with
the same formula, InChI, InChIKey, and structure.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Dodecyl_Sulfate.yaml
data/ingredients/mapped/Sodium_Ethyl_Sulfate.yaml
data/ingredients/mapped/Sodium_Ferric_EDTA.yaml
data/ingredients/mapped/Sodium_Ferulate.yaml
data/ingredients/mapped/Sodium_Fluoroacetate.yaml` passed for the 5-file batch
with 0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed.

**Evidence**: The exact CHEBI identity, CAS RN, formula, InChI, and SMILES
pass. Final SSSOM row 2641 exports only `CAS:62-74-8` in `other`, which is the
same CAS RN recorded locally and by ChEBI. The per-record YAML agrees with the
regenerated aggregate row when keyed by identifier and preferred term.

**Completeness**: The record has no roles or local synonyms needing evidence
review, and no unsafe synonyms are exported to final SSSOM.

**Recommended Edits**: None.
