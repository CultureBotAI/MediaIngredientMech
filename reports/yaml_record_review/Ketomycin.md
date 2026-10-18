# `data/ingredients/mapped/Ketomycin.yaml`

## Verdict

Needs curation. The exact MeSH ketomycin identity and final SSSOM row are
internally consistent, but `SELECTIVE_AGENT` is only provisional name-pattern
evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/Ketomycin.yaml`.
- Identifier and grounding: `identifier: mesh:C008231` with
  `ontology_mapping.ontology_id: mesh:C008231`, label `ketomycin`, source
  `MESH`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: intentionally absent; the record is grounded to MeSH
  rather than a structure-bearing ChEBI or CAS term.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Kcl.yaml data/ingredients/mapped/Keratin.yaml data/ingredients/mapped/Ketomycin.yaml data/ingredients/mapped/Kf.yaml data/ingredients/mapped/Kh2po4.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2245`:
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2245`:
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- EBI OLS4 resolves `mesh:C008231` as active MeSH term `ketomycin`, matching the
  YAML identifier and ontology mapping.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Ketomycin` to
  `mesh:C008231` with no `other` synonyms.
- The `UNKNOWN_TERM` OAK/OLS row is already triaged as
  `missing_prefix_validator_coverage_issue`; the prefix-specific EBI OLS row
  resolves the exact MeSH CURIE and label.
- Major: `physicochemical_roles.SELECTIVE_AGENT` has only
  `COMPUTATIONAL_PREDICTION` evidence from a curated name-pattern rule, with no
  inspected kg-microbe, CultureMech, FEBA, Hans80, or literature evidence
  attached to the claim.
- The hidden and ignored-inclusive search over `data/ingredients`, `mappings`,
  `reports/kg_microbe_node_id_mismatches.tsv`, `reports/hydrate_grounding.tsv`,
  `docs/data`, `src`, `tests`, `conf`, and `.claude` found the current YAML,
  final SSSOM row, docs projections, unknown-term triage row, and row-review
  disposition; it found no hits in `reports/kg_microbe_node_id_mismatches.tsv`,
  `reports/hydrate_grounding.tsv`, or `mappings/needs_curator_review.tsv`.

## Completeness

- The active MeSH identifier, aggregate copy, empty occurrence count, and final
  SSSOM row are present and consistent.
- The record is incomplete until the selective-agent role is either supported by
  inspected claim-level evidence or removed.

## Recommended Edits

- Major: remove `physicochemical_roles.SELECTIVE_AGENT` unless an inspected
  kg-microbe, CultureMech, FEBA, Hans80, or literature source can support
  ketomycin as a selective agent, then rerun strict, term, round-trip,
  component, and SSSOM validation.
