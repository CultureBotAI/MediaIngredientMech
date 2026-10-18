# Per-record structured review: Srcl2_X_6_H2o (data/ingredients/mapped/Srcl2_X_6_H2o.yaml)

- Review: 20261017T083000Z-srcl2-x-6-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Srcl2_X_6_H2o (data/ingredients/mapped/Srcl2_X_6_H2o.yaml, record-edb69fb35eaf3b37, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Srcl2_X_6_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Srcl2_X_6_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-edb69fb35eaf3b37 | data/ingredients/mapped/Srcl2_X_6_H2o.yaml | maintained | Srcl2_X_6_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-edb69fb35eaf3b37 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-edb69fb35eaf3b37 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-edb69fb35eaf3b37 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-edb69fb35eaf3b37.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-edb69fb35eaf3b37.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:23:59Z; reviewed SHA-256=2a0c4904c8905c7d5fad50026359115047f4132963cdbf77758399649085cd91; current SHA-256=2a0c4904c8905c7d5fad50026359115047f4132963cdbf77758399649085cd91; hash_changed=False. Reports=["reports/yaml_record_review/Srcl2_X_6_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The strontium hexahydrate row exports a 0.1% w/v source label as a hydrate synonym.

## Findings

### rec-f-4d9d16fb343ea724: Historical review coverage and residual narrative: Srcl2_X_6_H2o

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-edb69fb35eaf3b37.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:23:59Z; reviewed SHA-256=2a0c4904c8905c7d5fad50026359115047f4132963cdbf77758399649085cd91; current SHA-256=2a0c4904c8905c7d5fad50026359115047f4132963cdbf77758399649085cd91; hash_changed=False. Reports=["reports/yaml_record_review/Srcl2_X_6_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The strontium hexahydrate row exports a 0.1% w/v source label as a hydrate synonym.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-83065f3796452792 | data/ingredients/mapped/Srcl2_X_6_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1893],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:36385","line":1895,"mapping_status":"MAPPED","ontology_id":"CHEBI:36385","preferred_term":"SrCl2 x 6 H2O"}],"identifier":"CHEBI:36385","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":230,"edge_count":230,"occurrences":230},"occurrence_statistics":{"media_count":230,"total_occurrences":230},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:36385","ontology_label":"strontium dichloride hexahydrate","ontology_source":"CHEBI"},"preferred_term":"SrCl2 x 6 H2O","sssom_rows":[{"data_row":2639,"object_id":"CHEBI:36385","object_label":"strontium dichloride hexahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Srcl2_X_6_H2o","synonym_count":10} |
| ev-41ec6c8f3d3c5251 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1893] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-514c6498ffb7b76a | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Srcl2_X_6_H2o; data-row positions=[2639] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2639,"object_id":"CHEBI:36385","object_label":"strontium dichloride hexahydrate","other":"SrCl2 . 6H2O&#124;SrCl2 x 6 H2O (0.1% w/v)&#124;SrCl2.6H2O&#124;SrCl2\u00b76H2O&#124;SrCl2\u30fb6H2O&#124;Strontium chloride hexahydrate&#124;strontium dichloride--water (1/6)&#124;CAS:10025-70-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Srcl2_X_6_H2o","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-b4cc8bee59f70bf8 | docs/data/mapped_ingredients.csv; CSV lines=[1895] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:36385","line":1895,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"230","ontology_id":"CHEBI:36385","preferred_term":"SrCl2 x 6 H2O","total_occurrences":"230"}] |
| ev-1a9cfb5ba34fc747 | reports/yaml_record_review/Srcl2_X_6_H2o.md; &#96;data/ingredients/mapped/Srcl2_X_6_H2o.yaml&#96;:2; Verdict:4; Identity:10; Validation:22; Evidence:31; Completeness:47; Recommended Edits:54 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-f53d8787ffa92637 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1245] | context_only | [{"current_record_sha256":"2a0c4904c8905c7d5fad50026359115047f4132963cdbf77758399649085cd91","finding_id":"SEM:1966ee6923e7a6e88a05","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-srcl2-x-6-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Srcl2_X_6_H2o (data/ingredients/mapped/Srcl2_X_6_H2o.yaml)'
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
summary: Per-record structured review for Srcl2_X_6_H2o (data/ingredients/mapped/Srcl2_X_6_H2o.yaml,
  record-edb69fb35eaf3b37, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Srcl2_X_6_H2o.yaml
    sha256: 2a0c4904c8905c7d5fad50026359115047f4132963cdbf77758399649085cd91
    role: target
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
    sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
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
  - path: reports/yaml_record_review/Srcl2_X_6_H2o.md
    sha256: 92ace2b47addc2938dfd087d2ce8ae398463042c5d64316ae1904a0602ae54e1
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-edb69fb35eaf3b37
  path: data/ingredients/mapped/Srcl2_X_6_H2o.yaml
  label: Srcl2_X_6_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Srcl2_X_6_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Srcl2_X_6_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Srcl2_X_6_H2o.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-edb69fb35eaf3b37
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-edb69fb35eaf3b37
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-edb69fb35eaf3b37
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-edb69fb35eaf3b37
evidence:
- evidence_id: ev-83065f3796452792
  kind: record_content
  reference: data/ingredients/mapped/Srcl2_X_6_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1893],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:36385","line":1895,"mapping_status":"MAPPED","ontology_id":"CHEBI:36385","preferred_term":"SrCl2
    x 6 H2O"}],"identifier":"CHEBI:36385","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":230,"edge_count":230,"occurrences":230},"occurrence_statistics":{"media_count":230,"total_occurrences":230},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:36385","ontology_label":"strontium
    dichloride hexahydrate","ontology_source":"CHEBI"},"preferred_term":"SrCl2 x 6
    H2O","sssom_rows":[{"data_row":2639,"object_id":"CHEBI:36385","object_label":"strontium
    dichloride hexahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Srcl2_X_6_H2o","synonym_count":10}'
  snapshot_sha256: 2a0c4904c8905c7d5fad50026359115047f4132963cdbf77758399649085cd91
