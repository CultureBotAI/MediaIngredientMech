# Per-record structured review: Navo3 (data/ingredients/mapped/Navo3.yaml)

- Review: 20261017T083000Z-navo3
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Navo3 (data/ingredients/mapped/Navo3.yaml, record-2c4799e33df88fc4, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Navo3.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Navo3.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-2c4799e33df88fc4 | data/ingredients/mapped/Navo3.yaml | maintained | Navo3 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-2c4799e33df88fc4 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-2c4799e33df88fc4 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-2c4799e33df88fc4 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-2c4799e33df88fc4.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-2c4799e33df88fc4.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T06:11:55Z; reviewed SHA-256=022bb56159ebab55f1511533a72e5549ff43bcdd09de227f1fb193df2475eb78; current SHA-256=022bb56159ebab55f1511533a72e5549ff43bcdd09de227f1fb193df2475eb78; hash_changed=False. Reports=["reports/yaml_record_review/Navo3.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:75221 sodium metavanadate identity passes, but TRACE_ELEMENT is over-derived from generic Mineral role text.

## Findings

### rec-f-b04906e1d2d9b0bc: Historical review coverage and residual narrative: Navo3

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-2c4799e33df88fc4.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T06:11:55Z; reviewed SHA-256=022bb56159ebab55f1511533a72e5549ff43bcdd09de227f1fb193df2475eb78; current SHA-256=022bb56159ebab55f1511533a72e5549ff43bcdd09de227f1fb193df2475eb78; hash_changed=False. Reports=["reports/yaml_record_review/Navo3.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:75221 sodium metavanadate identity passes, but TRACE_ELEMENT is over-derived from generic Mineral role text.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-553f97d68d0bf778 | data/ingredients/mapped/Navo3.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1537],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:75221","line":1539,"mapping_status":"MAPPED","ontology_id":"CHEBI:75221","preferred_term":"NaVO3"}],"identifier":"CHEBI:75221","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7,"edge_count":7,"occurrences":7},"occurrence_statistics":{"media_count":7,"total_occurrences":7},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:75221","ontology_label":"sodium metavanadate","ontology_source":"CHEBI"},"preferred_term":"NaVO3","sssom_rows":[{"data_row":2051,"object_id":"CHEBI:75221","object_label":"sodium metavanadate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Navo3","synonym_count":6} |
| ev-a22d07a9ce18a951 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1537] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-1465d8e46495d695 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Navo3; data-row positions=[2051] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2051,"object_id":"CHEBI:75221","object_label":"sodium metavanadate","other":"Sodium trioxovanadate&#124;Vanadic acid, monosodium salt&#124;sodium oxido(dioxo)vanadium&#124;CAS:13718-26-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Navo3","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-9fc38dde7c4bf13a | docs/data/mapped_ingredients.csv; CSV lines=[1539] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:75221","line":1539,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"7","ontology_id":"CHEBI:75221","preferred_term":"NaVO3","total_occurrences":"7"}] |
| ev-46ba1d727dbf4f0d | reports/yaml_record_review/Navo3.md; &#96;data/ingredients/mapped/Navo3.yaml&#96;:2; Verdict:4; Identity:10; Validation:19; Evidence:26; Completeness:41; Recommended Edits:48 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-641d93aa31ebf58a | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1035] | context_only | [{"current_record_sha256":"022bb56159ebab55f1511533a72e5549ff43bcdd09de227f1fb193df2475eb78","finding_id":"SEM:d6abba971c83a5f5ebd3","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-navo3
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Navo3 (data/ingredients/mapped/Navo3.yaml)'
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
summary: Per-record structured review for Navo3 (data/ingredients/mapped/Navo3.yaml,
  record-2c4799e33df88fc4, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Navo3.yaml
    sha256: 022bb56159ebab55f1511533a72e5549ff43bcdd09de227f1fb193df2475eb78
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
  - path: reports/yaml_record_review/Navo3.md
    sha256: 2dbce8a31423a130e868149625762f38087a65be8180ae45554616e1ec1c7906
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-2c4799e33df88fc4
  path: data/ingredients/mapped/Navo3.yaml
  label: Navo3
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Navo3.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Navo3.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Navo3.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-2c4799e33df88fc4
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-2c4799e33df88fc4
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-2c4799e33df88fc4
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-2c4799e33df88fc4
evidence:
- evidence_id: ev-553f97d68d0bf778
  kind: record_content
  reference: data/ingredients/mapped/Navo3.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1537],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:75221","line":1539,"mapping_status":"MAPPED","ontology_id":"CHEBI:75221","preferred_term":"NaVO3"}],"identifier":"CHEBI:75221","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7,"edge_count":7,"occurrences":7},"occurrence_statistics":{"media_count":7,"total_occurrences":7},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:75221","ontology_label":"sodium
    metavanadate","ontology_source":"CHEBI"},"preferred_term":"NaVO3","sssom_rows":[{"data_row":2051,"object_id":"CHEBI:75221","object_label":"sodium
    metavanadate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Navo3","synonym_count":6}'
  snapshot_sha256: 022bb56159ebab55f1511533a72e5549ff43bcdd09de227f1fb193df2475eb78
