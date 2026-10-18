# Per-record structured review: Heart_Infusion_Agar_BD_211065 (data/ingredients/mapped/Heart_Infusion_Agar_BD_211065.yaml)

- Review: 20261017T083000Z-heart-infusion-agar-bd-211065
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Heart_Infusion_Agar_BD_211065 (data/ingredients/mapped/Heart_Infusion_Agar_BD_211065.yaml, record-d7087ebb95882c08, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Heart_Infusion_Agar_BD_211065.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Heart_Infusion_Agar_BD_211065.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-d7087ebb95882c08 | data/ingredients/mapped/Heart_Infusion_Agar_BD_211065.yaml | maintained | Heart_Infusion_Agar_BD_211065 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-d7087ebb95882c08 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-d7087ebb95882c08 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-d7087ebb95882c08 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-d7087ebb95882c08.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-d7087ebb95882c08.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T19:09:40Z; reviewed SHA-256=1ca2d82b3de84d05372ed220e9d8face54d79c34b6593bb15a64f97f3a66628d; current SHA-256=1ca2d82b3de84d05372ed220e9d8face54d79c34b6593bb15a64f97f3a66628d; hash_changed=False. Reports=["reports/yaml_record_review/Heart_Infusion_Agar_BD_211065.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The generic MICRO target is active, but the record erases BD/Difco/Eiken catalog-specific boundaries.

## Findings

### rec-f-3dae36ed2474026d: Historical review coverage and residual narrative: Heart_Infusion_Agar_BD_211065

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-d7087ebb95882c08.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T19:09:40Z; reviewed SHA-256=1ca2d82b3de84d05372ed220e9d8face54d79c34b6593bb15a64f97f3a66628d; current SHA-256=1ca2d82b3de84d05372ed220e9d8face54d79c34b6593bb15a64f97f3a66628d; hash_changed=False. Reports=["reports/yaml_record_review/Heart_Infusion_Agar_BD_211065.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The generic MICRO target is active, but the record erases BD/Difco/Eiken catalog-specific boundaries.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-47551c5142c6473b | data/ingredients/mapped/Heart_Infusion_Agar_BD_211065.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2568],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0000567","line":2570,"mapping_status":"MAPPED","ontology_id":"MICRO:0000567","preferred_term":"Heart Infusion Agar (BD 211065)"}],"identifier":"MICRO:0000567","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","match_level":"NORMALIZED","ontology_id":"MICRO:0000567","ontology_label":"heart infusion agar","ontology_source":"MICRO"},"preferred_term":"Heart Infusion Agar (BD 211065)","sssom_rows":[{"data_row":1411,"object_id":"MICRO:0000567","object_label":"heart infusion agar","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Heart_Infusion_Agar_BD_211065","synonym_count":2} |
| ev-fb3f171cf0414c9c | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2568] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-74fd07c5c8ee2922 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Heart_Infusion_Agar_BD_211065; data-row positions=[1411] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1411,"object_id":"MICRO:0000567","object_label":"heart infusion agar","other":"Heart Infusion Agar (Difco)&#124;Heart infusion agar (Eiken)","predicate_id":"skos:exactMatch","subject_id":"MIM:Heart_Infusion_Agar_BD_211065","validation_method":"manual:claude_culturemech_residual_grounding&#124;CREATED&#124;2026-08-30"}] |
| ev-1dfb10cdf4b64ff0 | docs/data/mapped_ingredients.csv; CSV lines=[2570] | supports | Published identity and count rows inspected: [{"identifier":"MICRO:0000567","line":2570,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"MICRO:0000567","preferred_term":"Heart Infusion Agar (BD 211065)","total_occurrences":"1"}] |
| ev-96dcf339e59e3e31 | reports/yaml_record_review/Heart_Infusion_Agar_BD_211065.md; &#96;data/ingredients/mapped/Heart_Infusion_Agar_BD_211065.yaml&#96;:2; Verdict:4; Identity:10; Validation:20; Evidence:29; Completeness:44; Recommended Edits:50 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-69d6e2631b79acf0 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[725] | context_only | [{"current_record_sha256":"1ca2d82b3de84d05372ed220e9d8face54d79c34b6593bb15a64f97f3a66628d","finding_id":"SEM:bc4df8ffe0eed9576a7b","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-heart-infusion-agar-bd-211065
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Heart_Infusion_Agar_BD_211065 (data/ingredients/mapped/Heart_Infusion_Agar_BD_211065.yaml)'
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
summary: Per-record structured review for Heart_Infusion_Agar_BD_211065 (data/ingredients/mapped/Heart_Infusion_Agar_BD_211065.yaml,
  record-d7087ebb95882c08, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Heart_Infusion_Agar_BD_211065.yaml
    sha256: 1ca2d82b3de84d05372ed220e9d8face54d79c34b6593bb15a64f97f3a66628d
    role: target
  - path: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
    sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
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
  - path: reports/yaml_record_review/Heart_Infusion_Agar_BD_211065.md
    sha256: a602e2e0aeb423e218f68ee5f533d06a675b68acca3661d09f9be38205abbb3c
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-d7087ebb95882c08
  path: data/ingredients/mapped/Heart_Infusion_Agar_BD_211065.yaml
  label: Heart_Infusion_Agar_BD_211065
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Heart_Infusion_Agar_BD_211065.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Heart_Infusion_Agar_BD_211065.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Heart_Infusion_Agar_BD_211065.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-d7087ebb95882c08
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-d7087ebb95882c08
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-d7087ebb95882c08
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-d7087ebb95882c08
evidence:
- evidence_id: ev-47551c5142c6473b
  kind: record_content
  reference: data/ingredients/mapped/Heart_Infusion_Agar_BD_211065.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2568],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0000567","line":2570,"mapping_status":"MAPPED","ontology_id":"MICRO:0000567","preferred_term":"Heart
    Infusion Agar (BD 211065)"}],"identifier":"MICRO:0000567","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","match_level":"NORMALIZED","ontology_id":"MICRO:0000567","ontology_label":"heart
    infusion agar","ontology_source":"MICRO"},"preferred_term":"Heart Infusion Agar
    (BD 211065)","sssom_rows":[{"data_row":1411,"object_id":"MICRO:0000567","object_label":"heart
    infusion agar","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Heart_Infusion_Agar_BD_211065","synonym_count":2}'
  snapshot_sha256: 1ca2d82b3de84d05372ed220e9d8face54d79c34b6593bb15a64f97f3a66628d
