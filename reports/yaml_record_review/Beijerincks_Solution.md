# `data/ingredients/mapped/Beijerincks_Solution.yaml`

## Verdict

Needs curation, major. The kg-microbe fallback registry identity and SSSOM row
are correct for a named stock solution with no external ontology term, but the
record still has no component list for a curated `STOCK_SOLUTION`.

## Identity

- Reviewed record: `data/ingredients/mapped/Beijerincks_Solution.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.ingredient:beijerincks_solution` with
  `ontology_mapping.ontology_id: kgmicrobe.ingredient:beijerincks_solution`,
  `ontology_label: Beijerinck's Solution`,
  `ontology_source: kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- Exact OLS search over labels and synonyms returned no term for
  `Beijerinck's Solution`; hidden/ignored-inclusive local search found the
  earlier `UNMAPPED_0085` audit row with `NO_EXACT_OLS_HIT`.
- The record denotes a lab stock/pre-mix solution, not a single chemical.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Beef_Heart.yaml data/ingredients/mapped/Beef_Heart_Infusion.yaml data/ingredients/mapped/Beijerincks_Solution.yaml data/ingredients/mapped/Benzaldehyde.yaml data/ingredients/mapped/Benzalkonium_Chloride.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- Engine A term validation was intentionally skipped for this record because
  `kgmicrobe.ingredient` is a registry prefix, not an OBO ontology adapter. The
  local SSSOM row is an own-identifier registry exact match.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports/kg_microbe_node_id_mismatches.tsv`, excluding
  `data/curated/backups`, found the authoritative registry SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 550 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- The 2026-05-11 review classified the record as a named stock/pre-mix
  solution and explicitly left component-level recipe curation pending.
- The 2026-08-06 promotion moved the local fallback registry identity to
  `MAPPED` and added the SSSOM row, without claiming any single-compound or
  broader ontology parent.

## Completeness

- The kg-microbe registry identity, raw source synonym, fallback evidence,
  SSSOM row, and aggregate copy are populated.
- The `components` and `component_assertion` slots are still absent even though
  `ingredient_type: STOCK_SOLUTION` and the review note identify this as a
  multi-component preparation pending component-level curation.

## Recommended Edits

- Major: curate the component recipe for
  `data/ingredients/mapped/Beijerincks_Solution.yaml` from the maintained
  CultureMech source occurrence if it contains the formulation; populate
  `components` with a matching `component_assertion`, then run
  `just sync-curated` and `just qc-component-partonomy`.
