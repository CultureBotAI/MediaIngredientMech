# Per-record structured review: Proteose_Peptone (data/ingredients/mapped/Proteose_Peptone.yaml)

- Review: 20261017T083000Z-proteose-peptone
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Proteose_Peptone (data/ingredients/mapped/Proteose_Peptone.yaml, record-cd3c1fcd33dd4ec6, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Proteose_Peptone.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Proteose_Peptone.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-cd3c1fcd33dd4ec6 | data/ingredients/mapped/Proteose_Peptone.yaml | maintained | Proteose_Peptone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-cd3c1fcd33dd4ec6 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-cd3c1fcd33dd4ec6 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-cd3c1fcd33dd4ec6 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-cd3c1fcd33dd4ec6.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-cd3c1fcd33dd4ec6.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T10:43:30Z; reviewed SHA-256=c0541faf7f493f617c3f92f8082a1aab6052aa3fa392f802534e201b50ace34e; current SHA-256=c0541faf7f493f617c3f92f8082a1aab6052aa3fa392f802534e201b50ace34e; hash_changed=False. Reports=["reports/yaml_record_review/Proteose_Peptone.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact MICRO:0000180 identity passes, but final SSSOM exports a broad peptic-digest synonym and PROTEIN_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-cd3c1fcd33dd4ec6.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-4bcce20a7fef6e6f: Reassess prediction-only role support: Proteose Peptone

major / open / confirmed; issue key: mim-reconciliation-role-support-cd3c1fcd33dd4ec6.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-4bcce20a7fef6e6f

Reassess prediction-only role support: Proteose Peptone

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-913fc448ef8f8815 | data/ingredients/mapped/Proteose_Peptone.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1708],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0000180","line":1710,"mapping_status":"MAPPED","ontology_id":"MICRO:0000180","preferred_term":"Proteose Peptone"}],"identifier":"MICRO:0000180","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":563,"edge_count":563,"occurrences":571},"occurrence_statistics":{"media_count":563,"total_occurrences":571},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"MICRO:0000180","ontology_label":"proteose peptone","ontology_source":"MICRO"},"preferred_term":"Proteose Peptone","sssom_rows":[{"data_row":2357,"object_id":"MICRO:0000180","object_label":"proteose peptone","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Proteose_Peptone","synonym_count":18} |
| ev-3d7d19477c615093 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1708] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-7b251b8102df7c12 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Proteose_Peptone; data-row positions=[2357] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2357,"object_id":"MICRO:0000180","object_label":"proteose peptone","other":"Proteose Peptone(BD 211684)&#124;Proteose peptone no. 3&#124;Proteose peptone No. 3 (BD-Difco)&#124;Bacto Proteose Peptone No. 3 (Difco)&#124;Proteose peptone (BD-Difco)&#124;Proteose Peptone (Difco no. 3)&#124;Proteose peptone (Difco)&#124;Proteose peptone (BD Difco)&#124;Bacto Proteose Peptone No.3 (Difco)&#124;Proteose peptone no.3 (Difco)&#124;Proteose peptone No. 3 (BD--Difco)&#124;Proteose peptone (BD--Difco)&#124;Peptic digest of animal tissue&#124;Proteose peptone (BD Difico)&#124;CAS:91079-38-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Proteose_Peptone","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-7d190656356ccc6a | docs/data/mapped_ingredients.csv; CSV lines=[1710] | supports | Published identity and count rows inspected: [{"identifier":"MICRO:0000180","line":1710,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"563","ontology_id":"MICRO:0000180","preferred_term":"Proteose Peptone","total_occurrences":"571"}] |
| ev-dcd1398156c5661f | reports/yaml_record_review/Proteose_Peptone.md; &#96;data/ingredients/mapped/Proteose_Peptone.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-b4ead25b68a4d8c1 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1144,1437] | context_only | [{"current_record_sha256":"c0541faf7f493f617c3f92f8082a1aab6052aa3fa392f802534e201b50ace34e","finding_id":"SEM:9023f8783016407b83d9","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c0541faf7f493f617c3f92f8082a1aab6052aa3fa392f802534e201b50ace34e","finding_id":"SEM:8850e6476dbdc8aa080f","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-70d63bc9e8058af4 | data/ingredients/mapped/Proteose_Peptone.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1708],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0000180","line":1710,"mapping_status":"MAPPED","ontology_id":"MICRO:0000180","preferred_term":"Proteose Peptone"}],"identifier":"MICRO:0000180","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":563,"edge_count":563,"occurrences":571},"occurrence_statistics":{"media_count":563,"total_occurrences":571},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"MICRO:0000180","ontology_label":"proteose peptone","ontology_source":"MICRO"},"preferred_term":"Proteose Peptone","sssom_rows":[{"data_row":2357,"object_id":"MICRO:0000180","object_label":"proteose peptone","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Proteose_Peptone","synonym_count":18} |
| ev-1c84e53a4b083505 | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml; findings[finding_id=f-4bcce20a7fef6e6f] | context_only | Predecessor structured review finding f-4bcce20a7fef6e6f in 20261011T024638Z-mim-reconcile-all-batch-10 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-proteose-peptone
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Proteose_Peptone (data/ingredients/mapped/Proteose_Peptone.yaml)'
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
summary: Per-record structured review for Proteose_Peptone (data/ingredients/mapped/Proteose_Peptone.yaml,
  record-cd3c1fcd33dd4ec6, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Proteose_Peptone.yaml
    sha256: c0541faf7f493f617c3f92f8082a1aab6052aa3fa392f802534e201b50ace34e
    role: target
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
    sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
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
  - path: reports/yaml_record_review/Proteose_Peptone.md
    sha256: 15a84c2af5180a8e7b7022c153197d0c5a8c09bed02cd684ae48d7fb37bc8faa
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-cd3c1fcd33dd4ec6
  path: data/ingredients/mapped/Proteose_Peptone.yaml
  label: Proteose_Peptone
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Proteose_Peptone.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Proteose_Peptone.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Proteose_Peptone.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-cd3c1fcd33dd4ec6
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-cd3c1fcd33dd4ec6
  evidence_ids:
  - ev-913fc448ef8f8815
  - ev-3d7d19477c615093
  - ev-7b251b8102df7c12
  - ev-7d190656356ccc6a
  - ev-70d63bc9e8058af4
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-cd3c1fcd33dd4ec6
  evidence_ids:
  - ev-913fc448ef8f8815
  - ev-b4ead25b68a4d8c1
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10
    and semantic review dispositions on HEAD.
  target_ids:
  - record-cd3c1fcd33dd4ec6
  evidence_ids:
  - ev-dcd1398156c5661f
  - ev-b4ead25b68a4d8c1
  - ev-1c84e53a4b083505
evidence:
- evidence_id: ev-913fc448ef8f8815
  kind: record_content
  reference: data/ingredients/mapped/Proteose_Peptone.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1708],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0000180","line":1710,"mapping_status":"MAPPED","ontology_id":"MICRO:0000180","preferred_term":"Proteose
    Peptone"}],"identifier":"MICRO:0000180","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":563,"edge_count":563,"occurrences":571},"occurrence_statistics":{"media_count":563,"total_occurrences":571},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"MICRO:0000180","ontology_label":"proteose
    peptone","ontology_source":"MICRO"},"preferred_term":"Proteose Peptone","sssom_rows":[{"data_row":2357,"object_id":"MICRO:0000180","object_label":"proteose
    peptone","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Proteose_Peptone","synonym_count":18}'
  snapshot_sha256: c0541faf7f493f617c3f92f8082a1aab6052aa3fa392f802534e201b50ace34e
