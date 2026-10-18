# `data/ingredients/mapped/Porfiromycin.yaml`

**Verdict**: pass.

**Identity**: `Porfiromycin` maps exactly to `CHEBI:208611` / `Porfiromycin` from the MicrobeDecoder import. The CHEBI ID, canonical label, structural properties, `SINGLE_INGREDIENT` classification, and final SSSOM row 2375 agree.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Porfiromycin.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Porfiromycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The MicrobeDecoder import used an exact CHEBI label hit, and the local review-ingredients pass promoted the record after checking the CHEBI ID and canonical label. The stored formula, SMILES, InChI, and molecular weight came from the ChEBI/PubChem enrichment pass for this CHEBI subject. Final SSSOM row 2375 has no `other` synonyms to triage. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected curated, generated, MicrobeDecoder review, and final SSSOM references.

**Completeness**: No active roles, components, or extra synonyms are asserted.

**Recommended Edits**: None.
