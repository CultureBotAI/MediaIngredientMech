# Per-record structured review: Na2moo4_X_7_H2o (data/ingredients/mapped/Na2moo4_X_7_H2o.yaml)

- Review: 20261017T083000Z-na2moo4-x-7-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Na2moo4_X_7_H2o (data/ingredients/mapped/Na2moo4_X_7_H2o.yaml, record-d41203d614779c47, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Na2moo4_X_7_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Na2moo4_X_7_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-d41203d614779c47 | data/ingredients/mapped/Na2moo4_X_7_H2o.yaml | maintained | Na2moo4_X_7_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-d41203d614779c47 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-d41203d614779c47 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-d41203d614779c47 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-d41203d614779c47.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-d41203d614779c47.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:24:19Z; reviewed SHA-256=c38475fd99369be070f4498f2fc6af0159695713a28ff1383a73e69d1e1fc6e8; current SHA-256=c38475fd99369be070f4498f2fc6af0159695713a28ff1383a73e69d1e1fc6e8; hash_changed=False. Reports=["reports/yaml_record_review/Na2moo4_X_7_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:86473 sodium molybdate heptahydrate identity passes, but TRACE_ELEMENT is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-d41203d614779c47.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-afb54daf8f9945c4: Reassess prediction-only role support: Na2MoO4 x 7 H2O

major / open / confirmed; issue key: mim-reconciliation-role-support-d41203d614779c47.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-afb54daf8f9945c4

Reassess prediction-only role support: Na2MoO4 x 7 H2O

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-35ddb92a4e9f3d48 | data/ingredients/mapped/Na2moo4_X_7_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1497],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:86473","line":1499,"mapping_status":"MAPPED","ontology_id":"CHEBI:86473","preferred_term":"Na2MoO4 x 7 H2O"}],"identifier":"CHEBI:86473","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":6,"edge_count":6,"occurrences":6},"occurrence_statistics":{"media_count":6,"total_occurrences":6},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:86473","ontology_label":"sodium molybdate heptahydrate","ontology_source":"CHEBI"},"preferred_term":"Na2MoO4 x 7 H2O","sssom_rows":[{"data_row":2007,"object_id":"CHEBI:86473","object_label":"sodium molybdate heptahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2moo4_X_7_H2o","synonym_count":3} |
| ev-d5d6669e97e96221 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1497] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-c9fc6ca6f9565278 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Na2moo4_X_7_H2o; data-row positions=[2007] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2007,"object_id":"CHEBI:86473","object_label":"sodium molybdate heptahydrate","other":"Na2MoO4.7H2O&#124;sodium dioxido(dioxo)molybdenum--water (1/7)","predicate_id":"skos:exactMatch","subject_id":"MIM:Na2moo4_X_7_H2o","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-cef08e5c5bbc83d0 | docs/data/mapped_ingredients.csv; CSV lines=[1499] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:86473","line":1499,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"6","ontology_id":"CHEBI:86473","preferred_term":"Na2MoO4 x 7 H2O","total_occurrences":"6"}] |
| ev-26e54e8dd796b65d | reports/yaml_record_review/Na2moo4_X_7_H2o.md; &#96;data/ingredients/mapped/Na2moo4_X_7_H2o.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:28; Completeness:41; Recommended Edits:48 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-6a6b858125a1d27d | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1003,1374] | context_only | [{"current_record_sha256":"c38475fd99369be070f4498f2fc6af0159695713a28ff1383a73e69d1e1fc6e8","finding_id":"SEM:f51f6d6b660a7bea1259","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c38475fd99369be070f4498f2fc6af0159695713a28ff1383a73e69d1e1fc6e8","finding_id":"SEM:4e9e28cb8731790b095f","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-a327517673be4b95 | data/ingredients/mapped/Na2moo4_X_7_H2o.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"TRACE_ELEMENT"}}] |
| ev-61b065e9ac6069c5 | reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml; findings[finding_id=f-afb54daf8f9945c4] | context_only | Predecessor structured review finding f-afb54daf8f9945c4 in 20261011T024637Z-mim-reconcile-all-batch-09 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-na2moo4-x-7-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Na2moo4_X_7_H2o (data/ingredients/mapped/Na2moo4_X_7_H2o.yaml)'
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
summary: Per-record structured review for Na2moo4_X_7_H2o (data/ingredients/mapped/Na2moo4_X_7_H2o.yaml,
  record-d41203d614779c47, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Na2moo4_X_7_H2o.yaml
    sha256: c38475fd99369be070f4498f2fc6af0159695713a28ff1383a73e69d1e1fc6e8
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
  - path: reports/yaml_record_review/Na2moo4_X_7_H2o.md
    sha256: 04f3ac40f822f98ef1c113cf934402a9aac4551b9fd8d579615a44521dae1edf
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-d41203d614779c47
  path: data/ingredients/mapped/Na2moo4_X_7_H2o.yaml
  label: Na2moo4_X_7_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2moo4_X_7_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Na2moo4_X_7_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Na2moo4_X_7_H2o.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-d41203d614779c47
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-d41203d614779c47
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-d41203d614779c47
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-d41203d614779c47
evidence:
- evidence_id: ev-35ddb92a4e9f3d48
  kind: record_content
  reference: data/ingredients/mapped/Na2moo4_X_7_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1497],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:86473","line":1499,"mapping_status":"MAPPED","ontology_id":"CHEBI:86473","preferred_term":"Na2MoO4
    x 7 H2O"}],"identifier":"CHEBI:86473","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":6,"edge_count":6,"occurrences":6},"occurrence_statistics":{"media_count":6,"total_occurrences":6},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:86473","ontology_label":"sodium
    molybdate heptahydrate","ontology_source":"CHEBI"},"preferred_term":"Na2MoO4 x
    7 H2O","sssom_rows":[{"data_row":2007,"object_id":"CHEBI:86473","object_label":"sodium
    molybdate heptahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2moo4_X_7_H2o","synonym_count":3}'
  snapshot_sha256: c38475fd99369be070f4498f2fc6af0159695713a28ff1383a73e69d1e1fc6e8
