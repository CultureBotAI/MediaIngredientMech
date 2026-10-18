# Per-record structured review: Inulin (data/ingredients/mapped/Inulin.yaml)

- Review: 20261017T083000Z-inulin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Inulin (data/ingredients/mapped/Inulin.yaml, record-393cf62724662d82, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Inulin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Inulin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-393cf62724662d82 | data/ingredients/mapped/Inulin.yaml | maintained | Inulin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-393cf62724662d82 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-393cf62724662d82 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-393cf62724662d82 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-393cf62724662d82.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-393cf62724662d82.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T20:30:52Z; reviewed SHA-256=2ee73a4aae9ba1f5f7bf8bfc046171e1de70f5b9de61aec5afd4b930090f43de; current SHA-256=2ee73a4aae9ba1f5f7bf8bfc046171e1de70f5b9de61aec5afd4b930090f43de; hash_changed=False. Reports=["reports/yaml_record_review/Inulin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact inulin identity and final SSSOM row pass, but CARBON_SOURCE is only a provisional ChEBI-ancestry assertion.

### Historical provisional-role concern

evidence: concern. Targets: record-393cf62724662d82.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-1b45e466bbb83756: Reassess prediction-only role support: Inulin

major / open / confirmed; issue key: mim-reconciliation-role-support-393cf62724662d82.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-1b45e466bbb83756

Reassess prediction-only role support: Inulin

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-dbdf3baeedf886b4 | data/ingredients/mapped/Inulin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1165],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15443","line":1167,"mapping_status":"MAPPED","ontology_id":"CHEBI:15443","preferred_term":"Inulin"}],"identifier":"CHEBI:15443","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15443","ontology_label":"inulin","ontology_source":"CHEBI"},"preferred_term":"Inulin","sssom_rows":[{"data_row":1489,"object_id":"CHEBI:15443","object_label":"inulin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Inulin","synonym_count":3} |
| ev-f52c124dbd93fe6d | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1165] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-3ef06e39fb8706a7 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Inulin; data-row positions=[1489] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1489,"object_id":"CHEBI:15443","object_label":"inulin","other":"(2,1-beta-D-Fructosyl)n&#124;(2-&gt;1)-beta-D-fructofuranan&#124;CAS:9005-80-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Inulin","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-da4ed7b20cd65ef7 | docs/data/mapped_ingredients.csv; CSV lines=[1167] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:15443","line":1167,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"5","ontology_id":"CHEBI:15443","preferred_term":"Inulin","total_occurrences":"5"}] |
| ev-1717eede458fbb8a | reports/yaml_record_review/Inulin.md; &#96;data/ingredients/mapped/Inulin.yaml&#96;:2; Verdict:4; Identity:10; Validation:19; Evidence:30; Completeness:49; Recommended Edits:56 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-a52ccf62fb7461e8 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[750,1805] | context_only | [{"current_record_sha256":"2ee73a4aae9ba1f5f7bf8bfc046171e1de70f5b9de61aec5afd4b930090f43de","finding_id":"SEM:9459ff9932b816fbe04a","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"2ee73a4aae9ba1f5f7bf8bfc046171e1de70f5b9de61aec5afd4b930090f43de","finding_id":"SEM:abf53e73e2696a61b84b","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-f48d80720f402ad6 | data/ingredients/mapped/Inulin.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1165],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15443","line":1167,"mapping_status":"MAPPED","ontology_id":"CHEBI:15443","preferred_term":"Inulin"}],"identifier":"CHEBI:15443","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15443","ontology_label":"inulin","ontology_source":"CHEBI"},"preferred_term":"Inulin","sssom_rows":[{"data_row":1489,"object_id":"CHEBI:15443","object_label":"inulin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Inulin","synonym_count":3} |
| ev-fb276b84252958e1 | reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml; findings[finding_id=f-1b45e466bbb83756] | context_only | Predecessor structured review finding f-1b45e466bbb83756 in 20261011T024635Z-mim-reconcile-all-batch-07 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-inulin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Inulin (data/ingredients/mapped/Inulin.yaml)'
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
summary: Per-record structured review for Inulin (data/ingredients/mapped/Inulin.yaml,
  record-393cf62724662d82, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Inulin.yaml
    sha256: 2ee73a4aae9ba1f5f7bf8bfc046171e1de70f5b9de61aec5afd4b930090f43de
    role: target
  - path: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
    sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
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
  - path: reports/yaml_record_review/Inulin.md
    sha256: 10c19c310d1847b25eed32b155a448b73ac732fc48a15460405a0c1f3dd7f161
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-393cf62724662d82
  path: data/ingredients/mapped/Inulin.yaml
  label: Inulin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Inulin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Inulin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Inulin.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-393cf62724662d82
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-393cf62724662d82
  evidence_ids:
  - ev-dbdf3baeedf886b4
  - ev-f52c124dbd93fe6d
  - ev-3ef06e39fb8706a7
  - ev-da4ed7b20cd65ef7
  - ev-f48d80720f402ad6
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-393cf62724662d82
  evidence_ids:
  - ev-dbdf3baeedf886b4
  - ev-a52ccf62fb7461e8
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-393cf62724662d82
  evidence_ids:
  - ev-1717eede458fbb8a
  - ev-a52ccf62fb7461e8
  - ev-fb276b84252958e1
evidence:
- evidence_id: ev-dbdf3baeedf886b4
  kind: record_content
  reference: data/ingredients/mapped/Inulin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1165],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15443","line":1167,"mapping_status":"MAPPED","ontology_id":"CHEBI:15443","preferred_term":"Inulin"}],"identifier":"CHEBI:15443","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15443","ontology_label":"inulin","ontology_source":"CHEBI"},"preferred_term":"Inulin","sssom_rows":[{"data_row":1489,"object_id":"CHEBI:15443","object_label":"inulin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Inulin","synonym_count":3}'
  snapshot_sha256: 2ee73a4aae9ba1f5f7bf8bfc046171e1de70f5b9de61aec5afd4b930090f43de