- evidence_id: ev-a22d07a9ce18a951
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1537]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-1465d8e46495d695
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Navo3; data-row positions=[2051]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2051,"object_id":"CHEBI:75221","object_label":"sodium
    metavanadate","other":"Sodium trioxovanadate|Vanadic acid, monosodium salt|sodium
    oxido(dioxo)vanadium|CAS:13718-26-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Navo3","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-9fc38dde7c4bf13a
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1539]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:75221","line":1539,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"7","ontology_id":"CHEBI:75221","preferred_term":"NaVO3","total_occurrences":"7"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-46ba1d727dbf4f0d
  kind: prior_review
  reference: reports/yaml_record_review/Navo3.md
  locator: '`data/ingredients/mapped/Navo3.yaml`:2; Verdict:4; Identity:10; Validation:19;
    Evidence:26; Completeness:41; Recommended Edits:48'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 2dbce8a31423a130e868149625762f38087a65be8180ae45554616e1ec1c7906
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Navo3.yaml`, either\
    \ replace\n  `TRACE_ELEMENT` with a source-backed role that preserves the original\n\
    \  `Mineral` scope or add source evidence showing that sodium metavanadate is\
    \ a\n  trace-element ingredient in the source recipes."
- evidence_id: ev-641d93aa31ebf58a
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1035]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"022bb56159ebab55f1511533a72e5549ff43bcdd09de227f1fb193df2475eb78","finding_id":"SEM:d6abba971c83a5f5ebd3","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-a8946ea9d7b34f5b
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-2c4799e33df88fc4
  evidence_ids:
  - ev-553f97d68d0bf778
  - ev-a22d07a9ce18a951
  - ev-1465d8e46495d695
  - ev-9fc38dde7c4bf13a
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-40100447b8b2783d
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-2c4799e33df88fc4
  evidence_ids:
  - ev-46ba1d727dbf4f0d
  - ev-553f97d68d0bf778
  - ev-641d93aa31ebf58a
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T06:11:55Z;
    reviewed SHA-256=022bb56159ebab55f1511533a72e5549ff43bcdd09de227f1fb193df2475eb78;
    current SHA-256=022bb56159ebab55f1511533a72e5549ff43bcdd09de227f1fb193df2475eb78;
    hash_changed=False. Reports=["reports/yaml_record_review/Navo3.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI:75221 sodium
    metavanadate identity passes, but TRACE_ELEMENT is over-derived from generic Mineral
    role text.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-46ba1d727dbf4f0d
    - ev-553f97d68d0bf778
  - name: legacy-native-ids
    value: '["SEM:d6abba971c83a5f5ebd3"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-553f97d68d0bf778
    - ev-46ba1d727dbf4f0d
    - ev-641d93aa31ebf58a
findings:
- finding_id: rec-f-b04906e1d2d9b0bc
  issue_key: mim-reconciliation-historical-review-coverage-and-r-2c4799e33df88fc4
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Navo3'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T06:11:55Z;
    reviewed SHA-256=022bb56159ebab55f1511533a72e5549ff43bcdd09de227f1fb193df2475eb78;
    current SHA-256=022bb56159ebab55f1511533a72e5549ff43bcdd09de227f1fb193df2475eb78;
    hash_changed=False. Reports=["reports/yaml_record_review/Navo3.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI:75221 sodium
    metavanadate identity passes, but TRACE_ELEMENT is over-derived from generic Mineral
    role text.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-2c4799e33df88fc4
  evidence_ids:
  - ev-46ba1d727dbf4f0d
  - ev-553f97d68d0bf778
  - ev-641d93aa31ebf58a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Navo3.yaml
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
