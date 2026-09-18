# `data/ingredients/mapped/Malt_Extract_Broth.yaml`

## Verdict

Needs curation. The local exact malt-extract-broth identity, close FoodOn
parent, five-recipe occurrence count, and final SSSOM registry rows pass, but
this complete broth formulation still lacks component-level curation.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Malt_Extract_Broth.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:malt_extract_broth` with
  `ontology_mapping.ontology_id: FOODON:03301056`, label `malt extract`,
  source `FOODON`, `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: UNDEFINED_MIXTURE`.
- Local exact subject: `kgmicrobe.ingredient:malt_extract_broth`.
- Occurrences: five total occurrences in five CultureMech recipes.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Malt_Extract_Broth` through `Maltose`: exited 0 and wrote zero ERROR rows.
- LinkML term validation was skipped for this local-primary record because the
  subject identifier is outside the CHEBI/OBO term adapter scope.

## Evidence

- The 2026-05-05 review corrected an over-broad
  `FOODON:03301056` exact match by making the local malt-extract-broth
  identifier primary and retaining FoodOn malt extract only as a close parent.
- The final SSSOM publishes one close row to `FOODON:03301056` and one exact
  Rule B1 registry row to `kgmicrobe.ingredient:malt_extract_broth`.
- An ignored-file-inclusive search of the active YAML found no `components` or
  `component_assertion` block.

## Completeness

- The final SSSOM no longer overclaims exact equivalence to plain malt extract.
- The record names a complete medium formulation, but it has no component list
  or source-backed completeness assertion. Downstream exports therefore
  preserve the label without the formulation.

## Recommended Edits

- Transcribe component records and a `component_assertion` from source evidence
  for malt extract broth, or add a reviewed note explaining why the formulation
  cannot be decomposed yet.
