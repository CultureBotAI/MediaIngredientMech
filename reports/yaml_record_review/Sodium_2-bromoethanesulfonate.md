# `data/ingredients/mapped/Sodium_2-bromoethanesulfonate.yaml`

**Verdict**: pass.

**Identity**: `Sodium 2-bromoethanesulfonate` maps to local fallback registry
identifier `cas:4263-52-9`. Fresh PubChem lookup resolves CAS RN `4263-52-9` to
CID 23666797, and PubChem's formula, InChI, and SMILES agree with the record.
Fresh OLS4 searches by the CAS RN and label found no exact ChEBI term; the
row-review `UNKNOWN_TERM` result is therefore expected CAS registry coverage,
not a missing ChEBI repair.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sncl2_X_2_H2o.yaml
data/ingredients/mapped/Sodium().yaml
data/ingredients/mapped/Sodium_2-bromoethanesulfonate.yaml
data/ingredients/mapped/Sodium_2-mercaptoethanesulfonate.yaml
data/ingredients/mapped/Sodium_4-Hydroxybenzoate.yaml` passed for the 5-file
batch with 0 ERROR rows. Direct `linkml-term-validator validate-data` with
`--labels` passed for the 4 CHEBI files; `Sodium_2-bromoethanesulfonate` was
skipped because `cas` is outside the Engine A OBO term-validation subset.

**Evidence**: The CultureBotHT CAS source, CAS fallback identity, PubChem
structure fields, synonym, expected row-review `UNKNOWN_TERM` classification,
and final SSSOM row pass. The per-record YAML agrees with the regenerated
aggregate row when keyed by `(identifier, preferred_term)`. Final SSSOM row
2610 maps exactly to `cas:4263-52-9` and exports `sodium bromoethanesulfonate`
plus `CAS:4263-52-9` in `other`.

**Completeness**: The CAS fallback identity, PubChem structure fields, synonym,
single-ingredient classification, and final SSSOM row agree. No roles or
components are asserted.

**Recommended Edits**: None.
