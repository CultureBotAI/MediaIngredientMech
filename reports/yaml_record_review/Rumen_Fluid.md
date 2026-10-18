# `data/ingredients/mapped/Rumen_Fluid.yaml`

**Verdict**: pass.

**Identity**: `Rumen fluid` maps exactly to active, defining `UBERON:0010228` /
`ruminal fluid`. Fresh OLS4 lookup resolved the UBERON term with the same
canonical label, and the manual `#114`/`#204` curation note correctly reserves
the processed MICRO clarified-rumen-fluid class for labels that explicitly say
clarified.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Roxithromycin.yaml
data/ingredients/mapped/Rubidium_Chloride.yaml
data/ingredients/mapped/Rubradirin.yaml
data/ingredients/mapped/Rubrolone.yaml
data/ingredients/mapped/Rumen_Fluid.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels` passed
for the same 5 files.

**Evidence**: The mim-queue source label, unresolved-mixture classification,
manual promotion, and refreshed CultureMech occurrence count all point at the
same generic rumen-fluid material. The per-record YAML agrees with the
regenerated aggregate row when keyed by `(identifier, preferred_term)`. Final
SSSOM row 2538 maps exactly to `UBERON:0010228` and exports an empty `other`
field.

**Completeness**: The exact UBERON identity, 37-occurrence count,
unqualified-versus-clarified distinction, undefined-mixture classification, and
final SSSOM row agree. No roles, components, or chemical properties are
asserted.

**Recommended Edits**: None.
