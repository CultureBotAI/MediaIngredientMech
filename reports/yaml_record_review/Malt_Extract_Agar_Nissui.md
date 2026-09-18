# `data/ingredients/mapped/Malt_Extract_Agar_Nissui.yaml`

## Verdict

Needs curation. The local exact Nissui identity, close FoodOn parent,
one-recipe occurrence count, and final SSSOM registry rows pass, but this
supplier-specific malt-extract-agar formulation still lacks component-level
curation.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Malt_Extract_Agar_Nissui.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:malt_extract_agar_~28nissui~29` with
  `ontology_mapping.ontology_id: FOODON:03301056`, label `malt extract`,
  source `FOODON`, `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: UNDEFINED_MIXTURE`.
- Local exact subject:
  `kgmicrobe.ingredient:malt_extract_agar_~28nissui~29`.
- Occurrences: one total occurrence in one CultureMech recipe.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Malonic_Acid` through `Malt_Extract_Agar_Oxoid`: exited 0 and wrote zero
  ERROR rows.
- LinkML term validation was skipped for this local-primary record because the
  subject identifier is outside the CHEBI/OBO term adapter scope.

## Evidence

- The 2026-05-05 review corrected an over-broad
  `FOODON:03301056` exact match by making the local supplier-specific
  malt-extract-agar identifier primary and retaining FoodOn malt extract only
  as a close parent.
- A current EBI OLS4 exact search found no FoodOn class for
  `Malt extract agar`, supporting the local exact identity.
- The final SSSOM publishes one close row to `FOODON:03301056` and one exact
  Rule B1 registry row to
  `kgmicrobe.ingredient:malt_extract_agar_~28nissui~29`.
- An ignored-file-inclusive search of the active YAML found no `components` or
  `component_assertion` block.

## Completeness

- The final SSSOM no longer overclaims exact equivalence to plain malt extract.
- The record preserves the Nissui catalog surface form as its local exact
  identity, but it has no component list or source-backed completeness
  assertion for the supplier-specific formulation.

## Recommended Edits

- Transcribe component records and a `component_assertion` from source evidence
  for the Nissui formulation, or add a reviewed note explaining why the
  formulation cannot be decomposed yet.
