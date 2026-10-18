# `data/ingredients/mapped/Propionate.yaml`

**Verdict**: pass.

**Identity**: `Propionate` is mapped exactly to active `CHEBI:17272` / `propionate`, the conjugate-base anion of propionic acid. The stored formula, SMILES, InChI, and molecular weight match the anion rather than the acid or a sodium salt.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Propionate.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Propionate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: OLS4 CHEBI lists `propanoate` as an exact synonym of `CHEBI:17272`, so the CultureMech `Propanoate` surface belongs on this record. Final SSSOM row 2428 publishes only that anion synonym and does not leak `Propionic acid` or sodium-propionate aliases into `other`.

**Completeness**: The record has the expected MicrobeDecoder source occurrence, no CAS value, and no active roles or components.

**Recommended Edits**: None.
