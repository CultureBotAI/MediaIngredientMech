# Per-record structured review: Geomycin (data/ingredients/mapped/Geomycin.yaml)

- Review: 20261017T083000Z-geomycin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Geomycin (data/ingredients/mapped/Geomycin.yaml, record-7792bc0c82f05e91, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Geomycin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Geomycin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-7792bc0c82f05e91 | data/ingredients/mapped/Geomycin.yaml | maintained | Geomycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-7792bc0c82f05e91 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-7792bc0c82f05e91 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-7792bc0c82f05e91 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-7792bc0c82f05e91.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-7792bc0c82f05e91.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:38:04Z; reviewed SHA-256=fa269060e6ebc77f8c8bdf474dbae2432967d180e859387780789a8268d19bda; current SHA-256=fa269060e6ebc77f8c8bdf474dbae2432967d180e859387780789a8268d19bda; hash_changed=False. Reports=["reports/yaml_record_review/Geomycin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact MeSH synonym identity passes through external-prefix OLS validation, but SELECTIVE_AGENT is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-7792bc0c82f05e91.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-0d87a92810020171: Reassess prediction-only role support: Geomycin

major / open / confirmed; issue key: mim-reconciliation-role-support-7792bc0c82f05e91.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-0d87a92810020171

Reassess prediction-only role support: Geomycin

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-1b470d2f08205155 | data/ingredients/mapped/Geomycin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1049],"raw_equal":true},"docs_rows":[{"identifier":"mesh:D010118","line":1051,"mapping_status":"MAPPED","ontology_id":"mesh:D010118","preferred_term":"Geomycin"}],"identifier":"mesh:D010118","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:D010118","ontology_label":"Oxytetracycline","ontology_source":"MESH"},"preferred_term":"Geomycin","sssom_rows":[{"data_row":1294,"object_id":"mesh:D010118","object_label":"Oxytetracycline","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Geomycin","synonym_count":0} |
| ev-0496cea978282ccb | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1049] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-e838aca40bd9fc3f | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Geomycin; data-row positions=[1294] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1294,"object_id":"mesh:D010118","object_label":"Oxytetracycline","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Geomycin","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-0dbb6a0865c87790 | docs/data/mapped_ingredients.csv; CSV lines=[1051] | supports | Published identity and count rows inspected: [{"identifier":"mesh:D010118","line":1051,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:D010118","preferred_term":"Geomycin","total_occurrences":"0"}] |
| ev-ef4f4ff5e6f66949 | reports/yaml_record_review/Geomycin.md; &#96;data/ingredients/mapped/Geomycin.yaml&#96;:2; Verdict:4; Identity:11; Validation:23; Evidence:38; Completeness:58; Recommended Edits:64 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-23932eee9463388f | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[660,1854] | context_only | [{"current_record_sha256":"fa269060e6ebc77f8c8bdf474dbae2432967d180e859387780789a8268d19bda","finding_id":"SEM:fb3a6cf37e8dbcdd7633","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"fa269060e6ebc77f8c8bdf474dbae2432967d180e859387780789a8268d19bda","finding_id":"SEM:480f6a8774fa47a7328e","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-cb0535c1f7ada3b0 | data/ingredients/mapped/Geomycin.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1049],"raw_equal":true},"docs_rows":[{"identifier":"mesh:D010118","line":1051,"mapping_status":"MAPPED","ontology_id":"mesh:D010118","preferred_term":"Geomycin"}],"identifier":"mesh:D010118","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:D010118","ontology_label":"Oxytetracycline","ontology_source":"MESH"},"preferred_term":"Geomycin","sssom_rows":[{"data_row":1294,"object_id":"mesh:D010118","object_label":"Oxytetracycline","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Geomycin","synonym_count":0} |
| ev-c48c63c2860846f7 | reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml; findings[finding_id=f-0d87a92810020171] | context_only | Predecessor structured review finding f-0d87a92810020171 in 20261011T024634Z-mim-reconcile-all-batch-06 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-geomycin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Geomycin (data/ingredients/mapped/Geomycin.yaml)'
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
summary: Per-record structured review for Geomycin (data/ingredients/mapped/Geomycin.yaml,
  record-7792bc0c82f05e91, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Geomycin.yaml
    sha256: fa269060e6ebc77f8c8bdf474dbae2432967d180e859387780789a8268d19bda
    role: target
  - path: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
    sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
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
  - path: reports/yaml_record_review/Geomycin.md
    sha256: f91815423f154a8538230c0241c4c607c12a05b8563c23469f3cd3a2a7bcd802
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-7792bc0c82f05e91
  path: data/ingredients/mapped/Geomycin.yaml
  label: Geomycin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Geomycin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Geomycin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Geomycin.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-7792bc0c82f05e91
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-7792bc0c82f05e91
  evidence_ids:
  - ev-1b470d2f08205155
  - ev-0496cea978282ccb
  - ev-e838aca40bd9fc3f
  - ev-0dbb6a0865c87790
  - ev-cb0535c1f7ada3b0
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-7792bc0c82f05e91
  evidence_ids:
  - ev-1b470d2f08205155
  - ev-23932eee9463388f
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-7792bc0c82f05e91
  evidence_ids:
  - ev-ef4f4ff5e6f66949
  - ev-23932eee9463388f
  - ev-c48c63c2860846f7
evidence:
- evidence_id: ev-1b470d2f08205155
  kind: record_content
  reference: data/ingredients/mapped/Geomycin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1049],"raw_equal":true},"docs_rows":[{"identifier":"mesh:D010118","line":1051,"mapping_status":"MAPPED","ontology_id":"mesh:D010118","preferred_term":"Geomycin"}],"identifier":"mesh:D010118","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:D010118","ontology_label":"Oxytetracycline","ontology_source":"MESH"},"preferred_term":"Geomycin","sssom_rows":[{"data_row":1294,"object_id":"mesh:D010118","object_label":"Oxytetracycline","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Geomycin","synonym_count":0}'
  snapshot_sha256: fa269060e6ebc77f8c8bdf474dbae2432967d180e859387780789a8268d19bda
- evidence_id: ev-0496cea978282ccb
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1049]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-e838aca40bd9fc3f
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Geomycin; data-row positions=[1294]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1294,"object_id":"mesh:D010118","object_label":"Oxytetracycline","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Geomycin","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-0dbb6a0865c87790
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1051]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"mesh:D010118","line":1051,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:D010118","preferred_term":"Geomycin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-ef4f4ff5e6f66949
  kind: prior_review
  reference: reports/yaml_record_review/Geomycin.md
  locator: '`data/ingredients/mapped/Geomycin.yaml`:2; Verdict:4; Identity:11; Validation:23;
    Evidence:38; Completeness:58; Recommended Edits:64'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: f91815423f154a8538230c0241c4c607c12a05b8563c23469f3cd3a2a7bcd802
  quote: "Recommended Edits:\n- Major: replace `SELECTIVE_AGENT` with source-backed\
    \ evidence or remove the\n  role, then rerun strict validation."
