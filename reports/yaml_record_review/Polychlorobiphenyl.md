# `data/ingredients/mapped/Polychlorobiphenyl.yaml`

**Verdict**: pass.

**Identity**: `Polychlorobiphenyl` maps exactly to `CHEBI:53156` / `polychlorobiphenyl` from the MicrobeDecoder import. The CHEBI ID, canonical label, `SINGLE_INGREDIENT`-free exact mapping, and final SSSOM row 2362 agree.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Polychlorobiphenyl.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Polychlorobiphenyl.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The MicrobeDecoder import created the row from an exact CHEBI label match, and the local review-ingredients pass promoted the record after confirming the CHEBI ID and label. Final SSSOM row 2362 preserves that exact CHEBI mapping and has no `other` tokens to triage. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected curated, generated, MicrobeDecoder review, and final SSSOM references.

**Completeness**: This is a zero-media MicrobeDecoder trait import with no active synonyms, roles, components, or chemistry fields that need additional source support.

**Recommended Edits**: None.
