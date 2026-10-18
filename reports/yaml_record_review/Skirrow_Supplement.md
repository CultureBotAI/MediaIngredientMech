# `data/ingredients/mapped/Skirrow_Supplement.yaml`

**Verdict**: pass.

**Identity**: `Skirrow supplement` maps exactly to local fallback registry
identifier `kgmicrobe.ingredient:skirrow_supplement`. The record's own issue
#288 curation history records why a named multi-component preparation should
use the stock-solution convention rather than narrow to one compound, and a
fresh all-ontology OLS4 exact-label search found no public ontology term that
supersedes the local registry identifier.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sio2.yaml
data/ingredients/mapped/Sisomicin_Sulfate_Salt.yaml
data/ingredients/mapped/Skim_milk_powder.yaml
data/ingredients/mapped/Skimmed_Milk.yaml
data/ingredients/mapped/Skirrow_Supplement.yaml` passed for the 5-file batch
with 0 ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for `Sio2`, `Sisomicin_Sulfate_Salt`, and `Skimmed_Milk`; the MICRO and
kgmicrobe.ingredient records were skipped because those prefixes are outside the
Engine A OBO term-validation subset.

**Evidence**: The local fallback identity, stock-solution classification,
occurrence count refresh, exact kg-microbe registry row, and empty final SSSOM
`other` field pass. The per-record YAML agrees with the regenerated aggregate
row when keyed by `(identifier, preferred_term)`. Final SSSOM row 2598 maps
exactly to `kgmicrobe.ingredient:skirrow_supplement`.

**Completeness**: The local registry identity and stock-solution classification
agree. The synonym duplicates the preferred term but is filtered out of final
SSSOM, and no public ontology replacement was found.

**Recommended Edits**: None.
