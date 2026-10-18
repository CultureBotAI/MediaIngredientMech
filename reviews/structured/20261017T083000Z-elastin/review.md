# Per-record structured review: Elastin (data/ingredients/mapped/Elastin.yaml)

- Review: 20261017T083000Z-elastin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Elastin (data/ingredients/mapped/Elastin.yaml, record-aafab49648f0658d, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Elastin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Elastin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-aafab49648f0658d | data/ingredients/mapped/Elastin.yaml | maintained | Elastin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-aafab49648f0658d | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-aafab49648f0658d | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-aafab49648f0658d | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-aafab49648f0658d.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-aafab49648f0658d.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:13Z; reviewed SHA-256=a90a0fed8c0a5a9b12d57d0360baa49376bc9886ef614ced984bf31fce9541f5; current SHA-256=a90a0fed8c0a5a9b12d57d0360baa49376bc9886ef614ced984bf31fce9541f5; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050213Z-Elastin.md","reports/yaml_record_review/Elastin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Elastin.md&#96; after the record changed from 5b4289019de7264e0503c91a6cc4dbcd821152ea8450dc673d53cbeebe9b4718 to a90a0fed8c0a5a9b12d57d0360baa49376bc9886ef614ced984bf31fce9541f5; preserved the previous major finding floor pending targeted retirement.

## Findings

### rec-f-b534de388797107f: Historical review coverage and residual narrative: Elastin

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-aafab49648f0658d.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:13Z; reviewed SHA-256=a90a0fed8c0a5a9b12d57d0360baa49376bc9886ef614ced984bf31fce9541f5; current SHA-256=a90a0fed8c0a5a9b12d57d0360baa49376bc9886ef614ced984bf31fce9541f5; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050213Z-Elastin.md","reports/yaml_record_review/Elastin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Elastin.md&#96; after the record changed from 5b4289019de7264e0503c91a6cc4dbcd821152ea8450dc673d53cbeebe9b4718 to a90a0fed8c0a5a9b12d57d0360baa49376bc9886ef614ced984bf31fce9541f5; preserved the previous major finding floor pending targeted retirement.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-726b7ad3f05ca885 | data/ingredients/mapped/Elastin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[941],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:4767","line":943,"mapping_status":"MAPPED","ontology_id":"CHEBI:4767","preferred_term":"Elastin"}],"identifier":"CHEBI:4767","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:4767","ontology_label":"Elastin","ontology_source":"CHEBI"},"preferred_term":"Elastin","sssom_rows":[{"data_row":1115,"object_id":"CHEBI:4767","object_label":"Elastin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Elastin","synonym_count":1} |
| ev-f711a6e4759b3b0f | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [941] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-0874f09c4b260d79 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Elastin; data-row positions=[1115] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1115,"object_id":"CHEBI:4767","object_label":"Elastin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Elastin","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-d134ff3c7ff6464b | docs/data/mapped_ingredients.csv; CSV lines=[943] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:4767","line":943,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:4767","preferred_term":"Elastin","total_occurrences":"0"}] |
| ev-2543fa45e971b5e2 | reports/yaml_record_review/20261001T050213Z-Elastin.md; YAML Record Review: Elastin:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-76bb2670f0f9993c | reports/yaml_record_review/Elastin.md; &#96;data/ingredients/mapped/Elastin.yaml&#96;:2; Verdict:4; Identity:10; Validation:19; Evidence:26; Completeness:43; Recommended Edits:50 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-f19d471b9dafe2bd | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[567] | context_only | [{"current_record_sha256":"a90a0fed8c0a5a9b12d57d0360baa49376bc9886ef614ced984bf31fce9541f5","finding_id":"SEM:75fd62cdc7f8ae4961f5","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-elastin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Elastin (data/ingredients/mapped/Elastin.yaml)'
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
summary: Per-record structured review for Elastin (data/ingredients/mapped/Elastin.yaml,
  record-aafab49648f0658d, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Elastin.yaml
    sha256: a90a0fed8c0a5a9b12d57d0360baa49376bc9886ef614ced984bf31fce9541f5
    role: target
  - path: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
    sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
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
  - path: reports/yaml_record_review/20261001T050213Z-Elastin.md
    sha256: eb2cd18f951e504b2c5db1b8605c2fa33aec5ff39ce4e333fd3d669ff580c28a
    role: context
  - path: reports/yaml_record_review/Elastin.md
    sha256: 00a3840c3987ecf02fe8a099435327691720bc98616201bb08f7027bf2d29f5c
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-aafab49648f0658d
  path: data/ingredients/mapped/Elastin.yaml
  label: Elastin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Elastin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Elastin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Elastin.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-aafab49648f0658d
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-aafab49648f0658d
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-aafab49648f0658d
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-aafab49648f0658d
evidence:
- evidence_id: ev-726b7ad3f05ca885
  kind: record_content
  reference: data/ingredients/mapped/Elastin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[941],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:4767","line":943,"mapping_status":"MAPPED","ontology_id":"CHEBI:4767","preferred_term":"Elastin"}],"identifier":"CHEBI:4767","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:4767","ontology_label":"Elastin","ontology_source":"CHEBI"},"preferred_term":"Elastin","sssom_rows":[{"data_row":1115,"object_id":"CHEBI:4767","object_label":"Elastin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Elastin","synonym_count":1}'
  snapshot_sha256: a90a0fed8c0a5a9b12d57d0360baa49376bc9886ef614ced984bf31fce9541f5
- evidence_id: ev-f711a6e4759b3b0f
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [941]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-0874f09c4b260d79
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Elastin; data-row positions=[1115]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1115,"object_id":"CHEBI:4767","object_label":"Elastin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Elastin","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-d134ff3c7ff6464b
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[943]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:4767","line":943,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:4767","preferred_term":"Elastin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-2543fa45e971b5e2
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050213Z-Elastin.md
  locator: 'YAML Record Review: Elastin:2; Target:10; Validation:20; Identity and
    Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: eb2cd18f951e504b2c5db1b8605c2fa33aec5ff39ce4e333fd3d669ff580c28a
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/Elastin.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The exact
    ChEBI identity passes, but final SSSOM exports `degradation: elastin` as a synonym.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Elastin.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Elastin.yaml`,
    `just validate-terms data/ingredients/mapped/Elastin.yaml` where applicable, and
    `just qc-sssom`.'
- evidence_id: ev-76bb2670f0f9993c
  kind: prior_review
  reference: reports/yaml_record_review/Elastin.md
  locator: '`data/ingredients/mapped/Elastin.yaml`:2; Verdict:4; Identity:10; Validation:19;
    Evidence:26; Completeness:43; Recommended Edits:50'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 00a3840c3987ecf02fe8a099435327691720bc98616201bb08f7027bf2d29f5c
  quote: "Recommended Edits:\n- Major: remove `degradation: elastin` from the active\
    \ synonym surface in\n  `data/ingredients/mapped/Elastin.yaml`, or reclassify\
    \ it as\n  rejected/provenance-only so it cannot be exported in final SSSOM `other`.\n\
    - After editing the per-record YAML, run `sync-curated`, rebuild SSSOM, and\n\
    \  rerun `validate-all`, `qc-sssom`, and strict validation."
- evidence_id: ev-f19d471b9dafe2bd
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[567]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"a90a0fed8c0a5a9b12d57d0360baa49376bc9886ef614ced984bf31fce9541f5","finding_id":"SEM:75fd62cdc7f8ae4961f5","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-9f26b1e133d3592a
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-aafab49648f0658d
  evidence_ids:
  - ev-726b7ad3f05ca885
  - ev-f711a6e4759b3b0f
  - ev-0874f09c4b260d79
  - ev-d134ff3c7ff6464b
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-f1f6ab0f959c1d48
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-aafab49648f0658d
  evidence_ids:
  - ev-2543fa45e971b5e2
  - ev-76bb2670f0f9993c
  - ev-726b7ad3f05ca885
  - ev-f19d471b9dafe2bd
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:13Z;
    reviewed SHA-256=a90a0fed8c0a5a9b12d57d0360baa49376bc9886ef614ced984bf31fce9541f5;
    current SHA-256=a90a0fed8c0a5a9b12d57d0360baa49376bc9886ef614ced984bf31fce9541f5;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050213Z-Elastin.md","reports/yaml_record_review/Elastin.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Elastin.md` after the record changed from 5b4289019de7264e0503c91a6cc4dbcd821152ea8450dc673d53cbeebe9b4718
    to a90a0fed8c0a5a9b12d57d0360baa49376bc9886ef614ced984bf31fce9541f5; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-2543fa45e971b5e2
    - ev-76bb2670f0f9993c
    - ev-726b7ad3f05ca885
  - name: legacy-native-ids
    value: '["SEM:75fd62cdc7f8ae4961f5"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-726b7ad3f05ca885
    - ev-2543fa45e971b5e2
    - ev-76bb2670f0f9993c
    - ev-f19d471b9dafe2bd
findings:
- finding_id: rec-f-b534de388797107f
  issue_key: mim-reconciliation-historical-review-coverage-and-r-aafab49648f0658d
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Elastin'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:13Z;
    reviewed SHA-256=a90a0fed8c0a5a9b12d57d0360baa49376bc9886ef614ced984bf31fce9541f5;
    current SHA-256=a90a0fed8c0a5a9b12d57d0360baa49376bc9886ef614ced984bf31fce9541f5;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050213Z-Elastin.md","reports/yaml_record_review/Elastin.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Elastin.md` after the record changed from 5b4289019de7264e0503c91a6cc4dbcd821152ea8450dc673d53cbeebe9b4718
    to a90a0fed8c0a5a9b12d57d0360baa49376bc9886ef614ced984bf31fce9541f5; preserved
    the previous major finding floor pending targeted retirement.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-aafab49648f0658d
  evidence_ids:
  - ev-2543fa45e971b5e2
  - ev-76bb2670f0f9993c
  - ev-726b7ad3f05ca885
  - ev-f19d471b9dafe2bd
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Elastin.yaml
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
  with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.
```
