# `data/ingredients/mapped/Sodium_Iodate.yaml`

**Verdict**: pass.

**Identity**: `sodium iodate` maps exactly to active, defining `CHEBI:81708` /
`Sodium iodate`. Fresh OLS4 lookup confirmed the ChEBI label, CAS RN
`7681-55-2`, formula `IO3.Na`, InChI, InChIKey, and SMILES, and PubChem
resolves the CAS RN to CID `23675764` with the same formula, InChI, InChIKey,
and structure.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Iodate.yaml
data/ingredients/mapped/Sodium_Iodide.yaml
data/ingredients/mapped/Sodium_Iodoacetate.yaml
data/ingredients/mapped/Sodium_Isethionate.yaml
data/ingredients/mapped/Sodium_L-glutamate.yaml` passed for the 5-file batch
with 0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed.

**Evidence**: The exact CHEBI identity, CAS RN, formula, InChI, and SMILES
pass. Final SSSOM row 2648 exports only `CAS:7681-55-2` in `other`, matching
the local CAS RN and ChEBI xref. The per-record YAML agrees with the
regenerated aggregate row when keyed by identifier and preferred term.

**Completeness**: The record has no roles or local synonyms needing evidence
review, and no unsafe synonyms are exported to final SSSOM.

**Recommended Edits**: None.
