# `data/ingredients/mapped/Sulfur-free_DL_Minerals.yaml`

## Verdict

Pass. The local `kgmicrobe.ingredient` stock-solution identity, complete
15-component partonomy, source-backed mineral-source role, aggregate row, and
final SSSOM registry row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Sulfur-free_DL_Minerals.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:sulfur-free_dl_minerals` with the same
  `ontology_mapping.ontology_id`, label `Sulfur-free DL minerals`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, `ingredient_type: STOCK_SOLUTION`, and
  `solution_type: MINERAL_STOCK`.
- Components: 15 `MIM_CATALOG` components transcribed from the CultureBotHT
  Mixes tab and marked `component_assertion.completeness: COMPLETE`.
- Occurrences: 6 occurrences across 6 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sulfite` through `Sulfur`: exited 0 and wrote zero ERROR rows.
- Direct old Engine A/OBO term validation was skipped for this local
  `kgmicrobe.ingredient` fallback row because that prefix is intentionally
  outside the CHEBI-focused OBO term subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- `uv run --frozen python scripts/validate_component_partonomy.py` was rerun
  after this batch and exited 0.

## Evidence

- The CultureBotHT Mixes-tab transcription supports the named 15-component
  sulfur-free mineral stock and its chloride, borate, molybdate, selenite, and
  tungstate constituents.
- The `MINERAL_SOURCE` role is supported by the same database-entry evidence
  that identifies the stock as a mineral and trace stock for sulfur-omission
  media.
- The final SSSOM row exact-matches
  `kgmicrobe.ingredient:sulfur-free_dl_minerals`, uses
  `semapv:ManualMappingCuration`, and leaves `other` empty.

## Completeness

- The local fallback identity, stock classification, aggregate row, 6
  occurrences, 15 component rows, and final SSSOM row agree.
- All components have `MIM_CATALOG` scope, component IDs, concentration values,
  and concentration units.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected CultureBotHT, component,
  alias, aggregate, generated index, and final SSSOM rows. The
  `mim_curie_aliases.tsv` `Sulfur-free_DL_minerals` alias is the expected
  compatibility alias for a case-only filename change.

## Recommended Edits

- None.
