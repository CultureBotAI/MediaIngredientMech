# Per-record structured review: Sodium_L-lactate (data/ingredients/mapped/Sodium_L-lactate.yaml)

- Review: 20261017T083000Z-sodium-l-lactate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Sodium_L-lactate (data/ingredients/mapped/Sodium_L-lactate.yaml, record-0d86662afef1df4c, mapping_status=REJECTED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Sodium_L-lactate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Sodium_L-lactate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-0d86662afef1df4c | data/ingredients/mapped/Sodium_L-lactate.yaml | maintained | Sodium_L-lactate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-0d86662afef1df4c | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-0d86662afef1df4c | Role assertions on nutritional_roles[0], nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-0d86662afef1df4c | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-0d86662afef1df4c.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-0d86662afef1df4c.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-17T15:22:24Z; reviewed SHA-256=c9b2157390a5a84dfd18e5d8d869edd2114b62b3b92b82e064c0b3a29cb3ccce; current SHA-256=c9b2157390a5a84dfd18e5d8d869edd2114b62b3b92b82e064c0b3a29cb3ccce; hash_changed=False. Reports=["reports/yaml_record_review/Sodium_L-lactate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The rejected duplicate points at the live CHEBI:232798 target and emits no final row; stale roles are tombstone-only.

### Historical provisional-role concern

evidence: unknown. Targets: record-0d86662afef1df4c.

Current role assertions on nutritional_roles[0], nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence lists and require source-backed curation support.

## Findings

### rec-f-role-0d86662afef1df4c: Reassess prediction-only or empty role support: Sodium_L-lactate

minor / deferred / provisional; issue key: mim-reconciliation-role-support-0d86662afef1df4c.

Prediction-only or empty evidence payloads remain on the named current role assertions (nutritional_roles[0], nutritional_roles[1]). This confirms the local evidence gap, not that the biological role is false.

Disposition: The current local observation is recorded on a REJECTED tombstone, but the named source/context or policy decision is still required; no correction is inferred.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-c241a7c50640b1f3 | data/ingredients/mapped/Sodium_L-lactate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1846],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:232798","line":1848,"mapping_status":"REJECTED","ontology_id":"CHEBI:232798","preferred_term":"Sodium L-lactate"}],"identifier":"CHEBI:232798","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":162,"edge_count":162,"occurrences":162},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:232798","ontology_label":"sodium L-lactate","ontology_source":"CHEBI"},"preferred_term":"Sodium L-lactate","sssom_rows":[],"sssom_subject":"MIM:Sodium_L-lactate","synonym_count":1} |
| ev-9d861a394797dbcc | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1846] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-d2f0e7fe47ff04fa | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Sodium_L-lactate; data-row positions=[] | context_only | Current exact-subject rows, including complete other payload: [] |
| ev-70ddac9b16d87d0c | docs/data/mapped_ingredients.csv; CSV lines=[1848] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:232798","line":1848,"mapping_quality":"EXACT_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:232798","preferred_term":"Sodium L-lactate","total_occurrences":"0"}] |
| ev-bf2d791ba7229391 | reports/yaml_record_review/Sodium_L-lactate.md; &#96;data/ingredients/mapped/Sodium_L-lactate.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-b26222588fecb744 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1219] | context_only | [{"current_record_sha256":"c9b2157390a5a84dfd18e5d8d869edd2114b62b3b92b82e064c0b3a29cb3ccce","finding_id":"SEM:62dd5d8f80ed06927808","kind":"existing_record_review","resolution_reason":"Source record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-sodium-l-lactate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Sodium_L-lactate (data/ingredients/mapped/Sodium_L-lactate.yaml)'
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
summary: Per-record structured review for Sodium_L-lactate (data/ingredients/mapped/Sodium_L-lactate.yaml,
  record-0d86662afef1df4c, mapping_status=REJECTED). Records 0 open finding(s) and
  1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Sodium_L-lactate.yaml
    sha256: c9b2157390a5a84dfd18e5d8d869edd2114b62b3b92b82e064c0b3a29cb3ccce
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
  - path: reports/yaml_record_review/Sodium_L-lactate.md
    sha256: c1452826e08ca383473fe683a0208415c10276ffb2f0da3db153a2afb623520a
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-0d86662afef1df4c
  path: data/ingredients/mapped/Sodium_L-lactate.yaml
  label: Sodium_L-lactate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_L-lactate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Sodium_L-lactate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Sodium_L-lactate.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-0d86662afef1df4c
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-0d86662afef1df4c
  evidence_ids:
  - ev-c241a7c50640b1f3
  - ev-9d861a394797dbcc
  - ev-d2f0e7fe47ff04fa
  - ev-70ddac9b16d87d0c
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0], nutritional_roles[1] rely only
    on COMPUTATIONAL_PREDICTION or empty evidence.
  target_ids:
  - record-0d86662afef1df4c
  evidence_ids:
  - ev-c241a7c50640b1f3
  - ev-b26222588fecb744
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-0d86662afef1df4c
  evidence_ids:
  - ev-bf2d791ba7229391
  - ev-b26222588fecb744
