# Per-record structured review: Staphylomycin_M1 (data/ingredients/mapped/Staphylomycin_M1.yaml)

- Review: 20261017T083000Z-staphylomycin-m1
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Staphylomycin_M1 (data/ingredients/mapped/Staphylomycin_M1.yaml, record-a23ca2964dcddeec, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Staphylomycin_M1.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Staphylomycin_M1.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-a23ca2964dcddeec | data/ingredients/mapped/Staphylomycin_M1.yaml | maintained | Staphylomycin_M1 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-a23ca2964dcddeec | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-a23ca2964dcddeec | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-a23ca2964dcddeec | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-a23ca2964dcddeec.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-a23ca2964dcddeec.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:29:20Z; reviewed SHA-256=04785e91917d2e9a1a1e670e3dd871cc6745b43eed0f75d32c41f1e83061a431; current SHA-256=04785e91917d2e9a1a1e670e3dd871cc6745b43eed0f75d32c41f1e83061a431; hash_changed=False. Reports=["reports/yaml_record_review/Staphylomycin_M1.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact NCIT:C1295 identity resolves, but SELECTIVE_AGENT remains a provisional name-pattern role.

### Historical provisional-role concern

evidence: concern. Targets: record-a23ca2964dcddeec.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-68f08b6bf2f567f0: Reassess prediction-only role support: Staphylomycin M1

major / open / confirmed; issue key: mim-reconciliation-role-support-a23ca2964dcddeec.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-68f08b6bf2f567f0

Reassess prediction-only role support: Staphylomycin M1

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-dbb79f3910837456 | data/ingredients/mapped/Staphylomycin_M1.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1897],"raw_equal":true},"docs_rows":[{"identifier":"NCIT:C1295","line":1899,"mapping_status":"MAPPED","ontology_id":"NCIT:C1295","preferred_term":"Staphylomycin M1"}],"identifier":"NCIT:C1295","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"NCIT:C1295","ontology_label":"Streptogramin A","ontology_source":"NCIT"},"preferred_term":"Staphylomycin M1","sssom_rows":[{"data_row":2644,"object_id":"NCIT:C1295","object_label":"Streptogramin A","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Staphylomycin_M1","synonym_count":0} |
| ev-d22b64901a4ec75a | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1897] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-db9e351296a900a6 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Staphylomycin_M1; data-row positions=[2644] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2644,"object_id":"NCIT:C1295","object_label":"Streptogramin A","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Staphylomycin_M1","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-49b43022a33ef653 | docs/data/mapped_ingredients.csv; CSV lines=[1899] | supports | Published identity and count rows inspected: [{"identifier":"NCIT:C1295","line":1899,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"NCIT:C1295","preferred_term":"Staphylomycin M1","total_occurrences":"0"}] |
| ev-7780d97ae9d2cdfa | reports/yaml_record_review/Staphylomycin_M1.md; &#96;data/ingredients/mapped/Staphylomycin_M1.yaml&#96;:2; Verdict:4; Identity:9; Validation:18; Evidence:26; Completeness:36; Recommended Edits:42 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-6be72a671b093486 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1249,2009] | context_only | [{"current_record_sha256":"04785e91917d2e9a1a1e670e3dd871cc6745b43eed0f75d32c41f1e83061a431","finding_id":"SEM:29f62f7b822c61c7c067","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"04785e91917d2e9a1a1e670e3dd871cc6745b43eed0f75d32c41f1e83061a431","finding_id":"SEM:5039e809f185b52b85d1","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-7c86d2b6443d5431 | data/ingredients/mapped/Staphylomycin_M1.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}] |
| ev-cbf9c689fbcd3eba | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml; findings[finding_id=f-68f08b6bf2f567f0] | context_only | Predecessor structured review finding f-68f08b6bf2f567f0 in 20261011T024638Z-mim-reconcile-all-batch-11 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-staphylomycin-m1
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Staphylomycin_M1 (data/ingredients/mapped/Staphylomycin_M1.yaml)'
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
summary: Per-record structured review for Staphylomycin_M1 (data/ingredients/mapped/Staphylomycin_M1.yaml,
  record-a23ca2964dcddeec, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Staphylomycin_M1.yaml
    sha256: 04785e91917d2e9a1a1e670e3dd871cc6745b43eed0f75d32c41f1e83061a431
    role: target
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
    sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
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
  - path: reports/yaml_record_review/Staphylomycin_M1.md
    sha256: c79f2b0886abbd1e9f9bbbcf79e51ac8e23f942c70b9411182ebae20c7e8f9e8
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-a23ca2964dcddeec
  path: data/ingredients/mapped/Staphylomycin_M1.yaml
  label: Staphylomycin_M1
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Staphylomycin_M1.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Staphylomycin_M1.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Staphylomycin_M1.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-a23ca2964dcddeec
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-a23ca2964dcddeec
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-a23ca2964dcddeec
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-a23ca2964dcddeec
evidence:
- evidence_id: ev-dbb79f3910837456
  kind: record_content
  reference: data/ingredients/mapped/Staphylomycin_M1.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1897],"raw_equal":true},"docs_rows":[{"identifier":"NCIT:C1295","line":1899,"mapping_status":"MAPPED","ontology_id":"NCIT:C1295","preferred_term":"Staphylomycin
    M1"}],"identifier":"NCIT:C1295","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"NCIT:C1295","ontology_label":"Streptogramin
    A","ontology_source":"NCIT"},"preferred_term":"Staphylomycin M1","sssom_rows":[{"data_row":2644,"object_id":"NCIT:C1295","object_label":"Streptogramin
    A","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Staphylomycin_M1","synonym_count":0}'
  snapshot_sha256: 04785e91917d2e9a1a1e670e3dd871cc6745b43eed0f75d32c41f1e83061a431
- evidence_id: ev-d22b64901a4ec75a
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1897]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-db9e351296a900a6
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Staphylomycin_M1; data-row positions=[2644]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2644,"object_id":"NCIT:C1295","object_label":"Streptogramin
    A","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Staphylomycin_M1","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-49b43022a33ef653
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1899]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"NCIT:C1295","line":1899,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"NCIT:C1295","preferred_term":"Staphylomycin
    M1","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-7780d97ae9d2cdfa
  kind: prior_review
  reference: reports/yaml_record_review/Staphylomycin_M1.md
  locator: '`data/ingredients/mapped/Staphylomycin_M1.yaml`:2; Verdict:4; Identity:9;
    Validation:18; Evidence:26; Completeness:36; Recommended Edits:42'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: c79f2b0886abbd1e9f9bbbcf79e51ac8e23f942c70b9411182ebae20c7e8f9e8
  quote: "Recommended Edits:\n- Major: either remove `physicochemical_roles.SELECTIVE_AGENT`\
    \ from\n  `data/ingredients/mapped/Staphylomycin_M1.yaml`, or replace the name-pattern\n\
    \  evidence with a source that explicitly uses Staphylomycin M1 as a selective\n\
    \  agent in a culture context."
