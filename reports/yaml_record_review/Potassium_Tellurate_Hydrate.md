# `data/ingredients/mapped/Potassium_Tellurate_Hydrate.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `potassium tellurate hydrate` is preserved as CAS `314041-10-6`, and PubChem CID 17749147 confirms the stored formula, SMILES, and InChI for the hydrate CAS. A fresh exact OLS4 CHEBI search found no exact `potassium tellurate hydrate` term, so the `CLOSE_MATCH` row to `CHEBI:30463` / `telluric acid` is the expected hydrate-safe parent relation rather than an exact ontology mapping.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Potassium_Tellurate_Hydrate.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Potassium_Tellurate_Hydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed, confirming the stored CHEBI parent label.

**Evidence**: The #342 curation note correctly explains why the hydrate row was demoted from a subsumptive `NARROW_MATCH` to `CLOSE_MATCH`, and final SSSOM row 2408 uses `skos:closeMatch`. Row 2409 keeps an exact CAS identity row, but an ignored/hidden local search over the current SSSOM found no exact `kgmicrobe.compound:potassium_tellurate_hydrate` sibling; `reports/hydrate_grounding.tsv` still marks this hydrate as `CAS_MISSING_ANCHOR_ROWS`.

**Completeness**: The chemical properties match the hydrate CAS and final `CAS:314041-10-6` token is valid. The final SSSOM is still missing the local exact registry anchor that should keep this CAS-primary close-match hydrate grounded as its own KG-Microbe compound.

**Recommended Edits**: Add an exact `kgmicrobe.compound:potassium_tellurate_hydrate` registry companion for `data/ingredients/mapped/Potassium_Tellurate_Hydrate.yaml`, synchronize `data/curated/mapped_ingredients.yaml`, regenerate SSSOM, and rerun `scripts/validate_sssom_invariants.py` plus `scripts/report_hydrate_grounding.py`.
