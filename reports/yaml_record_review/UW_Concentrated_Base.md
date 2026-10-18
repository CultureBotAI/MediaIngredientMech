# `data/ingredients/mapped/UW_Concentrated_Base.yaml`

## Verdict

Pass. The local fallback registry identity, complete 11-component stock
recipe, source-backed roles, aggregate row, case-preserving SSSOM alias, and
final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/UW_Concentrated_Base.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:uw_concentrated_base` with matching
  `ontology_mapping.ontology_id`, label `UW concentrated base`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, `ingredient_type: STOCK_SOLUTION`, and
  `solution_type: OTHER`.
- Components: 11 `MIM_CATALOG` components at the `g/L` values transcribed from
  the CultureBotHT `Mixes` tab.
- Occurrences: 9 CultureBotHT media occurrences.
- Roles: source-backed mineral, trace-element, iron, and sulfur roles.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `UW_Concentrated_Base` through `Uracil`: exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Engine A label validation was limited to the CHEBI records in this batch;
  this `kgmicrobe.ingredient` fallback registry row has no OBO adapter for that
  focused check.

## Evidence

- Downloaded the cited CultureBotHT Google Sheet as XLSX and inspected
  `Mixes!1602:1612`. The 11 source rows list the same component names,
  `20.0`, `28.9`, `6.67`, `0.0185`, `0.698`, `0.25`, `1.095`, `0.154`,
  `0.0392`, `0.025`, and `0.0177` concentrations, and `g/L` units recorded in
  `components`.
- The source rows contain magnesium/calcium salts, zinc/manganese/copper/cobalt
  and borate trace salts, one iron salt, and multiple sulfate salts, matching
  the four nutritional role facets.
- The final SSSOM row uses `MIM:UW_Concentrated_Base` and exactly maps to
  `kgmicrobe.ingredient:uw_concentrated_base`; `mappings/mim_curie_aliases.tsv`
  records the case alias from the old lower-case subject.

## Issues

None.

## Completeness

- The CultureBotHT source, 11-component partonomy, complete component
  assertion, source-backed roles, aggregate copy, case-preserving SSSOM alias,
  and final SSSOM row agree.
- A hidden/ignored-inclusive search across the worktree found the old lower-case
  alias seeds and no stale final SSSOM row for the superseded lower-case
  subject.

## Recommended Edits

None.
