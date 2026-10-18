# Per-record structured review: Alboverticillin (data/ingredients/mapped/Alboverticillin.yaml)

- Review: 20261017T083000Z-alboverticillin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Alboverticillin (data/ingredients/mapped/Alboverticillin.yaml, record-bdd7f0419bb2b782, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Alboverticillin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Alboverticillin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-bdd7f0419bb2b782 | data/ingredients/mapped/Alboverticillin.yaml | maintained | Alboverticillin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-bdd7f0419bb2b782 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-bdd7f0419bb2b782 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-bdd7f0419bb2b782 | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-bdd7f0419bb2b782.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-bdd7f0419bb2b782.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:31:45Z; reviewed SHA-256=bfdc3f61820466a9c73e46ce9f538574c59722266433dc6458cf6dfce77176d7; current SHA-256=bfdc3f61820466a9c73e46ce9f538574c59722266433dc6458cf6dfce77176d7; hash_changed=False. Reports=["reports/yaml_record_review/Alboverticillin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The kgmicrobe placeholder is intentionally retained after a no-hit OLS review, but SELECTIVE_AGENT is still only a provisional name-pattern prediction.

### Historical provisional-role concern

evidence: concern. Targets: record-bdd7f0419bb2b782.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-1021d02c1d655153: Reassess prediction-only role support: Alboverticillin

major / open / confirmed; issue key: mim-reconciliation-role-support-bdd7f0419bb2b782.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-1021d02c1d655153

Reassess prediction-only role support: Alboverticillin

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-e64e6afdda39ef87 | data/ingredients/mapped/Alboverticillin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[465],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:alboverticillin","line":467,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:alboverticillin","preferred_term":"Alboverticillin"}],"identifier":"kgmicrobe.compound:alboverticillin","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:alboverticillin","ontology_label":"Alboverticillin","ontology_source":"kgmicrobe.compound"},"preferred_term":"Alboverticillin","sssom_rows":[{"data_row":321,"object_id":"kgmicrobe.compound:alboverticillin","object_label":"Alboverticillin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Alboverticillin","synonym_count":0} |
| ev-2bbc9c35265c515e | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [465] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-081a8c364b02cf6c | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Alboverticillin; data-row positions=[321] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":321,"object_id":"kgmicrobe.compound:alboverticillin","object_label":"Alboverticillin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Alboverticillin","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-629981172a0f38cf | docs/data/mapped_ingredients.csv; CSV lines=[467] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:alboverticillin","line":467,"mapping_quality":"PLACEHOLDER","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.compound:alboverticillin","preferred_term":"Alboverticillin","total_occurrences":"0"}] |
| ev-a746bbd4c9211ca2 | reports/yaml_record_review/Alboverticillin.md; &#96;data/ingredients/mapped/Alboverticillin.yaml&#96;:2; Verdict:4; Identity:10; Validation:22; Evidence:35; Completeness:52; Recommended Edits:61 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-c6009ad95fcdd755 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[226,2035] | context_only | [{"current_record_sha256":"bfdc3f61820466a9c73e46ce9f538574c59722266433dc6458cf6dfce77176d7","finding_id":"SEM:11a026a8492adbec9228","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"bfdc3f61820466a9c73e46ce9f538574c59722266433dc6458cf6dfce77176d7","finding_id":"SEM:c29093fe33e799cc448e","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-0889f3ca6e3ebf50 | data/ingredients/mapped/Alboverticillin.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}] |
| ev-28d18188f8974800 | reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml; findings[finding_id=f-1021d02c1d655153] | context_only | Predecessor structured review finding f-1021d02c1d655153 in 20261011T024631Z-mim-reconcile-all-batch-03 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-alboverticillin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Alboverticillin (data/ingredients/mapped/Alboverticillin.yaml)'
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
summary: Per-record structured review for Alboverticillin (data/ingredients/mapped/Alboverticillin.yaml,
  record-bdd7f0419bb2b782, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Alboverticillin.yaml
    sha256: bfdc3f61820466a9c73e46ce9f538574c59722266433dc6458cf6dfce77176d7
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
  - path: reports/yaml_record_review/Alboverticillin.md
    sha256: afb2314b136d8d76e453930741a829a07ac4bfa21c0f643e4622f017bbbe1d91
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-bdd7f0419bb2b782
  path: data/ingredients/mapped/Alboverticillin.yaml
  label: Alboverticillin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Alboverticillin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Alboverticillin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Alboverticillin.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-bdd7f0419bb2b782
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-bdd7f0419bb2b782
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-bdd7f0419bb2b782
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-bdd7f0419bb2b782
evidence:
- evidence_id: ev-e64e6afdda39ef87
  kind: record_content
  reference: data/ingredients/mapped/Alboverticillin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[465],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:alboverticillin","line":467,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:alboverticillin","preferred_term":"Alboverticillin"}],"identifier":"kgmicrobe.compound:alboverticillin","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:alboverticillin","ontology_label":"Alboverticillin","ontology_source":"kgmicrobe.compound"},"preferred_term":"Alboverticillin","sssom_rows":[{"data_row":321,"object_id":"kgmicrobe.compound:alboverticillin","object_label":"Alboverticillin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Alboverticillin","synonym_count":0}'
  snapshot_sha256: bfdc3f61820466a9c73e46ce9f538574c59722266433dc6458cf6dfce77176d7
- evidence_id: ev-2bbc9c35265c515e
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [465]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-081a8c364b02cf6c
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Alboverticillin; data-row positions=[321]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":321,"object_id":"kgmicrobe.compound:alboverticillin","object_label":"Alboverticillin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Alboverticillin","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-629981172a0f38cf
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[467]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:alboverticillin","line":467,"mapping_quality":"PLACEHOLDER","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.compound:alboverticillin","preferred_term":"Alboverticillin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-a746bbd4c9211ca2
  kind: prior_review
  reference: reports/yaml_record_review/Alboverticillin.md
  locator: '`data/ingredients/mapped/Alboverticillin.yaml`:2; Verdict:4; Identity:10;
    Validation:22; Evidence:35; Completeness:52; Recommended Edits:61'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: afb2314b136d8d76e453930741a829a07ac4bfa21c0f643e4622f017bbbe1d91
  quote: "Recommended Edits:\n- Either cite claim-level evidence for alboverticillin\
    \ as a selective agent in\n  microbial media, or remove `physicochemical_roles.SELECTIVE_AGENT`\
    \ from\n  `data/ingredients/mapped/Alboverticillin.yaml`.\n- Regenerate synchronized\
    \ products, then rerun\n  `uv run --frozen python scripts/validate_strict.py`,\n\
    \  `uv run --frozen python scripts/validate_component_partonomy.py`, and\n  `uv\
    \ run --frozen python scripts/validate_sssom_invariants.py`."
- evidence_id: ev-c6009ad95fcdd755
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[226,2035]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"bfdc3f61820466a9c73e46ce9f538574c59722266433dc6458cf6dfce77176d7","finding_id":"SEM:11a026a8492adbec9228","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"bfdc3f61820466a9c73e46ce9f538574c59722266433dc6458cf6dfce77176d7","finding_id":"SEM:c29093fe33e799cc448e","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-0889f3ca6e3ebf50
  kind: record_content
  reference: data/ingredients/mapped/Alboverticillin.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}]'
  snapshot_sha256: bfdc3f61820466a9c73e46ce9f538574c59722266433dc6458cf6dfce77176d7
