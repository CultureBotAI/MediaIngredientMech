# Per-record structured review: Potassium_Aluminum_Chloride (data/ingredients/mapped/Potassium_Aluminum_Chloride.yaml)

- Review: 20261017T083000Z-potassium-aluminum-chloride
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Potassium_Aluminum_Chloride (data/ingredients/mapped/Potassium_Aluminum_Chloride.yaml, record-da888d2c78859ee3, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Potassium_Aluminum_Chloride.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Potassium_Aluminum_Chloride.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-da888d2c78859ee3 | data/ingredients/mapped/Potassium_Aluminum_Chloride.yaml | maintained | Potassium_Aluminum_Chloride |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-da888d2c78859ee3 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-da888d2c78859ee3 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-da888d2c78859ee3 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-da888d2c78859ee3.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-da888d2c78859ee3.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T10:12:31Z; reviewed SHA-256=a257d091eac80a0ed11f02f15d3cd3dcc478d508af28d8aa58adfc0d96ebb0f1; current SHA-256=a257d091eac80a0ed11f02f15d3cd3dcc478d508af28d8aa58adfc0d96ebb0f1; hash_changed=False. Reports=["reports/yaml_record_review/Potassium_Aluminum_Chloride.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS and KG-Microbe identity rows pass, but the NCIT aluminum chloride parent is only substring-derived.

## Findings

### rec-f-7c6f62b14ecd985c: Historical review coverage and residual narrative: Potassium_Aluminum_Chloride

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-da888d2c78859ee3.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T10:12:31Z; reviewed SHA-256=a257d091eac80a0ed11f02f15d3cd3dcc478d508af28d8aa58adfc0d96ebb0f1; current SHA-256=a257d091eac80a0ed11f02f15d3cd3dcc478d508af28d8aa58adfc0d96ebb0f1; hash_changed=False. Reports=["reports/yaml_record_review/Potassium_Aluminum_Chloride.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS and KG-Microbe identity rows pass, but the NCIT aluminum chloride parent is only substring-derived.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-252e9f06fd3172a4 | data/ingredients/mapped/Potassium_Aluminum_Chloride.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1688],"raw_equal":true},"docs_rows":[{"identifier":"cas:74978-20-4","line":1690,"mapping_status":"MAPPED","ontology_id":"NCIT:C83530","preferred_term":"Potassium aluminum chloride"}],"identifier":"cas:74978-20-4","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1,"edge_count":1,"occurrences":1},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"NCIT:C83530","ontology_label":"Aluminum Chloride","ontology_source":"NCIT"},"preferred_term":"Potassium aluminum chloride","sssom_rows":[{"data_row":2314,"object_id":"NCIT:C83530","object_label":"Aluminum Chloride","predicate_id":"skos:broadMatch"},{"data_row":2315,"object_id":"cas:74978-20-4","object_label":"Potassium aluminum chloride","predicate_id":"skos:exactMatch"},{"data_row":2316,"object_id":"kgmicrobe.compound:potassium_aluminum_chloride","object_label":"Potassium aluminum chloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Potassium_Aluminum_Chloride","synonym_count":1} |
| ev-d05ab0ef2230c5b3 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1688] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-608cd16542960ba4 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Potassium_Aluminum_Chloride; data-row positions=[2314,2315,2316] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2314,"object_id":"NCIT:C83530","object_label":"Aluminum Chloride","other":"AlKCl2","predicate_id":"skos:broadMatch","subject_id":"MIM:Potassium_Aluminum_Chloride","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":2315,"object_id":"cas:74978-20-4","object_label":"Potassium aluminum chloride","other":"CAS:74978-20-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Potassium_Aluminum_Chloride","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"},{"data_row":2316,"object_id":"kgmicrobe.compound:potassium_aluminum_chloride","object_label":"Potassium aluminum chloride","other":"CAS:74978-20-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Potassium_Aluminum_Chloride","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-1e042d64b1cc8673 | docs/data/mapped_ingredients.csv; CSV lines=[1690] | supports | Published identity and count rows inspected: [{"identifier":"cas:74978-20-4","line":1690,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"NCIT:C83530","preferred_term":"Potassium aluminum chloride","total_occurrences":"1"}] |
| ev-1e065a61ad17c107 | reports/yaml_record_review/Potassium_Aluminum_Chloride.md; &#96;data/ingredients/mapped/Potassium_Aluminum_Chloride.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-c63fa68a3519da5d | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1135] | context_only | [{"current_record_sha256":"a257d091eac80a0ed11f02f15d3cd3dcc478d508af28d8aa58adfc0d96ebb0f1","finding_id":"SEM:3c2084bad0616037f2f5","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-potassium-aluminum-chloride
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Potassium_Aluminum_Chloride (data/ingredients/mapped/Potassium_Aluminum_Chloride.yaml)'
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
summary: Per-record structured review for Potassium_Aluminum_Chloride (data/ingredients/mapped/Potassium_Aluminum_Chloride.yaml,
  record-da888d2c78859ee3, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Potassium_Aluminum_Chloride.yaml
    sha256: a257d091eac80a0ed11f02f15d3cd3dcc478d508af28d8aa58adfc0d96ebb0f1
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
  - path: reports/yaml_record_review/Potassium_Aluminum_Chloride.md
    sha256: dfeec7205b9e5b51573ccfa3d9cc9069393a2bce5fabf4cedf2ca4980a67dc1d
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-da888d2c78859ee3
  path: data/ingredients/mapped/Potassium_Aluminum_Chloride.yaml
  label: Potassium_Aluminum_Chloride
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Potassium_Aluminum_Chloride.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Potassium_Aluminum_Chloride.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Potassium_Aluminum_Chloride.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-da888d2c78859ee3
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-da888d2c78859ee3
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-da888d2c78859ee3
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10
    and semantic review dispositions on HEAD.
  target_ids:
  - record-da888d2c78859ee3
evidence:
- evidence_id: ev-252e9f06fd3172a4
  kind: record_content
  reference: data/ingredients/mapped/Potassium_Aluminum_Chloride.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1688],"raw_equal":true},"docs_rows":[{"identifier":"cas:74978-20-4","line":1690,"mapping_status":"MAPPED","ontology_id":"NCIT:C83530","preferred_term":"Potassium
    aluminum chloride"}],"identifier":"cas:74978-20-4","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1,"edge_count":1,"occurrences":1},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"NCIT:C83530","ontology_label":"Aluminum
    Chloride","ontology_source":"NCIT"},"preferred_term":"Potassium aluminum chloride","sssom_rows":[{"data_row":2314,"object_id":"NCIT:C83530","object_label":"Aluminum
    Chloride","predicate_id":"skos:broadMatch"},{"data_row":2315,"object_id":"cas:74978-20-4","object_label":"Potassium
    aluminum chloride","predicate_id":"skos:exactMatch"},{"data_row":2316,"object_id":"kgmicrobe.compound:potassium_aluminum_chloride","object_label":"Potassium
    aluminum chloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Potassium_Aluminum_Chloride","synonym_count":1}'
  snapshot_sha256: a257d091eac80a0ed11f02f15d3cd3dcc478d508af28d8aa58adfc0d96ebb0f1
- evidence_id: ev-d05ab0ef2230c5b3
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1688]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-608cd16542960ba4
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Potassium_Aluminum_Chloride; data-row positions=[2314,2315,2316]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2314,"object_id":"NCIT:C83530","object_label":"Aluminum
    Chloride","other":"AlKCl2","predicate_id":"skos:broadMatch","subject_id":"MIM:Potassium_Aluminum_Chloride","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":2315,"object_id":"cas:74978-20-4","object_label":"Potassium
    aluminum chloride","other":"CAS:74978-20-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Potassium_Aluminum_Chloride","validation_method":"none|UNKNOWN_TERM|2026-07-07"},{"data_row":2316,"object_id":"kgmicrobe.compound:potassium_aluminum_chloride","object_label":"Potassium
    aluminum chloride","other":"CAS:74978-20-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Potassium_Aluminum_Chloride","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-1e042d64b1cc8673
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1690]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:74978-20-4","line":1690,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"NCIT:C83530","preferred_term":"Potassium
    aluminum chloride","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-1e065a61ad17c107
  kind: prior_review
  reference: reports/yaml_record_review/Potassium_Aluminum_Chloride.md
  locator: '`data/ingredients/mapped/Potassium_Aluminum_Chloride.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: dfeec7205b9e5b51573ccfa3d9cc9069393a2bce5fabf4cedf2ca4980a67dc1d
