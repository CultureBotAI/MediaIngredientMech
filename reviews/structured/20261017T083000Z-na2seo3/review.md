# Per-record structured review: Na2seo3 (data/ingredients/mapped/Na2seo3.yaml)

- Review: 20261017T083000Z-na2seo3
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Na2seo3 (data/ingredients/mapped/Na2seo3.yaml, record-e13ee66355bbb0cf, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Na2seo3.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Na2seo3.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-e13ee66355bbb0cf | data/ingredients/mapped/Na2seo3.yaml | maintained | Na2seo3 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-e13ee66355bbb0cf | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-e13ee66355bbb0cf | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-e13ee66355bbb0cf | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-e13ee66355bbb0cf.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-e13ee66355bbb0cf.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:30:27Z; reviewed SHA-256=de098711130ca209fe06ee2a3239125f2aabb60c554830f93b2b24b72cc12cab; current SHA-256=de098711130ca209fe06ee2a3239125f2aabb60c554830f93b2b24b72cc12cab; hash_changed=False. Reports=["reports/yaml_record_review/Na2seo3.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:48843 disodium selenite identity passes, but final other publishes a garbled selenite formula.

## Findings

### rec-f-d01730a89495fd8c: Historical review coverage and residual narrative: Na2seo3

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-e13ee66355bbb0cf.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:30:27Z; reviewed SHA-256=de098711130ca209fe06ee2a3239125f2aabb60c554830f93b2b24b72cc12cab; current SHA-256=de098711130ca209fe06ee2a3239125f2aabb60c554830f93b2b24b72cc12cab; hash_changed=False. Reports=["reports/yaml_record_review/Na2seo3.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:48843 disodium selenite identity passes, but final other publishes a garbled selenite formula.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-4d22b7d149698f5c | data/ingredients/mapped/Na2seo3.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1503],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:48843","line":1505,"mapping_status":"MAPPED","ontology_id":"CHEBI:48843","preferred_term":"Na2SeO3"}],"identifier":"CHEBI:48843","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":185,"edge_count":185,"occurrences":185},"occurrence_statistics":{"media_count":185,"total_occurrences":185},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:48843","ontology_label":"disodium selenite","ontology_source":"CHEBI"},"preferred_term":"Na2SeO3","sssom_rows":[{"data_row":2013,"object_id":"CHEBI:48843","object_label":"disodium selenite","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2seo3","synonym_count":15} |
| ev-69c06f9986ed651f | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1503] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-574b63cd1e0c1ffe | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Na2seo3; data-row positions=[2013] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2013,"object_id":"CHEBI:48843","object_label":"disodium selenite","other":"Sodium selenite&#124;Natriumselenit&#124;disodium selenium trioxide&#124;selenious acid (H2SeO3) disodium salt&#124;selenious acid disodium salt&#124;selenious acid, disodium salt&#124;selenious acid, sodium salt (1:2)&#124;Na2Se2O3&#124;CAS:10102-18-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Na2seo3","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-09def1832344c6a8 | docs/data/mapped_ingredients.csv; CSV lines=[1505] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:48843","line":1505,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"185","ontology_id":"CHEBI:48843","preferred_term":"Na2SeO3","total_occurrences":"185"}] |
| ev-3acb1763a3260a12 | reports/yaml_record_review/Na2seo3.md; &#96;data/ingredients/mapped/Na2seo3.yaml&#96;:2; Verdict:4; Identity:11; Validation:20; Evidence:27; Completeness:45; Recommended Edits:53 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-1ded9d9f583f8a7c | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1009] | context_only | [{"current_record_sha256":"de098711130ca209fe06ee2a3239125f2aabb60c554830f93b2b24b72cc12cab","finding_id":"SEM:f9f4e26d79499739a271","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-na2seo3
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Na2seo3 (data/ingredients/mapped/Na2seo3.yaml)'
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
summary: Per-record structured review for Na2seo3 (data/ingredients/mapped/Na2seo3.yaml,
  record-e13ee66355bbb0cf, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Na2seo3.yaml
    sha256: de098711130ca209fe06ee2a3239125f2aabb60c554830f93b2b24b72cc12cab
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
  - path: reports/yaml_record_review/Na2seo3.md
    sha256: 98187c42b3cd99d0cafbdaec7dd827c839557537ff8cebd1e6020b1eb80c0b60
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-e13ee66355bbb0cf
  path: data/ingredients/mapped/Na2seo3.yaml
  label: Na2seo3
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2seo3.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Na2seo3.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Na2seo3.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-e13ee66355bbb0cf
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-e13ee66355bbb0cf
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-e13ee66355bbb0cf
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-e13ee66355bbb0cf
evidence:
- evidence_id: ev-4d22b7d149698f5c
  kind: record_content
  reference: data/ingredients/mapped/Na2seo3.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1503],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:48843","line":1505,"mapping_status":"MAPPED","ontology_id":"CHEBI:48843","preferred_term":"Na2SeO3"}],"identifier":"CHEBI:48843","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":185,"edge_count":185,"occurrences":185},"occurrence_statistics":{"media_count":185,"total_occurrences":185},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:48843","ontology_label":"disodium
    selenite","ontology_source":"CHEBI"},"preferred_term":"Na2SeO3","sssom_rows":[{"data_row":2013,"object_id":"CHEBI:48843","object_label":"disodium
    selenite","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2seo3","synonym_count":15}'
  snapshot_sha256: de098711130ca209fe06ee2a3239125f2aabb60c554830f93b2b24b72cc12cab
