# `data/ingredients/mapped/Pyridoxine_dihydrochloride.yaml`

**Verdict**: needs curation, minor issue.

**Identity**: `Pyridoxine dihydrochloride` is mapped exactly to active `CHEBI:189426` / `Pyridoxine dihydrochloride`. OLS4 CHEBI resolves the same two-HCl salt term and keeps it distinct from `CHEBI:30961` / `pyridoxine hydrochloride`.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Pyridoxine_dihydrochloride.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Pyridoxine_dihydrochloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The #260 manual curation note intentionally split this two-HCl CultureMech gap label away from the heavily used monohydrochloride record, and final SSSOM row 2462 emits only the exact `CHEBI:189426` row with no unsupported `other` tokens.

**Completeness**: The record has no stale roles, components, or synonyms. As a minor completeness gap, it has no `chemical_properties` block even though PubChem lookup by exact name resolves the two-HCl formula, SMILES, and InChI.

**Recommended Edits**: Backfill `chemical_properties` for `data/ingredients/mapped/Pyridoxine_dihydrochloride.yaml` from `CHEBI:189426` or an inspected PubChem lookup for pyridoxine dihydrochloride, preserving the two-HCl formula and InChI.
