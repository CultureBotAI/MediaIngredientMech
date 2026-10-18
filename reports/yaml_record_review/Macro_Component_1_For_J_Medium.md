# `data/ingredients/mapped/Macro_Component_1_For_J_Medium.yaml`

## Verdict

Needs curation. The local fallback identity, one-recipe occurrence count,
aggregate copy, and final SSSOM row pass, but the record still lacks
component-level curation for a named multi-component J medium stock.

Severity: major.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Macro_Component_1_For_J_Medium.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:macro_component_1_for_j_medium` with
  `ontology_mapping.ontology_id:
  kgmicrobe.ingredient:macro_component_1_for_j_medium`, label
  `Macro Component 1 for J Medium`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: STOCK_SOLUTION`.
- Solution type: `OTHER`.
- Occurrences: one total occurrence in one CultureMech recipe.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `MH_agar` through `Macro_Component_1_For_J_Medium`: exited 0 and wrote zero
  ERROR rows.
- Local `kgmicrobe.ingredient` identifiers are outside the CHEBI/OBO
  `linkml-term-validator` adapter scope.

## Evidence

- The OLS exact audit for the earlier unmapped
  `Macro_Component_1_For_J_Medium` record found no exact OLS hit and
  recommended keeping the term local or manually reviewing it.
- A gitignored-inclusive search found no later external OBO grounding for this
  J medium stock and found the current local exact row in final SSSOM.
- The final SSSOM publishes one local `skos:exactMatch` row to
  `kgmicrobe.ingredient:macro_component_1_for_j_medium`; its `other` field is
  empty.

## Completeness

- The local fallback identity, occurrence count, aggregate copy, and final SSSOM
  row are present and consistent.
- The 2026-05-11 review classified this record as a named macro-component stock
  for J medium pending component-level recipe curation. No `components` or
  `component_assertion` block has been added, so downstream exports cannot
  recover the actual composition of this named stock.

## Recommended Edits

- Transcribe the `Macro Component 1 for J Medium` stock recipe into
  `components` and add a `component_assertion` with source-backed completeness,
  or record why the source recipe is unavailable.
