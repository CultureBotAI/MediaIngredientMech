# Per-record structured review: M-xylene (data/ingredients/mapped/M-xylene.yaml)

- Review: 20261017T083000Z-m-xylene
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for M-xylene (data/ingredients/mapped/M-xylene.yaml, record-bd48f6264749ea16, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/M-xylene.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/M-xylene.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-bd48f6264749ea16 | data/ingredients/mapped/M-xylene.yaml | maintained | M-xylene |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-bd48f6264749ea16 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-bd48f6264749ea16 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-bd48f6264749ea16 | Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-bd48f6264749ea16.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-bd48f6264749ea16.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T00:57:54Z; reviewed SHA-256=31f4e266d3794ee7494468b5e6801cf0d98126e9c51db8b89fc86be253a7027d; current SHA-256=31f4e266d3794ee7494468b5e6801cf0d98126e9c51db8b89fc86be253a7027d; hash_changed=False. Reports=["reports/yaml_record_review/M-xylene.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:28488 identity, CAS value, PubChem structure, exact synonyms, and final SSSOM row pass, but CARBON_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-bd48f6264749ea16.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-066bc67b02ec8f6b: Reassess prediction-only role support: m-Xylene

major / open / confirmed; issue key: mim-reconciliation-role-support-bd48f6264749ea16.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-066bc67b02ec8f6b

Reassess prediction-only role support: m-Xylene

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-be7e04c4b9b49997 | data/ingredients/mapped/M-xylene.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1322],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:28488","line":1324,"mapping_status":"MAPPED","ontology_id":"CHEBI:28488","preferred_term":"m-Xylene"}],"identifier":"CHEBI:28488","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":9,"edge_count":9,"occurrences":9},"occurrence_statistics":{"media_count":9,"total_occurrences":9},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:28488","ontology_label":"m-xylene","ontology_source":"CHEBI"},"preferred_term":"m-Xylene","sssom_rows":[{"data_row":1725,"object_id":"CHEBI:28488","object_label":"m-xylene","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:M-xylene","synonym_count":8} |
| ev-c41365eec70da96d | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1322] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-f73ec4fee09c87b4 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:M-xylene; data-row positions=[1725] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1725,"object_id":"CHEBI:28488","object_label":"m-xylene","other":"1,3-Dimethylbenzene&#124;1,3-Dimethylbenzol&#124;1,3-Xylene&#124;3-xylene&#124;m-Xylol&#124;m-dimethylbenzene&#124;m-methyltoluene&#124;meta-xylene&#124;CAS:108-38-3","predicate_id":"skos:exactMatch","subject_id":"MIM:M-xylene","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-18ee35df3356c92c | docs/data/mapped_ingredients.csv; CSV lines=[1324] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:28488","line":1324,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"9","ontology_id":"CHEBI:28488","preferred_term":"m-Xylene","total_occurrences":"9"}] |
| ev-98000bfa93cf1255 | reports/yaml_record_review/M-xylene.md; &#96;data/ingredients/mapped/M-xylene.yaml&#96;:2; Verdict:4; Identity:13; Validation:24; Evidence:33; Completeness:43; Recommended Edits:53 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-7822a035d98199db | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[875,1713] | context_only | [{"current_record_sha256":"31f4e266d3794ee7494468b5e6801cf0d98126e9c51db8b89fc86be253a7027d","finding_id":"SEM:895f6bfd07ee1bf23750","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"31f4e266d3794ee7494468b5e6801cf0d98126e9c51db8b89fc86be253a7027d","finding_id":"SEM:cb51dcc00007ef0cc9f7","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-e04c848232fa843f | data/ingredients/mapped/M-xylene.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional in-session LLM role assignment; review recommended.","reference_text":"Assigned by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}] |
| ev-70a248b0560160cb | reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml; findings[finding_id=f-066bc67b02ec8f6b] | context_only | Predecessor structured review finding f-066bc67b02ec8f6b in 20261011T024636Z-mim-reconcile-all-batch-08 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-m-xylene
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: M-xylene (data/ingredients/mapped/M-xylene.yaml)'
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
summary: Per-record structured review for M-xylene (data/ingredients/mapped/M-xylene.yaml,
  record-bd48f6264749ea16, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/M-xylene.yaml
    sha256: 31f4e266d3794ee7494468b5e6801cf0d98126e9c51db8b89fc86be253a7027d
    role: target
  - path: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
    sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
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
  - path: reports/yaml_record_review/M-xylene.md
    sha256: c62f776ccc2b8e36e61176315969200dd83f56c6857997d5a44d7eeef1b2b744
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-bd48f6264749ea16
  path: data/ingredients/mapped/M-xylene.yaml
  label: M-xylene
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/M-xylene.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/M-xylene.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/M-xylene.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-bd48f6264749ea16
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-bd48f6264749ea16
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-bd48f6264749ea16
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08
    and semantic review dispositions on HEAD.
  target_ids:
  - record-bd48f6264749ea16
evidence:
- evidence_id: ev-be7e04c4b9b49997
  kind: record_content
  reference: data/ingredients/mapped/M-xylene.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1322],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:28488","line":1324,"mapping_status":"MAPPED","ontology_id":"CHEBI:28488","preferred_term":"m-Xylene"}],"identifier":"CHEBI:28488","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":9,"edge_count":9,"occurrences":9},"occurrence_statistics":{"media_count":9,"total_occurrences":9},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:28488","ontology_label":"m-xylene","ontology_source":"CHEBI"},"preferred_term":"m-Xylene","sssom_rows":[{"data_row":1725,"object_id":"CHEBI:28488","object_label":"m-xylene","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:M-xylene","synonym_count":8}'
  snapshot_sha256: 31f4e266d3794ee7494468b5e6801cf0d98126e9c51db8b89fc86be253a7027d
- evidence_id: ev-c41365eec70da96d
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1322]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-f73ec4fee09c87b4
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:M-xylene; data-row positions=[1725]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1725,"object_id":"CHEBI:28488","object_label":"m-xylene","other":"1,3-Dimethylbenzene|1,3-Dimethylbenzol|1,3-Xylene|3-xylene|m-Xylol|m-dimethylbenzene|m-methyltoluene|meta-xylene|CAS:108-38-3","predicate_id":"skos:exactMatch","subject_id":"MIM:M-xylene","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-18ee35df3356c92c
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1324]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:28488","line":1324,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"9","ontology_id":"CHEBI:28488","preferred_term":"m-Xylene","total_occurrences":"9"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-98000bfa93cf1255
  kind: prior_review
  reference: reports/yaml_record_review/M-xylene.md
  locator: '`data/ingredients/mapped/M-xylene.yaml`:2; Verdict:4; Identity:13; Validation:24;
    Evidence:33; Completeness:43; Recommended Edits:53'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: c62f776ccc2b8e36e61176315969200dd83f56c6857997d5a44d7eeef1b2b744
  quote: "Recommended Edits:\n- Curate evidence for `CARBON_SOURCE`, or remove the\
    \ role if no supporting\n  ingredient-level evidence is available."