- evidence_id: ev-f52c124dbd93fe6d
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1165]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-3ef06e39fb8706a7
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Inulin; data-row positions=[1489]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1489,"object_id":"CHEBI:15443","object_label":"inulin","other":"(2,1-beta-D-Fructosyl)n|(2->1)-beta-D-fructofuranan|CAS:9005-80-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Inulin","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-da4ed7b20cd65ef7
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1167]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:15443","line":1167,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"5","ontology_id":"CHEBI:15443","preferred_term":"Inulin","total_occurrences":"5"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-1717eede458fbb8a
  kind: prior_review
  reference: reports/yaml_record_review/Inulin.md
  locator: '`data/ingredients/mapped/Inulin.yaml`:2; Verdict:4; Identity:10; Validation:19;
    Evidence:30; Completeness:49; Recommended Edits:56'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 10c19c310d1847b25eed32b155a448b73ac732fc48a15460405a0c1f3dd7f161
  quote: "Recommended Edits:\n- Major: remove `nutritional_roles.CARBON_SOURCE` unless\
    \ an inspected\n  CultureMech, FEBA, Hans80, or literature source can support\
    \ inulin as a\n  carbon source, then rerun strict, term, round-trip, id-label,\
    \ component, and\n  SSSOM validation."
- evidence_id: ev-a52ccf62fb7461e8
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[750,1805]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"2ee73a4aae9ba1f5f7bf8bfc046171e1de70f5b9de61aec5afd4b930090f43de","finding_id":"SEM:9459ff9932b816fbe04a","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"2ee73a4aae9ba1f5f7bf8bfc046171e1de70f5b9de61aec5afd4b930090f43de","finding_id":"SEM:abf53e73e2696a61b84b","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-f48d80720f402ad6
  kind: record_content
  reference: data/ingredients/mapped/Inulin.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1165],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15443","line":1167,"mapping_status":"MAPPED","ontology_id":"CHEBI:15443","preferred_term":"Inulin"}],"identifier":"CHEBI:15443","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15443","ontology_label":"inulin","ontology_source":"CHEBI"},"preferred_term":"Inulin","sssom_rows":[{"data_row":1489,"object_id":"CHEBI:15443","object_label":"inulin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Inulin","synonym_count":3}'
  snapshot_sha256: 2ee73a4aae9ba1f5f7bf8bfc046171e1de70f5b9de61aec5afd4b930090f43de
- evidence_id: ev-fb276b84252958e1
  kind: prior_review
  reference: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
  locator: findings[finding_id=f-1b45e466bbb83756]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-1b45e466bbb83756 in 20261011T024635Z-mim-reconcile-all-batch-07
  snapshot_sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
assessments:
- assessment_id: a-90b172f1b9d169d6
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-393cf62724662d82
  evidence_ids:
  - ev-dbdf3baeedf886b4
  - ev-f52c124dbd93fe6d
  - ev-3ef06e39fb8706a7
  - ev-da4ed7b20cd65ef7
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-28bea8a8d08bf03d
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-393cf62724662d82
  evidence_ids:
  - ev-1717eede458fbb8a
  - ev-dbdf3baeedf886b4
  - ev-a52ccf62fb7461e8
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T20:30:52Z;
    reviewed SHA-256=2ee73a4aae9ba1f5f7bf8bfc046171e1de70f5b9de61aec5afd4b930090f43de;
    current SHA-256=2ee73a4aae9ba1f5f7bf8bfc046171e1de70f5b9de61aec5afd4b930090f43de;
    hash_changed=False. Reports=["reports/yaml_record_review/Inulin.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact inulin identity
    and final SSSOM row pass, but CARBON_SOURCE is only a provisional ChEBI-ancestry
    assertion.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-1717eede458fbb8a
    - ev-dbdf3baeedf886b4
  - name: legacy-native-ids
    value: '["SEM:9459ff9932b816fbe04a","SEM:abf53e73e2696a61b84b"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-dbdf3baeedf886b4
    - ev-1717eede458fbb8a
    - ev-a52ccf62fb7461e8
- assessment_id: a-f48d80720f402ad6
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-393cf62724662d82
  evidence_ids:
  - ev-1717eede458fbb8a
  - ev-f48d80720f402ad6
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-1717eede458fbb8a
    - ev-f48d80720f402ad6
findings:
- finding_id: rec-f-1b45e466bbb83756
  issue_key: mim-reconciliation-role-support-393cf62724662d82
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Inulin'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-393cf62724662d82
  evidence_ids:
  - ev-1717eede458fbb8a
  - ev-f48d80720f402ad6
  - ev-fb276b84252958e1
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Inulin.yaml
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
    review_id: 20261011T024635Z-mim-reconcile-all-batch-07
    finding_id: f-1b45e466bbb83756
actions:
- action_id: rec-action-1b45e466bbb83756
  description: 'Reassess prediction-only role support: Inulin'
  finding_ids:
  - rec-f-1b45e466bbb83756
  target_ids:
  - record-393cf62724662d82
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Inulin.yaml
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
  with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.
```
