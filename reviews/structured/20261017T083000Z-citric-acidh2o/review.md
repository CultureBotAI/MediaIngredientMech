# Per-record structured review: Citric_Acidh2o (data/ingredients/mapped/Citric_Acidh2o.yaml)

- Review: 20261017T083000Z-citric-acidh2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Citric_Acidh2o (data/ingredients/mapped/Citric_Acidh2o.yaml, record-23150eef97e7c5c3, mapping_status=REJECTED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Citric_Acidh2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Citric_Acidh2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-23150eef97e7c5c3 | data/ingredients/mapped/Citric_Acidh2o.yaml | maintained | Citric_Acidh2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-23150eef97e7c5c3 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-23150eef97e7c5c3 | Role assertions on nutritional_roles[0], nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-23150eef97e7c5c3 | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-23150eef97e7c5c3.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-23150eef97e7c5c3.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T12:15:13Z; reviewed SHA-256=79a13957b8b85ee26d080e7d08773f23362c0ea6c890775c6b5dac1c469959c0; current SHA-256=79a13957b8b85ee26d080e7d08773f23362c0ea6c890775c6b5dac1c469959c0; hash_changed=False. Reports=["reports/yaml_record_review/Citric_Acidh2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The old citric acid monohydrate duplicate is correctly rejected into Citric_Acid_X_H2o, but its tombstone still carries stale nutritional roles.

### Historical provisional-role concern

evidence: unknown. Targets: record-23150eef97e7c5c3.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-fac2052cfbdf1a2e: Reassess prediction-only role support: Citric Acid•H2O

minor / deferred / provisional; issue key: mim-reconciliation-role-support-23150eef97e7c5c3.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

Disposition: The current local observation is recorded, but the named source/context or policy decision is still required; no correction is inferred.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-75ce4f831f4b58cf | data/ingredients/mapped/Citric_Acidh2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[733],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:31404","line":735,"mapping_status":"REJECTED","ontology_id":"CHEBI:31404","preferred_term":"Citric Acid\u2022H2O"}],"identifier":"CHEBI:31404","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":8,"edge_count":8,"occurrences":8},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:31404","ontology_label":"Citric acid monohydrate","ontology_source":"CHEBI"},"preferred_term":"Citric Acid\u2022H2O","sssom_rows":[],"sssom_subject":"MIM:Citric_Acidh2o","synonym_count":3} |
| ev-f524708940b6cb47 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [733] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-26341adfadf099c5 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Citric_Acidh2o; data-row positions=[] | context_only | Current exact-subject rows, including complete other payload: [] |
| ev-d744f4510c07d706 | docs/data/mapped_ingredients.csv; CSV lines=[735] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:31404","line":735,"mapping_quality":"EXACT_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:31404","preferred_term":"Citric Acid\u2022H2O","total_occurrences":"0"}] |
| ev-fe4a503a8ac96b8d | reports/yaml_record_review/Citric_Acidh2o.md; &#96;data/ingredients/mapped/Citric_Acidh2o.yaml&#96;:2; Verdict:4; Identity:11; Validation:23; Evidence:42; Completeness:57; Recommended Edits:63 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-bf4f19c8ec0fb85b | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[422] | context_only | [{"current_record_sha256":"79a13957b8b85ee26d080e7d08773f23362c0ea6c890775c6b5dac1c469959c0","finding_id":"SEM:e109bff23dd6181f5154","kind":"existing_record_review","resolution_reason":"Source record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}] |
| ev-90caf3d71e01273f | data/ingredients/mapped/Citric_Acidh2o.yaml; nutritional_roles[0], nutritional_roles[1] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}},{"field":"nutritional_roles[1]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.","reference_text":"Canonical energy substrate (catabolised for energy)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"ENERGY_SOURCE"}}] |
| ev-34c4d1119daa5278 | reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml; findings[finding_id=f-fac2052cfbdf1a2e] | context_only | Predecessor structured review finding f-fac2052cfbdf1a2e in 20261011T024632Z-mim-reconcile-all-batch-04 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-citric-acidh2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Citric_Acidh2o (data/ingredients/mapped/Citric_Acidh2o.yaml)'
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
summary: Per-record structured review for Citric_Acidh2o (data/ingredients/mapped/Citric_Acidh2o.yaml,
  record-23150eef97e7c5c3, mapping_status=REJECTED). Records 0 open finding(s) and
  1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Citric_Acidh2o.yaml
    sha256: 79a13957b8b85ee26d080e7d08773f23362c0ea6c890775c6b5dac1c469959c0
    role: target
  - path: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
    sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
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
  - path: reports/yaml_record_review/Citric_Acidh2o.md
    sha256: 95405a254d729e1aa30dbc7198112d41291f94fc301ac9241dd435262d8eae16
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-23150eef97e7c5c3
  path: data/ingredients/mapped/Citric_Acidh2o.yaml
  label: Citric_Acidh2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Citric_Acidh2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Citric_Acidh2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Citric_Acidh2o.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-23150eef97e7c5c3
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-23150eef97e7c5c3
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0], nutritional_roles[1] rely only
    on COMPUTATIONAL_PREDICTION or empty evidence.
  target_ids:
  - record-23150eef97e7c5c3
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-23150eef97e7c5c3
evidence:
- evidence_id: ev-75ce4f831f4b58cf
  kind: record_content
  reference: data/ingredients/mapped/Citric_Acidh2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[733],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:31404","line":735,"mapping_status":"REJECTED","ontology_id":"CHEBI:31404","preferred_term":"Citric
    Acid\u2022H2O"}],"identifier":"CHEBI:31404","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":8,"edge_count":8,"occurrences":8},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:31404","ontology_label":"Citric
    acid monohydrate","ontology_source":"CHEBI"},"preferred_term":"Citric Acid\u2022H2O","sssom_rows":[],"sssom_subject":"MIM:Citric_Acidh2o","synonym_count":3}'
  snapshot_sha256: 79a13957b8b85ee26d080e7d08773f23362c0ea6c890775c6b5dac1c469959c0
