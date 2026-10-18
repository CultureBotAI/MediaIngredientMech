# Per-record structured review: Sporangiomycin (data/ingredients/mapped/Sporangiomycin.yaml)

- Review: 20261017T083000Z-sporangiomycin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Sporangiomycin (data/ingredients/mapped/Sporangiomycin.yaml, record-6f1e6279347df935, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Sporangiomycin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Sporangiomycin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-6f1e6279347df935 | data/ingredients/mapped/Sporangiomycin.yaml | maintained | Sporangiomycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-6f1e6279347df935 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-6f1e6279347df935 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-6f1e6279347df935 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-6f1e6279347df935.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-6f1e6279347df935.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:23:59Z; reviewed SHA-256=5e72445459f2a6190d5d0a087b2da5faa9e182d7d02468179d62f218304143ea; current SHA-256=5e72445459f2a6190d5d0a087b2da5faa9e182d7d02468179d62f218304143ea; hash_changed=False. Reports=["reports/yaml_record_review/Sporangiomycin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The MeSH identity resolves, but SELECTIVE_AGENT remains a provisional name-pattern role.

### Historical provisional-role concern

evidence: concern. Targets: record-6f1e6279347df935.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-680f5f4d7f31bd7f: Reassess prediction-only role support: Sporangiomycin

major / open / confirmed; issue key: mim-reconciliation-role-support-6f1e6279347df935.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-680f5f4d7f31bd7f

Reassess prediction-only role support: Sporangiomycin

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-539e04e23e1d570f | data/ingredients/mapped/Sporangiomycin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1890],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C003339","line":1892,"mapping_status":"MAPPED","ontology_id":"mesh:C003339","preferred_term":"Sporangiomycin"}],"identifier":"mesh:C003339","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C003339","ontology_label":"sporangiomycin","ontology_source":"MESH"},"preferred_term":"Sporangiomycin","sssom_rows":[{"data_row":2639,"object_id":"mesh:C003339","object_label":"sporangiomycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sporangiomycin","synonym_count":0} |
| ev-449083ae4799f476 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1890] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-c097a26727840ace | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Sporangiomycin; data-row positions=[2639] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2639,"object_id":"mesh:C003339","object_label":"sporangiomycin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Sporangiomycin","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-439823eab24bdfc7 | docs/data/mapped_ingredients.csv; CSV lines=[1892] | supports | Published identity and count rows inspected: [{"identifier":"mesh:C003339","line":1892,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C003339","preferred_term":"Sporangiomycin","total_occurrences":"0"}] |
| ev-f9b82e1c28c56225 | reports/yaml_record_review/Sporangiomycin.md; &#96;data/ingredients/mapped/Sporangiomycin.yaml&#96;:2; Verdict:4; Identity:9; Validation:18; Evidence:27; Completeness:39; Recommended Edits:45 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-e0aab3c08c2e4696 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1243,2014] | context_only | [{"current_record_sha256":"5e72445459f2a6190d5d0a087b2da5faa9e182d7d02468179d62f218304143ea","finding_id":"SEM:46e2e5383fc9a8b8388b","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"5e72445459f2a6190d5d0a087b2da5faa9e182d7d02468179d62f218304143ea","finding_id":"SEM:3b70ec779c6cf903e064","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-b8637d8fe088ae19 | data/ingredients/mapped/Sporangiomycin.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1890],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C003339","line":1892,"mapping_status":"MAPPED","ontology_id":"mesh:C003339","preferred_term":"Sporangiomycin"}],"identifier":"mesh:C003339","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C003339","ontology_label":"sporangiomycin","ontology_source":"MESH"},"preferred_term":"Sporangiomycin","sssom_rows":[{"data_row":2639,"object_id":"mesh:C003339","object_label":"sporangiomycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sporangiomycin","synonym_count":0} |
| ev-690258aaaaf9f0e1 | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml; findings[finding_id=f-680f5f4d7f31bd7f] | context_only | Predecessor structured review finding f-680f5f4d7f31bd7f in 20261011T024638Z-mim-reconcile-all-batch-11 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-sporangiomycin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Sporangiomycin (data/ingredients/mapped/Sporangiomycin.yaml)'
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
summary: Per-record structured review for Sporangiomycin (data/ingredients/mapped/Sporangiomycin.yaml,
  record-6f1e6279347df935, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Sporangiomycin.yaml
    sha256: 5e72445459f2a6190d5d0a087b2da5faa9e182d7d02468179d62f218304143ea
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
  - path: reports/yaml_record_review/Sporangiomycin.md
    sha256: 5279291c4d05c35e375d9533a076c8535bf88efcde6e16e0c5a1582e999e22f3
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-6f1e6279347df935
  path: data/ingredients/mapped/Sporangiomycin.yaml
  label: Sporangiomycin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sporangiomycin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Sporangiomycin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Sporangiomycin.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-6f1e6279347df935
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-6f1e6279347df935
  evidence_ids:
  - ev-539e04e23e1d570f
  - ev-449083ae4799f476
  - ev-c097a26727840ace
  - ev-439823eab24bdfc7
  - ev-b8637d8fe088ae19
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-6f1e6279347df935
  evidence_ids:
  - ev-539e04e23e1d570f
  - ev-e0aab3c08c2e4696
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-6f1e6279347df935
  evidence_ids:
  - ev-f9b82e1c28c56225
  - ev-e0aab3c08c2e4696
  - ev-690258aaaaf9f0e1
evidence:
- evidence_id: ev-539e04e23e1d570f
  kind: record_content
  reference: data/ingredients/mapped/Sporangiomycin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1890],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C003339","line":1892,"mapping_status":"MAPPED","ontology_id":"mesh:C003339","preferred_term":"Sporangiomycin"}],"identifier":"mesh:C003339","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C003339","ontology_label":"sporangiomycin","ontology_source":"MESH"},"preferred_term":"Sporangiomycin","sssom_rows":[{"data_row":2639,"object_id":"mesh:C003339","object_label":"sporangiomycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sporangiomycin","synonym_count":0}'
  snapshot_sha256: 5e72445459f2a6190d5d0a087b2da5faa9e182d7d02468179d62f218304143ea
