# `data/ingredients/mapped/Cladomycin.yaml`

## Verdict

Needs curation; major. `Cladomycin` is intentionally retained as the local
`kgmicrobe.compound:cladomycin` placeholder while no exact external ontology
identity is available, and the placeholder record, SSSOM row, zero occurrence
count, aggregate copy, and no-hit review artifacts agree. The only material gap
is that `SELECTIVE_AGENT` is supported solely by a provisional name-pattern
prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Cladomycin.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:cladomycin`,
  `ontology_mapping.ontology_id: kgmicrobe.compound:cladomycin`,
  `ontology_label: Cladomycin`, `ontology_source: kgmicrobe.compound`,
  `mapping_quality: PLACEHOLDER`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Current exact OLS search for `Cladomycin` in CHEBI and NCIT returns no
  results. That agrees with the prior hidden/ignored-inclusive review artifact
  saying the 2026-05-06 search across CHEBI, MeSH, NCIT, MICRO, BTO, and FOODON
  found no exact label or synonym candidate.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Citric_Acid_X_H2o.yaml data/ingredients/mapped/Citric_Acidh2o.yaml data/ingredients/mapped/Cl.yaml data/ingredients/mapped/Cladomycin.yaml data/ingredients/mapped/Clarified_rumen_fluid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Citric_Acid_X_H2o.yaml data/ingredients/mapped/Citric_Acidh2o.yaml data/ingredients/mapped/Cl.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-scoped records in this batch. `Cladomycin` was
  intentionally skipped because `kgmicrobe.compound:cladomycin` is a local
  registry CURIE outside Engine A's OAK/OLS prefix scope.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only the expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active exact `MIM:Cladomycin` SSSOM row, the
  `expected_registry_identifier` unknown-term triage row, the
  `NO_EXACT_CANDIDATE` OLS-candidate review, and matching aggregate/docs rows
  for `kgmicrobe.compound:cladomycin`.
- `reports/yaml_record_review_batch` still flags
  `kgmicrobe.compound:cladomycin` as invalid and nonexistent, but those
  advisory rows are stale relative to the active row review explicitly keeping
  this local registry identifier pending exact external promotion.
- Hidden/ignored-inclusive exact search of
  `mappings/culturemech_recipe_membership.tsv` found no
  `kgmicrobe.compound:cladomycin` rows, matching the explicit 0/0
  `occurrence_statistics`.
- `SELECTIVE_AGENT` has only `COMPUTATIONAL_PREDICTION` evidence from
  `infer_roles_from_name_lists` and is explicitly marked "Provisional role from
  a curated name-pattern rule; review recommended."

## Completeness

- The local kg-microbe placeholder identifier, no-hit review note, exact local
  SSSOM row, aggregate copy, docs row, and zero occurrence count are populated
  and agree.
- The record has no synonym, component, chemical property, or environment
  claims that need additional evidence.
- The only consequential gap is the unsupported provisional role.

## Recommended Edits

- Major: in `data/ingredients/mapped/Cladomycin.yaml`, either replace
  `physicochemical_roles.SELECTIVE_AGENT` with inspected evidence for
  Cladomycin as a selective agent in this media scope, or remove the role.
- Regenerate synchronized products and rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
