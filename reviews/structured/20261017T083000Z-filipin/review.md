# Per-record structured review: Filipin (data/ingredients/mapped/Filipin.yaml)

- Review: 20261017T083000Z-filipin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Filipin (data/ingredients/mapped/Filipin.yaml, record-b44eea43cb5eb807, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Filipin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Filipin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-b44eea43cb5eb807 | data/ingredients/mapped/Filipin.yaml | maintained | Filipin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-b44eea43cb5eb807 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-b44eea43cb5eb807 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-b44eea43cb5eb807 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-b44eea43cb5eb807.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-b44eea43cb5eb807.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T16:41:08Z; reviewed SHA-256=724237ffa72c839e92c25e6a587329ed45a7f1bd387057582578ac03d5a33d83; current SHA-256=724237ffa72c839e92c25e6a587329ed45a7f1bd387057582578ac03d5a33d83; hash_changed=False. Reports=["reports/yaml_record_review/Filipin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact MeSH filipin-complex identity and final SSSOM row pass, but the antibiotic mixture is missing ingredient_type.

## Findings

### rec-f-f67b409f2256ecc5: Historical review coverage and residual narrative: Filipin

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-b44eea43cb5eb807.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T16:41:08Z; reviewed SHA-256=724237ffa72c839e92c25e6a587329ed45a7f1bd387057582578ac03d5a33d83; current SHA-256=724237ffa72c839e92c25e6a587329ed45a7f1bd387057582578ac03d5a33d83; hash_changed=False. Reports=["reports/yaml_record_review/Filipin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact MeSH filipin-complex identity and final SSSOM row pass, but the antibiotic mixture is missing ingredient_type.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-e3bc47032ae3928d | data/ingredients/mapped/Filipin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[172],"raw_equal":true},"docs_rows":[{"identifier":"mesh:D005372","line":174,"mapping_status":"MAPPED","ontology_id":"mesh:D005372","preferred_term":"Filipin"}],"identifier":"mesh:D005372","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"BacDive_Metabolite_production"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:D005372","ontology_label":"Filipin","ontology_source":"MESH"},"preferred_term":"Filipin","sssom_rows":[{"data_row":1210,"object_id":"mesh:D005372","object_label":"Filipin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Filipin","synonym_count":1} |
| ev-45f9eedf8477f8d0 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [172] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-ddc438e90657ecb8 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Filipin; data-row positions=[1210] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1210,"object_id":"mesh:D005372","object_label":"Filipin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Filipin","validation_method":"manual:promote_resolved_unmapped&#124;PROMOTED&#124;2026-08-06"}] |
| ev-4aca499347298f95 | docs/data/mapped_ingredients.csv; CSV lines=[174] | supports | Published identity and count rows inspected: [{"identifier":"mesh:D005372","line":174,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:D005372","preferred_term":"Filipin","total_occurrences":"0"}] |
| ev-a7efb04426538c3a | reports/yaml_record_review/Filipin.md; &#96;data/ingredients/mapped/Filipin.yaml&#96;:2; Verdict:4; Identity:11; Validation:23; Evidence:33; Completeness:58; Recommended Edits:66 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-c6b9281cdb6ac679 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[616] | context_only | [{"current_record_sha256":"724237ffa72c839e92c25e6a587329ed45a7f1bd387057582578ac03d5a33d83","finding_id":"SEM:366937f89d07fd938646","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-filipin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Filipin (data/ingredients/mapped/Filipin.yaml)'
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
summary: Per-record structured review for Filipin (data/ingredients/mapped/Filipin.yaml,
  record-b44eea43cb5eb807, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Filipin.yaml
    sha256: 724237ffa72c839e92c25e6a587329ed45a7f1bd387057582578ac03d5a33d83
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
  - path: reports/yaml_record_review/Filipin.md
    sha256: 186b83ccf439b162396a8df7d2c2be0496cb0d1f01bb11bfc7957a904521d7ca
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-b44eea43cb5eb807
  path: data/ingredients/mapped/Filipin.yaml
  label: Filipin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Filipin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Filipin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Filipin.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-b44eea43cb5eb807
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-b44eea43cb5eb807
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-b44eea43cb5eb807
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-b44eea43cb5eb807
evidence:
- evidence_id: ev-e3bc47032ae3928d
  kind: record_content
  reference: data/ingredients/mapped/Filipin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[172],"raw_equal":true},"docs_rows":[{"identifier":"mesh:D005372","line":174,"mapping_status":"MAPPED","ontology_id":"mesh:D005372","preferred_term":"Filipin"}],"identifier":"mesh:D005372","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"BacDive_Metabolite_production"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:D005372","ontology_label":"Filipin","ontology_source":"MESH"},"preferred_term":"Filipin","sssom_rows":[{"data_row":1210,"object_id":"mesh:D005372","object_label":"Filipin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Filipin","synonym_count":1}'
  snapshot_sha256: 724237ffa72c839e92c25e6a587329ed45a7f1bd387057582578ac03d5a33d83
- evidence_id: ev-45f9eedf8477f8d0
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [172]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-ddc438e90657ecb8
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Filipin; data-row positions=[1210]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1210,"object_id":"mesh:D005372","object_label":"Filipin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Filipin","validation_method":"manual:promote_resolved_unmapped|PROMOTED|2026-08-06"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-4aca499347298f95
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[174]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"mesh:D005372","line":174,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:D005372","preferred_term":"Filipin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-a7efb04426538c3a
  kind: prior_review
  reference: reports/yaml_record_review/Filipin.md
  locator: '`data/ingredients/mapped/Filipin.yaml`:2; Verdict:4; Identity:11; Validation:23;
    Evidence:33; Completeness:58; Recommended Edits:66'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 186b83ccf439b162396a8df7d2c2be0496cb0d1f01bb11bfc7957a904521d7ca
  quote: "Recommended Edits:\n- Minor: set the curator-confirmed `ingredient_type`,\
    \ likely\n  `UNDEFINED_MIXTURE`, in `data/ingredients/mapped/Filipin.yaml`; while\n\
    \  touching the record, remove stale top-level review notes, sync\n  `data/curated/mapped_ingredients.yaml`,\
    \ and rerun strict validation plus the\n  final SSSOM invariant gates."
- evidence_id: ev-c6b9281cdb6ac679
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[616]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"724237ffa72c839e92c25e6a587329ed45a7f1bd387057582578ac03d5a33d83","finding_id":"SEM:366937f89d07fd938646","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-1342d79ca1dc843a
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-b44eea43cb5eb807
  evidence_ids:
  - ev-e3bc47032ae3928d
  - ev-45f9eedf8477f8d0
  - ev-ddc438e90657ecb8
  - ev-4aca499347298f95
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-45392cfabb67229e
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-b44eea43cb5eb807
  evidence_ids:
  - ev-a7efb04426538c3a
  - ev-e3bc47032ae3928d
  - ev-c6b9281cdb6ac679
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T16:41:08Z;
    reviewed SHA-256=724237ffa72c839e92c25e6a587329ed45a7f1bd387057582578ac03d5a33d83;
    current SHA-256=724237ffa72c839e92c25e6a587329ed45a7f1bd387057582578ac03d5a33d83;
    hash_changed=False. Reports=["reports/yaml_record_review/Filipin.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact MeSH filipin-complex
    identity and final SSSOM row pass, but the antibiotic mixture is missing ingredient_type.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-a7efb04426538c3a
    - ev-e3bc47032ae3928d
  - name: legacy-native-ids
    value: '["SEM:366937f89d07fd938646"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-e3bc47032ae3928d
    - ev-a7efb04426538c3a
    - ev-c6b9281cdb6ac679
findings:
- finding_id: rec-f-f67b409f2256ecc5
  issue_key: mim-reconciliation-historical-review-coverage-and-r-b44eea43cb5eb807
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Filipin'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T16:41:08Z;
    reviewed SHA-256=724237ffa72c839e92c25e6a587329ed45a7f1bd387057582578ac03d5a33d83;
    current SHA-256=724237ffa72c839e92c25e6a587329ed45a7f1bd387057582578ac03d5a33d83;
    hash_changed=False. Reports=["reports/yaml_record_review/Filipin.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact MeSH filipin-complex
    identity and final SSSOM row pass, but the antibiotic mixture is missing ingredient_type.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-b44eea43cb5eb807
  evidence_ids:
  - ev-a7efb04426538c3a
  - ev-e3bc47032ae3928d
  - ev-c6b9281cdb6ac679
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Filipin.yaml
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
