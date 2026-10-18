# Per-record structured review: Tuberactinomycin (data/ingredients/mapped/Tuberactinomycin.yaml)

- Review: 20261017T083000Z-tuberactinomycin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Tuberactinomycin (data/ingredients/mapped/Tuberactinomycin.yaml, record-e89b902374249843, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Tuberactinomycin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Tuberactinomycin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-e89b902374249843 | data/ingredients/mapped/Tuberactinomycin.yaml | maintained | Tuberactinomycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-e89b902374249843 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-e89b902374249843 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-e89b902374249843 | Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-e89b902374249843.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-e89b902374249843.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T20:12:39Z; reviewed SHA-256=1c818cbf1c39960029853fadc7f742eaf392c0d8529f711510cd2ad4e20724ee; current SHA-256=1c818cbf1c39960029853fadc7f742eaf392c0d8529f711510cd2ad4e20724ee; hash_changed=False. Reports=["reports/yaml_record_review/Tuberactinomycin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact MeSH fallback identity and final SSSOM row pass, but SELECTIVE_AGENT is provisional name-pattern evidence.

### Historical provisional-role concern

evidence: concern. Targets: record-e89b902374249843.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-91186c5544f7e8da: Reassess prediction-only role support: Tuberactinomycin

major / open / confirmed; issue key: mim-reconciliation-role-support-e89b902374249843.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-91186c5544f7e8da

Reassess prediction-only role support: Tuberactinomycin

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-bfec3dc8721214a7 | data/ingredients/mapped/Tuberactinomycin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2012],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C015563","line":2014,"mapping_status":"MAPPED","ontology_id":"mesh:C015563","preferred_term":"Tuberactinomycin"}],"identifier":"mesh:C015563","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C015563","ontology_label":"tuberactinomycin","ontology_source":"MESH"},"preferred_term":"Tuberactinomycin","sssom_rows":[{"data_row":2851,"object_id":"mesh:C015563","object_label":"tuberactinomycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Tuberactinomycin","synonym_count":0} |
| ev-34d88265dbb5a1ed | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2012] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-2be72c2820019207 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Tuberactinomycin; data-row positions=[2851] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2851,"object_id":"mesh:C015563","object_label":"tuberactinomycin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Tuberactinomycin","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-4cc0936b5d4375f4 | docs/data/mapped_ingredients.csv; CSV lines=[2014] | supports | Published identity and count rows inspected: [{"identifier":"mesh:C015563","line":2014,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C015563","preferred_term":"Tuberactinomycin","total_occurrences":"0"}] |
| ev-530b617263972d93 | reports/yaml_record_review/Tuberactinomycin.md; &#96;data/ingredients/mapped/Tuberactinomycin.yaml&#96;:2; Verdict:4; Identity:10; Validation:22; Evidence:33; Issues:42; Major: &#96;SELECTIVE_AGENT&#96; is provisional name-pattern evidence:44; Completeness:61; Recommended Edits:66 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-b2a9ebba58632cbd | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1324,1773] | context_only | [{"current_record_sha256":"1c818cbf1c39960029853fadc7f742eaf392c0d8529f711510cd2ad4e20724ee","finding_id":"SEM:8a44abb5cffd7fd46158","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"1c818cbf1c39960029853fadc7f742eaf392c0d8529f711510cd2ad4e20724ee","finding_id":"SEM:504e0d0d5f7fafe96df5","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-6bc014ac72b91abc | data/ingredients/mapped/Tuberactinomycin.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}] |
| ev-f634ee75d93a30ff | reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml; findings[finding_id=f-91186c5544f7e8da] | context_only | Predecessor structured review finding f-91186c5544f7e8da in 20261011T024639Z-mim-reconcile-all-batch-12 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.

## Complete Structured Record

The sibling review.yaml is authoritative.

````yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-tuberactinomycin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Tuberactinomycin (data/ingredients/mapped/Tuberactinomycin.yaml)'
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
summary: Per-record structured review for Tuberactinomycin (data/ingredients/mapped/Tuberactinomycin.yaml,
  record-e89b902374249843, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Tuberactinomycin.yaml
    sha256: 1c818cbf1c39960029853fadc7f742eaf392c0d8529f711510cd2ad4e20724ee
    role: target
  - path: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
    sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
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
  - path: reports/yaml_record_review/Tuberactinomycin.md
    sha256: ab1936b4d654ff3097d9ef54c2f5b3ed87141a5c086953d1e100d2dbd24f0a9c
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-e89b902374249843
  path: data/ingredients/mapped/Tuberactinomycin.yaml
  label: Tuberactinomycin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Tuberactinomycin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Tuberactinomycin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Tuberactinomycin.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-e89b902374249843
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-e89b902374249843
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-e89b902374249843
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12
    and semantic review dispositions on HEAD.
  target_ids:
  - record-e89b902374249843
evidence:
- evidence_id: ev-bfec3dc8721214a7
  kind: record_content
  reference: data/ingredients/mapped/Tuberactinomycin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2012],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C015563","line":2014,"mapping_status":"MAPPED","ontology_id":"mesh:C015563","preferred_term":"Tuberactinomycin"}],"identifier":"mesh:C015563","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C015563","ontology_label":"tuberactinomycin","ontology_source":"MESH"},"preferred_term":"Tuberactinomycin","sssom_rows":[{"data_row":2851,"object_id":"mesh:C015563","object_label":"tuberactinomycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Tuberactinomycin","synonym_count":0}'
  snapshot_sha256: 1c818cbf1c39960029853fadc7f742eaf392c0d8529f711510cd2ad4e20724ee
