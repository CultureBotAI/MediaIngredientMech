# `data/ingredients/mapped/Sncl2_X_2_H2o.yaml`

**Verdict**: pass.

**Identity**: `SnCl2 x 2 H2O` maps exactly to active, defining
`CHEBI:78074` / `tin(II) chloride dihydrate`. Fresh OLS4 lookup resolved the
ChEBI term, and the hydrate grounding report classifies this record as
`OK_HYDRATE_TERM`.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sncl2_X_2_H2o.yaml
data/ingredients/mapped/Sodium().yaml
data/ingredients/mapped/Sodium_2-bromoethanesulfonate.yaml
data/ingredients/mapped/Sodium_2-mercaptoethanesulfonate.yaml
data/ingredients/mapped/Sodium_4-Hydroxybenzoate.yaml` passed for the 5-file
batch with 0 ERROR rows. Direct `linkml-term-validator validate-data` with
`--labels` passed for the 4 CHEBI files; `Sodium_2-bromoethanesulfonate` was
skipped because `cas` is outside the Engine A OBO term-validation subset.

**Evidence**: The CultureMech direct match, exact ChEBI hydrate identity,
structure fields, hydrate-form synonyms, and migrated `TRACE_ELEMENT` role pass.
The per-record YAML agrees with the regenerated aggregate row when keyed by
`(identifier, preferred_term)`. Final SSSOM row 2608 maps exactly to
`CHEBI:78074`, exports only hydrate labels for the same ChEBI term, and filters
the raw CultureMech role/property token.

**Completeness**: The exact hydrate identity, structure fields, trace-element
role, occurrence counts, and final SSSOM row agree. No CAS field or components
are asserted.

**Recommended Edits**: None.
