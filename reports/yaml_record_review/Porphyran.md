# `data/ingredients/mapped/Porphyran.yaml`

**Verdict**: pass.

**Identity**: `Porphyran` maps exactly to MeSH `mesh:C038549` / `porphyran` after promotion from an unmapped CultureBotHT no-CAS record. The MeSH identifier, normalized label, exact mapping, and final SSSOM row 2376 agree.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Porphyran.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Porphyran.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: A fresh MeSH OLS exact lookup resolved `Porphyran` to `mesh:C038549`, matching the stored ontology ID and label. The row-review manifest classifies the older `UNKNOWN_TERM` stamp as missing-prefix validator coverage, not a mapping defect. Final SSSOM row 2376 uses `registry:mesh` and has no `other` synonyms to triage. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected curated, generated, row-review, and final SSSOM references.

**Completeness**: The exact MeSH identity is present, and no roles, components, or unsupported chemistry fields are asserted.

**Recommended Edits**: None.
