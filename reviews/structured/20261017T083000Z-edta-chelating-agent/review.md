# Per-record structured review: Edta_Chelating_Agent (data/ingredients/mapped/Edta_Chelating_Agent.yaml)

- Review: 20261017T083000Z-edta-chelating-agent
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Edta_Chelating_Agent (data/ingredients/mapped/Edta_Chelating_Agent.yaml, record-02b5116af3e070ea, mapping_status=REJECTED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Edta_Chelating_Agent.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Edta_Chelating_Agent.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-02b5116af3e070ea | data/ingredients/mapped/Edta_Chelating_Agent.yaml | maintained | Edta_Chelating_Agent |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-02b5116af3e070ea | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-02b5116af3e070ea | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-02b5116af3e070ea | Reconciled against predecessor batch review 20261011T024629Z-mim-reconcile-all-batch-01 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-02b5116af3e070ea.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-02b5116af3e070ea.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=blocker; reviewed_at=2026-10-01T05:02:12Z; reviewed SHA-256=85c00a1b83b9f31e8bd04b3ee56ee4b487aab3c0e18a5c0302b46b04bfee175f; current SHA-256=8b17c831323de52c442e5af106f7b765486791f5275b8716eefde43d6a32b63c; hash_changed=True. Reports=["reports/yaml_record_review/20261001T050212Z-Edta_Chelating_Agent.md","reports/yaml_record_review/Edta_Chelating_Agent.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Edta_Chelating_Agent.md&#96; after the record changed from 7fe6440002acca66be63af7bccb2a4e1c955511e5da0b044de2238097004d1c0 to 85c00a1b83b9f31e8bd04b3ee56ee4b487aab3c0e18a5c0302b46b04bfee175f; preserved the previous blocker finding floor pending targeted retirement.

### Historical provisional-role concern

evidence: unknown. Targets: record-02b5116af3e070ea.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

### Retired wrong mapping / stale tombstone ontology pointer

identity: supported. Targets: record-02b5116af3e070ea.

The narrow exported-mapping/pointer defect is already fixed: REJECTED tombstone, no own-subject SSSOM rows, identifier and ontology_id agree with a live merge target. This does not retire source-count, inert chemistry, role, or synonym questions.

## Findings

### rec-f-0a3fe0fd2ddc2251: Reassess prediction-only role support: EDTA (chelating agent)

minor / deferred / provisional; issue key: mim-reconciliation-role-support-02b5116af3e070ea.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

Disposition: The current local observation is recorded, but the named source/context or policy decision is still required; no correction is inferred.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-d8b7463cace0005c | data/ingredients/mapped/Edta_Chelating_Agent.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[933],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:4735","line":935,"mapping_status":"REJECTED","ontology_id":"CHEBI:4735","preferred_term":"EDTA (chelating agent)"}],"identifier":"CHEBI:4735","ingredient_type":null,"mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":568,"edge_count":568,"occurrences":569},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"LEXICAL_MATCH","ontology_id":"CHEBI:4735","ontology_label":"ethylenediaminetetraacetic acid","ontology_source":"CHEBI"},"preferred_term":"EDTA (chelating agent)","sssom_rows":[],"sssom_subject":"MIM:Edta_Chelating_Agent","synonym_count":1} |
| ev-44a5c78d0518be20 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [933] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-6ee4d9e56424706c | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Edta_Chelating_Agent; data-row positions=[] | context_only | Current exact-subject rows, including complete other payload: [] |
| ev-132825111efec404 | docs/data/mapped_ingredients.csv; CSV lines=[935] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:4735","line":935,"mapping_quality":"LEXICAL_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:4735","preferred_term":"EDTA (chelating agent)","total_occurrences":"0"}] |
| ev-ccb73004ba17130c | reports/yaml_record_review/20261001T050212Z-Edta_Chelating_Agent.md; YAML Record Review: EDTA (chelating agent):2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-1d6b1f3ca5e20f64 | reports/yaml_record_review/Edta_Chelating_Agent.md; &#96;data/ingredients/mapped/Edta_Chelating_Agent.yaml&#96;:2; Verdict:4; Identity:10; Validation:22; Evidence:29; Completeness:53; Recommended Edits:58 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-257c9ccf0fbcf212 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[566,1605] | context_only | [{"current_record_sha256":"8b17c831323de52c442e5af106f7b765486791f5275b8716eefde43d6a32b63c","finding_id":"SEM:22c6c53bc502552aed6a","kind":"existing_record_review","resolution_reason":"Source record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"},{"current_record_sha256":"8b17c831323de52c442e5af106f7b765486791f5275b8716eefde43d6a32b63c","finding_id":"SEM:582204b4bd6dffb6e882","kind":"role_evidence","resolution_reason":"Source record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}] |
| ev-5b1c4b3ce76d038e | data/ingredients/mapped/Edta_Chelating_Agent.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[933],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:4735","line":935,"mapping_status":"REJECTED","ontology_id":"CHEBI:4735","preferred_term":"EDTA (chelating agent)"}],"identifier":"CHEBI:4735","ingredient_type":null,"mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":568,"edge_count":568,"occurrences":569},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"LEXICAL_MATCH","ontology_id":"CHEBI:4735","ontology_label":"ethylenediaminetetraacetic acid","ontology_source":"CHEBI"},"preferred_term":"EDTA (chelating agent)","sssom_rows":[],"sssom_subject":"MIM:Edta_Chelating_Agent","synonym_count":1} |
| ev-2fea0ca12c76ecd5 | data/ingredients/mapped/Edta_Chelating_Agent.yaml; identifier; ontology_mapping.ontology_id; mapping_status; curation_history | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[933],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:4735","line":935,"mapping_status":"REJECTED","ontology_id":"CHEBI:4735","preferred_term":"EDTA (chelating agent)"}],"identifier":"CHEBI:4735","ingredient_type":null,"mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":568,"edge_count":568,"occurrences":569},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"LEXICAL_MATCH","ontology_id":"CHEBI:4735","ontology_label":"ethylenediaminetetraacetic acid","ontology_source":"CHEBI"},"preferred_term":"EDTA (chelating agent)","sssom_rows":[],"sssom_subject":"MIM:Edta_Chelating_Agent","synonym_count":1} |
| ev-bf4fe264a1fa19cf | reviews/structured/20261011T024629Z-mim-reconcile-all-batch-01/review.yaml; findings[finding_id=f-0a3fe0fd2ddc2251] | context_only | Predecessor structured review finding f-0a3fe0fd2ddc2251 in 20261011T024629Z-mim-reconcile-all-batch-01 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024629Z-mim-reconcile-all-batch-01.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-edta-chelating-agent
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Edta_Chelating_Agent (data/ingredients/mapped/Edta_Chelating_Agent.yaml)'
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
native_verdict: mapping_status=REJECTED; open=0; deferred=1
scientific_review: false
summary: Per-record structured review for Edta_Chelating_Agent (data/ingredients/mapped/Edta_Chelating_Agent.yaml,
  record-02b5116af3e070ea, mapping_status=REJECTED). Records 0 open finding(s) and
  1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Edta_Chelating_Agent.yaml
    sha256: 8b17c831323de52c442e5af106f7b765486791f5275b8716eefde43d6a32b63c
    role: target
  - path: reviews/structured/20261011T024629Z-mim-reconcile-all-batch-01/review.yaml
    sha256: f87124785da2057286555db743ccdb92b70dd4dc359294bde474b4beeb816e48
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
  - path: reports/yaml_record_review/20261001T050212Z-Edta_Chelating_Agent.md
    sha256: 9baf3ca7214206c8e5a364124da0647ea1116dc73a744f1911200853840106cc
    role: context
  - path: reports/yaml_record_review/Edta_Chelating_Agent.md
    sha256: 5209fa2e6972b471654833d8384545752d3b5dd6f2f0f284fb22c3fc9b0f8ba7
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-02b5116af3e070ea
  path: data/ingredients/mapped/Edta_Chelating_Agent.yaml
  label: Edta_Chelating_Agent
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Edta_Chelating_Agent.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Edta_Chelating_Agent.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Edta_Chelating_Agent.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-02b5116af3e070ea
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-02b5116af3e070ea
  evidence_ids:
  - ev-d8b7463cace0005c
  - ev-44a5c78d0518be20
  - ev-6ee4d9e56424706c
  - ev-132825111efec404
  - ev-5b1c4b3ce76d038e
  - ev-2fea0ca12c76ecd5
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-02b5116af3e070ea
  evidence_ids:
  - ev-d8b7463cace0005c
  - ev-257c9ccf0fbcf212
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024629Z-mim-reconcile-all-batch-01
    and semantic review dispositions on HEAD.
  target_ids:
  - record-02b5116af3e070ea
  evidence_ids:
  - ev-ccb73004ba17130c
  - ev-1d6b1f3ca5e20f64
  - ev-257c9ccf0fbcf212
  - ev-bf4fe264a1fa19cf
evidence:
- evidence_id: ev-d8b7463cace0005c
  kind: record_content
  reference: data/ingredients/mapped/Edta_Chelating_Agent.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[933],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:4735","line":935,"mapping_status":"REJECTED","ontology_id":"CHEBI:4735","preferred_term":"EDTA
    (chelating agent)"}],"identifier":"CHEBI:4735","ingredient_type":null,"mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":568,"edge_count":568,"occurrences":569},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"LEXICAL_MATCH","ontology_id":"CHEBI:4735","ontology_label":"ethylenediaminetetraacetic
    acid","ontology_source":"CHEBI"},"preferred_term":"EDTA (chelating agent)","sssom_rows":[],"sssom_subject":"MIM:Edta_Chelating_Agent","synonym_count":1}'
  snapshot_sha256: 8b17c831323de52c442e5af106f7b765486791f5275b8716eefde43d6a32b63c
- evidence_id: ev-44a5c78d0518be20
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [933]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-6ee4d9e56424706c
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Edta_Chelating_Agent; data-row positions=[]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: []'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-132825111efec404
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[935]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:4735","line":935,"mapping_quality":"LEXICAL_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:4735","preferred_term":"EDTA
    (chelating agent)","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-ccb73004ba17130c
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050212Z-Edta_Chelating_Agent.md
  locator: 'YAML Record Review: EDTA (chelating agent):2; Target:10; Validation:20;
    Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended
    Edits:56; Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 9baf3ca7214206c8e5a364124da0647ea1116dc73a744f1911200853840106cc
  quote: 'Findings:

    - **blocker**: The previous finding set in `reports/yaml_record_review/Edta_Chelating_Agent.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The record
    exact-maps an EDTA-specific label to generic NCIT:C360 Chelating Agent.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Edta_Chelating_Agent.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Edta_Chelating_Agent.yaml`,
    `just validate-terms data/ingredients/mapped/Edta_Chelating_Agent.yaml` where
    applicable, and `just qc-sssom`.'
- evidence_id: ev-1d6b1f3ca5e20f64
  kind: prior_review
  reference: reports/yaml_record_review/Edta_Chelating_Agent.md
  locator: '`data/ingredients/mapped/Edta_Chelating_Agent.yaml`:2; Verdict:4; Identity:10;
    Validation:22; Evidence:29; Completeness:53; Recommended Edits:58'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 5209fa2e6972b471654833d8384545752d3b5dd6f2f0f284fb22c3fc9b0f8ba7
  quote: "Recommended Edits:\n- Blocker: tombstone `data/ingredients/mapped/Edta_Chelating_Agent.yaml`\
    \ as a\n  zero-occurrence duplicate or reground it to `CHEBI:4735` if the\n  `communitymech-unmapped`\
    \ provenance must be preserved; either way, stop\n  exporting `MIM:Edta_Chelating_Agent\
    \ skos:exactMatch NCIT:C360`.\n- Major: remove the provisional `CHELATOR` role\
    \ when tombstoning or regrounding\n  the record unless claim-level evidence is\
    \ curated.\n- After editing the per-record YAML, run `sync-curated`, rebuild or\
    \ reconcile\n  SSSOM, and rerun `validate-all`, `qc-sssom`, strict validation,\
    \ and id-label\n  correspondence."
- evidence_id: ev-257c9ccf0fbcf212
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[566,1605]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"8b17c831323de52c442e5af106f7b765486791f5275b8716eefde43d6a32b63c","finding_id":"SEM:22c6c53bc502552aed6a","kind":"existing_record_review","resolution_reason":"Source
    record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"},{"current_record_sha256":"8b17c831323de52c442e5af106f7b765486791f5275b8716eefde43d6a32b63c","finding_id":"SEM:582204b4bd6dffb6e882","kind":"role_evidence","resolution_reason":"Source
    record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-5b1c4b3ce76d038e
  kind: record_content
  reference: data/ingredients/mapped/Edta_Chelating_Agent.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[933],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:4735","line":935,"mapping_status":"REJECTED","ontology_id":"CHEBI:4735","preferred_term":"EDTA
    (chelating agent)"}],"identifier":"CHEBI:4735","ingredient_type":null,"mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":568,"edge_count":568,"occurrences":569},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"LEXICAL_MATCH","ontology_id":"CHEBI:4735","ontology_label":"ethylenediaminetetraacetic
    acid","ontology_source":"CHEBI"},"preferred_term":"EDTA (chelating agent)","sssom_rows":[],"sssom_subject":"MIM:Edta_Chelating_Agent","synonym_count":1}'
  snapshot_sha256: 8b17c831323de52c442e5af106f7b765486791f5275b8716eefde43d6a32b63c
- evidence_id: ev-2fea0ca12c76ecd5
  kind: record_content
  reference: data/ingredients/mapped/Edta_Chelating_Agent.yaml
  locator: identifier; ontology_mapping.ontology_id; mapping_status; curation_history
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[933],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:4735","line":935,"mapping_status":"REJECTED","ontology_id":"CHEBI:4735","preferred_term":"EDTA
    (chelating agent)"}],"identifier":"CHEBI:4735","ingredient_type":null,"mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":568,"edge_count":568,"occurrences":569},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"LEXICAL_MATCH","ontology_id":"CHEBI:4735","ontology_label":"ethylenediaminetetraacetic
    acid","ontology_source":"CHEBI"},"preferred_term":"EDTA (chelating agent)","sssom_rows":[],"sssom_subject":"MIM:Edta_Chelating_Agent","synonym_count":1}'
  snapshot_sha256: 8b17c831323de52c442e5af106f7b765486791f5275b8716eefde43d6a32b63c
- evidence_id: ev-bf4fe264a1fa19cf
  kind: prior_review
  reference: reviews/structured/20261011T024629Z-mim-reconcile-all-batch-01/review.yaml
  locator: findings[finding_id=f-0a3fe0fd2ddc2251]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-0a3fe0fd2ddc2251 in 20261011T024629Z-mim-reconcile-all-batch-01
  snapshot_sha256: f87124785da2057286555db743ccdb92b70dd4dc359294bde474b4beeb816e48
assessments:
- assessment_id: a-51b7c1a90fbe4b2f
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-02b5116af3e070ea
  evidence_ids:
  - ev-d8b7463cace0005c
  - ev-44a5c78d0518be20
  - ev-6ee4d9e56424706c
  - ev-132825111efec404
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-8a0f9d3269944733
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-02b5116af3e070ea
  evidence_ids:
  - ev-ccb73004ba17130c
  - ev-1d6b1f3ca5e20f64
  - ev-d8b7463cace0005c
  - ev-257c9ccf0fbcf212
  details: 'Latest manifest verdict=needs_curation; severity=blocker; reviewed_at=2026-10-01T05:02:12Z;
    reviewed SHA-256=85c00a1b83b9f31e8bd04b3ee56ee4b487aab3c0e18a5c0302b46b04bfee175f;
    current SHA-256=8b17c831323de52c442e5af106f7b765486791f5275b8716eefde43d6a32b63c;
    hash_changed=True. Reports=["reports/yaml_record_review/20261001T050212Z-Edta_Chelating_Agent.md","reports/yaml_record_review/Edta_Chelating_Agent.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Edta_Chelating_Agent.md` after the record changed
    from 7fe6440002acca66be63af7bccb2a4e1c955511e5da0b044de2238097004d1c0 to 85c00a1b83b9f31e8bd04b3ee56ee4b487aab3c0e18a5c0302b46b04bfee175f;
    preserved the previous blocker finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ccb73004ba17130c
    - ev-1d6b1f3ca5e20f64
    - ev-d8b7463cace0005c
  - name: legacy-native-ids
    value: '["SEM:22c6c53bc502552aed6a","SEM:582204b4bd6dffb6e882"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-d8b7463cace0005c
    - ev-ccb73004ba17130c
    - ev-1d6b1f3ca5e20f64
    - ev-257c9ccf0fbcf212
- assessment_id: a-5b1c4b3ce76d038e
  area: evidence
  topic: Historical provisional-role concern
  outcome: unknown
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-02b5116af3e070ea
  evidence_ids:
  - ev-ccb73004ba17130c
  - ev-1d6b1f3ca5e20f64
  - ev-5b1c4b3ce76d038e
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ccb73004ba17130c
    - ev-1d6b1f3ca5e20f64
    - ev-5b1c4b3ce76d038e
- assessment_id: a-a4adc8971c74c795
  area: identity
  topic: Retired wrong mapping / stale tombstone ontology pointer
  outcome: supported
  summary: 'The narrow exported-mapping/pointer defect is already fixed: REJECTED
    tombstone, no own-subject SSSOM rows, identifier and ontology_id agree with a
    live merge target. This does not retire source-count, inert chemistry, role, or
    synonym questions.'
  target_ids:
  - record-02b5116af3e070ea
  evidence_ids:
  - ev-ccb73004ba17130c
  - ev-1d6b1f3ca5e20f64
  - ev-2fea0ca12c76ecd5
  - ev-d8b7463cace0005c
  dimensions:
  - name: legacy-disposition
    value: already_fixed
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ccb73004ba17130c
    - ev-1d6b1f3ca5e20f64
    - ev-2fea0ca12c76ecd5
    - ev-d8b7463cace0005c
findings:
- finding_id: rec-f-0a3fe0fd2ddc2251
  issue_key: mim-reconciliation-role-support-02b5116af3e070ea
  category: evidence
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Reassess prediction-only role support: EDTA (chelating agent)'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-02b5116af3e070ea
  evidence_ids:
  - ev-ccb73004ba17130c
  - ev-1d6b1f3ca5e20f64
  - ev-5b1c4b3ce76d038e
  - ev-bf4fe264a1fa19cf
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Edta_Chelating_Agent.yaml
    role: maintained ingredient
  field_paths:
  - physicochemical_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  disposition_reason: The current local observation is recorded, but the named source/context
    or policy decision is still required; no correction is inferred.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024629Z-mim-reconcile-all-batch-01
    finding_id: f-0a3fe0fd2ddc2251
actions: []
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
  with lineage to 20261011T024629Z-mim-reconcile-all-batch-01.
```
