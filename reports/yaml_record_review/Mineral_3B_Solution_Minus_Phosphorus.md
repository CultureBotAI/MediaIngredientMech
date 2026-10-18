# `data/ingredients/mapped/Mineral_3B_Solution_Minus_Phosphorus.yaml`

## Verdict

Pass. The local phosphorus-free Mineral 3B stock-solution identity,
occurrence count, fallback registry mapping, and final registry row pass.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Mineral_3B_Solution_Minus_Phosphorus.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:mineral_3b_solution_minus_phosphorus` with
  `ontology_mapping.ontology_id:
  kgmicrobe.ingredient:mineral_3b_solution_minus_phosphorus`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, `ingredient_type: STOCK_SOLUTION`, and
  `solution_type: MINERAL_STOCK`.
- Occurrences: one CultureMech recipe occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mineral_3B_Solution_Minus_Phosphorus` through `Minerals`: exited 0 and
  wrote zero ERROR rows.
- Direct Engine A term validation was skipped for this local registry record
  because its primary `kgmicrobe.ingredient` identifier is outside the OBO
  subset used for the batch.

## Evidence

- `mappings/unmapped_ingredients_ols_exact_audit.tsv` recorded no exact OLS hit
  before the fallback registry promotion.
- #114 curation kept this as a local mint because Mineral 3B solution minus
  phosphorus is a named, recurring, multi-component lab preparation rather
  than an external ontology substance.
- A fresh exact EBI OLS4 lookup returned no same-label external class.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Mineral_3B_Solution_Minus_Phosphorus` to
  `kgmicrobe.ingredient:mineral_3b_solution_minus_phosphorus` with empty
  `other`.

## Completeness

- The local stock identity, 1/1 occurrence count, fallback registry rationale,
  and final SSSOM row agree.
- The record does not publish unsupported roles or non-synonym final `other`
  text.

## Recommended Edits

- None.
