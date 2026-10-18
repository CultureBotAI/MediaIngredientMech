# Per-record structured review: MgO (data/ingredients/mapped/MgO.yaml)

- Review: 20261017T083000Z-mgo
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for MgO (data/ingredients/mapped/MgO.yaml, record-a49416b598be4e3d, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/MgO.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/MgO.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-a49416b598be4e3d | data/ingredients/mapped/MgO.yaml | maintained | MgO |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-a49416b598be4e3d | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-a49416b598be4e3d | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-a49416b598be4e3d | Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-a49416b598be4e3d.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-a49416b598be4e3d.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-17T03:03:27Z; reviewed SHA-256=9f0fe5b5d43690dbfbe0d506920905e1a1a79a6bd8ff28648bb430a0f75f8bda; current SHA-256=9f0fe5b5d43690dbfbe0d506920905e1a1a79a6bd8ff28648bb430a0f75f8bda; hash_changed=False. Reports=["reports/yaml_record_review/MgO.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:31794 magnesium oxide identity, residual occurrence, restored SSSOM evidence, and final row pass, but local chemical_properties and ingredient_type are missing.

## Findings

### rec-f-8c39de2174909f7d: Historical review coverage and residual narrative: MgO

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-a49416b598be4e3d.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-17T03:03:27Z; reviewed SHA-256=9f0fe5b5d43690dbfbe0d506920905e1a1a79a6bd8ff28648bb430a0f75f8bda; current SHA-256=9f0fe5b5d43690dbfbe0d506920905e1a1a79a6bd8ff28648bb430a0f75f8bda; hash_changed=False. Reports=["reports/yaml_record_review/MgO.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:31794 magnesium oxide identity, residual occurrence, restored SSSOM evidence, and final row pass, but local chemical_properties and ingredient_type are missing.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-76b4924b2e1520fd | data/ingredients/mapped/MgO.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2579],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:31794","line":2581,"mapping_status":"MAPPED","ontology_id":"CHEBI:31794","preferred_term":"MgO"}],"identifier":"CHEBI:31794","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","match_level":"NORMALIZED","ontology_id":"CHEBI:31794","ontology_label":"magnesium oxide","ontology_source":"CHEBI"},"preferred_term":"MgO","sssom_rows":[{"data_row":1859,"object_id":"CHEBI:31794","object_label":"magnesium oxide","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:MgO","synonym_count":0} |
| ev-0b46ce83671983a9 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2579] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-4b53b4f3f215d8d6 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:MgO; data-row positions=[1859] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1859,"object_id":"CHEBI:31794","object_label":"magnesium oxide","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:MgO","validation_method":"manual:claude_culturemech_residual_grounding&#124;CREATED&#124;2026-08-30"}] |
| ev-f0bb52628c7e097b | docs/data/mapped_ingredients.csv; CSV lines=[2581] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:31794","line":2581,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"3","ontology_id":"CHEBI:31794","preferred_term":"MgO","total_occurrences":"3"}] |
| ev-2dc0fd27e82928ff | reports/yaml_record_review/MgO.md; &#96;data/ingredients/mapped/MgO.yaml&#96;:2; Verdict:4; Identity:13; Validation:24; Evidence:31; Completeness:44; Recommended Edits:50 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-1c71a40c4d6ea076 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[929] | context_only | [{"current_record_sha256":"9f0fe5b5d43690dbfbe0d506920905e1a1a79a6bd8ff28648bb430a0f75f8bda","finding_id":"SEM:f8a2fa661795149ae16b","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-mgo
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: MgO (data/ingredients/mapped/MgO.yaml)'
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
summary: Per-record structured review for MgO (data/ingredients/mapped/MgO.yaml, record-a49416b598be4e3d,
  mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound
  to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/MgO.yaml
    sha256: 9f0fe5b5d43690dbfbe0d506920905e1a1a79a6bd8ff28648bb430a0f75f8bda
    role: target
  - path: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
    sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
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
  - path: reports/yaml_record_review/MgO.md
    sha256: acc8bf62fd6d7a6a679105407f35eda4ddb1c9e0627edc0c32efbd0592bc734b
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-a49416b598be4e3d
  path: data/ingredients/mapped/MgO.yaml
  label: MgO
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/MgO.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/MgO.yaml covering
    current record state, role evidence support, published surfaces, and residual
    historical review claims.
  selection: Single record data/ingredients/mapped/MgO.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-a49416b598be4e3d
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-a49416b598be4e3d
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-a49416b598be4e3d
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08
    and semantic review dispositions on HEAD.
  target_ids:
  - record-a49416b598be4e3d
evidence:
- evidence_id: ev-76b4924b2e1520fd
  kind: record_content
  reference: data/ingredients/mapped/MgO.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2579],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:31794","line":2581,"mapping_status":"MAPPED","ontology_id":"CHEBI:31794","preferred_term":"MgO"}],"identifier":"CHEBI:31794","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","match_level":"NORMALIZED","ontology_id":"CHEBI:31794","ontology_label":"magnesium
    oxide","ontology_source":"CHEBI"},"preferred_term":"MgO","sssom_rows":[{"data_row":1859,"object_id":"CHEBI:31794","object_label":"magnesium
    oxide","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:MgO","synonym_count":0}'
  snapshot_sha256: 9f0fe5b5d43690dbfbe0d506920905e1a1a79a6bd8ff28648bb430a0f75f8bda