- evidence_id: ev-c63fa68a3519da5d
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1135]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"a257d091eac80a0ed11f02f15d3cd3dcc478d508af28d8aa58adfc0d96ebb0f1","finding_id":"SEM:3c2084bad0616037f2f5","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-bd12b6d6522cf6a6
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-da888d2c78859ee3
  evidence_ids:
  - ev-252e9f06fd3172a4
  - ev-d05ab0ef2230c5b3
  - ev-608cd16542960ba4
  - ev-1e042d64b1cc8673
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-99919df6cd936491
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-da888d2c78859ee3
  evidence_ids:
  - ev-1e065a61ad17c107
  - ev-252e9f06fd3172a4
  - ev-c63fa68a3519da5d
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T10:12:31Z;
    reviewed SHA-256=a257d091eac80a0ed11f02f15d3cd3dcc478d508af28d8aa58adfc0d96ebb0f1;
    current SHA-256=a257d091eac80a0ed11f02f15d3cd3dcc478d508af28d8aa58adfc0d96ebb0f1;
    hash_changed=False. Reports=["reports/yaml_record_review/Potassium_Aluminum_Chloride.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS
    and KG-Microbe identity rows pass, but the NCIT aluminum chloride parent is only
    substring-derived.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-1e065a61ad17c107
    - ev-252e9f06fd3172a4
  - name: legacy-native-ids
    value: '["SEM:3c2084bad0616037f2f5"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-252e9f06fd3172a4
    - ev-1e065a61ad17c107
    - ev-c63fa68a3519da5d
findings:
- finding_id: rec-f-7c6f62b14ecd985c
  issue_key: mim-reconciliation-historical-review-coverage-and-r-da888d2c78859ee3
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Potassium_Aluminum_Chloride'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T10:12:31Z;
    reviewed SHA-256=a257d091eac80a0ed11f02f15d3cd3dcc478d508af28d8aa58adfc0d96ebb0f1;
    current SHA-256=a257d091eac80a0ed11f02f15d3cd3dcc478d508af28d8aa58adfc0d96ebb0f1;
    hash_changed=False. Reports=["reports/yaml_record_review/Potassium_Aluminum_Chloride.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS
    and KG-Microbe identity rows pass, but the NCIT aluminum chloride parent is only
    substring-derived.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-da888d2c78859ee3
  evidence_ids:
  - ev-1e065a61ad17c107
  - ev-252e9f06fd3172a4
  - ev-c63fa68a3519da5d
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Potassium_Aluminum_Chloride.yaml
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
