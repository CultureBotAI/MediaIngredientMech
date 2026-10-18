# Per-record structured review: Pea (data/ingredients/mapped/Pea.yaml)

- Review: 20261017T083000Z-pea
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Pea (data/ingredients/mapped/Pea.yaml, record-c7ce3b14ab2792e8, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Pea.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Pea.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-c7ce3b14ab2792e8 | data/ingredients/mapped/Pea.yaml | maintained | Pea |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-c7ce3b14ab2792e8 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-c7ce3b14ab2792e8 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-c7ce3b14ab2792e8 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-c7ce3b14ab2792e8.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-c7ce3b14ab2792e8.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T08:43:36Z; reviewed SHA-256=5a54bdb7bf84d9b0db9cc7b32bf7d3263a55c390d9cb0048ae47c87ff9bf1b12; current SHA-256=5a54bdb7bf84d9b0db9cc7b32bf7d3263a55c390d9cb0048ae47c87ff9bf1b12; hash_changed=False. Reports=["reports/yaml_record_review/Pea.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact NCIT:C72056 identity passes, but final other exports recipe-order text.

## Findings

### rec-f-3004cbce1de8dfc3: Historical review coverage and residual narrative: Pea

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-c7ce3b14ab2792e8.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T08:43:36Z; reviewed SHA-256=5a54bdb7bf84d9b0db9cc7b32bf7d3263a55c390d9cb0048ae47c87ff9bf1b12; current SHA-256=5a54bdb7bf84d9b0db9cc7b32bf7d3263a55c390d9cb0048ae47c87ff9bf1b12; hash_changed=False. Reports=["reports/yaml_record_review/Pea.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact NCIT:C72056 identity passes, but final other exports recipe-order text.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-eaf27890401cd09c | data/ingredients/mapped/Pea.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1624],"raw_equal":true},"docs_rows":[{"identifier":"NCIT:C72056","line":1626,"mapping_status":"MAPPED","ontology_id":"NCIT:C72056","preferred_term":"Pea"}],"identifier":"NCIT:C72056","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"NCIT:C72056","ontology_label":"Pea","ontology_source":"NCIT"},"preferred_term":"Pea","sssom_rows":[{"data_row":2209,"object_id":"NCIT:C72056","object_label":"Pea","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Pea","synonym_count":2} |
| ev-ae34ee69a673802b | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1624] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-49b8888718130cb2 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Pea; data-row positions=[2209] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2209,"object_id":"NCIT:C72056","object_label":"Pea","other":"Pea(add after dH2O)","predicate_id":"skos:exactMatch","subject_id":"MIM:Pea","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-0cdcb66ec5ebbe1b | docs/data/mapped_ingredients.csv; CSV lines=[1626] | supports | Published identity and count rows inspected: [{"identifier":"NCIT:C72056","line":1626,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"NCIT:C72056","preferred_term":"Pea","total_occurrences":"2"}] |
| ev-2604c4c6f8f5fe3c | reports/yaml_record_review/Pea.md; &#96;data/ingredients/mapped/Pea.yaml&#96;:2; Verdict:4; Identity:9; Validation:18; Evidence:27; Completeness:35; Recommended Edits:41 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-828d0376f4a1f1f4 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1098] | context_only | [{"current_record_sha256":"5a54bdb7bf84d9b0db9cc7b32bf7d3263a55c390d9cb0048ae47c87ff9bf1b12","finding_id":"SEM:aac1109b73fbb43813a0","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-pea
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Pea (data/ingredients/mapped/Pea.yaml)'
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
summary: Per-record structured review for Pea (data/ingredients/mapped/Pea.yaml, record-c7ce3b14ab2792e8,
  mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound
  to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Pea.yaml
    sha256: 5a54bdb7bf84d9b0db9cc7b32bf7d3263a55c390d9cb0048ae47c87ff9bf1b12
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
  - path: reports/yaml_record_review/Pea.md
    sha256: 17d70ac8b34f731159e82fa6d39211e133f85eae4e3e5fc70293791befe534d6
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-c7ce3b14ab2792e8
  path: data/ingredients/mapped/Pea.yaml
  label: Pea
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Pea.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Pea.yaml covering
    current record state, role evidence support, published surfaces, and residual
    historical review claims.
  selection: Single record data/ingredients/mapped/Pea.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-c7ce3b14ab2792e8
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-c7ce3b14ab2792e8
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-c7ce3b14ab2792e8
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-c7ce3b14ab2792e8
evidence:
- evidence_id: ev-eaf27890401cd09c
  kind: record_content
  reference: data/ingredients/mapped/Pea.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1624],"raw_equal":true},"docs_rows":[{"identifier":"NCIT:C72056","line":1626,"mapping_status":"MAPPED","ontology_id":"NCIT:C72056","preferred_term":"Pea"}],"identifier":"NCIT:C72056","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"NCIT:C72056","ontology_label":"Pea","ontology_source":"NCIT"},"preferred_term":"Pea","sssom_rows":[{"data_row":2209,"object_id":"NCIT:C72056","object_label":"Pea","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Pea","synonym_count":2}'
  snapshot_sha256: 5a54bdb7bf84d9b0db9cc7b32bf7d3263a55c390d9cb0048ae47c87ff9bf1b12
- evidence_id: ev-ae34ee69a673802b
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1624]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-49b8888718130cb2
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Pea; data-row positions=[2209]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2209,"object_id":"NCIT:C72056","object_label":"Pea","other":"Pea(add
    after dH2O)","predicate_id":"skos:exactMatch","subject_id":"MIM:Pea","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-0cdcb66ec5ebbe1b
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1626]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"NCIT:C72056","line":1626,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"NCIT:C72056","preferred_term":"Pea","total_occurrences":"2"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-2604c4c6f8f5fe3c
  kind: prior_review
  reference: reports/yaml_record_review/Pea.md
  locator: '`data/ingredients/mapped/Pea.yaml`:2; Verdict:4; Identity:9; Validation:18;
    Evidence:27; Completeness:35; Recommended Edits:41'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 17d70ac8b34f731159e82fa6d39211e133f85eae4e3e5fc70293791befe534d6
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Pea.yaml`, retype\
    \ or suppress the\n  `Pea(add after dH2O)` raw synonym so it remains provenance\
    \ only and no longer\n  appears in `mappings/ingredient_mappings.sssom.tsv`. Rebuild\
    \ the final SSSOM\n  and rerun `scripts/validate_sssom_invariants.py`."
- evidence_id: ev-828d0376f4a1f1f4
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1098]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"5a54bdb7bf84d9b0db9cc7b32bf7d3263a55c390d9cb0048ae47c87ff9bf1b12","finding_id":"SEM:aac1109b73fbb43813a0","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-0a2f264ed785c756
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-c7ce3b14ab2792e8
  evidence_ids:
  - ev-eaf27890401cd09c
  - ev-ae34ee69a673802b
  - ev-49b8888718130cb2
  - ev-0cdcb66ec5ebbe1b
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-1a06cbb76c851521
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-c7ce3b14ab2792e8
  evidence_ids:
  - ev-2604c4c6f8f5fe3c
  - ev-eaf27890401cd09c
  - ev-828d0376f4a1f1f4
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T08:43:36Z;
    reviewed SHA-256=5a54bdb7bf84d9b0db9cc7b32bf7d3263a55c390d9cb0048ae47c87ff9bf1b12;
    current SHA-256=5a54bdb7bf84d9b0db9cc7b32bf7d3263a55c390d9cb0048ae47c87ff9bf1b12;
    hash_changed=False. Reports=["reports/yaml_record_review/Pea.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact NCIT:C72056 identity
    passes, but final other exports recipe-order text.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-2604c4c6f8f5fe3c
    - ev-eaf27890401cd09c
  - name: legacy-native-ids
    value: '["SEM:aac1109b73fbb43813a0"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-eaf27890401cd09c
    - ev-2604c4c6f8f5fe3c
    - ev-828d0376f4a1f1f4
findings:
- finding_id: rec-f-3004cbce1de8dfc3
  issue_key: mim-reconciliation-historical-review-coverage-and-r-c7ce3b14ab2792e8
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Pea'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T08:43:36Z;
    reviewed SHA-256=5a54bdb7bf84d9b0db9cc7b32bf7d3263a55c390d9cb0048ae47c87ff9bf1b12;
    current SHA-256=5a54bdb7bf84d9b0db9cc7b32bf7d3263a55c390d9cb0048ae47c87ff9bf1b12;
    hash_changed=False. Reports=["reports/yaml_record_review/Pea.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact NCIT:C72056 identity
    passes, but final other exports recipe-order text.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-c7ce3b14ab2792e8
  evidence_ids:
  - ev-2604c4c6f8f5fe3c
  - ev-eaf27890401cd09c
  - ev-828d0376f4a1f1f4
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Pea.yaml
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