- evidence_id: ev-41ec6c8f3d3c5251
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1893]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-514c6498ffb7b76a
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Srcl2_X_6_H2o; data-row positions=[2639]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2639,"object_id":"CHEBI:36385","object_label":"strontium
    dichloride hexahydrate","other":"SrCl2 . 6H2O|SrCl2 x 6 H2O (0.1% w/v)|SrCl2.6H2O|SrCl2\u00b76H2O|SrCl2\u30fb6H2O|Strontium
    chloride hexahydrate|strontium dichloride--water (1/6)|CAS:10025-70-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Srcl2_X_6_H2o","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-b4cc8bee59f70bf8
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1895]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:36385","line":1895,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"230","ontology_id":"CHEBI:36385","preferred_term":"SrCl2
    x 6 H2O","total_occurrences":"230"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-1a9cfb5ba34fc747
  kind: prior_review
  reference: reports/yaml_record_review/Srcl2_X_6_H2o.md
  locator: '`data/ingredients/mapped/Srcl2_X_6_H2o.yaml`:2; Verdict:4; Identity:10;
    Validation:22; Evidence:31; Completeness:47; Recommended Edits:54'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 92ace2b47addc2938dfd087d2ce8ae398463042c5d64316ae1904a0602ae54e1
  quote: "Recommended Edits:\n- Major: remove `SrCl2 x 6 H2O (0.1% w/v)` from\n  `data/ingredients/mapped/Srcl2_X_6_H2o.yaml`\
    \ or retype it as non-exported\n  source provenance so SSSOM `other` contains\
    \ only dry-hexahydrate labels."
- evidence_id: ev-f53d8787ffa92637
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1245]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"2a0c4904c8905c7d5fad50026359115047f4132963cdbf77758399649085cd91","finding_id":"SEM:1966ee6923e7a6e88a05","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-4cb51df2b7d77332
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-edb69fb35eaf3b37
  evidence_ids:
  - ev-83065f3796452792
  - ev-41ec6c8f3d3c5251
  - ev-514c6498ffb7b76a
  - ev-b4cc8bee59f70bf8
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-5090d5430dc63fa6
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-edb69fb35eaf3b37
  evidence_ids:
  - ev-1a9cfb5ba34fc747
  - ev-83065f3796452792
  - ev-f53d8787ffa92637
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:23:59Z;
    reviewed SHA-256=2a0c4904c8905c7d5fad50026359115047f4132963cdbf77758399649085cd91;
    current SHA-256=2a0c4904c8905c7d5fad50026359115047f4132963cdbf77758399649085cd91;
    hash_changed=False. Reports=["reports/yaml_record_review/Srcl2_X_6_H2o.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The strontium hexahydrate
    row exports a 0.1% w/v source label as a hydrate synonym.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-1a9cfb5ba34fc747
    - ev-83065f3796452792
  - name: legacy-native-ids
    value: '["SEM:1966ee6923e7a6e88a05"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-83065f3796452792
    - ev-1a9cfb5ba34fc747
    - ev-f53d8787ffa92637
findings:
- finding_id: rec-f-4d9d16fb343ea724
  issue_key: mim-reconciliation-historical-review-coverage-and-r-edb69fb35eaf3b37
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Srcl2_X_6_H2o'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:23:59Z;
    reviewed SHA-256=2a0c4904c8905c7d5fad50026359115047f4132963cdbf77758399649085cd91;
    current SHA-256=2a0c4904c8905c7d5fad50026359115047f4132963cdbf77758399649085cd91;
    hash_changed=False. Reports=["reports/yaml_record_review/Srcl2_X_6_H2o.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The strontium hexahydrate
    row exports a 0.1% w/v source label as a hydrate synonym.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-edb69fb35eaf3b37
  evidence_ids:
  - ev-1a9cfb5ba34fc747
  - ev-83065f3796452792
  - ev-f53d8787ffa92637
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Srcl2_X_6_H2o.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.
```
