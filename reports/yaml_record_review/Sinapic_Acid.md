# `data/ingredients/mapped/Sinapic_Acid.yaml`

**Verdict**: pass.

**Identity**: `sinapic acid` maps exactly to active, defining `CHEBI:77131` /
`sinapic acid`. Fresh OLS4 lookup resolved the ChEBI term, its exact synonym
list contains the synonym stored in the YAML, and PubChem resolves CAS RN
`530-59-6` to CID 10743 with a formula and InChI matching the record.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Simvastatin.yaml
data/ingredients/mapped/Simvastatin_Hydroxy_Acid_Ammonium_Salt.yaml
data/ingredients/mapped/Sinapic_Acid.yaml
data/ingredients/mapped/Sinapinaldehyde.yaml
data/ingredients/mapped/Sinomenine.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the same 5 files.

**Evidence**: The CultureBotHT CAS source, exact CHEBI identity, structure
fields, CAS field, and reviewed exact synonym pass. The per-record YAML agrees
with the regenerated aggregate row when keyed by `(identifier, preferred_term)`.
Final SSSOM row 2589 maps exactly to `CHEBI:77131` and exports the reviewed
exact synonym plus `CAS:530-59-6` in `other`.

**Completeness**: The exact CHEBI identity, CAS field, structure fields, exact
synonym, single-ingredient classification, and final SSSOM row agree. No roles
or components are asserted.

**Recommended Edits**: None.
