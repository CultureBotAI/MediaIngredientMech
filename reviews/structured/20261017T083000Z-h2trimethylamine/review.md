# Per-record structured review: H2trimethylamine (data/ingredients/mapped/H2trimethylamine.yaml)

- Review: 20261017T083000Z-h2trimethylamine
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for H2trimethylamine (data/ingredients/mapped/H2trimethylamine.yaml, record-9b257865bb1d94d2, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/H2trimethylamine.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/H2trimethylamine.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-9b257865bb1d94d2 | data/ingredients/mapped/H2trimethylamine.yaml | maintained | H2trimethylamine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-9b257865bb1d94d2 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-9b257865bb1d94d2 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-9b257865bb1d94d2 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-9b257865bb1d94d2.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-9b257865bb1d94d2.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T18:58:35Z; reviewed SHA-256=6e2784721aeee54d35d3d4b85e970a39c94d98edfb1917596c52446016c2122e; current SHA-256=6e2784721aeee54d35d3d4b85e970a39c94d98edfb1917596c52446016c2122e; hash_changed=False. Reports=["reports/yaml_record_review/H2trimethylamine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local fallback identity and curated two-part decomposition pass, but stale notes still mention the old import state and DEFINED_MEDIUM value.

## Findings

### rec-f-2327e17034758fbd: Historical review coverage and residual narrative: H2trimethylamine

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-9b257865bb1d94d2.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T18:58:35Z; reviewed SHA-256=6e2784721aeee54d35d3d4b85e970a39c94d98edfb1917596c52446016c2122e; current SHA-256=6e2784721aeee54d35d3d4b85e970a39c94d98edfb1917596c52446016c2122e; hash_changed=False. Reports=["reports/yaml_record_review/H2trimethylamine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local fallback identity and curated two-part decomposition pass, but stale notes still mention the old import state and DEFINED_MEDIUM value.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-fe060be3919d1431 | data/ingredients/mapped/H2trimethylamine.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[45],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:h2_trimethylamine","line":47,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:h2_trimethylamine","preferred_term":"H2+trimethylamine"}],"identifier":"kgmicrobe.ingredient:h2_trimethylamine","ingredient_type":"NAMED_MEDIUM","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"bergey:substrates"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:h2_trimethylamine","ontology_label":"H2+trimethylamine","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"H2+trimethylamine","sssom_rows":[{"data_row":1394,"object_id":"kgmicrobe.ingredient:h2_trimethylamine","object_label":"H2+trimethylamine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:H2trimethylamine","synonym_count":1} |
| ev-9f0556216e57cb19 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [45] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-ee16fe008a15f7c4 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:H2trimethylamine; data-row positions=[1394] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1394,"object_id":"kgmicrobe.ingredient:h2_trimethylamine","object_label":"H2+trimethylamine","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:H2trimethylamine","validation_method":"manual:move_mapped_out_of_unmapped_collection&#124;MOVED&#124;2026-08-15"}] |
| ev-55bc9451aaeda856 | docs/data/mapped_ingredients.csv; CSV lines=[47] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:h2_trimethylamine","line":47,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:h2_trimethylamine","preferred_term":"H2+trimethylamine","total_occurrences":"0"}] |
| ev-f6c1f1e9303a85af | reports/yaml_record_review/H2trimethylamine.md; &#96;data/ingredients/mapped/H2trimethylamine.yaml&#96;:2; Verdict:4; Identity:11; Validation:24; Evidence:34; Completeness:51; Recommended Edits:58 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-d49713d6805fc5e8 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[717] | context_only | [{"current_record_sha256":"6e2784721aeee54d35d3d4b85e970a39c94d98edfb1917596c52446016c2122e","finding_id":"SEM:2a44b4f8c31235b613f4","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-h2trimethylamine
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: H2trimethylamine (data/ingredients/mapped/H2trimethylamine.yaml)'
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
summary: Per-record structured review for H2trimethylamine (data/ingredients/mapped/H2trimethylamine.yaml,
  record-9b257865bb1d94d2, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/H2trimethylamine.yaml
    sha256: 6e2784721aeee54d35d3d4b85e970a39c94d98edfb1917596c52446016c2122e
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
  - path: reports/yaml_record_review/H2trimethylamine.md
    sha256: e02d2d04f9fedac882bb4cc7c9c694f624149bc3462dc8a8a7ad677c05b3e9a7
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-9b257865bb1d94d2
  path: data/ingredients/mapped/H2trimethylamine.yaml
  label: H2trimethylamine
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/H2trimethylamine.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/H2trimethylamine.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/H2trimethylamine.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-9b257865bb1d94d2
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-9b257865bb1d94d2
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-9b257865bb1d94d2
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-9b257865bb1d94d2
evidence:
- evidence_id: ev-fe060be3919d1431
  kind: record_content
  reference: data/ingredients/mapped/H2trimethylamine.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[45],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:h2_trimethylamine","line":47,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:h2_trimethylamine","preferred_term":"H2+trimethylamine"}],"identifier":"kgmicrobe.ingredient:h2_trimethylamine","ingredient_type":"NAMED_MEDIUM","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"bergey:substrates"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:h2_trimethylamine","ontology_label":"H2+trimethylamine","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"H2+trimethylamine","sssom_rows":[{"data_row":1394,"object_id":"kgmicrobe.ingredient:h2_trimethylamine","object_label":"H2+trimethylamine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:H2trimethylamine","synonym_count":1}'
  snapshot_sha256: 6e2784721aeee54d35d3d4b85e970a39c94d98edfb1917596c52446016c2122e
