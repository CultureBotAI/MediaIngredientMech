# Per-record structured review: 3-hydroxybutyric_Acid (data/ingredients/mapped/3-hydroxybutyric_Acid.yaml)

- Review: 20261017T083000Z-3-hydroxybutyric-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 3-hydroxybutyric_Acid (data/ingredients/mapped/3-hydroxybutyric_Acid.yaml, record-11a6b1096c808da0, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/3-hydroxybutyric_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/3-hydroxybutyric_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-11a6b1096c808da0 | data/ingredients/mapped/3-hydroxybutyric_Acid.yaml | maintained | 3-hydroxybutyric_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-11a6b1096c808da0 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-11a6b1096c808da0 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-11a6b1096c808da0 | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-11a6b1096c808da0.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-11a6b1096c808da0.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T06:06:04Z; reviewed SHA-256=ae88860da0aed468ee8bf9ab2751050a59459240efcac34d9c0a16dc0744dec2; current SHA-256=ae88860da0aed468ee8bf9ab2751050a59459240efcac34d9c0a16dc0744dec2; hash_changed=False. Reports=["reports/yaml_record_review/3-hydroxybutyric_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Active CHEBI neutral-acid identity, CAS, chemistry, SSSOM, and aggregate pass, but CARBON_SOURCE is only supported by provisional name-pattern evidence.

### Historical provisional-role concern

evidence: concern. Targets: record-11a6b1096c808da0.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-a9ec55d840d0659c: Reassess prediction-only role support: 3-hydroxybutyric acid

major / open / confirmed; issue key: mim-reconciliation-role-support-11a6b1096c808da0.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-a9ec55d840d0659c

Reassess prediction-only role support: 3-hydroxybutyric acid

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-ec0fc9d968627f26 | data/ingredients/mapped/3-hydroxybutyric_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[363],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:20067","line":365,"mapping_status":"MAPPED","ontology_id":"CHEBI:20067","preferred_term":"3-hydroxybutyric acid"}],"identifier":"CHEBI:20067","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:20067","ontology_label":"3-hydroxybutyric acid","ontology_source":"CHEBI"},"preferred_term":"3-hydroxybutyric acid","sssom_rows":[{"data_row":146,"object_id":"CHEBI:20067","object_label":"3-hydroxybutyric acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:3-hydroxybutyric_Acid","synonym_count":1} |
| ev-ecd795afb19c56ad | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [363] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-32512f9fc287af73 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:3-hydroxybutyric_Acid; data-row positions=[146] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":146,"object_id":"CHEBI:20067","object_label":"3-hydroxybutyric acid","other":"3-hydroxybutanoic acid&#124;CAS:300-85-6","predicate_id":"skos:exactMatch","subject_id":"MIM:3-hydroxybutyric_Acid","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-340af5802fece1a8 | docs/data/mapped_ingredients.csv; CSV lines=[365] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:20067","line":365,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:20067","preferred_term":"3-hydroxybutyric acid","total_occurrences":"0"}] |
| ev-10dbd315f8f5e7c9 | reports/yaml_record_review/3-hydroxybutyric_Acid.md; &#96;data/ingredients/mapped/3-hydroxybutyric_Acid.yaml&#96;:2; Verdict:4; Identity:11; Validation:24; Evidence:35; Completeness:55; Recommended Edits:62 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-dab31e5ecf5aaf94 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[122,1813] | context_only | [{"current_record_sha256":"ae88860da0aed468ee8bf9ab2751050a59459240efcac34d9c0a16dc0744dec2","finding_id":"SEM:aabe20badedf367f1ee9","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"ae88860da0aed468ee8bf9ab2751050a59459240efcac34d9c0a16dc0744dec2","finding_id":"SEM:5f27bbc238bb90494f57","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-9f3e6c7761524216 | data/ingredients/mapped/3-hydroxybutyric_Acid.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}] |
| ev-76faacef83587488 | reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml; findings[finding_id=f-a9ec55d840d0659c] | context_only | Predecessor structured review finding f-a9ec55d840d0659c in 20261011T024630Z-mim-reconcile-all-batch-02 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-3-hydroxybutyric-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 3-hydroxybutyric_Acid (data/ingredients/mapped/3-hydroxybutyric_Acid.yaml)'
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
summary: Per-record structured review for 3-hydroxybutyric_Acid (data/ingredients/mapped/3-hydroxybutyric_Acid.yaml,
  record-11a6b1096c808da0, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/3-hydroxybutyric_Acid.yaml
    sha256: ae88860da0aed468ee8bf9ab2751050a59459240efcac34d9c0a16dc0744dec2
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
  - path: reports/yaml_record_review/3-hydroxybutyric_Acid.md
    sha256: 0f7ffb6fbf14d44036141cbf1ffb7e2fd2b65bba2d12934b852954409b7e1df7
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-11a6b1096c808da0
  path: data/ingredients/mapped/3-hydroxybutyric_Acid.yaml
  label: 3-hydroxybutyric_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/3-hydroxybutyric_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/3-hydroxybutyric_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/3-hydroxybutyric_Acid.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-11a6b1096c808da0
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-11a6b1096c808da0
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-11a6b1096c808da0
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-11a6b1096c808da0
evidence:
- evidence_id: ev-ec0fc9d968627f26
  kind: record_content
  reference: data/ingredients/mapped/3-hydroxybutyric_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[363],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:20067","line":365,"mapping_status":"MAPPED","ontology_id":"CHEBI:20067","preferred_term":"3-hydroxybutyric
    acid"}],"identifier":"CHEBI:20067","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:20067","ontology_label":"3-hydroxybutyric
    acid","ontology_source":"CHEBI"},"preferred_term":"3-hydroxybutyric acid","sssom_rows":[{"data_row":146,"object_id":"CHEBI:20067","object_label":"3-hydroxybutyric
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:3-hydroxybutyric_Acid","synonym_count":1}'
  snapshot_sha256: ae88860da0aed468ee8bf9ab2751050a59459240efcac34d9c0a16dc0744dec2
- evidence_id: ev-ecd795afb19c56ad
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [363]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-32512f9fc287af73
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:3-hydroxybutyric_Acid; data-row positions=[146]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":146,"object_id":"CHEBI:20067","object_label":"3-hydroxybutyric
    acid","other":"3-hydroxybutanoic acid|CAS:300-85-6","predicate_id":"skos:exactMatch","subject_id":"MIM:3-hydroxybutyric_Acid","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-340af5802fece1a8
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[365]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:20067","line":365,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:20067","preferred_term":"3-hydroxybutyric
    acid","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-10dbd315f8f5e7c9
  kind: prior_review
  reference: reports/yaml_record_review/3-hydroxybutyric_Acid.md
  locator: '`data/ingredients/mapped/3-hydroxybutyric_Acid.yaml`:2; Verdict:4; Identity:11;
    Validation:24; Evidence:35; Completeness:55; Recommended Edits:62'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 0f7ffb6fbf14d44036141cbf1ffb7e2fd2b65bba2d12934b852954409b7e1df7
  quote: "Recommended Edits:\n1. In `data/ingredients/mapped/3-hydroxybutyric_Acid.yaml`,\
    \ either replace the\n   provisional `CARBON_SOURCE` evidence with inspected,\
    \ claim-level evidence or\n   remove the role.\n2. Run `just sync-curated`, rebuild\
    \ SSSOM and docs, then verify with\n   `just validate-all`, `just qc-sssom`, `just\
    \ qc-roundtrip`, and\n   `just validate-terms data/ingredients/mapped/3-hydroxybutyric_Acid.yaml`."
- evidence_id: ev-dab31e5ecf5aaf94
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[122,1813]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"ae88860da0aed468ee8bf9ab2751050a59459240efcac34d9c0a16dc0744dec2","finding_id":"SEM:aabe20badedf367f1ee9","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"ae88860da0aed468ee8bf9ab2751050a59459240efcac34d9c0a16dc0744dec2","finding_id":"SEM:5f27bbc238bb90494f57","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-9f3e6c7761524216
  kind: record_content
  reference: data/ingredients/mapped/3-hydroxybutyric_Acid.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}]'
  snapshot_sha256: ae88860da0aed468ee8bf9ab2751050a59459240efcac34d9c0a16dc0744dec2
- evidence_id: ev-76faacef83587488
  kind: prior_review
  reference: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
  locator: findings[finding_id=f-a9ec55d840d0659c]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-a9ec55d840d0659c in 20261011T024630Z-mim-reconcile-all-batch-02
  snapshot_sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
assessments:
- assessment_id: a-e4b6e105d34d3f19
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-11a6b1096c808da0
  evidence_ids:
  - ev-ec0fc9d968627f26
  - ev-ecd795afb19c56ad
  - ev-32512f9fc287af73
  - ev-340af5802fece1a8
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-c29015493f6a8c7b
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-11a6b1096c808da0
  evidence_ids:
  - ev-10dbd315f8f5e7c9
  - ev-ec0fc9d968627f26
  - ev-dab31e5ecf5aaf94
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T06:06:04Z;
    reviewed SHA-256=ae88860da0aed468ee8bf9ab2751050a59459240efcac34d9c0a16dc0744dec2;
    current SHA-256=ae88860da0aed468ee8bf9ab2751050a59459240efcac34d9c0a16dc0744dec2;
    hash_changed=False. Reports=["reports/yaml_record_review/3-hydroxybutyric_Acid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Active CHEBI
    neutral-acid identity, CAS, chemistry, SSSOM, and aggregate pass, but CARBON_SOURCE
    is only supported by provisional name-pattern evidence.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-10dbd315f8f5e7c9
    - ev-ec0fc9d968627f26
  - name: legacy-native-ids
    value: '["SEM:aabe20badedf367f1ee9","SEM:5f27bbc238bb90494f57"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-ec0fc9d968627f26
    - ev-10dbd315f8f5e7c9
    - ev-dab31e5ecf5aaf94
- assessment_id: a-9f3e6c7761524216
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-11a6b1096c808da0
  evidence_ids:
  - ev-10dbd315f8f5e7c9
  - ev-9f3e6c7761524216
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-10dbd315f8f5e7c9
    - ev-9f3e6c7761524216
findings:
- finding_id: rec-f-a9ec55d840d0659c
  issue_key: mim-reconciliation-role-support-11a6b1096c808da0
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: 3-hydroxybutyric acid'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-11a6b1096c808da0
  evidence_ids:
  - ev-10dbd315f8f5e7c9
  - ev-9f3e6c7761524216
  - ev-76faacef83587488
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/3-hydroxybutyric_Acid.yaml
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
    finding_id: f-a9ec55d840d0659c
actions:
- action_id: rec-action-a9ec55d840d0659c
  description: 'Reassess prediction-only role support: 3-hydroxybutyric acid'
  finding_ids:
  - rec-f-a9ec55d840d0659c
  target_ids:
  - record-11a6b1096c808da0
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/3-hydroxybutyric_Acid.yaml
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