- evidence_id: ev-3d7d19477c615093
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1708]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-7b251b8102df7c12
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Proteose_Peptone; data-row positions=[2357]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2357,"object_id":"MICRO:0000180","object_label":"proteose
    peptone","other":"Proteose Peptone(BD 211684)|Proteose peptone no. 3|Proteose
    peptone No. 3 (BD-Difco)|Bacto Proteose Peptone No. 3 (Difco)|Proteose peptone
    (BD-Difco)|Proteose Peptone (Difco no. 3)|Proteose peptone (Difco)|Proteose peptone
    (BD Difco)|Bacto Proteose Peptone No.3 (Difco)|Proteose peptone no.3 (Difco)|Proteose
    peptone No. 3 (BD--Difco)|Proteose peptone (BD--Difco)|Peptic digest of animal
    tissue|Proteose peptone (BD Difico)|CAS:91079-38-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Proteose_Peptone","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-7d190656356ccc6a
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1710]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"MICRO:0000180","line":1710,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"563","ontology_id":"MICRO:0000180","preferred_term":"Proteose
    Peptone","total_occurrences":"571"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-dcd1398156c5661f
  kind: prior_review
  reference: reports/yaml_record_review/Proteose_Peptone.md
  locator: '`data/ingredients/mapped/Proteose_Peptone.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 15a84c2af5180a8e7b7022c153197d0c5a8c09bed02cd684ae48d7fb37bc8faa
