# Per-record structured review: Vanadium_Chloride (data/ingredients/mapped/Vanadium_Chloride.yaml)

- Review: 20261017T083000Z-vanadium-chloride
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Vanadium_Chloride (data/ingredients/mapped/Vanadium_Chloride.yaml, record-83cbeeeafb19f31c, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Vanadium_Chloride.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Vanadium_Chloride.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-83cbeeeafb19f31c | data/ingredients/mapped/Vanadium_Chloride.yaml | maintained | Vanadium_Chloride |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-83cbeeeafb19f31c | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-83cbeeeafb19f31c | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-83cbeeeafb19f31c | Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-83cbeeeafb19f31c.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-83cbeeeafb19f31c.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T20:40:40Z; reviewed SHA-256=c8aea81224aa456d3adaba2c0b09192b067bb612d45878774d3d6cab981aaa36; current SHA-256=c8aea81224aa456d3adaba2c0b09192b067bb612d45878774d3d6cab981aaa36; hash_changed=False. Reports=["reports/yaml_record_review/Vanadium_Chloride.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS fallback identity passes, but TRACE_ELEMENT is still supported only by a provisional in-session LLM role assignment.

### Historical provisional-role concern

evidence: concern. Targets: record-83cbeeeafb19f31c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-2eec3e72d6f1ae90: Reassess prediction-only role support: vanadium chloride

major / open / confirmed; issue key: mim-reconciliation-role-support-83cbeeeafb19f31c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-2eec3e72d6f1ae90

Reassess prediction-only role support: vanadium chloride

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-3823e39e3b2ae5c0 | data/ingredients/mapped/Vanadium_Chloride.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2032],"raw_equal":true},"docs_rows":[{"identifier":"cas:7718-98-1","line":2034,"mapping_status":"MAPPED","ontology_id":"cas:7718-98-1","preferred_term":"vanadium chloride"}],"identifier":"cas:7718-98-1","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":26,"edge_count":26,"occurrences":26},"occurrence_statistics":{"media_count":26,"total_occurrences":26},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:7718-98-1","ontology_label":"vanadium chloride","ontology_source":"CAS"},"preferred_term":"vanadium chloride","sssom_rows":[{"data_row":2885,"object_id":"cas:7718-98-1","object_label":"vanadium chloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Vanadium_Chloride","synonym_count":0} |
| ev-1b3b3c9f07847e0e | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2032] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-a0b096cbd4f08aea | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Vanadium_Chloride; data-row positions=[2885] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2885,"object_id":"cas:7718-98-1","object_label":"vanadium chloride","other":"CAS:7718-98-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Vanadium_Chloride","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-fe762b333bfdae4e | docs/data/mapped_ingredients.csv; CSV lines=[2034] | supports | Published identity and count rows inspected: [{"identifier":"cas:7718-98-1","line":2034,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"26","ontology_id":"cas:7718-98-1","preferred_term":"vanadium chloride","total_occurrences":"26"}] |
| ev-97b0dfbb6a588be6 | reports/yaml_record_review/Vanadium_Chloride.md; &#96;data/ingredients/mapped/Vanadium_Chloride.yaml&#96;:2; Verdict:4; Identity:10; Validation:23; Evidence:32; Issues:42; Completeness:49; Recommended Edits:56 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-111efb29a0a90bc3 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1333,1841] | context_only | [{"current_record_sha256":"c8aea81224aa456d3adaba2c0b09192b067bb612d45878774d3d6cab981aaa36","finding_id":"SEM:e09a429e69270c134871","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c8aea81224aa456d3adaba2c0b09192b067bb612d45878774d3d6cab981aaa36","finding_id":"SEM:e1a40eb4d5027f0d549d","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-832e650a945d646a | data/ingredients/mapped/Vanadium_Chloride.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2032],"raw_equal":true},"docs_rows":[{"identifier":"cas:7718-98-1","line":2034,"mapping_status":"MAPPED","ontology_id":"cas:7718-98-1","preferred_term":"vanadium chloride"}],"identifier":"cas:7718-98-1","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":26,"edge_count":26,"occurrences":26},"occurrence_statistics":{"media_count":26,"total_occurrences":26},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:7718-98-1","ontology_label":"vanadium chloride","ontology_source":"CAS"},"preferred_term":"vanadium chloride","sssom_rows":[{"data_row":2885,"object_id":"cas:7718-98-1","object_label":"vanadium chloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Vanadium_Chloride","synonym_count":0} |
| ev-ebcab18be4fce7e0 | reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml; findings[finding_id=f-2eec3e72d6f1ae90] | context_only | Predecessor structured review finding f-2eec3e72d6f1ae90 in 20261011T024639Z-mim-reconcile-all-batch-12 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-vanadium-chloride
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Vanadium_Chloride (data/ingredients/mapped/Vanadium_Chloride.yaml)'
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
summary: Per-record structured review for Vanadium_Chloride (data/ingredients/mapped/Vanadium_Chloride.yaml,
  record-83cbeeeafb19f31c, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Vanadium_Chloride.yaml
    sha256: c8aea81224aa456d3adaba2c0b09192b067bb612d45878774d3d6cab981aaa36
    role: target
  - path: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
    sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
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
  - path: reports/yaml_record_review/Vanadium_Chloride.md
    sha256: 4a895319d024e8438180964d98f958376a5a18a7e1e860e07913eb54f72af47e
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-83cbeeeafb19f31c
  path: data/ingredients/mapped/Vanadium_Chloride.yaml
  label: Vanadium_Chloride
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Vanadium_Chloride.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Vanadium_Chloride.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Vanadium_Chloride.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-83cbeeeafb19f31c
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-83cbeeeafb19f31c
  evidence_ids:
  - ev-3823e39e3b2ae5c0
  - ev-1b3b3c9f07847e0e
  - ev-a0b096cbd4f08aea
  - ev-fe762b333bfdae4e
  - ev-832e650a945d646a
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-83cbeeeafb19f31c
  evidence_ids:
  - ev-3823e39e3b2ae5c0
  - ev-111efb29a0a90bc3
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12
    and semantic review dispositions on HEAD.
  target_ids:
  - record-83cbeeeafb19f31c
  evidence_ids:
  - ev-97b0dfbb6a588be6
  - ev-111efb29a0a90bc3
  - ev-ebcab18be4fce7e0
evidence:
- evidence_id: ev-3823e39e3b2ae5c0
  kind: record_content
  reference: data/ingredients/mapped/Vanadium_Chloride.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2032],"raw_equal":true},"docs_rows":[{"identifier":"cas:7718-98-1","line":2034,"mapping_status":"MAPPED","ontology_id":"cas:7718-98-1","preferred_term":"vanadium
    chloride"}],"identifier":"cas:7718-98-1","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":26,"edge_count":26,"occurrences":26},"occurrence_statistics":{"media_count":26,"total_occurrences":26},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:7718-98-1","ontology_label":"vanadium
    chloride","ontology_source":"CAS"},"preferred_term":"vanadium chloride","sssom_rows":[{"data_row":2885,"object_id":"cas:7718-98-1","object_label":"vanadium
    chloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Vanadium_Chloride","synonym_count":0}'
  snapshot_sha256: c8aea81224aa456d3adaba2c0b09192b067bb612d45878774d3d6cab981aaa36
- evidence_id: ev-1b3b3c9f07847e0e
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2032]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-a0b096cbd4f08aea
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Vanadium_Chloride; data-row positions=[2885]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2885,"object_id":"cas:7718-98-1","object_label":"vanadium
    chloride","other":"CAS:7718-98-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Vanadium_Chloride","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-fe762b333bfdae4e
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2034]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:7718-98-1","line":2034,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"26","ontology_id":"cas:7718-98-1","preferred_term":"vanadium
    chloride","total_occurrences":"26"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-97b0dfbb6a588be6
  kind: prior_review
  reference: reports/yaml_record_review/Vanadium_Chloride.md
  locator: '`data/ingredients/mapped/Vanadium_Chloride.yaml`:2; Verdict:4; Identity:10;
    Validation:23; Evidence:32; Issues:42; Completeness:49; Recommended Edits:56'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 4a895319d024e8438180964d98f958376a5a18a7e1e860e07913eb54f72af47e
  quote: "Issues:\n- Major: `nutritional_roles.TRACE_ELEMENT` rests on\n  `COMPUTATIONAL_PREDICTION`\
    \ evidence whose text is explicitly\n  `Assigned by in-session Claude reasoning\
    \ (no external API)` and whose curator\n  note calls the assignment provisional.\n\
    \nRecommended Edits:\n- Replace or remove `data/ingredients/mapped/Vanadium_Chloride.yaml`\n\
    \  `nutritional_roles.TRACE_ELEMENT`; keep it only if a maintained source\n  supports\
    \ vanadium chloride as a trace element in the specific media records\n  that use\
    \ it, then rerun strict validation and SSSOM invariant checks."
