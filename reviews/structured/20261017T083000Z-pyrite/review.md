# Per-record structured review: Pyrite (data/ingredients/mapped/Pyrite.yaml)

- Review: 20261017T083000Z-pyrite
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Pyrite (data/ingredients/mapped/Pyrite.yaml, record-3d5d5fde8841d61b, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Pyrite.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Pyrite.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-3d5d5fde8841d61b | data/ingredients/mapped/Pyrite.yaml | maintained | Pyrite |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-3d5d5fde8841d61b | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-3d5d5fde8841d61b | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-3d5d5fde8841d61b | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-3d5d5fde8841d61b.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-3d5d5fde8841d61b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:03:15Z; reviewed SHA-256=5fbbf38f949e11e978ee47a294a8efcbf31b14c293bef1552437c1f5bd1532c0; current SHA-256=5fbbf38f949e11e978ee47a294a8efcbf31b14c293bef1552437c1f5bd1532c0; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050315Z-Pyrite.md","reports/yaml_record_review/Pyrite.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Pyrite.md&#96; after the record changed from fced595891511b3addcac807c4dd6e4d6ca0b434c45ea4a0414ee5aec8b141d7 to 5fbbf38f949e11e978ee47a294a8efcbf31b14c293bef1552437c1f5bd1532c0; preserved the previous major finding floor pending targeted retirement.

## Findings

### rec-f-20e62ec53ac4a329: Historical review coverage and residual narrative: Pyrite

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-3d5d5fde8841d61b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:03:15Z; reviewed SHA-256=5fbbf38f949e11e978ee47a294a8efcbf31b14c293bef1552437c1f5bd1532c0; current SHA-256=5fbbf38f949e11e978ee47a294a8efcbf31b14c293bef1552437c1f5bd1532c0; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050315Z-Pyrite.md","reports/yaml_record_review/Pyrite.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Pyrite.md&#96; after the record changed from fced595891511b3addcac807c4dd6e4d6ca0b434c45ea4a0414ee5aec8b141d7 to 5fbbf38f949e11e978ee47a294a8efcbf31b14c293bef1552437c1f5bd1532c0; preserved the previous major finding floor pending targeted retirement.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-3569a0c7c4e4fc58 | data/ingredients/mapped/Pyrite.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1730],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:86471","line":1732,"mapping_status":"MAPPED","ontology_id":"CHEBI:86471","preferred_term":"Pyrite"}],"identifier":"CHEBI:86471","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:86471","ontology_label":"pyrite","ontology_source":"CHEBI"},"preferred_term":"Pyrite","sssom_rows":[{"data_row":2387,"object_id":"CHEBI:86471","object_label":"pyrite","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Pyrite","synonym_count":2} |
| ev-3a2d08ad14fb68eb | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1730] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-081c43f6cca65b0a | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Pyrite; data-row positions=[2387] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2387,"object_id":"CHEBI:86471","object_label":"pyrite","other":"iron(2+) disulfide","predicate_id":"skos:exactMatch","subject_id":"MIM:Pyrite","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-237e52f7ae9827d0 | docs/data/mapped_ingredients.csv; CSV lines=[1732] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:86471","line":1732,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:86471","preferred_term":"Pyrite","total_occurrences":"0"}] |
| ev-68b97d154956d86d | reports/yaml_record_review/20261001T050315Z-Pyrite.md; YAML Record Review: Pyrite:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-2881e90f55fede87 | reports/yaml_record_review/Pyrite.md; &#96;data/ingredients/mapped/Pyrite.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-a2b8273524da269f | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1155] | context_only | [{"current_record_sha256":"5fbbf38f949e11e978ee47a294a8efcbf31b14c293bef1552437c1f5bd1532c0","finding_id":"SEM:49abb909d14d6d15fed6","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-pyrite
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Pyrite (data/ingredients/mapped/Pyrite.yaml)'
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
summary: Per-record structured review for Pyrite (data/ingredients/mapped/Pyrite.yaml,
  record-3d5d5fde8841d61b, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Pyrite.yaml
    sha256: 5fbbf38f949e11e978ee47a294a8efcbf31b14c293bef1552437c1f5bd1532c0
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
  - path: reports/yaml_record_review/20261001T050315Z-Pyrite.md
    sha256: 3b5dc3ca1d0ef871e5b4bd70c0c9ef41e21bf68fd8de71c2a20638c9ae5eb191
    role: context
  - path: reports/yaml_record_review/Pyrite.md
    sha256: 275fa7e67447d4c778a34f955202f16729207f480a8aa8cff939d7b114d117a9
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-3d5d5fde8841d61b
  path: data/ingredients/mapped/Pyrite.yaml
  label: Pyrite
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Pyrite.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Pyrite.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Pyrite.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-3d5d5fde8841d61b
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-3d5d5fde8841d61b
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-3d5d5fde8841d61b
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10
    and semantic review dispositions on HEAD.
  target_ids:
  - record-3d5d5fde8841d61b
evidence:
- evidence_id: ev-3569a0c7c4e4fc58
  kind: record_content
  reference: data/ingredients/mapped/Pyrite.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1730],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:86471","line":1732,"mapping_status":"MAPPED","ontology_id":"CHEBI:86471","preferred_term":"Pyrite"}],"identifier":"CHEBI:86471","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:86471","ontology_label":"pyrite","ontology_source":"CHEBI"},"preferred_term":"Pyrite","sssom_rows":[{"data_row":2387,"object_id":"CHEBI:86471","object_label":"pyrite","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Pyrite","synonym_count":2}'
  snapshot_sha256: 5fbbf38f949e11e978ee47a294a8efcbf31b14c293bef1552437c1f5bd1532c0
