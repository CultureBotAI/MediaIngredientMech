# `data/ingredients/mapped/Modified_P-iv_Chelated_Micronutrient_Solution.yaml`

## Verdict

Pass. The local Modified P-IV chelated Micronutrient Solution trace-metal stock
identity, occurrence count, fallback registry mapping, and final registry row
pass.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Modified_P-iv_Chelated_Micronutrient_Solution.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:modified_p-iv_chelated_micronutrient_solution`
  with `ontology_mapping.ontology_id:
  kgmicrobe.ingredient:modified_p-iv_chelated_micronutrient_solution`,
  source `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, `ingredient_type: STOCK_SOLUTION`, and
  `solution_type: TRACE_METAL_MIX`.
- Occurrences: one CultureMech recipe occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mnso4_X_7_H2o` through `Modified_Trace_Vitamins`: exited 0 and wrote zero
  ERROR rows.
- Direct Engine A term validation was skipped for this local registry record
  because its primary `kgmicrobe.ingredient` identifier is outside the OBO
  subset used for the batch.

## Evidence

- `mappings/unmapped_ingredients_ols_exact_audit.tsv` recorded no exact OLS hit
  before the fallback registry promotion.
- #114 curation kept this as a local mint because the label denotes a named,
  recurring, multi-component trace-metal preparation rather than an external
  ontology substance.
- A fresh exact EBI OLS4 lookup returned no same-label external class.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Modified_P-iv_Chelated_Micronutrient_Solution` to the local registry
  identifier with empty `other`.

## Completeness

- The local stock identity, 1/1 occurrence count, fallback registry rationale,
  and final row agree.
- The record does not publish unsupported roles or non-synonym final `other`
  text.

## Recommended Edits

- None.
