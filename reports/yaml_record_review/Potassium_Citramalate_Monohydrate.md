# `data/ingredients/mapped/Potassium_Citramalate_Monohydrate.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `potassium citramalate monohydrate` is preserved as CAS `1030365-02-6`, and the #342 repair correctly demoted the relation to `CHEBI:15584` / `citramalic acid` from a subsumptive narrow match to a hydrate/salt `CLOSE_MATCH`. Final SSSOM rows 2392 and 2393 publish the close CHEBI parent and exact CAS registry sibling.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Potassium_Citramalate_Monohydrate.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Potassium_Citramalate_Monohydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: PubChem CID 16211775 confirms the stored formula `C5H6K2O5`, SMILES, and InChI for CAS `1030365-02-6`, but those structure fields represent dipotassium citramalate without explicit hydrate water. They do not reproduce the monohydrate form named by the preferred term and curation notes. The final SSSOM `CAS:1030365-02-6` token is allowed because it matches `chemical_properties.cas_rn`. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected final close row, CAS exact row, and hydrate regrade references.

**Completeness**: The identity and predicate repair are complete enough, but the active chemical properties omit hydrate water and therefore describe the anhydrous dipotassium salt rather than the supplied monohydrate.

**Recommended Edits**: In `data/ingredients/mapped/Potassium_Citramalate_Monohydrate.yaml`, either replace the PubChem-derived formula, SMILES, and InChI with source-backed monohydrate chemistry or remove those fields until a registry source can represent the hydrate. Synchronize `data/curated/mapped_ingredients.yaml` and re-run strict validation plus the SSSOM invariant check.
