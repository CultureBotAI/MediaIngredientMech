# `data/ingredients/mapped/Potassium_Tellurite_Hydrate.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Potassium tellurite hydrate` is intended to preserve hydrate CAS `123333-66-4` and a `CLOSE_MATCH` parent relation to anhydrous `CHEBI:75248` / `potassium tellurite`. Fresh OLS4 exact search found no exact CHEBI hit for `potassium tellurite hydrate`, so the close parent shape is reasonable.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Potassium_Tellurite_Hydrate.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Potassium_Tellurite_Hydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed, confirming the stored CHEBI parent label.

**Evidence**: PubChem does not resolve CAS `123333-66-4`, and the stored PubChem CID 65186 has formula `K2O3Te`, SMILES, and InChI for anhydrous potassium tellurite rather than the named hydrate. The curated synonym `dipotassium tellurite` is also inherited from anhydrous `CHEBI:75248`, so final SSSOM row 2410 exports an anhydrous parent synonym as `other` for a hydrate-specific MIM subject. Row 2411 keeps an exact CAS identity row, but an ignored/hidden local search over the current SSSOM found no exact `kgmicrobe.compound:potassium_tellurite_hydrate` sibling; `reports/hydrate_grounding.tsv` still marks this hydrate as `CAS_MISSING_ANCHOR_ROWS`.

**Completeness**: The #342 close-match regrade is complete, but the record still needs hydrate-specific chemistry or no active structure fields, synonym cleanup so anhydrous parent aliases do not publish as exact hydrate aliases, and an exact KG-Microbe registry anchor in final SSSOM.

**Recommended Edits**: In `data/ingredients/mapped/Potassium_Tellurite_Hydrate.yaml`, remove the anhydrous `dipotassium tellurite` synonym from the hydrate record, replace or clear the anhydrous PubChem-derived structure fields, and add an exact `kgmicrobe.compound:potassium_tellurite_hydrate` registry companion. Synchronize `data/curated/mapped_ingredients.yaml`, regenerate SSSOM, and rerun strict validation, `scripts/validate_sssom_invariants.py`, and `scripts/report_hydrate_grounding.py`.
