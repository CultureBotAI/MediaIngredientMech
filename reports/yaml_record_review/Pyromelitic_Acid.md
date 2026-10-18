# `data/ingredients/mapped/Pyromelitic_Acid.yaml`

**Verdict**: pass.

**Identity**: `Pyromelitic acid` was intentionally promoted to active `CHEBI:45165` / `pyromellitic acid` after local OAK exact-label verification resolved the one-letter source misspelling. OLS4 CHEBI confirms `CHEBI:45165`, and PubChem lookup by the canonical pyromellitic acid name confirms the stored formula and InChI.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pyromelitic_Acid.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Pyromelitic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The `promote_resolved_unmapped` history records the exact promotion from unresolved `UNMAPPED_0504` to `CHEBI:45165`. Final SSSOM row 2467 emits a single exact CHEBI row with no `other` tokens, so the misspelled raw source spelling is not exported as a synonym.

**Completeness**: The record has no role assertions, components, CAS number, or unsupported final synonyms.

**Recommended Edits**: None.
