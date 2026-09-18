# `data/ingredients/mapped/Proline.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Proline` is mapped exactly to active `CHEBI:26271` / `proline`, the generic unstereospecified proline entry. The stored formula, SMILES, and InChI match that generic CHEBI structure.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Proline.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Proline.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The exact CHEBI row and CHEBI-derived synonyms in final SSSOM row 2423 are valid for generic proline, and the raw `Role: Nitrogen source` synonym is filtered from final `other`. However, `chemical_properties.cas_rn` is `147-85-3`, the L-proline CAS also used by the separate active `L-Proline` record; OLS4 CHEBI lists CAS `609-36-9` on `CHEBI:26271`, and PubChem resolves `609-36-9` to the DL-proline CID. The active `nutritional_roles.AMINO_ACID_SOURCE` assertion is also only a `COMPUTATIONAL_PREDICTION` from CHEBI ancestry with a provisional curator note.

**Completeness**: An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found that `CAS:147-85-3` is published for both `MIM:Proline` and the stereospecific `MIM:L-proline`; the latter owns that CAS RN.

**Recommended Edits**: In `data/ingredients/mapped/Proline.yaml`, replace `chemical_properties.cas_rn` with source-backed generic/DL-proline CAS `609-36-9` or remove the CAS field so `CAS:147-85-3` stops publishing on `MIM:Proline`. Replace the provisional `AMINO_ACID_SOURCE` role with source-backed evidence or remove it. Synchronize `data/curated/mapped_ingredients.yaml`, regenerate SSSOM, and rerun strict validation plus `scripts/validate_sssom_invariants.py`.
