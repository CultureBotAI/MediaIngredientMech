# Per-record structured review: Proteose_Peptone_No_2 (data/ingredients/mapped/Proteose_Peptone_No_2.yaml)

- Review: 20261017T083000Z-proteose-peptone-no-2
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Proteose_Peptone_No_2 (data/ingredients/mapped/Proteose_Peptone_No_2.yaml, record-18eab9407fa93a81, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Proteose_Peptone_No_2.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Proteose_Peptone_No_2.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-18eab9407fa93a81 | data/ingredients/mapped/Proteose_Peptone_No_2.yaml | maintained | Proteose_Peptone_No_2 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-18eab9407fa93a81 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-18eab9407fa93a81 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-18eab9407fa93a81 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-18eab9407fa93a81.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-18eab9407fa93a81.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:03:13Z; reviewed SHA-256=67ca4baee47a98b1ccd293403503a20d1ed757055d179658689f9ab7a6a17533; current SHA-256=67ca4baee47a98b1ccd293403503a20d1ed757055d179658689f9ab7a6a17533; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050313Z-Proteose_Peptone_No_2.md","reports/yaml_record_review/Proteose_Peptone_No_2.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Proteose_Peptone_No_2.md&#96; after the record changed from af94aaec0512002f2a0bc17f08a78937b0ed877ed419d232904e6553464890de to 67ca4baee47a98b1ccd293403503a20d1ed757055d179658689f9ab7a6a17533; preserved the previous major finding floor pending targeted retirement.

### Historical provisional-role concern

evidence: concern. Targets: record-18eab9407fa93a81.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-78598efbb1634fc5: Reassess prediction-only role support: Proteose peptone no. 2

major / open / confirmed; issue key: mim-reconciliation-role-support-18eab9407fa93a81.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-78598efbb1634fc5

Reassess prediction-only role support: Proteose peptone no. 2

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-705b93bccd0fe4f1 | data/ingredients/mapped/Proteose_Peptone_No_2.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2660],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0002393","line":2662,"mapping_status":"MAPPED","ontology_id":"MICRO:0002393","preferred_term":"Proteose peptone no. 2"}],"identifier":"MICRO:0002393","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7,"edge_count":7,"occurrences":7},"occurrence_statistics":{"media_count":7,"total_occurrences":7},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"MICRO:0002393","ontology_label":"Proteose Peptone No. 2","ontology_source":"MICRO"},"preferred_term":"Proteose peptone no. 2","sssom_rows":[{"data_row":2356,"object_id":"MICRO:0002393","object_label":"Proteose Peptone No. 2","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Proteose_Peptone_No_2","synonym_count":1} |
| ev-6bcc1606f22e4022 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2660] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-fdeef0821152f3fb | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Proteose_Peptone_No_2; data-row positions=[2356] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2356,"object_id":"MICRO:0002393","object_label":"Proteose Peptone No. 2","other":"Proteose peptone No 2 (DIFCO 0121-01-3)","predicate_id":"skos:exactMatch","subject_id":"MIM:Proteose_Peptone_No_2","validation_method":"manual:restore_micro_source_identities&#124;KGX_SOURCE&#124;2026-09-23"}] |
| ev-1b29b99150dee420 | docs/data/mapped_ingredients.csv; CSV lines=[2662] | supports | Published identity and count rows inspected: [{"identifier":"MICRO:0002393","line":2662,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"7","ontology_id":"MICRO:0002393","preferred_term":"Proteose peptone no. 2","total_occurrences":"7"}] |
| ev-e8176879e90b3936 | reports/yaml_record_review/20261001T050313Z-Proteose_Peptone_No_2.md; YAML Record Review: Proteose peptone no. 2:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-24bd9c11b1b55801 | reports/yaml_record_review/Proteose_Peptone_No_2.md; &#96;data/ingredients/mapped/Proteose_Peptone_No_2.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-4d27bbd4151796c5 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1145,1818] | context_only | [{"current_record_sha256":"67ca4baee47a98b1ccd293403503a20d1ed757055d179658689f9ab7a6a17533","finding_id":"SEM:94a18023493c80b0566e","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"67ca4baee47a98b1ccd293403503a20d1ed757055d179658689f9ab7a6a17533","finding_id":"SEM:e53960c7b82d36e71749","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-600787c7506494bc | data/ingredients/mapped/Proteose_Peptone_No_2.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"PROTEIN_SOURCE"}}] |
| ev-278c77f52ef466f7 | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml; findings[finding_id=f-78598efbb1634fc5] | context_only | Predecessor structured review finding f-78598efbb1634fc5 in 20261011T024638Z-mim-reconcile-all-batch-10 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-proteose-peptone-no-2
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Proteose_Peptone_No_2 (data/ingredients/mapped/Proteose_Peptone_No_2.yaml)'
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
summary: Per-record structured review for Proteose_Peptone_No_2 (data/ingredients/mapped/Proteose_Peptone_No_2.yaml,
  record-18eab9407fa93a81, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Proteose_Peptone_No_2.yaml
    sha256: 67ca4baee47a98b1ccd293403503a20d1ed757055d179658689f9ab7a6a17533
    role: target
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
    sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
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
  - path: reports/yaml_record_review/20261001T050313Z-Proteose_Peptone_No_2.md
    sha256: 3ae009dfd848fd7f4c6911fecb22f9e58b0003623f79ce2f36387dcde35c5d00
    role: context
  - path: reports/yaml_record_review/Proteose_Peptone_No_2.md
    sha256: b7ef0c08e9707121a5f96b22fad1ac2898fbc46d3e2f0640dee22bf9fdb1b0fd
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-18eab9407fa93a81
  path: data/ingredients/mapped/Proteose_Peptone_No_2.yaml
  label: Proteose_Peptone_No_2
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Proteose_Peptone_No_2.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Proteose_Peptone_No_2.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Proteose_Peptone_No_2.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-18eab9407fa93a81
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-18eab9407fa93a81
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-18eab9407fa93a81
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10
    and semantic review dispositions on HEAD.
  target_ids:
  - record-18eab9407fa93a81
evidence:
- evidence_id: ev-705b93bccd0fe4f1
  kind: record_content
  reference: data/ingredients/mapped/Proteose_Peptone_No_2.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2660],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0002393","line":2662,"mapping_status":"MAPPED","ontology_id":"MICRO:0002393","preferred_term":"Proteose
    peptone no. 2"}],"identifier":"MICRO:0002393","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7,"edge_count":7,"occurrences":7},"occurrence_statistics":{"media_count":7,"total_occurrences":7},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"MICRO:0002393","ontology_label":"Proteose
    Peptone No. 2","ontology_source":"MICRO"},"preferred_term":"Proteose peptone no.
    2","sssom_rows":[{"data_row":2356,"object_id":"MICRO:0002393","object_label":"Proteose
    Peptone No. 2","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Proteose_Peptone_No_2","synonym_count":1}'
  snapshot_sha256: 67ca4baee47a98b1ccd293403503a20d1ed757055d179658689f9ab7a6a17533
