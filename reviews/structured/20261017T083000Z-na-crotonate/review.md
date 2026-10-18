# Per-record structured review: Na-crotonate (data/ingredients/mapped/Na-crotonate.yaml)

- Review: 20261017T083000Z-na-crotonate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Na-crotonate (data/ingredients/mapped/Na-crotonate.yaml, record-598cd4fea2f240d1, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Na-crotonate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Na-crotonate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-598cd4fea2f240d1 | data/ingredients/mapped/Na-crotonate.yaml | maintained | Na-crotonate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-598cd4fea2f240d1 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-598cd4fea2f240d1 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-598cd4fea2f240d1 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-598cd4fea2f240d1.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-598cd4fea2f240d1.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T04:50:08Z; reviewed SHA-256=580f37f396dd35e23abe7f215a7752f2fb956613982e33f029e2c7151ff0bc41; current SHA-256=580f37f396dd35e23abe7f215a7752f2fb956613982e33f029e2c7151ff0bc41; hash_changed=False. Reports=["reports/yaml_record_review/Na-crotonate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The #315 salt/ion repair correctly preserves a local sodium-crotonate identity plus a ChEBI acid parent row, but CARBON_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-598cd4fea2f240d1.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-8bcfac1c264c83f0: Reassess prediction-only role support: Na-crotonate

major / open / confirmed; issue key: mim-reconciliation-role-support-598cd4fea2f240d1.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-8bcfac1c264c83f0

Reassess prediction-only role support: Na-crotonate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-551f36faff7c2b8a | data/ingredients/mapped/Na-crotonate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1464],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:na-crotonate","line":1466,"mapping_status":"MAPPED","ontology_id":"CHEBI:41131","preferred_term":"Na-crotonate"}],"identifier":"kgmicrobe.compound:na-crotonate","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":9,"edge_count":9,"occurrences":9},"occurrence_statistics":{"media_count":9,"total_occurrences":9},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:41131","ontology_label":"crotonic acid","ontology_source":"CHEBI"},"preferred_term":"Na-crotonate","sssom_rows":[{"data_row":1967,"object_id":"CHEBI:41131","object_label":"crotonic acid","predicate_id":"skos:broadMatch"},{"data_row":1968,"object_id":"kgmicrobe.compound:na-crotonate","object_label":"Na-crotonate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na-crotonate","synonym_count":13} |
| ev-1017247568924135 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1464] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-cff3ef2fa265597c | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Na-crotonate; data-row positions=[1967,1968] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1967,"object_id":"CHEBI:41131","object_label":"crotonic acid","other":"Sodium crotonate","predicate_id":"skos:broadMatch","subject_id":"MIM:Na-crotonate","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":1968,"object_id":"kgmicrobe.compound:na-crotonate","object_label":"Na-crotonate","other":"Sodium crotonate","predicate_id":"skos:exactMatch","subject_id":"MIM:Na-crotonate","validation_method":""}] |
| ev-ecb2072dec6857c4 | docs/data/mapped_ingredients.csv; CSV lines=[1466] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:na-crotonate","line":1466,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"9","ontology_id":"CHEBI:41131","preferred_term":"Na-crotonate","total_occurrences":"9"}] |
| ev-03a7cc8277bad514 | reports/yaml_record_review/Na-crotonate.md; &#96;data/ingredients/mapped/Na-crotonate.yaml&#96;:2; Verdict:4; Identity:11; Validation:20; Evidence:27; Completeness:45; Recommended Edits:52 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-5303b4289371e774 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[973,1836] | context_only | [{"current_record_sha256":"580f37f396dd35e23abe7f215a7752f2fb956613982e33f029e2c7151ff0bc41","finding_id":"SEM:d5907f1dd4392249d00a","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"580f37f396dd35e23abe7f215a7752f2fb956613982e33f029e2c7151ff0bc41","finding_id":"SEM:99ea370dfca6ad11227a","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-ef9be04989818227 | data/ingredients/mapped/Na-crotonate.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional in-session LLM role assignment; review recommended.","reference_text":"Assigned by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}] |
| ev-38088c2344554b1f | reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml; findings[finding_id=f-8bcfac1c264c83f0] | context_only | Predecessor structured review finding f-8bcfac1c264c83f0 in 20261011T024637Z-mim-reconcile-all-batch-09 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-na-crotonate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Na-crotonate (data/ingredients/mapped/Na-crotonate.yaml)'
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
summary: Per-record structured review for Na-crotonate (data/ingredients/mapped/Na-crotonate.yaml,
  record-598cd4fea2f240d1, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Na-crotonate.yaml
    sha256: 580f37f396dd35e23abe7f215a7752f2fb956613982e33f029e2c7151ff0bc41
    role: target
  - path: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
    sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
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
  - path: reports/yaml_record_review/Na-crotonate.md
    sha256: e6c933e4e6f2aa2b9c45e59734935bfb100049908f3aea4d41e1315bb84dc322
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-598cd4fea2f240d1
  path: data/ingredients/mapped/Na-crotonate.yaml
  label: Na-crotonate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na-crotonate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Na-crotonate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Na-crotonate.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-598cd4fea2f240d1
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-598cd4fea2f240d1
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-598cd4fea2f240d1
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-598cd4fea2f240d1
evidence:
- evidence_id: ev-551f36faff7c2b8a
  kind: record_content
  reference: data/ingredients/mapped/Na-crotonate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1464],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:na-crotonate","line":1466,"mapping_status":"MAPPED","ontology_id":"CHEBI:41131","preferred_term":"Na-crotonate"}],"identifier":"kgmicrobe.compound:na-crotonate","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":9,"edge_count":9,"occurrences":9},"occurrence_statistics":{"media_count":9,"total_occurrences":9},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:41131","ontology_label":"crotonic
    acid","ontology_source":"CHEBI"},"preferred_term":"Na-crotonate","sssom_rows":[{"data_row":1967,"object_id":"CHEBI:41131","object_label":"crotonic
    acid","predicate_id":"skos:broadMatch"},{"data_row":1968,"object_id":"kgmicrobe.compound:na-crotonate","object_label":"Na-crotonate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na-crotonate","synonym_count":13}'
  snapshot_sha256: 580f37f396dd35e23abe7f215a7752f2fb956613982e33f029e2c7151ff0bc41
