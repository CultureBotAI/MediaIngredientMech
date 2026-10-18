# `data/ingredients/mapped/Wolfes_Vitamin_Mix.yaml`

## Verdict

Pass. The local Wolfe's vitamin mix identity, fallback registry grounding,
component transcription, source-backed vitamin role, aggregate row, and final
exact SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Wolfes_Vitamin_Mix.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:wolfes_vitamin_mix` with matching
  `ontology_mapping.ontology_id`, label `Wolfe's vitamin mix`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`, and
  `mapping_status: MAPPED`.
- `ingredient_type: STOCK_SOLUTION` and `solution_type: VITAMIN_MIX`.
- Components: 12 complete `MIM_CATALOG` entries transcribed from NCMA Medium 6
  Wolfe's Vitamin Solution.
- Synonyms: one raw CultureBotHT surface form, `Wolfe's vitamin mix`.
- Occurrences: 61 CultureBotHT media occurrences.
- Role: source-backed `VITAMIN_SOURCE`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Wolfes_Vitamin_Mix` through `Xanthine`: exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- `uv run --frozen python scripts/validate_component_partonomy.py` found 83
  decompositions, 505 components, and zero violations.
- Engine A label validation was limited to the CHEBI-primary records in this
  batch; this local `kgmicrobe.ingredient` row has no OBO adapter for that
  focused check.

## Evidence

- The `#114` curation history records this as a named standard
  multi-component supplement that had no exact CHEBI, NCIT, MeSH, FOODON, or
  ENVO term and should keep a local fallback identifier.
- The cited NCMA Medium 6 source lists Wolfe's Vitamin Solution as pyridoxine
  HCl 10.0 mg/L, thiamine HCl 5.0 mg/L, riboflavin 5.0 mg/L, nicotinic acid
  5.0 mg/L, calcium pantothenate 5.0 mg/L, p-aminobenzoic acid 5.0 mg/L,
  thioctic acid 5.0 mg/L, biotin 2.0 mg/L, folic acid 2 mg/L, vitamin B12
  0.1 mg/L, and potassium phosphate monobasic 900 mg/L; it directs adding the
  components to distilled water, matching the record's solvent component.
- The `VITAMIN_SOURCE` role cites the same NCMA technical report.
- The final SSSOM correctly exports
  `MIM:Wolfes_Vitamin_Mix skos:exactMatch kgmicrobe.ingredient:wolfes_vitamin_mix`.

## Issues

None.

## Completeness

- The local exact identity, stock-solution classification, component list,
  source-backed role, aggregate copy, occurrence count, and final SSSOM row
  agree.

## Recommended Edits

None.
