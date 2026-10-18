# Per-record structured review: Phoslactomycin (data/ingredients/mapped/Phoslactomycin.yaml)

- Review: 20261017T083000Z-phoslactomycin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Phoslactomycin (data/ingredients/mapped/Phoslactomycin.yaml, record-29a7cfdfdb7dacab, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Phoslactomycin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Phoslactomycin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-29a7cfdfdb7dacab | data/ingredients/mapped/Phoslactomycin.yaml | maintained | Phoslactomycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-29a7cfdfdb7dacab | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-29a7cfdfdb7dacab | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-29a7cfdfdb7dacab | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-29a7cfdfdb7dacab.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-29a7cfdfdb7dacab.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T09:16:23Z; reviewed SHA-256=668d501fc6afdf4e76ff8dfc0021a3e1351c923dae7dfa2a38e17e0c207dda7d; current SHA-256=668d501fc6afdf4e76ff8dfc0021a3e1351c923dae7dfa2a38e17e0c207dda7d; hash_changed=False. Reports=["reports/yaml_record_review/Phoslactomycin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local phoslactomycin family placeholder is intentionally retained, but SELECTIVE_AGENT is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-29a7cfdfdb7dacab.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-12111d3e0c9420d7: Reassess prediction-only role support: Phoslactomycin

major / open / confirmed; issue key: mim-reconciliation-role-support-29a7cfdfdb7dacab.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-12111d3e0c9420d7

Reassess prediction-only role support: Phoslactomycin

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-bcaaeac8ab9d7cd5 | data/ingredients/mapped/Phoslactomycin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1649],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:phoslactomycin","line":1651,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:phoslactomycin","preferred_term":"Phoslactomycin"}],"identifier":"kgmicrobe.compound:phoslactomycin","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:phoslactomycin","ontology_label":"Phoslactomycin","ontology_source":"kgmicrobe.compound"},"preferred_term":"Phoslactomycin","sssom_rows":[{"data_row":2245,"object_id":"kgmicrobe.compound:phoslactomycin","object_label":"Phoslactomycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Phoslactomycin","synonym_count":0} |
| ev-b81c99cfe5ec370e | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1649] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-e3e91f1660dc88ce | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Phoslactomycin; data-row positions=[2245] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2245,"object_id":"kgmicrobe.compound:phoslactomycin","object_label":"Phoslactomycin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Phoslactomycin","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-d58de164e4ad951e | docs/data/mapped_ingredients.csv; CSV lines=[1651] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:phoslactomycin","line":1651,"mapping_quality":"PLACEHOLDER","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.compound:phoslactomycin","preferred_term":"Phoslactomycin","total_occurrences":"0"}] |
| ev-cddf276c52508793 | reports/yaml_record_review/Phoslactomycin.md; &#96;data/ingredients/mapped/Phoslactomycin.yaml&#96;:2; Verdict:4; Identity:10; Validation:21; Evidence:34; Completeness:46; Recommended Edits:53 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-ac00b505e08006f9 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1108,1755] | context_only | [{"current_record_sha256":"668d501fc6afdf4e76ff8dfc0021a3e1351c923dae7dfa2a38e17e0c207dda7d","finding_id":"SEM:8871918dd96afd6458f5","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"668d501fc6afdf4e76ff8dfc0021a3e1351c923dae7dfa2a38e17e0c207dda7d","finding_id":"SEM:c88ad167cfcdfb9596b7","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-8a158957bd9bf25a | data/ingredients/mapped/Phoslactomycin.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}] |
| ev-e5a29b0f5614e339 | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml; findings[finding_id=f-12111d3e0c9420d7] | context_only | Predecessor structured review finding f-12111d3e0c9420d7 in 20261011T024638Z-mim-reconcile-all-batch-10 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-phoslactomycin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Phoslactomycin (data/ingredients/mapped/Phoslactomycin.yaml)'
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
summary: Per-record structured review for Phoslactomycin (data/ingredients/mapped/Phoslactomycin.yaml,
  record-29a7cfdfdb7dacab, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Phoslactomycin.yaml
    sha256: 668d501fc6afdf4e76ff8dfc0021a3e1351c923dae7dfa2a38e17e0c207dda7d
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
  - path: reports/yaml_record_review/Phoslactomycin.md
    sha256: fde67a41c7a821a8bcbff6842f73228a1b1c3aa27aa32bdc88d019fb35de55d5
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-29a7cfdfdb7dacab
  path: data/ingredients/mapped/Phoslactomycin.yaml
  label: Phoslactomycin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Phoslactomycin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Phoslactomycin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Phoslactomycin.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-29a7cfdfdb7dacab
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-29a7cfdfdb7dacab
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-29a7cfdfdb7dacab
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10
    and semantic review dispositions on HEAD.
  target_ids:
  - record-29a7cfdfdb7dacab
evidence:
- evidence_id: ev-bcaaeac8ab9d7cd5
  kind: record_content
  reference: data/ingredients/mapped/Phoslactomycin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1649],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:phoslactomycin","line":1651,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:phoslactomycin","preferred_term":"Phoslactomycin"}],"identifier":"kgmicrobe.compound:phoslactomycin","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:phoslactomycin","ontology_label":"Phoslactomycin","ontology_source":"kgmicrobe.compound"},"preferred_term":"Phoslactomycin","sssom_rows":[{"data_row":2245,"object_id":"kgmicrobe.compound:phoslactomycin","object_label":"Phoslactomycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Phoslactomycin","synonym_count":0}'
  snapshot_sha256: 668d501fc6afdf4e76ff8dfc0021a3e1351c923dae7dfa2a38e17e0c207dda7d
- evidence_id: ev-b81c99cfe5ec370e
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1649]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-e3e91f1660dc88ce
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Phoslactomycin; data-row positions=[2245]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2245,"object_id":"kgmicrobe.compound:phoslactomycin","object_label":"Phoslactomycin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Phoslactomycin","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-d58de164e4ad951e
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1651]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:phoslactomycin","line":1651,"mapping_quality":"PLACEHOLDER","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.compound:phoslactomycin","preferred_term":"Phoslactomycin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-cddf276c52508793
  kind: prior_review
  reference: reports/yaml_record_review/Phoslactomycin.md
  locator: '`data/ingredients/mapped/Phoslactomycin.yaml`:2; Verdict:4; Identity:10;
    Validation:21; Evidence:34; Completeness:46; Recommended Edits:53'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: fde67a41c7a821a8bcbff6842f73228a1b1c3aa27aa32bdc88d019fb35de55d5
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Phoslactomycin.yaml`,\
    \ replace\n  `physicochemical_roles.SELECTIVE_AGENT` with source-backed evidence\
    \ or remove\n  the provisional role facet until it is curated."
- evidence_id: ev-ac00b505e08006f9
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1108,1755]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"668d501fc6afdf4e76ff8dfc0021a3e1351c923dae7dfa2a38e17e0c207dda7d","finding_id":"SEM:8871918dd96afd6458f5","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"668d501fc6afdf4e76ff8dfc0021a3e1351c923dae7dfa2a38e17e0c207dda7d","finding_id":"SEM:c88ad167cfcdfb9596b7","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-8a158957bd9bf25a
  kind: record_content
  reference: data/ingredients/mapped/Phoslactomycin.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}]'
  snapshot_sha256: 668d501fc6afdf4e76ff8dfc0021a3e1351c923dae7dfa2a38e17e0c207dda7d
- evidence_id: ev-e5a29b0f5614e339
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
  locator: findings[finding_id=f-12111d3e0c9420d7]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-12111d3e0c9420d7 in 20261011T024638Z-mim-reconcile-all-batch-10
  snapshot_sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
assessments:
- assessment_id: a-d35f0fe91d892c4e
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-29a7cfdfdb7dacab
  evidence_ids:
  - ev-bcaaeac8ab9d7cd5
  - ev-b81c99cfe5ec370e
  - ev-e3e91f1660dc88ce
  - ev-d58de164e4ad951e
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-72bea31a4c179ef5
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-29a7cfdfdb7dacab
  evidence_ids:
  - ev-cddf276c52508793
  - ev-bcaaeac8ab9d7cd5
  - ev-ac00b505e08006f9
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T09:16:23Z;
    reviewed SHA-256=668d501fc6afdf4e76ff8dfc0021a3e1351c923dae7dfa2a38e17e0c207dda7d;
    current SHA-256=668d501fc6afdf4e76ff8dfc0021a3e1351c923dae7dfa2a38e17e0c207dda7d;
    hash_changed=False. Reports=["reports/yaml_record_review/Phoslactomycin.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    phoslactomycin family placeholder is intentionally retained, but SELECTIVE_AGENT
    is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-cddf276c52508793
    - ev-bcaaeac8ab9d7cd5
  - name: legacy-native-ids
    value: '["SEM:8871918dd96afd6458f5","SEM:c88ad167cfcdfb9596b7"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-bcaaeac8ab9d7cd5
    - ev-cddf276c52508793
    - ev-ac00b505e08006f9
- assessment_id: a-8a158957bd9bf25a
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-29a7cfdfdb7dacab
  evidence_ids:
  - ev-cddf276c52508793
  - ev-8a158957bd9bf25a
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-cddf276c52508793
    - ev-8a158957bd9bf25a
findings:
- finding_id: rec-f-12111d3e0c9420d7
  issue_key: mim-reconciliation-role-support-29a7cfdfdb7dacab
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Phoslactomycin'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-29a7cfdfdb7dacab
  evidence_ids:
  - ev-cddf276c52508793
  - ev-8a158957bd9bf25a
  - ev-e5a29b0f5614e339
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Phoslactomycin.yaml
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
    review_id: 20261011T024638Z-mim-reconcile-all-batch-10
    finding_id: f-12111d3e0c9420d7
actions:
- action_id: rec-action-12111d3e0c9420d7
  description: 'Reassess prediction-only role support: Phoslactomycin'
  finding_ids:
  - rec-f-12111d3e0c9420d7
  target_ids:
  - record-29a7cfdfdb7dacab
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Phoslactomycin.yaml
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
