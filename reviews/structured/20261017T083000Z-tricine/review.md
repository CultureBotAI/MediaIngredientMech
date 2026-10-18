# Per-record structured review: Tricine (data/ingredients/mapped/Tricine.yaml)

- Review: 20261017T083000Z-tricine
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Tricine (data/ingredients/mapped/Tricine.yaml, record-7f2b801aea8e7a54, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Tricine.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Tricine.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-7f2b801aea8e7a54 | data/ingredients/mapped/Tricine.yaml | maintained | Tricine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-7f2b801aea8e7a54 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-7f2b801aea8e7a54 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-7f2b801aea8e7a54 | Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-7f2b801aea8e7a54.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-7f2b801aea8e7a54.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:03:45Z; reviewed SHA-256=a437294e8d72a87d9e0312005d7c1426fc95cd4af5a885f7724910a26d8c0187; current SHA-256=a437294e8d72a87d9e0312005d7c1426fc95cd4af5a885f7724910a26d8c0187; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050345Z-Tricine.md","reports/yaml_record_review/Tricine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Tricine.md&#96; after the record changed from fcfadeeb55acce26cd71ac7a804ec6f42be4d472fef3f81cb9ca771a8722588c to a437294e8d72a87d9e0312005d7c1426fc95cd4af5a885f7724910a26d8c0187; preserved the previous major finding floor pending targeted retirement.

### Historical provisional-role concern

evidence: concern. Targets: record-7f2b801aea8e7a54.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-ca918864c63e2ac3: Reassess prediction-only role support: Tricine

major / open / confirmed; issue key: mim-reconciliation-role-support-7f2b801aea8e7a54.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-ca918864c63e2ac3

Reassess prediction-only role support: Tricine

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-185e91a3c317c9f8 | data/ingredients/mapped/Tricine.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2677],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:39063","line":2679,"mapping_status":"MAPPED","ontology_id":"CHEBI:39063","preferred_term":"Tricine"}],"identifier":"CHEBI:39063","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":44,"edge_count":44,"occurrences":44},"occurrence_statistics":{"media_count":44,"total_occurrences":44},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:39063","ontology_label":"N-tris(hydroxymethyl)methylglycine","ontology_source":"CHEBI"},"preferred_term":"Tricine","sssom_rows":[{"data_row":2823,"object_id":"CHEBI:39063","object_label":"N-tris(hydroxymethyl)methylglycine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Tricine","synonym_count":0} |
| ev-bc50ffd056505201 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2677] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-7ac4ccfbd56a7133 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Tricine; data-row positions=[2823] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2823,"object_id":"CHEBI:39063","object_label":"N-tris(hydroxymethyl)methylglycine","other":"CAS:5704-04-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Tricine","validation_method":"manual:apply_669_704_rulings&#124;IDENTITY&#124;2026-09-24"}] |
| ev-fa212ce380447376 | docs/data/mapped_ingredients.csv; CSV lines=[2679] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:39063","line":2679,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"44","ontology_id":"CHEBI:39063","preferred_term":"Tricine","total_occurrences":"44"}] |
| ev-0e9cd20230cb1dca | reports/yaml_record_review/20261001T050345Z-Tricine.md; YAML Record Review: Tricine:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-f766f280db381527 | reports/yaml_record_review/Tricine.md; &#96;data/ingredients/mapped/Tricine.yaml&#96;:2; Verdict:4; Identity:10; Validation:22; Evidence:29; Issues:38; Major: &#96;BUFFER&#96; is provisional name-pattern evidence:40; Completeness:56; Recommended Edits:62 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-a2bd1c5cc7da0643 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1306,1990] | context_only | [{"current_record_sha256":"a437294e8d72a87d9e0312005d7c1426fc95cd4af5a885f7724910a26d8c0187","finding_id":"SEM:03e6b59c36007b80eda7","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"a437294e8d72a87d9e0312005d7c1426fc95cd4af5a885f7724910a26d8c0187","finding_id":"SEM:45145f975f47c92be184","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-2b475514d073b967 | data/ingredients/mapped/Tricine.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2677],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:39063","line":2679,"mapping_status":"MAPPED","ontology_id":"CHEBI:39063","preferred_term":"Tricine"}],"identifier":"CHEBI:39063","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":44,"edge_count":44,"occurrences":44},"occurrence_statistics":{"media_count":44,"total_occurrences":44},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:39063","ontology_label":"N-tris(hydroxymethyl)methylglycine","ontology_source":"CHEBI"},"preferred_term":"Tricine","sssom_rows":[{"data_row":2823,"object_id":"CHEBI:39063","object_label":"N-tris(hydroxymethyl)methylglycine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Tricine","synonym_count":0} |
| ev-c210ac40ebbb1b8c | reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml; findings[finding_id=f-ca918864c63e2ac3] | context_only | Predecessor structured review finding f-ca918864c63e2ac3 in 20261011T024639Z-mim-reconcile-all-batch-12 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.

