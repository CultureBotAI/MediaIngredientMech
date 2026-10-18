# Per-record structured review: 3-O-methyl-glucose (data/ingredients/mapped/3-O-methyl-glucose.yaml)

- Review: 20261017T083000Z-3-o-methyl-glucose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 3-O-methyl-glucose (data/ingredients/mapped/3-O-methyl-glucose.yaml, record-e67b09720348917c, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/3-O-methyl-glucose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/3-O-methyl-glucose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-e67b09720348917c | data/ingredients/mapped/3-O-methyl-glucose.yaml | maintained | 3-O-methyl-glucose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-e67b09720348917c | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-e67b09720348917c | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-e67b09720348917c | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-e67b09720348917c.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-e67b09720348917c.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T05:58:44Z; reviewed SHA-256=94db4b3fd0beec97b1eca146749dfdd9e4d2b0512c51c99c9f24e154003952d1; current SHA-256=94db4b3fd0beec97b1eca146749dfdd9e4d2b0512c51c99c9f24e154003952d1; hash_changed=False. Reports=["reports/yaml_record_review/3-O-methyl-glucose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Active CHEBI identity, chemistry, SSSOM, and aggregate pass, but CARBON_SOURCE is provisional and contradicts the local energy-substrate exclusion.

### Historical provisional-role concern

evidence: concern. Targets: record-e67b09720348917c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-bcd0554f797ffa19: Reassess prediction-only role support: 3-O-methyl-glucose

major / open / confirmed; issue key: mim-reconciliation-role-support-e67b09720348917c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-bcd0554f797ffa19

Reassess prediction-only role support: 3-O-methyl-glucose

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-f53acf004b7ce7f5 | data/ingredients/mapped/3-O-methyl-glucose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[355],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:73918","line":357,"mapping_status":"MAPPED","ontology_id":"CHEBI:73918","preferred_term":"3-O-methyl-glucose"}],"identifier":"CHEBI:73918","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:73918","ontology_label":"3-O-methyl-D-glucose","ontology_source":"CHEBI"},"preferred_term":"3-O-methyl-glucose","sssom_rows":[{"data_row":130,"object_id":"CHEBI:73918","object_label":"3-O-methyl-D-glucose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:3-O-methyl-glucose","synonym_count":1} |
| ev-7ecd0522c30793ca | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [355] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-1b8e1a6a7ff27208 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:3-O-methyl-glucose; data-row positions=[130] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":130,"object_id":"CHEBI:73918","object_label":"3-O-methyl-D-glucose","other":"3-methylglucose&#124;CAS:146-72-5","predicate_id":"skos:exactMatch","subject_id":"MIM:3-O-methyl-glucose","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-3d1f821ea9bf6ebe | docs/data/mapped_ingredients.csv; CSV lines=[357] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:73918","line":357,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:73918","preferred_term":"3-O-methyl-glucose","total_occurrences":"0"}] |
| ev-9e76d30c2ddb162d | reports/yaml_record_review/3-O-methyl-glucose.md; &#96;data/ingredients/mapped/3-O-methyl-glucose.yaml&#96;:2; Verdict:4; Identity:12; Validation:25; Evidence:39; Completeness:55; Recommended Edits:61 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-a60b625cd32432a0 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[109,1522] | context_only | [{"current_record_sha256":"94db4b3fd0beec97b1eca146749dfdd9e4d2b0512c51c99c9f24e154003952d1","finding_id":"SEM:a14aff5659919ff736a3","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"94db4b3fd0beec97b1eca146749dfdd9e4d2b0512c51c99c9f24e154003952d1","finding_id":"SEM:c970e95740be37dd82a1","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-d23539e8d1ba0183 | data/ingredients/mapped/3-O-methyl-glucose.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}] |
| ev-bd7d5da5d63faad3 | reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml; findings[finding_id=f-bcd0554f797ffa19] | context_only | Predecessor structured review finding f-bcd0554f797ffa19 in 20261011T024630Z-mim-reconcile-all-batch-02 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-3-o-methyl-glucose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 3-O-methyl-glucose (data/ingredients/mapped/3-O-methyl-glucose.yaml)'
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
summary: Per-record structured review for 3-O-methyl-glucose (data/ingredients/mapped/3-O-methyl-glucose.yaml,
  record-e67b09720348917c, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/3-O-methyl-glucose.yaml
    sha256: 94db4b3fd0beec97b1eca146749dfdd9e4d2b0512c51c99c9f24e154003952d1
    role: target
  - path: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
    sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
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
  - path: reports/yaml_record_review/3-O-methyl-glucose.md
    sha256: a0220270312deb9760baaa8b42f64372e46c6e241e0851cfe049ab59640ddf80
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-e67b09720348917c
  path: data/ingredients/mapped/3-O-methyl-glucose.yaml
  label: 3-O-methyl-glucose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/3-O-methyl-glucose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/3-O-methyl-glucose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/3-O-methyl-glucose.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-e67b09720348917c
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-e67b09720348917c
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-e67b09720348917c
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-e67b09720348917c
evidence:
- evidence_id: ev-f53acf004b7ce7f5
  kind: record_content
  reference: data/ingredients/mapped/3-O-methyl-glucose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[355],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:73918","line":357,"mapping_status":"MAPPED","ontology_id":"CHEBI:73918","preferred_term":"3-O-methyl-glucose"}],"identifier":"CHEBI:73918","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:73918","ontology_label":"3-O-methyl-D-glucose","ontology_source":"CHEBI"},"preferred_term":"3-O-methyl-glucose","sssom_rows":[{"data_row":130,"object_id":"CHEBI:73918","object_label":"3-O-methyl-D-glucose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:3-O-methyl-glucose","synonym_count":1}'
  snapshot_sha256: 94db4b3fd0beec97b1eca146749dfdd9e4d2b0512c51c99c9f24e154003952d1
- evidence_id: ev-7ecd0522c30793ca
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [355]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-1b8e1a6a7ff27208
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:3-O-methyl-glucose; data-row positions=[130]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":130,"object_id":"CHEBI:73918","object_label":"3-O-methyl-D-glucose","other":"3-methylglucose|CAS:146-72-5","predicate_id":"skos:exactMatch","subject_id":"MIM:3-O-methyl-glucose","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-3d1f821ea9bf6ebe
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[357]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:73918","line":357,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:73918","preferred_term":"3-O-methyl-glucose","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-9e76d30c2ddb162d
  kind: prior_review
  reference: reports/yaml_record_review/3-O-methyl-glucose.md
  locator: '`data/ingredients/mapped/3-O-methyl-glucose.yaml`:2; Verdict:4; Identity:12;
    Validation:25; Evidence:39; Completeness:55; Recommended Edits:61'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: a0220270312deb9760baaa8b42f64372e46c6e241e0851cfe049ab59640ddf80
  quote: "Recommended Edits:\n1. In `data/ingredients/mapped/3-O-methyl-glucose.yaml`,\
    \ remove\n   `nutritional_roles.CARBON_SOURCE` or replace it with direct medium-use\n\
    \   evidence scoped to organisms and conditions where this compound is actually\n\
    \   a usable carbon source.\n2. Run the per-record strict validator, compare the\
    \ record against\n   `data/curated/mapped_ingredients.yaml`, rebuild the SSSOM/docs\
    \ with the\n   maintained generators, and then rerun the whole-corpus SSSOM and\
    \ flat-export\n   checks."
- evidence_id: ev-a60b625cd32432a0
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[109,1522]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"94db4b3fd0beec97b1eca146749dfdd9e4d2b0512c51c99c9f24e154003952d1","finding_id":"SEM:a14aff5659919ff736a3","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"94db4b3fd0beec97b1eca146749dfdd9e4d2b0512c51c99c9f24e154003952d1","finding_id":"SEM:c970e95740be37dd82a1","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-d23539e8d1ba0183
  kind: record_content
  reference: data/ingredients/mapped/3-O-methyl-glucose.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}]'
  snapshot_sha256: 94db4b3fd0beec97b1eca146749dfdd9e4d2b0512c51c99c9f24e154003952d1
- evidence_id: ev-bd7d5da5d63faad3
  kind: prior_review
  reference: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
  locator: findings[finding_id=f-bcd0554f797ffa19]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-bcd0554f797ffa19 in 20261011T024630Z-mim-reconcile-all-batch-02
  snapshot_sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
assessments:
- assessment_id: a-ecbb9be80d6935fe
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-e67b09720348917c
  evidence_ids:
  - ev-f53acf004b7ce7f5
  - ev-7ecd0522c30793ca
  - ev-1b8e1a6a7ff27208
  - ev-3d1f821ea9bf6ebe
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-89308c2536835f4f
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-e67b09720348917c
  evidence_ids:
  - ev-9e76d30c2ddb162d
  - ev-f53acf004b7ce7f5
  - ev-a60b625cd32432a0
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T05:58:44Z;
    reviewed SHA-256=94db4b3fd0beec97b1eca146749dfdd9e4d2b0512c51c99c9f24e154003952d1;
    current SHA-256=94db4b3fd0beec97b1eca146749dfdd9e4d2b0512c51c99c9f24e154003952d1;
    hash_changed=False. Reports=["reports/yaml_record_review/3-O-methyl-glucose.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Active CHEBI
    identity, chemistry, SSSOM, and aggregate pass, but CARBON_SOURCE is provisional
    and contradicts the local energy-substrate exclusion.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-9e76d30c2ddb162d
    - ev-f53acf004b7ce7f5
  - name: legacy-native-ids
    value: '["SEM:a14aff5659919ff736a3","SEM:c970e95740be37dd82a1"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-f53acf004b7ce7f5
    - ev-9e76d30c2ddb162d
    - ev-a60b625cd32432a0
- assessment_id: a-d23539e8d1ba0183
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-e67b09720348917c
  evidence_ids:
  - ev-9e76d30c2ddb162d
  - ev-d23539e8d1ba0183
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-9e76d30c2ddb162d
    - ev-d23539e8d1ba0183
findings:
- finding_id: rec-f-bcd0554f797ffa19
  issue_key: mim-reconciliation-role-support-e67b09720348917c
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: 3-O-methyl-glucose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-e67b09720348917c
  evidence_ids:
  - ev-9e76d30c2ddb162d
  - ev-d23539e8d1ba0183
  - ev-bd7d5da5d63faad3
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/3-O-methyl-glucose.yaml
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
    review_id: 20261011T024630Z-mim-reconcile-all-batch-02
    finding_id: f-bcd0554f797ffa19
actions:
- action_id: rec-action-bcd0554f797ffa19
  description: 'Reassess prediction-only role support: 3-O-methyl-glucose'
  finding_ids:
  - rec-f-bcd0554f797ffa19
  target_ids:
  - record-e67b09720348917c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/3-O-methyl-glucose.yaml
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
  with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.
```
