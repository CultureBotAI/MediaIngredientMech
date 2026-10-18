# Per-record structured review: Curdlan (data/ingredients/mapped/Curdlan.yaml)

- Review: 20261017T083000Z-curdlan
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Curdlan (data/ingredients/mapped/Curdlan.yaml, record-3178c74d9643d513, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Curdlan.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Curdlan.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-3178c74d9643d513 | data/ingredients/mapped/Curdlan.yaml | maintained | Curdlan |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-3178c74d9643d513 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-3178c74d9643d513 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-3178c74d9643d513 | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-3178c74d9643d513.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-3178c74d9643d513.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T12:50:19Z; reviewed SHA-256=f6d77336e6292bbc92b12127ea94db3d43089a0b195e6da3893e3ccab4edbbd0; current SHA-256=f6d77336e6292bbc92b12127ea94db3d43089a0b195e6da3893e3ccab4edbbd0; hash_changed=False. Reports=["reports/yaml_record_review/Curdlan.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS and MeSH Curdlan rows pass structurally, but a fresh CHEBI curdlan candidate makes the no-CHEBI provenance stale.

## Findings

### rec-f-ba9e36c836880012: Historical review coverage and residual narrative: Curdlan

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-3178c74d9643d513.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T12:50:19Z; reviewed SHA-256=f6d77336e6292bbc92b12127ea94db3d43089a0b195e6da3893e3ccab4edbbd0; current SHA-256=f6d77336e6292bbc92b12127ea94db3d43089a0b195e6da3893e3ccab4edbbd0; hash_changed=False. Reports=["reports/yaml_record_review/Curdlan.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS and MeSH Curdlan rows pass structurally, but a fresh CHEBI curdlan candidate makes the no-CHEBI provenance stale.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-b7a0ce8510a2c843 | data/ingredients/mapped/Curdlan.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[780],"raw_equal":true},"docs_rows":[{"identifier":"cas:54724-00-4","line":782,"mapping_status":"MAPPED","ontology_id":"mesh:C038459","preferred_term":"Curdlan"}],"identifier":"cas:54724-00-4","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"mesh:C038459","ontology_label":"curdlan","ontology_source":"MESH"},"preferred_term":"Curdlan","sssom_rows":[{"data_row":849,"object_id":"mesh:C038459","object_label":"curdlan","predicate_id":"skos:broadMatch"},{"data_row":850,"object_id":"cas:54724-00-4","object_label":"Curdlan","predicate_id":"skos:exactMatch"},{"data_row":851,"object_id":"kgmicrobe.compound:curdlan","object_label":"Curdlan","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Curdlan","synonym_count":0} |
| ev-0cbd4a468ca0d4fd | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [780] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-896ba806a786b5c3 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Curdlan; data-row positions=[849,850,851] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":849,"object_id":"mesh:C038459","object_label":"curdlan","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Curdlan","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":850,"object_id":"cas:54724-00-4","object_label":"Curdlan","other":"CAS:54724-00-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Curdlan","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"},{"data_row":851,"object_id":"kgmicrobe.compound:curdlan","object_label":"Curdlan","other":"CAS:54724-00-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Curdlan","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-4caa10c91ee2dc6b | docs/data/mapped_ingredients.csv; CSV lines=[782] | supports | Published identity and count rows inspected: [{"identifier":"cas:54724-00-4","line":782,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C038459","preferred_term":"Curdlan","total_occurrences":"0"}] |
| ev-6c931d60e92a2b51 | reports/yaml_record_review/Curdlan.md; &#96;data/ingredients/mapped/Curdlan.yaml&#96;:2; Verdict:4; Identity:11; Validation:28; Evidence:47; Completeness:63; Recommended Edits:70 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-6071d9cc0877e6de | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[452] | context_only | [{"current_record_sha256":"f6d77336e6292bbc92b12127ea94db3d43089a0b195e6da3893e3ccab4edbbd0","finding_id":"SEM:8e73ae07347a18c17b16","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-curdlan
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Curdlan (data/ingredients/mapped/Curdlan.yaml)'
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
summary: Per-record structured review for Curdlan (data/ingredients/mapped/Curdlan.yaml,
  record-3178c74d9643d513, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Curdlan.yaml
    sha256: f6d77336e6292bbc92b12127ea94db3d43089a0b195e6da3893e3ccab4edbbd0
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
  - path: reports/yaml_record_review/Curdlan.md
    sha256: 0ca48b6e6bdbc66a0f04f0de056ce98d2961837d03c866ec4f3baea75d077040
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-3178c74d9643d513
  path: data/ingredients/mapped/Curdlan.yaml
  label: Curdlan
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Curdlan.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Curdlan.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Curdlan.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-3178c74d9643d513
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-3178c74d9643d513
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-3178c74d9643d513
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-3178c74d9643d513
evidence:
- evidence_id: ev-b7a0ce8510a2c843
  kind: record_content
  reference: data/ingredients/mapped/Curdlan.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[780],"raw_equal":true},"docs_rows":[{"identifier":"cas:54724-00-4","line":782,"mapping_status":"MAPPED","ontology_id":"mesh:C038459","preferred_term":"Curdlan"}],"identifier":"cas:54724-00-4","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"mesh:C038459","ontology_label":"curdlan","ontology_source":"MESH"},"preferred_term":"Curdlan","sssom_rows":[{"data_row":849,"object_id":"mesh:C038459","object_label":"curdlan","predicate_id":"skos:broadMatch"},{"data_row":850,"object_id":"cas:54724-00-4","object_label":"Curdlan","predicate_id":"skos:exactMatch"},{"data_row":851,"object_id":"kgmicrobe.compound:curdlan","object_label":"Curdlan","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Curdlan","synonym_count":0}'
  snapshot_sha256: f6d77336e6292bbc92b12127ea94db3d43089a0b195e6da3893e3ccab4edbbd0
- evidence_id: ev-0cbd4a468ca0d4fd
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [780]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-896ba806a786b5c3
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Curdlan; data-row positions=[849,850,851]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":849,"object_id":"mesh:C038459","object_label":"curdlan","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Curdlan","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":850,"object_id":"cas:54724-00-4","object_label":"Curdlan","other":"CAS:54724-00-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Curdlan","validation_method":"none|UNKNOWN_TERM|2026-07-07"},{"data_row":851,"object_id":"kgmicrobe.compound:curdlan","object_label":"Curdlan","other":"CAS:54724-00-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Curdlan","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-4caa10c91ee2dc6b
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[782]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:54724-00-4","line":782,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C038459","preferred_term":"Curdlan","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-6c931d60e92a2b51
  kind: prior_review
  reference: reports/yaml_record_review/Curdlan.md
  locator: '`data/ingredients/mapped/Curdlan.yaml`:2; Verdict:4; Identity:11; Validation:28;
    Evidence:47; Completeness:63; Recommended Edits:70'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 0ca48b6e6bdbc66a0f04f0de056ce98d2961837d03c866ec4f3baea75d077040
  quote: "Recommended Edits:\n- Major: review `CHEBI:37671` against `cas:54724-00-4`\
    \ in\n  `data/ingredients/mapped/Curdlan.yaml`; either remap to CHEBI if it is\
    \ exact\n  or a better parent, or keep the MeSH parent and record why the CHEBI\
    \ result\n  is too broad.\n- Regenerate synchronized products and rerun strict\
    \ validation, SSSOM QC,\n  aggregate roundtrip, and `git diff --check`."
- evidence_id: ev-6071d9cc0877e6de
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[452]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"f6d77336e6292bbc92b12127ea94db3d43089a0b195e6da3893e3ccab4edbbd0","finding_id":"SEM:8e73ae07347a18c17b16","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-d9541fc73074c6e3
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-3178c74d9643d513
  evidence_ids:
  - ev-b7a0ce8510a2c843
  - ev-0cbd4a468ca0d4fd
  - ev-896ba806a786b5c3
  - ev-4caa10c91ee2dc6b
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-efd8f58dd48e370f
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-3178c74d9643d513
  evidence_ids:
  - ev-6c931d60e92a2b51
  - ev-b7a0ce8510a2c843
  - ev-6071d9cc0877e6de
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T12:50:19Z;
    reviewed SHA-256=f6d77336e6292bbc92b12127ea94db3d43089a0b195e6da3893e3ccab4edbbd0;
    current SHA-256=f6d77336e6292bbc92b12127ea94db3d43089a0b195e6da3893e3ccab4edbbd0;
    hash_changed=False. Reports=["reports/yaml_record_review/Curdlan.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The CAS and MeSH Curdlan
    rows pass structurally, but a fresh CHEBI curdlan candidate makes the no-CHEBI
    provenance stale.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-6c931d60e92a2b51
    - ev-b7a0ce8510a2c843
  - name: legacy-native-ids
    value: '["SEM:8e73ae07347a18c17b16"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-b7a0ce8510a2c843
    - ev-6c931d60e92a2b51
    - ev-6071d9cc0877e6de
findings:
- finding_id: rec-f-ba9e36c836880012
  issue_key: mim-reconciliation-historical-review-coverage-and-r-3178c74d9643d513
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Curdlan'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T12:50:19Z;
    reviewed SHA-256=f6d77336e6292bbc92b12127ea94db3d43089a0b195e6da3893e3ccab4edbbd0;
    current SHA-256=f6d77336e6292bbc92b12127ea94db3d43089a0b195e6da3893e3ccab4edbbd0;
    hash_changed=False. Reports=["reports/yaml_record_review/Curdlan.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The CAS and MeSH Curdlan
    rows pass structurally, but a fresh CHEBI curdlan candidate makes the no-CHEBI
    provenance stale.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-3178c74d9643d513
  evidence_ids:
  - ev-6c931d60e92a2b51
  - ev-b7a0ce8510a2c843
  - ev-6071d9cc0877e6de
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Curdlan.yaml
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
