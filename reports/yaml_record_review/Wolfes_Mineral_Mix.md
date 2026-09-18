# `data/ingredients/mapped/Wolfes_Mineral_Mix.yaml`

## Verdict

Pass. The local Wolfe's mineral mix identity, fallback registry grounding,
component transcription, source-backed mineral and trace-element roles,
aggregate row, and final exact SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Wolfes_Mineral_Mix.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:wolfes_mineral_mix` with matching
  `ontology_mapping.ontology_id`, label `Wolfe's mineral mix`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`, and
  `mapping_status: MAPPED`.
- `ingredient_type: STOCK_SOLUTION` and `solution_type: MINERAL_STOCK`.
- Components: 13 complete `MIM_CATALOG` entries transcribed from ATCC Medium
  2672 Wolfe's Mineral Solution.
- Synonyms: one raw CultureBotHT surface form, `Wolfe's mineral mix`.
- Occurrences: 60 CultureBotHT media occurrences.
- Roles: source-backed `MINERAL_SOURCE` and `TRACE_ELEMENT`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Wc_Trace_Elements_Solution` through
  `Wolfes_Mineral_Mix_minus_Nitrilotriacetic_acid`: exited 0 and wrote zero
  ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- `uv run --frozen python scripts/validate_component_partonomy.py` found 83
  decompositions, 505 components, and zero violations.
- Engine A label validation was limited to the CHEBI-primary record in this
  batch; this local `kgmicrobe.ingredient` row has no OBO adapter for that
  focused check.

## Evidence

- The `#114` curation history records this as a named recurring
  multi-component preparation that had no exact CHEBI, NCIT, MeSH, FOODON, or
  ENVO term and should keep a local fallback identifier.
- The cited ATCC Medium 2672 source lists Wolfe's Mineral Solution as 0.5 g
  EDTA, 3.0 g magnesium sulfate heptahydrate, 0.5 g manganese sulfate
  monohydrate, 1.0 g sodium chloride, 0.1 g ferrous sulfate heptahydrate,
  0.1 g cobalt chloride hexahydrate, 0.1 g calcium chloride, 0.1 g zinc sulfate
  heptahydrate, 0.01 g copper sulfate pentahydrate, 0.01 g potassium aluminum
  sulfate dodecahydrate, 0.01 g boric acid, 0.01 g sodium molybdate
  dihydrate, and 1.0 L distilled water, matching the record.
- The `MINERAL_SOURCE` and `TRACE_ELEMENT` roles cite the same ATCC technical
  report.
- The final SSSOM correctly exports
  `MIM:Wolfes_Mineral_Mix skos:exactMatch kgmicrobe.ingredient:wolfes_mineral_mix`.

## Issues

None.

## Completeness

- The local exact identity, stock-solution classification, component list,
  source-backed roles, aggregate copy, occurrence count, and final SSSOM row
  agree.

## Recommended Edits

None.
