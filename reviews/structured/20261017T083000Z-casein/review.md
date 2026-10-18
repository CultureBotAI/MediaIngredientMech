# Per-record structured review: Casein (data/ingredients/mapped/Casein.yaml)

- Review: 20261017T083000Z-casein
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Casein (data/ingredients/mapped/Casein.yaml, record-8f96dc0ec2240d17, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Casein.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Casein.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-8f96dc0ec2240d17 | data/ingredients/mapped/Casein.yaml | maintained | Casein |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-8f96dc0ec2240d17 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-8f96dc0ec2240d17 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-8f96dc0ec2240d17 | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-8f96dc0ec2240d17.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-8f96dc0ec2240d17.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T11:04:30Z; reviewed SHA-256=5c278fe135bc89885328d3704bf03f11591a43ca08bfec0a4b992c0ecc4d393d; current SHA-256=5c278fe135bc89885328d3704bf03f11591a43ca08bfec0a4b992c0ecc4d393d; hash_changed=False. Reports=["reports/yaml_record_review/Casein.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The FOODON casein identity, CultureMech role, and occurrence count pass, but kg_microbe_node_id still points at removed CHEBI:3448.

## Findings

### rec-f-3124cb8b8aaf1ac7: Historical review coverage and residual narrative: Casein

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-8f96dc0ec2240d17.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T11:04:30Z; reviewed SHA-256=5c278fe135bc89885328d3704bf03f11591a43ca08bfec0a4b992c0ecc4d393d; current SHA-256=5c278fe135bc89885328d3704bf03f11591a43ca08bfec0a4b992c0ecc4d393d; hash_changed=False. Reports=["reports/yaml_record_review/Casein.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The FOODON casein identity, CultureMech role, and occurrence count pass, but kg_microbe_node_id still points at removed CHEBI:3448.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-31ab302061a7d9e2 | data/ingredients/mapped/Casein.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[662],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:03420180","line":664,"mapping_status":"MAPPED","ontology_id":"FOODON:03420180","preferred_term":"Casein"}],"identifier":"FOODON:03420180","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":20,"edge_count":20,"occurrences":20},"occurrence_statistics":{"media_count":20,"total_occurrences":20},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"FOODON:03420180","ontology_label":"casein","ontology_source":"FOODON"},"preferred_term":"Casein","sssom_rows":[{"data_row":658,"object_id":"FOODON:03420180","object_label":"casein","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Casein","synonym_count":1} |
| ev-e813021ac1022af8 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [662] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-37221964905b80d9 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Casein; data-row positions=[658] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":658,"object_id":"FOODON:03420180","object_label":"casein","other":"CAS:9000-71-9","predicate_id":"skos:exactMatch","subject_id":"MIM:Casein","validation_method":"OLS:foodon&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-475845e3c856a875 | docs/data/mapped_ingredients.csv; CSV lines=[664] | supports | Published identity and count rows inspected: [{"identifier":"FOODON:03420180","line":664,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"20","ontology_id":"FOODON:03420180","preferred_term":"Casein","total_occurrences":"20"}] |
| ev-f2999400dad7a530 | reports/yaml_record_review/Casein.md; &#96;data/ingredients/mapped/Casein.yaml&#96;:2; Verdict:4; Identity:10; Validation:24; Evidence:42; Completeness:55; Recommended Edits:60 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-90a8654dc03f56e4 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[366] | context_only | [{"current_record_sha256":"5c278fe135bc89885328d3704bf03f11591a43ca08bfec0a4b992c0ecc4d393d","finding_id":"SEM:d10b94a7501f8eb672c8","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-casein
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Casein (data/ingredients/mapped/Casein.yaml)'
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
summary: Per-record structured review for Casein (data/ingredients/mapped/Casein.yaml,
  record-8f96dc0ec2240d17, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Casein.yaml
    sha256: 5c278fe135bc89885328d3704bf03f11591a43ca08bfec0a4b992c0ecc4d393d
    role: target
  - path: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
    sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
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
  - path: reports/yaml_record_review/Casein.md
    sha256: d6e531624df1c50a4afde7afb85f4bfe3f0d8cd6cb063b751d60db9865f8fcdc
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-8f96dc0ec2240d17
  path: data/ingredients/mapped/Casein.yaml
  label: Casein
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Casein.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Casein.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Casein.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-8f96dc0ec2240d17
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-8f96dc0ec2240d17
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-8f96dc0ec2240d17
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-8f96dc0ec2240d17
evidence:
- evidence_id: ev-31ab302061a7d9e2
  kind: record_content
  reference: data/ingredients/mapped/Casein.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[662],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:03420180","line":664,"mapping_status":"MAPPED","ontology_id":"FOODON:03420180","preferred_term":"Casein"}],"identifier":"FOODON:03420180","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":20,"edge_count":20,"occurrences":20},"occurrence_statistics":{"media_count":20,"total_occurrences":20},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"FOODON:03420180","ontology_label":"casein","ontology_source":"FOODON"},"preferred_term":"Casein","sssom_rows":[{"data_row":658,"object_id":"FOODON:03420180","object_label":"casein","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Casein","synonym_count":1}'
  snapshot_sha256: 5c278fe135bc89885328d3704bf03f11591a43ca08bfec0a4b992c0ecc4d393d
- evidence_id: ev-e813021ac1022af8
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [662]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-37221964905b80d9
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Casein; data-row positions=[658]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":658,"object_id":"FOODON:03420180","object_label":"casein","other":"CAS:9000-71-9","predicate_id":"skos:exactMatch","subject_id":"MIM:Casein","validation_method":"OLS:foodon|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-475845e3c856a875
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[664]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"FOODON:03420180","line":664,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"20","ontology_id":"FOODON:03420180","preferred_term":"Casein","total_occurrences":"20"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-f2999400dad7a530
  kind: prior_review
  reference: reports/yaml_record_review/Casein.md
  locator: '`data/ingredients/mapped/Casein.yaml`:2; Verdict:4; Identity:10; Validation:24;
    Evidence:42; Completeness:55; Recommended Edits:60'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: d6e531624df1c50a4afde7afb85f4bfe3f0d8cd6cb063b751d60db9865f8fcdc
  quote: "Recommended Edits:\n- Major: update or remove the stale `kg_microbe_node_id:\
    \ CHEBI:3448` in\n  `data/ingredients/mapped/Casein.yaml`, then rerun\n  `qc-kg-microbe-node-ids`\
    \ and the standard strict, SSSOM, roundtrip, and diff\n  checks."
- evidence_id: ev-90a8654dc03f56e4
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[366]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"5c278fe135bc89885328d3704bf03f11591a43ca08bfec0a4b992c0ecc4d393d","finding_id":"SEM:d10b94a7501f8eb672c8","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-ac6667024702f9f7
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-8f96dc0ec2240d17
  evidence_ids:
  - ev-31ab302061a7d9e2
  - ev-e813021ac1022af8
  - ev-37221964905b80d9
  - ev-475845e3c856a875
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-f3840152f046a6e8
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-8f96dc0ec2240d17
  evidence_ids:
  - ev-f2999400dad7a530
  - ev-31ab302061a7d9e2
  - ev-90a8654dc03f56e4
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T11:04:30Z;
    reviewed SHA-256=5c278fe135bc89885328d3704bf03f11591a43ca08bfec0a4b992c0ecc4d393d;
    current SHA-256=5c278fe135bc89885328d3704bf03f11591a43ca08bfec0a4b992c0ecc4d393d;
    hash_changed=False. Reports=["reports/yaml_record_review/Casein.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The FOODON casein identity,
    CultureMech role, and occurrence count pass, but kg_microbe_node_id still points
    at removed CHEBI:3448.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f2999400dad7a530
    - ev-31ab302061a7d9e2
  - name: legacy-native-ids
    value: '["SEM:d10b94a7501f8eb672c8"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-31ab302061a7d9e2
    - ev-f2999400dad7a530
    - ev-90a8654dc03f56e4
findings:
- finding_id: rec-f-3124cb8b8aaf1ac7
  issue_key: mim-reconciliation-historical-review-coverage-and-r-8f96dc0ec2240d17
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Casein'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T11:04:30Z;
    reviewed SHA-256=5c278fe135bc89885328d3704bf03f11591a43ca08bfec0a4b992c0ecc4d393d;
    current SHA-256=5c278fe135bc89885328d3704bf03f11591a43ca08bfec0a4b992c0ecc4d393d;
    hash_changed=False. Reports=["reports/yaml_record_review/Casein.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The FOODON casein identity,
    CultureMech role, and occurrence count pass, but kg_microbe_node_id still points
    at removed CHEBI:3448.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-8f96dc0ec2240d17
  evidence_ids:
  - ev-f2999400dad7a530
  - ev-31ab302061a7d9e2
  - ev-90a8654dc03f56e4
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Casein.yaml
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
  with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.
```
