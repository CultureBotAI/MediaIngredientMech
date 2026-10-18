# `data/ingredients/mapped/Polyvinyl_alcohol.yaml`

**Verdict**: pass.

**Identity**: `Polyvinyl alcohol` maps by exact synonym to `CHEBI:17246` / `poly(vinyl alcohol) macromolecule`. The CultureMech residual source, CHEBI target, `SYNONYM_MATCH` quality, and final SSSOM row 2373 agree.

**Validation**: `uv run --frozen python scripts/validate_strict.py ... Polyvinyl_alcohol.yaml ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Polyvinyl_alcohol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels` passed.

**Evidence**: The creation history and restored structured evidence both point to CultureMech occurrence-table rows that were grounded to `CHEBI:17246` through an exact ontology synonym for `Polyvinyl alcohol`. Final SSSOM row 2373 has no `other` synonyms to triage. An ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found the expected residual-grounding, curated, generated, and final SSSOM references.

**Completeness**: The record has its two CultureMech source occurrences, the exact CHEBI class, and no unsupported roles, components, or chemistry fields.

**Recommended Edits**: None.
