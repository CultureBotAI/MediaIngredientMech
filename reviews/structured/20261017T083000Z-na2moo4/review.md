# Per-record structured review: Na2moo4 (data/ingredients/mapped/Na2moo4.yaml)

- Review: 20261017T083000Z-na2moo4
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Na2moo4 (data/ingredients/mapped/Na2moo4.yaml, record-fa80b058812c8549, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Na2moo4.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Na2moo4.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-fa80b058812c8549 | data/ingredients/mapped/Na2moo4.yaml | maintained | Na2moo4 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-fa80b058812c8549 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-fa80b058812c8549 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-fa80b058812c8549 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-fa80b058812c8549.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-fa80b058812c8549.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:19:32Z; reviewed SHA-256=61771cf9de80581a816c2747c7d83d51d58830b529096058b858104d98845277; current SHA-256=61771cf9de80581a816c2747c7d83d51d58830b529096058b858104d98845277; hash_changed=False. Reports=["reports/yaml_record_review/Na2moo4.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:75215 anhydrous sodium molybdate identity and TRACE_ELEMENT role pass, but final other has a concentration token.

## Findings

### rec-f-9890b179b07273c0: Historical review coverage and residual narrative: Na2moo4

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-fa80b058812c8549.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:19:32Z; reviewed SHA-256=61771cf9de80581a816c2747c7d83d51d58830b529096058b858104d98845277; current SHA-256=61771cf9de80581a816c2747c7d83d51d58830b529096058b858104d98845277; hash_changed=False. Reports=["reports/yaml_record_review/Na2moo4.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:75215 anhydrous sodium molybdate identity and TRACE_ELEMENT role pass, but final other has a concentration token.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-4fdab8a8dda45dce | data/ingredients/mapped/Na2moo4.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1494],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:75215","line":1496,"mapping_status":"MAPPED","ontology_id":"CHEBI:75215","preferred_term":"Na2MoO4"}],"identifier":"CHEBI:75215","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":227,"edge_count":227,"occurrences":227},"occurrence_statistics":{"media_count":227,"total_occurrences":227},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:75215","ontology_label":"sodium molybdate (anhydrous)","ontology_source":"CHEBI"},"preferred_term":"Na2MoO4","sssom_rows":[{"data_row":2005,"object_id":"CHEBI:75215","object_label":"sodium molybdate (anhydrous)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2moo4","synonym_count":27} |
| ev-a0e4d4d8a6c57d61 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1494] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-330e21300daa5999 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Na2moo4; data-row positions=[2005] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2005,"object_id":"CHEBI:75215","object_label":"sodium molybdate (anhydrous)","other":"Disodium molybdate&#124;Molybdic acid, disodium salt&#124;Natriummolybdat&#124;Sodium molybdate&#124;Sodium molybdate(VI)&#124;sodium dioxido(dioxo)molybdenum&#124;Na2MoO4 (0.01 M)&#124;CAS:7631-95-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Na2moo4","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-3815ccff31b45d24 | docs/data/mapped_ingredients.csv; CSV lines=[1496] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:75215","line":1496,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"227","ontology_id":"CHEBI:75215","preferred_term":"Na2MoO4","total_occurrences":"227"}] |
| ev-0b836e31b1de33e8 | reports/yaml_record_review/Na2moo4.md; &#96;data/ingredients/mapped/Na2moo4.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:28; Completeness:44; Recommended Edits:52 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-3f14eced7a5bf28b | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1000] | context_only | [{"current_record_sha256":"61771cf9de80581a816c2747c7d83d51d58830b529096058b858104d98845277","finding_id":"SEM:7cafd2fb0264facd6719","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-na2moo4
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Na2moo4 (data/ingredients/mapped/Na2moo4.yaml)'
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
summary: Per-record structured review for Na2moo4 (data/ingredients/mapped/Na2moo4.yaml,
  record-fa80b058812c8549, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Na2moo4.yaml
    sha256: 61771cf9de80581a816c2747c7d83d51d58830b529096058b858104d98845277
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
  - path: reports/yaml_record_review/Na2moo4.md
    sha256: cd9a91439eea08956253c8248bf644b36c00e0f551de46b2d3eee39077ab0664
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-fa80b058812c8549
  path: data/ingredients/mapped/Na2moo4.yaml
  label: Na2moo4
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2moo4.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Na2moo4.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Na2moo4.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-fa80b058812c8549
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-fa80b058812c8549
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-fa80b058812c8549
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-fa80b058812c8549
evidence:
- evidence_id: ev-4fdab8a8dda45dce
  kind: record_content
  reference: data/ingredients/mapped/Na2moo4.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1494],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:75215","line":1496,"mapping_status":"MAPPED","ontology_id":"CHEBI:75215","preferred_term":"Na2MoO4"}],"identifier":"CHEBI:75215","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":227,"edge_count":227,"occurrences":227},"occurrence_statistics":{"media_count":227,"total_occurrences":227},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:75215","ontology_label":"sodium
    molybdate (anhydrous)","ontology_source":"CHEBI"},"preferred_term":"Na2MoO4","sssom_rows":[{"data_row":2005,"object_id":"CHEBI:75215","object_label":"sodium
    molybdate (anhydrous)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2moo4","synonym_count":27}'
  snapshot_sha256: 61771cf9de80581a816c2747c7d83d51d58830b529096058b858104d98845277
