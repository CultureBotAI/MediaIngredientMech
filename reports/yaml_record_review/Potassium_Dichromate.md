# `data/ingredients/mapped/Potassium_Dichromate.yaml`

**Verdict**: pass.

**Identity**: `Potassium dichromate` maps exactly to `CHEBI:53444` / `potassium dichromate`. The CHEBI ID, canonical label, CAS RN `7778-50-9`, formula, structure fields, reviewed CHEBI synonyms, and final SSSOM row 2394 agree.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Potassium_Dichromate.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Potassium_Dichromate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The CultureBotHT CAS-bearing import and ChEBI structure backfill both support the exact potassium dichromate identity. The final SSSOM row exports only true synonyms plus `CAS:7778-50-9`, which matches `chemical_properties.cas_rn`. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected curated, generated, row-review, and final SSSOM references.

**Completeness**: The CAS number, formula, InChI, SMILES, and exact synonyms are present; no roles or components are asserted.

**Recommended Edits**: None.