- evidence_id: ev-0b46ce83671983a9
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2579]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-4b53b4f3f215d8d6
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:MgO; data-row positions=[1859]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1859,"object_id":"CHEBI:31794","object_label":"magnesium
    oxide","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:MgO","validation_method":"manual:claude_culturemech_residual_grounding|CREATED|2026-08-30"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-f0bb52628c7e097b
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2581]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:31794","line":2581,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"3","ontology_id":"CHEBI:31794","preferred_term":"MgO","total_occurrences":"3"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-2dc0fd27e82928ff
  kind: prior_review
  reference: reports/yaml_record_review/MgO.md
  locator: '`data/ingredients/mapped/MgO.yaml`:2; Verdict:4; Identity:13; Validation:24;
    Evidence:31; Completeness:44; Recommended Edits:50'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: acc8bf62fd6d7a6a679105407f35eda4ddb1c9e0627edc0c32efbd0592bc734b
  quote: "Recommended Edits:\n- Minor: backfill `ingredient_type: SINGLE_INGREDIENT`\
    \ and\n  `chemical_properties` from the active `CHEBI:31794` term in\n  `data/ingredients/mapped/MgO.yaml`,\
    \ then sync\n  `data/curated/mapped_ingredients.yaml` and regenerate affected\
    \ docs."
- evidence_id: ev-1c71a40c4d6ea076
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[929]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"9f0fe5b5d43690dbfbe0d506920905e1a1a79a6bd8ff28648bb430a0f75f8bda","finding_id":"SEM:f8a2fa661795149ae16b","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-870b721d706a9a2d
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-a49416b598be4e3d
  evidence_ids:
  - ev-76b4924b2e1520fd
  - ev-0b46ce83671983a9
  - ev-4b53b4f3f215d8d6
  - ev-f0bb52628c7e097b
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-ef98dba22d08247f
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-a49416b598be4e3d
  evidence_ids:
  - ev-2dc0fd27e82928ff
  - ev-76b4924b2e1520fd
  - ev-1c71a40c4d6ea076
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-17T03:03:27Z;
    reviewed SHA-256=9f0fe5b5d43690dbfbe0d506920905e1a1a79a6bd8ff28648bb430a0f75f8bda;
    current SHA-256=9f0fe5b5d43690dbfbe0d506920905e1a1a79a6bd8ff28648bb430a0f75f8bda;
    hash_changed=False. Reports=["reports/yaml_record_review/MgO.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI:31794 magnesium
    oxide identity, residual occurrence, restored SSSOM evidence, and final row pass,
    but local chemical_properties and ingredient_type are missing.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-2dc0fd27e82928ff
    - ev-76b4924b2e1520fd
  - name: legacy-native-ids
    value: '["SEM:f8a2fa661795149ae16b"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-76b4924b2e1520fd
    - ev-2dc0fd27e82928ff
    - ev-1c71a40c4d6ea076
findings:
- finding_id: rec-f-8c39de2174909f7d
  issue_key: mim-reconciliation-historical-review-coverage-and-r-a49416b598be4e3d
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: MgO'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-17T03:03:27Z;
    reviewed SHA-256=9f0fe5b5d43690dbfbe0d506920905e1a1a79a6bd8ff28648bb430a0f75f8bda;
    current SHA-256=9f0fe5b5d43690dbfbe0d506920905e1a1a79a6bd8ff28648bb430a0f75f8bda;
    hash_changed=False. Reports=["reports/yaml_record_review/MgO.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI:31794 magnesium
    oxide identity, residual occurrence, restored SSSOM evidence, and final row pass,
    but local chemical_properties and ingredient_type are missing.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-a49416b598be4e3d
  evidence_ids:
  - ev-2dc0fd27e82928ff
  - ev-76b4924b2e1520fd
  - ev-1c71a40c4d6ea076
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/MgO.yaml
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
  with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.
```
