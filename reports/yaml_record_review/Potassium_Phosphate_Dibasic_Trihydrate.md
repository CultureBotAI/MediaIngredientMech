# `data/ingredients/mapped/Potassium_Phosphate_Dibasic_Trihydrate.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Potassium phosphate dibasic trihydrate` is preserved as CAS `16788-57-1`; PubChem CID 16217523 confirms the stored trihydrate formula, SMILES, and InChI with three explicit water components. The `mesh:C013216` / `potassium phosphate` row is a broader phosphate parent, and final SSSOM rows 2403-2405 preserve that parent together with exact CAS and `kgmicrobe.compound:potassium_phosphate_dibasic_trihydrate` rows for the hydrate identity.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Potassium_Phosphate_Dibasic_Trihydrate.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Potassium_Phosphate_Dibasic_Trihydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed, confirming the stored MESH label.

**Evidence**: The CAS identity, PubChem chemistry, and final `CAS:16788-57-1` synonym are internally consistent. The active `physicochemical_roles.BUFFER` assertion is still only a `COMPUTATIONAL_PREDICTION` with the note `Provisional in-session LLM role assignment; review recommended.`, so it is not source-backed evidence for this exact salt hydrate.

**Completeness**: The mapping, hydrate chemistry, occurrence statistics, and final SSSOM rows are complete enough for the represented identity. The remaining gap is the provisional role claim.

**Recommended Edits**: In `data/ingredients/mapped/Potassium_Phosphate_Dibasic_Trihydrate.yaml`, either replace `physicochemical_roles.BUFFER` with source-backed evidence or remove the role. Synchronize `data/curated/mapped_ingredients.yaml`, regenerate SSSOM if the curated output changes, and rerun strict validation plus `scripts/validate_sssom_invariants.py`.
