# `data/ingredients/mapped/Potassium_Fluoride.yaml`

**Verdict**: pass.

**Identity**: `potassium fluoride` maps exactly to `CHEBI:66872` / `potassium fluoride`. The CHEBI ID, canonical label, CAS RN `7789-23-3`, formula, structure strings, merged `KF` / `K-F` synonyms, and final SSSOM row 2395 agree.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Potassium_Fluoride.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Potassium_Fluoride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The CultureBotHT CAS-bearing import supports the CHEBI identity, and the #346 merge explains why `KF` and `K-F` are retained on this record rather than on the false Lys-Phe dipeptide record. The final SSSOM `other` values are true formula synonyms plus `CAS:7789-23-3`, which matches `chemical_properties.cas_rn`. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected curated, generated, cross-record baseline, row-review, and final SSSOM references.

**Completeness**: The record has the exact CHEBI term, CAS number, formula, InChI, SMILES, and same-substance formula synonyms. No active roles or components need further support.

**Recommended Edits**: None.
