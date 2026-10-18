# Per-record structured review: Na2haso4_X_7_H2o (data/ingredients/mapped/Na2haso4_X_7_H2o.yaml)

- Review: 20261017T083000Z-na2haso4-x-7-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Na2haso4_X_7_H2o (data/ingredients/mapped/Na2haso4_X_7_H2o.yaml, record-5d500020f3d47fe1, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Na2haso4_X_7_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Na2haso4_X_7_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-5d500020f3d47fe1 | data/ingredients/mapped/Na2haso4_X_7_H2o.yaml | maintained | Na2haso4_X_7_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-5d500020f3d47fe1 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-5d500020f3d47fe1 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-5d500020f3d47fe1 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-5d500020f3d47fe1.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-5d500020f3d47fe1.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:14:57Z; reviewed SHA-256=c377e758d697bfe07475c192cd19c995a822691f0e6862c0ffc25ff739b3facc; current SHA-256=c377e758d697bfe07475c192cd19c995a822691f0e6862c0ffc25ff739b3facc; hash_changed=False. Reports=["reports/yaml_record_review/Na2haso4_X_7_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:91257 heptahydrate identity passes, but malformed and anhydrous formula tokens still publish as synonyms.

## Findings

### rec-f-789d22b6b646800f: Historical review coverage and residual narrative: Na2haso4_X_7_H2o

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-5d500020f3d47fe1.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:14:57Z; reviewed SHA-256=c377e758d697bfe07475c192cd19c995a822691f0e6862c0ffc25ff739b3facc; current SHA-256=c377e758d697bfe07475c192cd19c995a822691f0e6862c0ffc25ff739b3facc; hash_changed=False. Reports=["reports/yaml_record_review/Na2haso4_X_7_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:91257 heptahydrate identity passes, but malformed and anhydrous formula tokens still publish as synonyms.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-ca127b9cb00d2633 | data/ingredients/mapped/Na2haso4_X_7_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1487],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:91257","line":1489,"mapping_status":"MAPPED","ontology_id":"CHEBI:91257","preferred_term":"Na2HAsO4 x 7 H2O"}],"identifier":"CHEBI:91257","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":14,"edge_count":14,"occurrences":14},"occurrence_statistics":{"media_count":14,"total_occurrences":14},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:91257","ontology_label":"disodium hydrogenarsenate heptahydrate","ontology_source":"CHEBI"},"preferred_term":"Na2HAsO4 x 7 H2O","sssom_rows":[{"data_row":1995,"object_id":"CHEBI:91257","object_label":"disodium hydrogenarsenate heptahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2haso4_X_7_H2o","synonym_count":12} |
| ev-7eccc95023a68ed4 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1487] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-54fff2922f3ff63b | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Na2haso4_X_7_H2o; data-row positions=[1995] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1995,"object_id":"CHEBI:91257","object_label":"disodium hydrogenarsenate heptahydrate","other":"Dibasic sodium arsenate heptahydrate&#124;Disodium acid arsenate heptahydrate&#124;Disodium monohydrogen arsenate heptahydrate&#124;Hydrogen disodium arsenate heptahydrate&#124;NaHAsO4.7H2O&#124;Sodium acid arsenate, heptahydrate&#124;Sodium hydrogen arsenate heptahydrate&#124;Sodium orthoarsenate heptahydrate&#124;disodium arsenate heptahydrate&#124;disodium hydrogen arsorate--water (1/7)&#124;Na2HAsO4&#124;CAS:10048-95-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Na2haso4_X_7_H2o","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-05a348df44f3290f | docs/data/mapped_ingredients.csv; CSV lines=[1489] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:91257","line":1489,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"14","ontology_id":"CHEBI:91257","preferred_term":"Na2HAsO4 x 7 H2O","total_occurrences":"14"}] |
| ev-660fc62af7975d29 | reports/yaml_record_review/Na2haso4_X_7_H2o.md; &#96;data/ingredients/mapped/Na2haso4_X_7_H2o.yaml&#96;:2; Verdict:4; Identity:12; Validation:22; Evidence:30; Completeness:43; Recommended Edits:50 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-f9223b92e0e13b7d | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[994] | context_only | [{"current_record_sha256":"c377e758d697bfe07475c192cd19c995a822691f0e6862c0ffc25ff739b3facc","finding_id":"SEM:b3fa4fe961a6e676262a","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-na2haso4-x-7-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Na2haso4_X_7_H2o (data/ingredients/mapped/Na2haso4_X_7_H2o.yaml)'
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
summary: Per-record structured review for Na2haso4_X_7_H2o (data/ingredients/mapped/Na2haso4_X_7_H2o.yaml,
  record-5d500020f3d47fe1, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Na2haso4_X_7_H2o.yaml
    sha256: c377e758d697bfe07475c192cd19c995a822691f0e6862c0ffc25ff739b3facc
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
  - path: reports/yaml_record_review/Na2haso4_X_7_H2o.md
    sha256: 8b92f00c15f061ba6083963929e9c37150707fd4c75bbe1433f156512ae3fad6
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-5d500020f3d47fe1
  path: data/ingredients/mapped/Na2haso4_X_7_H2o.yaml
  label: Na2haso4_X_7_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2haso4_X_7_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Na2haso4_X_7_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Na2haso4_X_7_H2o.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-5d500020f3d47fe1
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-5d500020f3d47fe1
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-5d500020f3d47fe1
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-5d500020f3d47fe1
evidence:
- evidence_id: ev-ca127b9cb00d2633
  kind: record_content
  reference: data/ingredients/mapped/Na2haso4_X_7_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1487],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:91257","line":1489,"mapping_status":"MAPPED","ontology_id":"CHEBI:91257","preferred_term":"Na2HAsO4
    x 7 H2O"}],"identifier":"CHEBI:91257","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":14,"edge_count":14,"occurrences":14},"occurrence_statistics":{"media_count":14,"total_occurrences":14},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:91257","ontology_label":"disodium
    hydrogenarsenate heptahydrate","ontology_source":"CHEBI"},"preferred_term":"Na2HAsO4
    x 7 H2O","sssom_rows":[{"data_row":1995,"object_id":"CHEBI:91257","object_label":"disodium
    hydrogenarsenate heptahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2haso4_X_7_H2o","synonym_count":12}'
  snapshot_sha256: c377e758d697bfe07475c192cd19c995a822691f0e6862c0ffc25ff739b3facc
