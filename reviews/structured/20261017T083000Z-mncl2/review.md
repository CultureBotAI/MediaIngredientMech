# Per-record structured review: Mncl2 (data/ingredients/mapped/Mncl2.yaml)

- Review: 20261017T083000Z-mncl2
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Mncl2 (data/ingredients/mapped/Mncl2.yaml, record-a4c3e9ae8efce8fa, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Mncl2.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Mncl2.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-a4c3e9ae8efce8fa | data/ingredients/mapped/Mncl2.yaml | maintained | Mncl2 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-a4c3e9ae8efce8fa | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-a4c3e9ae8efce8fa | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-a4c3e9ae8efce8fa | Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-a4c3e9ae8efce8fa.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-a4c3e9ae8efce8fa.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T03:39:29Z; reviewed SHA-256=6efc4b6c0a60c00984eaa246754ca7174940c98a59e3f483cd42a2cabcd26a0e; current SHA-256=6efc4b6c0a60c00984eaa246754ca7174940c98a59e3f483cd42a2cabcd26a0e; hash_changed=False. Reports=["reports/yaml_record_review/Mncl2.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:63041 anhydrous manganese chloride identity, structure, occurrence count, and final SSSOM row pass, but TRACE_ELEMENT is still provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-a4c3e9ae8efce8fa.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-ccd132cb0998612a: Reassess prediction-only role support: MnCl2

major / open / confirmed; issue key: mim-reconciliation-role-support-a4c3e9ae8efce8fa.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-ccd132cb0998612a

Reassess prediction-only role support: MnCl2

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-31f422474cc76041 | data/ingredients/mapped/Mncl2.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1413],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:63041","line":1415,"mapping_status":"MAPPED","ontology_id":"CHEBI:63041","preferred_term":"MnCl2"}],"identifier":"CHEBI:63041","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":156,"edge_count":156,"occurrences":156},"occurrence_statistics":{"media_count":156,"total_occurrences":156},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:63041","ontology_label":"manganese(II) chloride","ontology_source":"CHEBI"},"preferred_term":"MnCl2","sssom_rows":[{"data_row":1889,"object_id":"CHEBI:63041","object_label":"manganese(II) chloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Mncl2","synonym_count":14} |
| ev-34c3d4dd4753365f | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1413] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-7fa813a6d75861bb | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Mncl2; data-row positions=[1889] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1889,"object_id":"CHEBI:63041","object_label":"manganese(II) chloride","other":"Manganese chloride&#124;manganese dichloride&#124;anhydrous manganese chloride&#124;Mangandichlorid&#124;Manganese bichloride&#124;Manganese(II) chloride (1:2)&#124;Manganous chloride&#124;dichlorure de manganese&#124;manganese(2+) dichloride&#124;manganese(II) dichloride&#124;manganous dichloride","predicate_id":"skos:exactMatch","subject_id":"MIM:Mncl2","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-a0f2e5a8a8ad2a81 | docs/data/mapped_ingredients.csv; CSV lines=[1415] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:63041","line":1415,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"156","ontology_id":"CHEBI:63041","preferred_term":"MnCl2","total_occurrences":"156"}] |
| ev-574ba9e35f3c9c52 | reports/yaml_record_review/Mncl2.md; &#96;data/ingredients/mapped/Mncl2.yaml&#96;:2; Verdict:4; Identity:12; Validation:22; Evidence:29; Completeness:40; Recommended Edits:47 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-3bdc7f79ba8cd524 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[947,1934] | context_only | [{"current_record_sha256":"6efc4b6c0a60c00984eaa246754ca7174940c98a59e3f483cd42a2cabcd26a0e","finding_id":"SEM:5ecc4ca9cddc4a471475","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"6efc4b6c0a60c00984eaa246754ca7174940c98a59e3f483cd42a2cabcd26a0e","finding_id":"SEM:792052203d185f030289","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-114e48e0955695d7 | data/ingredients/mapped/Mncl2.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"TRACE_ELEMENT"}}] |
| ev-e093ee9edd9aea09 | reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml; findings[finding_id=f-ccd132cb0998612a] | context_only | Predecessor structured review finding f-ccd132cb0998612a in 20261011T024636Z-mim-reconcile-all-batch-08 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-mncl2
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Mncl2 (data/ingredients/mapped/Mncl2.yaml)'
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
summary: Per-record structured review for Mncl2 (data/ingredients/mapped/Mncl2.yaml,
  record-a4c3e9ae8efce8fa, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Mncl2.yaml
    sha256: 6efc4b6c0a60c00984eaa246754ca7174940c98a59e3f483cd42a2cabcd26a0e
    role: target
  - path: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
    sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
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
  - path: reports/yaml_record_review/Mncl2.md
    sha256: 09bec73a0c0ba04ef5510da29609f0f43bce41808e544427f1fc3215155cba71
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-a4c3e9ae8efce8fa
  path: data/ingredients/mapped/Mncl2.yaml
  label: Mncl2
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Mncl2.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Mncl2.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Mncl2.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-a4c3e9ae8efce8fa
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-a4c3e9ae8efce8fa
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-a4c3e9ae8efce8fa
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08
    and semantic review dispositions on HEAD.
  target_ids:
  - record-a4c3e9ae8efce8fa
evidence:
- evidence_id: ev-31f422474cc76041
  kind: record_content
  reference: data/ingredients/mapped/Mncl2.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1413],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:63041","line":1415,"mapping_status":"MAPPED","ontology_id":"CHEBI:63041","preferred_term":"MnCl2"}],"identifier":"CHEBI:63041","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":156,"edge_count":156,"occurrences":156},"occurrence_statistics":{"media_count":156,"total_occurrences":156},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:63041","ontology_label":"manganese(II)
    chloride","ontology_source":"CHEBI"},"preferred_term":"MnCl2","sssom_rows":[{"data_row":1889,"object_id":"CHEBI:63041","object_label":"manganese(II)
    chloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Mncl2","synonym_count":14}'
  snapshot_sha256: 6efc4b6c0a60c00984eaa246754ca7174940c98a59e3f483cd42a2cabcd26a0e
