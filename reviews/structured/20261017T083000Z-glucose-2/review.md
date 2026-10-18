# Per-record structured review: Glucose_2 (data/ingredients/mapped/Glucose_2.yaml)

- Review: 20261017T083000Z-glucose-2
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Glucose_2 (data/ingredients/mapped/Glucose_2.yaml, record-b3a9e2fcf5fcfc95, mapping_status=REJECTED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Glucose_2.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Glucose_2.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-b3a9e2fcf5fcfc95 | data/ingredients/mapped/Glucose_2.yaml | maintained | Glucose_2 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-b3a9e2fcf5fcfc95 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-b3a9e2fcf5fcfc95 | Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-b3a9e2fcf5fcfc95 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-b3a9e2fcf5fcfc95.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-b3a9e2fcf5fcfc95.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T17:44:41Z; reviewed SHA-256=bb5ada131940775cce28d997888912c5337dd39aaab35d95bf8c566cb2bb22ed; current SHA-256=bb5ada131940775cce28d997888912c5337dd39aaab35d95bf8c566cb2bb22ed; hash_changed=False. Reports=["reports/yaml_record_review/Glucose_2.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The rejected lowercase glucose tombstone no longer publishes final SSSOM, but stale pre-merge fields remain.

### Historical provisional-role concern

evidence: unknown. Targets: record-b3a9e2fcf5fcfc95.

Current role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence lists and require source-backed curation support.

## Findings

### rec-f-role-b3a9e2fcf5fcfc95: Reassess prediction-only or empty role support: Glucose_2

minor / deferred / provisional; issue key: mim-reconciliation-role-support-b3a9e2fcf5fcfc95.

Prediction-only or empty evidence payloads remain on the named current role assertions (nutritional_roles[1]). This confirms the local evidence gap, not that the biological role is false.

Disposition: The current local observation is recorded on a REJECTED tombstone, but the named source/context or policy decision is still required; no correction is inferred.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-88be9db0fc9e05d8 | data/ingredients/mapped/Glucose_2.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1059],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17234","line":1061,"mapping_status":"REJECTED","ontology_id":"CHEBI:17234","preferred_term":"glucose"}],"identifier":"CHEBI:17234","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":2675,"edge_count":2675,"occurrences":2752},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17234","ontology_label":"glucose","ontology_source":"CHEBI"},"preferred_term":"glucose","sssom_rows":[],"sssom_subject":"MIM:Glucose_2","synonym_count":8} |
| ev-27ccb9f6dcac2386 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1059] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-91a6876250418c37 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Glucose_2; data-row positions=[] | context_only | Current exact-subject rows, including complete other payload: [] |
| ev-23d6c57b39482672 | docs/data/mapped_ingredients.csv; CSV lines=[1061] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:17234","line":1061,"mapping_quality":"EXACT_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:17234","preferred_term":"glucose","total_occurrences":"0"}] |
| ev-b876af810a203338 | reports/yaml_record_review/Glucose_2.md; &#96;data/ingredients/mapped/Glucose_2.yaml&#96;:2; Verdict:4; Identity:11; Validation:22; Evidence:34; Completeness:54; Recommended Edits:60 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-e06d8ea23fed3000 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[668] | context_only | [{"current_record_sha256":"bb5ada131940775cce28d997888912c5337dd39aaab35d95bf8c566cb2bb22ed","finding_id":"SEM:3019d0011249aad9f1d2","kind":"existing_record_review","resolution_reason":"Source record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-glucose-2
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Glucose_2 (data/ingredients/mapped/Glucose_2.yaml)'
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
native_verdict: mapping_status=REJECTED; open=0; deferred=1
scientific_review: false
summary: Per-record structured review for Glucose_2 (data/ingredients/mapped/Glucose_2.yaml,
  record-b3a9e2fcf5fcfc95, mapping_status=REJECTED). Records 0 open finding(s) and
  1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Glucose_2.yaml
    sha256: bb5ada131940775cce28d997888912c5337dd39aaab35d95bf8c566cb2bb22ed
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
  - path: reports/yaml_record_review/Glucose_2.md
    sha256: 875173351380a8994a5abae3a54c9e7bc3f2e9a0040b324c2eb742abc278f002
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-b3a9e2fcf5fcfc95
  path: data/ingredients/mapped/Glucose_2.yaml
  label: Glucose_2
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glucose_2.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Glucose_2.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Glucose_2.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-b3a9e2fcf5fcfc95
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-b3a9e2fcf5fcfc95
  evidence_ids:
  - ev-88be9db0fc9e05d8
  - ev-27ccb9f6dcac2386
  - ev-91a6876250418c37
  - ev-23d6c57b39482672
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-b3a9e2fcf5fcfc95
  evidence_ids:
  - ev-88be9db0fc9e05d8
  - ev-e06d8ea23fed3000
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-b3a9e2fcf5fcfc95
  evidence_ids:
  - ev-b876af810a203338
  - ev-e06d8ea23fed3000
