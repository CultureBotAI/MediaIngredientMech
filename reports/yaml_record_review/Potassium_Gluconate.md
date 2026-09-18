# `data/ingredients/mapped/Potassium_Gluconate.yaml`

**Verdict**: pass.

**Identity**: `Potassium Gluconate` maps exactly to `CHEBI:32032` / `Potassium gluconate` from the MicrobeDecoder import. The CHEBI ID, canonical label, structure fields, refreshed occurrence count, and final SSSOM row 2396 agree.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Potassium_Gluconate.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Potassium_Gluconate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The MicrobeDecoder import used an exact CHEBI label hit, and the local review-ingredients pass re-confirmed that the ID resolves and the canonical label matches case-insensitively. Final SSSOM row 2396 has no `other` synonyms to triage. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected curated, generated, MicrobeDecoder review, and final SSSOM references.

**Completeness**: The record has the exact CHEBI identity and ChEBI/PubChem formula, InChI, SMILES, and molecular weight. No active roles or components need further support.

**Recommended Edits**: None.
