# Per-record structured review: Ferric_Iron (data/ingredients/mapped/Ferric_Iron.yaml)

- Review: 20261017T083000Z-ferric-iron
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Ferric_Iron (data/ingredients/mapped/Ferric_Iron.yaml, record-5ca6612a5f0e53d0, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Ferric_Iron.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Ferric_Iron.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-5ca6612a5f0e53d0 | data/ingredients/mapped/Ferric_Iron.yaml | maintained | Ferric_Iron |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-5ca6612a5f0e53d0 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-5ca6612a5f0e53d0 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-5ca6612a5f0e53d0 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-5ca6612a5f0e53d0.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-5ca6612a5f0e53d0.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T16:23:27Z; reviewed SHA-256=bac6010f9c1cc6b852db7ebbd6289d20f5eaf9f9126f3b007b6f856ecfcda322; current SHA-256=bac6010f9c1cc6b852db7ebbd6289d20f5eaf9f9126f3b007b6f856ecfcda322; hash_changed=False. Reports=["reports/yaml_record_review/Ferric_Iron.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact ferric-cation identity and Fe3+ alias pass, but top-level notes still carry stale import-era review text.

## Findings

### rec-f-2c606b5c9038c9c7: Historical review coverage and residual narrative: Ferric_Iron

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-5ca6612a5f0e53d0.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T16:23:27Z; reviewed SHA-256=bac6010f9c1cc6b852db7ebbd6289d20f5eaf9f9126f3b007b6f856ecfcda322; current SHA-256=bac6010f9c1cc6b852db7ebbd6289d20f5eaf9f9126f3b007b6f856ecfcda322; hash_changed=False. Reports=["reports/yaml_record_review/Ferric_Iron.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact ferric-cation identity and Fe3+ alias pass, but top-level notes still carry stale import-era review text.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-3016bf4d456a4d60 | data/ingredients/mapped/Ferric_Iron.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[264],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:29034","line":266,"mapping_status":"MAPPED","ontology_id":"CHEBI:29034","preferred_term":"Ferric Iron"}],"identifier":"CHEBI:29034","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":12,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:29034","ontology_label":"iron(3+)","ontology_source":"CHEBI"},"preferred_term":"Ferric Iron","sssom_rows":[{"data_row":1188,"object_id":"CHEBI:29034","object_label":"iron(3+)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Ferric_Iron","synonym_count":2} |
| ev-a938c0bddf8d62e4 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [264] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-1e5e6d5877cbcea3 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Ferric_Iron; data-row positions=[1188] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1188,"object_id":"CHEBI:29034","object_label":"iron(3+)","other":"Fe3+","predicate_id":"skos:exactMatch","subject_id":"MIM:Ferric_Iron","validation_method":"manual:promote_resolved_unmapped&#124;PROMOTED&#124;2026-08-04"}] |
| ev-219dd8b4d55453b8 | docs/data/mapped_ingredients.csv; CSV lines=[266] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:29034","line":266,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:29034","preferred_term":"Ferric Iron","total_occurrences":"0"}] |
| ev-c4f3ef27c87c6e11 | reports/yaml_record_review/Ferric_Iron.md; &#96;data/ingredients/mapped/Ferric_Iron.yaml&#96;:2; Verdict:4; Identity:11; Validation:24; Evidence:31; Completeness:52; Recommended Edits:59 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-4a908fe62d7e8e0e | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[597] | context_only | [{"current_record_sha256":"bac6010f9c1cc6b852db7ebbd6289d20f5eaf9f9126f3b007b6f856ecfcda322","finding_id":"SEM:36d55fc8f50f53f227d0","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-ferric-iron
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Ferric_Iron (data/ingredients/mapped/Ferric_Iron.yaml)'
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
summary: Per-record structured review for Ferric_Iron (data/ingredients/mapped/Ferric_Iron.yaml,
  record-5ca6612a5f0e53d0, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Ferric_Iron.yaml
    sha256: bac6010f9c1cc6b852db7ebbd6289d20f5eaf9f9126f3b007b6f856ecfcda322
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
  - path: reports/yaml_record_review/Ferric_Iron.md
    sha256: 35c1aa31ec7cdac6c5dc335e0894f5c6c563f967265217e98ec5d0a3c682e87c
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-5ca6612a5f0e53d0
  path: data/ingredients/mapped/Ferric_Iron.yaml
  label: Ferric_Iron
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Ferric_Iron.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Ferric_Iron.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Ferric_Iron.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-5ca6612a5f0e53d0
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-5ca6612a5f0e53d0
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-5ca6612a5f0e53d0
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-5ca6612a5f0e53d0
evidence:
- evidence_id: ev-3016bf4d456a4d60
  kind: record_content
  reference: data/ingredients/mapped/Ferric_Iron.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[264],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:29034","line":266,"mapping_status":"MAPPED","ontology_id":"CHEBI:29034","preferred_term":"Ferric
    Iron"}],"identifier":"CHEBI:29034","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":12,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:29034","ontology_label":"iron(3+)","ontology_source":"CHEBI"},"preferred_term":"Ferric
    Iron","sssom_rows":[{"data_row":1188,"object_id":"CHEBI:29034","object_label":"iron(3+)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Ferric_Iron","synonym_count":2}'
  snapshot_sha256: bac6010f9c1cc6b852db7ebbd6289d20f5eaf9f9126f3b007b6f856ecfcda322
