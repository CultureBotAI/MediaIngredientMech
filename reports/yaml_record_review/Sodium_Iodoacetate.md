# `data/ingredients/mapped/Sodium_Iodoacetate.yaml`

**Verdict**: pass.

**Identity**: `Sodium iodoacetate` maps exactly to active, defining
`CHEBI:234594` / `Sodium iodoacetate`. Fresh OLS4 lookup confirmed the ChEBI
label, CAS RN `305-53-3`, formula `C2H2IO2.Na`, InChI, InChIKey, SMILES, and
same-substance synonym, and PubChem resolves the CAS RN to CID `5239` with the
same formula, InChI, InChIKey, and structure.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Iodate.yaml
data/ingredients/mapped/Sodium_Iodide.yaml
data/ingredients/mapped/Sodium_Iodoacetate.yaml
data/ingredients/mapped/Sodium_Isethionate.yaml
data/ingredients/mapped/Sodium_L-glutamate.yaml` passed for the 5-file batch
with 0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed.

**Evidence**: The exact CHEBI identity, CAS RN, formula, InChI, and SMILES
pass. Final SSSOM row 2650 exports only `CAS:305-53-3` in `other`, matching
the local CAS RN and ChEBI xref. The per-record YAML agrees with the
regenerated aggregate row when keyed by identifier and preferred term.

**Completeness**: The record has no roles or local synonyms needing evidence
review, and no unsafe synonyms are exported to final SSSOM.

**Recommended Edits**: None.
