# `data/ingredients/mapped/Plastic.yaml`

**Verdict**: pass.

**Identity**: `Plastic` is an imported kgm-metatraits environmental material record mapped exactly to `ENVO:06105101` `plastic` and classified as `UNDEFINED_MIXTURE`. The ENVO identifier, canonical label, source prefix, `EXACT_MATCH` quality, and final SSSOM row 2347 agree.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Plastic.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Plastic.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed, confirming the ENVO ID and label.

**Evidence**: The kgm-metatraits import evidence supports a source-preset import from `kgm.metatraits.special:plastic`; the later history correction aligns `ontology_source: ENVO` with the ENVO identifier. The final SSSOM row maps `MIM:Plastic` to `ENVO:06105101`, uses `obo:envo.owl` as the object source, and has no `other` tokens that need synonym triage. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected curated, generated, row-review, and final SSSOM references.

**Completeness**: No chemical formula, components, roles, or media occurrences are expected for this zero-occurrence environmental mixture import. Empty synonym and component slots are appropriate.

**Recommended Edits**: None.