- evidence_id: ev-449083ae4799f476
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1890]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-c097a26727840ace
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Sporangiomycin; data-row positions=[2639]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2639,"object_id":"mesh:C003339","object_label":"sporangiomycin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Sporangiomycin","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-439823eab24bdfc7
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1892]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"mesh:C003339","line":1892,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C003339","preferred_term":"Sporangiomycin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-f9b82e1c28c56225
  kind: prior_review
  reference: reports/yaml_record_review/Sporangiomycin.md
  locator: '`data/ingredients/mapped/Sporangiomycin.yaml`:2; Verdict:4; Identity:9;
    Validation:18; Evidence:27; Completeness:39; Recommended Edits:45'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 5279291c4d05c35e375d9533a076c8535bf88efcde6e16e0c5a1582e999e22f3
  quote: "Recommended Edits:\n- Major: either remove `physicochemical_roles.SELECTIVE_AGENT`\
    \ from\n  `data/ingredients/mapped/Sporangiomycin.yaml`, or replace the name-pattern\n\
    \  evidence with a source that explicitly uses sporangiomycin as a selective\n\
    \  agent in a culture context."
- evidence_id: ev-e0aab3c08c2e4696
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1243,2014]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"5e72445459f2a6190d5d0a087b2da5faa9e182d7d02468179d62f218304143ea","finding_id":"SEM:46e2e5383fc9a8b8388b","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"5e72445459f2a6190d5d0a087b2da5faa9e182d7d02468179d62f218304143ea","finding_id":"SEM:3b70ec779c6cf903e064","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-b8637d8fe088ae19
  kind: record_content
  reference: data/ingredients/mapped/Sporangiomycin.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1890],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C003339","line":1892,"mapping_status":"MAPPED","ontology_id":"mesh:C003339","preferred_term":"Sporangiomycin"}],"identifier":"mesh:C003339","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C003339","ontology_label":"sporangiomycin","ontology_source":"MESH"},"preferred_term":"Sporangiomycin","sssom_rows":[{"data_row":2639,"object_id":"mesh:C003339","object_label":"sporangiomycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sporangiomycin","synonym_count":0}'
  snapshot_sha256: 5e72445459f2a6190d5d0a087b2da5faa9e182d7d02468179d62f218304143ea
- evidence_id: ev-690258aaaaf9f0e1
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
  locator: findings[finding_id=f-680f5f4d7f31bd7f]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-680f5f4d7f31bd7f in 20261011T024638Z-mim-reconcile-all-batch-11
  snapshot_sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
assessments:
- assessment_id: a-697f6e9229d14ff6
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-6f1e6279347df935
  evidence_ids:
  - ev-539e04e23e1d570f
  - ev-449083ae4799f476
  - ev-c097a26727840ace
  - ev-439823eab24bdfc7
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-f98c0f05909fb00f
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-6f1e6279347df935
  evidence_ids:
  - ev-f9b82e1c28c56225
  - ev-539e04e23e1d570f
  - ev-e0aab3c08c2e4696
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:23:59Z;
    reviewed SHA-256=5e72445459f2a6190d5d0a087b2da5faa9e182d7d02468179d62f218304143ea;
    current SHA-256=5e72445459f2a6190d5d0a087b2da5faa9e182d7d02468179d62f218304143ea;
    hash_changed=False. Reports=["reports/yaml_record_review/Sporangiomycin.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The MeSH
    identity resolves, but SELECTIVE_AGENT remains a provisional name-pattern role.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f9b82e1c28c56225
    - ev-539e04e23e1d570f
  - name: legacy-native-ids
    value: '["SEM:46e2e5383fc9a8b8388b","SEM:3b70ec779c6cf903e064"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-539e04e23e1d570f
    - ev-f9b82e1c28c56225
    - ev-e0aab3c08c2e4696
- assessment_id: a-b8637d8fe088ae19
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-6f1e6279347df935
  evidence_ids:
  - ev-f9b82e1c28c56225
  - ev-b8637d8fe088ae19
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f9b82e1c28c56225
    - ev-b8637d8fe088ae19
findings:
- finding_id: rec-f-680f5f4d7f31bd7f
  issue_key: mim-reconciliation-role-support-6f1e6279347df935
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Sporangiomycin'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-6f1e6279347df935
  evidence_ids:
  - ev-f9b82e1c28c56225
  - ev-b8637d8fe088ae19
  - ev-690258aaaaf9f0e1
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sporangiomycin.yaml
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
    finding_id: f-680f5f4d7f31bd7f
actions:
- action_id: rec-action-680f5f4d7f31bd7f
  description: 'Reassess prediction-only role support: Sporangiomycin'
  finding_ids:
  - rec-f-680f5f4d7f31bd7f
  target_ids:
  - record-6f1e6279347df935
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sporangiomycin.yaml
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
