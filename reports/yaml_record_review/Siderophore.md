# `data/ingredients/mapped/Siderophore.yaml`

**Verdict**: needs curation, major issues.

**Identity**: `Siderophore` maps exactly to active, defining `CHEBI:26672` /
`siderophore`. Fresh OLS4 lookup resolved the ChEBI term by exact CURIE and
exact label, matching the kgm-metatraits source-preset import.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sialyllacto-N-tetraose_D.yaml
data/ingredients/mapped/Siderophore.yaml
data/ingredients/mapped/Silibinin.yaml
data/ingredients/mapped/Silver_Chloride.yaml
data/ingredients/mapped/Silver_Sulfate.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the 3 CHEBI files; `Sialyllacto-N-tetraose_D` and `Silver_Sulfate`
were skipped because `cas` is outside the Engine A OBO term-validation subset.

**Evidence**: The kgm-metatraits import and exact CHEBI identity pass. The
per-record YAML agrees with the regenerated aggregate row when keyed by
`(identifier, preferred_term)`.

Two exported or asserted claims need curation. Final SSSOM row 2581 exports
`produces: siderophore` as `other`; that token is a process-qualified trait
surface form, not an exact synonym of the ChEBI chemical class. The `CHELATOR`
role is also only a `COMPUTATIONAL_PREDICTION` from ChEBI ancestry, and its
curator note explicitly says the assertion is provisional and needs review.

**Completeness**: The exact CHEBI identity and row-review confirmation agree.
The raw process-qualified surface form needs removal from final SSSOM, and the
chelator role needs source-backed curation or removal.

**Recommended Edits**: Remove `produces: siderophore` from
`data/ingredients/mapped/Siderophore.yaml` or change the SSSOM synonym policy so
process-qualified raw tokens are not exported as `other`, then rebuild final
SSSOM and confirm row 2581 no longer carries it. Replace the provisional
`CHELATOR` role with source-backed evidence, or remove it if no
MediaIngredientMech source supports using siderophores as chelators.
