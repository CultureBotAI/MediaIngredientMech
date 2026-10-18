# `data/ingredients/mapped/Yeast_Extract_Gluconate.yaml`

## Verdict

Pass. The local Yeast Extract + Gluconate identity, two-part decomposition,
aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Yeast_Extract_Gluconate.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:yeast_extract_gluconate` with matching
  `ontology_mapping.ontology_id`, label `Yeast Extract + Gluconate`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`, and
  `mapping_status: MAPPED`.
- `ingredient_type: UNDEFINED_MIXTURE`.
- Components: two complete `MIM_CATALOG` components, `yeast extract`
  `FOODON:03315426` and `D-gluconate` `CHEBI:18391`, with no concentrations
  because the source label states none.
- Synonyms: one raw MicrobeDecoder label, `Yeast Extract + Gluconate`.
- Occurrences: one MicrobeDecoder Bergey's substrates occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Xylotriose` through `Yeast_Extract_Gluconate`: exited 0 and wrote zero ERROR
  rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- `uv run --frozen python scripts/validate_component_partonomy.py` found 83
  decompositions, 505 components, and zero violations.
- Engine A label validation was limited to the CHEBI-primary record in this
  batch; this local `kgmicrobe.ingredient` row has no OBO adapter for that
  focused check.

## Evidence

- The curated `component_assertion` uses `LABEL_ENUMERATION` evidence from the
  MicrobeDecoder source label plus the curated residual-research split, with
  both top-level constituents resolved to existing MIM records.
- The final SSSOM correctly exports
  `MIM:Yeast_Extract_Gluconate skos:exactMatch
  kgmicrobe.ingredient:yeast_extract_gluconate`.
- The raw duplicate label is not exported into final SSSOM `other`.

## Issues

None.

## Completeness

- The local exact identity, decomposition, aggregate copy, source occurrence,
  and final SSSOM row agree.

## Recommended Edits

None.
