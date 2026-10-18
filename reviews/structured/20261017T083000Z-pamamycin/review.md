# Per-record structured review: Pamamycin (data/ingredients/mapped/Pamamycin.yaml)

- Review: 20261017T083000Z-pamamycin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Pamamycin (data/ingredients/mapped/Pamamycin.yaml, record-7e54869d5ab14d94, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Pamamycin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Pamamycin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-7e54869d5ab14d94 | data/ingredients/mapped/Pamamycin.yaml | maintained | Pamamycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-7e54869d5ab14d94 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-7e54869d5ab14d94 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-7e54869d5ab14d94 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-7e54869d5ab14d94.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-7e54869d5ab14d94.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T08:34:11Z; reviewed SHA-256=475300bb7e677226a9b74e2b945bc34cf086d0a3bd0e72c465e27293c79a4afe; current SHA-256=475300bb7e677226a9b74e2b945bc34cf086d0a3bd0e72c465e27293c79a4afe; hash_changed=False. Reports=["reports/yaml_record_review/Pamamycin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact mesh:C024500 identity passes, but SELECTIVE_AGENT is only provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-7e54869d5ab14d94.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-e95241fbe3c6ef28: Reassess prediction-only role support: Pamamycin

major / open / confirmed; issue key: mim-reconciliation-role-support-7e54869d5ab14d94.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-e95241fbe3c6ef28

Reassess prediction-only role support: Pamamycin

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-40ca2133c57c227c | data/ingredients/mapped/Pamamycin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1613],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C024500","line":1615,"mapping_status":"MAPPED","ontology_id":"mesh:C024500","preferred_term":"Pamamycin"}],"identifier":"mesh:C024500","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C024500","ontology_label":"pamamycin","ontology_source":"MESH"},"preferred_term":"Pamamycin","sssom_rows":[{"data_row":2197,"object_id":"mesh:C024500","object_label":"pamamycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Pamamycin","synonym_count":0} |
| ev-ef4fb6f72667ff6f | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1613] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-dd8d54c2c7fcffce | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Pamamycin; data-row positions=[2197] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2197,"object_id":"mesh:C024500","object_label":"pamamycin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Pamamycin","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-78d247481d063a15 | docs/data/mapped_ingredients.csv; CSV lines=[1615] | supports | Published identity and count rows inspected: [{"identifier":"mesh:C024500","line":1615,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C024500","preferred_term":"Pamamycin","total_occurrences":"0"}] |
| ev-7c00f2b18978da73 | reports/yaml_record_review/Pamamycin.md; &#96;data/ingredients/mapped/Pamamycin.yaml&#96;:2; Verdict:4; Identity:10; Validation:19; Evidence:29; Completeness:43; Recommended Edits:50 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-ff1427fe14f44339 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1095,1491] | context_only | [{"current_record_sha256":"475300bb7e677226a9b74e2b945bc34cf086d0a3bd0e72c465e27293c79a4afe","finding_id":"SEM:c1d0cf66f793e62c2aab","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"475300bb7e677226a9b74e2b945bc34cf086d0a3bd0e72c465e27293c79a4afe","finding_id":"SEM:326c0c6d6bfa914780c4","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-91005b3296d29741 | data/ingredients/mapped/Pamamycin.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1613],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C024500","line":1615,"mapping_status":"MAPPED","ontology_id":"mesh:C024500","preferred_term":"Pamamycin"}],"identifier":"mesh:C024500","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C024500","ontology_label":"pamamycin","ontology_source":"MESH"},"preferred_term":"Pamamycin","sssom_rows":[{"data_row":2197,"object_id":"mesh:C024500","object_label":"pamamycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Pamamycin","synonym_count":0} |
| ev-8ffea020c36e3650 | reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml; findings[finding_id=f-e95241fbe3c6ef28] | context_only | Predecessor structured review finding f-e95241fbe3c6ef28 in 20261011T024637Z-mim-reconcile-all-batch-09 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-pamamycin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Pamamycin (data/ingredients/mapped/Pamamycin.yaml)'
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
summary: Per-record structured review for Pamamycin (data/ingredients/mapped/Pamamycin.yaml,
  record-7e54869d5ab14d94, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Pamamycin.yaml
    sha256: 475300bb7e677226a9b74e2b945bc34cf086d0a3bd0e72c465e27293c79a4afe
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
  - path: reports/yaml_record_review/Pamamycin.md
    sha256: 038b32580b957af1b89bbfb65569ec5e45ccb2a19f2a78e54f6b9fb1dbb6d0d9
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-7e54869d5ab14d94
  path: data/ingredients/mapped/Pamamycin.yaml
  label: Pamamycin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Pamamycin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Pamamycin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Pamamycin.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-7e54869d5ab14d94
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-7e54869d5ab14d94
  evidence_ids:
  - ev-40ca2133c57c227c
  - ev-ef4fb6f72667ff6f
  - ev-dd8d54c2c7fcffce
  - ev-78d247481d063a15
  - ev-91005b3296d29741
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-7e54869d5ab14d94
  evidence_ids:
  - ev-40ca2133c57c227c
  - ev-ff1427fe14f44339
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-7e54869d5ab14d94
  evidence_ids:
  - ev-7c00f2b18978da73
  - ev-ff1427fe14f44339
  - ev-8ffea020c36e3650
evidence:
- evidence_id: ev-40ca2133c57c227c
  kind: record_content
  reference: data/ingredients/mapped/Pamamycin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1613],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C024500","line":1615,"mapping_status":"MAPPED","ontology_id":"mesh:C024500","preferred_term":"Pamamycin"}],"identifier":"mesh:C024500","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C024500","ontology_label":"pamamycin","ontology_source":"MESH"},"preferred_term":"Pamamycin","sssom_rows":[{"data_row":2197,"object_id":"mesh:C024500","object_label":"pamamycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Pamamycin","synonym_count":0}'
  snapshot_sha256: 475300bb7e677226a9b74e2b945bc34cf086d0a3bd0e72c465e27293c79a4afe