- evidence_id: ev-6bcc1606f22e4022
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2660]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-fdeef0821152f3fb
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Proteose_Peptone_No_2; data-row positions=[2356]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2356,"object_id":"MICRO:0002393","object_label":"Proteose
    Peptone No. 2","other":"Proteose peptone No 2 (DIFCO 0121-01-3)","predicate_id":"skos:exactMatch","subject_id":"MIM:Proteose_Peptone_No_2","validation_method":"manual:restore_micro_source_identities|KGX_SOURCE|2026-09-23"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-1b29b99150dee420
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2662]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"MICRO:0002393","line":2662,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"7","ontology_id":"MICRO:0002393","preferred_term":"Proteose
    peptone no. 2","total_occurrences":"7"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-e8176879e90b3936
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050313Z-Proteose_Peptone_No_2.md
  locator: 'YAML Record Review: Proteose peptone no. 2:2; Target:10; Validation:20;
    Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended
    Edits:56; Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 3ae009dfd848fd7f4c6911fecb22f9e58b0003623f79ce2f36387dcde35c5d00
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/Proteose_Peptone_No_2.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The local
    No. 2 identity and MICRO parent pass, but PROTEIN_SOURCE is provisional.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Proteose_Peptone_No_2.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Proteose_Peptone_No_2.yaml`,
    `just validate-terms data/ingredients/mapped/Proteose_Peptone_No_2.yaml` where
    applicable, and `just qc-sssom`.'
- evidence_id: ev-24bd9c11b1b55801
  kind: prior_review
  reference: reports/yaml_record_review/Proteose_Peptone_No_2.md
  locator: '`data/ingredients/mapped/Proteose_Peptone_No_2.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: b7ef0c08e9707121a5f96b22fad1ac2898fbc46d3e2f0640dee22bf9fdb1b0fd
