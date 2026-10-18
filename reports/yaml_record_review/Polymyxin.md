# `data/ingredients/mapped/Polymyxin.yaml`

**Verdict**: pass.

**Identity**: `Polymyxin` maps exactly to `CHEBI:59062` / `polymyxin` from the MicrobeDecoder import. The CHEBI ID, canonical label, exact mapping, MicrobeDecoder source occurrence, and final SSSOM row 2368 agree.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Polymyxin.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Polymyxin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The MicrobeDecoder import used an exact CHEBI label hit, and the local `review-ingredients` pass re-confirmed that the ID resolves and the canonical label matches case-insensitively. Final SSSOM row 2368 has no `other` synonyms to triage. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected curated, generated, MicrobeDecoder review, and final SSSOM references.

**Completeness**: No active synonyms, roles, components, or chemical properties require additional support for this zero-media MicrobeDecoder trait import.

**Recommended Edits**: None.