- evidence_id: ev-a0e4d4d8a6c57d61
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1494]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-330e21300daa5999
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Na2moo4; data-row positions=[2005]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2005,"object_id":"CHEBI:75215","object_label":"sodium
    molybdate (anhydrous)","other":"Disodium molybdate|Molybdic acid, disodium salt|Natriummolybdat|Sodium
    molybdate|Sodium molybdate(VI)|sodium dioxido(dioxo)molybdenum|Na2MoO4 (0.01 M)|CAS:7631-95-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Na2moo4","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-3815ccff31b45d24
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1496]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:75215","line":1496,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"227","ontology_id":"CHEBI:75215","preferred_term":"Na2MoO4","total_occurrences":"227"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-0b836e31b1de33e8
  kind: prior_review
  reference: reports/yaml_record_review/Na2moo4.md
  locator: '`data/ingredients/mapped/Na2moo4.yaml`:2; Verdict:4; Identity:11; Validation:21;
    Evidence:28; Completeness:44; Recommended Edits:52'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: cd9a91439eea08956253c8248bf644b36c00e0f551de46b2d3eee39077ab0664
  quote: "Recommended Edits:\n- Major: keep `Na2MoO4 (0.01 M)` as occurrence provenance\
    \ only so it no longer\n  publishes as an exact `Na2MoO4` synonym; rebuild final\
    \ SSSOM and rerun final\n  SSSOM validation plus product label validation."
- evidence_id: ev-3f14eced7a5bf28b
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1000]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"61771cf9de80581a816c2747c7d83d51d58830b529096058b858104d98845277","finding_id":"SEM:7cafd2fb0264facd6719","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-46a504b9607ac680
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-fa80b058812c8549
  evidence_ids:
  - ev-4fdab8a8dda45dce
  - ev-a0e4d4d8a6c57d61
  - ev-330e21300daa5999
  - ev-3815ccff31b45d24
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-613105ee79b1e28a
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-fa80b058812c8549
  evidence_ids:
  - ev-0b836e31b1de33e8
  - ev-4fdab8a8dda45dce
  - ev-3f14eced7a5bf28b
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:19:32Z;
    reviewed SHA-256=61771cf9de80581a816c2747c7d83d51d58830b529096058b858104d98845277;
    current SHA-256=61771cf9de80581a816c2747c7d83d51d58830b529096058b858104d98845277;
    hash_changed=False. Reports=["reports/yaml_record_review/Na2moo4.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI:75215 anhydrous
    sodium molybdate identity and TRACE_ELEMENT role pass, but final other has a concentration
    token.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0b836e31b1de33e8
    - ev-4fdab8a8dda45dce
  - name: legacy-native-ids
    value: '["SEM:7cafd2fb0264facd6719"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-4fdab8a8dda45dce
    - ev-0b836e31b1de33e8
    - ev-3f14eced7a5bf28b
findings:
- finding_id: rec-f-9890b179b07273c0
  issue_key: mim-reconciliation-historical-review-coverage-and-r-fa80b058812c8549
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Na2moo4'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:19:32Z;
    reviewed SHA-256=61771cf9de80581a816c2747c7d83d51d58830b529096058b858104d98845277;
    current SHA-256=61771cf9de80581a816c2747c7d83d51d58830b529096058b858104d98845277;
    hash_changed=False. Reports=["reports/yaml_record_review/Na2moo4.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI:75215 anhydrous
    sodium molybdate identity and TRACE_ELEMENT role pass, but final other has a concentration
    token.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-fa80b058812c8549
  evidence_ids:
  - ev-0b836e31b1de33e8
  - ev-4fdab8a8dda45dce
  - ev-3f14eced7a5bf28b
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2moo4.yaml
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
  with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.
```
