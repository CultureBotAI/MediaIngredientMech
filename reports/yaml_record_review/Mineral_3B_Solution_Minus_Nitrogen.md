# `data/ingredients/mapped/Mineral_3B_Solution_Minus_Nitrogen.yaml`

## Verdict

Pass. The local nitrogen-free Mineral 3B stock-solution identity, complete
component assertion, mineral-source role, occurrence count, and final registry
row pass.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Mineral_3B_Solution_Minus_Nitrogen.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:mineral_3b_solution_minus_nitrogen` with
  `ontology_mapping.ontology_id:
  kgmicrobe.ingredient:mineral_3b_solution_minus_nitrogen`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, `ingredient_type: STOCK_SOLUTION`, and
  `solution_type: MINERAL_STOCK`.
- Occurrences: five CultureMech recipe occurrences.

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
- #114 curation kept this as a local mint because the nitrogen-free Mineral 3B
  solution is a named, recurring, multi-component lab preparation rather than
  an external ontology substance.
- The CultureBotHT Mixes-tab transcription supports the seven potassium,
  sodium, magnesium, calcium, cobalt, manganese, and sulfate salt components
  and omits the ammonium chloride component present in the full Mineral 3B
  solution.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Mineral_3B_Solution_Minus_Nitrogen` to
  `kgmicrobe.ingredient:mineral_3b_solution_minus_nitrogen` with empty
  `other`.

## Completeness

- The local stock identity, seven-component complete recipe transcription,
  source-backed mineral role, 5/5 occurrence count, and final registry row
  agree.
- The record does not publish unsupported roles or non-synonym final `other`
  text.

## Recommended Edits

- None.
