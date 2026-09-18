# `data/ingredients/mapped/Sinomenine.yaml`

**Verdict**: pass.

**Identity**: `Sinomenine` maps exactly to active, defining `CHEBI:9163` /
`Sinomenine`. Fresh OLS4 lookup resolved the ChEBI term by exact CURIE and
exact label, and PubChem resolves CAS RN `115-53-7` to CID 5459308 with a
formula and InChI matching the record.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Simvastatin.yaml
data/ingredients/mapped/Simvastatin_Hydroxy_Acid_Ammonium_Salt.yaml
data/ingredients/mapped/Sinapic_Acid.yaml
data/ingredients/mapped/Sinapinaldehyde.yaml
data/ingredients/mapped/Sinomenine.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the same 5 files.

**Evidence**: The CultureBotHT CAS source, exact CHEBI identity, structure
fields, and CAS field pass. The per-record YAML agrees with the regenerated
aggregate row when keyed by `(identifier, preferred_term)`. Final SSSOM row
2591 maps exactly to `CHEBI:9163` and exports only `CAS:115-53-7` in `other`.

**Completeness**: The exact CHEBI identity, CAS field, structure fields,
single-ingredient classification, and final SSSOM row agree. No roles,
components, or curated synonyms are asserted.

**Recommended Edits**: None.
