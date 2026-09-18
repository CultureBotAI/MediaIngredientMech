# `data/ingredients/mapped/Potassium.yaml`

**Verdict**: pass.

**Identity**: `Potassium` maps exactly to `NCIT:C765` / `Potassium` from the MicrobeDecoder import. The NCIT ID, canonical label, exact mapping, refreshed occurrence count, and final SSSOM row 2378 agree.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Potassium.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Potassium.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The MicrobeDecoder import used an exact NCIT label hit, and the local `review-ingredients` pass re-confirmed that the ID resolves and the canonical label matches case-insensitively. Final SSSOM row 2378 has no `other` synonyms to triage. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected curated, generated, MicrobeDecoder review, and final SSSOM references.

**Completeness**: No roles, components, or chemistry fields are asserted for this element record.

**Recommended Edits**: None.
