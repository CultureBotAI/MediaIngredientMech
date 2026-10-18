# Per-record structured review: H3PO4 (data/ingredients/mapped/H3PO4.yaml)

- Review: 20261017T083000Z-h3po4
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for H3PO4 (data/ingredients/mapped/H3PO4.yaml, record-e22f75de511f18dc, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/H3PO4.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/H3PO4.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-e22f75de511f18dc | data/ingredients/mapped/H3PO4.yaml | maintained | H3PO4 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-e22f75de511f18dc | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-e22f75de511f18dc | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-e22f75de511f18dc | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-e22f75de511f18dc.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-e22f75de511f18dc.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T18:58:35Z; reviewed SHA-256=9d9f352e94f6f7508f2c3d0c869f41c4a94f5f3e3bb3c07196502a8cb6e2ce4e; current SHA-256=9d9f352e94f6f7508f2c3d0c869f41c4a94f5f3e3bb3c07196502a8cb6e2ce4e; hash_changed=False. Reports=["reports/yaml_record_review/H3PO4.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The phosphoric-acid identity and final SSSOM row pass, but the thin residual import still needs standard ChEBI enrichment fields.

## Findings

### rec-f-1e8f0b3b1d249f89: Historical review coverage and residual narrative: H3PO4

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-e22f75de511f18dc.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T18:58:35Z; reviewed SHA-256=9d9f352e94f6f7508f2c3d0c869f41c4a94f5f3e3bb3c07196502a8cb6e2ce4e; current SHA-256=9d9f352e94f6f7508f2c3d0c869f41c4a94f5f3e3bb3c07196502a8cb6e2ce4e; hash_changed=False. Reports=["reports/yaml_record_review/H3PO4.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The phosphoric-acid identity and final SSSOM row pass, but the thin residual import still needs standard ChEBI enrichment fields.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-20b9a3cea8094b43 | data/ingredients/mapped/H3PO4.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2567],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:26078","line":2569,"mapping_status":"MAPPED","ontology_id":"CHEBI:26078","preferred_term":"H3PO4"}],"identifier":"CHEBI:26078","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","match_level":"NORMALIZED","ontology_id":"CHEBI:26078","ontology_label":"phosphoric acid","ontology_source":"CHEBI"},"preferred_term":"H3PO4","sssom_rows":[{"data_row":1396,"object_id":"CHEBI:26078","object_label":"phosphoric acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:H3PO4","synonym_count":0} |
| ev-b7f72e8868765966 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2567] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-4ba642bbcfe00ef2 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:H3PO4; data-row positions=[1396] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1396,"object_id":"CHEBI:26078","object_label":"phosphoric acid","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:H3PO4","validation_method":"manual:claude_culturemech_residual_grounding&#124;CREATED&#124;2026-08-30"}] |
| ev-1c5493745c8c69c2 | docs/data/mapped_ingredients.csv; CSV lines=[2569] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:26078","line":2569,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:26078","preferred_term":"H3PO4","total_occurrences":"2"}] |
| ev-03b218547c789f5d | reports/yaml_record_review/H3PO4.md; &#96;data/ingredients/mapped/H3PO4.yaml&#96;:2; Verdict:4; Identity:11; Validation:20; Evidence:28; Completeness:46; Recommended Edits:52 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-619dc986f523e0a0 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[718] | context_only | [{"current_record_sha256":"9d9f352e94f6f7508f2c3d0c869f41c4a94f5f3e3bb3c07196502a8cb6e2ce4e","finding_id":"SEM:21412dfab89dccd2bfbd","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-h3po4
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: H3PO4 (data/ingredients/mapped/H3PO4.yaml)'
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
summary: Per-record structured review for H3PO4 (data/ingredients/mapped/H3PO4.yaml,
  record-e22f75de511f18dc, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/H3PO4.yaml
    sha256: 9d9f352e94f6f7508f2c3d0c869f41c4a94f5f3e3bb3c07196502a8cb6e2ce4e
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
  - path: reports/yaml_record_review/H3PO4.md
    sha256: 054bebff712b81e35f43d7401f5685fcfc0c64b4ce1f8195d42faabb97dc6d62
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-e22f75de511f18dc
  path: data/ingredients/mapped/H3PO4.yaml
  label: H3PO4
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/H3PO4.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/H3PO4.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/H3PO4.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-e22f75de511f18dc
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-e22f75de511f18dc
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-e22f75de511f18dc
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-e22f75de511f18dc
evidence:
- evidence_id: ev-20b9a3cea8094b43
  kind: record_content
  reference: data/ingredients/mapped/H3PO4.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2567],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:26078","line":2569,"mapping_status":"MAPPED","ontology_id":"CHEBI:26078","preferred_term":"H3PO4"}],"identifier":"CHEBI:26078","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","match_level":"NORMALIZED","ontology_id":"CHEBI:26078","ontology_label":"phosphoric
    acid","ontology_source":"CHEBI"},"preferred_term":"H3PO4","sssom_rows":[{"data_row":1396,"object_id":"CHEBI:26078","object_label":"phosphoric
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:H3PO4","synonym_count":0}'
  snapshot_sha256: 9d9f352e94f6f7508f2c3d0c869f41c4a94f5f3e3bb3c07196502a8cb6e2ce4e
