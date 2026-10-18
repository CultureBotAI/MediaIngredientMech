# `data/ingredients/mapped/Sodium_2-mercaptoethanesulfonate.yaml`

**Verdict**: pass.

**Identity**: `Sodium 2-mercaptoethanesulfonate` maps exactly to active,
defining `CHEBI:31824` / `Mesna`. Fresh OLS4 lookup resolved the ChEBI term,
and PubChem resolves CAS RN `19767-45-4` to CID 23662354 with a formula and
InChI matching the record.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sncl2_X_2_H2o.yaml
data/ingredients/mapped/Sodium().yaml
data/ingredients/mapped/Sodium_2-bromoethanesulfonate.yaml
data/ingredients/mapped/Sodium_2-mercaptoethanesulfonate.yaml
data/ingredients/mapped/Sodium_4-Hydroxybenzoate.yaml` passed for the 5-file
batch with 0 ERROR rows. Direct `linkml-term-validator validate-data` with
`--labels` passed for the 4 CHEBI files; `Sodium_2-bromoethanesulfonate` was
skipped because `cas` is outside the Engine A OBO term-validation subset.

**Evidence**: The CultureBotHT CAS source, exact CAS-to-ChEBI identity, CAS
field, structure fields, and row-review `SYNONYM_ENRICH` classification pass.
The per-record YAML agrees with the regenerated aggregate row when keyed by
`(identifier, preferred_term)`. Final SSSOM row 2611 maps exactly to
`CHEBI:31824` and exports only `CAS:19767-45-4` in `other`.

**Completeness**: The exact CHEBI identity, CAS field, structure fields,
single-ingredient classification, and final SSSOM row agree. No roles,
components, or curated synonyms are asserted.

**Recommended Edits**: None.
