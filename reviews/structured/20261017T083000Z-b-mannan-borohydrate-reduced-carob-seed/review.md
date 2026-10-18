# Per-record structured review: B-Mannan_Borohydrate_Reduced_Carob_Seed (data/ingredients/mapped/B-Mannan_Borohydrate_Reduced_Carob_Seed.yaml)

- Review: 20261017T083000Z-b-mannan-borohydrate-reduced-carob-seed
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for B-Mannan_Borohydrate_Reduced_Carob_Seed (data/ingredients/mapped/B-Mannan_Borohydrate_Reduced_Carob_Seed.yaml, record-99ff921fd495a24c, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/B-Mannan_Borohydrate_Reduced_Carob_Seed.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/B-Mannan_Borohydrate_Reduced_Carob_Seed.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-99ff921fd495a24c | data/ingredients/mapped/B-Mannan_Borohydrate_Reduced_Carob_Seed.yaml | maintained | B-Mannan_Borohydrate_Reduced_Carob_Seed |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-99ff921fd495a24c | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-99ff921fd495a24c | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-99ff921fd495a24c | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-99ff921fd495a24c.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-99ff921fd495a24c.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T09:12:21Z; reviewed SHA-256=5fac547527ee432196f47f58cb33131108624b43449be8346f8ad37514965499; current SHA-256=5fac547527ee432196f47f58cb33131108624b43449be8346f8ad37514965499; hash_changed=False. Reports=["reports/yaml_record_review/B-Mannan_Borohydrate_Reduced_Carob_Seed.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS fallback identity passes, but pubchem_cid 870 and the stored structure describe amylotetraose rather than CAS 9036-88-8.

### Historical provisional-role concern

evidence: concern. Targets: record-99ff921fd495a24c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-75d6fcd57f3f8499: Reassess prediction-only role support: b-Mannan borohydrate reduced carob seed

major / open / confirmed; issue key: mim-reconciliation-role-support-99ff921fd495a24c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-75d6fcd57f3f8499

Reassess prediction-only role support: b-Mannan borohydrate reduced carob seed

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-76945188546e1e2d | data/ingredients/mapped/B-Mannan_Borohydrate_Reduced_Carob_Seed.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[540],"raw_equal":true},"docs_rows":[{"identifier":"cas:9036-88-8","line":542,"mapping_status":"MAPPED","ontology_id":"cas:9036-88-8","preferred_term":"b-Mannan borohydrate reduced carob seed"}],"identifier":"cas:9036-88-8","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:9036-88-8","ontology_label":"b-Mannan borohydrate reduced carob seed","ontology_source":"CAS"},"preferred_term":"b-Mannan borohydrate reduced carob seed","sssom_rows":[{"data_row":470,"object_id":"cas:9036-88-8","object_label":"b-Mannan borohydrate reduced carob seed","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:B-Mannan_Borohydrate_Reduced_Carob_Seed","synonym_count":0} |
| ev-a89eb0a02c96404e | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [540] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-b7f087d496277f56 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:B-Mannan_Borohydrate_Reduced_Carob_Seed; data-row positions=[470] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":470,"object_id":"cas:9036-88-8","object_label":"b-Mannan borohydrate reduced carob seed","other":"CAS:9036-88-8","predicate_id":"skos:exactMatch","subject_id":"MIM:B-Mannan_Borohydrate_Reduced_Carob_Seed","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-f13cf40d64a4860c | docs/data/mapped_ingredients.csv; CSV lines=[542] | supports | Published identity and count rows inspected: [{"identifier":"cas:9036-88-8","line":542,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"cas:9036-88-8","preferred_term":"b-Mannan borohydrate reduced carob seed","total_occurrences":"0"}] |
| ev-95e7e9d17041e8a7 | reports/yaml_record_review/B-Mannan_Borohydrate_Reduced_Carob_Seed.md; &#96;data/ingredients/mapped/B-Mannan_Borohydrate_Reduced_Carob_Seed.yaml&#96;:2; Verdict:4; Identity:11; Validation:28; Evidence:44; Completeness:59; Recommended Edits:68 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-5b6b44570a132188 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[288,1947] | context_only | [{"current_record_sha256":"5fac547527ee432196f47f58cb33131108624b43449be8346f8ad37514965499","finding_id":"SEM:910f76feca50c487fd60","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"5fac547527ee432196f47f58cb33131108624b43449be8346f8ad37514965499","finding_id":"SEM:2164db6e72e159c5e665","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-a383801d6c52c39e | data/ingredients/mapped/B-Mannan_Borohydrate_Reduced_Carob_Seed.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[540],"raw_equal":true},"docs_rows":[{"identifier":"cas:9036-88-8","line":542,"mapping_status":"MAPPED","ontology_id":"cas:9036-88-8","preferred_term":"b-Mannan borohydrate reduced carob seed"}],"identifier":"cas:9036-88-8","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:9036-88-8","ontology_label":"b-Mannan borohydrate reduced carob seed","ontology_source":"CAS"},"preferred_term":"b-Mannan borohydrate reduced carob seed","sssom_rows":[{"data_row":470,"object_id":"cas:9036-88-8","object_label":"b-Mannan borohydrate reduced carob seed","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:B-Mannan_Borohydrate_Reduced_Carob_Seed","synonym_count":0} |
| ev-13addc779c4fd350 | reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml; findings[finding_id=f-75d6fcd57f3f8499] | context_only | Predecessor structured review finding f-75d6fcd57f3f8499 in 20261011T024631Z-mim-reconcile-all-batch-03 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-b-mannan-borohydrate-reduced-carob-seed
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: B-Mannan_Borohydrate_Reduced_Carob_Seed (data/ingredients/mapped/B-Mannan_Borohydrate_Reduced_Carob_Seed.yaml)'
started_at: '2026-10-17T08:25:00Z'
finished_at: '2026-10-17T08:30:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Independent per-record structured review and reconciliation
    against current HEAD and historical review inputs.
skill: review-yaml-record
completion: partial
verdict: needs_curation
native_verdict: mapping_status=MAPPED; open=1; deferred=0
scientific_review: false
summary: Per-record structured review for B-Mannan_Borohydrate_Reduced_Carob_Seed
  (data/ingredients/mapped/B-Mannan_Borohydrate_Reduced_Carob_Seed.yaml, record-99ff921fd495a24c,
  mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound
  to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/B-Mannan_Borohydrate_Reduced_Carob_Seed.yaml
    sha256: 5fac547527ee432196f47f58cb33131108624b43449be8346f8ad37514965499
    role: target
  - path: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
    sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
    role: context
  - path: data/curated/mapped_ingredients.yaml
    sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
    role: context
  - path: mappings/ingredient_mappings.sssom.tsv
    sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
    role: context
  - path: docs/data/mapped_ingredients.csv
    sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
    role: context
  - path: reports/yaml_record_review/B-Mannan_Borohydrate_Reduced_Carob_Seed.md
    sha256: 630d6739d18c5bde2bf16f7d6b3a56a932ca29e24768c5bea5e7e28bdec42600
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-99ff921fd495a24c
  path: data/ingredients/mapped/B-Mannan_Borohydrate_Reduced_Carob_Seed.yaml
  label: B-Mannan_Borohydrate_Reduced_Carob_Seed
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/B-Mannan_Borohydrate_Reduced_Carob_Seed.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/B-Mannan_Borohydrate_Reduced_Carob_Seed.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/B-Mannan_Borohydrate_Reduced_Carob_Seed.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-99ff921fd495a24c
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-99ff921fd495a24c
  evidence_ids:
  - ev-76945188546e1e2d
  - ev-a89eb0a02c96404e
  - ev-b7f087d496277f56
  - ev-f13cf40d64a4860c
  - ev-a383801d6c52c39e
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-99ff921fd495a24c
  evidence_ids:
  - ev-76945188546e1e2d
  - ev-5b6b44570a132188
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-99ff921fd495a24c
  evidence_ids:
  - ev-95e7e9d17041e8a7
  - ev-5b6b44570a132188
  - ev-13addc779c4fd350
evidence:
- evidence_id: ev-76945188546e1e2d
  kind: record_content
  reference: data/ingredients/mapped/B-Mannan_Borohydrate_Reduced_Carob_Seed.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[540],"raw_equal":true},"docs_rows":[{"identifier":"cas:9036-88-8","line":542,"mapping_status":"MAPPED","ontology_id":"cas:9036-88-8","preferred_term":"b-Mannan
    borohydrate reduced carob seed"}],"identifier":"cas:9036-88-8","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:9036-88-8","ontology_label":"b-Mannan
    borohydrate reduced carob seed","ontology_source":"CAS"},"preferred_term":"b-Mannan
    borohydrate reduced carob seed","sssom_rows":[{"data_row":470,"object_id":"cas:9036-88-8","object_label":"b-Mannan
    borohydrate reduced carob seed","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:B-Mannan_Borohydrate_Reduced_Carob_Seed","synonym_count":0}'
  snapshot_sha256: 5fac547527ee432196f47f58cb33131108624b43449be8346f8ad37514965499
- evidence_id: ev-a89eb0a02c96404e
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [540]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-b7f087d496277f56
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:B-Mannan_Borohydrate_Reduced_Carob_Seed; data-row positions=[470]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":470,"object_id":"cas:9036-88-8","object_label":"b-Mannan
    borohydrate reduced carob seed","other":"CAS:9036-88-8","predicate_id":"skos:exactMatch","subject_id":"MIM:B-Mannan_Borohydrate_Reduced_Carob_Seed","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-f13cf40d64a4860c
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[542]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:9036-88-8","line":542,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"cas:9036-88-8","preferred_term":"b-Mannan
    borohydrate reduced carob seed","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-95e7e9d17041e8a7
  kind: prior_review
  reference: reports/yaml_record_review/B-Mannan_Borohydrate_Reduced_Carob_Seed.md
  locator: '`data/ingredients/mapped/B-Mannan_Borohydrate_Reduced_Carob_Seed.yaml`:2;
    Verdict:4; Identity:11; Validation:28; Evidence:44; Completeness:59; Recommended
    Edits:68'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 630d6739d18c5bde2bf16f7d6b3a56a932ca29e24768c5bea5e7e28bdec42600
  quote: "Recommended Edits:\n- Re-curate `data/ingredients/mapped/B-Mannan_Borohydrate_Reduced_Carob_Seed.yaml`\n\
    \  from CAS `9036-88-8`: at minimum remove `pubchem_cid: 870` and its derived\n\
    \  InChI/SMILES fields, then add replacement PubChem fields only if the\n  CAS-resolved\
    \ compound is verified to represent the exact\n  borohydrate-reduced carob seed\
    \ mannan identity.\n- Synchronize `data/curated/mapped_ingredients.yaml` and rerun\
    \ focused strict\n  validation, SSSOM invariants, product id/label correspondence,\
    \ duplicate-ID\n  baseline audit, and flat-export coverage."
- evidence_id: ev-5b6b44570a132188
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[288,1947]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"5fac547527ee432196f47f58cb33131108624b43449be8346f8ad37514965499","finding_id":"SEM:910f76feca50c487fd60","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"5fac547527ee432196f47f58cb33131108624b43449be8346f8ad37514965499","finding_id":"SEM:2164db6e72e159c5e665","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-a383801d6c52c39e
  kind: record_content
  reference: data/ingredients/mapped/B-Mannan_Borohydrate_Reduced_Carob_Seed.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[540],"raw_equal":true},"docs_rows":[{"identifier":"cas:9036-88-8","line":542,"mapping_status":"MAPPED","ontology_id":"cas:9036-88-8","preferred_term":"b-Mannan
    borohydrate reduced carob seed"}],"identifier":"cas:9036-88-8","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:9036-88-8","ontology_label":"b-Mannan
    borohydrate reduced carob seed","ontology_source":"CAS"},"preferred_term":"b-Mannan
    borohydrate reduced carob seed","sssom_rows":[{"data_row":470,"object_id":"cas:9036-88-8","object_label":"b-Mannan
    borohydrate reduced carob seed","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:B-Mannan_Borohydrate_Reduced_Carob_Seed","synonym_count":0}'
  snapshot_sha256: 5fac547527ee432196f47f58cb33131108624b43449be8346f8ad37514965499
- evidence_id: ev-13addc779c4fd350
  kind: prior_review
  reference: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
  locator: findings[finding_id=f-75d6fcd57f3f8499]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-75d6fcd57f3f8499 in 20261011T024631Z-mim-reconcile-all-batch-03
  snapshot_sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
assessments:
- assessment_id: a-b6cf76d29f06b57a
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-99ff921fd495a24c
  evidence_ids:
  - ev-76945188546e1e2d
  - ev-a89eb0a02c96404e
  - ev-b7f087d496277f56
  - ev-f13cf40d64a4860c
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-e785216193aca84a
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-99ff921fd495a24c
  evidence_ids:
  - ev-95e7e9d17041e8a7
  - ev-76945188546e1e2d
  - ev-5b6b44570a132188
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T09:12:21Z;
    reviewed SHA-256=5fac547527ee432196f47f58cb33131108624b43449be8346f8ad37514965499;
    current SHA-256=5fac547527ee432196f47f58cb33131108624b43449be8346f8ad37514965499;
    hash_changed=False. Reports=["reports/yaml_record_review/B-Mannan_Borohydrate_Reduced_Carob_Seed.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS
    fallback identity passes, but pubchem_cid 870 and the stored structure describe
    amylotetraose rather than CAS 9036-88-8.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-95e7e9d17041e8a7
    - ev-76945188546e1e2d
  - name: legacy-native-ids
    value: '["SEM:910f76feca50c487fd60","SEM:2164db6e72e159c5e665"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-76945188546e1e2d
    - ev-95e7e9d17041e8a7
    - ev-5b6b44570a132188
- assessment_id: a-a383801d6c52c39e
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-99ff921fd495a24c
  evidence_ids:
  - ev-95e7e9d17041e8a7
  - ev-a383801d6c52c39e
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-95e7e9d17041e8a7
    - ev-a383801d6c52c39e
findings:
- finding_id: rec-f-75d6fcd57f3f8499
  issue_key: mim-reconciliation-role-support-99ff921fd495a24c
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: b-Mannan borohydrate reduced carob
    seed'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-99ff921fd495a24c
  evidence_ids:
  - ev-95e7e9d17041e8a7
  - ev-a383801d6c52c39e
  - ev-13addc779c4fd350
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/B-Mannan_Borohydrate_Reduced_Carob_Seed.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024631Z-mim-reconcile-all-batch-03
    finding_id: f-75d6fcd57f3f8499
actions:
- action_id: rec-action-75d6fcd57f3f8499
  description: 'Reassess prediction-only role support: b-Mannan borohydrate reduced
    carob seed'
  finding_ids:
  - rec-f-75d6fcd57f3f8499
  target_ids:
  - record-99ff921fd495a24c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/B-Mannan_Borohydrate_Reduced_Carob_Seed.yaml
    role: maintained ingredient
  acceptance_checks:
  - Address the exact fields/tokens and evidence gap described in this finding; preserve
    unrelated source labels and audit history.
  - Inspect the original preparation, organism, or mapping evidence where needed;
    do not promote a label/name-pattern inference to proof.
  - For an authorized fix, synchronize maintained surfaces, run focused validation,
    and save an evidence-backed successor citing this finding.
limitations:
- 'Read-only per-record structured review (scientific_review: false); no ingredient
  YAML, curated aggregate, or SSSOM files were modified.'
- Confirmed local evidence gaps and structural issues are recorded as open with bounded
  remediation actions; historical or source-context claims requiring primary recipe/literature
  verification remain deferred (provisional).
tags:
- record-review
- per-record
- reconciliation
- bundle-by-owner
notes:
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb)
  with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.
```
