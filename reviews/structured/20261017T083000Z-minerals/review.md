# Per-record structured review: Minerals (data/ingredients/mapped/Minerals.yaml)

- Review: 20261017T083000Z-minerals
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Minerals (data/ingredients/mapped/Minerals.yaml, record-337eabcab58efd30, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Minerals.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Minerals.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-337eabcab58efd30 | data/ingredients/mapped/Minerals.yaml | maintained | Minerals |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-337eabcab58efd30 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-337eabcab58efd30 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-337eabcab58efd30 | Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-337eabcab58efd30.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-337eabcab58efd30.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T03:31:33Z; reviewed SHA-256=59c492c529f0e80ba85fcdb9cb848a45a0d05b12300c288fb7966dcda830ba99; current SHA-256=59c492c529f0e80ba85fcdb9cb848a45a0d05b12300c288fb7966dcda830ba99; hash_changed=False. Reports=["reports/yaml_record_review/Minerals.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The active CHEBI:46662 target validates, but the CultureMech Minerals surface needs re-review because OLS only exposes minerals as a related synonym.

## Findings

### rec-f-6efa475189f4db0c: Historical review coverage and residual narrative: Minerals

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-337eabcab58efd30.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T03:31:33Z; reviewed SHA-256=59c492c529f0e80ba85fcdb9cb848a45a0d05b12300c288fb7966dcda830ba99; current SHA-256=59c492c529f0e80ba85fcdb9cb848a45a0d05b12300c288fb7966dcda830ba99; hash_changed=False. Reports=["reports/yaml_record_review/Minerals.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The active CHEBI:46662 target validates, but the CultureMech Minerals surface needs re-review because OLS only exposes minerals as a related synonym.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-aaaf64d7457f31e9 | data/ingredients/mapped/Minerals.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2581],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:46662","line":2583,"mapping_status":"MAPPED","ontology_id":"CHEBI:46662","preferred_term":"Minerals"}],"identifier":"CHEBI:46662","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","match_level":"NORMALIZED","ontology_id":"CHEBI:46662","ontology_label":"mineral","ontology_source":"CHEBI"},"preferred_term":"Minerals","sssom_rows":[{"data_row":1883,"object_id":"CHEBI:46662","object_label":"mineral","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Minerals","synonym_count":0} |
| ev-576479816357f2d4 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2581] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-713a47baa05ba442 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Minerals; data-row positions=[1883] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1883,"object_id":"CHEBI:46662","object_label":"mineral","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Minerals","validation_method":"manual:claude_culturemech_residual_grounding&#124;CREATED&#124;2026-08-30"}] |
| ev-7ecde7e0afcb0671 | docs/data/mapped_ingredients.csv; CSV lines=[2583] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:46662","line":2583,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:46662","preferred_term":"Minerals","total_occurrences":"1"}] |
| ev-b7386fc1fe76a308 | reports/yaml_record_review/Minerals.md; &#96;data/ingredients/mapped/Minerals.yaml&#96;:2; Verdict:4; Identity:13; Validation:22; Evidence:30; Completeness:42; Recommended Edits:49 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-b579788f668414f9 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[943] | context_only | [{"current_record_sha256":"59c492c529f0e80ba85fcdb9cb848a45a0d05b12300c288fb7966dcda830ba99","finding_id":"SEM:f654501b73dfd3915fdf","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-minerals
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Minerals (data/ingredients/mapped/Minerals.yaml)'
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
summary: Per-record structured review for Minerals (data/ingredients/mapped/Minerals.yaml,
  record-337eabcab58efd30, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Minerals.yaml
    sha256: 59c492c529f0e80ba85fcdb9cb848a45a0d05b12300c288fb7966dcda830ba99
    role: target
  - path: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
    sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
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
  - path: reports/yaml_record_review/Minerals.md
    sha256: c289d95a65ff75cd71900bb8e8cd1e2134be65b90d0f207060e74b970adc546b
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-337eabcab58efd30
  path: data/ingredients/mapped/Minerals.yaml
  label: Minerals
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Minerals.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Minerals.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Minerals.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-337eabcab58efd30
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-337eabcab58efd30
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-337eabcab58efd30
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08
    and semantic review dispositions on HEAD.
  target_ids:
  - record-337eabcab58efd30
evidence:
- evidence_id: ev-aaaf64d7457f31e9
  kind: record_content
  reference: data/ingredients/mapped/Minerals.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2581],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:46662","line":2583,"mapping_status":"MAPPED","ontology_id":"CHEBI:46662","preferred_term":"Minerals"}],"identifier":"CHEBI:46662","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","match_level":"NORMALIZED","ontology_id":"CHEBI:46662","ontology_label":"mineral","ontology_source":"CHEBI"},"preferred_term":"Minerals","sssom_rows":[{"data_row":1883,"object_id":"CHEBI:46662","object_label":"mineral","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Minerals","synonym_count":0}'
  snapshot_sha256: 59c492c529f0e80ba85fcdb9cb848a45a0d05b12300c288fb7966dcda830ba99
