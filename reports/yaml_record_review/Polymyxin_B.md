# `data/ingredients/mapped/Polymyxin_B.yaml`

**Verdict**: pass.

**Identity**: `Polymyxin B` maps exactly to `NCIT:C61894` / `Polymyxin B`. The record deliberately uses NCIT rather than the newer live CHEBI term: the 2026-08-07 curator ruling says the NCIT grounding is final unless a new curator decision supersedes it.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Polymyxin_B.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Polymyxin_B.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The promotion history records the move from the unresolved local CHEBI accession to `NCIT:C61894`, and the explicit curator ruling documents why this is not a temporary stopgap. Final SSSOM row 2369 publishes the exact NCIT mapping with no `other` tokens. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the original demotion, the NCIT promotion, the ruling script references, and the final SSSOM row.

**Completeness**: No active synonyms, roles, components, or chemical properties require additional support for this zero-media MicrobeDecoder trait import.

**Recommended Edits**: None.
