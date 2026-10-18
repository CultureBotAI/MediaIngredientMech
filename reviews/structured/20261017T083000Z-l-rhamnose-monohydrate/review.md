# Per-record structured review: L-Rhamnose_Monohydrate (data/ingredients/mapped/L-Rhamnose_Monohydrate.yaml)

- Review: 20261017T083000Z-l-rhamnose-monohydrate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for L-Rhamnose_Monohydrate (data/ingredients/mapped/L-Rhamnose_Monohydrate.yaml, record-dd0f65adc920f236, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/L-Rhamnose_Monohydrate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/L-Rhamnose_Monohydrate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-dd0f65adc920f236 | data/ingredients/mapped/L-Rhamnose_Monohydrate.yaml | maintained | L-Rhamnose_Monohydrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-dd0f65adc920f236 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-dd0f65adc920f236 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-dd0f65adc920f236 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-dd0f65adc920f236.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-dd0f65adc920f236.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T22:23:47Z; reviewed SHA-256=eb05ee0a45c1a49feb004fdded1ec8490ee6e8d3689ff70fe850737aac78133f; current SHA-256=eb05ee0a45c1a49feb004fdded1ec8490ee6e8d3689ff70fe850737aac78133f; hash_changed=False. Reports=["reports/yaml_record_review/L-Rhamnose_Monohydrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS primary identity, PubChem monohydrate structure, close parent, exact CAS row, and hydrate review pass, but the local registry anchor is missing and CARBON_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-dd0f65adc920f236.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-a5547e7ec28d850d: Reassess prediction-only role support: L-Rhamnose monohydrate

major / open / confirmed; issue key: mim-reconciliation-role-support-dd0f65adc920f236.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-a5547e7ec28d850d

Reassess prediction-only role support: L-Rhamnose monohydrate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-3110895804027ad6 | data/ingredients/mapped/L-Rhamnose_Monohydrate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1232],"raw_equal":true},"docs_rows":[{"identifier":"cas:10030-85-0","line":1234,"mapping_status":"MAPPED","ontology_id":"CHEBI:62345","preferred_term":"L-Rhamnose monohydrate"}],"identifier":"cas:10030-85-0","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:62345","ontology_label":"L-rhamnose","ontology_source":"CHEBI"},"preferred_term":"L-Rhamnose monohydrate","sssom_rows":[{"data_row":1587,"object_id":"CHEBI:62345","object_label":"L-rhamnose","predicate_id":"skos:closeMatch"},{"data_row":1588,"object_id":"cas:10030-85-0","object_label":"L-Rhamnose monohydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-Rhamnose_Monohydrate","synonym_count":0} |
| ev-2b5f5f641d8a930d | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1232] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-528b888c01c82eae | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:L-Rhamnose_Monohydrate; data-row positions=[1587, 1588] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1587,"object_id":"CHEBI:62345","object_label":"L-rhamnose","other":"CAS:10030-85-0","predicate_id":"skos:closeMatch","subject_id":"MIM:L-Rhamnose_Monohydrate","validation_method":"OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-09-02"},{"data_row":1588,"object_id":"cas:10030-85-0","object_label":"L-Rhamnose monohydrate","other":"CAS:10030-85-0","predicate_id":"skos:exactMatch","subject_id":"MIM:L-Rhamnose_Monohydrate","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-936a81360c044517 | docs/data/mapped_ingredients.csv; CSV lines=[1234] | supports | Published identity and count rows inspected: [{"identifier":"cas:10030-85-0","line":1234,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:62345","preferred_term":"L-Rhamnose monohydrate","total_occurrences":"0"}] |
| ev-723a4822b80a6792 | reports/yaml_record_review/L-Rhamnose_Monohydrate.md; &#96;data/ingredients/mapped/L-Rhamnose_Monohydrate.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:32; Completeness:57; Recommended Edits:66 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-a83b20303367fb17 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[798,2081] | context_only | [{"current_record_sha256":"eb05ee0a45c1a49feb004fdded1ec8490ee6e8d3689ff70fe850737aac78133f","finding_id":"SEM:1ea7b42dd9aa6388aa7f","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"eb05ee0a45c1a49feb004fdded1ec8490ee6e8d3689ff70fe850737aac78133f","finding_id":"SEM:8de0e184a4a9e57bcb14","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-04f1860589fd7fd8 | data/ingredients/mapped/L-Rhamnose_Monohydrate.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1232],"raw_equal":true},"docs_rows":[{"identifier":"cas:10030-85-0","line":1234,"mapping_status":"MAPPED","ontology_id":"CHEBI:62345","preferred_term":"L-Rhamnose monohydrate"}],"identifier":"cas:10030-85-0","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:62345","ontology_label":"L-rhamnose","ontology_source":"CHEBI"},"preferred_term":"L-Rhamnose monohydrate","sssom_rows":[{"data_row":1587,"object_id":"CHEBI:62345","object_label":"L-rhamnose","predicate_id":"skos:closeMatch"},{"data_row":1588,"object_id":"cas:10030-85-0","object_label":"L-Rhamnose monohydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-Rhamnose_Monohydrate","synonym_count":0} |
| ev-1f3c275d00afc793 | reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml; findings[finding_id=f-a5547e7ec28d850d] | context_only | Predecessor structured review finding f-a5547e7ec28d850d in 20261011T024635Z-mim-reconcile-all-batch-07 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-l-rhamnose-monohydrate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: L-Rhamnose_Monohydrate (data/ingredients/mapped/L-Rhamnose_Monohydrate.yaml)'
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
summary: Per-record structured review for L-Rhamnose_Monohydrate (data/ingredients/mapped/L-Rhamnose_Monohydrate.yaml,
  record-dd0f65adc920f236, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/L-Rhamnose_Monohydrate.yaml
    sha256: eb05ee0a45c1a49feb004fdded1ec8490ee6e8d3689ff70fe850737aac78133f
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
  - path: reports/yaml_record_review/L-Rhamnose_Monohydrate.md
    sha256: 0f180a93b43c7d775786e124b54e3def91f2d8f907cd57c4340bf9148d2ea17f
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-dd0f65adc920f236
  path: data/ingredients/mapped/L-Rhamnose_Monohydrate.yaml
  label: L-Rhamnose_Monohydrate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-Rhamnose_Monohydrate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/L-Rhamnose_Monohydrate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/L-Rhamnose_Monohydrate.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-dd0f65adc920f236
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-dd0f65adc920f236
  evidence_ids:
  - ev-3110895804027ad6
  - ev-2b5f5f641d8a930d
  - ev-528b888c01c82eae
  - ev-936a81360c044517
  - ev-04f1860589fd7fd8
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-dd0f65adc920f236
  evidence_ids:
  - ev-3110895804027ad6
  - ev-a83b20303367fb17
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-dd0f65adc920f236
  evidence_ids:
  - ev-723a4822b80a6792
  - ev-a83b20303367fb17
  - ev-1f3c275d00afc793
evidence:
- evidence_id: ev-3110895804027ad6
  kind: record_content
  reference: data/ingredients/mapped/L-Rhamnose_Monohydrate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1232],"raw_equal":true},"docs_rows":[{"identifier":"cas:10030-85-0","line":1234,"mapping_status":"MAPPED","ontology_id":"CHEBI:62345","preferred_term":"L-Rhamnose
    monohydrate"}],"identifier":"cas:10030-85-0","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:62345","ontology_label":"L-rhamnose","ontology_source":"CHEBI"},"preferred_term":"L-Rhamnose
    monohydrate","sssom_rows":[{"data_row":1587,"object_id":"CHEBI:62345","object_label":"L-rhamnose","predicate_id":"skos:closeMatch"},{"data_row":1588,"object_id":"cas:10030-85-0","object_label":"L-Rhamnose
    monohydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-Rhamnose_Monohydrate","synonym_count":0}'
  snapshot_sha256: eb05ee0a45c1a49feb004fdded1ec8490ee6e8d3689ff70fe850737aac78133f
- evidence_id: ev-2b5f5f641d8a930d
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1232]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-528b888c01c82eae
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:L-Rhamnose_Monohydrate; data-row positions=[1587, 1588]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1587,"object_id":"CHEBI:62345","object_label":"L-rhamnose","other":"CAS:10030-85-0","predicate_id":"skos:closeMatch","subject_id":"MIM:L-Rhamnose_Monohydrate","validation_method":"OLS:chebi|SYNONYM_ENRICH|2026-09-02"},{"data_row":1588,"object_id":"cas:10030-85-0","object_label":"L-Rhamnose
    monohydrate","other":"CAS:10030-85-0","predicate_id":"skos:exactMatch","subject_id":"MIM:L-Rhamnose_Monohydrate","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-936a81360c044517
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1234]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:10030-85-0","line":1234,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:62345","preferred_term":"L-Rhamnose
    monohydrate","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-723a4822b80a6792
  kind: prior_review
  reference: reports/yaml_record_review/L-Rhamnose_Monohydrate.md
  locator: '`data/ingredients/mapped/L-Rhamnose_Monohydrate.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:32; Completeness:57; Recommended Edits:66'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 0f180a93b43c7d775786e124b54e3def91f2d8f907cd57c4340bf9148d2ea17f
  quote: "Recommended Edits:\n- Major: repair final SSSOM generation for this CAS-primary\
    \ close-match hydrate\n  so `MIM:L-Rhamnose_Monohydrate` receives an exact local\n\
    \  `kgmicrobe.compound:l-rhamnose_monohydrate` row alongside the close parent\
    \ and\n  exact CAS rows.\n- Major: remove `nutritional_roles.CARBON_SOURCE` unless\
    \ an inspected\n  CultureMech, FEBA, Hans80, or literature source can support\
    \ L-rhamnose\n  monohydrate as a carbon source.\n- Rerun strict, term, hydrate,\
    \ round-trip, role, component, and SSSOM validation\n  after those changes."