- evidence_id: ev-34c3d4dd4753365f
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1413]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-7fa813a6d75861bb
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Mncl2; data-row positions=[1889]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1889,"object_id":"CHEBI:63041","object_label":"manganese(II)
    chloride","other":"Manganese chloride|manganese dichloride|anhydrous manganese
    chloride|Mangandichlorid|Manganese bichloride|Manganese(II) chloride (1:2)|Manganous
    chloride|dichlorure de manganese|manganese(2+) dichloride|manganese(II) dichloride|manganous
    dichloride","predicate_id":"skos:exactMatch","subject_id":"MIM:Mncl2","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-a0f2e5a8a8ad2a81
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1415]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:63041","line":1415,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"156","ontology_id":"CHEBI:63041","preferred_term":"MnCl2","total_occurrences":"156"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-574ba9e35f3c9c52
  kind: prior_review
  reference: reports/yaml_record_review/Mncl2.md
  locator: '`data/ingredients/mapped/Mncl2.yaml`:2; Verdict:4; Identity:12; Validation:22;
    Evidence:29; Completeness:40; Recommended Edits:47'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 09bec73a0c0ba04ef5510da29609f0f43bce41808e544427f1fc3215155cba71
  quote: "Recommended Edits:\n- Major: add source-backed evidence that anhydrous MnCl2\
    \ is used as a trace\n  element source in media, or remove the provisional `TRACE_ELEMENT`\
    \ role."
- evidence_id: ev-3bdc7f79ba8cd524
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[947,1934]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"6efc4b6c0a60c00984eaa246754ca7174940c98a59e3f483cd42a2cabcd26a0e","finding_id":"SEM:5ecc4ca9cddc4a471475","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"6efc4b6c0a60c00984eaa246754ca7174940c98a59e3f483cd42a2cabcd26a0e","finding_id":"SEM:792052203d185f030289","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-114e48e0955695d7
  kind: record_content
  reference: data/ingredients/mapped/Mncl2.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"TRACE_ELEMENT"}}]'
  snapshot_sha256: 6efc4b6c0a60c00984eaa246754ca7174940c98a59e3f483cd42a2cabcd26a0e
- evidence_id: ev-e093ee9edd9aea09
  kind: prior_review
  reference: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
  locator: findings[finding_id=f-ccd132cb0998612a]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-ccd132cb0998612a in 20261011T024636Z-mim-reconcile-all-batch-08
  snapshot_sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
assessments:
- assessment_id: a-710ef21d57020092
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-a4c3e9ae8efce8fa
  evidence_ids:
  - ev-31f422474cc76041
  - ev-34c3d4dd4753365f
  - ev-7fa813a6d75861bb
  - ev-a0f2e5a8a8ad2a81
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-48fbced83719d8f9
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-a4c3e9ae8efce8fa
  evidence_ids:
  - ev-574ba9e35f3c9c52
  - ev-31f422474cc76041
  - ev-3bdc7f79ba8cd524
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T03:39:29Z;
    reviewed SHA-256=6efc4b6c0a60c00984eaa246754ca7174940c98a59e3f483cd42a2cabcd26a0e;
    current SHA-256=6efc4b6c0a60c00984eaa246754ca7174940c98a59e3f483cd42a2cabcd26a0e;
    hash_changed=False. Reports=["reports/yaml_record_review/Mncl2.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI:63041 anhydrous
    manganese chloride identity, structure, occurrence count, and final SSSOM row
    pass, but TRACE_ELEMENT is still provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-574ba9e35f3c9c52
    - ev-31f422474cc76041
  - name: legacy-native-ids
    value: '["SEM:5ecc4ca9cddc4a471475","SEM:792052203d185f030289"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-31f422474cc76041
    - ev-574ba9e35f3c9c52
    - ev-3bdc7f79ba8cd524
- assessment_id: a-114e48e0955695d7
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-a4c3e9ae8efce8fa
  evidence_ids:
  - ev-574ba9e35f3c9c52
  - ev-114e48e0955695d7
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-574ba9e35f3c9c52
    - ev-114e48e0955695d7
findings:
- finding_id: rec-f-ccd132cb0998612a
  issue_key: mim-reconciliation-role-support-a4c3e9ae8efce8fa
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: MnCl2'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-a4c3e9ae8efce8fa
  evidence_ids:
  - ev-574ba9e35f3c9c52
  - ev-114e48e0955695d7
  - ev-e093ee9edd9aea09
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Mncl2.yaml
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
    review_id: 20261011T024636Z-mim-reconcile-all-batch-08
    finding_id: f-ccd132cb0998612a
actions:
- action_id: rec-action-ccd132cb0998612a
  description: 'Reassess prediction-only role support: MnCl2'
  finding_ids:
  - rec-f-ccd132cb0998612a
  target_ids:
  - record-a4c3e9ae8efce8fa
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Mncl2.yaml
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
  with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.
```
