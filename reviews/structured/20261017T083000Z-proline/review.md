# Per-record structured review: Proline (data/ingredients/mapped/Proline.yaml)

- Review: 20261017T083000Z-proline
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Proline (data/ingredients/mapped/Proline.yaml, record-d28ecde607a30883, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Proline.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Proline.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-d28ecde607a30883 | data/ingredients/mapped/Proline.yaml | maintained | Proline |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-d28ecde607a30883 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-d28ecde607a30883 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-d28ecde607a30883 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-d28ecde607a30883.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-d28ecde607a30883.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T10:34:32Z; reviewed SHA-256=3e61bdcb6aaa68b6f0d188489811526edd438ec7ccab6574a601effa9dd62df2; current SHA-256=3e61bdcb6aaa68b6f0d188489811526edd438ec7ccab6574a601effa9dd62df2; hash_changed=False. Reports=["reports/yaml_record_review/Proline.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact generic CHEBI:26271 identity passes, but CAS 147-85-3 belongs to L-proline and the amino-acid-source role is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-d28ecde607a30883.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-b6d5b07a54baa8c5: Reassess prediction-only role support: Proline

major / open / confirmed; issue key: mim-reconciliation-role-support-d28ecde607a30883.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-b6d5b07a54baa8c5

Reassess prediction-only role support: Proline

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-7ee4fe28defc52cd | data/ingredients/mapped/Proline.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1703],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:26271","line":1705,"mapping_status":"MAPPED","ontology_id":"CHEBI:26271","preferred_term":"Proline"}],"identifier":"CHEBI:26271","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":23,"edge_count":23,"occurrences":23},"occurrence_statistics":{"media_count":23,"total_occurrences":23},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:26271","ontology_label":"proline","ontology_source":"CHEBI"},"preferred_term":"Proline","sssom_rows":[{"data_row":2349,"object_id":"CHEBI:26271","object_label":"proline","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Proline","synonym_count":5} |
| ev-f4335f2587805402 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1703] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-cc39dec962638095 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Proline; data-row positions=[2349] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2349,"object_id":"CHEBI:26271","object_label":"proline","other":"DL-Proline&#124;Hpro&#124;Prolin&#124;pyrrolidine-2-carboxylic acid&#124;CAS:147-85-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Proline","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-2dc32a5fc695cc6a | docs/data/mapped_ingredients.csv; CSV lines=[1705] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:26271","line":1705,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"23","ontology_id":"CHEBI:26271","preferred_term":"Proline","total_occurrences":"23"}] |
| ev-b3422fe6d9b3bcdd | reports/yaml_record_review/Proline.md; &#96;data/ingredients/mapped/Proline.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-9b8552457dd380d5 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1142,2062] | context_only | [{"current_record_sha256":"3e61bdcb6aaa68b6f0d188489811526edd438ec7ccab6574a601effa9dd62df2","finding_id":"SEM:cec36a2b0d65c36229dd","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"3e61bdcb6aaa68b6f0d188489811526edd438ec7ccab6574a601effa9dd62df2","finding_id":"SEM:504547479707c0e2cde0","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-a4216c54632988ff | data/ingredients/mapped/Proline.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1703],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:26271","line":1705,"mapping_status":"MAPPED","ontology_id":"CHEBI:26271","preferred_term":"Proline"}],"identifier":"CHEBI:26271","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":23,"edge_count":23,"occurrences":23},"occurrence_statistics":{"media_count":23,"total_occurrences":23},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:26271","ontology_label":"proline","ontology_source":"CHEBI"},"preferred_term":"Proline","sssom_rows":[{"data_row":2349,"object_id":"CHEBI:26271","object_label":"proline","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Proline","synonym_count":5} |
| ev-e2acb5b8c7f6cb0f | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml; findings[finding_id=f-b6d5b07a54baa8c5] | context_only | Predecessor structured review finding f-b6d5b07a54baa8c5 in 20261011T024638Z-mim-reconcile-all-batch-10 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-proline
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Proline (data/ingredients/mapped/Proline.yaml)'
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
summary: Per-record structured review for Proline (data/ingredients/mapped/Proline.yaml,
  record-d28ecde607a30883, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Proline.yaml
    sha256: 3e61bdcb6aaa68b6f0d188489811526edd438ec7ccab6574a601effa9dd62df2
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
  - path: reports/yaml_record_review/Proline.md
    sha256: a6528566f3c0f6cc8296f0c7b0e5426e173ce349618f8f68b108a3823e87d9d3
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-d28ecde607a30883
  path: data/ingredients/mapped/Proline.yaml
  label: Proline
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Proline.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Proline.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Proline.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-d28ecde607a30883
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-d28ecde607a30883
  evidence_ids:
  - ev-7ee4fe28defc52cd
  - ev-f4335f2587805402
  - ev-cc39dec962638095
  - ev-2dc32a5fc695cc6a
  - ev-a4216c54632988ff
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-d28ecde607a30883
  evidence_ids:
  - ev-7ee4fe28defc52cd
  - ev-9b8552457dd380d5
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10
    and semantic review dispositions on HEAD.
  target_ids:
  - record-d28ecde607a30883
  evidence_ids:
  - ev-b3422fe6d9b3bcdd
  - ev-9b8552457dd380d5
  - ev-e2acb5b8c7f6cb0f
evidence:
- evidence_id: ev-7ee4fe28defc52cd
  kind: record_content
  reference: data/ingredients/mapped/Proline.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1703],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:26271","line":1705,"mapping_status":"MAPPED","ontology_id":"CHEBI:26271","preferred_term":"Proline"}],"identifier":"CHEBI:26271","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":23,"edge_count":23,"occurrences":23},"occurrence_statistics":{"media_count":23,"total_occurrences":23},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:26271","ontology_label":"proline","ontology_source":"CHEBI"},"preferred_term":"Proline","sssom_rows":[{"data_row":2349,"object_id":"CHEBI:26271","object_label":"proline","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Proline","synonym_count":5}'
  snapshot_sha256: 3e61bdcb6aaa68b6f0d188489811526edd438ec7ccab6574a601effa9dd62df2
- evidence_id: ev-f4335f2587805402
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1703]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-cc39dec962638095
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Proline; data-row positions=[2349]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2349,"object_id":"CHEBI:26271","object_label":"proline","other":"DL-Proline|Hpro|Prolin|pyrrolidine-2-carboxylic
    acid|CAS:147-85-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Proline","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-2dc32a5fc695cc6a
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1705]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:26271","line":1705,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"23","ontology_id":"CHEBI:26271","preferred_term":"Proline","total_occurrences":"23"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-b3422fe6d9b3bcdd
  kind: prior_review
  reference: reports/yaml_record_review/Proline.md
  locator: '`data/ingredients/mapped/Proline.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: a6528566f3c0f6cc8296f0c7b0e5426e173ce349618f8f68b108a3823e87d9d3
