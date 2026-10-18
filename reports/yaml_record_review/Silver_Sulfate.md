# `data/ingredients/mapped/Silver_Sulfate.yaml`

**Verdict**: pass.

**Identity**: `silver sulfate` maps to local fallback registry identifier
`cas:10294-26-5`. Fresh PubChem lookup resolves CAS RN `10294-26-5` to CID
159865, and PubChem's formula, InChI, and SMILES agree with the record. Fresh
OLS4 searches by the CAS RN and label found no exact ChEBI term; the row-review
`UNKNOWN_TERM` result is therefore expected CAS registry coverage, not a
missing ChEBI repair.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sialyllacto-N-tetraose_D.yaml
data/ingredients/mapped/Siderophore.yaml
data/ingredients/mapped/Silibinin.yaml
data/ingredients/mapped/Silver_Chloride.yaml
data/ingredients/mapped/Silver_Sulfate.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the 3 CHEBI files; `Sialyllacto-N-tetraose_D` and `Silver_Sulfate`
were skipped because `cas` is outside the Engine A OBO term-validation subset.

**Evidence**: The CultureBotHT CAS source, CAS fallback identity, PubChem
structure fields, expected row-review `UNKNOWN_TERM` classification, and final
SSSOM row pass. The per-record YAML agrees with the regenerated aggregate row
when keyed by `(identifier, preferred_term)`. Final SSSOM row 2584 maps exactly
to `cas:10294-26-5` and exports only `CAS:10294-26-5` in `other`.

**Completeness**: The CAS fallback identity, PubChem structure fields,
single-ingredient classification, and final SSSOM row agree. No roles or
components are asserted.

**Recommended Edits**: None.
