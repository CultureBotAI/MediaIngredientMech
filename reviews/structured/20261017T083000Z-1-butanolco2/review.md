# Per-record structured review: 1-butanolCO2 (data/ingredients/mapped/1-butanolCO2.yaml)

- Review: 20261017T083000Z-1-butanolco2
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 1-butanolCO2 (data/ingredients/mapped/1-butanolCO2.yaml, record-1821bceb0fbf72d1, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/1-butanolCO2.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/1-butanolCO2.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-1821bceb0fbf72d1 | data/ingredients/mapped/1-butanolCO2.yaml | maintained | 1-butanolCO2 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-1821bceb0fbf72d1 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-1821bceb0fbf72d1 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-1821bceb0fbf72d1 | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-1821bceb0fbf72d1.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-1821bceb0fbf72d1.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T05:07:02Z; reviewed SHA-256=50e87c5ea60a056062c81c01bf5e8ea28a1dc8c8f8e3f20acb27a18ef7f5213d; current SHA-256=50e87c5ea60a056062c81c01bf5e8ea28a1dc8c8f8e3f20acb27a18ef7f5213d; hash_changed=False. Reports=["reports/yaml_record_review/1-butanolCO2.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Decomposition to local fallback with butan-1-ol and carbon dioxide components passes, but current notes still contain stale pre-resolution text.

## Findings

### rec-f-241598d6a85285ca: Historical review coverage and residual narrative: 1-butanolCO2

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-1821bceb0fbf72d1.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T05:07:02Z; reviewed SHA-256=50e87c5ea60a056062c81c01bf5e8ea28a1dc8c8f8e3f20acb27a18ef7f5213d; current SHA-256=50e87c5ea60a056062c81c01bf5e8ea28a1dc8c8f8e3f20acb27a18ef7f5213d; hash_changed=False. Reports=["reports/yaml_record_review/1-butanolCO2.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Decomposition to local fallback with butan-1-ol and carbon dioxide components passes, but current notes still contain stale pre-resolution text.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-77f03ca14b6effb1 | data/ingredients/mapped/1-butanolCO2.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[12],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:1_butanol_co2","line":14,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:1_butanol_co2","preferred_term":"1-butanol+CO2"}],"identifier":"kgmicrobe.ingredient:1_butanol_co2","ingredient_type":"NAMED_MEDIUM","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"bergey:substrates"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:1_butanol_co2","ontology_label":"1-butanol+CO2","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"1-butanol+CO2","sssom_rows":[{"data_row":14,"object_id":"kgmicrobe.ingredient:1_butanol_co2","object_label":"1-butanol+CO2","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:1-butanolCO2","synonym_count":1} |
| ev-8464981e98cb4806 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [12] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-7dd21a7c391fa728 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:1-butanolCO2; data-row positions=[14] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":14,"object_id":"kgmicrobe.ingredient:1_butanol_co2","object_label":"1-butanol+CO2","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:1-butanolCO2","validation_method":"manual:move_mapped_out_of_unmapped_collection&#124;MOVED&#124;2026-08-15"}] |
| ev-8a93a2cb325b8088 | docs/data/mapped_ingredients.csv; CSV lines=[14] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:1_butanol_co2","line":14,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:1_butanol_co2","preferred_term":"1-butanol+CO2","total_occurrences":"0"}] |
| ev-f3d1de4c8608c911 | reports/yaml_record_review/1-butanolCO2.md; &#96;data/ingredients/mapped/1-butanolCO2.yaml&#96;:2; Verdict:4; Identity:14; Validation:35; Evidence:64; Completeness:92; Recommended Edits:103 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-9e339e17a40250b7 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[15] | context_only | [{"current_record_sha256":"50e87c5ea60a056062c81c01bf5e8ea28a1dc8c8f8e3f20acb27a18ef7f5213d","finding_id":"SEM:f0b96f127101596a4c9d","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-1-butanolco2
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 1-butanolCO2 (data/ingredients/mapped/1-butanolCO2.yaml)'
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
summary: Per-record structured review for 1-butanolCO2 (data/ingredients/mapped/1-butanolCO2.yaml,
  record-1821bceb0fbf72d1, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/1-butanolCO2.yaml
    sha256: 50e87c5ea60a056062c81c01bf5e8ea28a1dc8c8f8e3f20acb27a18ef7f5213d
    role: target
  - path: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
    sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
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
  - path: reports/yaml_record_review/1-butanolCO2.md
    sha256: 643a903322c684ee3cd50c65222799ddab4551fa0b62c686e46ac9ed7604a471
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-1821bceb0fbf72d1
  path: data/ingredients/mapped/1-butanolCO2.yaml
  label: 1-butanolCO2
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/1-butanolCO2.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/1-butanolCO2.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/1-butanolCO2.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-1821bceb0fbf72d1
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-1821bceb0fbf72d1
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-1821bceb0fbf72d1
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-1821bceb0fbf72d1
evidence:
- evidence_id: ev-77f03ca14b6effb1
  kind: record_content
  reference: data/ingredients/mapped/1-butanolCO2.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[12],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:1_butanol_co2","line":14,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:1_butanol_co2","preferred_term":"1-butanol+CO2"}],"identifier":"kgmicrobe.ingredient:1_butanol_co2","ingredient_type":"NAMED_MEDIUM","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"bergey:substrates"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:1_butanol_co2","ontology_label":"1-butanol+CO2","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"1-butanol+CO2","sssom_rows":[{"data_row":14,"object_id":"kgmicrobe.ingredient:1_butanol_co2","object_label":"1-butanol+CO2","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:1-butanolCO2","synonym_count":1}'
  snapshot_sha256: 50e87c5ea60a056062c81c01bf5e8ea28a1dc8c8f8e3f20acb27a18ef7f5213d
- evidence_id: ev-8464981e98cb4806
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [12]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-7dd21a7c391fa728
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:1-butanolCO2; data-row positions=[14]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":14,"object_id":"kgmicrobe.ingredient:1_butanol_co2","object_label":"1-butanol+CO2","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:1-butanolCO2","validation_method":"manual:move_mapped_out_of_unmapped_collection|MOVED|2026-08-15"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-8a93a2cb325b8088
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[14]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:1_butanol_co2","line":14,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:1_butanol_co2","preferred_term":"1-butanol+CO2","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-f3d1de4c8608c911
  kind: prior_review
  reference: reports/yaml_record_review/1-butanolCO2.md
  locator: '`data/ingredients/mapped/1-butanolCO2.yaml`:2; Verdict:4; Identity:14;
    Validation:35; Evidence:64; Completeness:92; Recommended Edits:103'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 643a903322c684ee3cd50c65222799ddab4551fa0b62c686e46ac9ed7604a471
  quote: "Recommended Edits:\n1. Update `ontology_mapping.evidence[0].notes` in\n\
    \   `data/ingredients/mapped/1-butanolCO2.yaml` so it reflects the current\n \
    \  post-#369 state: both components resolved, both carry identifiers, and the\n\
    \   record type is `NAMED_MEDIUM`.\n2. Replace the stale top-level `notes` string\
    \ with a short note that the\n   MicrobeDecoder blend has already been reviewed,\
    \ decomposed to\n   `butan-1-ol` plus `carbon dioxide`, and moved to the mapped\
    \ collection.\n3. No identifier, component, `component_assertion`, mapping predicate,\
    \ SSSOM,\n   or docs edit is needed for the active\n   `kgmicrobe.ingredient:1_butanol_co2`\
    \ identity."
- evidence_id: ev-9e339e17a40250b7
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[15]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"50e87c5ea60a056062c81c01bf5e8ea28a1dc8c8f8e3f20acb27a18ef7f5213d","finding_id":"SEM:f0b96f127101596a4c9d","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-1d7e12ff8a006124
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-1821bceb0fbf72d1
  evidence_ids:
  - ev-77f03ca14b6effb1
  - ev-8464981e98cb4806
  - ev-7dd21a7c391fa728
  - ev-8a93a2cb325b8088
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-269d803c1786e622
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-1821bceb0fbf72d1
  evidence_ids:
  - ev-f3d1de4c8608c911
  - ev-77f03ca14b6effb1
  - ev-9e339e17a40250b7
  details: 'Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T05:07:02Z;
    reviewed SHA-256=50e87c5ea60a056062c81c01bf5e8ea28a1dc8c8f8e3f20acb27a18ef7f5213d;
    current SHA-256=50e87c5ea60a056062c81c01bf5e8ea28a1dc8c8f8e3f20acb27a18ef7f5213d;
    hash_changed=False. Reports=["reports/yaml_record_review/1-butanolCO2.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: Decomposition to
    local fallback with butan-1-ol and carbon dioxide components passes, but current
    notes still contain stale pre-resolution text.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f3d1de4c8608c911
    - ev-77f03ca14b6effb1
  - name: legacy-native-ids
    value: '["SEM:f0b96f127101596a4c9d"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-77f03ca14b6effb1
    - ev-f3d1de4c8608c911
    - ev-9e339e17a40250b7
findings:
- finding_id: rec-f-241598d6a85285ca
  issue_key: mim-reconciliation-historical-review-coverage-and-r-1821bceb0fbf72d1
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: 1-butanolCO2'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T05:07:02Z;
    reviewed SHA-256=50e87c5ea60a056062c81c01bf5e8ea28a1dc8c8f8e3f20acb27a18ef7f5213d;
    current SHA-256=50e87c5ea60a056062c81c01bf5e8ea28a1dc8c8f8e3f20acb27a18ef7f5213d;
    hash_changed=False. Reports=["reports/yaml_record_review/1-butanolCO2.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: Decomposition to
    local fallback with butan-1-ol and carbon dioxide components passes, but current
    notes still contain stale pre-resolution text.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-1821bceb0fbf72d1
  evidence_ids:
  - ev-f3d1de4c8608c911
  - ev-77f03ca14b6effb1
  - ev-9e339e17a40250b7
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/1-butanolCO2.yaml
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
  with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.
```
