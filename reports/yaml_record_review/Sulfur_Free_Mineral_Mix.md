# `data/ingredients/mapped/Sulfur_Free_Mineral_Mix.yaml`

## Verdict

Needs curation - major. The local `kgmicrobe.ingredient` fallback identity and
final SSSOM row pass, but the record is a mapped sulfur-free mineral stock with
no component partonomy even though its own curation notes still say component
recipe curation is pending.

## Identity

- Reviewed record: `data/ingredients/mapped/Sulfur_Free_Mineral_Mix.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:sulfur_free_mineral_mix` with the same
  `ontology_mapping.ontology_id`, label `Sulfur free mineral mix`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, `ingredient_type: STOCK_SOLUTION`, and
  `solution_type: MINERAL_STOCK`.
- Components: none.
- Occurrences: 1 occurrence in 1 CultureMech medium.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sulfur_Compounds` through `Sunflower_Oil`: exited 0 and wrote zero ERROR
  rows.
- Direct old Engine A/OBO term validation was skipped for this local
  `kgmicrobe.ingredient` fallback row because that prefix is intentionally
  outside the CHEBI-focused OBO term subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- `uv run --frozen python scripts/validate_component_partonomy.py` was rerun
  after this batch and exited 0, but this does not prove a missing
  decomposition is complete.

## Evidence

- The CultureBotHT import and #114 fallback decision support minting a local
  stock-solution identifier because `Sulfur free mineral mix` is a named
  multi-component lab preparation rather than a single public ontology
  substance.
- The May 2026 review classified the record as a sulfur-free mineral stock and
  explicitly left it awaiting component-level recipe curation.
- Major: unlike the adjacent `Sulfur-free_DL_Minerals` stock, this record still
  has no `components`, no `component_assertion`, and no source-backed
  nutritional role. An ignored/hidden search for the label, slug, and
  `M63_no_sulfur` only found the promoted fallback record and generated copies,
  not a later component transcription.
- The final SSSOM row exact-matches
  `kgmicrobe.ingredient:sulfur_free_mineral_mix`, uses
  `semapv:ManualMappingCuration`, and leaves `other` empty.

## Completeness

- The local fallback identity, aggregate row, 1 occurrence, and final SSSOM row
  agree.
- The record is materially incomplete as a stock solution because it lacks the
  Mixes-tab component rows, recipe-transcription assertion, and mineral-source
  evidence needed to describe what the stock contains.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected CultureBotHT, alias,
  aggregate, generated index, and final SSSOM rows; the
  `mim_curie_aliases.tsv` `Sulfur_free_mineral_mix` alias is the expected
  compatibility alias for a case-only filename change.

## Recommended Edits

- Major: transcribe the maintained CultureBotHT recipe for `Sulfur free mineral
  mix` into `data/ingredients/mapped/Sulfur_Free_Mineral_Mix.yaml`, adding the
  component list, `component_assertion`, and any source-backed mineral role
  that the recipe supports.
- Major: rerun `uv run --frozen python scripts/validate_component_partonomy.py`
  and the normal generated-product build after curation so the aggregate and
  docs carry the complete stock decomposition.
