# `data/ingredients/mapped/Yeast_Extract_Peptone.yaml`

## Verdict

Pass. The local Yeast Extract + Peptone identity, complete two-part
decomposition, aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Yeast_Extract_Peptone.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:yeast_extract_peptone` with matching
  `ontology_mapping.ontology_id`, label `Yeast Extract + Peptone`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`, and
  `mapping_status: MAPPED`.
- `ingredient_type: UNDEFINED_MIXTURE`.
- Components: two complete `MIM_CATALOG` components, Yeast Extract
  `FOODON:03315426` and Peptone `MICRO:0000178`, with no concentrations
  because the source label states none.
- Synonyms: one raw MicrobeDecoder label, `Yeast Extract + Peptone`.
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
  MicrobeDecoder source label, with both constituents resolved to existing MIM
  records.
- The final SSSOM correctly exports
  `MIM:Yeast_Extract_Peptone skos:exactMatch
  kgmicrobe.ingredient:yeast_extract_peptone`.
- The raw duplicate label is not exported into final SSSOM `other`.

## Issues

None.

## Completeness

- The local exact identity, decomposition, aggregate copy, source occurrence,
  and final SSSOM row agree.

## Recommended Edits

None.
