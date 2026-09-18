# `data/ingredients/mapped/Modified_Cooked_Meat_Medium.yaml`

## Verdict

Pass. The local Modified Cooked Meat Medium identity, curated partial
component assertion, MicrobeDecoder provenance, and final registry row pass.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Modified_Cooked_Meat_Medium.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:modified_cooked_meat_medium` with
  `ontology_mapping.ontology_id:
  kgmicrobe.ingredient:modified_cooked_meat_medium`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, and `ingredient_type: UNDEFINED_MIXTURE`.
- Occurrences: one imported MicrobeDecoder substrate occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mnso4_X_7_H2o` through `Modified_Trace_Vitamins`: exited 0 and wrote zero
  ERROR rows.
- Direct Engine A term validation was skipped for this local registry record
  because its primary `kgmicrobe.ingredient` identifier is outside the OBO
  subset used for the batch.

## Evidence

- `mappings/microbedecoder_residual_research_decomposition.tsv` classified the
  original residual as a complex medium and curated a partial `map_to_medium`
  decomposition to FOODON `meat (cooked)`.
- A fresh exact EBI OLS4 lookup returned no same-label external class for
  `Modified Cooked Meat Medium`.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Modified_Cooked_Meat_Medium` to
  `kgmicrobe.ingredient:modified_cooked_meat_medium` with empty `other`.

## Completeness

- The local medium identity, partial curated component assertion, source
  occurrence, fallback registry mapping, and final row agree.
- The record does not publish unsupported roles or non-synonym final `other`
  text.

## Recommended Edits

- None.
