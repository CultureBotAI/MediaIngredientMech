# `data/ingredients/mapped/Sinapinaldehyde.yaml`

**Verdict**: pass.

**Identity**: `sinapinaldehyde` maps exactly to active, defining `CHEBI:27949` /
`(E)-sinapaldehyde`. Fresh OLS4 lookup resolved the ChEBI term, its exact
synonym list contains the systematic synonym stored in the YAML, and PubChem
resolves CAS RN `4206-58-0` to CID 5280802 with a formula and InChI matching
the record.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Simvastatin.yaml
data/ingredients/mapped/Simvastatin_Hydroxy_Acid_Ammonium_Salt.yaml
data/ingredients/mapped/Sinapic_Acid.yaml
data/ingredients/mapped/Sinapinaldehyde.yaml
data/ingredients/mapped/Sinomenine.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the same 5 files.

**Evidence**: The CultureBotHT CAS source, exact CAS-to-ChEBI identity,
structure fields, CAS field, and reviewed exact synonym pass. The row-review
`SYNONYM_ENRICH` result is already represented in the preferred term. The
per-record YAML agrees with the regenerated aggregate row when keyed by
`(identifier, preferred_term)`. Final SSSOM row 2590 maps exactly to
`CHEBI:27949` and exports the reviewed exact synonym plus `CAS:4206-58-0` in
`other`.

**Completeness**: The exact CHEBI identity, CAS field, structure fields, exact
synonym, single-ingredient classification, and final SSSOM row agree. No roles
or components are asserted.

**Recommended Edits**: None.
