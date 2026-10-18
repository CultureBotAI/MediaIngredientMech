# Per-record structured review: Sparassol (data/ingredients/mapped/Sparassol.yaml)

- Review: 20261017T083000Z-sparassol
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Sparassol (data/ingredients/mapped/Sparassol.yaml, record-c385b11cb40e560f, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Sparassol.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Sparassol.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-c385b11cb40e560f | data/ingredients/mapped/Sparassol.yaml | maintained | Sparassol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-c385b11cb40e560f | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-c385b11cb40e560f | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-c385b11cb40e560f | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-c385b11cb40e560f.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-c385b11cb40e560f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:12:31Z; reviewed SHA-256=37d30219a759bb7eddf97b270783e1568beb922be08234f32a6cbe3e87eb5d6a; current SHA-256=37d30219a759bb7eddf97b270783e1568beb922be08234f32a6cbe3e87eb5d6a; hash_changed=False. Reports=["reports/yaml_record_review/Sparassol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS fallback is stale because PubChem and OLS now identify active CHEBI:92544 for the same Sparassol compound.

## Findings

### rec-f-7316b6d527dad385: Historical review coverage and residual narrative: Sparassol

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-c385b11cb40e560f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:12:31Z; reviewed SHA-256=37d30219a759bb7eddf97b270783e1568beb922be08234f32a6cbe3e87eb5d6a; current SHA-256=37d30219a759bb7eddf97b270783e1568beb922be08234f32a6cbe3e87eb5d6a; hash_changed=False. Reports=["reports/yaml_record_review/Sparassol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS fallback is stale because PubChem and OLS now identify active CHEBI:92544 for the same Sparassol compound.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-c3fdc1426e0e1388 | data/ingredients/mapped/Sparassol.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1886],"raw_equal":true},"docs_rows":[{"identifier":"cas:520-43-4","line":1888,"mapping_status":"MAPPED","ontology_id":"cas:520-43-4","preferred_term":"Sparassol"}],"identifier":"cas:520-43-4","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:520-43-4","ontology_label":"Sparassol","ontology_source":"CAS"},"preferred_term":"Sparassol","sssom_rows":[{"data_row":2626,"object_id":"cas:520-43-4","object_label":"Sparassol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sparassol","synonym_count":0} |
| ev-276c348f7e65b16f | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1886] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-789dc092b71fde75 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Sparassol; data-row positions=[2626] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2626,"object_id":"cas:520-43-4","object_label":"Sparassol","other":"CAS:520-43-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Sparassol","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-763b394bc77ea09d | docs/data/mapped_ingredients.csv; CSV lines=[1888] | supports | Published identity and count rows inspected: [{"identifier":"cas:520-43-4","line":1888,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"cas:520-43-4","preferred_term":"Sparassol","total_occurrences":"0"}] |
| ev-8bef11f4523f2908 | reports/yaml_record_review/Sparassol.md; &#96;data/ingredients/mapped/Sparassol.yaml&#96;:2; Verdict:4; Identity:10; Validation:20; Evidence:30; Completeness:46; Recommended Edits:54 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-e1816b54cf08945f | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1240] | context_only | [{"current_record_sha256":"37d30219a759bb7eddf97b270783e1568beb922be08234f32a6cbe3e87eb5d6a","finding_id":"SEM:aa50dd7d907a0443e965","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-sparassol
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Sparassol (data/ingredients/mapped/Sparassol.yaml)'
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
summary: Per-record structured review for Sparassol (data/ingredients/mapped/Sparassol.yaml,
  record-c385b11cb40e560f, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Sparassol.yaml
    sha256: 37d30219a759bb7eddf97b270783e1568beb922be08234f32a6cbe3e87eb5d6a
    role: target
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
    sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
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
  - path: reports/yaml_record_review/Sparassol.md
    sha256: 12966f51db42e374175dcdda685695a5ff7131acea7407be2e1bfbbe9a937e8a
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-c385b11cb40e560f
  path: data/ingredients/mapped/Sparassol.yaml
  label: Sparassol
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sparassol.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Sparassol.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Sparassol.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-c385b11cb40e560f
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-c385b11cb40e560f
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-c385b11cb40e560f
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-c385b11cb40e560f
evidence:
- evidence_id: ev-c3fdc1426e0e1388
  kind: record_content
  reference: data/ingredients/mapped/Sparassol.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1886],"raw_equal":true},"docs_rows":[{"identifier":"cas:520-43-4","line":1888,"mapping_status":"MAPPED","ontology_id":"cas:520-43-4","preferred_term":"Sparassol"}],"identifier":"cas:520-43-4","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:520-43-4","ontology_label":"Sparassol","ontology_source":"CAS"},"preferred_term":"Sparassol","sssom_rows":[{"data_row":2626,"object_id":"cas:520-43-4","object_label":"Sparassol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sparassol","synonym_count":0}'
  snapshot_sha256: 37d30219a759bb7eddf97b270783e1568beb922be08234f32a6cbe3e87eb5d6a
- evidence_id: ev-276c348f7e65b16f
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1886]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-789dc092b71fde75
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Sparassol; data-row positions=[2626]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2626,"object_id":"cas:520-43-4","object_label":"Sparassol","other":"CAS:520-43-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Sparassol","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-763b394bc77ea09d
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1888]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:520-43-4","line":1888,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"cas:520-43-4","preferred_term":"Sparassol","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-8bef11f4523f2908
  kind: prior_review
  reference: reports/yaml_record_review/Sparassol.md
  locator: '`data/ingredients/mapped/Sparassol.yaml`:2; Verdict:4; Identity:10; Validation:20;
    Evidence:30; Completeness:46; Recommended Edits:54'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 12966f51db42e374175dcdda685695a5ff7131acea7407be2e1bfbbe9a937e8a
  quote: "Recommended Edits:\n- Major: verify `CHEBI:92544` directly against the ChEBI\
    \ term and, if it is the\n  exact Sparassol identity, update `data/ingredients/mapped/Sparassol.yaml`\
    \ and\n  the aggregate mapped row from `cas:520-43-4` to `CHEBI:92544`, retaining\n\
    \  `520-43-4` as `chemical_properties.cas_rn`.\n- Regenerate the SSSOM row after\
    \ that YAML repair so\n  `mappings/ingredient_mappings.sssom.tsv` points at the\
    \ CHEBI target instead\n  of a stale CAS fallback."
