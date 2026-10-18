# Per-record structured review: Glutarate (data/ingredients/mapped/Glutarate.yaml)

- Review: 20261017T083000Z-glutarate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Glutarate (data/ingredients/mapped/Glutarate.yaml, record-0e4d87c9113236d7, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Glutarate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Glutarate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-0e4d87c9113236d7 | data/ingredients/mapped/Glutarate.yaml | maintained | Glutarate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-0e4d87c9113236d7 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-0e4d87c9113236d7 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-0e4d87c9113236d7 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-0e4d87c9113236d7.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-0e4d87c9113236d7.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T17:59:15Z; reviewed SHA-256=7135ef010e6e0231e04e7e9d5dbade037949fc49f81a0ae6104ba8ef9020b624; current SHA-256=7135ef010e6e0231e04e7e9d5dbade037949fc49f81a0ae6104ba8ef9020b624; hash_changed=False. Reports=["reports/yaml_record_review/Glutarate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact glutarate identity and final SSSOM row pass, but ingredient type and structure fields need backfill.

## Findings

### rec-f-00de7eb7be6d5616: Historical review coverage and residual narrative: Glutarate

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-0e4d87c9113236d7.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T17:59:15Z; reviewed SHA-256=7135ef010e6e0231e04e7e9d5dbade037949fc49f81a0ae6104ba8ef9020b624; current SHA-256=7135ef010e6e0231e04e7e9d5dbade037949fc49f81a0ae6104ba8ef9020b624; hash_changed=False. Reports=["reports/yaml_record_review/Glutarate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact glutarate identity and final SSSOM row pass, but ingredient type and structure fields need backfill.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-6da93504a202b2cc | data/ingredients/mapped/Glutarate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2290],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:24329","line":2292,"mapping_status":"MAPPED","ontology_id":"CHEBI:24329","preferred_term":"Glutarate"}],"identifier":"CHEBI:24329","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:24329","ontology_label":"glutarate","ontology_source":"CHEBI"},"preferred_term":"Glutarate","sssom_rows":[{"data_row":1324,"object_id":"CHEBI:24329","object_label":"glutarate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glutarate","synonym_count":0} |
| ev-13e4f9c6474522a6 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2290] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-9ae5a21ea929aee6 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Glutarate; data-row positions=[1324] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1324,"object_id":"CHEBI:24329","object_label":"glutarate","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Glutarate","validation_method":"manual:review-ingredients&#124;APPROVED&#124;2026-08-04"}] |
| ev-1451816e370478e2 | docs/data/mapped_ingredients.csv; CSV lines=[2292] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:24329","line":2292,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:24329","preferred_term":"Glutarate","total_occurrences":"0"}] |
| ev-724b7340f356d059 | reports/yaml_record_review/Glutarate.md; &#96;data/ingredients/mapped/Glutarate.yaml&#96;:2; Verdict:4; Identity:11; Validation:18; Evidence:30; Completeness:52; Recommended Edits:58 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-f3517bee0779ad3d | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[681] | context_only | [{"current_record_sha256":"7135ef010e6e0231e04e7e9d5dbade037949fc49f81a0ae6104ba8ef9020b624","finding_id":"SEM:4d8e1747809d6a5e268e","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-glutarate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Glutarate (data/ingredients/mapped/Glutarate.yaml)'
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
summary: Per-record structured review for Glutarate (data/ingredients/mapped/Glutarate.yaml,
  record-0e4d87c9113236d7, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Glutarate.yaml
    sha256: 7135ef010e6e0231e04e7e9d5dbade037949fc49f81a0ae6104ba8ef9020b624
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
  - path: reports/yaml_record_review/Glutarate.md
    sha256: d0325528ffd9da20b03e35795f06597298314962291aca35fa14c8adac2078f6
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-0e4d87c9113236d7
  path: data/ingredients/mapped/Glutarate.yaml
  label: Glutarate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glutarate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Glutarate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Glutarate.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-0e4d87c9113236d7
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-0e4d87c9113236d7
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-0e4d87c9113236d7
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-0e4d87c9113236d7
evidence:
- evidence_id: ev-6da93504a202b2cc
  kind: record_content
  reference: data/ingredients/mapped/Glutarate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2290],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:24329","line":2292,"mapping_status":"MAPPED","ontology_id":"CHEBI:24329","preferred_term":"Glutarate"}],"identifier":"CHEBI:24329","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:24329","ontology_label":"glutarate","ontology_source":"CHEBI"},"preferred_term":"Glutarate","sssom_rows":[{"data_row":1324,"object_id":"CHEBI:24329","object_label":"glutarate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glutarate","synonym_count":0}'
  snapshot_sha256: 7135ef010e6e0231e04e7e9d5dbade037949fc49f81a0ae6104ba8ef9020b624
