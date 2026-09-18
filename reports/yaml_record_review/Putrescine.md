# `data/ingredients/mapped/Putrescine.yaml`

**Verdict**: pass.

**Identity**: `Putrescine` is mapped exactly to active `CHEBI:17148` / `putrescine`. OLS4 CHEBI resolves the same term, and PubChem lookup by CAS `110-60-1` confirms the stored formula and InChI for the free base.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Putrescine.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Putrescine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: CultureMech, the PubChem CAS lookup, and the OAK/OLS row review all support the same CHEBI identity. Final SSSOM row 2447 exports only real kg-microbe putrescine synonyms plus `CAS:110-60-1`; the rejected N-substituted-putrescine enrichment candidate is not in `other`, and the raw CultureMech `Role:` / `Properties:` imports are filtered out.

**Completeness**: The `NITROGEN_SOURCE` role is backed by `DATABASE_ENTRY` evidence imported from CultureMech with the original `Nitrogen Source` role text.

**Recommended Edits**: None.