- evidence_id: ev-69c06f9986ed651f
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1503]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-574b63cd1e0c1ffe
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Na2seo3; data-row positions=[2013]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2013,"object_id":"CHEBI:48843","object_label":"disodium
    selenite","other":"Sodium selenite|Natriumselenit|disodium selenium trioxide|selenious
    acid (H2SeO3) disodium salt|selenious acid disodium salt|selenious acid, disodium
    salt|selenious acid, sodium salt (1:2)|Na2Se2O3|CAS:10102-18-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Na2seo3","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-09def1832344c6a8
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1505]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:48843","line":1505,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"185","ontology_id":"CHEBI:48843","preferred_term":"Na2SeO3","total_occurrences":"185"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-3acb1763a3260a12
  kind: prior_review
  reference: reports/yaml_record_review/Na2seo3.md
  locator: '`data/ingredients/mapped/Na2seo3.yaml`:2; Verdict:4; Identity:11; Validation:20;
    Evidence:27; Completeness:45; Recommended Edits:53'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 98187c42b3cd99d0cafbdaec7dd827c839557537ff8cebd1e6020b1eb80c0b60
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Na2seo3.yaml`,\
    \ demote `Na2Se2O3` from an\n  active `RAW_TEXT` synonym to typo/merge provenance\
    \ that does not export to\n  final SSSOM. Rebuild final SSSOM and rerun final\
    \ SSSOM validation plus\n  product label validation."
- evidence_id: ev-1ded9d9f583f8a7c
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1009]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"de098711130ca209fe06ee2a3239125f2aabb60c554830f93b2b24b72cc12cab","finding_id":"SEM:f9f4e26d79499739a271","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-07996ecf4d3e1391
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-e13ee66355bbb0cf
  evidence_ids:
  - ev-4d22b7d149698f5c
  - ev-69c06f9986ed651f
  - ev-574b63cd1e0c1ffe
  - ev-09def1832344c6a8
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-14c30b53bdecb4ff
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-e13ee66355bbb0cf
  evidence_ids:
  - ev-3acb1763a3260a12
  - ev-4d22b7d149698f5c
  - ev-1ded9d9f583f8a7c
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:30:27Z;
    reviewed SHA-256=de098711130ca209fe06ee2a3239125f2aabb60c554830f93b2b24b72cc12cab;
    current SHA-256=de098711130ca209fe06ee2a3239125f2aabb60c554830f93b2b24b72cc12cab;
    hash_changed=False. Reports=["reports/yaml_record_review/Na2seo3.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI:48843 disodium
    selenite identity passes, but final other publishes a garbled selenite formula.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-3acb1763a3260a12
    - ev-4d22b7d149698f5c
  - name: legacy-native-ids
    value: '["SEM:f9f4e26d79499739a271"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-4d22b7d149698f5c
    - ev-3acb1763a3260a12
    - ev-1ded9d9f583f8a7c
findings:
- finding_id: rec-f-d01730a89495fd8c
  issue_key: mim-reconciliation-historical-review-coverage-and-r-e13ee66355bbb0cf
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Na2seo3'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:30:27Z;
    reviewed SHA-256=de098711130ca209fe06ee2a3239125f2aabb60c554830f93b2b24b72cc12cab;
    current SHA-256=de098711130ca209fe06ee2a3239125f2aabb60c554830f93b2b24b72cc12cab;
    hash_changed=False. Reports=["reports/yaml_record_review/Na2seo3.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI:48843 disodium
    selenite identity passes, but final other publishes a garbled selenite formula.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-e13ee66355bbb0cf
  evidence_ids:
  - ev-3acb1763a3260a12
  - ev-4d22b7d149698f5c
  - ev-1ded9d9f583f8a7c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2seo3.yaml
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
