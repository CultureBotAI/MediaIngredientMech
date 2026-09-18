# `data/ingredients/mapped/Chelated_Iron_Solution.yaml`

## Verdict

Needs curation; major issue. The local fallback registry identity and SSSOM row
are correct for this named chelated iron stock solution with no external exact
ontology term, but the record still has no component list for a curated
`STOCK_SOLUTION`.

## Identity

- Reviewed record: `data/ingredients/mapped/Chelated_Iron_Solution.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:chelated_iron_solution`,
  `ontology_mapping.ontology_id:
  kgmicrobe.ingredient:chelated_iron_solution`,
  `ontology_label: Chelated Iron Solution`,
  `ontology_source: kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`,
  `ingredient_type: STOCK_SOLUTION`, and `solution_type: OTHER`.
- Current exact OLS search for `Chelated Iron Solution` across CHEBI, NCIT,
  MeSH, FOODON, and ENVO returns no results, preserving the premise that this
  named lab preparation needs a local registry identity rather than an external
  ontology exact match.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Chaninin.yaml data/ingredients/mapped/Charcoal.yaml data/ingredients/mapped/Chartreusin.yaml data/ingredients/mapped/Chaulmoogric_Acid.yaml data/ingredients/mapped/Chelated_Iron_Solution.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data ... -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for `Charcoal`, `Chartreusin`, and `Chaulmoogric_Acid`. Engine A term
  validation was intentionally skipped for `Chelated_Iron_Solution` because
  `kgmicrobe.ingredient` is a local registry prefix, not an OBO ontology
  adapter.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active exact `MIM:Chelated_Iron_Solution` SSSOM row, the
  mapped aggregate copy, matching docs rows, the previous no-exact-OLS audit
  row for `UNMAPPED_0095`, and the raw `CultureMech:000025` occurrence in
  `UNIFIED_INGREDIENT_MAPPING.tsv`.
- The 2026-05-11 review classified the record as a named chelated iron stock
  solution and explicitly left component-level recipe curation pending.
- The 2026-08-06 promotion moved the local fallback registry identity to
  `MAPPED` and added the SSSOM row, without claiming any single-compound or
  broader ontology parent.
- `reports/yaml_record_review_batch/validation_report.md` still says
  `kgmicrobe.ingredient:chelated_iron_solution` is invalid and does not exist,
  but that advisory batch report is stale: this is the intentionally minted
  local registry identifier for the promoted fallback record.

## Completeness

- The kg-microbe registry identity, raw CultureMech synonym, fallback evidence,
  SSSOM row, occurrence count, and aggregate copy are populated.
- The `components` and `component_assertion` slots are still absent even though
  `ingredient_type: STOCK_SOLUTION` and the review note identify this as a
  multi-component preparation pending component-level curation.

## Recommended Edits

- Major: curate the component recipe for
  `data/ingredients/mapped/Chelated_Iron_Solution.yaml` from the maintained
  `CultureMech:000025` source occurrence if it contains the formulation;
  populate `components` with a matching `component_assertion`, then run
  `just sync-curated` and `just qc-component-partonomy`.
