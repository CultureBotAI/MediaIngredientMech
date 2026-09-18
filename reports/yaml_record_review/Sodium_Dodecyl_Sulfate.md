# `data/ingredients/mapped/Sodium_Dodecyl_Sulfate.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Sodium Dodecyl Sulfate` maps exactly to active, defining
`CHEBI:8984` / `sodium dodecyl sulfate`. Fresh OLS4 lookup confirmed the
ChEBI label, CAS RN `151-21-3`, formula `C12H25O4S.Na`, InChI, InChIKey,
SMILES, and `SDS` synonym, and PubChem resolves the CAS RN to CID `3423265`
with the same formula, InChI, InChIKey, and structure.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sodium_Dodecyl_Sulfate.yaml
data/ingredients/mapped/Sodium_Ethyl_Sulfate.yaml
data/ingredients/mapped/Sodium_Ferric_EDTA.yaml
data/ingredients/mapped/Sodium_Ferulate.yaml
data/ingredients/mapped/Sodium_Fluoroacetate.yaml` passed for the 5-file batch
with 0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed.

**Evidence**: The exact CHEBI identity, CAS RN, formula, structure fields, and
`SDS` synonym pass. Final SSSOM row 2637 exports only `SDS` and
`CAS:151-21-3` in `other`, both valid same-substance tokens. The per-record
YAML agrees with the regenerated aggregate row when keyed by identifier and
preferred term.

The `SURFACTANT` physicochemical role still needs curation. It is a
`COMPUTATIONAL_PREDICTION` from CHEBI ancestry with confidence `0.7` and an
explicit provisional `review recommended` curator note, so the identity review
passes while this role remains unsupported by database or literature evidence.

**Completeness**: The record is otherwise complete for exact sodium dodecyl
sulfate identity. There are no stale broader, hydrate, CAS-decorated, or raw
occurrence synonyms leaking into final SSSOM.

**Recommended Edits**: Either replace the `SURFACTANT` role with a sourced
database or literature claim or remove it, then rebuild final SSSOM and confirm
row 2637 continues to export only `SDS` plus `CAS:151-21-3`.
