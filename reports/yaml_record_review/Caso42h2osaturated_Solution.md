# `data/ingredients/mapped/Caso42h2osaturated_Solution.yaml`

## Verdict

Needs curation; major issue. The local stock-solution fallback identity is
intentional after no-hit OLS review, but `occurrence_statistics` still says
`1/1` while the current recipe-membership table has no row for this local
identifier.

## Identity

- Reviewed record: `data/ingredients/mapped/Caso42h2osaturated_Solution.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:caso42h2osaturated_solution`,
  `ontology_mapping.ontology_id: kgmicrobe.ingredient:caso42h2osaturated_solution`,
  `ontology_source: kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`,
  `ingredient_type: STOCK_SOLUTION`, and `solution_type: OTHER`.
- Exact OLS search for the calcium sulfate dihydrate saturated-solution label
  returned 0 hits, matching the #114 curation decision that the record denotes
  a stock solution, not neat gypsum dihydrate.
- The active SSSOM row uses `MIM:Caso42h2osaturated_Solution` and the
  `mappings/mim_curie_aliases.tsv` compatibility row preserves the older
  `MIM:CaSO42H2Osaturated_solution` spelling.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Caso42h2osaturated_Solution.yaml data/ingredients/mapped/Caso4_X_2_H2o.yaml data/ingredients/mapped/Caso4_X_7_H2o.yaml data/ingredients/mapped/Catalase.yaml data/ingredients/mapped/Cd_No32_X_4_H2o.yaml`:
  passed.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Caso4_X_2_H2o.yaml data/ingredients/mapped/Caso4_X_7_H2o.yaml data/ingredients/mapped/Catalase.yaml data/ingredients/mapped/Cd_No32_X_4_H2o.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 4 external-ontology records in this batch.
- Engine A label validation is unavailable for the local
  `kgmicrobe.ingredient` identifier because the local kgmicrobe OAK adapter has
  no `rdfs_label_statement` table.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding generated review reports and curated
  backups, found the active `MIM:Caso42h2osaturated_Solution` SSSOM row, the
  old/new MIM alias rows, the no-hit exact OLS audit, and matching
  aggregate/docs rows.
- The current `mappings/culturemech_recipe_membership.tsv` table has 0 rows
  for `kgmicrobe.ingredient:caso42h2osaturated_solution`, but the YAML,
  aggregate, and docs rows still publish `occurrence_statistics` `1/1`.

## Completeness

- The local identifier, stock-solution type, no-hit OLS audit, SSSOM row,
  aggregate copy, and docs row are populated.
- Components are absent; resolving the gypsum solute and water would require a
  separate stock-solution decomposition decision because the saturated label
  supplies no recipe concentration.

## Recommended Edits

- Major: inspect the current CultureMech occurrence source for this raw label
  and either backfill the missing membership edge to
  `kgmicrobe.ingredient:caso42h2osaturated_solution` or refresh the YAML
  `occurrence_statistics` to `0/0`, then rerun the strict, SSSOM, aggregate
  roundtrip, flat-coverage, and diff checks.