- evidence_id: ev-a83b20303367fb17
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[798,2081]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"eb05ee0a45c1a49feb004fdded1ec8490ee6e8d3689ff70fe850737aac78133f","finding_id":"SEM:1ea7b42dd9aa6388aa7f","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"eb05ee0a45c1a49feb004fdded1ec8490ee6e8d3689ff70fe850737aac78133f","finding_id":"SEM:8de0e184a4a9e57bcb14","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-04f1860589fd7fd8
  kind: record_content
  reference: data/ingredients/mapped/L-Rhamnose_Monohydrate.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1232],"raw_equal":true},"docs_rows":[{"identifier":"cas:10030-85-0","line":1234,"mapping_status":"MAPPED","ontology_id":"CHEBI:62345","preferred_term":"L-Rhamnose
    monohydrate"}],"identifier":"cas:10030-85-0","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:62345","ontology_label":"L-rhamnose","ontology_source":"CHEBI"},"preferred_term":"L-Rhamnose
    monohydrate","sssom_rows":[{"data_row":1587,"object_id":"CHEBI:62345","object_label":"L-rhamnose","predicate_id":"skos:closeMatch"},{"data_row":1588,"object_id":"cas:10030-85-0","object_label":"L-Rhamnose
    monohydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-Rhamnose_Monohydrate","synonym_count":0}'
  snapshot_sha256: eb05ee0a45c1a49feb004fdded1ec8490ee6e8d3689ff70fe850737aac78133f
- evidence_id: ev-1f3c275d00afc793
  kind: prior_review
  reference: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
  locator: findings[finding_id=f-a5547e7ec28d850d]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-a5547e7ec28d850d in 20261011T024635Z-mim-reconcile-all-batch-07
  snapshot_sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
assessments:
- assessment_id: a-4d617c9dae8667a0
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-dd0f65adc920f236
  evidence_ids:
  - ev-3110895804027ad6
  - ev-2b5f5f641d8a930d
  - ev-528b888c01c82eae
  - ev-936a81360c044517
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-711e5ebe3a68f256
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-dd0f65adc920f236
  evidence_ids:
  - ev-723a4822b80a6792
  - ev-3110895804027ad6
  - ev-a83b20303367fb17
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T22:23:47Z;
    reviewed SHA-256=eb05ee0a45c1a49feb004fdded1ec8490ee6e8d3689ff70fe850737aac78133f;
    current SHA-256=eb05ee0a45c1a49feb004fdded1ec8490ee6e8d3689ff70fe850737aac78133f;
    hash_changed=False. Reports=["reports/yaml_record_review/L-Rhamnose_Monohydrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS
    primary identity, PubChem monohydrate structure, close parent, exact CAS row,
    and hydrate review pass, but the local registry anchor is missing and CARBON_SOURCE
    is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-723a4822b80a6792
    - ev-3110895804027ad6
  - name: legacy-native-ids
    value: '["SEM:1ea7b42dd9aa6388aa7f","SEM:8de0e184a4a9e57bcb14"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-3110895804027ad6
    - ev-723a4822b80a6792
    - ev-a83b20303367fb17
- assessment_id: a-04f1860589fd7fd8
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-dd0f65adc920f236
  evidence_ids:
  - ev-723a4822b80a6792
  - ev-04f1860589fd7fd8
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-723a4822b80a6792
    - ev-04f1860589fd7fd8
findings:
- finding_id: rec-f-a5547e7ec28d850d
  issue_key: mim-reconciliation-role-support-dd0f65adc920f236
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: L-Rhamnose monohydrate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-dd0f65adc920f236
  evidence_ids:
  - ev-723a4822b80a6792
  - ev-04f1860589fd7fd8
  - ev-1f3c275d00afc793
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-Rhamnose_Monohydrate.yaml
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
    review_id: 20261011T024635Z-mim-reconcile-all-batch-07
    finding_id: f-a5547e7ec28d850d
actions:
- action_id: rec-action-a5547e7ec28d850d
  description: 'Reassess prediction-only role support: L-Rhamnose monohydrate'
  finding_ids:
  - rec-f-a5547e7ec28d850d
  target_ids:
  - record-dd0f65adc920f236
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-Rhamnose_Monohydrate.yaml
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