- evidence_id: ev-b7f72e8868765966
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2567]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-4ba642bbcfe00ef2
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:H3PO4; data-row positions=[1396]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1396,"object_id":"CHEBI:26078","object_label":"phosphoric
    acid","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:H3PO4","validation_method":"manual:claude_culturemech_residual_grounding|CREATED|2026-08-30"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-1c5493745c8c69c2
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2569]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:26078","line":2569,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:26078","preferred_term":"H3PO4","total_occurrences":"2"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-03b218547c789f5d
  kind: prior_review
  reference: reports/yaml_record_review/H3PO4.md
  locator: '`data/ingredients/mapped/H3PO4.yaml`:2; Verdict:4; Identity:11; Validation:20;
    Evidence:28; Completeness:46; Recommended Edits:52'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 054bebff712b81e35f43d7401f5685fcfc0c64b4ce1f8195d42faabb97dc6d62
  quote: "Recommended Edits:\n- Minor: run or reproduce the standard ChEBI enrichment\
    \ so `H3PO4` gains\n  `ingredient_type`, CAS RN, formula, InChI, SMILES, and appropriate\
    \ exact\n  synonyms for `CHEBI:26078`."
- evidence_id: ev-619dc986f523e0a0
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[718]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"9d9f352e94f6f7508f2c3d0c869f41c4a94f5f3e3bb3c07196502a8cb6e2ce4e","finding_id":"SEM:21412dfab89dccd2bfbd","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-a3370681df61aa5a
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-e22f75de511f18dc
  evidence_ids:
  - ev-20b9a3cea8094b43
  - ev-b7f72e8868765966
  - ev-4ba642bbcfe00ef2
  - ev-1c5493745c8c69c2
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-8d3421f219fa57de
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-e22f75de511f18dc
  evidence_ids:
  - ev-03b218547c789f5d
  - ev-20b9a3cea8094b43
  - ev-619dc986f523e0a0
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T18:58:35Z;
    reviewed SHA-256=9d9f352e94f6f7508f2c3d0c869f41c4a94f5f3e3bb3c07196502a8cb6e2ce4e;
    current SHA-256=9d9f352e94f6f7508f2c3d0c869f41c4a94f5f3e3bb3c07196502a8cb6e2ce4e;
    hash_changed=False. Reports=["reports/yaml_record_review/H3PO4.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The phosphoric-acid identity
    and final SSSOM row pass, but the thin residual import still needs standard ChEBI
    enrichment fields.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-03b218547c789f5d
    - ev-20b9a3cea8094b43
  - name: legacy-native-ids
    value: '["SEM:21412dfab89dccd2bfbd"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-20b9a3cea8094b43
    - ev-03b218547c789f5d
    - ev-619dc986f523e0a0
findings:
- finding_id: rec-f-1e8f0b3b1d249f89
  issue_key: mim-reconciliation-historical-review-coverage-and-r-e22f75de511f18dc
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: H3PO4'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T18:58:35Z;
    reviewed SHA-256=9d9f352e94f6f7508f2c3d0c869f41c4a94f5f3e3bb3c07196502a8cb6e2ce4e;
    current SHA-256=9d9f352e94f6f7508f2c3d0c869f41c4a94f5f3e3bb3c07196502a8cb6e2ce4e;
    hash_changed=False. Reports=["reports/yaml_record_review/H3PO4.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The phosphoric-acid identity
    and final SSSOM row pass, but the thin residual import still needs standard ChEBI
    enrichment fields.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-e22f75de511f18dc
  evidence_ids:
  - ev-03b218547c789f5d
  - ev-20b9a3cea8094b43
  - ev-619dc986f523e0a0
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/H3PO4.yaml
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
