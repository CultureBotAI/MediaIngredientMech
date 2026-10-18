# `data/ingredients/mapped/Potassium_Oxalate_Monohydrate.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Potassium oxalate monohydrate` is preserved as CAS `6487-48-5`, and PubChem CID 2724193 confirms the stored formula, SMILES, and InChI for the monohydrate CAS. The record pairs that exact identity with a `NARROW_MATCH` parent row to `NCIT:C87592` / `Potassium Oxalate`.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Potassium_Oxalate_Monohydrate.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Potassium_Oxalate_Monohydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed, confirming the stored NCIT parent label.

**Evidence**: Final SSSOM rows 2399 and 2400 correctly preserve exact CAS and KG-Microbe registry rows for the hydrate identity, and `CAS:6487-48-5` is valid because it matches `chemical_properties.cas_rn`. Row 2398 still treats a hydrate as narrower than the anhydrous potassium oxalate term; that is the same subsumptive hydrate predicate that #342 regraded to `CLOSE_MATCH` for potassium citramalate monohydrate. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected exact registry rows and final NCIT parent row.

**Completeness**: The chemistry fields include hydrate water and match the CAS identity, but the non-exact ontology relation overstates the relationship to the anhydrous parent.

**Recommended Edits**: Regrade the `NCIT:C87592` parent relation in `data/ingredients/mapped/Potassium_Oxalate_Monohydrate.yaml` from `NARROW_MATCH` to the hydrate-safe close-match form used by #342, then regenerate SSSOM and rerun `scripts/validate_sssom_invariants.py`.
