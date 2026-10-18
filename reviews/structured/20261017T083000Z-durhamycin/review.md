# Per-record structured review: Durhamycin (data/ingredients/mapped/Durhamycin.yaml)

- Review: 20261017T083000Z-durhamycin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Durhamycin (data/ingredients/mapped/Durhamycin.yaml, record-59f931b0b274af90, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Durhamycin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Durhamycin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-59f931b0b274af90 | data/ingredients/mapped/Durhamycin.yaml | maintained | Durhamycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-59f931b0b274af90 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-59f931b0b274af90 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-59f931b0b274af90 | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-59f931b0b274af90.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-59f931b0b274af90.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T15:24:05Z; reviewed SHA-256=0f1ab3359b879b2a9917cd713f8683634c6c22395f616fc44030eed83e42ae9e; current SHA-256=0f1ab3359b879b2a9917cd713f8683634c6c22395f616fc44030eed83e42ae9e; hash_changed=False. Reports=["reports/yaml_record_review/Durhamycin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local family-level placeholder passes, but the selective-agent role is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-59f931b0b274af90.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-4ccd78542b9da8f1: Reassess prediction-only role support: Durhamycin

major / open / confirmed; issue key: mim-reconciliation-role-support-59f931b0b274af90.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-4ccd78542b9da8f1

Reassess prediction-only role support: Durhamycin

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-46c0c62e4409d82b | data/ingredients/mapped/Durhamycin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[929],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:durhamycin","line":931,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:durhamycin","preferred_term":"Durhamycin"}],"identifier":"kgmicrobe.compound:durhamycin","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:durhamycin","ontology_label":"Durhamycin","ontology_source":"kgmicrobe.compound"},"preferred_term":"Durhamycin","sssom_rows":[{"data_row":1102,"object_id":"kgmicrobe.compound:durhamycin","object_label":"Durhamycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Durhamycin","synonym_count":0} |
| ev-f73bc5f1d6a54a79 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [929] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-2440ca65f89ea173 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Durhamycin; data-row positions=[1102] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1102,"object_id":"kgmicrobe.compound:durhamycin","object_label":"Durhamycin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Durhamycin","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-63308c61bcd9cf29 | docs/data/mapped_ingredients.csv; CSV lines=[931] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:durhamycin","line":931,"mapping_quality":"PLACEHOLDER","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.compound:durhamycin","preferred_term":"Durhamycin","total_occurrences":"0"}] |
| ev-205538e2bd2a1230 | reports/yaml_record_review/Durhamycin.md; &#96;data/ingredients/mapped/Durhamycin.yaml&#96;:2; Verdict:4; Identity:11; Validation:22; Evidence:37; Completeness:56; Recommended Edits:64 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-43ca0ab18ca4f906 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[560,1912] | context_only | [{"current_record_sha256":"0f1ab3359b879b2a9917cd713f8683634c6c22395f616fc44030eed83e42ae9e","finding_id":"SEM:99c297a041d2eee054bf","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"0f1ab3359b879b2a9917cd713f8683634c6c22395f616fc44030eed83e42ae9e","finding_id":"SEM:e4bef249694262f820b7","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-4fee369e25779ebf | data/ingredients/mapped/Durhamycin.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[929],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:durhamycin","line":931,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:durhamycin","preferred_term":"Durhamycin"}],"identifier":"kgmicrobe.compound:durhamycin","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:durhamycin","ontology_label":"Durhamycin","ontology_source":"kgmicrobe.compound"},"preferred_term":"Durhamycin","sssom_rows":[{"data_row":1102,"object_id":"kgmicrobe.compound:durhamycin","object_label":"Durhamycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Durhamycin","synonym_count":0} |
| ev-72302d7e0a283b1c | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-4ccd78542b9da8f1] | context_only | Predecessor structured review finding f-4ccd78542b9da8f1 in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-durhamycin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Durhamycin (data/ingredients/mapped/Durhamycin.yaml)'
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
summary: Per-record structured review for Durhamycin (data/ingredients/mapped/Durhamycin.yaml,
  record-59f931b0b274af90, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Durhamycin.yaml
    sha256: 0f1ab3359b879b2a9917cd713f8683634c6c22395f616fc44030eed83e42ae9e
    role: target
  - path: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
    sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
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
  - path: reports/yaml_record_review/Durhamycin.md
    sha256: fad4a250e2cfc431d3af2531f5b13bd870c96067ad2d95d5f607082df0936d37
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-59f931b0b274af90
  path: data/ingredients/mapped/Durhamycin.yaml
  label: Durhamycin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Durhamycin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Durhamycin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Durhamycin.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-59f931b0b274af90
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-59f931b0b274af90
  evidence_ids:
  - ev-46c0c62e4409d82b
  - ev-f73bc5f1d6a54a79
  - ev-2440ca65f89ea173
  - ev-63308c61bcd9cf29
  - ev-4fee369e25779ebf
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-59f931b0b274af90
  evidence_ids:
  - ev-46c0c62e4409d82b
  - ev-43ca0ab18ca4f906
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-59f931b0b274af90
  evidence_ids:
  - ev-205538e2bd2a1230
  - ev-43ca0ab18ca4f906
  - ev-72302d7e0a283b1c
evidence:
- evidence_id: ev-46c0c62e4409d82b
  kind: record_content
  reference: data/ingredients/mapped/Durhamycin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[929],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:durhamycin","line":931,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:durhamycin","preferred_term":"Durhamycin"}],"identifier":"kgmicrobe.compound:durhamycin","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:durhamycin","ontology_label":"Durhamycin","ontology_source":"kgmicrobe.compound"},"preferred_term":"Durhamycin","sssom_rows":[{"data_row":1102,"object_id":"kgmicrobe.compound:durhamycin","object_label":"Durhamycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Durhamycin","synonym_count":0}'
  snapshot_sha256: 0f1ab3359b879b2a9917cd713f8683634c6c22395f616fc44030eed83e42ae9e
- evidence_id: ev-f73bc5f1d6a54a79
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [929]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-2440ca65f89ea173
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Durhamycin; data-row positions=[1102]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1102,"object_id":"kgmicrobe.compound:durhamycin","object_label":"Durhamycin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Durhamycin","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-63308c61bcd9cf29
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[931]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:durhamycin","line":931,"mapping_quality":"PLACEHOLDER","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.compound:durhamycin","preferred_term":"Durhamycin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-205538e2bd2a1230
  kind: prior_review
  reference: reports/yaml_record_review/Durhamycin.md
  locator: '`data/ingredients/mapped/Durhamycin.yaml`:2; Verdict:4; Identity:11; Validation:22;
    Evidence:37; Completeness:56; Recommended Edits:64'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: fad4a250e2cfc431d3af2531f5b13bd870c96067ad2d95d5f607082df0936d37
  quote: "Recommended Edits:\n- Major: replace the `SELECTIVE_AGENT` computational\
    \ role in\n  `data/ingredients/mapped/Durhamycin.yaml` with source-backed role\
    \ evidence\n  scoped to durhamycin, or remove the role if no support is available;\
    \ then\n  synchronize `data/curated/mapped_ingredients.yaml`."
- evidence_id: ev-43ca0ab18ca4f906
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[560,1912]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"0f1ab3359b879b2a9917cd713f8683634c6c22395f616fc44030eed83e42ae9e","finding_id":"SEM:99c297a041d2eee054bf","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"0f1ab3359b879b2a9917cd713f8683634c6c22395f616fc44030eed83e42ae9e","finding_id":"SEM:e4bef249694262f820b7","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-4fee369e25779ebf
  kind: record_content
  reference: data/ingredients/mapped/Durhamycin.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[929],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:durhamycin","line":931,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:durhamycin","preferred_term":"Durhamycin"}],"identifier":"kgmicrobe.compound:durhamycin","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:durhamycin","ontology_label":"Durhamycin","ontology_source":"kgmicrobe.compound"},"preferred_term":"Durhamycin","sssom_rows":[{"data_row":1102,"object_id":"kgmicrobe.compound:durhamycin","object_label":"Durhamycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Durhamycin","synonym_count":0}'
  snapshot_sha256: 0f1ab3359b879b2a9917cd713f8683634c6c22395f616fc44030eed83e42ae9e
- evidence_id: ev-72302d7e0a283b1c
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-4ccd78542b9da8f1]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-4ccd78542b9da8f1 in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-8f20fe6329e5a312
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-59f931b0b274af90
  evidence_ids:
  - ev-46c0c62e4409d82b
  - ev-f73bc5f1d6a54a79
  - ev-2440ca65f89ea173
  - ev-63308c61bcd9cf29
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-cad8565d347c8d36
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-59f931b0b274af90
  evidence_ids:
  - ev-205538e2bd2a1230
  - ev-46c0c62e4409d82b
  - ev-43ca0ab18ca4f906
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T15:24:05Z;
    reviewed SHA-256=0f1ab3359b879b2a9917cd713f8683634c6c22395f616fc44030eed83e42ae9e;
    current SHA-256=0f1ab3359b879b2a9917cd713f8683634c6c22395f616fc44030eed83e42ae9e;
    hash_changed=False. Reports=["reports/yaml_record_review/Durhamycin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The local family-level
    placeholder passes, but the selective-agent role is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-205538e2bd2a1230
    - ev-46c0c62e4409d82b
  - name: legacy-native-ids
    value: '["SEM:99c297a041d2eee054bf","SEM:e4bef249694262f820b7"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-46c0c62e4409d82b
    - ev-205538e2bd2a1230
    - ev-43ca0ab18ca4f906
- assessment_id: a-4fee369e25779ebf
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-59f931b0b274af90
  evidence_ids:
  - ev-205538e2bd2a1230
  - ev-4fee369e25779ebf
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-205538e2bd2a1230
    - ev-4fee369e25779ebf
findings:
- finding_id: rec-f-4ccd78542b9da8f1
  issue_key: mim-reconciliation-role-support-59f931b0b274af90
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Durhamycin'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-59f931b0b274af90
  evidence_ids:
  - ev-205538e2bd2a1230
  - ev-4fee369e25779ebf
  - ev-72302d7e0a283b1c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Durhamycin.yaml
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
    review_id: 20261011T024633Z-mim-reconcile-all-batch-05
    finding_id: f-4ccd78542b9da8f1
actions:
- action_id: rec-action-4ccd78542b9da8f1
  description: 'Reassess prediction-only role support: Durhamycin'
  finding_ids:
  - rec-f-4ccd78542b9da8f1
  target_ids:
  - record-59f931b0b274af90
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Durhamycin.yaml
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
  with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.
```