- evidence_id: ev-9b8552457dd380d5
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1142,2062]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"3e61bdcb6aaa68b6f0d188489811526edd438ec7ccab6574a601effa9dd62df2","finding_id":"SEM:cec36a2b0d65c36229dd","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"3e61bdcb6aaa68b6f0d188489811526edd438ec7ccab6574a601effa9dd62df2","finding_id":"SEM:504547479707c0e2cde0","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-a4216c54632988ff
  kind: record_content
  reference: data/ingredients/mapped/Proline.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1703],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:26271","line":1705,"mapping_status":"MAPPED","ontology_id":"CHEBI:26271","preferred_term":"Proline"}],"identifier":"CHEBI:26271","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":23,"edge_count":23,"occurrences":23},"occurrence_statistics":{"media_count":23,"total_occurrences":23},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:26271","ontology_label":"proline","ontology_source":"CHEBI"},"preferred_term":"Proline","sssom_rows":[{"data_row":2349,"object_id":"CHEBI:26271","object_label":"proline","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Proline","synonym_count":5}'
  snapshot_sha256: 3e61bdcb6aaa68b6f0d188489811526edd438ec7ccab6574a601effa9dd62df2
- evidence_id: ev-e2acb5b8c7f6cb0f
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
  locator: findings[finding_id=f-b6d5b07a54baa8c5]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-b6d5b07a54baa8c5 in 20261011T024638Z-mim-reconcile-all-batch-10
  snapshot_sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
assessments:
- assessment_id: a-d98a563066af2b2e
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-d28ecde607a30883
  evidence_ids:
  - ev-7ee4fe28defc52cd
  - ev-f4335f2587805402
  - ev-cc39dec962638095
  - ev-2dc32a5fc695cc6a
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-51016130f4218b1e
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d28ecde607a30883
  evidence_ids:
  - ev-b3422fe6d9b3bcdd
  - ev-7ee4fe28defc52cd
  - ev-9b8552457dd380d5
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T10:34:32Z;
    reviewed SHA-256=3e61bdcb6aaa68b6f0d188489811526edd438ec7ccab6574a601effa9dd62df2;
    current SHA-256=3e61bdcb6aaa68b6f0d188489811526edd438ec7ccab6574a601effa9dd62df2;
    hash_changed=False. Reports=["reports/yaml_record_review/Proline.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact generic CHEBI:26271
    identity passes, but CAS 147-85-3 belongs to L-proline and the amino-acid-source
    role is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b3422fe6d9b3bcdd
    - ev-7ee4fe28defc52cd
  - name: legacy-native-ids
    value: '["SEM:cec36a2b0d65c36229dd","SEM:504547479707c0e2cde0"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-7ee4fe28defc52cd
    - ev-b3422fe6d9b3bcdd
    - ev-9b8552457dd380d5
- assessment_id: a-a4216c54632988ff
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-d28ecde607a30883
  evidence_ids:
  - ev-b3422fe6d9b3bcdd
  - ev-a4216c54632988ff
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b3422fe6d9b3bcdd
    - ev-a4216c54632988ff
findings:
- finding_id: rec-f-b6d5b07a54baa8c5
  issue_key: mim-reconciliation-role-support-d28ecde607a30883
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Proline'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-d28ecde607a30883
  evidence_ids:
  - ev-b3422fe6d9b3bcdd
  - ev-a4216c54632988ff
  - ev-e2acb5b8c7f6cb0f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Proline.yaml
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
    finding_id: f-b6d5b07a54baa8c5
actions:
- action_id: rec-action-b6d5b07a54baa8c5
  description: 'Reassess prediction-only role support: Proline'
  finding_ids:
  - rec-f-b6d5b07a54baa8c5
  target_ids:
  - record-d28ecde607a30883
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Proline.yaml
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
