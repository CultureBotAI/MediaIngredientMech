# Per-record structured review: Glucose_1-phosphate (data/ingredients/mapped/Glucose_1-phosphate.yaml)

- Review: 20261017T083000Z-glucose-1-phosphate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Glucose_1-phosphate (data/ingredients/mapped/Glucose_1-phosphate.yaml, record-e03fab784c20e25d, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Glucose_1-phosphate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Glucose_1-phosphate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-e03fab784c20e25d | data/ingredients/mapped/Glucose_1-phosphate.yaml | maintained | Glucose_1-phosphate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-e03fab784c20e25d | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-e03fab784c20e25d | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-e03fab784c20e25d | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-e03fab784c20e25d.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-e03fab784c20e25d.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T17:44:41Z; reviewed SHA-256=1552deda8ced71002bde65f7dd753d3be40c0fda327c6f9ed8fbc98649a40d26; current SHA-256=1552deda8ced71002bde65f7dd753d3be40c0fda327c6f9ed8fbc98649a40d26; hash_changed=False. Reports=["reports/yaml_record_review/Glucose_1-phosphate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The close match to D-glucopyranose 1-phosphate passes, but structure fields and top-level notes need cleanup.

## Findings

### rec-f-059531d0a8386d6f: Historical review coverage and residual narrative: Glucose_1-phosphate

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-e03fab784c20e25d.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T17:44:41Z; reviewed SHA-256=1552deda8ced71002bde65f7dd753d3be40c0fda327c6f9ed8fbc98649a40d26; current SHA-256=1552deda8ced71002bde65f7dd753d3be40c0fda327c6f9ed8fbc98649a40d26; hash_changed=False. Reports=["reports/yaml_record_review/Glucose_1-phosphate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The close match to D-glucopyranose 1-phosphate passes, but structure fields and top-level notes need cleanup.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-8ebc96491c7b0b30 | data/ingredients/mapped/Glucose_1-phosphate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[206],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16077","line":208,"mapping_status":"MAPPED","ontology_id":"CHEBI:16077","preferred_term":"Glucose 1-phosphate"}],"identifier":"CHEBI:16077","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":7,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:16077","ontology_label":"D-glucopyranose 1-phosphate","ontology_source":"CHEBI"},"preferred_term":"Glucose 1-phosphate","sssom_rows":[{"data_row":1308,"object_id":"CHEBI:16077","object_label":"D-glucopyranose 1-phosphate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glucose_1-phosphate","synonym_count":1} |
| ev-5572c24566d82467 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [206] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-8ed552e917e2aa2f | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Glucose_1-phosphate; data-row positions=[1308] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1308,"object_id":"CHEBI:16077","object_label":"D-glucopyranose 1-phosphate","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Glucose_1-phosphate","validation_method":"manual:promote_resolved_unmapped&#124;PROMOTED&#124;2026-08-06"}] |
| ev-555b9a52d1c3a28d | docs/data/mapped_ingredients.csv; CSV lines=[208] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:16077","line":208,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:16077","preferred_term":"Glucose 1-phosphate","total_occurrences":"0"}] |
| ev-34dbfba5b82540cd | reports/yaml_record_review/Glucose_1-phosphate.md; &#96;data/ingredients/mapped/Glucose_1-phosphate.yaml&#96;:2; Verdict:4; Identity:11; Validation:23; Evidence:35; Completeness:57; Recommended Edits:63 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-b491b753e21bc486 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[667] | context_only | [{"current_record_sha256":"1552deda8ced71002bde65f7dd753d3be40c0fda327c6f9ed8fbc98649a40d26","finding_id":"SEM:d139c9d57eca32e95420","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-glucose-1-phosphate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Glucose_1-phosphate (data/ingredients/mapped/Glucose_1-phosphate.yaml)'
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
summary: Per-record structured review for Glucose_1-phosphate (data/ingredients/mapped/Glucose_1-phosphate.yaml,
  record-e03fab784c20e25d, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Glucose_1-phosphate.yaml
    sha256: 1552deda8ced71002bde65f7dd753d3be40c0fda327c6f9ed8fbc98649a40d26
    role: target
  - path: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
    sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
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
  - path: reports/yaml_record_review/Glucose_1-phosphate.md
    sha256: 9fc3c241f2a874509cc57080d5d00ca6a0886fb5b0d320f230c9b14ad3573fb1
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-e03fab784c20e25d
  path: data/ingredients/mapped/Glucose_1-phosphate.yaml
  label: Glucose_1-phosphate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glucose_1-phosphate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Glucose_1-phosphate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Glucose_1-phosphate.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-e03fab784c20e25d
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-e03fab784c20e25d
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-e03fab784c20e25d
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-e03fab784c20e25d
evidence:
- evidence_id: ev-8ebc96491c7b0b30
  kind: record_content
  reference: data/ingredients/mapped/Glucose_1-phosphate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[206],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16077","line":208,"mapping_status":"MAPPED","ontology_id":"CHEBI:16077","preferred_term":"Glucose
    1-phosphate"}],"identifier":"CHEBI:16077","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":7,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:16077","ontology_label":"D-glucopyranose
    1-phosphate","ontology_source":"CHEBI"},"preferred_term":"Glucose 1-phosphate","sssom_rows":[{"data_row":1308,"object_id":"CHEBI:16077","object_label":"D-glucopyranose
    1-phosphate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glucose_1-phosphate","synonym_count":1}'
  snapshot_sha256: 1552deda8ced71002bde65f7dd753d3be40c0fda327c6f9ed8fbc98649a40d26
- evidence_id: ev-5572c24566d82467
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [206]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-8ed552e917e2aa2f
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Glucose_1-phosphate; data-row positions=[1308]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1308,"object_id":"CHEBI:16077","object_label":"D-glucopyranose
    1-phosphate","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Glucose_1-phosphate","validation_method":"manual:promote_resolved_unmapped|PROMOTED|2026-08-06"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-555b9a52d1c3a28d
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[208]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:16077","line":208,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:16077","preferred_term":"Glucose
    1-phosphate","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-34dbfba5b82540cd
  kind: prior_review
  reference: reports/yaml_record_review/Glucose_1-phosphate.md
  locator: '`data/ingredients/mapped/Glucose_1-phosphate.yaml`:2; Verdict:4; Identity:11;
    Validation:23; Evidence:35; Completeness:57; Recommended Edits:63'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 9fc3c241f2a874509cc57080d5d00ca6a0886fb5b0d320f230c9b14ad3573fb1
  quote: "Recommended Edits:\n- Minor: backfill `chemical_properties` from `CHEBI:16077`\
    \ and remove or update\n  the stale top-level `notes`."
- evidence_id: ev-b491b753e21bc486
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[667]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"1552deda8ced71002bde65f7dd753d3be40c0fda327c6f9ed8fbc98649a40d26","finding_id":"SEM:d139c9d57eca32e95420","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-c278dcf9199b0017
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-e03fab784c20e25d
  evidence_ids:
  - ev-8ebc96491c7b0b30
  - ev-5572c24566d82467
  - ev-8ed552e917e2aa2f
  - ev-555b9a52d1c3a28d
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-4eb78aedbe6795a6
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-e03fab784c20e25d
  evidence_ids:
  - ev-34dbfba5b82540cd
  - ev-8ebc96491c7b0b30
  - ev-b491b753e21bc486
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T17:44:41Z;
    reviewed SHA-256=1552deda8ced71002bde65f7dd753d3be40c0fda327c6f9ed8fbc98649a40d26;
    current SHA-256=1552deda8ced71002bde65f7dd753d3be40c0fda327c6f9ed8fbc98649a40d26;
    hash_changed=False. Reports=["reports/yaml_record_review/Glucose_1-phosphate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The close
    match to D-glucopyranose 1-phosphate passes, but structure fields and top-level
    notes need cleanup.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-34dbfba5b82540cd
    - ev-8ebc96491c7b0b30
  - name: legacy-native-ids
    value: '["SEM:d139c9d57eca32e95420"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-8ebc96491c7b0b30
    - ev-34dbfba5b82540cd
    - ev-b491b753e21bc486
findings:
- finding_id: rec-f-059531d0a8386d6f
  issue_key: mim-reconciliation-historical-review-coverage-and-r-e03fab784c20e25d
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Glucose_1-phosphate'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T17:44:41Z;
    reviewed SHA-256=1552deda8ced71002bde65f7dd753d3be40c0fda327c6f9ed8fbc98649a40d26;
    current SHA-256=1552deda8ced71002bde65f7dd753d3be40c0fda327c6f9ed8fbc98649a40d26;
    hash_changed=False. Reports=["reports/yaml_record_review/Glucose_1-phosphate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The close
    match to D-glucopyranose 1-phosphate passes, but structure fields and top-level
    notes need cleanup.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-e03fab784c20e25d
  evidence_ids:
  - ev-34dbfba5b82540cd
  - ev-8ebc96491c7b0b30
  - ev-b491b753e21bc486
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glucose_1-phosphate.yaml
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
  with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.
```