- evidence_id: ev-d5d6669e97e96221
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1497]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-c9fc6ca6f9565278
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Na2moo4_X_7_H2o; data-row positions=[2007]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2007,"object_id":"CHEBI:86473","object_label":"sodium
    molybdate heptahydrate","other":"Na2MoO4.7H2O|sodium dioxido(dioxo)molybdenum--water
    (1/7)","predicate_id":"skos:exactMatch","subject_id":"MIM:Na2moo4_X_7_H2o","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-cef08e5c5bbc83d0
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1499]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:86473","line":1499,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"6","ontology_id":"CHEBI:86473","preferred_term":"Na2MoO4
    x 7 H2O","total_occurrences":"6"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-26e54e8dd796b65d
  kind: prior_review
  reference: reports/yaml_record_review/Na2moo4_X_7_H2o.md
  locator: '`data/ingredients/mapped/Na2moo4_X_7_H2o.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:28; Completeness:41; Recommended Edits:48'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 04f3ac40f822f98ef1c113cf934402a9aac4551b9fd8d579615a44521dae1edf
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Na2moo4_X_7_H2o.yaml`,\
    \ either remove\n  `nutritional_roles.TRACE_ELEMENT` or replace its name-pattern\
    \ placeholder with\n  source-backed evidence from maintained role-text or literature\
    \ inputs. Rerun\n  strict validation and the role/output SSSOM checks after the\
    \ role facet\n  change."
- evidence_id: ev-6a6b858125a1d27d
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1003,1374]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"c38475fd99369be070f4498f2fc6af0159695713a28ff1383a73e69d1e1fc6e8","finding_id":"SEM:f51f6d6b660a7bea1259","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c38475fd99369be070f4498f2fc6af0159695713a28ff1383a73e69d1e1fc6e8","finding_id":"SEM:4e9e28cb8731790b095f","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-a327517673be4b95
  kind: record_content
  reference: data/ingredients/mapped/Na2moo4_X_7_H2o.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"TRACE_ELEMENT"}}]'
  snapshot_sha256: c38475fd99369be070f4498f2fc6af0159695713a28ff1383a73e69d1e1fc6e8
- evidence_id: ev-61b065e9ac6069c5
  kind: prior_review
  reference: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
  locator: findings[finding_id=f-afb54daf8f9945c4]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-afb54daf8f9945c4 in 20261011T024637Z-mim-reconcile-all-batch-09
  snapshot_sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
assessments:
- assessment_id: a-9eebcba569ece014
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-d41203d614779c47
  evidence_ids:
  - ev-35ddb92a4e9f3d48
  - ev-d5d6669e97e96221
  - ev-c9fc6ca6f9565278
  - ev-cef08e5c5bbc83d0
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-118c73023085e505
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d41203d614779c47
  evidence_ids:
  - ev-26e54e8dd796b65d
  - ev-35ddb92a4e9f3d48
  - ev-6a6b858125a1d27d
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:24:19Z;
    reviewed SHA-256=c38475fd99369be070f4498f2fc6af0159695713a28ff1383a73e69d1e1fc6e8;
    current SHA-256=c38475fd99369be070f4498f2fc6af0159695713a28ff1383a73e69d1e1fc6e8;
    hash_changed=False. Reports=["reports/yaml_record_review/Na2moo4_X_7_H2o.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:86473 sodium molybdate heptahydrate identity passes, but TRACE_ELEMENT is
    provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-26e54e8dd796b65d
    - ev-35ddb92a4e9f3d48
  - name: legacy-native-ids
    value: '["SEM:f51f6d6b660a7bea1259","SEM:4e9e28cb8731790b095f"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-35ddb92a4e9f3d48
    - ev-26e54e8dd796b65d
    - ev-6a6b858125a1d27d
- assessment_id: a-a327517673be4b95
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-d41203d614779c47
  evidence_ids:
  - ev-26e54e8dd796b65d
  - ev-a327517673be4b95
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-26e54e8dd796b65d
    - ev-a327517673be4b95
findings:
- finding_id: rec-f-afb54daf8f9945c4
  issue_key: mim-reconciliation-role-support-d41203d614779c47
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Na2MoO4 x 7 H2O'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-d41203d614779c47
  evidence_ids:
  - ev-26e54e8dd796b65d
  - ev-a327517673be4b95
  - ev-61b065e9ac6069c5
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2moo4_X_7_H2o.yaml
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
    finding_id: f-afb54daf8f9945c4
actions:
- action_id: rec-action-afb54daf8f9945c4
  description: 'Reassess prediction-only role support: Na2MoO4 x 7 H2O'
  finding_ids:
  - rec-f-afb54daf8f9945c4
  target_ids:
  - record-d41203d614779c47
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2moo4_X_7_H2o.yaml
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
