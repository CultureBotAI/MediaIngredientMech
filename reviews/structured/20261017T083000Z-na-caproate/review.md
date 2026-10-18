# Per-record structured review: Na-caproate (data/ingredients/mapped/Na-caproate.yaml)

- Review: 20261017T083000Z-na-caproate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Na-caproate (data/ingredients/mapped/Na-caproate.yaml, record-cd441cb8f0ddec4c, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Na-caproate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Na-caproate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-cd441cb8f0ddec4c | data/ingredients/mapped/Na-caproate.yaml | maintained | Na-caproate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-cd441cb8f0ddec4c | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-cd441cb8f0ddec4c | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-cd441cb8f0ddec4c | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-cd441cb8f0ddec4c.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-cd441cb8f0ddec4c.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T04:50:08Z; reviewed SHA-256=870041a253a626e5a82110191012c81539c524557e6f879321a3fe4acad3d586; current SHA-256=870041a253a626e5a82110191012c81539c524557e6f879321a3fe4acad3d586; hash_changed=False. Reports=["reports/yaml_record_review/Na-caproate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:114126 sodium hexanoate identity, CAS-backed structure, occurrence count, synonyms, and final exact row pass, but CARBON_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-cd441cb8f0ddec4c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-c44415f5e26fbd58: Reassess prediction-only role support: Na-caproate

major / open / confirmed; issue key: mim-reconciliation-role-support-cd441cb8f0ddec4c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-c44415f5e26fbd58

Reassess prediction-only role support: Na-caproate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-8ce5b20b2f65ead7 | data/ingredients/mapped/Na-caproate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1463],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:114126","line":1465,"mapping_status":"MAPPED","ontology_id":"CHEBI:114126","preferred_term":"Na-caproate"}],"identifier":"CHEBI:114126","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":10,"edge_count":10,"occurrences":10},"occurrence_statistics":{"media_count":10,"total_occurrences":10},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:114126","ontology_label":"sodium hexanoate","ontology_source":"CHEBI"},"preferred_term":"Na-caproate","sssom_rows":[{"data_row":1965,"object_id":"CHEBI:114126","object_label":"sodium hexanoate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na-caproate","synonym_count":6} |
| ev-65820e32b6ce2ec3 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1463] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-59722249efb0e262 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Na-caproate; data-row positions=[1965] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1965,"object_id":"CHEBI:114126","object_label":"sodium hexanoate","other":"Hexanoic acid, sodium salt&#124;Sodium caproate&#124;Sodium capronate&#124;Sodium n-caproate&#124;CAS:10051-44-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Na-caproate","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-85974aaf9d4b78e6 | docs/data/mapped_ingredients.csv; CSV lines=[1465] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:114126","line":1465,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"10","ontology_id":"CHEBI:114126","preferred_term":"Na-caproate","total_occurrences":"10"}] |
| ev-3747170e3a4ce387 | reports/yaml_record_review/Na-caproate.md; &#96;data/ingredients/mapped/Na-caproate.yaml&#96;:2; Verdict:4; Identity:11; Validation:20; Evidence:27; Completeness:42; Recommended Edits:48 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-1cd403416717a7fd | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[972,1958] | context_only | [{"current_record_sha256":"870041a253a626e5a82110191012c81539c524557e6f879321a3fe4acad3d586","finding_id":"SEM:e88d529a4c8d64bc10ef","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"870041a253a626e5a82110191012c81539c524557e6f879321a3fe4acad3d586","finding_id":"SEM:b1c4cff64800f68393a8","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-d26630187bb1dc0c | data/ingredients/mapped/Na-caproate.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}] |
| ev-274077046cce9ffe | reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml; findings[finding_id=f-c44415f5e26fbd58] | context_only | Predecessor structured review finding f-c44415f5e26fbd58 in 20261011T024637Z-mim-reconcile-all-batch-09 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-na-caproate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Na-caproate (data/ingredients/mapped/Na-caproate.yaml)'
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
summary: Per-record structured review for Na-caproate (data/ingredients/mapped/Na-caproate.yaml,
  record-cd441cb8f0ddec4c, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Na-caproate.yaml
    sha256: 870041a253a626e5a82110191012c81539c524557e6f879321a3fe4acad3d586
    role: target
  - path: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
    sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
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
  - path: reports/yaml_record_review/Na-caproate.md
    sha256: ec4013bf7f7c8be49c8f0f7440721b66353d5ee64d14b1aa394378aa2c317b86
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-cd441cb8f0ddec4c
  path: data/ingredients/mapped/Na-caproate.yaml
  label: Na-caproate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na-caproate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Na-caproate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Na-caproate.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-cd441cb8f0ddec4c
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-cd441cb8f0ddec4c
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-cd441cb8f0ddec4c
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-cd441cb8f0ddec4c
evidence:
- evidence_id: ev-8ce5b20b2f65ead7
  kind: record_content
  reference: data/ingredients/mapped/Na-caproate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1463],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:114126","line":1465,"mapping_status":"MAPPED","ontology_id":"CHEBI:114126","preferred_term":"Na-caproate"}],"identifier":"CHEBI:114126","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":10,"edge_count":10,"occurrences":10},"occurrence_statistics":{"media_count":10,"total_occurrences":10},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:114126","ontology_label":"sodium
    hexanoate","ontology_source":"CHEBI"},"preferred_term":"Na-caproate","sssom_rows":[{"data_row":1965,"object_id":"CHEBI:114126","object_label":"sodium
    hexanoate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na-caproate","synonym_count":6}'
  snapshot_sha256: 870041a253a626e5a82110191012c81539c524557e6f879321a3fe4acad3d586