- evidence_id: ev-f524708940b6cb47
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [733]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-26341adfadf099c5
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Citric_Acidh2o; data-row positions=[]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: []'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-d744f4510c07d706
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[735]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:31404","line":735,"mapping_quality":"EXACT_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:31404","preferred_term":"Citric
    Acid\u2022H2O","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-fe4a503a8ac96b8d
  kind: prior_review
  reference: reports/yaml_record_review/Citric_Acidh2o.md
  locator: '`data/ingredients/mapped/Citric_Acidh2o.yaml`:2; Verdict:4; Identity:11;
    Validation:23; Evidence:42; Completeness:57; Recommended Edits:63'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 95405a254d729e1aa30dbc7198112d41291f94fc301ac9241dd435262d8eae16
  quote: "Recommended Edits:\n- Minor: remove the stale `nutritional_roles` block\
    \ from\n  `data/ingredients/mapped/Citric_Acidh2o.yaml`; the rejected tombstone\
    \ should\n  retain only the provenance needed to explain the merge into\n  `Citric_Acid_X_H2o`."
- evidence_id: ev-bf4f19c8ec0fb85b
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[422]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"79a13957b8b85ee26d080e7d08773f23362c0ea6c890775c6b5dac1c469959c0","finding_id":"SEM:e109bff23dd6181f5154","kind":"existing_record_review","resolution_reason":"Source
    record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-90caf3d71e01273f
  kind: record_content
  reference: data/ingredients/mapped/Citric_Acidh2o.yaml
  locator: nutritional_roles[0], nutritional_roles[1]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}},{"field":"nutritional_roles[1]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.","reference_text":"Canonical
    energy substrate (catabolised for energy)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"ENERGY_SOURCE"}}]'
  snapshot_sha256: 79a13957b8b85ee26d080e7d08773f23362c0ea6c890775c6b5dac1c469959c0
- evidence_id: ev-34c4d1119daa5278
  kind: prior_review
  reference: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
  locator: findings[finding_id=f-fac2052cfbdf1a2e]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-fac2052cfbdf1a2e in 20261011T024632Z-mim-reconcile-all-batch-04
  snapshot_sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
assessments:
- assessment_id: a-79cba63ff464ef73
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-23150eef97e7c5c3
  evidence_ids:
  - ev-75ce4f831f4b58cf
  - ev-f524708940b6cb47
  - ev-26341adfadf099c5
  - ev-d744f4510c07d706
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-c20a4875e4796700
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-23150eef97e7c5c3
  evidence_ids:
  - ev-fe4a503a8ac96b8d
  - ev-75ce4f831f4b58cf
  - ev-bf4f19c8ec0fb85b
  details: 'Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T12:15:13Z;
    reviewed SHA-256=79a13957b8b85ee26d080e7d08773f23362c0ea6c890775c6b5dac1c469959c0;
    current SHA-256=79a13957b8b85ee26d080e7d08773f23362c0ea6c890775c6b5dac1c469959c0;
    hash_changed=False. Reports=["reports/yaml_record_review/Citric_Acidh2o.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The old
    citric acid monohydrate duplicate is correctly rejected into Citric_Acid_X_H2o,
    but its tombstone still carries stale nutritional roles.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-fe4a503a8ac96b8d
    - ev-75ce4f831f4b58cf
  - name: legacy-native-ids
    value: '["SEM:e109bff23dd6181f5154"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-75ce4f831f4b58cf
    - ev-fe4a503a8ac96b8d
    - ev-bf4f19c8ec0fb85b
- assessment_id: a-90caf3d71e01273f
  area: evidence
  topic: Historical provisional-role concern
  outcome: unknown
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-23150eef97e7c5c3
  evidence_ids:
  - ev-fe4a503a8ac96b8d
  - ev-90caf3d71e01273f
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-fe4a503a8ac96b8d
    - ev-90caf3d71e01273f
findings:
- finding_id: rec-f-fac2052cfbdf1a2e
  issue_key: mim-reconciliation-role-support-23150eef97e7c5c3
  category: evidence
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Reassess prediction-only role support: Citric Acid•H2O'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-23150eef97e7c5c3
  evidence_ids:
  - ev-fe4a503a8ac96b8d
  - ev-90caf3d71e01273f
  - ev-34c4d1119daa5278
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Citric_Acidh2o.yaml
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
  disposition_reason: The current local observation is recorded, but the named source/context
    or policy decision is still required; no correction is inferred.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024632Z-mim-reconcile-all-batch-04
    finding_id: f-fac2052cfbdf1a2e
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
  with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.
```