- evidence_id: ev-7eccc95023a68ed4
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1487]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-54fff2922f3ff63b
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Na2haso4_X_7_H2o; data-row positions=[1995]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1995,"object_id":"CHEBI:91257","object_label":"disodium
    hydrogenarsenate heptahydrate","other":"Dibasic sodium arsenate heptahydrate|Disodium
    acid arsenate heptahydrate|Disodium monohydrogen arsenate heptahydrate|Hydrogen
    disodium arsenate heptahydrate|NaHAsO4.7H2O|Sodium acid arsenate, heptahydrate|Sodium
    hydrogen arsenate heptahydrate|Sodium orthoarsenate heptahydrate|disodium arsenate
    heptahydrate|disodium hydrogen arsorate--water (1/7)|Na2HAsO4|CAS:10048-95-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Na2haso4_X_7_H2o","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-05a348df44f3290f
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1489]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:91257","line":1489,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"14","ontology_id":"CHEBI:91257","preferred_term":"Na2HAsO4
    x 7 H2O","total_occurrences":"14"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-660fc62af7975d29
  kind: prior_review
  reference: reports/yaml_record_review/Na2haso4_X_7_H2o.md
  locator: '`data/ingredients/mapped/Na2haso4_X_7_H2o.yaml`:2; Verdict:4; Identity:12;
    Validation:22; Evidence:30; Completeness:43; Recommended Edits:50'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 8b92f00c15f061ba6083963929e9c37150707fd4c75bbe1433f156512ae3fad6
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Na2haso4_X_7_H2o.yaml`,\
    \ mark the\n  one-sodium heptahydrate and anhydrous formula tokens as `REJECTED_LABEL`\
    \ or\n  otherwise keep them provenance-only, then rebuild final SSSOM and rerun\
    \ the\n  final SSSOM plus product label validators."
- evidence_id: ev-f9223b92e0e13b7d
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[994]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"c377e758d697bfe07475c192cd19c995a822691f0e6862c0ffc25ff739b3facc","finding_id":"SEM:b3fa4fe961a6e676262a","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-23c1c4e933bfbdf2
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-5d500020f3d47fe1
  evidence_ids:
  - ev-ca127b9cb00d2633
  - ev-7eccc95023a68ed4
  - ev-54fff2922f3ff63b
  - ev-05a348df44f3290f
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-fa9217a069f26c70
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-5d500020f3d47fe1
  evidence_ids:
  - ev-660fc62af7975d29
  - ev-ca127b9cb00d2633
  - ev-f9223b92e0e13b7d
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:14:57Z;
    reviewed SHA-256=c377e758d697bfe07475c192cd19c995a822691f0e6862c0ffc25ff739b3facc;
    current SHA-256=c377e758d697bfe07475c192cd19c995a822691f0e6862c0ffc25ff739b3facc;
    hash_changed=False. Reports=["reports/yaml_record_review/Na2haso4_X_7_H2o.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:91257 heptahydrate identity passes, but malformed and anhydrous formula
    tokens still publish as synonyms.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-660fc62af7975d29
    - ev-ca127b9cb00d2633
  - name: legacy-native-ids
    value: '["SEM:b3fa4fe961a6e676262a"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-ca127b9cb00d2633
    - ev-660fc62af7975d29
    - ev-f9223b92e0e13b7d
findings:
- finding_id: rec-f-789d22b6b646800f
  issue_key: mim-reconciliation-historical-review-coverage-and-r-5d500020f3d47fe1
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Na2haso4_X_7_H2o'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:14:57Z;
    reviewed SHA-256=c377e758d697bfe07475c192cd19c995a822691f0e6862c0ffc25ff739b3facc;
    current SHA-256=c377e758d697bfe07475c192cd19c995a822691f0e6862c0ffc25ff739b3facc;
    hash_changed=False. Reports=["reports/yaml_record_review/Na2haso4_X_7_H2o.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:91257 heptahydrate identity passes, but malformed and anhydrous formula
    tokens still publish as synonyms.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-5d500020f3d47fe1
  evidence_ids:
  - ev-660fc62af7975d29
  - ev-ca127b9cb00d2633
  - ev-f9223b92e0e13b7d
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2haso4_X_7_H2o.yaml
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
