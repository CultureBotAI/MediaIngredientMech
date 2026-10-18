# Per-record structured review: Azureomycin (data/ingredients/mapped/Azureomycin.yaml)

- Review: 20261017T083000Z-azureomycin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Azureomycin (data/ingredients/mapped/Azureomycin.yaml, record-b6c3f8931f08d05c, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Azureomycin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Azureomycin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-b6c3f8931f08d05c | data/ingredients/mapped/Azureomycin.yaml | maintained | Azureomycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-b6c3f8931f08d05c | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-b6c3f8931f08d05c | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-b6c3f8931f08d05c | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-b6c3f8931f08d05c.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: not_applicable. Targets: record-b6c3f8931f08d05c.

The latest legacy review reports no outstanding finding. This run verifies local consistency only; it does not renew that earlier scientific pass.

Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-16T09:12:21Z; reviewed SHA-256=7526eae4b8d62730cd4ac486066b7f92919695d5db8b90688b66a9cd3327d727; current SHA-256=7526eae4b8d62730cd4ac486066b7f92919695d5db8b90688b66a9cd3327d727; hash_changed=False. Reports=["reports/yaml_record_review/Azureomycin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The kgmicrobe.compound placeholder is intentionally retained; current OLS only finds narrower azureomycin A/B terms, not exact bare Azureomycin.

### Historical provisional-role concern

evidence: concern. Targets: record-b6c3f8931f08d05c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-cf04c97b1eb4d6cd: Reassess prediction-only role support: Azureomycin

major / open / confirmed; issue key: mim-reconciliation-role-support-b6c3f8931f08d05c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-cf04c97b1eb4d6cd

Reassess prediction-only role support: Azureomycin

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-6082d3a254957a10 | data/ingredients/mapped/Azureomycin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[539],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:azureomycin","line":541,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:azureomycin","preferred_term":"Azureomycin"}],"identifier":"kgmicrobe.compound:azureomycin","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:azureomycin","ontology_label":"Azureomycin","ontology_source":"kgmicrobe.compound"},"preferred_term":"Azureomycin","sssom_rows":[{"data_row":468,"object_id":"kgmicrobe.compound:azureomycin","object_label":"Azureomycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Azureomycin","synonym_count":0} |
| ev-e5bce7c4a9431160 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [539] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-dd3b9201533b0ff4 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Azureomycin; data-row positions=[468] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":468,"object_id":"kgmicrobe.compound:azureomycin","object_label":"Azureomycin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Azureomycin","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-606d7ccb7867957d | docs/data/mapped_ingredients.csv; CSV lines=[541] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:azureomycin","line":541,"mapping_quality":"PLACEHOLDER","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.compound:azureomycin","preferred_term":"Azureomycin","total_occurrences":"0"}] |
| ev-0c2064719d7b1df2 | reports/yaml_record_review/Azureomycin.md; &#96;data/ingredients/mapped/Azureomycin.yaml&#96;:2; Verdict:4; Identity:11; Validation:26; Evidence:40; Completeness:59; Recommended Edits:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-f3acd94978d42f14 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1580] | context_only | [{"current_record_sha256":"7526eae4b8d62730cd4ac486066b7f92919695d5db8b90688b66a9cd3327d727","finding_id":"SEM:5bc4a5365a85479d7654","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-e7f06272dbc240de | data/ingredients/mapped/Azureomycin.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}] |
| ev-75bab7e57b3b3815 | reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml; findings[finding_id=f-cf04c97b1eb4d6cd] | context_only | Predecessor structured review finding f-cf04c97b1eb4d6cd in 20261011T024631Z-mim-reconcile-all-batch-03 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-azureomycin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Azureomycin (data/ingredients/mapped/Azureomycin.yaml)'
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
summary: Per-record structured review for Azureomycin (data/ingredients/mapped/Azureomycin.yaml,
  record-b6c3f8931f08d05c, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Azureomycin.yaml
    sha256: 7526eae4b8d62730cd4ac486066b7f92919695d5db8b90688b66a9cd3327d727
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
  - path: reports/yaml_record_review/Azureomycin.md
    sha256: 045932368e6928422116b3963ab776d92f5cfc008de08e4d0f6dfd6b57957701
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-b6c3f8931f08d05c
  path: data/ingredients/mapped/Azureomycin.yaml
  label: Azureomycin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Azureomycin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Azureomycin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Azureomycin.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-b6c3f8931f08d05c
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-b6c3f8931f08d05c
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-b6c3f8931f08d05c
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-b6c3f8931f08d05c
evidence:
- evidence_id: ev-6082d3a254957a10
  kind: record_content
  reference: data/ingredients/mapped/Azureomycin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[539],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:azureomycin","line":541,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:azureomycin","preferred_term":"Azureomycin"}],"identifier":"kgmicrobe.compound:azureomycin","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:azureomycin","ontology_label":"Azureomycin","ontology_source":"kgmicrobe.compound"},"preferred_term":"Azureomycin","sssom_rows":[{"data_row":468,"object_id":"kgmicrobe.compound:azureomycin","object_label":"Azureomycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Azureomycin","synonym_count":0}'
  snapshot_sha256: 7526eae4b8d62730cd4ac486066b7f92919695d5db8b90688b66a9cd3327d727
- evidence_id: ev-e5bce7c4a9431160
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [539]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-dd3b9201533b0ff4
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Azureomycin; data-row positions=[468]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":468,"object_id":"kgmicrobe.compound:azureomycin","object_label":"Azureomycin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Azureomycin","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-606d7ccb7867957d
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[541]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:azureomycin","line":541,"mapping_quality":"PLACEHOLDER","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.compound:azureomycin","preferred_term":"Azureomycin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-0c2064719d7b1df2
  kind: prior_review
  reference: reports/yaml_record_review/Azureomycin.md
  locator: '`data/ingredients/mapped/Azureomycin.yaml`:2; Verdict:4; Identity:11;
    Validation:26; Evidence:40; Completeness:59; Recommended Edits:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 045932368e6928422116b3963ab776d92f5cfc008de08e4d0f6dfd6b57957701
  quote: 'Recommended Edits:

    - None.'
- evidence_id: ev-f3acd94978d42f14
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1580]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"7526eae4b8d62730cd4ac486066b7f92919695d5db8b90688b66a9cd3327d727","finding_id":"SEM:5bc4a5365a85479d7654","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-e7f06272dbc240de
  kind: record_content
  reference: data/ingredients/mapped/Azureomycin.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}]'
  snapshot_sha256: 7526eae4b8d62730cd4ac486066b7f92919695d5db8b90688b66a9cd3327d727
