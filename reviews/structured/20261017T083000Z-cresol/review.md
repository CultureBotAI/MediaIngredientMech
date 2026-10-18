# Per-record structured review: Cresol (data/ingredients/mapped/Cresol.yaml)

- Review: 20261017T083000Z-cresol
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Cresol (data/ingredients/mapped/Cresol.yaml, record-3803548af6670cfc, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Cresol.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Cresol.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-3803548af6670cfc | data/ingredients/mapped/Cresol.yaml | maintained | Cresol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-3803548af6670cfc | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-3803548af6670cfc | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-3803548af6670cfc | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-3803548af6670cfc.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-3803548af6670cfc.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T12:38:48Z; reviewed SHA-256=87886c72e9eb3d159db42f24a5dc514bd6bcb4eefda4bca206c16a9ef9e2feca; current SHA-256=87886c72e9eb3d159db42f24a5dc514bd6bcb4eefda4bca206c16a9ef9e2feca; hash_changed=False. Reports=["reports/yaml_record_review/Cresol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI cresol identity and SSSOM row pass, but the residual source has 3/3 occurrences while the record publishes 1/1 and no membership rows.

## Findings

### rec-f-b95f5fd3bcaa7e54: Historical review coverage and residual narrative: Cresol

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-3803548af6670cfc.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T12:38:48Z; reviewed SHA-256=87886c72e9eb3d159db42f24a5dc514bd6bcb4eefda4bca206c16a9ef9e2feca; current SHA-256=87886c72e9eb3d159db42f24a5dc514bd6bcb4eefda4bca206c16a9ef9e2feca; hash_changed=False. Reports=["reports/yaml_record_review/Cresol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI cresol identity and SSSOM row pass, but the residual source has 3/3 occurrences while the record publishes 1/1 and no membership rows.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-51b2198171b6cefa | data/ingredients/mapped/Cresol.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2555],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:25399","line":2557,"mapping_status":"MAPPED","ontology_id":"CHEBI:25399","preferred_term":"Cresol"}],"identifier":"CHEBI:25399","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","match_level":"EXACT","ontology_id":"CHEBI:25399","ontology_label":"cresol","ontology_source":"CHEBI"},"preferred_term":"Cresol","sssom_rows":[{"data_row":830,"object_id":"CHEBI:25399","object_label":"cresol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cresol","synonym_count":0} |
| ev-188ae876234d6e16 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2555] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-5a32c2f69a5979cc | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Cresol; data-row positions=[830] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":830,"object_id":"CHEBI:25399","object_label":"cresol","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Cresol","validation_method":"manual:claude_culturemech_residual_grounding&#124;CREATED&#124;2026-08-30"}] |
| ev-dfa7a9a51c9444f6 | docs/data/mapped_ingredients.csv; CSV lines=[2557] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:25399","line":2557,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:25399","preferred_term":"Cresol","total_occurrences":"1"}] |
| ev-a4ef484f8c4b1bd1 | reports/yaml_record_review/Cresol.md; &#96;data/ingredients/mapped/Cresol.yaml&#96;:2; Verdict:4; Identity:12; Validation:24; Evidence:44; Completeness:58; Recommended Edits:66 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-cde98821047b4383 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[445] | context_only | [{"current_record_sha256":"87886c72e9eb3d159db42f24a5dc514bd6bcb4eefda4bca206c16a9ef9e2feca","finding_id":"SEM:b66edf88ea583849f19f","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-cresol
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Cresol (data/ingredients/mapped/Cresol.yaml)'
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
summary: Per-record structured review for Cresol (data/ingredients/mapped/Cresol.yaml,
  record-3803548af6670cfc, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Cresol.yaml
    sha256: 87886c72e9eb3d159db42f24a5dc514bd6bcb4eefda4bca206c16a9ef9e2feca
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
  - path: reports/yaml_record_review/Cresol.md
    sha256: 1a8a838d26da80bdab561806c7c657372130f75ae979d372a484b76f26e8fb1d
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-3803548af6670cfc
  path: data/ingredients/mapped/Cresol.yaml
  label: Cresol
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cresol.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Cresol.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Cresol.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-3803548af6670cfc
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-3803548af6670cfc
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-3803548af6670cfc
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-3803548af6670cfc
evidence:
- evidence_id: ev-51b2198171b6cefa
  kind: record_content
  reference: data/ingredients/mapped/Cresol.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2555],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:25399","line":2557,"mapping_status":"MAPPED","ontology_id":"CHEBI:25399","preferred_term":"Cresol"}],"identifier":"CHEBI:25399","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","match_level":"EXACT","ontology_id":"CHEBI:25399","ontology_label":"cresol","ontology_source":"CHEBI"},"preferred_term":"Cresol","sssom_rows":[{"data_row":830,"object_id":"CHEBI:25399","object_label":"cresol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cresol","synonym_count":0}'
  snapshot_sha256: 87886c72e9eb3d159db42f24a5dc514bd6bcb4eefda4bca206c16a9ef9e2feca