- evidence_id: ev-13e4f9c6474522a6
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2290]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-9ae5a21ea929aee6
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Glutarate; data-row positions=[1324]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1324,"object_id":"CHEBI:24329","object_label":"glutarate","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Glutarate","validation_method":"manual:review-ingredients|APPROVED|2026-08-04"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-1451816e370478e2
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2292]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:24329","line":2292,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:24329","preferred_term":"Glutarate","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-724b7340f356d059
  kind: prior_review
  reference: reports/yaml_record_review/Glutarate.md
  locator: '`data/ingredients/mapped/Glutarate.yaml`:2; Verdict:4; Identity:11; Validation:18;
    Evidence:30; Completeness:52; Recommended Edits:58'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: d0325528ffd9da20b03e35795f06597298314962291aca35fa14c8adac2078f6
  quote: "Recommended Edits:\n- Minor: add `ingredient_type: SINGLE_INGREDIENT` to\n\
    \  `data/ingredients/mapped/Glutarate.yaml`.\n- Minor: backfill `chemical_properties`\
    \ from `CHEBI:24329` if ChEBI exposes a\n  structure for the exact term."
- evidence_id: ev-f3517bee0779ad3d
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[681]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"7135ef010e6e0231e04e7e9d5dbade037949fc49f81a0ae6104ba8ef9020b624","finding_id":"SEM:4d8e1747809d6a5e268e","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-eecfce2cb36d52c6
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-0e4d87c9113236d7
  evidence_ids:
  - ev-6da93504a202b2cc
  - ev-13e4f9c6474522a6
  - ev-9ae5a21ea929aee6
  - ev-1451816e370478e2
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-9a22ac87037f0fa4
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-0e4d87c9113236d7
  evidence_ids:
  - ev-724b7340f356d059
  - ev-6da93504a202b2cc
  - ev-f3517bee0779ad3d
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T17:59:15Z;
    reviewed SHA-256=7135ef010e6e0231e04e7e9d5dbade037949fc49f81a0ae6104ba8ef9020b624;
    current SHA-256=7135ef010e6e0231e04e7e9d5dbade037949fc49f81a0ae6104ba8ef9020b624;
    hash_changed=False. Reports=["reports/yaml_record_review/Glutarate.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact glutarate
    identity and final SSSOM row pass, but ingredient type and structure fields need
    backfill.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-724b7340f356d059
    - ev-6da93504a202b2cc
  - name: legacy-native-ids
    value: '["SEM:4d8e1747809d6a5e268e"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-6da93504a202b2cc
    - ev-724b7340f356d059
    - ev-f3517bee0779ad3d
findings:
- finding_id: rec-f-00de7eb7be6d5616
  issue_key: mim-reconciliation-historical-review-coverage-and-r-0e4d87c9113236d7
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Glutarate'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T17:59:15Z;
    reviewed SHA-256=7135ef010e6e0231e04e7e9d5dbade037949fc49f81a0ae6104ba8ef9020b624;
    current SHA-256=7135ef010e6e0231e04e7e9d5dbade037949fc49f81a0ae6104ba8ef9020b624;
    hash_changed=False. Reports=["reports/yaml_record_review/Glutarate.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact glutarate
    identity and final SSSOM row pass, but ingredient type and structure fields need
    backfill.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-0e4d87c9113236d7
  evidence_ids:
  - ev-724b7340f356d059
  - ev-6da93504a202b2cc
  - ev-f3517bee0779ad3d
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glutarate.yaml
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