- evidence_id: ev-23932eee9463388f
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[660,1854]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"fa269060e6ebc77f8c8bdf474dbae2432967d180e859387780789a8268d19bda","finding_id":"SEM:fb3a6cf37e8dbcdd7633","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"fa269060e6ebc77f8c8bdf474dbae2432967d180e859387780789a8268d19bda","finding_id":"SEM:480f6a8774fa47a7328e","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-cb0535c1f7ada3b0
  kind: record_content
  reference: data/ingredients/mapped/Geomycin.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1049],"raw_equal":true},"docs_rows":[{"identifier":"mesh:D010118","line":1051,"mapping_status":"MAPPED","ontology_id":"mesh:D010118","preferred_term":"Geomycin"}],"identifier":"mesh:D010118","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:D010118","ontology_label":"Oxytetracycline","ontology_source":"MESH"},"preferred_term":"Geomycin","sssom_rows":[{"data_row":1294,"object_id":"mesh:D010118","object_label":"Oxytetracycline","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Geomycin","synonym_count":0}'
  snapshot_sha256: fa269060e6ebc77f8c8bdf474dbae2432967d180e859387780789a8268d19bda
- evidence_id: ev-c48c63c2860846f7
  kind: prior_review
  reference: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
  locator: findings[finding_id=f-0d87a92810020171]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-0d87a92810020171 in 20261011T024634Z-mim-reconcile-all-batch-06
  snapshot_sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
assessments:
- assessment_id: a-a418e15b35eae9ef
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-7792bc0c82f05e91
  evidence_ids:
  - ev-1b470d2f08205155
  - ev-0496cea978282ccb
  - ev-e838aca40bd9fc3f
  - ev-0dbb6a0865c87790
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-a1224596ee8f8034
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-7792bc0c82f05e91
  evidence_ids:
  - ev-ef4f4ff5e6f66949
  - ev-1b470d2f08205155
  - ev-23932eee9463388f
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:38:04Z;
    reviewed SHA-256=fa269060e6ebc77f8c8bdf474dbae2432967d180e859387780789a8268d19bda;
    current SHA-256=fa269060e6ebc77f8c8bdf474dbae2432967d180e859387780789a8268d19bda;
    hash_changed=False. Reports=["reports/yaml_record_review/Geomycin.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact MeSH synonym
    identity passes through external-prefix OLS validation, but SELECTIVE_AGENT is
    computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ef4f4ff5e6f66949
    - ev-1b470d2f08205155
  - name: legacy-native-ids
    value: '["SEM:fb3a6cf37e8dbcdd7633","SEM:480f6a8774fa47a7328e"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-1b470d2f08205155
    - ev-ef4f4ff5e6f66949
    - ev-23932eee9463388f
- assessment_id: a-cb0535c1f7ada3b0
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-7792bc0c82f05e91
  evidence_ids:
  - ev-ef4f4ff5e6f66949
  - ev-cb0535c1f7ada3b0
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ef4f4ff5e6f66949
    - ev-cb0535c1f7ada3b0
findings:
- finding_id: rec-f-0d87a92810020171
  issue_key: mim-reconciliation-role-support-7792bc0c82f05e91
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Geomycin'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-7792bc0c82f05e91
  evidence_ids:
  - ev-ef4f4ff5e6f66949
  - ev-cb0535c1f7ada3b0
  - ev-c48c63c2860846f7
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Geomycin.yaml
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
    review_id: 20261011T024634Z-mim-reconcile-all-batch-06
    finding_id: f-0d87a92810020171
actions:
- action_id: rec-action-0d87a92810020171
  description: 'Reassess prediction-only role support: Geomycin'
  finding_ids:
  - rec-f-0d87a92810020171
  target_ids:
  - record-7792bc0c82f05e91
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Geomycin.yaml
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
  with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.
```