- evidence_id: ev-111efb29a0a90bc3
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1333,1841]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"c8aea81224aa456d3adaba2c0b09192b067bb612d45878774d3d6cab981aaa36","finding_id":"SEM:e09a429e69270c134871","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c8aea81224aa456d3adaba2c0b09192b067bb612d45878774d3d6cab981aaa36","finding_id":"SEM:e1a40eb4d5027f0d549d","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-832e650a945d646a
  kind: record_content
  reference: data/ingredients/mapped/Vanadium_Chloride.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2032],"raw_equal":true},"docs_rows":[{"identifier":"cas:7718-98-1","line":2034,"mapping_status":"MAPPED","ontology_id":"cas:7718-98-1","preferred_term":"vanadium
    chloride"}],"identifier":"cas:7718-98-1","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":26,"edge_count":26,"occurrences":26},"occurrence_statistics":{"media_count":26,"total_occurrences":26},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:7718-98-1","ontology_label":"vanadium
    chloride","ontology_source":"CAS"},"preferred_term":"vanadium chloride","sssom_rows":[{"data_row":2885,"object_id":"cas:7718-98-1","object_label":"vanadium
    chloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Vanadium_Chloride","synonym_count":0}'
  snapshot_sha256: c8aea81224aa456d3adaba2c0b09192b067bb612d45878774d3d6cab981aaa36
- evidence_id: ev-ebcab18be4fce7e0
  kind: prior_review
  reference: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
  locator: findings[finding_id=f-2eec3e72d6f1ae90]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-2eec3e72d6f1ae90 in 20261011T024639Z-mim-reconcile-all-batch-12
  snapshot_sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
assessments:
- assessment_id: a-c54385aabd267dd6
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-83cbeeeafb19f31c
  evidence_ids:
  - ev-3823e39e3b2ae5c0
  - ev-1b3b3c9f07847e0e
  - ev-a0b096cbd4f08aea
  - ev-fe762b333bfdae4e
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-464fc3b6042b5b89
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-83cbeeeafb19f31c
  evidence_ids:
  - ev-97b0dfbb6a588be6
  - ev-3823e39e3b2ae5c0
  - ev-111efb29a0a90bc3
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T20:40:40Z;
    reviewed SHA-256=c8aea81224aa456d3adaba2c0b09192b067bb612d45878774d3d6cab981aaa36;
    current SHA-256=c8aea81224aa456d3adaba2c0b09192b067bb612d45878774d3d6cab981aaa36;
    hash_changed=False. Reports=["reports/yaml_record_review/Vanadium_Chloride.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS
    fallback identity passes, but TRACE_ELEMENT is still supported only by a provisional
    in-session LLM role assignment.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-97b0dfbb6a588be6
    - ev-3823e39e3b2ae5c0
  - name: legacy-native-ids
    value: '["SEM:e09a429e69270c134871","SEM:e1a40eb4d5027f0d549d"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-3823e39e3b2ae5c0
    - ev-97b0dfbb6a588be6
    - ev-111efb29a0a90bc3
- assessment_id: a-832e650a945d646a
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-83cbeeeafb19f31c
  evidence_ids:
  - ev-97b0dfbb6a588be6
  - ev-832e650a945d646a
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-97b0dfbb6a588be6
    - ev-832e650a945d646a
findings:
- finding_id: rec-f-2eec3e72d6f1ae90
  issue_key: mim-reconciliation-role-support-83cbeeeafb19f31c
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: vanadium chloride'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-83cbeeeafb19f31c
  evidence_ids:
  - ev-97b0dfbb6a588be6
  - ev-832e650a945d646a
  - ev-ebcab18be4fce7e0
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Vanadium_Chloride.yaml
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
    review_id: 20261011T024639Z-mim-reconcile-all-batch-12
    finding_id: f-2eec3e72d6f1ae90
actions:
- action_id: rec-action-2eec3e72d6f1ae90
  description: 'Reassess prediction-only role support: vanadium chloride'
  finding_ids:
  - rec-f-2eec3e72d6f1ae90
  target_ids:
  - record-83cbeeeafb19f31c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Vanadium_Chloride.yaml
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
  with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.
```
