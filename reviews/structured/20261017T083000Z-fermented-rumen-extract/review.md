# Per-record structured review: Fermented_Rumen_Extract (data/ingredients/mapped/Fermented_Rumen_Extract.yaml)

- Review: 20261017T083000Z-fermented-rumen-extract
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Fermented_Rumen_Extract (data/ingredients/mapped/Fermented_Rumen_Extract.yaml, record-081b6627b5aee2ee, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Fermented_Rumen_Extract.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Fermented_Rumen_Extract.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-081b6627b5aee2ee | data/ingredients/mapped/Fermented_Rumen_Extract.yaml | maintained | Fermented_Rumen_Extract |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-081b6627b5aee2ee | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-081b6627b5aee2ee | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-081b6627b5aee2ee | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-081b6627b5aee2ee.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-081b6627b5aee2ee.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T16:19:32Z; reviewed SHA-256=68606cf3a121f3937468204907878a64aefc896fef3b4c185d562aa6715f4f5a; current SHA-256=68606cf3a121f3937468204907878a64aefc896fef3b4c185d562aa6715f4f5a; hash_changed=False. Reports=["reports/yaml_record_review/Fermented_Rumen_Extract.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local fermented-rumen-extract registry identity passes, but top-level notes still carry stale import-era review text.

## Findings

### rec-f-e8e5e6207c649f25: Historical review coverage and residual narrative: Fermented_Rumen_Extract

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-081b6627b5aee2ee.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T16:19:32Z; reviewed SHA-256=68606cf3a121f3937468204907878a64aefc896fef3b4c185d562aa6715f4f5a; current SHA-256=68606cf3a121f3937468204907878a64aefc896fef3b4c185d562aa6715f4f5a; hash_changed=False. Reports=["reports/yaml_record_review/Fermented_Rumen_Extract.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local fermented-rumen-extract registry identity passes, but top-level notes still carry stale import-era review text.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-c6a8ea308a27cf95 | data/ingredients/mapped/Fermented_Rumen_Extract.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[24],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:fermented_rumen_extract","line":26,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:fermented_rumen_extract","preferred_term":"Fermented Rumen Extract"}],"identifier":"kgmicrobe.ingredient:fermented_rumen_extract","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":3,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:fermented_rumen_extract","ontology_label":"Fermented Rumen Extract","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Fermented Rumen Extract","sssom_rows":[{"data_row":1185,"object_id":"kgmicrobe.ingredient:fermented_rumen_extract","object_label":"Fermented Rumen Extract","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fermented_Rumen_Extract","synonym_count":1} |
| ev-fc3e8e2d75a31d70 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [24] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-f8b06a0cd2b2ec95 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Fermented_Rumen_Extract; data-row positions=[1185] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1185,"object_id":"kgmicrobe.ingredient:fermented_rumen_extract","object_label":"Fermented Rumen Extract","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Fermented_Rumen_Extract","validation_method":"manual:move_mapped_out_of_unmapped_collection&#124;MOVED&#124;2026-08-15"}] |
| ev-050e57ea559b3638 | docs/data/mapped_ingredients.csv; CSV lines=[26] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:fermented_rumen_extract","line":26,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:fermented_rumen_extract","preferred_term":"Fermented Rumen Extract","total_occurrences":"0"}] |
| ev-643be828efebd98c | reports/yaml_record_review/Fermented_Rumen_Extract.md; &#96;data/ingredients/mapped/Fermented_Rumen_Extract.yaml&#96;:2; Verdict:4; Identity:12; Validation:28; Evidence:39; Completeness:66; Recommended Edits:75 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-a5f3fe2273caef2d | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[596] | context_only | [{"current_record_sha256":"68606cf3a121f3937468204907878a64aefc896fef3b4c185d562aa6715f4f5a","finding_id":"SEM:a3915b03b3414b046186","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-fermented-rumen-extract
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Fermented_Rumen_Extract (data/ingredients/mapped/Fermented_Rumen_Extract.yaml)'
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
summary: Per-record structured review for Fermented_Rumen_Extract (data/ingredients/mapped/Fermented_Rumen_Extract.yaml,
  record-081b6627b5aee2ee, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Fermented_Rumen_Extract.yaml
    sha256: 68606cf3a121f3937468204907878a64aefc896fef3b4c185d562aa6715f4f5a
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
  - path: reports/yaml_record_review/Fermented_Rumen_Extract.md
    sha256: 8be2d2211c0fbc3e830a9f4a1cd48d1820588201dca8edce50ea6df5bd4f2af0
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-081b6627b5aee2ee
  path: data/ingredients/mapped/Fermented_Rumen_Extract.yaml
  label: Fermented_Rumen_Extract
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fermented_Rumen_Extract.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Fermented_Rumen_Extract.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Fermented_Rumen_Extract.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-081b6627b5aee2ee
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-081b6627b5aee2ee
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-081b6627b5aee2ee
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-081b6627b5aee2ee
evidence:
- evidence_id: ev-c6a8ea308a27cf95
  kind: record_content
  reference: data/ingredients/mapped/Fermented_Rumen_Extract.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[24],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:fermented_rumen_extract","line":26,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:fermented_rumen_extract","preferred_term":"Fermented
    Rumen Extract"}],"identifier":"kgmicrobe.ingredient:fermented_rumen_extract","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":3,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:fermented_rumen_extract","ontology_label":"Fermented
    Rumen Extract","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Fermented
    Rumen Extract","sssom_rows":[{"data_row":1185,"object_id":"kgmicrobe.ingredient:fermented_rumen_extract","object_label":"Fermented
    Rumen Extract","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fermented_Rumen_Extract","synonym_count":1}'
  snapshot_sha256: 68606cf3a121f3937468204907878a64aefc896fef3b4c185d562aa6715f4f5a
- evidence_id: ev-fc3e8e2d75a31d70
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [24]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-f8b06a0cd2b2ec95
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Fermented_Rumen_Extract; data-row positions=[1185]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1185,"object_id":"kgmicrobe.ingredient:fermented_rumen_extract","object_label":"Fermented
    Rumen Extract","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Fermented_Rumen_Extract","validation_method":"manual:move_mapped_out_of_unmapped_collection|MOVED|2026-08-15"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-050e57ea559b3638
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[26]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:fermented_rumen_extract","line":26,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:fermented_rumen_extract","preferred_term":"Fermented
    Rumen Extract","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-643be828efebd98c
  kind: prior_review
  reference: reports/yaml_record_review/Fermented_Rumen_Extract.md
  locator: '`data/ingredients/mapped/Fermented_Rumen_Extract.yaml`:2; Verdict:4; Identity:12;
    Validation:28; Evidence:39; Completeness:66; Recommended Edits:75'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 8be2d2211c0fbc3e830a9f4a1cd48d1820588201dca8edce50ea6df5bd4f2af0
  quote: "Recommended Edits:\n- Minor: replace the stale import-era top-level `notes`\
    \ in\n  `data/ingredients/mapped/Fermented_Rumen_Extract.yaml`, sync\n  `data/curated/mapped_ingredients.yaml`,\
    \ and rerun strict validation plus the\n  roundtrip gate."
- evidence_id: ev-a5f3fe2273caef2d
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[596]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"68606cf3a121f3937468204907878a64aefc896fef3b4c185d562aa6715f4f5a","finding_id":"SEM:a3915b03b3414b046186","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-12b06e7b55de4163
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-081b6627b5aee2ee
  evidence_ids:
  - ev-c6a8ea308a27cf95
  - ev-fc3e8e2d75a31d70
  - ev-f8b06a0cd2b2ec95
  - ev-050e57ea559b3638
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-619baf1ab197e05b
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-081b6627b5aee2ee
  evidence_ids:
  - ev-643be828efebd98c
  - ev-c6a8ea308a27cf95
  - ev-a5f3fe2273caef2d
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T16:19:32Z;
    reviewed SHA-256=68606cf3a121f3937468204907878a64aefc896fef3b4c185d562aa6715f4f5a;
    current SHA-256=68606cf3a121f3937468204907878a64aefc896fef3b4c185d562aa6715f4f5a;
    hash_changed=False. Reports=["reports/yaml_record_review/Fermented_Rumen_Extract.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    fermented-rumen-extract registry identity passes, but top-level notes still carry
    stale import-era review text.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-643be828efebd98c
    - ev-c6a8ea308a27cf95
  - name: legacy-native-ids
    value: '["SEM:a3915b03b3414b046186"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-c6a8ea308a27cf95
    - ev-643be828efebd98c
    - ev-a5f3fe2273caef2d
findings:
- finding_id: rec-f-e8e5e6207c649f25
  issue_key: mim-reconciliation-historical-review-coverage-and-r-081b6627b5aee2ee
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Fermented_Rumen_Extract'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T16:19:32Z;
    reviewed SHA-256=68606cf3a121f3937468204907878a64aefc896fef3b4c185d562aa6715f4f5a;
    current SHA-256=68606cf3a121f3937468204907878a64aefc896fef3b4c185d562aa6715f4f5a;
    hash_changed=False. Reports=["reports/yaml_record_review/Fermented_Rumen_Extract.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    fermented-rumen-extract registry identity passes, but top-level notes still carry
    stale import-era review text.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-081b6627b5aee2ee
  evidence_ids:
  - ev-643be828efebd98c
  - ev-c6a8ea308a27cf95
  - ev-a5f3fe2273caef2d
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fermented_Rumen_Extract.yaml
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