- evidence_id: ev-9f0556216e57cb19
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [45]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-ee16fe008a15f7c4
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:H2trimethylamine; data-row positions=[1394]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1394,"object_id":"kgmicrobe.ingredient:h2_trimethylamine","object_label":"H2+trimethylamine","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:H2trimethylamine","validation_method":"manual:move_mapped_out_of_unmapped_collection|MOVED|2026-08-15"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-55bc9451aaeda856
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[47]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:h2_trimethylamine","line":47,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:h2_trimethylamine","preferred_term":"H2+trimethylamine","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-f6c1f1e9303a85af
  kind: prior_review
  reference: reports/yaml_record_review/H2trimethylamine.md
  locator: '`data/ingredients/mapped/H2trimethylamine.yaml`:2; Verdict:4; Identity:11;
    Validation:24; Evidence:34; Completeness:51; Recommended Edits:58'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: e02d2d04f9fedac882bb4cc7c9c694f624149bc3462dc8a8a7ad677c05b3e9a7
  quote: "Recommended Edits:\n- Minor: update top-level `notes` to summarize the accepted\
    \ local fallback and\n  curated two-component decomposition.\n- Minor: refresh\
    \ `ontology_mapping.evidence[0].notes` so the exact SSSOM\n  evidence no longer\
    \ mentions the old `DEFINED_MEDIUM` value."
- evidence_id: ev-d49713d6805fc5e8
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[717]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"6e2784721aeee54d35d3d4b85e970a39c94d98edfb1917596c52446016c2122e","finding_id":"SEM:2a44b4f8c31235b613f4","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-50aa5d5ba293182a
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-9b257865bb1d94d2
  evidence_ids:
  - ev-fe060be3919d1431
  - ev-9f0556216e57cb19
  - ev-ee16fe008a15f7c4
  - ev-55bc9451aaeda856
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-a16b77a7fb26a9b3
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-9b257865bb1d94d2
  evidence_ids:
  - ev-f6c1f1e9303a85af
  - ev-fe060be3919d1431
  - ev-d49713d6805fc5e8
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T18:58:35Z;
    reviewed SHA-256=6e2784721aeee54d35d3d4b85e970a39c94d98edfb1917596c52446016c2122e;
    current SHA-256=6e2784721aeee54d35d3d4b85e970a39c94d98edfb1917596c52446016c2122e;
    hash_changed=False. Reports=["reports/yaml_record_review/H2trimethylamine.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    fallback identity and curated two-part decomposition pass, but stale notes still
    mention the old import state and DEFINED_MEDIUM value.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f6c1f1e9303a85af
    - ev-fe060be3919d1431
  - name: legacy-native-ids
    value: '["SEM:2a44b4f8c31235b613f4"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-fe060be3919d1431
    - ev-f6c1f1e9303a85af
    - ev-d49713d6805fc5e8
findings:
- finding_id: rec-f-2327e17034758fbd
  issue_key: mim-reconciliation-historical-review-coverage-and-r-9b257865bb1d94d2
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: H2trimethylamine'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T18:58:35Z;
    reviewed SHA-256=6e2784721aeee54d35d3d4b85e970a39c94d98edfb1917596c52446016c2122e;
    current SHA-256=6e2784721aeee54d35d3d4b85e970a39c94d98edfb1917596c52446016c2122e;
    hash_changed=False. Reports=["reports/yaml_record_review/H2trimethylamine.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    fallback identity and curated two-part decomposition pass, but stale notes still
    mention the old import state and DEFINED_MEDIUM value.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-9b257865bb1d94d2
  evidence_ids:
  - ev-f6c1f1e9303a85af
  - ev-fe060be3919d1431
  - ev-d49713d6805fc5e8
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/H2trimethylamine.yaml
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
