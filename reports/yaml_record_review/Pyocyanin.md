# `data/ingredients/mapped/Pyocyanin.yaml`

**Verdict**: pass.

**Identity**: `Pyocyanin` is mapped to active `CHEBI:8653` / `pyocyanine` through CAS `85-66-5`. OLS4 CHEBI resolves `CHEBI:8653` and also exposes the protonated `CHEBI:62220` cation, while PubChem lookup by the stored CAS confirms the formula and InChI on this record for the neutral iminium betaine.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pyocyanin.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Pyocyanin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The CultureBotHT CAS lookup, later CAS_RN_LOOKUP regrade, and OAK/OLS row review all support `CHEBI:8653`. Final SSSOM row 2451 maps the subject exactly to `CHEBI:8653` and keeps only `5-methylphenazin-5-ium-1-olate` plus `CAS:85-66-5` in `other`.

**Completeness**: The record has no role assertions, components, or unsupported final synonyms.

**Recommended Edits**: None.