- evidence_id: ev-ef4fb6f72667ff6f
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1613]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-dd8d54c2c7fcffce
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Pamamycin; data-row positions=[2197]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2197,"object_id":"mesh:C024500","object_label":"pamamycin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Pamamycin","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-78d247481d063a15
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1615]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"mesh:C024500","line":1615,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C024500","preferred_term":"Pamamycin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-7c00f2b18978da73
  kind: prior_review
  reference: reports/yaml_record_review/Pamamycin.md
  locator: '`data/ingredients/mapped/Pamamycin.yaml`:2; Verdict:4; Identity:10; Validation:19;
    Evidence:29; Completeness:43; Recommended Edits:50'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 038b32580b957af1b89bbfb65569ec5e45ccb2a19f2a78e54f6b9fb1dbb6d0d9
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Pamamycin.yaml`,\
    \ either replace\n  `physicochemical_roles.SELECTIVE_AGENT` with cited source\
    \ evidence that\n  supports the selective-agent role for pamamycin, or remove\
    \ the provisional\n  role facet until source-backed role evidence is curated."
- evidence_id: ev-ff1427fe14f44339
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1095,1491]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"475300bb7e677226a9b74e2b945bc34cf086d0a3bd0e72c465e27293c79a4afe","finding_id":"SEM:c1d0cf66f793e62c2aab","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"475300bb7e677226a9b74e2b945bc34cf086d0a3bd0e72c465e27293c79a4afe","finding_id":"SEM:326c0c6d6bfa914780c4","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-91005b3296d29741
  kind: record_content
  reference: data/ingredients/mapped/Pamamycin.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1613],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C024500","line":1615,"mapping_status":"MAPPED","ontology_id":"mesh:C024500","preferred_term":"Pamamycin"}],"identifier":"mesh:C024500","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C024500","ontology_label":"pamamycin","ontology_source":"MESH"},"preferred_term":"Pamamycin","sssom_rows":[{"data_row":2197,"object_id":"mesh:C024500","object_label":"pamamycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Pamamycin","synonym_count":0}'
  snapshot_sha256: 475300bb7e677226a9b74e2b945bc34cf086d0a3bd0e72c465e27293c79a4afe
- evidence_id: ev-8ffea020c36e3650
  kind: prior_review
  reference: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
  locator: findings[finding_id=f-e95241fbe3c6ef28]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-e95241fbe3c6ef28 in 20261011T024637Z-mim-reconcile-all-batch-09
  snapshot_sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
assessments:
- assessment_id: a-5670ecac267fdb07
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-7e54869d5ab14d94
  evidence_ids:
  - ev-40ca2133c57c227c
  - ev-ef4fb6f72667ff6f
  - ev-dd8d54c2c7fcffce
  - ev-78d247481d063a15
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-650faa1a18c93a8c
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-7e54869d5ab14d94
  evidence_ids:
  - ev-7c00f2b18978da73
  - ev-40ca2133c57c227c
  - ev-ff1427fe14f44339
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T08:34:11Z;
    reviewed SHA-256=475300bb7e677226a9b74e2b945bc34cf086d0a3bd0e72c465e27293c79a4afe;
    current SHA-256=475300bb7e677226a9b74e2b945bc34cf086d0a3bd0e72c465e27293c79a4afe;
    hash_changed=False. Reports=["reports/yaml_record_review/Pamamycin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact mesh:C024500
    identity passes, but SELECTIVE_AGENT is only provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-7c00f2b18978da73
    - ev-40ca2133c57c227c
  - name: legacy-native-ids
    value: '["SEM:c1d0cf66f793e62c2aab","SEM:326c0c6d6bfa914780c4"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-40ca2133c57c227c
    - ev-7c00f2b18978da73
    - ev-ff1427fe14f44339
- assessment_id: a-91005b3296d29741
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-7e54869d5ab14d94
  evidence_ids:
  - ev-7c00f2b18978da73
  - ev-91005b3296d29741
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-7c00f2b18978da73
    - ev-91005b3296d29741
findings:
- finding_id: rec-f-e95241fbe3c6ef28
  issue_key: mim-reconciliation-role-support-7e54869d5ab14d94
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Pamamycin'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-7e54869d5ab14d94
  evidence_ids:
  - ev-7c00f2b18978da73
  - ev-91005b3296d29741
  - ev-8ffea020c36e3650
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Pamamycin.yaml
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
    review_id: 20261011T024637Z-mim-reconcile-all-batch-09
    finding_id: f-e95241fbe3c6ef28
actions:
- action_id: rec-action-e95241fbe3c6ef28
  description: 'Reassess prediction-only role support: Pamamycin'
  finding_ids:
  - rec-f-e95241fbe3c6ef28
  target_ids:
  - record-7e54869d5ab14d94
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Pamamycin.yaml
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
