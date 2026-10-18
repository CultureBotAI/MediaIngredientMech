# Per-record structured review: Na2-edta_X_2_H2o (data/ingredients/mapped/Na2-edta_X_2_H2o.yaml)

- Review: 20261017T083000Z-na2-edta-x-2-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Na2-edta_X_2_H2o (data/ingredients/mapped/Na2-edta_X_2_H2o.yaml, record-9b40e28e8fe3ad48, mapping_status=REJECTED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Na2-edta_X_2_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Na2-edta_X_2_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-9b40e28e8fe3ad48 | data/ingredients/mapped/Na2-edta_X_2_H2o.yaml | maintained | Na2-edta_X_2_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-9b40e28e8fe3ad48 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-9b40e28e8fe3ad48 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-9b40e28e8fe3ad48 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-9b40e28e8fe3ad48.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-9b40e28e8fe3ad48.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-10-01T05:02:50Z; reviewed SHA-256=9f02a335a6dfebf13a162ed0d697ec16f4d584a5a4af55dfdba7aa7f26d24670; current SHA-256=9f02a335a6dfebf13a162ed0d697ec16f4d584a5a4af55dfdba7aa7f26d24670; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050250Z-Na2-edta_X_2_H2o.md","reports/yaml_record_review/Na2-edta_X_2_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Na2-edta_X_2_H2o.md&#96; after the record changed from 75ed775eb108925f06cb86d2d136daf16bfca48452002d5599e8594adfb06c10 to 9f02a335a6dfebf13a162ed0d697ec16f4d584a5a4af55dfdba7aa7f26d24670; preserved the previous minor finding floor pending targeted retirement.

### Historical provisional-role concern

evidence: unknown. Targets: record-9b40e28e8fe3ad48.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-299959d93cd9bbd6: Reassess prediction-only role support: Na2-EDTA x 2 H2O

minor / deferred / provisional; issue key: mim-reconciliation-role-support-9b40e28e8fe3ad48.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

Disposition: The current local observation is recorded, but the named source/context or policy decision is still required; no correction is inferred.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-4073bb1838002263 | data/ingredients/mapped/Na2-edta_X_2_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1478],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:64758","line":1480,"mapping_status":"REJECTED","ontology_id":"CHEBI:64758","preferred_term":"Na2-EDTA x 2 H2O"}],"identifier":"CHEBI:64758","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":139,"edge_count":139,"occurrences":140},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:64758","ontology_label":"EDTA disodium salt dihydrate","ontology_source":"CHEBI"},"preferred_term":"Na2-EDTA x 2 H2O","sssom_rows":[],"sssom_subject":"MIM:Na2-edta_X_2_H2o","synonym_count":9} |
| ev-02ec9af1bcfc9813 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1478] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-b8162ce3cb322201 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Na2-edta_X_2_H2o; data-row positions=[] | context_only | Current exact-subject rows, including complete other payload: [] |
| ev-41fa9675a7893c1f | docs/data/mapped_ingredients.csv; CSV lines=[1480] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:64758","line":1480,"mapping_quality":"NARROW_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:64758","preferred_term":"Na2-EDTA x 2 H2O","total_occurrences":"0"}] |
| ev-85f9b8933372b9e0 | reports/yaml_record_review/20261001T050250Z-Na2-edta_X_2_H2o.md; YAML Record Review: Na2-EDTA x 2 H2O:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-068af2cfb7d21511 | reports/yaml_record_review/Na2-edta_X_2_H2o.md; &#96;data/ingredients/mapped/Na2-edta_X_2_H2o.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:29; Completeness:45; Recommended Edits:53 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-c295452482ffc128 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[986] | context_only | [{"current_record_sha256":"9f02a335a6dfebf13a162ed0d697ec16f4d584a5a4af55dfdba7aa7f26d24670","finding_id":"SEM:3bfdd2771d2bd1571f51","kind":"existing_record_review","resolution_reason":"Source record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}] |
| ev-4f79f0e35977e3c2 | data/ingredients/mapped/Na2-edta_X_2_H2o.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1478],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:64758","line":1480,"mapping_status":"REJECTED","ontology_id":"CHEBI:64758","preferred_term":"Na2-EDTA x 2 H2O"}],"identifier":"CHEBI:64758","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":139,"edge_count":139,"occurrences":140},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:64758","ontology_label":"EDTA disodium salt dihydrate","ontology_source":"CHEBI"},"preferred_term":"Na2-EDTA x 2 H2O","sssom_rows":[],"sssom_subject":"MIM:Na2-edta_X_2_H2o","synonym_count":9} |
| ev-a82e93bade2bed4d | reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml; findings[finding_id=f-299959d93cd9bbd6] | context_only | Predecessor structured review finding f-299959d93cd9bbd6 in 20261011T024637Z-mim-reconcile-all-batch-09 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-na2-edta-x-2-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Na2-edta_X_2_H2o (data/ingredients/mapped/Na2-edta_X_2_H2o.yaml)'
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
summary: Per-record structured review for Na2-edta_X_2_H2o (data/ingredients/mapped/Na2-edta_X_2_H2o.yaml,
  record-9b40e28e8fe3ad48, mapping_status=REJECTED). Records 0 open finding(s) and
  1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Na2-edta_X_2_H2o.yaml
    sha256: 9f02a335a6dfebf13a162ed0d697ec16f4d584a5a4af55dfdba7aa7f26d24670
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
  - path: reports/yaml_record_review/20261001T050250Z-Na2-edta_X_2_H2o.md
    sha256: 951d21f2e876ce03128b94e4aab22b56a7a6afcf8d706ef507625affcbcc5ea8
    role: context
  - path: reports/yaml_record_review/Na2-edta_X_2_H2o.md
    sha256: e9a3555f005db94c0ded33823e2a4e1ed6296d9291928f68bc7b722b574859ee
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-9b40e28e8fe3ad48
  path: data/ingredients/mapped/Na2-edta_X_2_H2o.yaml
  label: Na2-edta_X_2_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2-edta_X_2_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Na2-edta_X_2_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Na2-edta_X_2_H2o.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-9b40e28e8fe3ad48
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-9b40e28e8fe3ad48
  evidence_ids:
  - ev-4073bb1838002263
  - ev-02ec9af1bcfc9813
  - ev-b8162ce3cb322201
  - ev-41fa9675a7893c1f
  - ev-4f79f0e35977e3c2
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-9b40e28e8fe3ad48
  evidence_ids:
  - ev-4073bb1838002263
  - ev-c295452482ffc128
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-9b40e28e8fe3ad48
  evidence_ids:
  - ev-85f9b8933372b9e0
  - ev-068af2cfb7d21511
  - ev-c295452482ffc128
  - ev-a82e93bade2bed4d
