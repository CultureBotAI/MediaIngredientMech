# `data/ingredients/mapped/Pterostilbene.yaml`

**Verdict**: pass.

**Identity**: `Pterostilbene` is mapped exactly to active `CHEBI:8630` / `pterostilbene`. The stored CAS `537-42-8`, formula, SMILES, and InChI agree with OLS4 CHEBI.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pterostilbene.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Pterostilbene.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: `4-[(E)-2-(3,5-dimethoxyphenyl)ethenyl]phenol` is an exact CHEBI synonym for the same compound, and final SSSOM row 2439 pairs it with the matching `CAS:537-42-8` token.

**Completeness**: The record has no role assertions, components, or unsupported final synonyms.

**Recommended Edits**: None.
