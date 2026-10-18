# Per-record structured review: Glycylglycine (data/ingredients/mapped/Glycylglycine.yaml)

- Review: 20261017T083000Z-glycylglycine
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Glycylglycine (data/ingredients/mapped/Glycylglycine.yaml, record-81cfa3f4ed7416ca, mapping_status=REJECTED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Glycylglycine.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Glycylglycine.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-81cfa3f4ed7416ca | data/ingredients/mapped/Glycylglycine.yaml | maintained | Glycylglycine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-81cfa3f4ed7416ca | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-81cfa3f4ed7416ca | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-81cfa3f4ed7416ca | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-81cfa3f4ed7416ca.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-81cfa3f4ed7416ca.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T18:32:48Z; reviewed SHA-256=3d902b3b5870c5317df4c90d03f58ba75f356236ecb1a1dcda3a9bc4b5d461d9; current SHA-256=3d902b3b5870c5317df4c90d03f58ba75f356236ecb1a1dcda3a9bc4b5d461d9; hash_changed=False. Reports=["reports/yaml_record_review/Glycylglycine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The rejected duplicate no longer publishes a final SSSOM row, but stale active fields remain on the tombstone.

### Historical provisional-role concern

evidence: unknown. Targets: record-81cfa3f4ed7416ca.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-18c1765d74d01983: Reassess prediction-only role support: Glycylglycine

minor / deferred / provisional; issue key: mim-reconciliation-role-support-81cfa3f4ed7416ca.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

Disposition: The current local observation is recorded, but the named source/context or policy decision is still required; no correction is inferred.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-52a8c337b0bbdae6 | data/ingredients/mapped/Glycylglycine.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1082],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17201","line":1084,"mapping_status":"REJECTED","ontology_id":"CHEBI:17201","preferred_term":"Glycylglycine"}],"identifier":"CHEBI:17201","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":14,"edge_count":14,"occurrences":14},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17201","ontology_label":"glycylglycine","ontology_source":"CHEBI"},"preferred_term":"Glycylglycine","sssom_rows":[],"sssom_subject":"MIM:Glycylglycine","synonym_count":1} |
| ev-f1adbac93af583d9 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1082] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-6c35ec75a591812c | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Glycylglycine; data-row positions=[] | context_only | Current exact-subject rows, including complete other payload: [] |
| ev-910772fa7a4e58f1 | docs/data/mapped_ingredients.csv; CSV lines=[1084] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:17201","line":1084,"mapping_quality":"EXACT_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:17201","preferred_term":"Glycylglycine","total_occurrences":"0"}] |
| ev-cb184322e64f9213 | reports/yaml_record_review/Glycylglycine.md; &#96;data/ingredients/mapped/Glycylglycine.yaml&#96;:2; Verdict:4; Identity:12; Validation:23; Evidence:30; Completeness:53; Recommended Edits:61 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-95e90b5e0028d7a3 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[701] | context_only | [{"current_record_sha256":"3d902b3b5870c5317df4c90d03f58ba75f356236ecb1a1dcda3a9bc4b5d461d9","finding_id":"SEM:86d01fd2651c8b59ff87","kind":"existing_record_review","resolution_reason":"Source record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}] |
| ev-65c02b9400d6af6f | data/ingredients/mapped/Glycylglycine.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional in-session LLM role assignment; review recommended.","reference_text":"Assigned by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"BUFFER"}}] |
| ev-19f4731a53a7ed6e | reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml; findings[finding_id=f-18c1765d74d01983] | context_only | Predecessor structured review finding f-18c1765d74d01983 in 20261011T024634Z-mim-reconcile-all-batch-06 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-glycylglycine
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Glycylglycine (data/ingredients/mapped/Glycylglycine.yaml)'
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
summary: Per-record structured review for Glycylglycine (data/ingredients/mapped/Glycylglycine.yaml,
  record-81cfa3f4ed7416ca, mapping_status=REJECTED). Records 0 open finding(s) and
  1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Glycylglycine.yaml
    sha256: 3d902b3b5870c5317df4c90d03f58ba75f356236ecb1a1dcda3a9bc4b5d461d9
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
  - path: reports/yaml_record_review/Glycylglycine.md
    sha256: 850fbb65a598b4c86c57edee81c1d83650d81c12804c55b71a706c12af9ff3f4
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-81cfa3f4ed7416ca
  path: data/ingredients/mapped/Glycylglycine.yaml
  label: Glycylglycine
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glycylglycine.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Glycylglycine.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Glycylglycine.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-81cfa3f4ed7416ca
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-81cfa3f4ed7416ca
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-81cfa3f4ed7416ca
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-81cfa3f4ed7416ca
evidence:
- evidence_id: ev-52a8c337b0bbdae6
  kind: record_content
  reference: data/ingredients/mapped/Glycylglycine.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1082],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17201","line":1084,"mapping_status":"REJECTED","ontology_id":"CHEBI:17201","preferred_term":"Glycylglycine"}],"identifier":"CHEBI:17201","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":14,"edge_count":14,"occurrences":14},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17201","ontology_label":"glycylglycine","ontology_source":"CHEBI"},"preferred_term":"Glycylglycine","sssom_rows":[],"sssom_subject":"MIM:Glycylglycine","synonym_count":1}'
  snapshot_sha256: 3d902b3b5870c5317df4c90d03f58ba75f356236ecb1a1dcda3a9bc4b5d461d9
