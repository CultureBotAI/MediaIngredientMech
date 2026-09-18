# `data/ingredients/mapped/Hitachimycin.yaml`

## Verdict

Needs curation. OLS resolves the MeSH `stubomycin` term with exact synonym
`hitachimycin`, but `SELECTIVE_AGENT` is still only a provisional name-pattern
assignment.

## Identity

- Reviewed record: `data/ingredients/mapped/Hitachimycin.yaml`.
- Identifier and grounding: `identifier: mesh:C031780` with
  `ontology_mapping.ontology_id: mesh:C031780`, label `stubomycin`, source
  `MESH`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Role: `physicochemical_roles.SELECTIVE_AGENT`, with only provisional
  `COMPUTATIONAL_PREDICTION` evidence.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hexanoate.yaml data/ingredients/mapped/Hexanol.yaml data/ingredients/mapped/Hippuric_Acid.yaml data/ingredients/mapped/Histamine.yaml data/ingredients/mapped/Hitachimycin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation was run for the four CHEBI records in this
  batch and skipped for `Hitachimycin` because its exact target is a lowercase
  `mesh:` registry CURIE outside the CHEBI/OBO adapter subset.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1428`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1428`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `mesh:C031780` as active `stubomycin`, with `hitachimycin` as
  a synonym.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Hitachimycin`
  to `mesh:C031780` and exports no `other` synonym noise.
- The row-review manifest already records the earlier
  `kgmicrobe.compound:hitachimycin` `UNKNOWN_TERM` as a
  `missing_prefix_validator_coverage_issue`; the current YAML no longer points
  at that local placeholder.
- Major: `physicochemical_roles.SELECTIVE_AGENT` has only
  `COMPUTATIONAL_PREDICTION` evidence from a curated name-pattern rule, with no
  inspected media occurrence or literature evidence that supports selective
  agent use.

## Completeness

- The active MeSH identifier and final SSSOM row are present and consistent.
- The record is incomplete until the selective-agent role is either supported
  by claim-level evidence or removed.

## Recommended Edits

- Major: remove `physicochemical_roles.SELECTIVE_AGENT` unless an inspected
  CultureMech source row or literature source can support hitachimycin as a
  selective agent, then rerun strict, round-trip, component, id-label, and
  SSSOM validation.
