# Per-record structured review: Adenomycin (data/ingredients/mapped/Adenomycin.yaml)

- Review: 20261017T083000Z-adenomycin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Adenomycin (data/ingredients/mapped/Adenomycin.yaml, record-59def74ade9b119e, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Adenomycin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Adenomycin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-59def74ade9b119e | data/ingredients/mapped/Adenomycin.yaml | maintained | Adenomycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-59def74ade9b119e | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-59def74ade9b119e | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-59def74ade9b119e | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-59def74ade9b119e.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-59def74ade9b119e.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:20:04Z; reviewed SHA-256=2433bb3d3b37534cebeb11091c1a95ee2c27024910b966413e04ca5f76bdafed; current SHA-256=2433bb3d3b37534cebeb11091c1a95ee2c27024910b966413e04ca5f76bdafed; hash_changed=False. Reports=["reports/yaml_record_review/Adenomycin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact NCIT grounding is supported, but the SELECTIVE_AGENT role is still only provisional computational curation.

### Historical provisional-role concern

evidence: concern. Targets: record-59def74ade9b119e.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-354d37a4d9ffcc0e: Reassess prediction-only role support: Adenomycin

major / open / confirmed; issue key: mim-reconciliation-role-support-59def74ade9b119e.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-354d37a4d9ffcc0e

Reassess prediction-only role support: Adenomycin

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-4d74f25faf07979f | data/ingredients/mapped/Adenomycin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[455],"raw_equal":true},"docs_rows":[{"identifier":"NCIT:C221830","line":457,"mapping_status":"MAPPED","ontology_id":"NCIT:C221830","preferred_term":"Adenomycin"}],"identifier":"NCIT:C221830","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"NCIT:C221830","ontology_label":"Adenomycin","ontology_source":"NCIT"},"preferred_term":"Adenomycin","sssom_rows":[{"data_row":305,"object_id":"NCIT:C221830","object_label":"Adenomycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Adenomycin","synonym_count":0} |
| ev-27dc9b73319365b6 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [455] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-1933cc17ca0a5b0f | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Adenomycin; data-row positions=[305] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":305,"object_id":"NCIT:C221830","object_label":"Adenomycin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Adenomycin","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-68d8fc431fa8f583 | docs/data/mapped_ingredients.csv; CSV lines=[457] | supports | Published identity and count rows inspected: [{"identifier":"NCIT:C221830","line":457,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"NCIT:C221830","preferred_term":"Adenomycin","total_occurrences":"0"}] |
| ev-7d8bcf1c2aa18274 | reports/yaml_record_review/Adenomycin.md; &#96;data/ingredients/mapped/Adenomycin.yaml&#96;:2; Verdict:4; Identity:9; Validation:22; Evidence:36; Completeness:53; Recommended Edits:60 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-e9044ae93f23faa2 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[213,1803] | context_only | [{"current_record_sha256":"2433bb3d3b37534cebeb11091c1a95ee2c27024910b966413e04ca5f76bdafed","finding_id":"SEM:7196bcfbb00f9574f76a","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"2433bb3d3b37534cebeb11091c1a95ee2c27024910b966413e04ca5f76bdafed","finding_id":"SEM:2da37714d7559f6fde70","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-2b99f1be6c9d2e8a | data/ingredients/mapped/Adenomycin.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}] |
| ev-81f5761d5f5d3bfd | reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml; findings[finding_id=f-354d37a4d9ffcc0e] | context_only | Predecessor structured review finding f-354d37a4d9ffcc0e in 20261011T024631Z-mim-reconcile-all-batch-03 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-adenomycin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Adenomycin (data/ingredients/mapped/Adenomycin.yaml)'
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
summary: Per-record structured review for Adenomycin (data/ingredients/mapped/Adenomycin.yaml,
  record-59def74ade9b119e, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Adenomycin.yaml
    sha256: 2433bb3d3b37534cebeb11091c1a95ee2c27024910b966413e04ca5f76bdafed
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
  - path: reports/yaml_record_review/Adenomycin.md
    sha256: e8f18284eb3c4e4015b7b37cd29362f71c009c3bbf293df72ec6f6db6ab4cf17
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-59def74ade9b119e
  path: data/ingredients/mapped/Adenomycin.yaml
  label: Adenomycin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Adenomycin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Adenomycin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Adenomycin.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-59def74ade9b119e
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-59def74ade9b119e
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-59def74ade9b119e
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-59def74ade9b119e
evidence:
- evidence_id: ev-4d74f25faf07979f
  kind: record_content
  reference: data/ingredients/mapped/Adenomycin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[455],"raw_equal":true},"docs_rows":[{"identifier":"NCIT:C221830","line":457,"mapping_status":"MAPPED","ontology_id":"NCIT:C221830","preferred_term":"Adenomycin"}],"identifier":"NCIT:C221830","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"NCIT:C221830","ontology_label":"Adenomycin","ontology_source":"NCIT"},"preferred_term":"Adenomycin","sssom_rows":[{"data_row":305,"object_id":"NCIT:C221830","object_label":"Adenomycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Adenomycin","synonym_count":0}'
  snapshot_sha256: 2433bb3d3b37534cebeb11091c1a95ee2c27024910b966413e04ca5f76bdafed
- evidence_id: ev-27dc9b73319365b6
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [455]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-1933cc17ca0a5b0f
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Adenomycin; data-row positions=[305]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":305,"object_id":"NCIT:C221830","object_label":"Adenomycin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Adenomycin","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-68d8fc431fa8f583
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[457]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"NCIT:C221830","line":457,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"NCIT:C221830","preferred_term":"Adenomycin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-7d8bcf1c2aa18274
  kind: prior_review
  reference: reports/yaml_record_review/Adenomycin.md
  locator: '`data/ingredients/mapped/Adenomycin.yaml`:2; Verdict:4; Identity:9; Validation:22;
    Evidence:36; Completeness:53; Recommended Edits:60'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: e8f18284eb3c4e4015b7b37cd29362f71c009c3bbf293df72ec6f6db6ab4cf17
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/Adenomycin.yaml`, remove\
    \ or evidence the\n  provisional `physicochemical_roles.SELECTIVE_AGENT` assertion,\
    \ then run\n  `uv run --frozen python scripts/validate_strict.py`, `uv run --frozen\
    \ python scripts/validate_component_partonomy.py`,\n  and `uv run --frozen python\
    \ scripts/validate_sssom_invariants.py`."
- evidence_id: ev-e9044ae93f23faa2
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[213,1803]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"2433bb3d3b37534cebeb11091c1a95ee2c27024910b966413e04ca5f76bdafed","finding_id":"SEM:7196bcfbb00f9574f76a","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"2433bb3d3b37534cebeb11091c1a95ee2c27024910b966413e04ca5f76bdafed","finding_id":"SEM:2da37714d7559f6fde70","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-2b99f1be6c9d2e8a
  kind: record_content
  reference: data/ingredients/mapped/Adenomycin.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}]'
  snapshot_sha256: 2433bb3d3b37534cebeb11091c1a95ee2c27024910b966413e04ca5f76bdafed
- evidence_id: ev-81f5761d5f5d3bfd
  kind: prior_review
  reference: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
  locator: findings[finding_id=f-354d37a4d9ffcc0e]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-354d37a4d9ffcc0e in 20261011T024631Z-mim-reconcile-all-batch-03
  snapshot_sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
assessments:
- assessment_id: a-1212ea703fa8c197
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-59def74ade9b119e
  evidence_ids:
  - ev-4d74f25faf07979f
  - ev-27dc9b73319365b6
  - ev-1933cc17ca0a5b0f
  - ev-68d8fc431fa8f583
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-ef931c641e0ed514
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-59def74ade9b119e
  evidence_ids:
  - ev-7d8bcf1c2aa18274
  - ev-4d74f25faf07979f
  - ev-e9044ae93f23faa2
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:20:04Z;
    reviewed SHA-256=2433bb3d3b37534cebeb11091c1a95ee2c27024910b966413e04ca5f76bdafed;
    current SHA-256=2433bb3d3b37534cebeb11091c1a95ee2c27024910b966413e04ca5f76bdafed;
    hash_changed=False. Reports=["reports/yaml_record_review/Adenomycin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact NCIT
    grounding is supported, but the SELECTIVE_AGENT role is still only provisional
    computational curation.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-7d8bcf1c2aa18274
    - ev-4d74f25faf07979f
  - name: legacy-native-ids
    value: '["SEM:7196bcfbb00f9574f76a","SEM:2da37714d7559f6fde70"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-4d74f25faf07979f
    - ev-7d8bcf1c2aa18274
    - ev-e9044ae93f23faa2
- assessment_id: a-2b99f1be6c9d2e8a
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-59def74ade9b119e
  evidence_ids:
  - ev-7d8bcf1c2aa18274
  - ev-2b99f1be6c9d2e8a
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-7d8bcf1c2aa18274
    - ev-2b99f1be6c9d2e8a
findings:
- finding_id: rec-f-354d37a4d9ffcc0e
  issue_key: mim-reconciliation-role-support-59def74ade9b119e
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Adenomycin'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-59def74ade9b119e
  evidence_ids:
  - ev-7d8bcf1c2aa18274
  - ev-2b99f1be6c9d2e8a
  - ev-81f5761d5f5d3bfd
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Adenomycin.yaml
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
    finding_id: f-354d37a4d9ffcc0e
actions:
- action_id: rec-action-354d37a4d9ffcc0e
  description: 'Reassess prediction-only role support: Adenomycin'
  finding_ids:
  - rec-f-354d37a4d9ffcc0e
  target_ids:
  - record-59def74ade9b119e
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Adenomycin.yaml
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
