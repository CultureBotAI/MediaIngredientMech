# `data/ingredients/mapped/Procaine_Hydrochloride.yaml`

**Verdict**: pass.

**Identity**: `Procaine hydrochloride` is mapped exactly to active `CHEBI:8431` / `Procaine hydrochloride`. OLS4 CHEBI confirms the CAS `51-05-8` xref and the formula, SMILES, and InChI stored on the record.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Procaine_Hydrochloride.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Procaine_Hydrochloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The CultureBotHT CAS source, CHEBI exact mapping, active chemical properties, and final SSSOM row 2422 all describe procaine hydrochloride. The final `CAS:51-05-8` token is allowed because it matches `chemical_properties.cas_rn`.

**Completeness**: The record has no role assertions, active synonyms, or components that would require narrower evidence.

**Recommended Edits**: None.
