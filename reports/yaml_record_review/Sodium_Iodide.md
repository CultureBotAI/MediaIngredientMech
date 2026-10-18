# `data/ingredients/mapped/Sodium_Iodide.yaml`

**Verdict**: pass.

**Identity**: `sodium iodide` maps exactly to active, defining `CHEBI:33167` /
`sodium iodide`. Fresh OLS4 lookup confirmed the ChEBI label, CAS RN
`7681-82-5`, formula `I.Na`, InChI, InChIKey, SMILES, and same-substance
synonyms, and PubChem resolves the CAS RN to CID `5238` with the same formula,
InChI, InChIKey, and structure.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Iodate.yaml
data/ingredients/mapped/Sodium_Iodide.yaml
data/ingredients/mapped/Sodium_Iodoacetate.yaml
data/ingredients/mapped/Sodium_Isethionate.yaml
data/ingredients/mapped/Sodium_L-glutamate.yaml` passed for the 5-file batch
with 0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed.

**Evidence**: The exact CHEBI identity, CAS RN, formula, InChI, and SMILES
pass. Final SSSOM row 2649 exports only `CAS:7681-82-5` in `other`, matching
the local CAS RN and ChEBI xref. The per-record YAML agrees with the
regenerated aggregate row when keyed by identifier and preferred term.

**Completeness**: The record has refreshed 6-occurrence statistics, no roles
needing evidence review, and no unsafe synonyms in final SSSOM.

**Recommended Edits**: None.
