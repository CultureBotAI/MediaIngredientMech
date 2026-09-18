# `data/ingredients/mapped/Poly(ethylene_Terephthalate).yaml`

**Verdict**: pass.

**Identity**: `Poly(ethylene Terephthalate)` maps by synonym to `CHEBI:53259` / `poly(ethylene terephthalate) macromolecule`. The MicrobeDecoder source label, CHEBI target, `SYNONYM_MATCH` quality, polymer formula fields, and final SSSOM row 2355 agree.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Poly(ethylene_Terephthalate).yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Poly(ethylene_Terephthalate).yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The recovered MicrobeDecoder curation records `Poly(ethylene terephthalate)` as a synonym of `CHEBI:53259`, and the CHEBI label check confirms the stored canonical label. Final SSSOM row 2355 has no `other` tokens, so no raw source or broader-parent payload leaks into the synonym surface. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected curated and generated references for this file.

**Completeness**: The record has the exact polymer target, formula and SMILES from ChEBI, one MicrobeDecoder source occurrence, and no unsupported roles or synonyms.

**Recommended Edits**: None.
