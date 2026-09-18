# `data/ingredients/mapped/Rice_straw.yaml`

**Verdict**: pass.

**Identity**: `rice straw` maps exactly to active, defining `ENVO:00003870` /
`rice straw`. Fresh OLS4 lookup resolved the ENVO CURIE with the same canonical
label.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Ribose.yaml data/ingredients/mapped/Rice_straw.yaml
data/ingredients/mapped/Rifabutin.yaml data/ingredients/mapped/Rifampicin.yaml
data/ingredients/mapped/Rifamycin.yaml` passed for the 5-file batch with 0 ERROR
rows. Direct `linkml-term-validator validate-data` with `--labels` passed for
the same 5 files.

**Evidence**: The per-record YAML agrees with the regenerated aggregate row
when keyed by `(identifier, preferred_term)`. Final SSSOM row 2512 maps exactly
to `ENVO:00003870`, exports an empty `other` field, and carries the restored
`culturemech:output/ingredient_occurrences.tsv` evidence that was added back in
#541.

**Completeness**: The CultureMech residual grounding, one-recipe occurrence
count, exact ENVO target, and final SSSOM row agree. No roles, synonyms, or
chemical properties are asserted.

**Recommended Edits**: None.
