# Per-record structured review: Methane (data/ingredients/mapped/Methane.yaml)

- Review: 20261017T083000Z-methane
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Methane (data/ingredients/mapped/Methane.yaml, record-d582055d252a80d6, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Methane.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Methane.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-d582055d252a80d6 | data/ingredients/mapped/Methane.yaml | maintained | Methane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-d582055d252a80d6 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-d582055d252a80d6 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-d582055d252a80d6 | Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-d582055d252a80d6.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-d582055d252a80d6.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:42Z; reviewed SHA-256=c0f1aa55fe19a70d6108f0b9247c852879470d46263195899939cd8e08a6feb3; current SHA-256=c0f1aa55fe19a70d6108f0b9247c852879470d46263195899939cd8e08a6feb3; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050242Z-Methane.md","reports/yaml_record_review/Methane.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Methane.md&#96; after the record changed from 1a58fe2a7cb8ceae62cb651d60e639684dff8d769a3b820545cb9e31bbffe5f0 to c0f1aa55fe19a70d6108f0b9247c852879470d46263195899939cd8e08a6feb3; preserved the previous major finding floor pending targeted retirement.

## Findings

### rec-f-4b72acf0fc2c77fd: Historical review coverage and residual narrative: Methane

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-d582055d252a80d6.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:42Z; reviewed SHA-256=c0f1aa55fe19a70d6108f0b9247c852879470d46263195899939cd8e08a6feb3; current SHA-256=c0f1aa55fe19a70d6108f0b9247c852879470d46263195899939cd8e08a6feb3; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050242Z-Methane.md","reports/yaml_record_review/Methane.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Methane.md&#96; after the record changed from 1a58fe2a7cb8ceae62cb651d60e639684dff8d769a3b820545cb9e31bbffe5f0 to c0f1aa55fe19a70d6108f0b9247c852879470d46263195899939cd8e08a6feb3; preserved the previous major finding floor pending targeted retirement.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-6b0ad89c5a797297 | data/ingredients/mapped/Methane.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1366],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16183","line":1368,"mapping_status":"MAPPED","ontology_id":"CHEBI:16183","preferred_term":"methane"}],"identifier":"CHEBI:16183","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":8,"edge_count":8,"occurrences":8},"occurrence_statistics":{"media_count":8,"total_occurrences":8},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16183","ontology_label":"methane","ontology_source":"CHEBI"},"preferred_term":"methane","sssom_rows":[{"data_row":1818,"object_id":"CHEBI:16183","object_label":"methane","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Methane","synonym_count":3} |
| ev-6e6dbccc35b0b8ef | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1366] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-bd599946e55af7d4 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Methane; data-row positions=[1818] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1818,"object_id":"CHEBI:16183","object_label":"methane","other":"tetrahydridocarbon&#124;CAS:74-82-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Methane","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-a02c7839b0c9a8dc | docs/data/mapped_ingredients.csv; CSV lines=[1368] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:16183","line":1368,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"8","ontology_id":"CHEBI:16183","preferred_term":"methane","total_occurrences":"8"}] |
| ev-a6f84fcad48a8ce3 | reports/yaml_record_review/20261001T050242Z-Methane.md; YAML Record Review: methane:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-f3c25b143e1c0a1b | reports/yaml_record_review/Methane.md; &#96;data/ingredients/mapped/Methane.yaml&#96;:2; Verdict:4; Identity:12; Validation:23; Evidence:30; Completeness:41; Recommended Edits:47 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-345b4fcade4061f0 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[917] | context_only | [{"current_record_sha256":"c0f1aa55fe19a70d6108f0b9247c852879470d46263195899939cd8e08a6feb3","finding_id":"SEM:58bcb9394b41ec098b3c","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-methane
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Methane (data/ingredients/mapped/Methane.yaml)'
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
summary: Per-record structured review for Methane (data/ingredients/mapped/Methane.yaml,
  record-d582055d252a80d6, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Methane.yaml
    sha256: c0f1aa55fe19a70d6108f0b9247c852879470d46263195899939cd8e08a6feb3
    role: target
  - path: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
    sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
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
  - path: reports/yaml_record_review/20261001T050242Z-Methane.md
    sha256: fcf186f25b7f695f4113b19d7fbf8af5911e5028123cdf2752b14b04111ca749
    role: context
  - path: reports/yaml_record_review/Methane.md
    sha256: 42936aac1b0c347e681f68475f8969294b025eaf042a6ba5768babdc1adf83ff
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-d582055d252a80d6
  path: data/ingredients/mapped/Methane.yaml
  label: Methane
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Methane.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Methane.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Methane.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-d582055d252a80d6
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-d582055d252a80d6
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-d582055d252a80d6
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08
    and semantic review dispositions on HEAD.
  target_ids:
  - record-d582055d252a80d6
evidence:
- evidence_id: ev-6b0ad89c5a797297
  kind: record_content
  reference: data/ingredients/mapped/Methane.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1366],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16183","line":1368,"mapping_status":"MAPPED","ontology_id":"CHEBI:16183","preferred_term":"methane"}],"identifier":"CHEBI:16183","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":8,"edge_count":8,"occurrences":8},"occurrence_statistics":{"media_count":8,"total_occurrences":8},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16183","ontology_label":"methane","ontology_source":"CHEBI"},"preferred_term":"methane","sssom_rows":[{"data_row":1818,"object_id":"CHEBI:16183","object_label":"methane","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Methane","synonym_count":3}'
  snapshot_sha256: c0f1aa55fe19a70d6108f0b9247c852879470d46263195899939cd8e08a6feb3
- evidence_id: ev-6e6dbccc35b0b8ef
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1366]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-bd599946e55af7d4
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Methane; data-row positions=[1818]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1818,"object_id":"CHEBI:16183","object_label":"methane","other":"tetrahydridocarbon|CAS:74-82-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Methane","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-a02c7839b0c9a8dc
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1368]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:16183","line":1368,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"8","ontology_id":"CHEBI:16183","preferred_term":"methane","total_occurrences":"8"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-a6f84fcad48a8ce3
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050242Z-Methane.md
  locator: 'YAML Record Review: methane:2; Target:10; Validation:20; Identity and
    Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: fcf186f25b7f695f4113b19d7fbf8af5911e5028123cdf2752b14b04111ca749
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/Methane.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The exact
    CHEBI:16183 identity, CAS, structure, occurrence count, and tetrahydridocarbon
    synonym pass, but final other exports produces-process labels.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Methane.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Methane.yaml`,
    `just validate-terms data/ingredients/mapped/Methane.yaml` where applicable, and
    `just qc-sssom`.'
- evidence_id: ev-f3c25b143e1c0a1b
  kind: prior_review
  reference: reports/yaml_record_review/Methane.md
  locator: '`data/ingredients/mapped/Methane.yaml`:2; Verdict:4; Identity:12; Validation:23;
    Evidence:30; Completeness:41; Recommended Edits:47'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 42936aac1b0c347e681f68475f8969294b025eaf042a6ba5768babdc1adf83ff
  quote: "Recommended Edits:\n- Mark the two `produces:` labels as non-resolving provenance\
    \ or extend the\n  synonym policy so raw production-process text is filtered from\
    \ final SSSOM\n  `other`."
- evidence_id: ev-345b4fcade4061f0
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[917]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"c0f1aa55fe19a70d6108f0b9247c852879470d46263195899939cd8e08a6feb3","finding_id":"SEM:58bcb9394b41ec098b3c","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-b5b34925f2a20612
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-d582055d252a80d6
  evidence_ids:
  - ev-6b0ad89c5a797297
  - ev-6e6dbccc35b0b8ef
  - ev-bd599946e55af7d4
  - ev-a02c7839b0c9a8dc
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-80bd7bf3f43df48a
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d582055d252a80d6
  evidence_ids:
  - ev-a6f84fcad48a8ce3
  - ev-f3c25b143e1c0a1b
  - ev-6b0ad89c5a797297
  - ev-345b4fcade4061f0
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:42Z;
    reviewed SHA-256=c0f1aa55fe19a70d6108f0b9247c852879470d46263195899939cd8e08a6feb3;
    current SHA-256=c0f1aa55fe19a70d6108f0b9247c852879470d46263195899939cd8e08a6feb3;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050242Z-Methane.md","reports/yaml_record_review/Methane.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Methane.md` after the record changed from 1a58fe2a7cb8ceae62cb651d60e639684dff8d769a3b820545cb9e31bbffe5f0
    to c0f1aa55fe19a70d6108f0b9247c852879470d46263195899939cd8e08a6feb3; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-a6f84fcad48a8ce3
    - ev-f3c25b143e1c0a1b
    - ev-6b0ad89c5a797297
  - name: legacy-native-ids
    value: '["SEM:58bcb9394b41ec098b3c"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-6b0ad89c5a797297
    - ev-a6f84fcad48a8ce3
    - ev-f3c25b143e1c0a1b
    - ev-345b4fcade4061f0
findings:
- finding_id: rec-f-4b72acf0fc2c77fd
  issue_key: mim-reconciliation-historical-review-coverage-and-r-d582055d252a80d6
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Methane'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:42Z;
    reviewed SHA-256=c0f1aa55fe19a70d6108f0b9247c852879470d46263195899939cd8e08a6feb3;
    current SHA-256=c0f1aa55fe19a70d6108f0b9247c852879470d46263195899939cd8e08a6feb3;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050242Z-Methane.md","reports/yaml_record_review/Methane.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Methane.md` after the record changed from 1a58fe2a7cb8ceae62cb651d60e639684dff8d769a3b820545cb9e31bbffe5f0
    to c0f1aa55fe19a70d6108f0b9247c852879470d46263195899939cd8e08a6feb3; preserved
    the previous major finding floor pending targeted retirement.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d582055d252a80d6
  evidence_ids:
  - ev-a6f84fcad48a8ce3
  - ev-f3c25b143e1c0a1b
  - ev-6b0ad89c5a797297
  - ev-345b4fcade4061f0
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Methane.yaml
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
  with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.
```