- evidence_id: ev-3a2d08ad14fb68eb
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1730]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-081c43f6cca65b0a
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Pyrite; data-row positions=[2387]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2387,"object_id":"CHEBI:86471","object_label":"pyrite","other":"iron(2+)
    disulfide","predicate_id":"skos:exactMatch","subject_id":"MIM:Pyrite","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-237e52f7ae9827d0
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1732]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:86471","line":1732,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:86471","preferred_term":"Pyrite","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-68b97d154956d86d
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050315Z-Pyrite.md
  locator: 'YAML Record Review: Pyrite:2; Target:10; Validation:20; Identity and Grounding:27;
    Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61;
    Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 3b5dc3ca1d0ef871e5b4bd70c0c9ef41e21bf68fd8de71c2a20638c9ae5eb191
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/Pyrite.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The exact
    CHEBI:86471 pyrite identity passes, but final SSSOM exports a process-qualified
    oxidation token.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Pyrite.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Pyrite.yaml`,
    `just validate-terms data/ingredients/mapped/Pyrite.yaml` where applicable, and
    `just qc-sssom`.'
- evidence_id: ev-2881e90f55fede87
  kind: prior_review
  reference: reports/yaml_record_review/Pyrite.md
  locator: '`data/ingredients/mapped/Pyrite.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 275fa7e67447d4c778a34f955202f16729207f480a8aa8cff939d7b114d117a9
- evidence_id: ev-a2b8273524da269f
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1155]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"5fbbf38f949e11e978ee47a294a8efcbf31b14c293bef1552437c1f5bd1532c0","finding_id":"SEM:49abb909d14d6d15fed6","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-7de2ab666f661142
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-3d5d5fde8841d61b
  evidence_ids:
  - ev-3569a0c7c4e4fc58
  - ev-3a2d08ad14fb68eb
  - ev-081c43f6cca65b0a
  - ev-237e52f7ae9827d0
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-d208aedd1559f29a
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-3d5d5fde8841d61b
  evidence_ids:
  - ev-68b97d154956d86d
  - ev-2881e90f55fede87
  - ev-3569a0c7c4e4fc58
  - ev-a2b8273524da269f
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:03:15Z;
    reviewed SHA-256=5fbbf38f949e11e978ee47a294a8efcbf31b14c293bef1552437c1f5bd1532c0;
    current SHA-256=5fbbf38f949e11e978ee47a294a8efcbf31b14c293bef1552437c1f5bd1532c0;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050315Z-Pyrite.md","reports/yaml_record_review/Pyrite.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Pyrite.md` after the record changed from fced595891511b3addcac807c4dd6e4d6ca0b434c45ea4a0414ee5aec8b141d7
    to 5fbbf38f949e11e978ee47a294a8efcbf31b14c293bef1552437c1f5bd1532c0; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-68b97d154956d86d
    - ev-2881e90f55fede87
    - ev-3569a0c7c4e4fc58
  - name: legacy-native-ids
    value: '["SEM:49abb909d14d6d15fed6"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-3569a0c7c4e4fc58
    - ev-68b97d154956d86d
    - ev-2881e90f55fede87
    - ev-a2b8273524da269f
findings:
- finding_id: rec-f-20e62ec53ac4a329
  issue_key: mim-reconciliation-historical-review-coverage-and-r-3d5d5fde8841d61b
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Pyrite'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:03:15Z;
    reviewed SHA-256=5fbbf38f949e11e978ee47a294a8efcbf31b14c293bef1552437c1f5bd1532c0;
    current SHA-256=5fbbf38f949e11e978ee47a294a8efcbf31b14c293bef1552437c1f5bd1532c0;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050315Z-Pyrite.md","reports/yaml_record_review/Pyrite.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Pyrite.md` after the record changed from fced595891511b3addcac807c4dd6e4d6ca0b434c45ea4a0414ee5aec8b141d7
    to 5fbbf38f949e11e978ee47a294a8efcbf31b14c293bef1552437c1f5bd1532c0; preserved
    the previous major finding floor pending targeted retirement.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-3d5d5fde8841d61b
  evidence_ids:
  - ev-68b97d154956d86d
  - ev-2881e90f55fede87
  - ev-3569a0c7c4e4fc58
  - ev-a2b8273524da269f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Pyrite.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.
```