- evidence_id: ev-576479816357f2d4
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2581]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-713a47baa05ba442
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Minerals; data-row positions=[1883]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1883,"object_id":"CHEBI:46662","object_label":"mineral","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Minerals","validation_method":"manual:claude_culturemech_residual_grounding|CREATED|2026-08-30"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-7ecde7e0afcb0671
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2583]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:46662","line":2583,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:46662","preferred_term":"Minerals","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-b7386fc1fe76a308
  kind: prior_review
  reference: reports/yaml_record_review/Minerals.md
  locator: '`data/ingredients/mapped/Minerals.yaml`:2; Verdict:4; Identity:13; Validation:22;
    Evidence:30; Completeness:42; Recommended Edits:49'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: c289d95a65ff75cd71900bb8e8cd1e2134be65b90d0f207060e74b970adc546b
  quote: "Recommended Edits:\n- Major: re-review the CultureMech `Minerals` row and\
    \ either ground it to a\n  stock-solution record for the source recipe or record\
    \ stronger evidence that\n  its intended referent is `CHEBI:46662`.\n- Major:\
    \ if `CHEBI:46662` is retained, revise the evidence and\n  `mapping_quality` so\
    \ they no longer claim an exact ontology synonym."
- evidence_id: ev-b579788f668414f9
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[943]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"59c492c529f0e80ba85fcdb9cb848a45a0d05b12300c288fb7966dcda830ba99","finding_id":"SEM:f654501b73dfd3915fdf","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-41e1de40054e3a7f
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-337eabcab58efd30
  evidence_ids:
  - ev-aaaf64d7457f31e9
  - ev-576479816357f2d4
  - ev-713a47baa05ba442
  - ev-7ecde7e0afcb0671
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-ada3fed5987bec67
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-337eabcab58efd30
  evidence_ids:
  - ev-b7386fc1fe76a308
  - ev-aaaf64d7457f31e9
  - ev-b579788f668414f9
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T03:31:33Z;
    reviewed SHA-256=59c492c529f0e80ba85fcdb9cb848a45a0d05b12300c288fb7966dcda830ba99;
    current SHA-256=59c492c529f0e80ba85fcdb9cb848a45a0d05b12300c288fb7966dcda830ba99;
    hash_changed=False. Reports=["reports/yaml_record_review/Minerals.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The active CHEBI:46662
    target validates, but the CultureMech Minerals surface needs re-review because
    OLS only exposes minerals as a related synonym.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b7386fc1fe76a308
    - ev-aaaf64d7457f31e9
  - name: legacy-native-ids
    value: '["SEM:f654501b73dfd3915fdf"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-aaaf64d7457f31e9
    - ev-b7386fc1fe76a308
    - ev-b579788f668414f9
findings:
- finding_id: rec-f-6efa475189f4db0c
  issue_key: mim-reconciliation-historical-review-coverage-and-r-337eabcab58efd30
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Minerals'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T03:31:33Z;
    reviewed SHA-256=59c492c529f0e80ba85fcdb9cb848a45a0d05b12300c288fb7966dcda830ba99;
    current SHA-256=59c492c529f0e80ba85fcdb9cb848a45a0d05b12300c288fb7966dcda830ba99;
    hash_changed=False. Reports=["reports/yaml_record_review/Minerals.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The active CHEBI:46662
    target validates, but the CultureMech Minerals surface needs re-review because
    OLS only exposes minerals as a related synonym.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-337eabcab58efd30
  evidence_ids:
  - ev-b7386fc1fe76a308
  - ev-aaaf64d7457f31e9
  - ev-b579788f668414f9
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Minerals.yaml
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
  with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.
```
