# Per-record structured review: Calprotectin (data/ingredients/mapped/Calprotectin.yaml)

- Review: 20261017T083000Z-calprotectin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Calprotectin (data/ingredients/mapped/Calprotectin.yaml, record-a692a82830c4678c, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Calprotectin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Calprotectin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-a692a82830c4678c | data/ingredients/mapped/Calprotectin.yaml | maintained | Calprotectin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-a692a82830c4678c | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-a692a82830c4678c | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-a692a82830c4678c | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-a692a82830c4678c.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-a692a82830c4678c.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T10:45:31Z; reviewed SHA-256=42089795dca191212388bb24a7f6019a8fc48e2ae9dc7a9273052e740adf7974; current SHA-256=42089795dca191212388bb24a7f6019a8fc48e2ae9dc7a9273052e740adf7974; hash_changed=False. Reports=["reports/yaml_record_review/Calprotectin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact NCIT calprotectin identity, SSSOM row, and prefix-specific OLS resolution pass, but top-level notes are stale.

## Findings

### rec-f-a2163061411c7e40: Historical review coverage and residual narrative: Calprotectin

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-a692a82830c4678c.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T10:45:31Z; reviewed SHA-256=42089795dca191212388bb24a7f6019a8fc48e2ae9dc7a9273052e740adf7974; current SHA-256=42089795dca191212388bb24a7f6019a8fc48e2ae9dc7a9273052e740adf7974; hash_changed=False. Reports=["reports/yaml_record_review/Calprotectin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact NCIT calprotectin identity, SSSOM row, and prefix-specific OLS resolution pass, but top-level notes are stale.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-3744c11439bfc0f0 | data/ingredients/mapped/Calprotectin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[637],"raw_equal":true},"docs_rows":[{"identifier":"NCIT:C105971","line":639,"mapping_status":"MAPPED","ontology_id":"NCIT:C105971","preferred_term":"Calprotectin"}],"identifier":"NCIT:C105971","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"NCIT:C105971","ontology_label":"Calprotectin","ontology_source":"NCIT"},"preferred_term":"Calprotectin","sssom_rows":[{"data_row":620,"object_id":"NCIT:C105971","object_label":"Calprotectin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Calprotectin","synonym_count":1} |
| ev-a624b3491f11d88b | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [637] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-039c31635dbeeb97 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Calprotectin; data-row positions=[620] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":620,"object_id":"NCIT:C105971","object_label":"Calprotectin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Calprotectin","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-a5d770b5410b2222 | docs/data/mapped_ingredients.csv; CSV lines=[639] | supports | Published identity and count rows inspected: [{"identifier":"NCIT:C105971","line":639,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"NCIT:C105971","preferred_term":"Calprotectin","total_occurrences":"0"}] |
| ev-4130ea46258002e5 | reports/yaml_record_review/Calprotectin.md; &#96;data/ingredients/mapped/Calprotectin.yaml&#96;:2; Verdict:4; Identity:10; Validation:21; Evidence:36; Completeness:50; Recommended Edits:58 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-a79dc230e2a6b7e4 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[350] | context_only | [{"current_record_sha256":"42089795dca191212388bb24a7f6019a8fc48e2ae9dc7a9273052e740adf7974","finding_id":"SEM:2d062077656f8e53dcbe","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-calprotectin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Calprotectin (data/ingredients/mapped/Calprotectin.yaml)'
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
summary: Per-record structured review for Calprotectin (data/ingredients/mapped/Calprotectin.yaml,
  record-a692a82830c4678c, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Calprotectin.yaml
    sha256: 42089795dca191212388bb24a7f6019a8fc48e2ae9dc7a9273052e740adf7974
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
  - path: reports/yaml_record_review/Calprotectin.md
    sha256: 4583857c03d84fc3ddc200521857f9ae256f08706314352d4e9bbc8e9eb23e8e
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-a692a82830c4678c
  path: data/ingredients/mapped/Calprotectin.yaml
  label: Calprotectin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Calprotectin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Calprotectin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Calprotectin.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-a692a82830c4678c
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-a692a82830c4678c
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-a692a82830c4678c
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-a692a82830c4678c
evidence:
- evidence_id: ev-3744c11439bfc0f0
  kind: record_content
  reference: data/ingredients/mapped/Calprotectin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[637],"raw_equal":true},"docs_rows":[{"identifier":"NCIT:C105971","line":639,"mapping_status":"MAPPED","ontology_id":"NCIT:C105971","preferred_term":"Calprotectin"}],"identifier":"NCIT:C105971","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"NCIT:C105971","ontology_label":"Calprotectin","ontology_source":"NCIT"},"preferred_term":"Calprotectin","sssom_rows":[{"data_row":620,"object_id":"NCIT:C105971","object_label":"Calprotectin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Calprotectin","synonym_count":1}'
  snapshot_sha256: 42089795dca191212388bb24a7f6019a8fc48e2ae9dc7a9273052e740adf7974
- evidence_id: ev-a624b3491f11d88b
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [637]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-039c31635dbeeb97
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Calprotectin; data-row positions=[620]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":620,"object_id":"NCIT:C105971","object_label":"Calprotectin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Calprotectin","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-a5d770b5410b2222
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[639]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"NCIT:C105971","line":639,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"NCIT:C105971","preferred_term":"Calprotectin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-4130ea46258002e5
  kind: prior_review
  reference: reports/yaml_record_review/Calprotectin.md
  locator: '`data/ingredients/mapped/Calprotectin.yaml`:2; Verdict:4; Identity:10;
    Validation:21; Evidence:36; Completeness:50; Recommended Edits:58'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 4583857c03d84fc3ddc200521857f9ae256f08706314352d4e9bbc8e9eb23e8e
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/Calprotectin.yaml`, replace\
    \ the stale top-level\n  `notes` with NCIT-resolution wording or remove the note\
    \ entirely.\n- Regenerate the aggregate/docs products and prove the cleanup with\
    \ strict\n  validation and round-trip verification."
- evidence_id: ev-a79dc230e2a6b7e4
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[350]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"42089795dca191212388bb24a7f6019a8fc48e2ae9dc7a9273052e740adf7974","finding_id":"SEM:2d062077656f8e53dcbe","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-5bd548a7ee77bb6d
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-a692a82830c4678c
  evidence_ids:
  - ev-3744c11439bfc0f0
  - ev-a624b3491f11d88b
  - ev-039c31635dbeeb97
  - ev-a5d770b5410b2222
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-58898a8689e073a3
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-a692a82830c4678c
  evidence_ids:
  - ev-4130ea46258002e5
  - ev-3744c11439bfc0f0
  - ev-a79dc230e2a6b7e4
  details: 'Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T10:45:31Z;
    reviewed SHA-256=42089795dca191212388bb24a7f6019a8fc48e2ae9dc7a9273052e740adf7974;
    current SHA-256=42089795dca191212388bb24a7f6019a8fc48e2ae9dc7a9273052e740adf7974;
    hash_changed=False. Reports=["reports/yaml_record_review/Calprotectin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact NCIT
    calprotectin identity, SSSOM row, and prefix-specific OLS resolution pass, but
    top-level notes are stale.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-4130ea46258002e5
    - ev-3744c11439bfc0f0
  - name: legacy-native-ids
    value: '["SEM:2d062077656f8e53dcbe"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-3744c11439bfc0f0
    - ev-4130ea46258002e5
    - ev-a79dc230e2a6b7e4
findings:
- finding_id: rec-f-a2163061411c7e40
  issue_key: mim-reconciliation-historical-review-coverage-and-r-a692a82830c4678c
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Calprotectin'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T10:45:31Z;
    reviewed SHA-256=42089795dca191212388bb24a7f6019a8fc48e2ae9dc7a9273052e740adf7974;
    current SHA-256=42089795dca191212388bb24a7f6019a8fc48e2ae9dc7a9273052e740adf7974;
    hash_changed=False. Reports=["reports/yaml_record_review/Calprotectin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact NCIT
    calprotectin identity, SSSOM row, and prefix-specific OLS resolution pass, but
    top-level notes are stale.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-a692a82830c4678c
  evidence_ids:
  - ev-4130ea46258002e5
  - ev-3744c11439bfc0f0
  - ev-a79dc230e2a6b7e4
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Calprotectin.yaml
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
