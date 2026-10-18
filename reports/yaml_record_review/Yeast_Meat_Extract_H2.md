# `data/ingredients/mapped/Yeast_Meat_Extract_H2.yaml`

## Verdict

Needs curation. The local Yeast + Meat Extract + H2 fallback identity,
aggregate row, and final SSSOM row pass, but the complete decomposition still
leaves `Yeast` as an unresolved component even though MIM now has a mapped
Yeast record.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Yeast_Meat_Extract_H2.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:yeast_meat_extract_h2` with matching
  `ontology_mapping.ontology_id`, label `Yeast + Meat Extract + H2`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`, and
  `mapping_status: MAPPED`.
- `ingredient_type: UNDEFINED_MIXTURE`.
- Components: Meat Extract `FOODON:03315424` and H2 `CHEBI:18276` are
  `MIM_CATALOG`, but the `Yeast` component remains `reference_scope: UNMAPPED`
  and has no `component_id`.
- Synonyms: one raw MicrobeDecoder label, `Yeast + Meat Extract + H2`.
- Occurrences: one MicrobeDecoder Bergey's substrates occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on this 5-file batch:
  exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- `uv run --frozen python scripts/validate_component_partonomy.py` found 83
  decompositions, 505 components, and zero violations.
- Focused Engine A label validation was skipped for this local
  `kgmicrobe.ingredient` row because it has no CHEBI/OBO adapter.

## Evidence

- The curated `component_assertion` uses `LABEL_ENUMERATION` evidence from the
  MicrobeDecoder source label and marks the decomposition `COMPLETE`.
- The 2026-08-14 decomposition history says the Yeast constituent had no
  component ID because MIM had no record for it at the time.
- MIM now has `data/ingredients/mapped/Yeast.yaml`, mapped exactly to
  `FOODON:03411345`, so the unresolved component assertion is stale.
- The final SSSOM correctly exports
  `MIM:Yeast_Meat_Extract_H2 skos:exactMatch
  kgmicrobe.ingredient:yeast_meat_extract_h2`.
- The raw duplicate label is not exported into final SSSOM `other`.

## Issues

- Major: the first component should be linked to the existing MIM Yeast record
  instead of remaining an `UNMAPPED` component without a `component_id`.

## Completeness

- The local exact identity, aggregate copy, occurrence, and final SSSOM row
  agree.
- The complete component assertion should be refreshed now that all three
  named parts are mapped.

## Recommended Edits

- Set the `Yeast` component to `component_id: FOODON:03411345` with
  `reference_scope: MIM_CATALOG`.
- Add curation history documenting the component repair.
- Rerun strict validation, SSSOM invariant validation, and component-partonomy
  validation.
