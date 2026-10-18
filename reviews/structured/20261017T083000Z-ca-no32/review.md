# Per-record structured review: Ca_No32 (data/ingredients/mapped/Ca_No32.yaml)

- Review: 20261017T083000Z-ca-no32
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Ca_No32 (data/ingredients/mapped/Ca_No32.yaml, record-0895105b981d23a4, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Ca_No32.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Ca_No32.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-0895105b981d23a4 | data/ingredients/mapped/Ca_No32.yaml | maintained | Ca_No32 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-0895105b981d23a4 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-0895105b981d23a4 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-0895105b981d23a4 | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-0895105b981d23a4.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-0895105b981d23a4.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:01:40Z; reviewed SHA-256=49012605fd008e5152cd647dda7f7a10dcd2f10468b0d2b68efc7339fea638ba; current SHA-256=49012605fd008e5152cd647dda7f7a10dcd2f10468b0d2b68efc7339fea638ba; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050140Z-Ca_No32.md","reports/yaml_record_review/Ca_No32.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Ca_No32.md&#96; after the record changed from 0ae0423521457237c2420e6c3ae700a1bcbfa673ae0c44b3a34eeed021f032ab to 49012605fd008e5152cd647dda7f7a10dcd2f10468b0d2b68efc7339fea638ba; preserved the previous major finding floor pending targeted retirement.

## Findings

### rec-f-772a8c6a713704c1: Historical review coverage and residual narrative: Ca_No32

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-0895105b981d23a4.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:01:40Z; reviewed SHA-256=49012605fd008e5152cd647dda7f7a10dcd2f10468b0d2b68efc7339fea638ba; current SHA-256=49012605fd008e5152cd647dda7f7a10dcd2f10468b0d2b68efc7339fea638ba; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050140Z-Ca_No32.md","reports/yaml_record_review/Ca_No32.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Ca_No32.md&#96; after the record changed from 0ae0423521457237c2420e6c3ae700a1bcbfa673ae0c44b3a34eeed021f032ab to 49012605fd008e5152cd647dda7f7a10dcd2f10468b0d2b68efc7339fea638ba; preserved the previous major finding floor pending targeted retirement.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-2e89ec5126828ae0 | data/ingredients/mapped/Ca_No32.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[618],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:64205","line":620,"mapping_status":"MAPPED","ontology_id":"CHEBI:64205","preferred_term":"Ca(NO3)2"}],"identifier":"CHEBI:64205","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":37,"edge_count":37,"occurrences":37},"occurrence_statistics":{"media_count":37,"total_occurrences":37},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:64205","ontology_label":"calcium nitrate","ontology_source":"CHEBI"},"preferred_term":"Ca(NO3)2","sssom_rows":[{"data_row":599,"object_id":"CHEBI:64205","object_label":"calcium nitrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Ca_No32","synonym_count":12} |
| ev-ccbbf2f0a2d3baae | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [618] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-c6394d8ad2bb7ddb | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Ca_No32; data-row positions=[599] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":599,"object_id":"CHEBI:64205","object_label":"calcium nitrate","other":"calcium dinitrate&#124;CAS:10124-37-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Ca_No32","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-f4d1670919198e9a | docs/data/mapped_ingredients.csv; CSV lines=[620] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:64205","line":620,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"37","ontology_id":"CHEBI:64205","preferred_term":"Ca(NO3)2","total_occurrences":"37"}] |
| ev-3a470b13251e512a | reports/yaml_record_review/20261001T050140Z-Ca_No32.md; YAML Record Review: Ca(NO3)2:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-7ccf6d1303b3d96f | reports/yaml_record_review/Ca_No32.md; &#96;data/ingredients/mapped/Ca_No32.yaml&#96;:2; Verdict:4; Identity:11; Validation:27; Evidence:40; Completeness:63; Recommended Edits:73 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-27e653d037b96f49 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[341] | context_only | [{"current_record_sha256":"49012605fd008e5152cd647dda7f7a10dcd2f10468b0d2b68efc7339fea638ba","finding_id":"SEM:641010f30b93bec1bc79","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-ca-no32
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Ca_No32 (data/ingredients/mapped/Ca_No32.yaml)'
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
native_verdict: mapping_status=MAPPED; open=0; deferred=1
scientific_review: false
summary: Per-record structured review for Ca_No32 (data/ingredients/mapped/Ca_No32.yaml,
  record-0895105b981d23a4, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Ca_No32.yaml
    sha256: 49012605fd008e5152cd647dda7f7a10dcd2f10468b0d2b68efc7339fea638ba
    role: target
  - path: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
    sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
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
  - path: reports/yaml_record_review/20261001T050140Z-Ca_No32.md
    sha256: e49254843337c97d6f9b2293b152236f835b1bc502858f62efadaaf3f2acab89
    role: context
  - path: reports/yaml_record_review/Ca_No32.md
    sha256: 04c238db2885eb1daa6d5525e56df396a837243cf7a2f3b7d4fef3b57523aac1
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-0895105b981d23a4
  path: data/ingredients/mapped/Ca_No32.yaml
  label: Ca_No32
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Ca_No32.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Ca_No32.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Ca_No32.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-0895105b981d23a4
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-0895105b981d23a4
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-0895105b981d23a4
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-0895105b981d23a4
evidence:
- evidence_id: ev-2e89ec5126828ae0
  kind: record_content
  reference: data/ingredients/mapped/Ca_No32.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[618],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:64205","line":620,"mapping_status":"MAPPED","ontology_id":"CHEBI:64205","preferred_term":"Ca(NO3)2"}],"identifier":"CHEBI:64205","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":37,"edge_count":37,"occurrences":37},"occurrence_statistics":{"media_count":37,"total_occurrences":37},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:64205","ontology_label":"calcium
    nitrate","ontology_source":"CHEBI"},"preferred_term":"Ca(NO3)2","sssom_rows":[{"data_row":599,"object_id":"CHEBI:64205","object_label":"calcium
    nitrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Ca_No32","synonym_count":12}'
  snapshot_sha256: 49012605fd008e5152cd647dda7f7a10dcd2f10468b0d2b68efc7339fea638ba
- evidence_id: ev-ccbbf2f0a2d3baae
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [618]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-c6394d8ad2bb7ddb
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Ca_No32; data-row positions=[599]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":599,"object_id":"CHEBI:64205","object_label":"calcium
    nitrate","other":"calcium dinitrate|CAS:10124-37-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Ca_No32","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-f4d1670919198e9a
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[620]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:64205","line":620,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"37","ontology_id":"CHEBI:64205","preferred_term":"Ca(NO3)2","total_occurrences":"37"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-3a470b13251e512a
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050140Z-Ca_No32.md
  locator: 'YAML Record Review: Ca(NO3)2:2; Target:10; Validation:20; Identity and
    Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: e49254843337c97d6f9b2293b152236f835b1bc502858f62efadaaf3f2acab89
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/Ca_No32.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The exact
    CHEBI calcium nitrate identity, CAS, role, occurrence count, SSSOM row, and aggregate
    copy pass, but cadmium nitrate synonyms remain.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Ca_No32.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Ca_No32.yaml`,
    `just validate-terms data/ingredients/mapped/Ca_No32.yaml` where applicable, and
    `just qc-sssom`.'
- evidence_id: ev-7ccf6d1303b3d96f
  kind: prior_review
  reference: reports/yaml_record_review/Ca_No32.md
  locator: '`data/ingredients/mapped/Ca_No32.yaml`:2; Verdict:4; Identity:11; Validation:27;
    Evidence:40; Completeness:63; Recommended Edits:73'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 04c238db2885eb1daa6d5525e56df396a837243cf7a2f3b7d4fef3b57523aac1
  quote: "Recommended Edits:\n- Major: remove the six cadmium nitrate synonyms from\n\
    \  `data/ingredients/mapped/Ca_No32.yaml`, regenerate\n  `mappings/ingredient_mappings.sssom.tsv`\
    \ so the `MIM:Ca_No32` `other` field\n  keeps only calcium nitrate aliases, then\
    \ run `just sync-curated` and focused\n  strict/term/SSSOM validation."
- evidence_id: ev-27e653d037b96f49
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[341]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"49012605fd008e5152cd647dda7f7a10dcd2f10468b0d2b68efc7339fea638ba","finding_id":"SEM:641010f30b93bec1bc79","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-e26d87fe5bb3136f
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-0895105b981d23a4
  evidence_ids:
  - ev-2e89ec5126828ae0
  - ev-ccbbf2f0a2d3baae
  - ev-c6394d8ad2bb7ddb
  - ev-f4d1670919198e9a
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-93a8cf96eba04c6a
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-0895105b981d23a4
  evidence_ids:
  - ev-3a470b13251e512a
  - ev-7ccf6d1303b3d96f
  - ev-2e89ec5126828ae0
  - ev-27e653d037b96f49
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:01:40Z;
    reviewed SHA-256=49012605fd008e5152cd647dda7f7a10dcd2f10468b0d2b68efc7339fea638ba;
    current SHA-256=49012605fd008e5152cd647dda7f7a10dcd2f10468b0d2b68efc7339fea638ba;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050140Z-Ca_No32.md","reports/yaml_record_review/Ca_No32.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Ca_No32.md` after the record changed from 0ae0423521457237c2420e6c3ae700a1bcbfa673ae0c44b3a34eeed021f032ab
    to 49012605fd008e5152cd647dda7f7a10dcd2f10468b0d2b68efc7339fea638ba; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-3a470b13251e512a
    - ev-7ccf6d1303b3d96f
    - ev-2e89ec5126828ae0
  - name: legacy-native-ids
    value: '["SEM:641010f30b93bec1bc79"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-2e89ec5126828ae0
    - ev-3a470b13251e512a
    - ev-7ccf6d1303b3d96f
    - ev-27e653d037b96f49
findings:
- finding_id: rec-f-772a8c6a713704c1
  issue_key: mim-reconciliation-historical-review-coverage-and-r-0895105b981d23a4
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Ca_No32'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:01:40Z;
    reviewed SHA-256=49012605fd008e5152cd647dda7f7a10dcd2f10468b0d2b68efc7339fea638ba;
    current SHA-256=49012605fd008e5152cd647dda7f7a10dcd2f10468b0d2b68efc7339fea638ba;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050140Z-Ca_No32.md","reports/yaml_record_review/Ca_No32.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Ca_No32.md` after the record changed from 0ae0423521457237c2420e6c3ae700a1bcbfa673ae0c44b3a34eeed021f032ab
    to 49012605fd008e5152cd647dda7f7a10dcd2f10468b0d2b68efc7339fea638ba; preserved
    the previous major finding floor pending targeted retirement.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-0895105b981d23a4
  evidence_ids:
  - ev-3a470b13251e512a
  - ev-7ccf6d1303b3d96f
  - ev-2e89ec5126828ae0
  - ev-27e653d037b96f49
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Ca_No32.yaml
    role: maintained ingredient
  field_paths:
  - curation_history
  tags:
  - reconciliation
  - bundle-by-owner
  - historical-review-coverage-and-r
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
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
  with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.
```