evidence:
- evidence_id: ev-88be9db0fc9e05d8
  kind: record_content
  reference: data/ingredients/mapped/Glucose_2.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1059],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17234","line":1061,"mapping_status":"REJECTED","ontology_id":"CHEBI:17234","preferred_term":"glucose"}],"identifier":"CHEBI:17234","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":2675,"edge_count":2675,"occurrences":2752},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17234","ontology_label":"glucose","ontology_source":"CHEBI"},"preferred_term":"glucose","sssom_rows":[],"sssom_subject":"MIM:Glucose_2","synonym_count":8}'
  snapshot_sha256: bb5ada131940775cce28d997888912c5337dd39aaab35d95bf8c566cb2bb22ed
- evidence_id: ev-27ccb9f6dcac2386
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1059]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-91a6876250418c37
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Glucose_2; data-row positions=[]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: []'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-23d6c57b39482672
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1061]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:17234","line":1061,"mapping_quality":"EXACT_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:17234","preferred_term":"glucose","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-b876af810a203338
  kind: prior_review
  reference: reports/yaml_record_review/Glucose_2.md
  locator: '`data/ingredients/mapped/Glucose_2.yaml`:2; Verdict:4; Identity:11; Validation:22;
    Evidence:34; Completeness:54; Recommended Edits:60'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 875173351380a8994a5abae3a54c9e7bc3f2e9a0040b324c2eb742abc278f002
  quote: "Recommended Edits:\n- Minor: remove stale structure, type, and nutritional-role\
    \ fields from the\n  rejected tombstone if tombstones are intended to retain only\
    \ merge\n  provenance."
- evidence_id: ev-e06d8ea23fed3000
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[668]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"bb5ada131940775cce28d997888912c5337dd39aaab35d95bf8c566cb2bb22ed","finding_id":"SEM:3019d0011249aad9f1d2","kind":"existing_record_review","resolution_reason":"Source
    record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-c8570dbf9cd56717
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-b3a9e2fcf5fcfc95
  evidence_ids:
  - ev-88be9db0fc9e05d8
  - ev-27ccb9f6dcac2386
  - ev-91a6876250418c37
  - ev-23d6c57b39482672
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-d85d21c513dfa766
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-b3a9e2fcf5fcfc95
  evidence_ids:
  - ev-b876af810a203338
  - ev-88be9db0fc9e05d8
  - ev-e06d8ea23fed3000
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T17:44:41Z;
    reviewed SHA-256=bb5ada131940775cce28d997888912c5337dd39aaab35d95bf8c566cb2bb22ed;
    current SHA-256=bb5ada131940775cce28d997888912c5337dd39aaab35d95bf8c566cb2bb22ed;
    hash_changed=False. Reports=["reports/yaml_record_review/Glucose_2.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The rejected lowercase
    glucose tombstone no longer publishes final SSSOM, but stale pre-merge fields
    remain.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b876af810a203338
    - ev-88be9db0fc9e05d8
  - name: legacy-native-ids
    value: '["SEM:3019d0011249aad9f1d2"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-88be9db0fc9e05d8
    - ev-b876af810a203338
    - ev-e06d8ea23fed3000
- assessment_id: a-role-b3a9e2fcf5fcfc95
  area: evidence
  topic: Historical provisional-role concern
  outcome: unknown
  summary: Current role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence lists and require source-backed curation support.
  target_ids:
  - record-b3a9e2fcf5fcfc95
  evidence_ids:
  - ev-88be9db0fc9e05d8
  - ev-e06d8ea23fed3000
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-88be9db0fc9e05d8
    - ev-e06d8ea23fed3000
findings:
- finding_id: rec-f-role-b3a9e2fcf5fcfc95
  issue_key: mim-reconciliation-role-support-b3a9e2fcf5fcfc95
  category: evidence
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Reassess prediction-only or empty role support: Glucose_2'
  description: Prediction-only or empty evidence payloads remain on the named current
    role assertions (nutritional_roles[1]). This confirms the local evidence gap,
    not that the biological role is false.
  target_ids:
  - record-b3a9e2fcf5fcfc95
  evidence_ids:
  - ev-88be9db0fc9e05d8
  - ev-e06d8ea23fed3000
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glucose_2.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[1]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  disposition_reason: The current local observation is recorded on a REJECTED tombstone,
    but the named source/context or policy decision is still required; no correction
    is inferred.
actions: []
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
