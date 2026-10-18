# `data/ingredients/mapped/Polyethylene_Glycol.yaml`

**Verdict**: pass.

**Identity**: `Polyethylene glycol` maps to `CHEBI:46793` / `poly(ethylene glycol)` by the CultureBotHT CAS RN `25322-68-3`. The `CAS_RN_LOOKUP` quality records the mapping method, while final SSSOM row 2363 correctly remains an exact CHEBI row for the record's own ontology identity.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Polyethylene_Glycol.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Polyethylene_Glycol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The CultureBotHT CAS lookup supports the CHEBI mapping, and the #317 regrade records why `CAS_RN_LOOKUP` is provenance rather than a weaker identity grade. Final SSSOM `other` contains the reviewed CHEBI synonym, the CultureMech molecular-weight surface form for PEG, and `CAS:25322-68-3`, which matches `chemical_properties.cas_rn`. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected curated, generated, CultureMech alias, row-review, and final SSSOM references.

**Completeness**: The record has the CAS number, formula, structure strings from ChEBI, and curated same-substance synonyms. No component or role assertions are active.

**Recommended Edits**: None.
