# `data/ingredients/mapped/Sodium_4-Hydroxybenzoate.yaml`

**Verdict**: pass.

**Identity**: `Sodium 4-Hydroxybenzoate` maps exactly to active, defining
`CHEBI:113449` / `sodium 4-hydroxybenzoate`. Fresh OLS4 lookup resolved the
ChEBI term, and PubChem resolves CAS RN `114-63-6` to CID 16219477 with a
formula and InChI matching the record.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sncl2_X_2_H2o.yaml
data/ingredients/mapped/Sodium().yaml
data/ingredients/mapped/Sodium_2-bromoethanesulfonate.yaml
data/ingredients/mapped/Sodium_2-mercaptoethanesulfonate.yaml
data/ingredients/mapped/Sodium_4-Hydroxybenzoate.yaml` passed for the 5-file
batch with 0 ERROR rows. Direct `linkml-term-validator validate-data` with
`--labels` passed for the 4 CHEBI files; `Sodium_2-bromoethanesulfonate` was
skipped because `cas` is outside the Engine A OBO term-validation subset.

**Evidence**: The CultureBotHT CAS source, exact CHEBI identity, CAS field, and
structure fields pass. The per-record YAML agrees with the regenerated
aggregate row when keyed by `(identifier, preferred_term)`. Final SSSOM row
2612 maps exactly to `CHEBI:113449` and exports only `CAS:114-63-6` in `other`.

**Completeness**: The exact CHEBI identity, CAS field, structure fields,
single-ingredient classification, and final SSSOM row agree. No roles,
components, or curated synonyms are asserted.

**Recommended Edits**: None.
