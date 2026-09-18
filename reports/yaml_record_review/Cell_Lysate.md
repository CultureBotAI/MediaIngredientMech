# `data/ingredients/mapped/Cell_Lysate.yaml`

## Verdict

Needs curation; major issue. `Cell lysate` is exactly grounded to active
`BTO:0004304`, its two CultureMech memberships match `occurrence_statistics`,
and its SSSOM row and aggregate copy agree. The remaining `PROTEIN_SOURCE` role
is supported only by a provisional name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Cell_Lysate.yaml`.
- Identifier and grounding: `identifier: BTO:0004304`,
  `ontology_mapping.ontology_id: BTO:0004304`,
  `ontology_label: cell lysate`, `ontology_source: BTO`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Direct prefix-specific OLS lookup for `BTO:0004304` returns one active BTO
  term labelled `cell lysate`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cefuroxime.yaml data/ingredients/mapped/Cefuroxime_Sodium.yaml data/ingredients/mapped/Celesticetin.yaml data/ingredients/mapped/Cell_Lysate.yaml data/ingredients/mapped/Cellobiose.yaml`:
  passed.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cefuroxime.yaml data/ingredients/mapped/Cefuroxime_Sodium.yaml data/ingredients/mapped/Celesticetin.yaml data/ingredients/mapped/Cell_Lysate.yaml data/ingredients/mapped/Cellobiose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 external-ontology records in this batch.
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
  backups, found the active exact `MIM:Cell_Lysate` SSSOM row, the
  prefix-specific `RESOLVED_EXACT_CURIE` BTO validation row, the
  `missing_prefix_validator_coverage_issue` row-review disposition, and
  matching aggregate/docs rows for `BTO:0004304`.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` marks the earlier
  `UNKNOWN_TERM` row as a synonym-review dispatcher gap, not a mapping defect:
  prefix-specific EBI OLS resolves the exact BTO CURIE.
- `reports/yaml_record_review_batch/validation_report.md` still says
  `BTO:0004304` does not exist, but that advisory batch report is stale for the
  same prefix-coverage reason.
- `mappings/culturemech_recipe_membership.tsv` contains two `BTO:0004304`
  memberships with two total occurrences, matching `occurrence_statistics`.
- `PROTEIN_SOURCE` has only `COMPUTATIONAL_PREDICTION` evidence from
  `infer_roles_from_name_lists` and is explicitly marked "Provisional role from
  a curated name-pattern rule; review recommended."

## Completeness

- The BTO identifier, source raw label, exact SSSOM row, aggregate copy, docs
  row, and 2/2 CultureMech occurrence count are populated and agree.
- No chemical structure fields are expected for a biological lysate material.

## Recommended Edits

- Major: either replace `nutritional_roles.PROTEIN_SOURCE` with inspected
  evidence for cell lysate as a protein source in media, or remove the role,
  then rerun strict validation, SSSOM QC, aggregate roundtrip, and
  `git diff --check`.
