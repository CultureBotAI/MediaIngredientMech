# `data/ingredients/mapped/Showdomycin.yaml`

**Verdict**: pass.

**Identity**: `Showdomycin` maps exactly to active, defining `CHEBI:226519` /
`Showdomycin`. Fresh OLS4 lookup resolved the ChEBI term by exact CURIE and
exact label, and its formula, InChI, and SMILES agree with the record.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sheep_blood.yaml
data/ingredients/mapped/Shikimic_Acid.yaml
data/ingredients/mapped/Showdomycin.yaml
data/ingredients/mapped/Sialyllacto-N-tetraose_A.yaml
data/ingredients/mapped/Sialyllacto-N-tetraose_C.yaml` passed for the 5-file
batch with 0 ERROR rows. Direct `linkml-term-validator validate-data` with
`--labels` passed for the 4 CHEBI files; `Sheep_blood` was skipped because
`MICRO` is outside the Engine A CHEBI/OBO term-validation subset.

**Evidence**: The MicrobeDecoder exact-label import, exact CHEBI identity, and
structure fields pass. The per-record YAML agrees with the regenerated
aggregate row when keyed by `(identifier, preferred_term)`. Final SSSOM row
2577 maps exactly to `CHEBI:226519` and exports an empty `other` field.

**Completeness**: The exact CHEBI identity, single-ingredient classification,
structure fields, occurrence source, and final SSSOM row agree. No roles,
components, or CAS field are asserted.

**Recommended Edits**: None.
