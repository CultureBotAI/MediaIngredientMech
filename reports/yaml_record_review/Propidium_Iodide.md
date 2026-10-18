# `data/ingredients/mapped/Propidium_Iodide.yaml`

**Verdict**: pass.

**Identity**: `Propidium iodide` is mapped exactly to active `CHEBI:51240` / `propidium iodide`. OLS4 CHEBI confirms CAS `25535-16-4`, formula `C27H34N4.2I`, and the stored SMILES and InChI.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Propidium_Iodide.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Propidium_Iodide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The curated long synonym `3,8-diamino-5-{3-[diethyl(methyl)ammonio]propyl}-6-phenylphenanthridinium diiodide` is an exact synonym on the CHEBI term, and final SSSOM row 2426 keeps it with the matching CAS token.

**Completeness**: The record has no unsupported roles, components, or extra synonyms.

**Recommended Edits**: None.