- evidence_id: ev-6be72a671b093486
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1249,2009]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"04785e91917d2e9a1a1e670e3dd871cc6745b43eed0f75d32c41f1e83061a431","finding_id":"SEM:29f62f7b822c61c7c067","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"04785e91917d2e9a1a1e670e3dd871cc6745b43eed0f75d32c41f1e83061a431","finding_id":"SEM:5039e809f185b52b85d1","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-7c86d2b6443d5431
  kind: record_content
  reference: data/ingredients/mapped/Staphylomycin_M1.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}]'
  snapshot_sha256: 04785e91917d2e9a1a1e670e3dd871cc6745b43eed0f75d32c41f1e83061a431
- evidence_id: ev-cbf9c689fbcd3eba
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
  locator: findings[finding_id=f-68f08b6bf2f567f0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-68f08b6bf2f567f0 in 20261011T024638Z-mim-reconcile-all-batch-11
  snapshot_sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
assessments:
- assessment_id: a-87889ad2a67aa0fa
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-a23ca2964dcddeec
  evidence_ids:
  - ev-dbb79f3910837456
  - ev-d22b64901a4ec75a
  - ev-db9e351296a900a6
  - ev-49b43022a33ef653
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-0d059592cb2aac90
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-a23ca2964dcddeec
  evidence_ids:
  - ev-7780d97ae9d2cdfa
  - ev-dbb79f3910837456
  - ev-6be72a671b093486
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:29:20Z;
    reviewed SHA-256=04785e91917d2e9a1a1e670e3dd871cc6745b43eed0f75d32c41f1e83061a431;
    current SHA-256=04785e91917d2e9a1a1e670e3dd871cc6745b43eed0f75d32c41f1e83061a431;
    hash_changed=False. Reports=["reports/yaml_record_review/Staphylomycin_M1.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    NCIT:C1295 identity resolves, but SELECTIVE_AGENT remains a provisional name-pattern
    role.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-7780d97ae9d2cdfa
    - ev-dbb79f3910837456
  - name: legacy-native-ids
    value: '["SEM:29f62f7b822c61c7c067","SEM:5039e809f185b52b85d1"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-dbb79f3910837456
    - ev-7780d97ae9d2cdfa
    - ev-6be72a671b093486
- assessment_id: a-7c86d2b6443d5431
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-a23ca2964dcddeec
  evidence_ids:
  - ev-7780d97ae9d2cdfa
  - ev-7c86d2b6443d5431
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-7780d97ae9d2cdfa
    - ev-7c86d2b6443d5431
findings:
- finding_id: rec-f-68f08b6bf2f567f0
  issue_key: mim-reconciliation-role-support-a23ca2964dcddeec
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Staphylomycin M1'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-a23ca2964dcddeec
  evidence_ids:
  - ev-7780d97ae9d2cdfa
  - ev-7c86d2b6443d5431
  - ev-cbf9c689fbcd3eba
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Staphylomycin_M1.yaml
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
    review_id: 20261011T024638Z-mim-reconcile-all-batch-11
    finding_id: f-68f08b6bf2f567f0
actions:
- action_id: rec-action-68f08b6bf2f567f0
  description: 'Reassess prediction-only role support: Staphylomycin M1'
  finding_ids:
  - rec-f-68f08b6bf2f567f0
  target_ids:
  - record-a23ca2964dcddeec
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Staphylomycin_M1.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.
```