- evidence_id: ev-28d18188f8974800
  kind: prior_review
  reference: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
  locator: findings[finding_id=f-1021d02c1d655153]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-1021d02c1d655153 in 20261011T024631Z-mim-reconcile-all-batch-03
  snapshot_sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
assessments:
- assessment_id: a-cf66cbabad7aff1a
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-bdd7f0419bb2b782
  evidence_ids:
  - ev-e64e6afdda39ef87
  - ev-2bbc9c35265c515e
  - ev-081a8c364b02cf6c
  - ev-629981172a0f38cf
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-9718b71b1c414e1a
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-bdd7f0419bb2b782
  evidence_ids:
  - ev-a746bbd4c9211ca2
  - ev-e64e6afdda39ef87
  - ev-c6009ad95fcdd755
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:31:45Z;
    reviewed SHA-256=bfdc3f61820466a9c73e46ce9f538574c59722266433dc6458cf6dfce77176d7;
    current SHA-256=bfdc3f61820466a9c73e46ce9f538574c59722266433dc6458cf6dfce77176d7;
    hash_changed=False. Reports=["reports/yaml_record_review/Alboverticillin.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The kgmicrobe
    placeholder is intentionally retained after a no-hit OLS review, but SELECTIVE_AGENT
    is still only a provisional name-pattern prediction.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-a746bbd4c9211ca2
    - ev-e64e6afdda39ef87
  - name: legacy-native-ids
    value: '["SEM:11a026a8492adbec9228","SEM:c29093fe33e799cc448e"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-e64e6afdda39ef87
    - ev-a746bbd4c9211ca2
    - ev-c6009ad95fcdd755
- assessment_id: a-0889f3ca6e3ebf50
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-bdd7f0419bb2b782
  evidence_ids:
  - ev-a746bbd4c9211ca2
  - ev-0889f3ca6e3ebf50
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-a746bbd4c9211ca2
    - ev-0889f3ca6e3ebf50
findings:
- finding_id: rec-f-1021d02c1d655153
  issue_key: mim-reconciliation-role-support-bdd7f0419bb2b782
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Alboverticillin'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-bdd7f0419bb2b782
  evidence_ids:
  - ev-a746bbd4c9211ca2
  - ev-0889f3ca6e3ebf50
  - ev-28d18188f8974800
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Alboverticillin.yaml
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
    finding_id: f-1021d02c1d655153
actions:
- action_id: rec-action-1021d02c1d655153
  description: 'Reassess prediction-only role support: Alboverticillin'
  finding_ids:
  - rec-f-1021d02c1d655153
  target_ids:
  - record-bdd7f0419bb2b782
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Alboverticillin.yaml
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
