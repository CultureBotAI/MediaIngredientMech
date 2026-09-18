# `data/ingredients/mapped/Quinoline.yaml`

**Verdict**: pass.

**Identity**: `Quinoline` is an exact `CHEBI:17362` / `quinoline` record created
from a one-mention CultureMech residual label. Fresh OLS4 lookup resolved
`CHEBI:17362` as a defining ChEBI term labeled `quinoline`, and PubChem lookup by
the record label resolved CID 7047 with formula `C9H7N` and the expected
quinoline connectivity.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Quinoline.yaml
data/ingredients/mapped/R-3-hydroxybutyrate.yaml
data/ingredients/mapped/R2A_agar.yaml
data/ingredients/mapped/Rabbit_Blood.yaml
data/ingredients/mapped/Rabbit_Serum.yaml` passed for the 5-file batch with 0
ERROR rows. Direct `linkml-term-validator validate-data` with
`--labels` passed for this CHEBI record.

**Evidence**: The per-record YAML agrees with the aggregate
`data/curated/mapped_ingredients.yaml` row. The structured
`ontology_mapping.evidence` points at
`culturemech:output/ingredient_occurrences.tsv`, matching the creation-history
provenance restored for #541. Final SSSOM row 2479 maps `MIM:Quinoline` to
`CHEBI:17362` with `skos:exactMatch`, canonical object label `quinoline`, and an
empty `other` field.

**Completeness**: No roles, synonyms, components, supplied forms, or
chemical-properties fields are asserted, so there is no unsupported secondary
payload. A hidden/ignored-inclusive search across `mappings`, `data`, `reports`,
`docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the active YAML, aggregate
copy, final SSSOM row, and CultureMech residual provenance for this one active
record.

**Recommended Edits**: None.
