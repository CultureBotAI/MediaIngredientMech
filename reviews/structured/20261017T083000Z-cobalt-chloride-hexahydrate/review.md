# Per-record structured review: Cobalt_chloride_hexahydrate (data/ingredients/mapped/Cobalt_chloride_hexahydrate.yaml)

- Review: 20261017T083000Z-cobalt-chloride-hexahydrate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Cobalt_chloride_hexahydrate (data/ingredients/mapped/Cobalt_chloride_hexahydrate.yaml, record-f9db6fc3a8d2618f, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Cobalt_chloride_hexahydrate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Cobalt_chloride_hexahydrate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-f9db6fc3a8d2618f | data/ingredients/mapped/Cobalt_chloride_hexahydrate.yaml | maintained | Cobalt_chloride_hexahydrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-f9db6fc3a8d2618f | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-f9db6fc3a8d2618f | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-f9db6fc3a8d2618f | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-f9db6fc3a8d2618f.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-f9db6fc3a8d2618f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T12:24:28Z; reviewed SHA-256=f32ab49c0fa30ca998c07a039503ff4f943b1cb428fb994da6906be8349247dc; current SHA-256=f32ab49c0fa30ca998c07a039503ff4f943b1cb428fb994da6906be8349247dc; hash_changed=False. Reports=["reports/yaml_record_review/Cobalt_chloride_hexahydrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI cobalt chloride hexahydrate identity and 2636/2638 count pass, but its trace-element role is only computationally supported.

### Historical provisional-role concern

evidence: concern. Targets: record-f9db6fc3a8d2618f.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-46a0cf617c770d22: Reassess prediction-only role support: Cobalt chloride hexahydrate

major / open / confirmed; issue key: mim-reconciliation-role-support-f9db6fc3a8d2618f.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-46a0cf617c770d22

Reassess prediction-only role support: Cobalt chloride hexahydrate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-beaf3eea521ad334 | data/ingredients/mapped/Cobalt_chloride_hexahydrate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[742],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:53503","line":744,"mapping_status":"MAPPED","ontology_id":"CHEBI:53503","preferred_term":"Cobalt chloride hexahydrate"}],"identifier":"CHEBI:53503","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2636,"edge_count":2636,"occurrences":2638},"occurrence_statistics":{"media_count":2636,"total_occurrences":2638},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:53503","ontology_label":"cobalt chloride hexahydrate","ontology_source":"CHEBI"},"preferred_term":"Cobalt chloride hexahydrate","sssom_rows":[{"data_row":795,"object_id":"CHEBI:53503","object_label":"cobalt chloride hexahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cobalt_chloride_hexahydrate","synonym_count":7} |
| ev-9af2719fee58a2ab | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [742] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-59300f2f598ea9e8 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Cobalt_chloride_hexahydrate; data-row positions=[795] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":795,"object_id":"CHEBI:53503","object_label":"cobalt chloride hexahydrate","other":"Cobalt dichloride hexahydrate&#124;Cobalt(II) chloride hexahydrate&#124;cobalt (II) chloride hexahydrate&#124;cobalt chloride hydrate&#124;cobalt(2+) dichloride hexahydrate&#124;Cobalt(II) chloride--water (1/7)&#124;CoCl2 x 6 H2O&#124;CAS:7791-13-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Cobalt_chloride_hexahydrate","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-090f0290016c03e2 | docs/data/mapped_ingredients.csv; CSV lines=[744] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:53503","line":744,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"2636","ontology_id":"CHEBI:53503","preferred_term":"Cobalt chloride hexahydrate","total_occurrences":"2638"}] |
| ev-7c3ef400f19ca46b | reports/yaml_record_review/Cobalt_chloride_hexahydrate.md; &#96;data/ingredients/mapped/Cobalt_chloride_hexahydrate.yaml&#96;:2; Verdict:4; Identity:12; Validation:28; Evidence:48; Completeness:69; Recommended Edits:76 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-c8ae09ee189612b4 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[430,1600] | context_only | [{"current_record_sha256":"f32ab49c0fa30ca998c07a039503ff4f943b1cb428fb994da6906be8349247dc","finding_id":"SEM:fb7bde6c0dcac86f65a5","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"f32ab49c0fa30ca998c07a039503ff4f943b1cb428fb994da6906be8349247dc","finding_id":"SEM:7aa99c3fc33f337b24ea","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-f55febd79e451c02 | data/ingredients/mapped/Cobalt_chloride_hexahydrate.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional in-session LLM role assignment; review recommended.","reference_text":"Assigned by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"TRACE_ELEMENT"}}] |
| ev-43c0562a0f44b2de | reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml; findings[finding_id=f-46a0cf617c770d22] | context_only | Predecessor structured review finding f-46a0cf617c770d22 in 20261011T024632Z-mim-reconcile-all-batch-04 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-cobalt-chloride-hexahydrate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Cobalt_chloride_hexahydrate (data/ingredients/mapped/Cobalt_chloride_hexahydrate.yaml)'
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
summary: Per-record structured review for Cobalt_chloride_hexahydrate (data/ingredients/mapped/Cobalt_chloride_hexahydrate.yaml,
  record-f9db6fc3a8d2618f, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Cobalt_chloride_hexahydrate.yaml
    sha256: f32ab49c0fa30ca998c07a039503ff4f943b1cb428fb994da6906be8349247dc
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
  - path: reports/yaml_record_review/Cobalt_chloride_hexahydrate.md
    sha256: 089977a02f8ce3b0d45046ec27f898aa775d63f0772eb85ce122eab3945bcbe5
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-f9db6fc3a8d2618f
  path: data/ingredients/mapped/Cobalt_chloride_hexahydrate.yaml
  label: Cobalt_chloride_hexahydrate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cobalt_chloride_hexahydrate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Cobalt_chloride_hexahydrate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Cobalt_chloride_hexahydrate.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-f9db6fc3a8d2618f
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-f9db6fc3a8d2618f
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-f9db6fc3a8d2618f
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-f9db6fc3a8d2618f
evidence:
- evidence_id: ev-beaf3eea521ad334
  kind: record_content
  reference: data/ingredients/mapped/Cobalt_chloride_hexahydrate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[742],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:53503","line":744,"mapping_status":"MAPPED","ontology_id":"CHEBI:53503","preferred_term":"Cobalt
    chloride hexahydrate"}],"identifier":"CHEBI:53503","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2636,"edge_count":2636,"occurrences":2638},"occurrence_statistics":{"media_count":2636,"total_occurrences":2638},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:53503","ontology_label":"cobalt
    chloride hexahydrate","ontology_source":"CHEBI"},"preferred_term":"Cobalt chloride
    hexahydrate","sssom_rows":[{"data_row":795,"object_id":"CHEBI:53503","object_label":"cobalt
    chloride hexahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cobalt_chloride_hexahydrate","synonym_count":7}'
  snapshot_sha256: f32ab49c0fa30ca998c07a039503ff4f943b1cb428fb994da6906be8349247dc
- evidence_id: ev-9af2719fee58a2ab
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [742]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-59300f2f598ea9e8
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Cobalt_chloride_hexahydrate; data-row positions=[795]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":795,"object_id":"CHEBI:53503","object_label":"cobalt
    chloride hexahydrate","other":"Cobalt dichloride hexahydrate|Cobalt(II) chloride
    hexahydrate|cobalt (II) chloride hexahydrate|cobalt chloride hydrate|cobalt(2+)
    dichloride hexahydrate|Cobalt(II) chloride--water (1/7)|CoCl2 x 6 H2O|CAS:7791-13-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Cobalt_chloride_hexahydrate","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-090f0290016c03e2
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[744]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:53503","line":744,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"2636","ontology_id":"CHEBI:53503","preferred_term":"Cobalt
    chloride hexahydrate","total_occurrences":"2638"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-7c3ef400f19ca46b
  kind: prior_review
  reference: reports/yaml_record_review/Cobalt_chloride_hexahydrate.md
  locator: '`data/ingredients/mapped/Cobalt_chloride_hexahydrate.yaml`:2; Verdict:4;
    Identity:12; Validation:28; Evidence:48; Completeness:69; Recommended Edits:76'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 089977a02f8ce3b0d45046ec27f898aa775d63f0772eb85ce122eab3945bcbe5
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Cobalt_chloride_hexahydrate.yaml`,\
    \ either\n  replace `nutritional_roles.TRACE_ELEMENT` with inspected evidence\
    \ for cobalt\n  chloride hexahydrate as a trace element in this media scope, or\
    \ remove the\n  role.\n- Regenerate synchronized products and rerun strict validation,\
    \ SSSOM QC,\n  aggregate roundtrip, and `git diff --check`."
- evidence_id: ev-c8ae09ee189612b4
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[430,1600]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"f32ab49c0fa30ca998c07a039503ff4f943b1cb428fb994da6906be8349247dc","finding_id":"SEM:fb7bde6c0dcac86f65a5","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"f32ab49c0fa30ca998c07a039503ff4f943b1cb428fb994da6906be8349247dc","finding_id":"SEM:7aa99c3fc33f337b24ea","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-f55febd79e451c02
  kind: record_content
  reference: data/ingredients/mapped/Cobalt_chloride_hexahydrate.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional
    in-session LLM role assignment; review recommended.","reference_text":"Assigned
    by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"TRACE_ELEMENT"}}]'
  snapshot_sha256: f32ab49c0fa30ca998c07a039503ff4f943b1cb428fb994da6906be8349247dc
- evidence_id: ev-43c0562a0f44b2de
  kind: prior_review
  reference: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
  locator: findings[finding_id=f-46a0cf617c770d22]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-46a0cf617c770d22 in 20261011T024632Z-mim-reconcile-all-batch-04
  snapshot_sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
assessments:
- assessment_id: a-b3fe9260a767b2b5
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-f9db6fc3a8d2618f
  evidence_ids:
  - ev-beaf3eea521ad334
  - ev-9af2719fee58a2ab
  - ev-59300f2f598ea9e8
  - ev-090f0290016c03e2
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-b0d06eb873705d8d
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-f9db6fc3a8d2618f
  evidence_ids:
  - ev-7c3ef400f19ca46b
  - ev-beaf3eea521ad334
  - ev-c8ae09ee189612b4
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T12:24:28Z;
    reviewed SHA-256=f32ab49c0fa30ca998c07a039503ff4f943b1cb428fb994da6906be8349247dc;
    current SHA-256=f32ab49c0fa30ca998c07a039503ff4f943b1cb428fb994da6906be8349247dc;
    hash_changed=False. Reports=["reports/yaml_record_review/Cobalt_chloride_hexahydrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI cobalt chloride hexahydrate identity and 2636/2638 count pass, but its trace-element
    role is only computationally supported.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-7c3ef400f19ca46b
    - ev-beaf3eea521ad334
  - name: legacy-native-ids
    value: '["SEM:fb7bde6c0dcac86f65a5","SEM:7aa99c3fc33f337b24ea"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-beaf3eea521ad334
    - ev-7c3ef400f19ca46b
    - ev-c8ae09ee189612b4
- assessment_id: a-f55febd79e451c02
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-f9db6fc3a8d2618f
  evidence_ids:
  - ev-7c3ef400f19ca46b
  - ev-f55febd79e451c02
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-7c3ef400f19ca46b
    - ev-f55febd79e451c02
findings:
- finding_id: rec-f-46a0cf617c770d22
  issue_key: mim-reconciliation-role-support-f9db6fc3a8d2618f
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Cobalt chloride hexahydrate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-f9db6fc3a8d2618f
  evidence_ids:
  - ev-7c3ef400f19ca46b
  - ev-f55febd79e451c02
  - ev-43c0562a0f44b2de
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cobalt_chloride_hexahydrate.yaml
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
    review_id: 20261011T024632Z-mim-reconcile-all-batch-04
    finding_id: f-46a0cf617c770d22
actions:
- action_id: rec-action-46a0cf617c770d22
  description: 'Reassess prediction-only role support: Cobalt chloride hexahydrate'
  finding_ids:
  - rec-f-46a0cf617c770d22
  target_ids:
  - record-f9db6fc3a8d2618f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cobalt_chloride_hexahydrate.yaml
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
  with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.
```
