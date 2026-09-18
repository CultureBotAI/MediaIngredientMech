# `data/ingredients/mapped/Plumbagin.yaml`

**Verdict**: pass.

**Identity**: `Plumbagin` maps exactly to `CHEBI:8273` / `plumbagin`. The CHEBI identifier, canonical label, CultureBotHT CAS number `481-42-5`, `C11H8O3` structure fields, exact CHEBI synonym, and final SSSOM row 2350 agree.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Plumbagin.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Plumbagin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The CultureBotHT import supports the original CAS-bearing record, and the CHEBI mapping supports `CHEBI:8273` as the exact plumbagin term. The final SSSOM row exports `5-hydroxy-2-methylnaphthalene-1,4-dione` and `CAS:481-42-5` in `other`; both are true identifiers for the same subject form and the CAS token matches `chemical_properties.cas_rn`. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected curated, generated, row-review, and final SSSOM references.

**Completeness**: The record contains the exact ontology ID, molecular formula, InChI, SMILES, CAS number, and reviewed synonym. No component block is expected for this single defined compound, and no unsupported roles are asserted.

**Recommended Edits**: None.
