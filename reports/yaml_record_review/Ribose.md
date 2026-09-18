# `data/ingredients/mapped/Ribose.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Ribose` maps exactly to active, defining `CHEBI:33942` /
`ribose`. Fresh OLS4 lookup resolved the ChEBI term, matched the generic
`C5H10O5` formula stored in YAML, and listed both exported synonyms, `Rib` and
`ribo-pentose`, on the term.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Ribose.yaml data/ingredients/mapped/Rice_straw.yaml
data/ingredients/mapped/Rifabutin.yaml data/ingredients/mapped/Rifampicin.yaml
data/ingredients/mapped/Rifamycin.yaml` passed for the 5-file batch with 0 ERROR
rows. Direct `linkml-term-validator validate-data` with `--labels` passed for
the same 5 files.

**Evidence**: The per-record YAML agrees with the regenerated aggregate row
when keyed by `(identifier, preferred_term)`. Final SSSOM row 2511 maps exactly
to `CHEBI:33942` and exports only the two ChEBI-backed exact synonyms.

The `nutritional_roles.CARBON_SOURCE` and
`nutritional_roles.ENERGY_SOURCE` assertions are unsupported. Both are
`COMPUTATIONAL_PREDICTION` entries from ChEBI-ancestry and canonical-substrate
rules with the standard provisional curator notes.

**Completeness**: The exact ChEBI identity, occurrence statistics, ingredient
type, formula, and final SSSOM row agree. The only active gap is the two
provisional nutritional roles.

**Recommended Edits**: Either remove `nutritional_roles.CARBON_SOURCE` and
`nutritional_roles.ENERGY_SOURCE` or replace their computational predictions
with source-backed evidence for ribose as a carbon and energy source in the
relevant media context.
