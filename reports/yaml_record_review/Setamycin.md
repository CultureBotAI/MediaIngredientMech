# `data/ingredients/mapped/Setamycin.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Setamycin` maps exactly to active, defining `mesh:C032953` /
`setamycin`. Fresh OLS4 lookup resolved the MeSH term by exact CURIE and exact
label, matching the MESH via OLS upgrade from the local
`kgmicrobe.compound:setamycin` placeholder.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Serine.yaml
data/ingredients/mapped/Serine_Hydroxamate.yaml
data/ingredients/mapped/Serotonin.yaml data/ingredients/mapped/Serum.yaml
data/ingredients/mapped/Setamycin.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the same 5 files.

**Evidence**: The MeSH exact-label identity and final SSSOM row pass. The
row-review UNKNOWN_TERM finding is missing-prefix coverage only: a
prefix-specific OLS4 query resolves `mesh:C032953` exactly. The per-record YAML
agrees with the regenerated aggregate row when keyed by `(identifier,
preferred_term)`. Final SSSOM row 2574 maps exactly to `mesh:C032953` and
exports an empty `other` field.

The remaining issue is the `SELECTIVE_AGENT` role. It was inferred from a name
pattern, its only evidence is `COMPUTATIONAL_PREDICTION`, and its curator note
explicitly says the assertion is provisional and needs review. That is not
enough source support for a physicochemical role.

**Completeness**: The exact MeSH identity and final SSSOM row agree. The record
has no components, CAS, or chemical structure fields. The role facet needs
source-backed curation or removal.

**Recommended Edits**: Replace the provisional `SELECTIVE_AGENT` role with
source-backed evidence, or remove it if no MediaIngredientMech source supports
using setamycin as a selective agent.
