# Per-record structured review: Phenyl_Acetic_Acid (data/ingredients/mapped/Phenyl_Acetic_Acid.yaml)

- Review: 20261017T083000Z-phenyl-acetic-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Phenyl_Acetic_Acid (data/ingredients/mapped/Phenyl_Acetic_Acid.yaml, record-206b2de362210476, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Phenyl_Acetic_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Phenyl_Acetic_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-206b2de362210476 | data/ingredients/mapped/Phenyl_Acetic_Acid.yaml | maintained | Phenyl_Acetic_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-206b2de362210476 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-206b2de362210476 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-206b2de362210476 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-206b2de362210476.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-206b2de362210476.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:03:08Z; reviewed SHA-256=2d658c1eee89159e16e54af30159cd7345983f57fce943ab5858d00bc43e1a7b; current SHA-256=2d658c1eee89159e16e54af30159cd7345983f57fce943ab5858d00bc43e1a7b; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050308Z-Phenyl_Acetic_Acid.md","reports/yaml_record_review/Phenyl_Acetic_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Phenyl_Acetic_Acid.md&#96; after the record changed from 9b3c34056f552c0fe0d5645ba43b914fdf287f85c7afd1cafd2fd0a19a08bc58 to 2d658c1eee89159e16e54af30159cd7345983f57fce943ab5858d00bc43e1a7b; preserved the previous major finding floor pending targeted retirement.

### Historical provisional-role concern

evidence: concern. Targets: record-206b2de362210476.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-d5617c4a7b808a73: Reassess prediction-only role support: Phenyl acetic acid

major / open / confirmed; issue key: mim-reconciliation-role-support-206b2de362210476.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-d5617c4a7b808a73

Reassess prediction-only role support: Phenyl acetic acid

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-a71425b482482a5b | data/ingredients/mapped/Phenyl_Acetic_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1643],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:30745","line":1645,"mapping_status":"MAPPED","ontology_id":"CHEBI:30745","preferred_term":"Phenyl acetic acid"}],"identifier":"CHEBI:30745","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":6,"edge_count":6,"occurrences":6},"occurrence_statistics":{"media_count":6,"total_occurrences":6},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:30745","ontology_label":"phenylacetic acid","ontology_source":"CHEBI"},"preferred_term":"Phenyl acetic acid","sssom_rows":[{"data_row":2236,"object_id":"CHEBI:30745","object_label":"phenylacetic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Phenyl_Acetic_Acid","synonym_count":2} |
| ev-332bbba8a3feb4ae | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1643] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-b29bb965cb2a2ed9 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Phenyl_Acetic_Acid; data-row positions=[2236] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2236,"object_id":"CHEBI:30745","object_label":"phenylacetic acid","other":"CAS:103-82-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Phenyl_Acetic_Acid","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-44c424ce1359bf09 | docs/data/mapped_ingredients.csv; CSV lines=[1645] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:30745","line":1645,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"6","ontology_id":"CHEBI:30745","preferred_term":"Phenyl acetic acid","total_occurrences":"6"}] |
| ev-b6b29c78d83060ce | reports/yaml_record_review/20261001T050308Z-Phenyl_Acetic_Acid.md; YAML Record Review: Phenyl acetic acid:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-3947bfc482f0a6da | reports/yaml_record_review/Phenyl_Acetic_Acid.md; &#96;data/ingredients/mapped/Phenyl_Acetic_Acid.yaml&#96;:2; Verdict:4; Identity:10; Validation:19; Evidence:31; Completeness:44; Recommended Edits:50 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-314bbf41acc66d54 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1104,1720] | context_only | [{"current_record_sha256":"2d658c1eee89159e16e54af30159cd7345983f57fce943ab5858d00bc43e1a7b","finding_id":"SEM:9636e42840c48c4dc0d8","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"2d658c1eee89159e16e54af30159cd7345983f57fce943ab5858d00bc43e1a7b","finding_id":"SEM:e747ce389dea1d02bf4d","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-fc239bd389688cc7 | data/ingredients/mapped/Phenyl_Acetic_Acid.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional in-session LLM role assignment; review recommended.","reference_text":"Assigned by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}] |
| ev-0f697c795f87c605 | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml; findings[finding_id=f-d5617c4a7b808a73] | context_only | Predecessor structured review finding f-d5617c4a7b808a73 in 20261011T024638Z-mim-reconcile-all-batch-10 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-phenyl-acetic-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Phenyl_Acetic_Acid (data/ingredients/mapped/Phenyl_Acetic_Acid.yaml)'
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
summary: Per-record structured review for Phenyl_Acetic_Acid (data/ingredients/mapped/Phenyl_Acetic_Acid.yaml,
  record-206b2de362210476, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Phenyl_Acetic_Acid.yaml
    sha256: 2d658c1eee89159e16e54af30159cd7345983f57fce943ab5858d00bc43e1a7b
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
  - path: reports/yaml_record_review/20261001T050308Z-Phenyl_Acetic_Acid.md
    sha256: f176f111986024e4e1b67a46139e9863fbd0d9b6a3545b6921ca18c379dd92a7
    role: context
  - path: reports/yaml_record_review/Phenyl_Acetic_Acid.md
    sha256: 6a039e2a4446b183d486abda423cebf0985e9a2308e5588e85b67b39d74da097
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-206b2de362210476
  path: data/ingredients/mapped/Phenyl_Acetic_Acid.yaml
  label: Phenyl_Acetic_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Phenyl_Acetic_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Phenyl_Acetic_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Phenyl_Acetic_Acid.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-206b2de362210476
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-206b2de362210476
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-206b2de362210476
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10
    and semantic review dispositions on HEAD.
  target_ids:
  - record-206b2de362210476
evidence:
- evidence_id: ev-a71425b482482a5b
  kind: record_content
  reference: data/ingredients/mapped/Phenyl_Acetic_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1643],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:30745","line":1645,"mapping_status":"MAPPED","ontology_id":"CHEBI:30745","preferred_term":"Phenyl
    acetic acid"}],"identifier":"CHEBI:30745","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":6,"edge_count":6,"occurrences":6},"occurrence_statistics":{"media_count":6,"total_occurrences":6},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:30745","ontology_label":"phenylacetic
    acid","ontology_source":"CHEBI"},"preferred_term":"Phenyl acetic acid","sssom_rows":[{"data_row":2236,"object_id":"CHEBI:30745","object_label":"phenylacetic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Phenyl_Acetic_Acid","synonym_count":2}'
  snapshot_sha256: 2d658c1eee89159e16e54af30159cd7345983f57fce943ab5858d00bc43e1a7b
