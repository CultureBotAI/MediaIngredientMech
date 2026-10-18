# `data/ingredients/mapped/Kanchanomycin.yaml`

## Verdict

Needs curation. The label-exact MeSH upgrade now resolves to active
`mesh:C001493` and the final SSSOM row is internally consistent, but
`SELECTIVE_AGENT` is only provisional name-pattern evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/Kanchanomycin.yaml`.
- Identifier and grounding: `identifier: mesh:C001493` with
  `ontology_mapping.ontology_id: mesh:C001493`, label `kanchanomycin`, source
  `MESH`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: intentionally absent; the record is grounded to MeSH
  rather than a structure-bearing ChEBI or CAS term.

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

- OLS4 resolves `http://id.nlm.nih.gov/mesh/C001493` as active
  `mesh:C001493` with label `kanchanomycin`, matching the YAML identifier and
  ontology mapping.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Kanchanomycin`
  to `mesh:C001493` with no `other` synonyms.
- The `UNKNOWN_TERM` OAK/OLS row is already triaged as
  `missing_prefix_validator_coverage_issue`; the prefix-specific EBI OLS row
  resolves the exact MeSH CURIE and label.
- Major: `physicochemical_roles.SELECTIVE_AGENT` has only
  `COMPUTATIONAL_PREDICTION` evidence from a curated name-pattern rule, with no
  inspected CultureMech, FEBA, Hans80, or literature evidence attached to the
  claim.
- The hidden and ignored-inclusive search over `data/ingredients`, `mappings`,
  `reports/kg_microbe_node_id_mismatches.tsv`, `reports/hydrate_grounding.tsv`,
  `docs/data`, `src`, `tests`, `conf`, and `.claude` found the current
  per-record YAML, final SSSOM row, docs projections, external-prefix
  validation row, unknown-term triage row, and row-review disposition.

## Completeness

- The active MeSH identifier, aggregate copy, empty occurrence count, and final
  SSSOM row are present and consistent.
- The record is incomplete until the selective-agent role is either supported by
  inspected claim-level evidence or removed.

## Recommended Edits

- Major: remove `physicochemical_roles.SELECTIVE_AGENT` unless an inspected
  CultureMech, FEBA, Hans80, or literature source can support kanchanomycin as a
  selective agent, then rerun strict, term, round-trip, component, and SSSOM
  validation.
