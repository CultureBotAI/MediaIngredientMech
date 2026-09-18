# `data/ingredients/mapped/MH_agar.yaml`

## Verdict

Pass. The CultureMech residual exact-label grounding to MICRO:0001328, restored
structured evidence, one-recipe occurrence count, aggregate copy, and final
SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/MH_agar.yaml`.
- Identifier and grounding: `identifier: MICRO:0001328` with
  `ontology_mapping.ontology_id: MICRO:0001328`, label `MH agar`, source
  `MICRO`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`.
- Occurrences: one total occurrence in one CultureMech recipe.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `MH_agar` through `Macro_Component_1_For_J_Medium`: exited 0 and wrote zero
  ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` could not complete for
  this MICRO/local-primary batch because the local MICRO sqlite adapter lacks
  the expected OAK label table. EBI OLS4 was used for the MICRO label check
  instead.

## Evidence

- EBI OLS4 resolves `MICRO:0001328` as active `MH agar`.
- The final SSSOM publishes one `skos:exactMatch` row to `MICRO:0001328`; its
  `other` field is empty.
- The SSSOM row retains
  `MIM:culturemech:output/ingredient_occurrences.tsv`, reflecting the restored
  structured mapping evidence.

## Completeness

- The active MICRO identity, CultureMech occurrence count, restored SSSOM
  provenance, aggregate copy, and final SSSOM row are present and consistent.
- No unsupported role or synonym is asserted.

## Recommended Edits

- None.
