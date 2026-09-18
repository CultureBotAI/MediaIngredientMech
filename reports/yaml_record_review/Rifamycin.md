# `data/ingredients/mapped/Rifamycin.yaml`

**Verdict**: pass.

**Identity**: `Rifamycin` maps exactly to active, defining `NCIT:C29406` /
`Rifamycin`. Fresh OLS4 lookup resolved the NCIT CURIE and exact label; the
ChEBI xref on the NCIT term points at the active plural `CHEBI:26580` /
`rifamycins` class, so retaining the singular NCIT exact match is narrower than
replacing it with that ChEBI family term.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Ribose.yaml data/ingredients/mapped/Rice_straw.yaml
data/ingredients/mapped/Rifabutin.yaml data/ingredients/mapped/Rifampicin.yaml
data/ingredients/mapped/Rifamycin.yaml` passed for the 5-file batch with 0 ERROR
rows. Direct `linkml-term-validator validate-data` with `--labels` passed for
the same 5 files.

**Evidence**: The per-record YAML agrees with the regenerated aggregate row
when keyed by `(identifier, preferred_term)`. Final SSSOM row 2515 maps exactly
to `NCIT:C29406`, exports an empty `other` field, and carries the
MicrobeDecoder provenance plus `review-ingredients` approval.

**Completeness**: The reviewed NCIT identity, MicrobeDecoder occurrence
provenance, and final SSSOM row agree. This record asserts no roles, synonyms,
or chemical properties.

**Recommended Edits**: None.