- evidence_id: ev-65820e32b6ce2ec3
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1463]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-59722249efb0e262
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Na-caproate; data-row positions=[1965]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1965,"object_id":"CHEBI:114126","object_label":"sodium
    hexanoate","other":"Hexanoic acid, sodium salt|Sodium caproate|Sodium capronate|Sodium
    n-caproate|CAS:10051-44-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Na-caproate","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-85974aaf9d4b78e6
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1465]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:114126","line":1465,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"10","ontology_id":"CHEBI:114126","preferred_term":"Na-caproate","total_occurrences":"10"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-3747170e3a4ce387
  kind: prior_review
  reference: reports/yaml_record_review/Na-caproate.md
  locator: '`data/ingredients/mapped/Na-caproate.yaml`:2; Verdict:4; Identity:11;
    Validation:20; Evidence:27; Completeness:42; Recommended Edits:48'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: ec4013bf7f7c8be49c8f0f7440721b66353d5ee64d14b1aa394378aa2c317b86
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Na-caproate.yaml`,\
    \ either remove\n  `nutritional_roles.CARBON_SOURCE` or replace its name-pattern\
    \ placeholder with\n  source-backed evidence from the maintained CultureMech role-text\
    \ input that\n  says this ingredient is a carbon source. Rerun strict validation\
    \ and the\n  role/output SSSOM checks after the role facet changes."
- evidence_id: ev-1cd403416717a7fd
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[972,1958]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"870041a253a626e5a82110191012c81539c524557e6f879321a3fe4acad3d586","finding_id":"SEM:e88d529a4c8d64bc10ef","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"870041a253a626e5a82110191012c81539c524557e6f879321a3fe4acad3d586","finding_id":"SEM:b1c4cff64800f68393a8","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-d26630187bb1dc0c
  kind: record_content
  reference: data/ingredients/mapped/Na-caproate.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}]'
  snapshot_sha256: 870041a253a626e5a82110191012c81539c524557e6f879321a3fe4acad3d586
- evidence_id: ev-274077046cce9ffe
  kind: prior_review
  reference: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
  locator: findings[finding_id=f-c44415f5e26fbd58]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-c44415f5e26fbd58 in 20261011T024637Z-mim-reconcile-all-batch-09
  snapshot_sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
assessments:
- assessment_id: a-46534b9d1105ff61
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-cd441cb8f0ddec4c
  evidence_ids:
  - ev-8ce5b20b2f65ead7
  - ev-65820e32b6ce2ec3
  - ev-59722249efb0e262
  - ev-85974aaf9d4b78e6
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-2a7e494c8c7d7975
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-cd441cb8f0ddec4c
  evidence_ids:
  - ev-3747170e3a4ce387
  - ev-8ce5b20b2f65ead7
  - ev-1cd403416717a7fd
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T04:50:08Z;
    reviewed SHA-256=870041a253a626e5a82110191012c81539c524557e6f879321a3fe4acad3d586;
    current SHA-256=870041a253a626e5a82110191012c81539c524557e6f879321a3fe4acad3d586;
    hash_changed=False. Reports=["reports/yaml_record_review/Na-caproate.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI:114126
    sodium hexanoate identity, CAS-backed structure, occurrence count, synonyms, and
    final exact row pass, but CARBON_SOURCE is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-3747170e3a4ce387
    - ev-8ce5b20b2f65ead7
  - name: legacy-native-ids
    value: '["SEM:e88d529a4c8d64bc10ef","SEM:b1c4cff64800f68393a8"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-8ce5b20b2f65ead7
    - ev-3747170e3a4ce387
    - ev-1cd403416717a7fd
- assessment_id: a-d26630187bb1dc0c
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-cd441cb8f0ddec4c
  evidence_ids:
  - ev-3747170e3a4ce387
  - ev-d26630187bb1dc0c
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-3747170e3a4ce387
    - ev-d26630187bb1dc0c
findings:
- finding_id: rec-f-c44415f5e26fbd58
  issue_key: mim-reconciliation-role-support-cd441cb8f0ddec4c
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Na-caproate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-cd441cb8f0ddec4c
  evidence_ids:
  - ev-3747170e3a4ce387
  - ev-d26630187bb1dc0c
  - ev-274077046cce9ffe
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na-caproate.yaml
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
    review_id: 20261011T024637Z-mim-reconcile-all-batch-09
    finding_id: f-c44415f5e26fbd58
actions:
- action_id: rec-action-c44415f5e26fbd58
  description: 'Reassess prediction-only role support: Na-caproate'
  finding_ids:
  - rec-f-c44415f5e26fbd58
  target_ids:
  - record-cd441cb8f0ddec4c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na-caproate.yaml
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
  with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.
```