- evidence_id: ev-332bbba8a3feb4ae
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1643]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-b29bb965cb2a2ed9
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Phenyl_Acetic_Acid; data-row positions=[2236]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2236,"object_id":"CHEBI:30745","object_label":"phenylacetic
    acid","other":"CAS:103-82-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Phenyl_Acetic_Acid","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-44c424ce1359bf09
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1645]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:30745","line":1645,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"6","ontology_id":"CHEBI:30745","preferred_term":"Phenyl
    acetic acid","total_occurrences":"6"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-b6b29c78d83060ce
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050308Z-Phenyl_Acetic_Acid.md
  locator: 'YAML Record Review: Phenyl acetic acid:2; Target:10; Validation:20; Identity
    and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: f176f111986024e4e1b67a46139e9863fbd0d9b6a3545b6921ca18c379dd92a7
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/Phenyl_Acetic_Acid.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The corrected
    CHEBI:30745 phenylacetic-acid identity passes, but final other exports LSM-15166
    and CARBON_SOURCE is provisional.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Phenyl_Acetic_Acid.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Phenyl_Acetic_Acid.yaml`,
    `just validate-terms data/ingredients/mapped/Phenyl_Acetic_Acid.yaml` where applicable,
    and `just qc-sssom`.'
- evidence_id: ev-3947bfc482f0a6da
  kind: prior_review
  reference: reports/yaml_record_review/Phenyl_Acetic_Acid.md
  locator: '`data/ingredients/mapped/Phenyl_Acetic_Acid.yaml`:2; Verdict:4; Identity:10;
    Validation:19; Evidence:31; Completeness:44; Recommended Edits:50'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 6a039e2a4446b183d486abda423cebf0985e9a2308e5588e85b67b39d74da097
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Phenyl_Acetic_Acid.yaml`,\
    \ retype or remove\n  `LSM-15166` so it is retained, if needed, only as rejected\
    \ provenance for the\n  remapping from `CHEBI:103822` and no longer appears in\
    \ final SSSOM `other`.\n- Major: replace `nutritional_roles.CARBON_SOURCE` with\
    \ source-backed evidence\n  or remove the provisional role facet until it is curated."
