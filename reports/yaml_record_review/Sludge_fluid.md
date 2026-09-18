# `data/ingredients/mapped/Sludge_fluid.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Sludge fluid` maps exactly to active, defining `MICRO:0000521` /
`sludge fluid`. Fresh OLS4 lookup resolved the MICRO term by exact CURIE and
exact label, matching the restored CultureMech occurrence-table grounding.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Sludge.yaml
data/ingredients/mapped/Sludge_fluid.yaml
data/ingredients/mapped/Sn-Glycerol_3-phosphate_Lithium_Salt.yaml
data/ingredients/mapped/Sn-glycero-3-phosphocholine.yaml
data/ingredients/mapped/Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt.yaml`
passed for the 5-file batch with 0 ERROR rows. Direct
`linkml-term-validator validate-data` with `--labels` passed for the ENVO and
3 CHEBI files; `Sludge_fluid` was skipped because `MICRO` is outside the Engine
A OBO term-validation subset.

**Evidence**: The exact MICRO identity, occurrence count, and structured
CultureMech evidence pass. The per-record YAML agrees with the regenerated
aggregate row when keyed by `(identifier, preferred_term)`.

The final SSSOM row needs synonym cleanup. Row 2600 exports `Sludge fluid (see
below)` as `other`; that is a conditional recipe instruction fragment, not an
exact synonym of the MICRO sludge-fluid term.

**Completeness**: The exact MICRO identity and occurrence counts agree. The
conditional CultureMech surface form needs to be filtered from final SSSOM or
removed from the exported synonym set.

**Recommended Edits**: Remove `Sludge fluid (see below)` from
`data/ingredients/mapped/Sludge_fluid.yaml` or update the SSSOM synonym policy
to exclude conditional raw-text labels, then rebuild final SSSOM and confirm row
2600 has an empty `other` field.