- evidence_id: ev-188ae876234d6e16
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2555]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-5a32c2f69a5979cc
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Cresol; data-row positions=[830]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":830,"object_id":"CHEBI:25399","object_label":"cresol","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Cresol","validation_method":"manual:claude_culturemech_residual_grounding|CREATED|2026-08-30"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-dfa7a9a51c9444f6
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2557]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:25399","line":2557,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:25399","preferred_term":"Cresol","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-a4ef484f8c4b1bd1
  kind: prior_review
  reference: reports/yaml_record_review/Cresol.md
  locator: '`data/ingredients/mapped/Cresol.yaml`:2; Verdict:4; Identity:12; Validation:24;
    Evidence:44; Completeness:58; Recommended Edits:66'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 1a8a838d26da80bdab561806c7c657372130f75ae979d372a484b76f26e8fb1d
  quote: "Recommended Edits:\n- Minor: recompute `Cresol` occurrence statistics from\
    \ the current CultureMech\n  occurrence table or residual grounding source, update\n\
    \  `mappings/culturemech_recipe_membership.tsv` so `CHEBI:25399` is represented,\n\
    \  and preserve the distinct `4-Cresol` counts under `CHEBI:17847`.\n- Regenerate\
    \ synchronized products and rerun strict validation, SSSOM QC,\n  aggregate roundtrip,\
    \ and `git diff --check`."
- evidence_id: ev-cde98821047b4383
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[445]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"87886c72e9eb3d159db42f24a5dc514bd6bcb4eefda4bca206c16a9ef9e2feca","finding_id":"SEM:b66edf88ea583849f19f","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-44d0685beeb01b7d
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-3803548af6670cfc
  evidence_ids:
  - ev-51b2198171b6cefa
  - ev-188ae876234d6e16
  - ev-5a32c2f69a5979cc
  - ev-dfa7a9a51c9444f6
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-2c0476bb1d5a9473
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-3803548af6670cfc
  evidence_ids:
  - ev-a4ef484f8c4b1bd1
  - ev-51b2198171b6cefa
  - ev-cde98821047b4383
  details: 'Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T12:38:48Z;
    reviewed SHA-256=87886c72e9eb3d159db42f24a5dc514bd6bcb4eefda4bca206c16a9ef9e2feca;
    current SHA-256=87886c72e9eb3d159db42f24a5dc514bd6bcb4eefda4bca206c16a9ef9e2feca;
    hash_changed=False. Reports=["reports/yaml_record_review/Cresol.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI cresol
    identity and SSSOM row pass, but the residual source has 3/3 occurrences while
    the record publishes 1/1 and no membership rows.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-a4ef484f8c4b1bd1
    - ev-51b2198171b6cefa
  - name: legacy-native-ids
    value: '["SEM:b66edf88ea583849f19f"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-51b2198171b6cefa
    - ev-a4ef484f8c4b1bd1
    - ev-cde98821047b4383
findings:
- finding_id: rec-f-b95f5fd3bcaa7e54
  issue_key: mim-reconciliation-historical-review-coverage-and-r-3803548af6670cfc
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Cresol'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T12:38:48Z;
    reviewed SHA-256=87886c72e9eb3d159db42f24a5dc514bd6bcb4eefda4bca206c16a9ef9e2feca;
    current SHA-256=87886c72e9eb3d159db42f24a5dc514bd6bcb4eefda4bca206c16a9ef9e2feca;
    hash_changed=False. Reports=["reports/yaml_record_review/Cresol.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI cresol
    identity and SSSOM row pass, but the residual source has 3/3 occurrences while
    the record publishes 1/1 and no membership rows.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-3803548af6670cfc
  evidence_ids:
  - ev-a4ef484f8c4b1bd1
  - ev-51b2198171b6cefa
  - ev-cde98821047b4383
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cresol.yaml
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