- evidence_id: ev-314bbf41acc66d54
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1104,1720]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"2d658c1eee89159e16e54af30159cd7345983f57fce943ab5858d00bc43e1a7b","finding_id":"SEM:9636e42840c48c4dc0d8","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"2d658c1eee89159e16e54af30159cd7345983f57fce943ab5858d00bc43e1a7b","finding_id":"SEM:e747ce389dea1d02bf4d","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-fc239bd389688cc7
  kind: record_content
  reference: data/ingredients/mapped/Phenyl_Acetic_Acid.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional
    in-session LLM role assignment; review recommended.","reference_text":"Assigned
    by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}]'
  snapshot_sha256: 2d658c1eee89159e16e54af30159cd7345983f57fce943ab5858d00bc43e1a7b
- evidence_id: ev-0f697c795f87c605
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
  locator: findings[finding_id=f-d5617c4a7b808a73]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-d5617c4a7b808a73 in 20261011T024638Z-mim-reconcile-all-batch-10
  snapshot_sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
assessments:
- assessment_id: a-4d8bcf13aa92a0d5
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-206b2de362210476
  evidence_ids:
  - ev-a71425b482482a5b
  - ev-332bbba8a3feb4ae
  - ev-b29bb965cb2a2ed9
  - ev-44c424ce1359bf09
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-fe675bfd5871fae9
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-206b2de362210476
  evidence_ids:
  - ev-b6b29c78d83060ce
  - ev-3947bfc482f0a6da
  - ev-a71425b482482a5b
  - ev-314bbf41acc66d54
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:03:08Z;
    reviewed SHA-256=2d658c1eee89159e16e54af30159cd7345983f57fce943ab5858d00bc43e1a7b;
    current SHA-256=2d658c1eee89159e16e54af30159cd7345983f57fce943ab5858d00bc43e1a7b;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050308Z-Phenyl_Acetic_Acid.md","reports/yaml_record_review/Phenyl_Acetic_Acid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Phenyl_Acetic_Acid.md` after the record changed from
    9b3c34056f552c0fe0d5645ba43b914fdf287f85c7afd1cafd2fd0a19a08bc58 to 2d658c1eee89159e16e54af30159cd7345983f57fce943ab5858d00bc43e1a7b;
    preserved the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b6b29c78d83060ce
    - ev-3947bfc482f0a6da
    - ev-a71425b482482a5b
  - name: legacy-native-ids
    value: '["SEM:9636e42840c48c4dc0d8","SEM:e747ce389dea1d02bf4d"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-a71425b482482a5b
    - ev-b6b29c78d83060ce
    - ev-3947bfc482f0a6da
    - ev-314bbf41acc66d54
- assessment_id: a-fc239bd389688cc7
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-206b2de362210476
  evidence_ids:
  - ev-b6b29c78d83060ce
  - ev-3947bfc482f0a6da
  - ev-fc239bd389688cc7
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b6b29c78d83060ce
    - ev-3947bfc482f0a6da
    - ev-fc239bd389688cc7
findings:
- finding_id: rec-f-d5617c4a7b808a73
  issue_key: mim-reconciliation-role-support-206b2de362210476
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Phenyl acetic acid'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-206b2de362210476
  evidence_ids:
  - ev-b6b29c78d83060ce
  - ev-3947bfc482f0a6da
  - ev-fc239bd389688cc7
  - ev-0f697c795f87c605
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Phenyl_Acetic_Acid.yaml
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
    finding_id: f-d5617c4a7b808a73
actions:
- action_id: rec-action-d5617c4a7b808a73
  description: 'Reassess prediction-only role support: Phenyl acetic acid'
  finding_ids:
  - rec-f-d5617c4a7b808a73
  target_ids:
  - record-206b2de362210476
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Phenyl_Acetic_Acid.yaml
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
