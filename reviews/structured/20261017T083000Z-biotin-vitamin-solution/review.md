# Per-record structured review: Biotin_Vitamin_Solution (data/ingredients/mapped/Biotin_Vitamin_Solution.yaml)

- Review: 20261017T083000Z-biotin-vitamin-solution
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Biotin_Vitamin_Solution (data/ingredients/mapped/Biotin_Vitamin_Solution.yaml, record-ed8e2e0c812cde8e, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Biotin_Vitamin_Solution.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Biotin_Vitamin_Solution.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-ed8e2e0c812cde8e | data/ingredients/mapped/Biotin_Vitamin_Solution.yaml | maintained | Biotin_Vitamin_Solution |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-ed8e2e0c812cde8e | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-ed8e2e0c812cde8e | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-ed8e2e0c812cde8e | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-ed8e2e0c812cde8e.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: not_applicable. Targets: record-ed8e2e0c812cde8e.

The latest legacy review reports no outstanding finding. This run verifies local consistency only; it does not renew that earlier scientific pass.

Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-16T09:52:09Z; reviewed SHA-256=013bef115224a5848c7ff17e210c181a2a4f9313f49a59839df55000a40635e6; current SHA-256=013bef115224a5848c7ff17e210c181a2a4f9313f49a59839df55000a40635e6; hash_changed=False. Reports=["reports/yaml_record_review/Biotin_Vitamin_Solution.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local biotin vitamin-solution registry identity, MICRO close match, SSSOM registry pattern, stock-solution classification, and aggregate copy pass.

### Historical provisional-role concern

evidence: concern. Targets: record-ed8e2e0c812cde8e.

Current role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence lists and require source-backed curation support.

## Findings

### rec-f-role-ed8e2e0c812cde8e: Reassess prediction-only or empty role support: Biotin_Vitamin_Solution

major / open / confirmed; issue key: mim-reconciliation-role-support-ed8e2e0c812cde8e.

Prediction-only or empty evidence payloads remain on the named current role assertions (nutritional_roles[0]). This confirms the local evidence gap, not that the biological role is false.

## Recommended Actions And Acceptance Checks

### rec-act-role-ed8e2e0c812cde8e

Reassess prediction-only or empty role support: Biotin_Vitamin_Solution

- Address the exact role fields and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-ef9de23d2bcebf8a | data/ingredients/mapped/Biotin_Vitamin_Solution.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[592],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:biotin_vitamin_solution","line":594,"mapping_status":"MAPPED","ontology_id":"MICRO:0000460","preferred_term":"Biotin Vitamin Solution"}],"identifier":"kgmicrobe.ingredient:biotin_vitamin_solution","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":18,"total_occurrences":18},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"MICRO:0000460","ontology_label":"vitamin solution","ontology_source":"MICRO"},"preferred_term":"Biotin Vitamin Solution","sssom_rows":[{"data_row":550,"object_id":"MICRO:0000460","object_label":"vitamin solution","predicate_id":"skos:closeMatch"},{"data_row":551,"object_id":"kgmicrobe.ingredient:biotin_vitamin_solution","object_label":"Biotin Vitamin Solution","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Biotin_Vitamin_Solution","synonym_count":1} |
| ev-358d158642ff4011 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [592] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-523fcbe24fec4636 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Biotin_Vitamin_Solution; data-row positions=[550,551] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":550,"object_id":"MICRO:0000460","object_label":"vitamin solution","other":"","predicate_id":"skos:closeMatch","subject_id":"MIM:Biotin_Vitamin_Solution","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"},{"data_row":551,"object_id":"kgmicrobe.ingredient:biotin_vitamin_solution","object_label":"Biotin Vitamin Solution","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Biotin_Vitamin_Solution","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-237999d92d949297 | docs/data/mapped_ingredients.csv; CSV lines=[594] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:biotin_vitamin_solution","line":594,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"18","ontology_id":"MICRO:0000460","preferred_term":"Biotin Vitamin Solution","total_occurrences":"18"}] |
| ev-ae5ab3f436ba2419 | reports/yaml_record_review/Biotin_Vitamin_Solution.md; &#96;data/ingredients/mapped/Biotin_Vitamin_Solution.yaml&#96;:2; Verdict:4; Identity:10; Validation:25; Evidence:35; Completeness:48; Recommended Edits:57 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-5c239d2dd9a0faff | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[2040] | context_only | [{"current_record_sha256":"013bef115224a5848c7ff17e210c181a2a4f9313f49a59839df55000a40635e6","finding_id":"SEM:d84e368e7ec2dffd481d","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-d4198f78e8779dda | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; current_record=data/ingredients/mapped/Biotin_Vitamin_Solution.yaml | context_only | Semantic review finding dispositions ledger |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-biotin-vitamin-solution
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Biotin_Vitamin_Solution (data/ingredients/mapped/Biotin_Vitamin_Solution.yaml)'
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
summary: Per-record structured review for Biotin_Vitamin_Solution (data/ingredients/mapped/Biotin_Vitamin_Solution.yaml,
  record-ed8e2e0c812cde8e, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Biotin_Vitamin_Solution.yaml
    sha256: 013bef115224a5848c7ff17e210c181a2a4f9313f49a59839df55000a40635e6
    role: target
  - path: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
    sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
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
  - path: reports/yaml_record_review/Biotin_Vitamin_Solution.md
    sha256: e217ef3ff39459e54447878fff43ecbf34a23ca4e69e8b1fe7f220b755d42b52
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-ed8e2e0c812cde8e
  path: data/ingredients/mapped/Biotin_Vitamin_Solution.yaml
  label: Biotin_Vitamin_Solution
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Biotin_Vitamin_Solution.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Biotin_Vitamin_Solution.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Biotin_Vitamin_Solution.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-ed8e2e0c812cde8e
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-ed8e2e0c812cde8e
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-ed8e2e0c812cde8e
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-ed8e2e0c812cde8e
evidence:
- evidence_id: ev-ef9de23d2bcebf8a
  kind: record_content
  reference: data/ingredients/mapped/Biotin_Vitamin_Solution.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[592],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:biotin_vitamin_solution","line":594,"mapping_status":"MAPPED","ontology_id":"MICRO:0000460","preferred_term":"Biotin
    Vitamin Solution"}],"identifier":"kgmicrobe.ingredient:biotin_vitamin_solution","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":18,"total_occurrences":18},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"MICRO:0000460","ontology_label":"vitamin
    solution","ontology_source":"MICRO"},"preferred_term":"Biotin Vitamin Solution","sssom_rows":[{"data_row":550,"object_id":"MICRO:0000460","object_label":"vitamin
    solution","predicate_id":"skos:closeMatch"},{"data_row":551,"object_id":"kgmicrobe.ingredient:biotin_vitamin_solution","object_label":"Biotin
    Vitamin Solution","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Biotin_Vitamin_Solution","synonym_count":1}'
  snapshot_sha256: 013bef115224a5848c7ff17e210c181a2a4f9313f49a59839df55000a40635e6
- evidence_id: ev-358d158642ff4011
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [592]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-523fcbe24fec4636
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Biotin_Vitamin_Solution; data-row positions=[550,551]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":550,"object_id":"MICRO:0000460","object_label":"vitamin
    solution","other":"","predicate_id":"skos:closeMatch","subject_id":"MIM:Biotin_Vitamin_Solution","validation_method":"none|UNKNOWN_TERM|2026-07-07"},{"data_row":551,"object_id":"kgmicrobe.ingredient:biotin_vitamin_solution","object_label":"Biotin
    Vitamin Solution","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Biotin_Vitamin_Solution","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-237999d92d949297
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[594]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:biotin_vitamin_solution","line":594,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"18","ontology_id":"MICRO:0000460","preferred_term":"Biotin
    Vitamin Solution","total_occurrences":"18"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-ae5ab3f436ba2419
  kind: prior_review
  reference: reports/yaml_record_review/Biotin_Vitamin_Solution.md
  locator: '`data/ingredients/mapped/Biotin_Vitamin_Solution.yaml`:2; Verdict:4; Identity:10;
    Validation:25; Evidence:35; Completeness:48; Recommended Edits:57'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: e217ef3ff39459e54447878fff43ecbf34a23ca4e69e8b1fe7f220b755d42b52
  quote: 'Recommended Edits:

    - None.'
- evidence_id: ev-5c239d2dd9a0faff
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[2040]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"013bef115224a5848c7ff17e210c181a2a4f9313f49a59839df55000a40635e6","finding_id":"SEM:d84e368e7ec2dffd481d","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-d4198f78e8779dda
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: current_record=data/ingredients/mapped/Biotin_Vitamin_Solution.yaml
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Semantic review finding dispositions ledger
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-740631b75aac7e28
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-ed8e2e0c812cde8e
  evidence_ids:
  - ev-ef9de23d2bcebf8a
  - ev-358d158642ff4011
  - ev-523fcbe24fec4636
  - ev-237999d92d949297
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-597f5941bd497e01
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: not_applicable
  summary: The latest legacy review reports no outstanding finding. This run verifies
    local consistency only; it does not renew that earlier scientific pass.
  target_ids:
  - record-ed8e2e0c812cde8e
  evidence_ids:
  - ev-ae5ab3f436ba2419
  - ev-ef9de23d2bcebf8a
  - ev-5c239d2dd9a0faff
  details: 'Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-16T09:52:09Z;
    reviewed SHA-256=013bef115224a5848c7ff17e210c181a2a4f9313f49a59839df55000a40635e6;
    current SHA-256=013bef115224a5848c7ff17e210c181a2a4f9313f49a59839df55000a40635e6;
    hash_changed=False. Reports=["reports/yaml_record_review/Biotin_Vitamin_Solution.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    biotin vitamin-solution registry identity, MICRO close match, SSSOM registry pattern,
    stock-solution classification, and aggregate copy pass.'
  dimensions:
  - name: legacy-native-ids
    value: '["SEM:d84e368e7ec2dffd481d"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-ef9de23d2bcebf8a
    - ev-ae5ab3f436ba2419
    - ev-5c239d2dd9a0faff
- assessment_id: a-role-ed8e2e0c812cde8e
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Current role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence lists and require source-backed curation support.
  target_ids:
  - record-ed8e2e0c812cde8e
  evidence_ids:
  - ev-ef9de23d2bcebf8a
  - ev-d4198f78e8779dda
  dimensions:
  - name: legacy-disposition
    value: still_present
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ef9de23d2bcebf8a
    - ev-d4198f78e8779dda
findings:
- finding_id: rec-f-role-ed8e2e0c812cde8e
  issue_key: mim-reconciliation-role-support-ed8e2e0c812cde8e
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only or empty role support: Biotin_Vitamin_Solution'
  description: Prediction-only or empty evidence payloads remain on the named current
    role assertions (nutritional_roles[0]). This confirms the local evidence gap,
    not that the biological role is false.
  target_ids:
  - record-ed8e2e0c812cde8e
  evidence_ids:
  - ev-ef9de23d2bcebf8a
  - ev-d4198f78e8779dda
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Biotin_Vitamin_Solution.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
actions:
- action_id: rec-act-role-ed8e2e0c812cde8e
  description: 'Reassess prediction-only or empty role support: Biotin_Vitamin_Solution'
  finding_ids:
  - rec-f-role-ed8e2e0c812cde8e
  target_ids:
  - record-ed8e2e0c812cde8e
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Biotin_Vitamin_Solution.yaml
    role: maintained ingredient
  acceptance_checks:
  - Address the exact role fields and evidence gap described in this finding; preserve
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
  with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.
```
