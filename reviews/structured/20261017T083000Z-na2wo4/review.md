# Per-record structured review: Na2wo4 (data/ingredients/mapped/Na2wo4.yaml)

- Review: 20261017T083000Z-na2wo4
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Na2wo4 (data/ingredients/mapped/Na2wo4.yaml, record-72fc6ab22e3eb78d, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Na2wo4.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Na2wo4.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-72fc6ab22e3eb78d | data/ingredients/mapped/Na2wo4.yaml | maintained | Na2wo4 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-72fc6ab22e3eb78d | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-72fc6ab22e3eb78d | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-72fc6ab22e3eb78d | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-72fc6ab22e3eb78d.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-72fc6ab22e3eb78d.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:39:25Z; reviewed SHA-256=3fe854c3fabbea1841a8ca55ce42dcc9ed82015af31d2e636d0e86a5a48ec25a; current SHA-256=3fe854c3fabbea1841a8ca55ce42dcc9ed82015af31d2e636d0e86a5a48ec25a; hash_changed=False. Reports=["reports/yaml_record_review/Na2wo4.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:63940 sodium tungstate identity passes, but final other has a concentration-qualified label.

## Findings

### rec-f-fc1c1d097381ff13: Historical review coverage and residual narrative: Na2wo4

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-72fc6ab22e3eb78d.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:39:25Z; reviewed SHA-256=3fe854c3fabbea1841a8ca55ce42dcc9ed82015af31d2e636d0e86a5a48ec25a; current SHA-256=3fe854c3fabbea1841a8ca55ce42dcc9ed82015af31d2e636d0e86a5a48ec25a; hash_changed=False. Reports=["reports/yaml_record_review/Na2wo4.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:63940 sodium tungstate identity passes, but final other has a concentration-qualified label.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-64eb7d68adae72d4 | data/ingredients/mapped/Na2wo4.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1512],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:63940","line":1514,"mapping_status":"MAPPED","ontology_id":"CHEBI:63940","preferred_term":"Na2WO4"}],"identifier":"CHEBI:63940","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":132,"edge_count":132,"occurrences":132},"occurrence_statistics":{"media_count":132,"total_occurrences":132},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:63940","ontology_label":"sodium tungstate","ontology_source":"CHEBI"},"preferred_term":"Na2WO4","sssom_rows":[{"data_row":2021,"object_id":"CHEBI:63940","object_label":"sodium tungstate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2wo4","synonym_count":4} |
| ev-0ba4f0cfb82b3630 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1512] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-b009e5abf128389f | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Na2wo4; data-row positions=[2021] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2021,"object_id":"CHEBI:63940","object_label":"sodium tungstate","other":"disodium tungstate&#124;Na2WO4 (10 mM)&#124;CAS:13472-45-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Na2wo4","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-8dc7c7c2d52907fc | docs/data/mapped_ingredients.csv; CSV lines=[1514] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:63940","line":1514,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"132","ontology_id":"CHEBI:63940","preferred_term":"Na2WO4","total_occurrences":"132"}] |
| ev-5204a1c6a62efe5d | reports/yaml_record_review/Na2wo4.md; &#96;data/ingredients/mapped/Na2wo4.yaml&#96;:2; Verdict:4; Identity:11; Validation:20; Evidence:28; Completeness:42; Recommended Edits:50 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-3ba17091c14c81f3 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1018] | context_only | [{"current_record_sha256":"3fe854c3fabbea1841a8ca55ce42dcc9ed82015af31d2e636d0e86a5a48ec25a","finding_id":"SEM:45c1dcc025550a0c8d48","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-na2wo4
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Na2wo4 (data/ingredients/mapped/Na2wo4.yaml)'
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
summary: Per-record structured review for Na2wo4 (data/ingredients/mapped/Na2wo4.yaml,
  record-72fc6ab22e3eb78d, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Na2wo4.yaml
    sha256: 3fe854c3fabbea1841a8ca55ce42dcc9ed82015af31d2e636d0e86a5a48ec25a
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
  - path: reports/yaml_record_review/Na2wo4.md
    sha256: de407693711154a7b4a1bff2c9cd1a540eab7a238eadace1061652808820bce4
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-72fc6ab22e3eb78d
  path: data/ingredients/mapped/Na2wo4.yaml
  label: Na2wo4
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2wo4.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Na2wo4.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Na2wo4.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-72fc6ab22e3eb78d
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-72fc6ab22e3eb78d
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-72fc6ab22e3eb78d
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-72fc6ab22e3eb78d
evidence:
- evidence_id: ev-64eb7d68adae72d4
  kind: record_content
  reference: data/ingredients/mapped/Na2wo4.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1512],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:63940","line":1514,"mapping_status":"MAPPED","ontology_id":"CHEBI:63940","preferred_term":"Na2WO4"}],"identifier":"CHEBI:63940","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":132,"edge_count":132,"occurrences":132},"occurrence_statistics":{"media_count":132,"total_occurrences":132},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:63940","ontology_label":"sodium
    tungstate","ontology_source":"CHEBI"},"preferred_term":"Na2WO4","sssom_rows":[{"data_row":2021,"object_id":"CHEBI:63940","object_label":"sodium
    tungstate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2wo4","synonym_count":4}'
  snapshot_sha256: 3fe854c3fabbea1841a8ca55ce42dcc9ed82015af31d2e636d0e86a5a48ec25a
