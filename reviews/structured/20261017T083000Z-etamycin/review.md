# Per-record structured review: Etamycin (data/ingredients/mapped/Etamycin.yaml)

- Review: 20261017T083000Z-etamycin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Etamycin (data/ingredients/mapped/Etamycin.yaml, record-84a31a09d2209279, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Etamycin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Etamycin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-84a31a09d2209279 | data/ingredients/mapped/Etamycin.yaml | maintained | Etamycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-84a31a09d2209279 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-84a31a09d2209279 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-84a31a09d2209279 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-84a31a09d2209279.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-84a31a09d2209279.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T15:49:44Z; reviewed SHA-256=84d07722cb91d161afb8211b2a1cf76bfec8eaa9182b01d12c9e5f85648d8933; current SHA-256=84d07722cb91d161afb8211b2a1cf76bfec8eaa9182b01d12c9e5f85648d8933; hash_changed=False. Reports=["reports/yaml_record_review/Etamycin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The MeSH etamycin identity and Viridogrisein synonym pass, but SELECTIVE_AGENT is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-84a31a09d2209279.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-56a26af929b7324a: Reassess prediction-only role support: Etamycin

major / open / confirmed; issue key: mim-reconciliation-role-support-84a31a09d2209279.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-56a26af929b7324a

Reassess prediction-only role support: Etamycin

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-40d7bb5636e61d3f | data/ingredients/mapped/Etamycin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[951],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C004910","line":953,"mapping_status":"MAPPED","ontology_id":"mesh:C004910","preferred_term":"Etamycin"}],"identifier":"mesh:C004910","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C004910","ontology_label":"etamycin","ontology_source":"MESH"},"preferred_term":"Etamycin","sssom_rows":[{"data_row":1135,"object_id":"mesh:C004910","object_label":"etamycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Etamycin","synonym_count":1} |
| ev-c9c65686dce5b845 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [951] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-149069f11adbf93b | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Etamycin; data-row positions=[1135] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1135,"object_id":"mesh:C004910","object_label":"etamycin","other":"Viridogrisein","predicate_id":"skos:exactMatch","subject_id":"MIM:Etamycin","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-fb427e8273ac5bfa | docs/data/mapped_ingredients.csv; CSV lines=[953] | supports | Published identity and count rows inspected: [{"identifier":"mesh:C004910","line":953,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C004910","preferred_term":"Etamycin","total_occurrences":"0"}] |
| ev-bba8b78c11610a87 | reports/yaml_record_review/Etamycin.md; &#96;data/ingredients/mapped/Etamycin.yaml&#96;:2; Verdict:4; Identity:10; Validation:21; Evidence:28; Completeness:53; Recommended Edits:60 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-876019a77eb7ae88 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[571,1414] | context_only | [{"current_record_sha256":"84d07722cb91d161afb8211b2a1cf76bfec8eaa9182b01d12c9e5f85648d8933","finding_id":"SEM:c7ac253b2db2bd5b98a2","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"84d07722cb91d161afb8211b2a1cf76bfec8eaa9182b01d12c9e5f85648d8933","finding_id":"SEM:7be98705964a3304ea82","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-522c4e160bf8a245 | data/ingredients/mapped/Etamycin.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[951],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C004910","line":953,"mapping_status":"MAPPED","ontology_id":"mesh:C004910","preferred_term":"Etamycin"}],"identifier":"mesh:C004910","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C004910","ontology_label":"etamycin","ontology_source":"MESH"},"preferred_term":"Etamycin","sssom_rows":[{"data_row":1135,"object_id":"mesh:C004910","object_label":"etamycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Etamycin","synonym_count":1} |
| ev-85eaf51211ec7722 | reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml; findings[finding_id=f-56a26af929b7324a] | context_only | Predecessor structured review finding f-56a26af929b7324a in 20261011T024634Z-mim-reconcile-all-batch-06 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-etamycin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Etamycin (data/ingredients/mapped/Etamycin.yaml)'
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
summary: Per-record structured review for Etamycin (data/ingredients/mapped/Etamycin.yaml,
  record-84a31a09d2209279, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Etamycin.yaml
    sha256: 84d07722cb91d161afb8211b2a1cf76bfec8eaa9182b01d12c9e5f85648d8933
    role: target
  - path: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
    sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
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
  - path: reports/yaml_record_review/Etamycin.md
    sha256: 7490ca330b2038b44260df8605c934005e4ad4a97a39cc3c3610a9027812df79
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-84a31a09d2209279
  path: data/ingredients/mapped/Etamycin.yaml
  label: Etamycin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Etamycin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Etamycin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Etamycin.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-84a31a09d2209279
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-84a31a09d2209279
  evidence_ids:
  - ev-40d7bb5636e61d3f
  - ev-c9c65686dce5b845
  - ev-149069f11adbf93b
  - ev-fb427e8273ac5bfa
  - ev-522c4e160bf8a245
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-84a31a09d2209279
  evidence_ids:
  - ev-40d7bb5636e61d3f
  - ev-876019a77eb7ae88
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-84a31a09d2209279
  evidence_ids:
  - ev-bba8b78c11610a87
  - ev-876019a77eb7ae88
  - ev-85eaf51211ec7722
evidence:
- evidence_id: ev-40d7bb5636e61d3f
  kind: record_content
  reference: data/ingredients/mapped/Etamycin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[951],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C004910","line":953,"mapping_status":"MAPPED","ontology_id":"mesh:C004910","preferred_term":"Etamycin"}],"identifier":"mesh:C004910","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C004910","ontology_label":"etamycin","ontology_source":"MESH"},"preferred_term":"Etamycin","sssom_rows":[{"data_row":1135,"object_id":"mesh:C004910","object_label":"etamycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Etamycin","synonym_count":1}'
  snapshot_sha256: 84d07722cb91d161afb8211b2a1cf76bfec8eaa9182b01d12c9e5f85648d8933
- evidence_id: ev-c9c65686dce5b845
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [951]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-149069f11adbf93b
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Etamycin; data-row positions=[1135]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1135,"object_id":"mesh:C004910","object_label":"etamycin","other":"Viridogrisein","predicate_id":"skos:exactMatch","subject_id":"MIM:Etamycin","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-fb427e8273ac5bfa
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[953]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"mesh:C004910","line":953,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C004910","preferred_term":"Etamycin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-bba8b78c11610a87
  kind: prior_review
  reference: reports/yaml_record_review/Etamycin.md
  locator: '`data/ingredients/mapped/Etamycin.yaml`:2; Verdict:4; Identity:10; Validation:21;
    Evidence:28; Completeness:53; Recommended Edits:60'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 7490ca330b2038b44260df8605c934005e4ad4a97a39cc3c3610a9027812df79
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Etamycin.yaml`,\
    \ either replace the\n  computational `SELECTIVE_AGENT` evidence with direct,\
    \ source-backed role\n  evidence for etamycin, or remove the role facet; then\
    \ sync\n  `data/curated/mapped_ingredients.yaml` and rerun strict validation plus\
    \ the\n  final SSSOM gates."
- evidence_id: ev-876019a77eb7ae88
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[571,1414]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"84d07722cb91d161afb8211b2a1cf76bfec8eaa9182b01d12c9e5f85648d8933","finding_id":"SEM:c7ac253b2db2bd5b98a2","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"84d07722cb91d161afb8211b2a1cf76bfec8eaa9182b01d12c9e5f85648d8933","finding_id":"SEM:7be98705964a3304ea82","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-522c4e160bf8a245
  kind: record_content
  reference: data/ingredients/mapped/Etamycin.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[951],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C004910","line":953,"mapping_status":"MAPPED","ontology_id":"mesh:C004910","preferred_term":"Etamycin"}],"identifier":"mesh:C004910","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C004910","ontology_label":"etamycin","ontology_source":"MESH"},"preferred_term":"Etamycin","sssom_rows":[{"data_row":1135,"object_id":"mesh:C004910","object_label":"etamycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Etamycin","synonym_count":1}'
  snapshot_sha256: 84d07722cb91d161afb8211b2a1cf76bfec8eaa9182b01d12c9e5f85648d8933
- evidence_id: ev-85eaf51211ec7722
  kind: prior_review
  reference: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
  locator: findings[finding_id=f-56a26af929b7324a]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-56a26af929b7324a in 20261011T024634Z-mim-reconcile-all-batch-06
  snapshot_sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
assessments:
- assessment_id: a-9715e1c21ad43c9a
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-84a31a09d2209279
  evidence_ids:
  - ev-40d7bb5636e61d3f
  - ev-c9c65686dce5b845
  - ev-149069f11adbf93b
  - ev-fb427e8273ac5bfa
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-7259cd21e1f5565a
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-84a31a09d2209279
  evidence_ids:
  - ev-bba8b78c11610a87
  - ev-40d7bb5636e61d3f
  - ev-876019a77eb7ae88
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T15:49:44Z;
    reviewed SHA-256=84d07722cb91d161afb8211b2a1cf76bfec8eaa9182b01d12c9e5f85648d8933;
    current SHA-256=84d07722cb91d161afb8211b2a1cf76bfec8eaa9182b01d12c9e5f85648d8933;
    hash_changed=False. Reports=["reports/yaml_record_review/Etamycin.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The MeSH etamycin identity
    and Viridogrisein synonym pass, but SELECTIVE_AGENT is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-bba8b78c11610a87
    - ev-40d7bb5636e61d3f
  - name: legacy-native-ids
    value: '["SEM:c7ac253b2db2bd5b98a2","SEM:7be98705964a3304ea82"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-40d7bb5636e61d3f
    - ev-bba8b78c11610a87
    - ev-876019a77eb7ae88
- assessment_id: a-522c4e160bf8a245
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-84a31a09d2209279
  evidence_ids:
  - ev-bba8b78c11610a87
  - ev-522c4e160bf8a245
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-bba8b78c11610a87
    - ev-522c4e160bf8a245
findings:
- finding_id: rec-f-56a26af929b7324a
  issue_key: mim-reconciliation-role-support-84a31a09d2209279
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Etamycin'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-84a31a09d2209279
  evidence_ids:
  - ev-bba8b78c11610a87
  - ev-522c4e160bf8a245
  - ev-85eaf51211ec7722
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Etamycin.yaml
    role: maintained ingredient
  field_paths:
  - physicochemical_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024634Z-mim-reconcile-all-batch-06
    finding_id: f-56a26af929b7324a
actions:
- action_id: rec-action-56a26af929b7324a
  description: 'Reassess prediction-only role support: Etamycin'
  finding_ids:
  - rec-f-56a26af929b7324a
  target_ids:
  - record-84a31a09d2209279
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Etamycin.yaml
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
  with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.
```
