# `data/ingredients/mapped/Polysaccharides.yaml`

**Verdict**: pass.

**Identity**: `Polysaccharides` maps by plural synonym to `CHEBI:18154` / `polysaccharide`. The MicrobeDecoder source label, CHEBI class target, `SYNONYM_MATCH` quality, and final SSSOM row 2372 agree.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Polysaccharides.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Polysaccharides.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The residual MicrobeDecoder promotion records `Polysaccharides` as a synonym of `CHEBI:18154` `polysaccharide`, which is a safe plural-to-singular class mapping. Final SSSOM row 2372 has no `other` tokens to triage. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected curated, generated, residual-grounding, and final SSSOM references.

**Completeness**: No active roles, components, or chemistry fields are asserted for this MicrobeDecoder polysaccharide class.

**Recommended Edits**: None.