- evidence_id: ev-0ba4f0cfb82b3630
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1512]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-b009e5abf128389f
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Na2wo4; data-row positions=[2021]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2021,"object_id":"CHEBI:63940","object_label":"sodium
    tungstate","other":"disodium tungstate|Na2WO4 (10 mM)|CAS:13472-45-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Na2wo4","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-8dc7c7c2d52907fc
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1514]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:63940","line":1514,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"132","ontology_id":"CHEBI:63940","preferred_term":"Na2WO4","total_occurrences":"132"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-5204a1c6a62efe5d
  kind: prior_review
  reference: reports/yaml_record_review/Na2wo4.md
  locator: '`data/ingredients/mapped/Na2wo4.yaml`:2; Verdict:4; Identity:11; Validation:20;
    Evidence:28; Completeness:42; Recommended Edits:50'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: de407693711154a7b4a1bff2c9cd1a540eab7a238eadace1061652808820bce4
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Na2wo4.yaml`, demote\
    \ or reject\n  `Na2WO4 (10 mM)` so it no longer publishes as an exact `CHEBI:63940`\n\
    \  synonym. Rebuild final SSSOM and rerun final SSSOM validation plus product\n\
    \  label validation."
- evidence_id: ev-3ba17091c14c81f3
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1018]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"3fe854c3fabbea1841a8ca55ce42dcc9ed82015af31d2e636d0e86a5a48ec25a","finding_id":"SEM:45c1dcc025550a0c8d48","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-f8ce058196ef6d46
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-72fc6ab22e3eb78d
  evidence_ids:
  - ev-64eb7d68adae72d4
  - ev-0ba4f0cfb82b3630
  - ev-b009e5abf128389f
  - ev-8dc7c7c2d52907fc
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-053eae2022c7c9f5
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-72fc6ab22e3eb78d
  evidence_ids:
  - ev-5204a1c6a62efe5d
  - ev-64eb7d68adae72d4
  - ev-3ba17091c14c81f3
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:39:25Z;
    reviewed SHA-256=3fe854c3fabbea1841a8ca55ce42dcc9ed82015af31d2e636d0e86a5a48ec25a;
    current SHA-256=3fe854c3fabbea1841a8ca55ce42dcc9ed82015af31d2e636d0e86a5a48ec25a;
    hash_changed=False. Reports=["reports/yaml_record_review/Na2wo4.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI:63940 sodium
    tungstate identity passes, but final other has a concentration-qualified label.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-5204a1c6a62efe5d
    - ev-64eb7d68adae72d4
  - name: legacy-native-ids
    value: '["SEM:45c1dcc025550a0c8d48"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-64eb7d68adae72d4
    - ev-5204a1c6a62efe5d
    - ev-3ba17091c14c81f3
findings:
- finding_id: rec-f-fc1c1d097381ff13
  issue_key: mim-reconciliation-historical-review-coverage-and-r-72fc6ab22e3eb78d
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Na2wo4'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:39:25Z;
    reviewed SHA-256=3fe854c3fabbea1841a8ca55ce42dcc9ed82015af31d2e636d0e86a5a48ec25a;
    current SHA-256=3fe854c3fabbea1841a8ca55ce42dcc9ed82015af31d2e636d0e86a5a48ec25a;
    hash_changed=False. Reports=["reports/yaml_record_review/Na2wo4.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI:63940 sodium
    tungstate identity passes, but final other has a concentration-qualified label.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-72fc6ab22e3eb78d
  evidence_ids:
  - ev-5204a1c6a62efe5d
  - ev-64eb7d68adae72d4
  - ev-3ba17091c14c81f3
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2wo4.yaml
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
