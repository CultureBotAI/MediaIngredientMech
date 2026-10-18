# `data/ingredients/mapped/Quinate.yaml`

**Verdict**: needs curation, minor issue.

**Identity**: `Quinate` is mapped exactly to active `CHEBI:26490` / `quinate`, the generic anion class for quinic acid. OLS4 CHEBI resolves the same term and keeps it distinct from the narrower `(-)-quinate` term.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Quinate.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Quinate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The MicrobeDecoder import grounded quinate through an OLS label-exact CHEBI match, then `review-ingredients` promoted the row after local OAK label verification. Final SSSOM row 2476 maps `MIM:Quinate` exactly to `CHEBI:26490` and exports no unsupported synonym tokens.

**Completeness**: The exact identity and final SSSOM row pass. As a minor completeness gap, the record has no `ingredient_type` or `chemical_properties` fields even though it is a CHEBI primary with a structural definition.

**Recommended Edits**: Set `ingredient_type: SINGLE_INGREDIENT` and backfill quinate structure fields from `CHEBI:26490` after inspecting the anion formula and structure.