## Complete Structured Record

The sibling review.yaml is authoritative.

````yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-tricine
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Tricine (data/ingredients/mapped/Tricine.yaml)'
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
summary: Per-record structured review for Tricine (data/ingredients/mapped/Tricine.yaml,
  record-7f2b801aea8e7a54, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Tricine.yaml
    sha256: a437294e8d72a87d9e0312005d7c1426fc95cd4af5a885f7724910a26d8c0187
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
  - path: reports/yaml_record_review/20261001T050345Z-Tricine.md
    sha256: 304b83dbf423f0a6b9f96c63835251abd189388c920e6fed9d4f427bacaafd1c
    role: context
  - path: reports/yaml_record_review/Tricine.md
    sha256: bae7e91522e79c56e70c7100e770af78d7ec639f6f1f4822bf87fdb766d8f8f8
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-7f2b801aea8e7a54
  path: data/ingredients/mapped/Tricine.yaml
  label: Tricine
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Tricine.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Tricine.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Tricine.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-7f2b801aea8e7a54
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-7f2b801aea8e7a54
  evidence_ids:
  - ev-185e91a3c317c9f8
  - ev-bc50ffd056505201
  - ev-7ac4ccfbd56a7133
  - ev-fa212ce380447376
  - ev-2b475514d073b967
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-7f2b801aea8e7a54
  evidence_ids:
  - ev-185e91a3c317c9f8
  - ev-a2bd1c5cc7da0643
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12
    and semantic review dispositions on HEAD.
  target_ids:
  - record-7f2b801aea8e7a54
  evidence_ids:
  - ev-0e9cd20230cb1dca
  - ev-f766f280db381527
  - ev-a2bd1c5cc7da0643
  - ev-c210ac40ebbb1b8c
evidence:
- evidence_id: ev-185e91a3c317c9f8
  kind: record_content
  reference: data/ingredients/mapped/Tricine.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2677],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:39063","line":2679,"mapping_status":"MAPPED","ontology_id":"CHEBI:39063","preferred_term":"Tricine"}],"identifier":"CHEBI:39063","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":44,"edge_count":44,"occurrences":44},"occurrence_statistics":{"media_count":44,"total_occurrences":44},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:39063","ontology_label":"N-tris(hydroxymethyl)methylglycine","ontology_source":"CHEBI"},"preferred_term":"Tricine","sssom_rows":[{"data_row":2823,"object_id":"CHEBI:39063","object_label":"N-tris(hydroxymethyl)methylglycine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Tricine","synonym_count":0}'
  snapshot_sha256: a437294e8d72a87d9e0312005d7c1426fc95cd4af5a885f7724910a26d8c0187
- evidence_id: ev-bc50ffd056505201
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2677]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-7ac4ccfbd56a7133
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Tricine; data-row positions=[2823]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2823,"object_id":"CHEBI:39063","object_label":"N-tris(hydroxymethyl)methylglycine","other":"CAS:5704-04-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Tricine","validation_method":"manual:apply_669_704_rulings|IDENTITY|2026-09-24"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-fa212ce380447376
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2679]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:39063","line":2679,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"44","ontology_id":"CHEBI:39063","preferred_term":"Tricine","total_occurrences":"44"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-0e9cd20230cb1dca
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050345Z-Tricine.md
  locator: 'YAML Record Review: Tricine:2; Target:10; Validation:20; Identity and
    Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 304b83dbf423f0a6b9f96c63835251abd189388c920e6fed9d4f427bacaafd1c
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/Tricine.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The exact
    CHEBI identity and final SSSOM row pass, but BUFFER is provisional name-pattern
    evidence.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Tricine.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Tricine.yaml`,
    `just validate-terms data/ingredients/mapped/Tricine.yaml` where applicable, and
    `just qc-sssom`.'
- evidence_id: ev-f766f280db381527
  kind: prior_review
  reference: reports/yaml_record_review/Tricine.md
  locator: '`data/ingredients/mapped/Tricine.yaml`:2; Verdict:4; Identity:10; Validation:22;
    Evidence:29; Issues:38; Major: `BUFFER` is provisional name-pattern evidence:40;
    Completeness:56; Recommended Edits:62'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: bae7e91522e79c56e70c7100e770af78d7ec639f6f1f4822bf87fdb766d8f8f8
  quote: "Issues:\n\n\nMajor: `BUFFER` is provisional name-pattern evidence:\nThe\
    \ only role assertion is:\n\n```yaml\nphysicochemical_roles:\n- role: BUFFER\n\
    \  confidence: 0.8\n  evidence:\n  - reference_type: COMPUTATIONAL_PREDICTION\n\
    \    reference_text: Inferred from curated media-role name pattern\n    curator_note:\
    \ Provisional role from a curated name-pattern rule; review recommended.\n```\n\
    \nThe exact CHEBI and CAS identity do not independently curate the buffer role.\n\
    \nRecommended Edits:\n- Replace the `COMPUTATIONAL_PREDICTION` role evidence with\
    \ curated\n  database/literature evidence, or remove `physicochemical_roles` until\
    \ such\n  support is added."
- evidence_id: ev-a2bd1c5cc7da0643
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1306,1990]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"a437294e8d72a87d9e0312005d7c1426fc95cd4af5a885f7724910a26d8c0187","finding_id":"SEM:03e6b59c36007b80eda7","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"a437294e8d72a87d9e0312005d7c1426fc95cd4af5a885f7724910a26d8c0187","finding_id":"SEM:45145f975f47c92be184","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-2b475514d073b967
  kind: record_content
  reference: data/ingredients/mapped/Tricine.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2677],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:39063","line":2679,"mapping_status":"MAPPED","ontology_id":"CHEBI:39063","preferred_term":"Tricine"}],"identifier":"CHEBI:39063","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":44,"edge_count":44,"occurrences":44},"occurrence_statistics":{"media_count":44,"total_occurrences":44},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:39063","ontology_label":"N-tris(hydroxymethyl)methylglycine","ontology_source":"CHEBI"},"preferred_term":"Tricine","sssom_rows":[{"data_row":2823,"object_id":"CHEBI:39063","object_label":"N-tris(hydroxymethyl)methylglycine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Tricine","synonym_count":0}'
  snapshot_sha256: a437294e8d72a87d9e0312005d7c1426fc95cd4af5a885f7724910a26d8c0187
- evidence_id: ev-c210ac40ebbb1b8c
  kind: prior_review
  reference: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
  locator: findings[finding_id=f-ca918864c63e2ac3]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-ca918864c63e2ac3 in 20261011T024639Z-mim-reconcile-all-batch-12
  snapshot_sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
assessments:
- assessment_id: a-8e39356945a9d164
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-7f2b801aea8e7a54
  evidence_ids:
  - ev-185e91a3c317c9f8
  - ev-bc50ffd056505201
  - ev-7ac4ccfbd56a7133
  - ev-fa212ce380447376
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-58f6a9cdc914c900
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-7f2b801aea8e7a54
  evidence_ids:
  - ev-0e9cd20230cb1dca
  - ev-f766f280db381527
  - ev-185e91a3c317c9f8
  - ev-a2bd1c5cc7da0643
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:03:45Z;
    reviewed SHA-256=a437294e8d72a87d9e0312005d7c1426fc95cd4af5a885f7724910a26d8c0187;
    current SHA-256=a437294e8d72a87d9e0312005d7c1426fc95cd4af5a885f7724910a26d8c0187;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050345Z-Tricine.md","reports/yaml_record_review/Tricine.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Tricine.md` after the record changed from fcfadeeb55acce26cd71ac7a804ec6f42be4d472fef3f81cb9ca771a8722588c
    to a437294e8d72a87d9e0312005d7c1426fc95cd4af5a885f7724910a26d8c0187; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0e9cd20230cb1dca
    - ev-f766f280db381527
    - ev-185e91a3c317c9f8
  - name: legacy-native-ids
    value: '["SEM:03e6b59c36007b80eda7","SEM:45145f975f47c92be184"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-185e91a3c317c9f8
    - ev-0e9cd20230cb1dca
    - ev-f766f280db381527
    - ev-a2bd1c5cc7da0643
- assessment_id: a-2b475514d073b967
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-7f2b801aea8e7a54
  evidence_ids:
  - ev-0e9cd20230cb1dca
  - ev-f766f280db381527
  - ev-2b475514d073b967
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0e9cd20230cb1dca
    - ev-f766f280db381527
    - ev-2b475514d073b967
findings:
- finding_id: rec-f-ca918864c63e2ac3
  issue_key: mim-reconciliation-role-support-7f2b801aea8e7a54
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Tricine'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-7f2b801aea8e7a54
  evidence_ids:
  - ev-0e9cd20230cb1dca
  - ev-f766f280db381527
  - ev-2b475514d073b967
  - ev-c210ac40ebbb1b8c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Tricine.yaml
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
    finding_id: f-ca918864c63e2ac3
actions:
- action_id: rec-action-ca918864c63e2ac3
  description: 'Reassess prediction-only role support: Tricine'
  finding_ids:
  - rec-f-ca918864c63e2ac3
  target_ids:
  - record-7f2b801aea8e7a54
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Tricine.yaml
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
