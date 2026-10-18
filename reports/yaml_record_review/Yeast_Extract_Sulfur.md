# `data/ingredients/mapped/Yeast_Extract_Sulfur.yaml`

## Verdict

Pass. The local Yeast Extract + Sulfur identity, curated elemental-sulfur
component, complete two-part decomposition, aggregate row, and final SSSOM row
pass.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Yeast_Extract_Sulfur.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:yeast_extract_sulfur` with matching
  `ontology_mapping.ontology_id`, label `Yeast Extract + Sulfur`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`, and
  `mapping_status: MAPPED`.
- `ingredient_type: UNDEFINED_MIXTURE`.
- Components: two complete `MIM_CATALOG` components, yeast extract
  `FOODON:03315426` and sulfur `CHEBI:33403`, with no concentrations because
  the source label states none.
- Synonyms: one raw MicrobeDecoder label, `Yeast Extract + Sulfur`.
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
  MicrobeDecoder source label and the curated residual-research split, with
  both top-level constituents resolved to existing MIM records.
- The 2026-09-11 sulfur-family correction moved the second component from the
  sulfur atom term to elemental sulfur `CHEBI:33403`.
- The final SSSOM correctly exports
  `MIM:Yeast_Extract_Sulfur skos:exactMatch
  kgmicrobe.ingredient:yeast_extract_sulfur`.
- The raw duplicate label is not exported into final SSSOM `other`.

## Issues

None.

## Completeness

- The local exact identity, decomposition, aggregate copy, source occurrence,
  and final SSSOM row agree.

## Recommended Edits

None.