- evidence_id: ev-1017247568924135
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1464]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-cff3ef2fa265597c
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Na-crotonate; data-row positions=[1967,1968]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1967,"object_id":"CHEBI:41131","object_label":"crotonic
    acid","other":"Sodium crotonate","predicate_id":"skos:broadMatch","subject_id":"MIM:Na-crotonate","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":1968,"object_id":"kgmicrobe.compound:na-crotonate","object_label":"Na-crotonate","other":"Sodium
    crotonate","predicate_id":"skos:exactMatch","subject_id":"MIM:Na-crotonate","validation_method":""}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-ecb2072dec6857c4
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1466]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:na-crotonate","line":1466,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"9","ontology_id":"CHEBI:41131","preferred_term":"Na-crotonate","total_occurrences":"9"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-03a7cc8277bad514
  kind: prior_review
  reference: reports/yaml_record_review/Na-crotonate.md
  locator: '`data/ingredients/mapped/Na-crotonate.yaml`:2; Verdict:4; Identity:11;
    Validation:20; Evidence:27; Completeness:45; Recommended Edits:52'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: e6c933e4e6f2aa2b9c45e59734935bfb100049908f3aea4d41e1315bb84dc322
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Na-crotonate.yaml`,\
    \ either remove\n  `nutritional_roles.CARBON_SOURCE` or replace its computational\
    \ placeholder\n  with source-backed evidence from maintained occurrence, role-text,\
    \ or\n  literature inputs. Rerun strict validation and final SSSOM validation\
    \ after\n  the role facet changes."
- evidence_id: ev-5303b4289371e774
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[973,1836]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"580f37f396dd35e23abe7f215a7752f2fb956613982e33f029e2c7151ff0bc41","finding_id":"SEM:d5907f1dd4392249d00a","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"580f37f396dd35e23abe7f215a7752f2fb956613982e33f029e2c7151ff0bc41","finding_id":"SEM:99ea370dfca6ad11227a","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-ef9be04989818227
  kind: record_content
  reference: data/ingredients/mapped/Na-crotonate.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional
    in-session LLM role assignment; review recommended.","reference_text":"Assigned
    by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}]'
  snapshot_sha256: 580f37f396dd35e23abe7f215a7752f2fb956613982e33f029e2c7151ff0bc41
- evidence_id: ev-38088c2344554b1f
  kind: prior_review
  reference: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
  locator: findings[finding_id=f-8bcfac1c264c83f0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-8bcfac1c264c83f0 in 20261011T024637Z-mim-reconcile-all-batch-09
  snapshot_sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
assessments:
- assessment_id: a-24dbde66f841a980
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-598cd4fea2f240d1
  evidence_ids:
  - ev-551f36faff7c2b8a
  - ev-1017247568924135
  - ev-cff3ef2fa265597c
  - ev-ecb2072dec6857c4
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-1ecb4a5dda5fb4e8
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-598cd4fea2f240d1
  evidence_ids:
  - ev-03a7cc8277bad514
  - ev-551f36faff7c2b8a
  - ev-5303b4289371e774
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T04:50:08Z;
    reviewed SHA-256=580f37f396dd35e23abe7f215a7752f2fb956613982e33f029e2c7151ff0bc41;
    current SHA-256=580f37f396dd35e23abe7f215a7752f2fb956613982e33f029e2c7151ff0bc41;
    hash_changed=False. Reports=["reports/yaml_record_review/Na-crotonate.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The #315 salt/ion
    repair correctly preserves a local sodium-crotonate identity plus a ChEBI acid
    parent row, but CARBON_SOURCE is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-03a7cc8277bad514
    - ev-551f36faff7c2b8a
  - name: legacy-native-ids
    value: '["SEM:d5907f1dd4392249d00a","SEM:99ea370dfca6ad11227a"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-551f36faff7c2b8a
    - ev-03a7cc8277bad514
    - ev-5303b4289371e774
- assessment_id: a-ef9be04989818227
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-598cd4fea2f240d1
  evidence_ids:
  - ev-03a7cc8277bad514
  - ev-ef9be04989818227
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-03a7cc8277bad514
    - ev-ef9be04989818227
findings:
- finding_id: rec-f-8bcfac1c264c83f0
  issue_key: mim-reconciliation-role-support-598cd4fea2f240d1
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Na-crotonate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-598cd4fea2f240d1
  evidence_ids:
  - ev-03a7cc8277bad514
  - ev-ef9be04989818227
  - ev-38088c2344554b1f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na-crotonate.yaml
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
    review_id: 20261011T024637Z-mim-reconcile-all-batch-09
    finding_id: f-8bcfac1c264c83f0
actions:
- action_id: rec-action-8bcfac1c264c83f0
  description: 'Reassess prediction-only role support: Na-crotonate'
  finding_ids:
  - rec-f-8bcfac1c264c83f0
  target_ids:
  - record-598cd4fea2f240d1
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na-crotonate.yaml
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
  with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.
```
