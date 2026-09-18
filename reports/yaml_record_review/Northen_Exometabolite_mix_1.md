# `data/ingredients/mapped/Northen_Exometabolite_mix_1.yaml`

## Verdict

Pass. The named Northen exometabolite stock mix is intentionally retained as a
local `kgmicrobe.ingredient` fallback identity, with no exact external OBO hit
and no component or role claims that overstate the available evidence.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Northen_Exometabolite_mix_1.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:northen_exometabolite_mix_1` with
  matching `ontology_mapping.ontology_id`,
  `ontology_source: kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`,
  `ingredient_type: STOCK_SOLUTION`, and `solution_type: OTHER`.
- Occurrences: 3 CultureBot recipe occurrences across 3 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 and wrote zero
  ERROR rows.
- Engine A OBO label validation was skipped because the ontology id uses the
  non-OBO `kgmicrobe.ingredient` prefix.

## Evidence

- The curated fallback evidence says this is a recurring multi-component
  lab preparation and should be minted under `kgmicrobe.ingredient` rather
  than mapped to any single compound parent.
- Fresh exact OLS4 searches for both `Northen_Exometabolite_mix_1` and
  `Northen Exometabolite mix 1` found zero exact ontology hits, matching the
  local fallback-registry rationale.
- The final SSSOM row maps `MIM:Northen_Exometabolite_mix_1` exactly to
  `kgmicrobe.ingredient:northen_exometabolite_mix_1` and exports no `other`
  tokens.
- No roles, components, supplied forms, chemical properties, or environmental
  contexts are asserted.

## Completeness

- The local registry CURIE, stock-solution classification, occurrence count,
  and final SSSOM row agree.
- Component-level recipe curation remains explicitly pending, so the empty
  `components` slot is a known absence rather than a false decomposition.

## Recommended Edits

- None.
