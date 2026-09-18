# `data/ingredients/mapped/Poly_L_Lysine_Polymer.yaml`

**Verdict**: pass.

**Identity**: `Poly L Lysine Polymer` is a rejected duplicate tombstone for the same `CHEBI:61490` identity now represented by `data/ingredients/mapped/Poly_L-lysine_Polymer.yaml`. The old KG-Microbe placeholder was promoted to `CHEBI:61490`, then the record was merged into the active poly(L-lysine) record with `mapping_status: REJECTED`.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Poly_L_Lysine_Polymer.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Poly_L_Lysine_Polymer.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The promotion history cites punctuation-normalized OAK/OLS validation to `CHEBI:61490`, and the later `MERGED_INTO` event records the same-substance merge into `CHEBI:61490` `poly(L-lysine) polymer`. This tombstone is not present in the final SSSOM, so its retained CHEBI synonyms do not create duplicate published rows. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the rejected duplicate, its row-review promotion summary, and the known cross-record baseline entry that points to the active survivor.

**Completeness**: The tombstone keeps enough provenance to explain the placeholder promotion and duplicate merge. No active roles, components, or occurrence claims require further evidence.

**Recommended Edits**: None.
