# `data/ingredients/mapped/Rabbit_Blood.yaml`

**Verdict**: pass.

**Identity**: `Rabbit blood` exactly maps to defining `MICRO:0001229` / `rabbit
blood`. Fresh OLS4 lookup resolved the exact CURIE, and an exact MICRO lookup
for `Defibrinated rabbit blood` returned no row, matching the #260 decision to
fold that CultureMech surface onto the held rabbit-blood record rather than
minting a duplicate on the same MICRO identifier.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Quinoline.yaml
data/ingredients/mapped/R-3-hydroxybutyrate.yaml
data/ingredients/mapped/R2A_agar.yaml
data/ingredients/mapped/Rabbit_Blood.yaml
data/ingredients/mapped/Rabbit_Serum.yaml` passed for the 5-file batch with 0
ERROR rows. Engine A OBO label validation was skipped for this MICRO record:
`scripts/_engine_a_obo_safe.sh` exited non-zero because MICRO is deliberately
outside the sqlite OBO allowlist; OLS4 supplied the prefix-specific label check
instead.

**Evidence**: The per-record YAML agrees with the aggregate
`data/curated/mapped_ingredients.yaml` row. The final SSSOM row maps
`MIM:Rabbit_Blood` to `MICRO:0001229` with `skos:exactMatch`, canonical label
`rabbit blood`, and the curated folded surface `Defibrinated rabbit blood` in
`other`. `mappings/ingredient_mappings_unknown_term_triage.tsv` records the old
`UNKNOWN_TERM` row-review result as a missing-prefix coverage issue rather than
a failed MICRO term.

**Completeness**: `ingredient_type: UNDEFINED_MIXTURE`, the occurrence count,
the CultureMech related synonym, and the structured #260 evidence are
consistent. No roles, components, or chemical structure fields are asserted.

**Recommended Edits**: None.
