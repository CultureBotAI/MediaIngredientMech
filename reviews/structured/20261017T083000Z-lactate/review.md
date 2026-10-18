# Per-record structured review: Lactate (data/ingredients/mapped/Lactate.yaml)

- Review: 20261017T083000Z-lactate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Lactate (data/ingredients/mapped/Lactate.yaml, record-09c27e9da38f0c74, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Lactate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Lactate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-09c27e9da38f0c74 | data/ingredients/mapped/Lactate.yaml | maintained | Lactate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-09c27e9da38f0c74 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-09c27e9da38f0c74 | Role assertions on nutritional_roles[0], nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-09c27e9da38f0c74 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-09c27e9da38f0c74.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-09c27e9da38f0c74.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:38Z; reviewed SHA-256=31c51bf1fe574408d0283a89af8923db94f20cdd5405817ad2b35fea8a5f5891; current SHA-256=31c51bf1fe574408d0283a89af8923db94f20cdd5405817ad2b35fea8a5f5891; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050238Z-Lactate.md","reports/yaml_record_review/Lactate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Lactate.md&#96; after the record changed from 473205bc13ea916770dad2ffb219c57d34b1ec2caa5e4ef5a4573443f4043474 to 31c51bf1fe574408d0283a89af8923db94f20cdd5405817ad2b35fea8a5f5891; preserved the previous major finding floor pending targeted retirement.

### Historical provisional-role concern

evidence: concern. Targets: record-09c27e9da38f0c74.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-fcf00281c538a1c1: Reassess prediction-only role support: Lactate

major / open / confirmed; issue key: mim-reconciliation-role-support-09c27e9da38f0c74.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-fcf00281c538a1c1

Reassess prediction-only role support: Lactate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-2376cc2eeed5c087 | data/ingredients/mapped/Lactate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1274],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:24996","line":1276,"mapping_status":"MAPPED","ontology_id":"CHEBI:24996","preferred_term":"Lactate"}],"identifier":"CHEBI:24996","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":9,"edge_count":9,"occurrences":9},"occurrence_statistics":{"media_count":9,"total_occurrences":9},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:24996","ontology_label":"lactate","ontology_source":"CHEBI"},"preferred_term":"Lactate","sssom_rows":[{"data_row":1653,"object_id":"CHEBI:24996","object_label":"lactate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Lactate","synonym_count":13} |
| ev-1115f68d6256301a | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1274] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-7c23a5725d4e25eb | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Lactate; data-row positions=[1653] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1653,"object_id":"CHEBI:24996","object_label":"lactate","other":"(+)-lactate&#124;(2S)-2-hydroxypropanoate&#124;(S)-lactate&#124;2-hydroxypropanoate&#124;2-hydroxypropionate&#124;L(+)-lactate&#124;L-(+)-lactate&#124;L-lactate&#124;MeCH(OH)CO2 anion&#124;b-lactate&#124;beta-lactate&#124;DL-lactate&#124;CAS:113-21-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Lactate","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-bc5c532fec415cf7 | docs/data/mapped_ingredients.csv; CSV lines=[1276] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:24996","line":1276,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"9","ontology_id":"CHEBI:24996","preferred_term":"Lactate","total_occurrences":"9"}] |
| ev-5db3cf590d8514c0 | reports/yaml_record_review/20261001T050238Z-Lactate.md; YAML Record Review: Lactate:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-35ae159cbc725197 | reports/yaml_record_review/Lactate.md; &#96;data/ingredients/mapped/Lactate.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:29; Completeness:55; Recommended Edits:62 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-d2b5b81d27a89615 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[843,1386,1541] | context_only | [{"current_record_sha256":"31c51bf1fe574408d0283a89af8923db94f20cdd5405817ad2b35fea8a5f5891","finding_id":"SEM:00b1ac0c24fef647364c","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"31c51bf1fe574408d0283a89af8923db94f20cdd5405817ad2b35fea8a5f5891","finding_id":"SEM:6a709519a173ad04c3cd","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"31c51bf1fe574408d0283a89af8923db94f20cdd5405817ad2b35fea8a5f5891","finding_id":"SEM:c3a17a4e7f66270505a1","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-58f9d42d3330180f | data/ingredients/mapped/Lactate.yaml; nutritional_roles[0], nutritional_roles[1] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}},{"field":"nutritional_roles[1]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.","reference_text":"Canonical energy substrate (catabolised for energy)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"ENERGY_SOURCE"}}] |
| ev-54e9d0f70c54c217 | reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml; findings[finding_id=f-fcf00281c538a1c1] | context_only | Predecessor structured review finding f-fcf00281c538a1c1 in 20261011T024635Z-mim-reconcile-all-batch-07 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-lactate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Lactate (data/ingredients/mapped/Lactate.yaml)'
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
summary: Per-record structured review for Lactate (data/ingredients/mapped/Lactate.yaml,
  record-09c27e9da38f0c74, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Lactate.yaml
    sha256: 31c51bf1fe574408d0283a89af8923db94f20cdd5405817ad2b35fea8a5f5891
    role: target
  - path: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
    sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
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
  - path: reports/yaml_record_review/20261001T050238Z-Lactate.md
    sha256: ee7bcfbb89fc21dd96db23c06f2f4f6dfdabdb4996c0a7062af96a5cb2115572
    role: context
  - path: reports/yaml_record_review/Lactate.md
    sha256: 5f09b2ec1015032de2c0c0ac5184d7108185d4084d5714e56b91f3d9a5bbfaa2
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-09c27e9da38f0c74
  path: data/ingredients/mapped/Lactate.yaml
  label: Lactate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Lactate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Lactate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Lactate.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-09c27e9da38f0c74
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-09c27e9da38f0c74
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0], nutritional_roles[1] rely only
    on COMPUTATIONAL_PREDICTION or empty evidence.
  target_ids:
  - record-09c27e9da38f0c74
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-09c27e9da38f0c74
evidence:
- evidence_id: ev-2376cc2eeed5c087
  kind: record_content
  reference: data/ingredients/mapped/Lactate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1274],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:24996","line":1276,"mapping_status":"MAPPED","ontology_id":"CHEBI:24996","preferred_term":"Lactate"}],"identifier":"CHEBI:24996","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":9,"edge_count":9,"occurrences":9},"occurrence_statistics":{"media_count":9,"total_occurrences":9},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:24996","ontology_label":"lactate","ontology_source":"CHEBI"},"preferred_term":"Lactate","sssom_rows":[{"data_row":1653,"object_id":"CHEBI:24996","object_label":"lactate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Lactate","synonym_count":13}'
  snapshot_sha256: 31c51bf1fe574408d0283a89af8923db94f20cdd5405817ad2b35fea8a5f5891
- evidence_id: ev-1115f68d6256301a
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1274]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-7c23a5725d4e25eb
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Lactate; data-row positions=[1653]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1653,"object_id":"CHEBI:24996","object_label":"lactate","other":"(+)-lactate|(2S)-2-hydroxypropanoate|(S)-lactate|2-hydroxypropanoate|2-hydroxypropionate|L(+)-lactate|L-(+)-lactate|L-lactate|MeCH(OH)CO2
    anion|b-lactate|beta-lactate|DL-lactate|CAS:113-21-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Lactate","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-bc5c532fec415cf7
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1276]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:24996","line":1276,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"9","ontology_id":"CHEBI:24996","preferred_term":"Lactate","total_occurrences":"9"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-5db3cf590d8514c0
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050238Z-Lactate.md
  locator: 'YAML Record Review: Lactate:2; Target:10; Validation:20; Identity and
    Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: ee7bcfbb89fc21dd96db23c06f2f4f6dfdabdb4996c0a7062af96a5cb2115572
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/Lactate.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The exact
    generic CHEBI:24996 identity, CAS value, PubChem structure, and occurrence count
    pass, but final SSSOM exports process-qualified and L-specific synonyms and both
    nutritional roles are provisional.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Lactate.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Lactate.yaml`,
    `just validate-terms data/ingredients/mapped/Lactate.yaml` where applicable, and
    `just qc-sssom`.'
- evidence_id: ev-35ae159cbc725197
  kind: prior_review
  reference: reports/yaml_record_review/Lactate.md
  locator: '`data/ingredients/mapped/Lactate.yaml`:2; Verdict:4; Identity:11; Validation:21;
    Evidence:29; Completeness:55; Recommended Edits:62'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 5f09b2ec1015032de2c0c0ac5184d7108185d4084d5714e56b91f3d9a5bbfaa2
  quote: "Recommended Edits:\n- Major: remove `produces: DL-lactate` from active exact\
    \ synonyms in\n  `data/ingredients/mapped/Lactate.yaml` or retag it as provenance-only\
    \ so it no\n  longer reaches final SSSOM.\n- Major: remove the L-specific synonyms\
    \ from the generic `CHEBI:24996` record\n  or move any true L-lactate labels to\
    \ the exact L-lactate record that owns that\n  stereochemistry.\n- Major: either\
    \ replace `nutritional_roles.CARBON_SOURCE` and\n  `nutritional_roles.ENERGY_SOURCE`\
    \ with inspected source evidence for exact\n  generic lactate use, or remove the\
    \ provisional roles.\n- Sync the aggregate copy and regenerate final SSSOM after\
    \ the YAML changes;\n  rerun strict, term, product, component, and SSSOM validation."
- evidence_id: ev-d2b5b81d27a89615
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[843,1386,1541]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"31c51bf1fe574408d0283a89af8923db94f20cdd5405817ad2b35fea8a5f5891","finding_id":"SEM:00b1ac0c24fef647364c","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"31c51bf1fe574408d0283a89af8923db94f20cdd5405817ad2b35fea8a5f5891","finding_id":"SEM:6a709519a173ad04c3cd","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"31c51bf1fe574408d0283a89af8923db94f20cdd5405817ad2b35fea8a5f5891","finding_id":"SEM:c3a17a4e7f66270505a1","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-58f9d42d3330180f
  kind: record_content
  reference: data/ingredients/mapped/Lactate.yaml
  locator: nutritional_roles[0], nutritional_roles[1]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}},{"field":"nutritional_roles[1]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.","reference_text":"Canonical
    energy substrate (catabolised for energy)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"ENERGY_SOURCE"}}]'
  snapshot_sha256: 31c51bf1fe574408d0283a89af8923db94f20cdd5405817ad2b35fea8a5f5891
- evidence_id: ev-54e9d0f70c54c217
  kind: prior_review
  reference: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
  locator: findings[finding_id=f-fcf00281c538a1c1]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-fcf00281c538a1c1 in 20261011T024635Z-mim-reconcile-all-batch-07
  snapshot_sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
assessments:
- assessment_id: a-da7e4b7e613bb719
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-09c27e9da38f0c74
  evidence_ids:
  - ev-2376cc2eeed5c087
  - ev-1115f68d6256301a
  - ev-7c23a5725d4e25eb
  - ev-bc5c532fec415cf7
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-7f59ee03b5acf9ad
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-09c27e9da38f0c74
  evidence_ids:
  - ev-5db3cf590d8514c0
  - ev-35ae159cbc725197
  - ev-2376cc2eeed5c087
  - ev-d2b5b81d27a89615
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:38Z;
    reviewed SHA-256=31c51bf1fe574408d0283a89af8923db94f20cdd5405817ad2b35fea8a5f5891;
    current SHA-256=31c51bf1fe574408d0283a89af8923db94f20cdd5405817ad2b35fea8a5f5891;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050238Z-Lactate.md","reports/yaml_record_review/Lactate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Lactate.md` after the record changed from 473205bc13ea916770dad2ffb219c57d34b1ec2caa5e4ef5a4573443f4043474
    to 31c51bf1fe574408d0283a89af8923db94f20cdd5405817ad2b35fea8a5f5891; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-5db3cf590d8514c0
    - ev-35ae159cbc725197
    - ev-2376cc2eeed5c087
  - name: legacy-native-ids
    value: '["SEM:00b1ac0c24fef647364c","SEM:6a709519a173ad04c3cd","SEM:c3a17a4e7f66270505a1"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-2376cc2eeed5c087
    - ev-5db3cf590d8514c0
    - ev-35ae159cbc725197
    - ev-d2b5b81d27a89615
- assessment_id: a-58f9d42d3330180f
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-09c27e9da38f0c74
  evidence_ids:
  - ev-5db3cf590d8514c0
  - ev-35ae159cbc725197
  - ev-58f9d42d3330180f
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-5db3cf590d8514c0
    - ev-35ae159cbc725197
    - ev-58f9d42d3330180f
findings:
- finding_id: rec-f-fcf00281c538a1c1
  issue_key: mim-reconciliation-role-support-09c27e9da38f0c74
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Lactate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-09c27e9da38f0c74
  evidence_ids:
  - ev-5db3cf590d8514c0
  - ev-35ae159cbc725197
  - ev-58f9d42d3330180f
  - ev-54e9d0f70c54c217
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Lactate.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  - nutritional_roles[1]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024635Z-mim-reconcile-all-batch-07
    finding_id: f-fcf00281c538a1c1
actions:
- action_id: rec-action-fcf00281c538a1c1
  description: 'Reassess prediction-only role support: Lactate'
  finding_ids:
  - rec-f-fcf00281c538a1c1
  target_ids:
  - record-09c27e9da38f0c74
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Lactate.yaml
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
  with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.
```
