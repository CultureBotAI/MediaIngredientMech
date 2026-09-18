# `data/ingredients/mapped/TYG_Salts_Solution.yaml`

## Verdict

Needs curation - major. The local fallback identity, occurrence count,
aggregate row, and final exact registry row pass, but this recurring TYG stock
solution still lacks component partonomy.

## Identity

- Reviewed record: `data/ingredients/mapped/TYG_Salts_Solution.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:tyg_salts_solution` with the same
  `ontology_mapping.ontology_id`, label `TYG salts solution`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`, and
  `mapping_status: MAPPED`.
- Ingredient type: `STOCK_SOLUTION`.
- Occurrences: 2 CultureMech recipe occurrences across 2 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `TYGVS_Glucose` through `Takara_DO_Supp_MinusHisLeuTrp`: exited 0 and wrote
  zero ERROR rows.
- Direct old Engine A/OBO term validation was skipped for this local
  `kgmicrobe.ingredient` fallback row because that prefix is intentionally
  outside the CHEBI-focused OBO term subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 search for `TYG salts solution` returned zero results, and
  fresh PubChem name lookup found no CID.
- The final SSSOM has exactly one exact registry row for
  `MIM:TYG_Salts_Solution`, points at
  `kgmicrobe.ingredient:tyg_salts_solution`, names `kgm:ingredient`, and
  publishes no unsafe `other` synonyms.
- Major: the record classifies the ingredient as a stock solution but has no
  `components` list and no `component_assertion` explaining a bounded,
  evidence-backed composition.

## Completeness

- The local fallback identity, aggregate row, occurrence count, and final SSSOM
  row agree mechanically.
- The missing component-level representation is still consequential because the
  record is a named multi-component CultureBotHT stock solution rather than an
  indivisible ontology class or an explicitly undefined medium component.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected local fallback, aggregate,
  final SSSOM, and generated rows but no maintained decomposition for this
  stock solution.

## Recommended Edits

- Major: curate the TYG salts solution formula in
  `data/ingredients/mapped/TYG_Salts_Solution.yaml`, adding a supported
  `components` list and a `component_assertion` or recording an explicit
  unresolved-composition decision if the component amounts cannot be recovered.
- Major: regenerate generated component and product artifacts after the
  per-record YAML gains a component-level representation.