- evidence_id: ev-75bab7e57b3b3815
  kind: prior_review
  reference: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
  locator: findings[finding_id=f-cf04c97b1eb4d6cd]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-cf04c97b1eb4d6cd in 20261011T024631Z-mim-reconcile-all-batch-03
  snapshot_sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
assessments:
- assessment_id: a-e752a678c856ede6
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-b6c3f8931f08d05c
  evidence_ids:
  - ev-6082d3a254957a10
  - ev-e5bce7c4a9431160
  - ev-dd3b9201533b0ff4
  - ev-606d7ccb7867957d
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-67168c329d32cd1a
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: not_applicable
  summary: The latest legacy review reports no outstanding finding. This run verifies
    local consistency only; it does not renew that earlier scientific pass.
  target_ids:
  - record-b6c3f8931f08d05c
  evidence_ids:
  - ev-0c2064719d7b1df2
  - ev-6082d3a254957a10
  - ev-f3acd94978d42f14
  details: 'Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-16T09:12:21Z;
    reviewed SHA-256=7526eae4b8d62730cd4ac486066b7f92919695d5db8b90688b66a9cd3327d727;
    current SHA-256=7526eae4b8d62730cd4ac486066b7f92919695d5db8b90688b66a9cd3327d727;
    hash_changed=False. Reports=["reports/yaml_record_review/Azureomycin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The kgmicrobe.compound
    placeholder is intentionally retained; current OLS only finds narrower azureomycin
    A/B terms, not exact bare Azureomycin.'
  dimensions:
  - name: legacy-native-ids
    value: '["SEM:5bc4a5365a85479d7654"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-6082d3a254957a10
    - ev-0c2064719d7b1df2
    - ev-f3acd94978d42f14
- assessment_id: a-e7f06272dbc240de
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-b6c3f8931f08d05c
  evidence_ids:
  - ev-0c2064719d7b1df2
  - ev-e7f06272dbc240de
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0c2064719d7b1df2
    - ev-e7f06272dbc240de
findings:
- finding_id: rec-f-cf04c97b1eb4d6cd
  issue_key: mim-reconciliation-role-support-b6c3f8931f08d05c
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Azureomycin'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-b6c3f8931f08d05c
  evidence_ids:
  - ev-0c2064719d7b1df2
  - ev-e7f06272dbc240de
  - ev-75bab7e57b3b3815
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Azureomycin.yaml
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
    review_id: 20261011T024631Z-mim-reconcile-all-batch-03
    finding_id: f-cf04c97b1eb4d6cd
actions:
- action_id: rec-action-cf04c97b1eb4d6cd
  description: 'Reassess prediction-only role support: Azureomycin'
  finding_ids:
  - rec-f-cf04c97b1eb4d6cd
  target_ids:
  - record-b6c3f8931f08d05c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Azureomycin.yaml
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
  with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.
```
