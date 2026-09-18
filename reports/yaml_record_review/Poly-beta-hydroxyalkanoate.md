# `data/ingredients/mapped/Poly-beta-hydroxyalkanoate.yaml`

**Verdict**: pass.

**Identity**: `Poly-beta-hydroxyalkanoate` is grounded to `CHEBI:78037` / `polyhydroxyalkanoate` as the same PHA polymer class under two spellings. The `SYNONYM_MATCH` mapping, `PHA` surface form, and final SSSOM row 2356 agree.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Poly-beta-hydroxyalkanoate.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Poly-beta-hydroxyalkanoate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The #213/#308 manual curation decision explicitly records the class-granularity choice: `Poly-beta-hydroxyalkanoate` and `polyhydroxyalkanoate` are treated as the same PHA class, and no local registry mint is needed. Final SSSOM row 2356 exports only `PHA` in `other`, which is a real abbreviation for the class. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected curated, generated, and final SSSOM references.

**Completeness**: The record has no roles, components, or chemistry fields that need source support beyond the class mapping. The MicrobeDecoder provenance and mapped-collection move are recorded in curation history.

**Recommended Edits**: None.