evidence:
- evidence_id: ev-c241a7c50640b1f3
  kind: record_content
  reference: data/ingredients/mapped/Sodium_L-lactate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1846],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:232798","line":1848,"mapping_status":"REJECTED","ontology_id":"CHEBI:232798","preferred_term":"Sodium
    L-lactate"}],"identifier":"CHEBI:232798","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":162,"edge_count":162,"occurrences":162},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:232798","ontology_label":"sodium
    L-lactate","ontology_source":"CHEBI"},"preferred_term":"Sodium L-lactate","sssom_rows":[],"sssom_subject":"MIM:Sodium_L-lactate","synonym_count":1}'
  snapshot_sha256: c9b2157390a5a84dfd18e5d8d869edd2114b62b3b92b82e064c0b3a29cb3ccce
- evidence_id: ev-9d861a394797dbcc
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1846]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-d2f0e7fe47ff04fa
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Sodium_L-lactate; data-row positions=[]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: []'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-70ddac9b16d87d0c
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1848]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:232798","line":1848,"mapping_quality":"EXACT_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:232798","preferred_term":"Sodium
    L-lactate","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-bf2d791ba7229391
  kind: prior_review
  reference: reports/yaml_record_review/Sodium_L-lactate.md
  locator: '`data/ingredients/mapped/Sodium_L-lactate.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: c1452826e08ca383473fe683a0208415c10276ffb2f0da3db153a2afb623520a
- evidence_id: ev-b26222588fecb744
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1219]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"c9b2157390a5a84dfd18e5d8d869edd2114b62b3b92b82e064c0b3a29cb3ccce","finding_id":"SEM:62dd5d8f80ed06927808","kind":"existing_record_review","resolution_reason":"Source
    record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-6a48a816f4039274
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-0d86662afef1df4c
  evidence_ids:
  - ev-c241a7c50640b1f3
  - ev-9d861a394797dbcc
  - ev-d2f0e7fe47ff04fa
  - ev-70ddac9b16d87d0c
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-8ec18a32627e9dbb
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-0d86662afef1df4c
  evidence_ids:
  - ev-bf2d791ba7229391
  - ev-c241a7c50640b1f3
  - ev-b26222588fecb744
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-17T15:22:24Z;
    reviewed SHA-256=c9b2157390a5a84dfd18e5d8d869edd2114b62b3b92b82e064c0b3a29cb3ccce;
    current SHA-256=c9b2157390a5a84dfd18e5d8d869edd2114b62b3b92b82e064c0b3a29cb3ccce;
    hash_changed=False. Reports=["reports/yaml_record_review/Sodium_L-lactate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The rejected
    duplicate points at the live CHEBI:232798 target and emits no final row; stale
    roles are tombstone-only.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-bf2d791ba7229391
    - ev-c241a7c50640b1f3
  - name: legacy-native-ids
    value: '["SEM:62dd5d8f80ed06927808"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-c241a7c50640b1f3
    - ev-bf2d791ba7229391
    - ev-b26222588fecb744
- assessment_id: a-role-0d86662afef1df4c
  area: evidence
  topic: Historical provisional-role concern
  outcome: unknown
  summary: Current role assertions on nutritional_roles[0], nutritional_roles[1] rely
    only on COMPUTATIONAL_PREDICTION or empty evidence lists and require source-backed
    curation support.
  target_ids:
  - record-0d86662afef1df4c
  evidence_ids:
  - ev-c241a7c50640b1f3
  - ev-b26222588fecb744
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c241a7c50640b1f3
    - ev-b26222588fecb744
findings:
- finding_id: rec-f-role-0d86662afef1df4c
  issue_key: mim-reconciliation-role-support-0d86662afef1df4c
  category: evidence
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Reassess prediction-only or empty role support: Sodium_L-lactate'
  description: Prediction-only or empty evidence payloads remain on the named current
    role assertions (nutritional_roles[0], nutritional_roles[1]). This confirms the
    local evidence gap, not that the biological role is false.
  target_ids:
  - record-0d86662afef1df4c
  evidence_ids:
  - ev-c241a7c50640b1f3
  - ev-b26222588fecb744
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_L-lactate.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.
```
