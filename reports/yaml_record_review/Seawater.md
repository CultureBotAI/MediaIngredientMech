# `data/ingredients/mapped/Seawater.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Seawater` maps exactly to active, defining `ENVO:00002149` /
`sea water`. Fresh OLS4 lookup resolved the ENVO term and still lists
`seawater` as an exact synonym.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sea_Water.yaml data/ingredients/mapped/Seawater.yaml
data/ingredients/mapped/Sebacic_Acid.yaml data/ingredients/mapped/Selenate.yaml
data/ingredients/mapped/Selenite.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with `--labels`
passed for the same 5 files.

**Evidence**: The ENVO exact identity and environmental context pass. The
per-record YAML agrees with the regenerated aggregate row when keyed by
`(identifier, preferred_term)`. Final SSSOM row 2566 maps exactly to
`ENVO:00002149`, but it exports `Seawater (30 ppt)|Seawater(non-sterilized)`
in `other`.

Those two raw CultureMech labels are not plain synonyms of seawater. One is
salinity-qualified, and the other is process-qualified. They should not reach
the final SSSOM `other` column for the generic ENVO identity.

**Completeness**: The active `Sea water` duplicate has been merged into this
record and tombstoned. The occurrence count and natural-source environmental
context are populated. The only curation gap is the noisy SSSOM synonym export.

**Recommended Edits**: Remove or non-publish the two qualified seawater raw
aliases, then regenerate `ingredient_mappings.sssom.tsv` so row 2566 keeps an
empty `other` field.
