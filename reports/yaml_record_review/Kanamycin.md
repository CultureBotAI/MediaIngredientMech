# `data/ingredients/mapped/Kanamycin.yaml`

## Verdict

Needs curation. The CultureBotHT exact ChEBI kanamycin mapping and occurrence
count pass, but the final SSSOM exports a conditional recipe note as a synonym
and `SELECTIVE_AGENT` is only provisional name-pattern evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/Kanamycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:6104` with
  `ontology_mapping.ontology_id: CHEBI:6104`, label `kanamycin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: intentionally empty; the imported CultureBotHT record
  had no CAS RN and no structure block was backfilled for `CHEBI:6104`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/K2so4_X_7_H2o.yaml data/ingredients/mapped/KH2PO3.yaml data/ingredients/mapped/Kanamycin.yaml data/ingredients/mapped/Kanamycin_Sulfate.yaml data/ingredients/mapped/Kanchanomycin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2150`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2150`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:6104` as the active ChEBI class `kanamycin`, with the
  same canonical label as the YAML ontology mapping and the preferred term as a
  related synonym.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Kanamycin` to
  `CHEBI:6104`.
- Major: the final SSSOM and docs label index export `kanamycin (if needed)` as
  a resolving synonym. The parenthetical `if needed` suffix is recipe usage
  context, not a true same-substance label for kanamycin.
- Major: `physicochemical_roles.SELECTIVE_AGENT` has only
  `COMPUTATIONAL_PREDICTION` evidence from a curated name-pattern rule, with no
  inspected CultureMech, FEBA, Hans80, or literature evidence attached to the
  claim.
- The hidden and ignored-inclusive search over `data/ingredients`, `mappings`,
  `reports/kg_microbe_node_id_mismatches.tsv`, `reports/hydrate_grounding.tsv`,
  `docs/data`, `src`, `tests`, `conf`, and `.claude` found the current
  per-record YAML, final SSSOM row, docs projections, CultureMech residual
  triage for the conditional label, and five current CultureMech membership
  rows.

## Completeness

- The active ChEBI identifier, aggregate copy, occurrence count, and final SSSOM
  identity row are present and consistent.
- The record is incomplete until the conditional usage note stops resolving as
  a synonym and the selective-agent role is either supported by inspected
  claim-level evidence or removed.

## Recommended Edits

- Major: remove or retype `kanamycin (if needed)` in
  `data/ingredients/mapped/Kanamycin.yaml` so final SSSOM and docs label
  surfaces no longer expose it as a synonym.
- Major: remove `physicochemical_roles.SELECTIVE_AGENT` unless an inspected
  CultureMech, FEBA, Hans80, or literature source can support kanamycin as a
  selective agent, then rerun strict, term, round-trip, id-label, component, and
  SSSOM validation.
