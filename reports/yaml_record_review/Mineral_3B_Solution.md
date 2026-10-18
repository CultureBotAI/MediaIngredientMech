# `data/ingredients/mapped/Mineral_3B_Solution.yaml`

## Verdict

Pass. The local Mineral 3B stock-solution identity, component assertion,
source-backed nutritional roles, occurrence count, and final registry row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Mineral_3B_Solution.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:mineral_3b_solution` with
  `ontology_mapping.ontology_id:
  kgmicrobe.ingredient:mineral_3b_solution`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, `ingredient_type: STOCK_SOLUTION`, and
  `solution_type: MINERAL_STOCK`.
- Occurrences: nine CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Midecamycin` through `Mineral_3B_Solution_Minus_Nitrogen`: exited 0 and
  wrote zero ERROR rows.
- Direct Engine A term validation was skipped for this local registry record
  because its primary `kgmicrobe.ingredient` identifier is outside the OBO
  subset used for the batch.

## Evidence

- `mappings/unmapped_ingredients_ols_exact_audit.tsv` recorded no exact OLS hit
  before the fallback registry promotion.
- #114 curation kept this as a local mint because Mineral 3B solution is a
  named, recurring, multi-component lab preparation rather than an external
  ontology substance.
- The Bacic and Smith Mineral 3B solution recipe supports the eight inorganic
  salt components plus water, `component_assertion.method:
  RECIPE_TRANSCRIPTION`, and the mineral, phosphate, nitrogen, sulfur, and
  trace-element roles.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Mineral_3B_Solution` to
  `kgmicrobe.ingredient:mineral_3b_solution` with empty `other`.

## Completeness

- The local stock identity, component list, complete recipe transcription,
  role evidence, 9/9 occurrence count, and final registry row agree.
- The record does not publish unsupported roles or non-synonym final `other`
  text.

## Recommended Edits

- None.