- evidence_id: ev-fb3f171cf0414c9c
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2568]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-74fd07c5c8ee2922
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Heart_Infusion_Agar_BD_211065; data-row positions=[1411]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1411,"object_id":"MICRO:0000567","object_label":"heart
    infusion agar","other":"Heart Infusion Agar (Difco)|Heart infusion agar (Eiken)","predicate_id":"skos:exactMatch","subject_id":"MIM:Heart_Infusion_Agar_BD_211065","validation_method":"manual:claude_culturemech_residual_grounding|CREATED|2026-08-30"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-1dfb10cdf4b64ff0
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2570]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"MICRO:0000567","line":2570,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"MICRO:0000567","preferred_term":"Heart
    Infusion Agar (BD 211065)","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-96dcf339e59e3e31
  kind: prior_review
  reference: reports/yaml_record_review/Heart_Infusion_Agar_BD_211065.md
  locator: '`data/ingredients/mapped/Heart_Infusion_Agar_BD_211065.yaml`:2; Verdict:4;
    Identity:10; Validation:20; Evidence:29; Completeness:44; Recommended Edits:50'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: a602e2e0aeb423e218f68ee5f533d06a675b68acca3661d09f9be38205abbb3c
  quote: "Recommended Edits:\n- Major: reground the BD 211065 record as a local catalog-specific\
    \ identity with\n  a parent or close generic relationship to `MICRO:0000567`,\
    \ or demote the\n  catalog suffix if the record is intended to represent generic\
    \ heart infusion\n  agar.\n- Major: suppress or retype the Difco and Eiken catalog\
    \ aliases so they no\n  longer publish as exact synonyms of the BD-specific subject."
- evidence_id: ev-69d6e2631b79acf0
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[725]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"1ca2d82b3de84d05372ed220e9d8face54d79c34b6593bb15a64f97f3a66628d","finding_id":"SEM:bc4df8ffe0eed9576a7b","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-8e5762e56e875efd
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-d7087ebb95882c08
  evidence_ids:
  - ev-47551c5142c6473b
  - ev-fb3f171cf0414c9c
  - ev-74fd07c5c8ee2922
  - ev-1dfb10cdf4b64ff0
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-242ce5624e75db15
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d7087ebb95882c08
  evidence_ids:
  - ev-96dcf339e59e3e31
  - ev-47551c5142c6473b
  - ev-69d6e2631b79acf0
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T19:09:40Z;
    reviewed SHA-256=1ca2d82b3de84d05372ed220e9d8face54d79c34b6593bb15a64f97f3a66628d;
    current SHA-256=1ca2d82b3de84d05372ed220e9d8face54d79c34b6593bb15a64f97f3a66628d;
    hash_changed=False. Reports=["reports/yaml_record_review/Heart_Infusion_Agar_BD_211065.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The generic
    MICRO target is active, but the record erases BD/Difco/Eiken catalog-specific
    boundaries.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-96dcf339e59e3e31
    - ev-47551c5142c6473b
  - name: legacy-native-ids
    value: '["SEM:bc4df8ffe0eed9576a7b"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-47551c5142c6473b
    - ev-96dcf339e59e3e31
    - ev-69d6e2631b79acf0
findings:
- finding_id: rec-f-3dae36ed2474026d
  issue_key: mim-reconciliation-historical-review-coverage-and-r-d7087ebb95882c08
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Heart_Infusion_Agar_BD_211065'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T19:09:40Z;
    reviewed SHA-256=1ca2d82b3de84d05372ed220e9d8face54d79c34b6593bb15a64f97f3a66628d;
    current SHA-256=1ca2d82b3de84d05372ed220e9d8face54d79c34b6593bb15a64f97f3a66628d;
    hash_changed=False. Reports=["reports/yaml_record_review/Heart_Infusion_Agar_BD_211065.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The generic
    MICRO target is active, but the record erases BD/Difco/Eiken catalog-specific
    boundaries.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d7087ebb95882c08
  evidence_ids:
  - ev-96dcf339e59e3e31
  - ev-47551c5142c6473b
  - ev-69d6e2631b79acf0
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Heart_Infusion_Agar_BD_211065.yaml
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
  with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.
```