- evidence_id: ev-f1adbac93af583d9
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1082]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-6c35ec75a591812c
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Glycylglycine; data-row positions=[]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: []'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-910772fa7a4e58f1
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1084]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:17201","line":1084,"mapping_quality":"EXACT_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:17201","preferred_term":"Glycylglycine","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-cb184322e64f9213
  kind: prior_review
  reference: reports/yaml_record_review/Glycylglycine.md
  locator: '`data/ingredients/mapped/Glycylglycine.yaml`:2; Verdict:4; Identity:12;
    Validation:23; Evidence:30; Completeness:53; Recommended Edits:61'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 850fbb65a598b4c86c57edee81c1d83650d81c12804c55b71a706c12af9ff3f4
  quote: "Recommended Edits:\n- Minor: trim the rejected tombstone in\n  `data/ingredients/mapped/Glycylglycine.yaml`\
    \ to the fields needed for merge\n  provenance, or at least remove/retype the\
    \ stale `BUFFER` role and\n  `Glycylglycine(CAS: 556-50-3)` raw synonym when the\
    \ active\n  `Glycyl-glycine` synonym payload is fixed."
- evidence_id: ev-95e90b5e0028d7a3
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[701]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"3d902b3b5870c5317df4c90d03f58ba75f356236ecb1a1dcda3a9bc4b5d461d9","finding_id":"SEM:86d01fd2651c8b59ff87","kind":"existing_record_review","resolution_reason":"Source
    record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-65c02b9400d6af6f
  kind: record_content
  reference: data/ingredients/mapped/Glycylglycine.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional
    in-session LLM role assignment; review recommended.","reference_text":"Assigned
    by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"BUFFER"}}]'
  snapshot_sha256: 3d902b3b5870c5317df4c90d03f58ba75f356236ecb1a1dcda3a9bc4b5d461d9
- evidence_id: ev-19f4731a53a7ed6e
  kind: prior_review
  reference: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
  locator: findings[finding_id=f-18c1765d74d01983]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-18c1765d74d01983 in 20261011T024634Z-mim-reconcile-all-batch-06
  snapshot_sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
assessments:
- assessment_id: a-7b175ed52077c2d3
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-81cfa3f4ed7416ca
  evidence_ids:
  - ev-52a8c337b0bbdae6
  - ev-f1adbac93af583d9
  - ev-6c35ec75a591812c
  - ev-910772fa7a4e58f1
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-fc34e571c539ed2b
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-81cfa3f4ed7416ca
  evidence_ids:
  - ev-cb184322e64f9213
  - ev-52a8c337b0bbdae6
  - ev-95e90b5e0028d7a3
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T18:32:48Z;
    reviewed SHA-256=3d902b3b5870c5317df4c90d03f58ba75f356236ecb1a1dcda3a9bc4b5d461d9;
    current SHA-256=3d902b3b5870c5317df4c90d03f58ba75f356236ecb1a1dcda3a9bc4b5d461d9;
    hash_changed=False. Reports=["reports/yaml_record_review/Glycylglycine.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The rejected duplicate
    no longer publishes a final SSSOM row, but stale active fields remain on the tombstone.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-cb184322e64f9213
    - ev-52a8c337b0bbdae6
  - name: legacy-native-ids
    value: '["SEM:86d01fd2651c8b59ff87"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-52a8c337b0bbdae6
    - ev-cb184322e64f9213
    - ev-95e90b5e0028d7a3
- assessment_id: a-65c02b9400d6af6f
  area: evidence
  topic: Historical provisional-role concern
  outcome: unknown
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-81cfa3f4ed7416ca
  evidence_ids:
  - ev-cb184322e64f9213
  - ev-65c02b9400d6af6f
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-cb184322e64f9213
    - ev-65c02b9400d6af6f
findings:
- finding_id: rec-f-18c1765d74d01983
  issue_key: mim-reconciliation-role-support-81cfa3f4ed7416ca
  category: evidence
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Reassess prediction-only role support: Glycylglycine'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-81cfa3f4ed7416ca
  evidence_ids:
  - ev-cb184322e64f9213
  - ev-65c02b9400d6af6f
  - ev-19f4731a53a7ed6e
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glycylglycine.yaml
    role: maintained ingredient
  field_paths:
  - physicochemical_roles[0]
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
    review_id: 20261011T024634Z-mim-reconcile-all-batch-06
    finding_id: f-18c1765d74d01983
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