evidence:
- evidence_id: ev-4073bb1838002263
  kind: record_content
  reference: data/ingredients/mapped/Na2-edta_X_2_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1478],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:64758","line":1480,"mapping_status":"REJECTED","ontology_id":"CHEBI:64758","preferred_term":"Na2-EDTA
    x 2 H2O"}],"identifier":"CHEBI:64758","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":139,"edge_count":139,"occurrences":140},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:64758","ontology_label":"EDTA
    disodium salt dihydrate","ontology_source":"CHEBI"},"preferred_term":"Na2-EDTA
    x 2 H2O","sssom_rows":[],"sssom_subject":"MIM:Na2-edta_X_2_H2o","synonym_count":9}'
  snapshot_sha256: 9f02a335a6dfebf13a162ed0d697ec16f4d584a5a4af55dfdba7aa7f26d24670
- evidence_id: ev-02ec9af1bcfc9813
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1478]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-b8162ce3cb322201
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Na2-edta_X_2_H2o; data-row positions=[]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: []'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-41fa9675a7893c1f
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1480]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:64758","line":1480,"mapping_quality":"NARROW_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:64758","preferred_term":"Na2-EDTA
    x 2 H2O","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-85f9b8933372b9e0
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050250Z-Na2-edta_X_2_H2o.md
  locator: 'YAML Record Review: Na2-EDTA x 2 H2O:2; Target:10; Validation:20; Identity
    and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 951d21f2e876ce03128b94e4aab22b56a7a6afcf8d706ef507625affcbcc5ea8
  quote: 'Findings:

    - **minor**: The previous finding set in `reports/yaml_record_review/Na2-edta_X_2_H2o.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The rejected
    Na2-EDTA dihydrate tombstone correctly emits no final SSSOM row and defers to
    Na2EDTA dihydrate, but still carries stale pre-merge fields.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Na2-edta_X_2_H2o.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Na2-edta_X_2_H2o.yaml`,
    `just validate-terms data/ingredients/mapped/Na2-edta_X_2_H2o.yaml` where applicable,
    and `just qc-sssom`.'