- evidence_id: ev-34d88265dbb5a1ed
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2012]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-2be72c2820019207
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Tuberactinomycin; data-row positions=[2851]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2851,"object_id":"mesh:C015563","object_label":"tuberactinomycin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Tuberactinomycin","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-4cc0936b5d4375f4
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2014]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"mesh:C015563","line":2014,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C015563","preferred_term":"Tuberactinomycin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-530b617263972d93
  kind: prior_review
  reference: reports/yaml_record_review/Tuberactinomycin.md
  locator: '`data/ingredients/mapped/Tuberactinomycin.yaml`:2; Verdict:4; Identity:10;
    Validation:22; Evidence:33; Issues:42; Major: `SELECTIVE_AGENT` is provisional
    name-pattern evidence:44; Completeness:61; Recommended Edits:66'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: ab1936b4d654ff3097d9ef54c2f5b3ed87141a5c086953d1e100d2dbd24f0a9c
  quote: "Issues:\n\n\nMajor: `SELECTIVE_AGENT` is provisional name-pattern evidence:\n\
    The only role assertion is:\n\n```yaml\nphysicochemical_roles:\n- role: SELECTIVE_AGENT\n\
    \  confidence: 0.8\n  evidence:\n  - reference_type: COMPUTATIONAL_PREDICTION\n\
    \    reference_text: Inferred from curated media-role name pattern\n    curator_note:\
    \ Provisional role from a curated name-pattern rule; review recommended.\n```\n\
    \nThe MeSH fallback mapping does not independently curate the selective-agent\n\
    role.\n\nRecommended Edits:\n- Replace the `SELECTIVE_AGENT` computational prediction\
    \ with curated\n  database/literature evidence, or remove `physicochemical_roles`\
    \ until such\n  support is added."
- evidence_id: ev-b2a9ebba58632cbd
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1324,1773]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"1c818cbf1c39960029853fadc7f742eaf392c0d8529f711510cd2ad4e20724ee","finding_id":"SEM:8a44abb5cffd7fd46158","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"1c818cbf1c39960029853fadc7f742eaf392c0d8529f711510cd2ad4e20724ee","finding_id":"SEM:504e0d0d5f7fafe96df5","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-6bc014ac72b91abc
  kind: record_content
  reference: data/ingredients/mapped/Tuberactinomycin.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}]'
  snapshot_sha256: 1c818cbf1c39960029853fadc7f742eaf392c0d8529f711510cd2ad4e20724ee
- evidence_id: ev-f634ee75d93a30ff
  kind: prior_review
  reference: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
  locator: findings[finding_id=f-91186c5544f7e8da]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-91186c5544f7e8da in 20261011T024639Z-mim-reconcile-all-batch-12
  snapshot_sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
assessments:
- assessment_id: a-bf615bb1e884d41d
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-e89b902374249843
  evidence_ids:
  - ev-bfec3dc8721214a7
  - ev-34d88265dbb5a1ed
  - ev-2be72c2820019207
  - ev-4cc0936b5d4375f4
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-7f5825a3a8e3f784
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-e89b902374249843
  evidence_ids:
  - ev-530b617263972d93
  - ev-bfec3dc8721214a7
  - ev-b2a9ebba58632cbd
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T20:12:39Z;
    reviewed SHA-256=1c818cbf1c39960029853fadc7f742eaf392c0d8529f711510cd2ad4e20724ee;
    current SHA-256=1c818cbf1c39960029853fadc7f742eaf392c0d8529f711510cd2ad4e20724ee;
    hash_changed=False. Reports=["reports/yaml_record_review/Tuberactinomycin.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    MeSH fallback identity and final SSSOM row pass, but SELECTIVE_AGENT is provisional
    name-pattern evidence.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-530b617263972d93
    - ev-bfec3dc8721214a7
  - name: legacy-native-ids
    value: '["SEM:8a44abb5cffd7fd46158","SEM:504e0d0d5f7fafe96df5"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-bfec3dc8721214a7
    - ev-530b617263972d93
    - ev-b2a9ebba58632cbd
- assessment_id: a-6bc014ac72b91abc
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-e89b902374249843
  evidence_ids:
  - ev-530b617263972d93
  - ev-6bc014ac72b91abc
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-530b617263972d93
    - ev-6bc014ac72b91abc
findings:
- finding_id: rec-f-91186c5544f7e8da
  issue_key: mim-reconciliation-role-support-e89b902374249843
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Tuberactinomycin'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-e89b902374249843
  evidence_ids:
  - ev-530b617263972d93
  - ev-6bc014ac72b91abc
  - ev-f634ee75d93a30ff
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Tuberactinomycin.yaml
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
    review_id: 20261011T024639Z-mim-reconcile-all-batch-12
    finding_id: f-91186c5544f7e8da
actions:
- action_id: rec-action-91186c5544f7e8da
  description: 'Reassess prediction-only role support: Tuberactinomycin'
  finding_ids:
  - rec-f-91186c5544f7e8da
  target_ids:
  - record-e89b902374249843
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Tuberactinomycin.yaml
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
  with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.
````