- evidence_id: ev-b4ead25b68a4d8c1
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1144,1437]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"c0541faf7f493f617c3f92f8082a1aab6052aa3fa392f802534e201b50ace34e","finding_id":"SEM:9023f8783016407b83d9","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c0541faf7f493f617c3f92f8082a1aab6052aa3fa392f802534e201b50ace34e","finding_id":"SEM:8850e6476dbdc8aa080f","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-70d63bc9e8058af4
  kind: record_content
  reference: data/ingredients/mapped/Proteose_Peptone.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1708],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0000180","line":1710,"mapping_status":"MAPPED","ontology_id":"MICRO:0000180","preferred_term":"Proteose
    Peptone"}],"identifier":"MICRO:0000180","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":563,"edge_count":563,"occurrences":571},"occurrence_statistics":{"media_count":563,"total_occurrences":571},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"MICRO:0000180","ontology_label":"proteose
    peptone","ontology_source":"MICRO"},"preferred_term":"Proteose Peptone","sssom_rows":[{"data_row":2357,"object_id":"MICRO:0000180","object_label":"proteose
    peptone","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Proteose_Peptone","synonym_count":18}'
  snapshot_sha256: c0541faf7f493f617c3f92f8082a1aab6052aa3fa392f802534e201b50ace34e
- evidence_id: ev-1c84e53a4b083505
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
  locator: findings[finding_id=f-4bcce20a7fef6e6f]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-4bcce20a7fef6e6f in 20261011T024638Z-mim-reconcile-all-batch-10
  snapshot_sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
assessments:
- assessment_id: a-382000774d827089
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-cd3c1fcd33dd4ec6
  evidence_ids:
  - ev-913fc448ef8f8815
  - ev-3d7d19477c615093
  - ev-7b251b8102df7c12
  - ev-7d190656356ccc6a
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-d6ee61b61de50b7f
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-cd3c1fcd33dd4ec6
  evidence_ids:
  - ev-dcd1398156c5661f
  - ev-913fc448ef8f8815
  - ev-b4ead25b68a4d8c1
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T10:43:30Z;
    reviewed SHA-256=c0541faf7f493f617c3f92f8082a1aab6052aa3fa392f802534e201b50ace34e;
    current SHA-256=c0541faf7f493f617c3f92f8082a1aab6052aa3fa392f802534e201b50ace34e;
    hash_changed=False. Reports=["reports/yaml_record_review/Proteose_Peptone.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    MICRO:0000180 identity passes, but final SSSOM exports a broad peptic-digest synonym
    and PROTEIN_SOURCE is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-dcd1398156c5661f
    - ev-913fc448ef8f8815
  - name: legacy-native-ids
    value: '["SEM:9023f8783016407b83d9","SEM:8850e6476dbdc8aa080f"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-913fc448ef8f8815
    - ev-dcd1398156c5661f
    - ev-b4ead25b68a4d8c1
- assessment_id: a-70d63bc9e8058af4
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-cd3c1fcd33dd4ec6
  evidence_ids:
  - ev-dcd1398156c5661f
  - ev-70d63bc9e8058af4
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-dcd1398156c5661f
    - ev-70d63bc9e8058af4
findings:
- finding_id: rec-f-4bcce20a7fef6e6f
  issue_key: mim-reconciliation-role-support-cd3c1fcd33dd4ec6
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Proteose Peptone'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-cd3c1fcd33dd4ec6
  evidence_ids:
  - ev-dcd1398156c5661f
  - ev-70d63bc9e8058af4
  - ev-1c84e53a4b083505
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Proteose_Peptone.yaml
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
    review_id: 20261011T024638Z-mim-reconcile-all-batch-10
    finding_id: f-4bcce20a7fef6e6f
actions:
- action_id: rec-action-4bcce20a7fef6e6f
  description: 'Reassess prediction-only role support: Proteose Peptone'
  finding_ids:
  - rec-f-4bcce20a7fef6e6f
  target_ids:
  - record-cd3c1fcd33dd4ec6
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Proteose_Peptone.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.
```