- evidence_id: ev-068af2cfb7d21511
  kind: prior_review
  reference: reports/yaml_record_review/Na2-edta_X_2_H2o.md
  locator: '`data/ingredients/mapped/Na2-edta_X_2_H2o.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:29; Completeness:45; Recommended Edits:53'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: e9a3555f005db94c0ded33823e2a4e1ed6296d9291928f68bc7b722b574859ee
  quote: "Recommended Edits:\n- Minor: optionally clean the stale pre-merge chemical,\
    \ synonym, and `CHELATOR`\n  fields from `data/ingredients/mapped/Na2-edta_X_2_H2o.yaml`\
    \ while preserving\n  the curation history that explains the rejected tombstone.\
    \ Rerun strict\n  validation and final SSSOM validation afterward to confirm the\
    \ tombstone\n  remains unpublished."
- evidence_id: ev-c295452482ffc128
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[986]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"9f02a335a6dfebf13a162ed0d697ec16f4d584a5a4af55dfdba7aa7f26d24670","finding_id":"SEM:3bfdd2771d2bd1571f51","kind":"existing_record_review","resolution_reason":"Source
    record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-4f79f0e35977e3c2
  kind: record_content
  reference: data/ingredients/mapped/Na2-edta_X_2_H2o.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1478],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:64758","line":1480,"mapping_status":"REJECTED","ontology_id":"CHEBI:64758","preferred_term":"Na2-EDTA
    x 2 H2O"}],"identifier":"CHEBI:64758","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":139,"edge_count":139,"occurrences":140},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:64758","ontology_label":"EDTA
    disodium salt dihydrate","ontology_source":"CHEBI"},"preferred_term":"Na2-EDTA
    x 2 H2O","sssom_rows":[],"sssom_subject":"MIM:Na2-edta_X_2_H2o","synonym_count":9}'
  snapshot_sha256: 9f02a335a6dfebf13a162ed0d697ec16f4d584a5a4af55dfdba7aa7f26d24670
- evidence_id: ev-a82e93bade2bed4d
  kind: prior_review
  reference: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
  locator: findings[finding_id=f-299959d93cd9bbd6]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-299959d93cd9bbd6 in 20261011T024637Z-mim-reconcile-all-batch-09
  snapshot_sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
assessments:
- assessment_id: a-a73b33ec0f1a8132
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-9b40e28e8fe3ad48
  evidence_ids:
  - ev-4073bb1838002263
  - ev-02ec9af1bcfc9813
  - ev-b8162ce3cb322201
  - ev-41fa9675a7893c1f
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-ecaf0029e49e3c01
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-9b40e28e8fe3ad48
  evidence_ids:
  - ev-85f9b8933372b9e0
  - ev-068af2cfb7d21511
  - ev-4073bb1838002263
  - ev-c295452482ffc128
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-10-01T05:02:50Z;
    reviewed SHA-256=9f02a335a6dfebf13a162ed0d697ec16f4d584a5a4af55dfdba7aa7f26d24670;
    current SHA-256=9f02a335a6dfebf13a162ed0d697ec16f4d584a5a4af55dfdba7aa7f26d24670;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050250Z-Na2-edta_X_2_H2o.md","reports/yaml_record_review/Na2-edta_X_2_H2o.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Na2-edta_X_2_H2o.md` after the record changed from
    75ed775eb108925f06cb86d2d136daf16bfca48452002d5599e8594adfb06c10 to 9f02a335a6dfebf13a162ed0d697ec16f4d584a5a4af55dfdba7aa7f26d24670;
    preserved the previous minor finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-85f9b8933372b9e0
    - ev-068af2cfb7d21511
    - ev-4073bb1838002263
  - name: legacy-native-ids
    value: '["SEM:3bfdd2771d2bd1571f51"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-4073bb1838002263
    - ev-85f9b8933372b9e0
    - ev-068af2cfb7d21511
    - ev-c295452482ffc128
- assessment_id: a-4f79f0e35977e3c2
  area: evidence
  topic: Historical provisional-role concern
  outcome: unknown
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-9b40e28e8fe3ad48
  evidence_ids:
  - ev-85f9b8933372b9e0
  - ev-068af2cfb7d21511
  - ev-4f79f0e35977e3c2
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-85f9b8933372b9e0
    - ev-068af2cfb7d21511
    - ev-4f79f0e35977e3c2
findings:
- finding_id: rec-f-299959d93cd9bbd6
  issue_key: mim-reconciliation-role-support-9b40e28e8fe3ad48
  category: evidence
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Reassess prediction-only role support: Na2-EDTA x 2 H2O'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-9b40e28e8fe3ad48
  evidence_ids:
  - ev-85f9b8933372b9e0
  - ev-068af2cfb7d21511
  - ev-4f79f0e35977e3c2
  - ev-a82e93bade2bed4d
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2-edta_X_2_H2o.yaml
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
    review_id: 20261011T024637Z-mim-reconcile-all-batch-09
    finding_id: f-299959d93cd9bbd6
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
  with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.
```