- evidence_id: ev-a938c0bddf8d62e4
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [264]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-1e5e6d5877cbcea3
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Ferric_Iron; data-row positions=[1188]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1188,"object_id":"CHEBI:29034","object_label":"iron(3+)","other":"Fe3+","predicate_id":"skos:exactMatch","subject_id":"MIM:Ferric_Iron","validation_method":"manual:promote_resolved_unmapped|PROMOTED|2026-08-04"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-219dd8b4d55453b8
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[266]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:29034","line":266,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:29034","preferred_term":"Ferric
    Iron","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-c4f3ef27c87c6e11
  kind: prior_review
  reference: reports/yaml_record_review/Ferric_Iron.md
  locator: '`data/ingredients/mapped/Ferric_Iron.yaml`:2; Verdict:4; Identity:11;
    Validation:24; Evidence:31; Completeness:52; Recommended Edits:59'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 35c1aa31ec7cdac6c5dc335e0894f5c6c563f967265217e98ec5d0a3c682e87c
  quote: "Recommended Edits:\n- Minor: replace the stale import-era top-level `notes`\
    \ in\n  `data/ingredients/mapped/Ferric_Iron.yaml`, sync\n  `data/curated/mapped_ingredients.yaml`,\
    \ and rerun strict validation plus the\n  roundtrip gate."
- evidence_id: ev-4a908fe62d7e8e0e
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[597]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"bac6010f9c1cc6b852db7ebbd6289d20f5eaf9f9126f3b007b6f856ecfcda322","finding_id":"SEM:36d55fc8f50f53f227d0","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-db7ef7d3ea79f28b
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-5ca6612a5f0e53d0
  evidence_ids:
  - ev-3016bf4d456a4d60
  - ev-a938c0bddf8d62e4
  - ev-1e5e6d5877cbcea3
  - ev-219dd8b4d55453b8
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-7867ac4061d2fa04
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-5ca6612a5f0e53d0
  evidence_ids:
  - ev-c4f3ef27c87c6e11
  - ev-3016bf4d456a4d60
  - ev-4a908fe62d7e8e0e
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T16:23:27Z;
    reviewed SHA-256=bac6010f9c1cc6b852db7ebbd6289d20f5eaf9f9126f3b007b6f856ecfcda322;
    current SHA-256=bac6010f9c1cc6b852db7ebbd6289d20f5eaf9f9126f3b007b6f856ecfcda322;
    hash_changed=False. Reports=["reports/yaml_record_review/Ferric_Iron.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact ferric-cation
    identity and Fe3+ alias pass, but top-level notes still carry stale import-era
    review text.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c4f3ef27c87c6e11
    - ev-3016bf4d456a4d60
  - name: legacy-native-ids
    value: '["SEM:36d55fc8f50f53f227d0"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-3016bf4d456a4d60
    - ev-c4f3ef27c87c6e11
    - ev-4a908fe62d7e8e0e
findings:
- finding_id: rec-f-2c606b5c9038c9c7
  issue_key: mim-reconciliation-historical-review-coverage-and-r-5ca6612a5f0e53d0
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Ferric_Iron'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T16:23:27Z;
    reviewed SHA-256=bac6010f9c1cc6b852db7ebbd6289d20f5eaf9f9126f3b007b6f856ecfcda322;
    current SHA-256=bac6010f9c1cc6b852db7ebbd6289d20f5eaf9f9126f3b007b6f856ecfcda322;
    hash_changed=False. Reports=["reports/yaml_record_review/Ferric_Iron.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact ferric-cation
    identity and Fe3+ alias pass, but top-level notes still carry stale import-era
    review text.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-5ca6612a5f0e53d0
  evidence_ids:
  - ev-c4f3ef27c87c6e11
  - ev-3016bf4d456a4d60
  - ev-4a908fe62d7e8e0e
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Ferric_Iron.yaml
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
