# `data/ingredients/mapped/R2A_agar.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `R2A agar` is exactly grounded to defining `MICRO:0000543` / `R2A
agar`. Fresh OLS4 lookups by CURIE and by exact label both resolved the same
well-formed MICRO term, and the record correctly avoids the neighboring
`MICRO:0000541` broth term.

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
`data/curated/mapped_ingredients.yaml` row, and final SSSOM row 2481 maps
`MIM:R2A_agar` to `MICRO:0000543` with `skos:exactMatch`. The unsafe part is
the published `other` payload: `R2A agar (BD-Difco)`, `R2A agar (DB-Difco)`,
and `R2A agar (BD--Difco)` are vendor/catalog-qualified occurrence strings, not
genuine alternate names for the generic MICRO R2A agar class.

**Completeness**: The exact MICRO identity, source occurrence count, and #260
manual mapping note are present. Minor: `ingredient_type: UNDEFINED_MIXTURE`
conflicts with both the record's own curation note and `docs/ingredient_type.md`;
`R2A agar` is a whole named medium and should be classified as `NAMED_MEDIUM`.

**Recommended Edits**: Remove the three vendor-qualified CultureMech surface
forms from exported synonyms, or preserve them as provenance-only raw
occurrence labels so final SSSOM no longer emits them in `other`. Reclassify the
record as `NAMED_MEDIUM`, sync `data/curated/mapped_ingredients.yaml`, rebuild
the SSSOM, and rerun the SSSOM synonym/invariant checks.