- evidence_id: ev-7822a035d98199db
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[875,1713]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"31f4e266d3794ee7494468b5e6801cf0d98126e9c51db8b89fc86be253a7027d","finding_id":"SEM:895f6bfd07ee1bf23750","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"31f4e266d3794ee7494468b5e6801cf0d98126e9c51db8b89fc86be253a7027d","finding_id":"SEM:cb51dcc00007ef0cc9f7","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-e04c848232fa843f
  kind: record_content
  reference: data/ingredients/mapped/M-xylene.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional
    in-session LLM role assignment; review recommended.","reference_text":"Assigned
    by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}]'
  snapshot_sha256: 31f4e266d3794ee7494468b5e6801cf0d98126e9c51db8b89fc86be253a7027d
- evidence_id: ev-70a248b0560160cb
  kind: prior_review
  reference: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
  locator: findings[finding_id=f-066bc67b02ec8f6b]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-066bc67b02ec8f6b in 20261011T024636Z-mim-reconcile-all-batch-08
  snapshot_sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
assessments:
- assessment_id: a-c27b45a37c61fcb2
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-bd48f6264749ea16
  evidence_ids:
  - ev-be7e04c4b9b49997
  - ev-c41365eec70da96d
  - ev-f73ec4fee09c87b4
  - ev-18ee35df3356c92c
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-edb134156b3de190
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-bd48f6264749ea16
  evidence_ids:
  - ev-98000bfa93cf1255
  - ev-be7e04c4b9b49997
  - ev-7822a035d98199db
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T00:57:54Z;
    reviewed SHA-256=31f4e266d3794ee7494468b5e6801cf0d98126e9c51db8b89fc86be253a7027d;
    current SHA-256=31f4e266d3794ee7494468b5e6801cf0d98126e9c51db8b89fc86be253a7027d;
    hash_changed=False. Reports=["reports/yaml_record_review/M-xylene.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI:28488 identity,
    CAS value, PubChem structure, exact synonyms, and final SSSOM row pass, but CARBON_SOURCE
    is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-98000bfa93cf1255
    - ev-be7e04c4b9b49997
  - name: legacy-native-ids
    value: '["SEM:895f6bfd07ee1bf23750","SEM:cb51dcc00007ef0cc9f7"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-be7e04c4b9b49997
    - ev-98000bfa93cf1255
    - ev-7822a035d98199db
- assessment_id: a-e04c848232fa843f
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-bd48f6264749ea16
  evidence_ids:
  - ev-98000bfa93cf1255
  - ev-e04c848232fa843f
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-98000bfa93cf1255
    - ev-e04c848232fa843f
findings:
- finding_id: rec-f-066bc67b02ec8f6b
  issue_key: mim-reconciliation-role-support-bd48f6264749ea16
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: m-Xylene'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-bd48f6264749ea16
  evidence_ids:
  - ev-98000bfa93cf1255
  - ev-e04c848232fa843f
  - ev-70a248b0560160cb
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/M-xylene.yaml
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
    review_id: 20261011T024636Z-mim-reconcile-all-batch-08
    finding_id: f-066bc67b02ec8f6b
actions:
- action_id: rec-action-066bc67b02ec8f6b
  description: 'Reassess prediction-only role support: m-Xylene'
  finding_ids:
  - rec-f-066bc67b02ec8f6b
  target_ids:
  - record-bd48f6264749ea16
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/M-xylene.yaml
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
  with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.
```