- evidence_id: ev-e1816b54cf08945f
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1240]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"37d30219a759bb7eddf97b270783e1568beb922be08234f32a6cbe3e87eb5d6a","finding_id":"SEM:aa50dd7d907a0443e965","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-84c3a983eeccb453
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-c385b11cb40e560f
  evidence_ids:
  - ev-c3fdc1426e0e1388
  - ev-276c348f7e65b16f
  - ev-789dc092b71fde75
  - ev-763b394bc77ea09d
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-be3e5a1d7b9eb324
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-c385b11cb40e560f
  evidence_ids:
  - ev-8bef11f4523f2908
  - ev-c3fdc1426e0e1388
  - ev-e1816b54cf08945f
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:12:31Z;
    reviewed SHA-256=37d30219a759bb7eddf97b270783e1568beb922be08234f32a6cbe3e87eb5d6a;
    current SHA-256=37d30219a759bb7eddf97b270783e1568beb922be08234f32a6cbe3e87eb5d6a;
    hash_changed=False. Reports=["reports/yaml_record_review/Sparassol.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The CAS fallback
    is stale because PubChem and OLS now identify active CHEBI:92544 for the same
    Sparassol compound.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-8bef11f4523f2908
    - ev-c3fdc1426e0e1388
  - name: legacy-native-ids
    value: '["SEM:aa50dd7d907a0443e965"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-c3fdc1426e0e1388
    - ev-8bef11f4523f2908
    - ev-e1816b54cf08945f
findings:
- finding_id: rec-f-7316b6d527dad385
  issue_key: mim-reconciliation-historical-review-coverage-and-r-c385b11cb40e560f
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Sparassol'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:12:31Z;
    reviewed SHA-256=37d30219a759bb7eddf97b270783e1568beb922be08234f32a6cbe3e87eb5d6a;
    current SHA-256=37d30219a759bb7eddf97b270783e1568beb922be08234f32a6cbe3e87eb5d6a;
    hash_changed=False. Reports=["reports/yaml_record_review/Sparassol.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The CAS fallback
    is stale because PubChem and OLS now identify active CHEBI:92544 for the same
    Sparassol compound.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-c385b11cb40e560f
  evidence_ids:
  - ev-8bef11f4523f2908
  - ev-c3fdc1426e0e1388
  - ev-e1816b54cf08945f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sparassol.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.
```