- evidence_id: ev-4d27bbd4151796c5
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1145,1818]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"67ca4baee47a98b1ccd293403503a20d1ed757055d179658689f9ab7a6a17533","finding_id":"SEM:94a18023493c80b0566e","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"67ca4baee47a98b1ccd293403503a20d1ed757055d179658689f9ab7a6a17533","finding_id":"SEM:e53960c7b82d36e71749","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-600787c7506494bc
  kind: record_content
  reference: data/ingredients/mapped/Proteose_Peptone_No_2.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"PROTEIN_SOURCE"}}]'
  snapshot_sha256: 67ca4baee47a98b1ccd293403503a20d1ed757055d179658689f9ab7a6a17533
- evidence_id: ev-278c77f52ef466f7
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
  locator: findings[finding_id=f-78598efbb1634fc5]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-78598efbb1634fc5 in 20261011T024638Z-mim-reconcile-all-batch-10
  snapshot_sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
assessments:
- assessment_id: a-956be786fb16968f
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-18eab9407fa93a81
  evidence_ids:
  - ev-705b93bccd0fe4f1
  - ev-6bcc1606f22e4022
  - ev-fdeef0821152f3fb
  - ev-1b29b99150dee420
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-93078f3a0f98148e
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-18eab9407fa93a81
  evidence_ids:
  - ev-e8176879e90b3936
  - ev-24bd9c11b1b55801
  - ev-705b93bccd0fe4f1
  - ev-4d27bbd4151796c5
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:03:13Z;
    reviewed SHA-256=67ca4baee47a98b1ccd293403503a20d1ed757055d179658689f9ab7a6a17533;
    current SHA-256=67ca4baee47a98b1ccd293403503a20d1ed757055d179658689f9ab7a6a17533;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050313Z-Proteose_Peptone_No_2.md","reports/yaml_record_review/Proteose_Peptone_No_2.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Proteose_Peptone_No_2.md` after the record changed
    from af94aaec0512002f2a0bc17f08a78937b0ed877ed419d232904e6553464890de to 67ca4baee47a98b1ccd293403503a20d1ed757055d179658689f9ab7a6a17533;
    preserved the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-e8176879e90b3936
    - ev-24bd9c11b1b55801
    - ev-705b93bccd0fe4f1
  - name: legacy-native-ids
    value: '["SEM:94a18023493c80b0566e","SEM:e53960c7b82d36e71749"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-705b93bccd0fe4f1
    - ev-e8176879e90b3936
    - ev-24bd9c11b1b55801
    - ev-4d27bbd4151796c5
- assessment_id: a-600787c7506494bc
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-18eab9407fa93a81
  evidence_ids:
  - ev-e8176879e90b3936
  - ev-24bd9c11b1b55801
  - ev-600787c7506494bc
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-e8176879e90b3936
    - ev-24bd9c11b1b55801
    - ev-600787c7506494bc
findings:
- finding_id: rec-f-78598efbb1634fc5
  issue_key: mim-reconciliation-role-support-18eab9407fa93a81
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Proteose peptone no. 2'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-18eab9407fa93a81
  evidence_ids:
  - ev-e8176879e90b3936
  - ev-24bd9c11b1b55801
  - ev-600787c7506494bc
  - ev-278c77f52ef466f7
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Proteose_Peptone_No_2.yaml
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
    review_id: 20261011T024638Z-mim-reconcile-all-batch-10
    finding_id: f-78598efbb1634fc5
actions:
- action_id: rec-action-78598efbb1634fc5
  description: 'Reassess prediction-only role support: Proteose peptone no. 2'
  finding_ids:
  - rec-f-78598efbb1634fc5
  target_ids:
  - record-18eab9407fa93a81
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Proteose_Peptone_No_2.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.
```
