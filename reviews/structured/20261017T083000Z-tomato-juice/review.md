# Per-record structured review: Tomato_Juice (data/ingredients/mapped/Tomato_Juice.yaml)

- Review: 20261017T083000Z-tomato-juice
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Tomato_Juice (data/ingredients/mapped/Tomato_Juice.yaml, record-090d088900d69f4c, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Tomato_Juice.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Tomato_Juice.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-090d088900d69f4c | data/ingredients/mapped/Tomato_Juice.yaml | maintained | Tomato_Juice |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-090d088900d69f4c | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-090d088900d69f4c | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-090d088900d69f4c | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-090d088900d69f4c.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-090d088900d69f4c.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T19:09:25Z; reviewed SHA-256=24513b8692d9dca0927a7d4829126cda2cd69773bedaeb2af4fb35f6f7feab17; current SHA-256=24513b8692d9dca0927a7d4829126cda2cd69773bedaeb2af4fb35f6f7feab17; hash_changed=False. Reports=["reports/yaml_record_review/Tomato_Juice.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The FOODON identity passes, but a Del Monte brand-qualified raw label leaks into final SSSOM other.

## Findings

### rec-f-d606006791961266: Historical review coverage and residual narrative: Tomato_Juice

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-090d088900d69f4c.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T19:09:25Z; reviewed SHA-256=24513b8692d9dca0927a7d4829126cda2cd69773bedaeb2af4fb35f6f7feab17; current SHA-256=24513b8692d9dca0927a7d4829126cda2cd69773bedaeb2af4fb35f6f7feab17; hash_changed=False. Reports=["reports/yaml_record_review/Tomato_Juice.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The FOODON identity passes, but a Del Monte brand-qualified raw label leaks into final SSSOM other.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-b5169e9205053b1d | data/ingredients/mapped/Tomato_Juice.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1974],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:03301454","line":1976,"mapping_status":"MAPPED","ontology_id":"FOODON:03301454","preferred_term":"Tomato juice"}],"identifier":"FOODON:03301454","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":21,"edge_count":21,"occurrences":21},"occurrence_statistics":{"media_count":21,"total_occurrences":21},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"FOODON:03301454","ontology_label":"tomato juice","ontology_source":"FOODON"},"preferred_term":"Tomato juice","sssom_rows":[{"data_row":2794,"object_id":"FOODON:03301454","object_label":"tomato juice","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Tomato_Juice","synonym_count":2} |
| ev-d4ccd5fa28c3fc72 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1974] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-c4ee14ccc98e9b41 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Tomato_Juice; data-row positions=[2794] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2794,"object_id":"FOODON:03301454","object_label":"tomato juice","other":"Tomato juice (Del Monte)","predicate_id":"skos:exactMatch","subject_id":"MIM:Tomato_Juice","validation_method":"OLS:foodon&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-e0b17fe180a04569 | docs/data/mapped_ingredients.csv; CSV lines=[1976] | supports | Published identity and count rows inspected: [{"identifier":"FOODON:03301454","line":1976,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"21","ontology_id":"FOODON:03301454","preferred_term":"Tomato juice","total_occurrences":"21"}] |
| ev-8730319f82bcf979 | reports/yaml_record_review/Tomato_Juice.md; &#96;data/ingredients/mapped/Tomato_Juice.yaml&#96;:2; Verdict:4; Identity:10; Validation:21; Evidence:29; Issues:37; Major: final &#96;other&#96; exports a brand-qualified source label:39; Completeness:47; Recommended Edits:54 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-dee970a049f1e1d0 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1295] | context_only | [{"current_record_sha256":"24513b8692d9dca0927a7d4829126cda2cd69773bedaeb2af4fb35f6f7feab17","finding_id":"SEM:92c6518e72a9cfbeb6f3","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-tomato-juice
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Tomato_Juice (data/ingredients/mapped/Tomato_Juice.yaml)'
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
summary: Per-record structured review for Tomato_Juice (data/ingredients/mapped/Tomato_Juice.yaml,
  record-090d088900d69f4c, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Tomato_Juice.yaml
    sha256: 24513b8692d9dca0927a7d4829126cda2cd69773bedaeb2af4fb35f6f7feab17
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
  - path: reports/yaml_record_review/Tomato_Juice.md
    sha256: 349849e019385673bc399b6f50a946e493cfa5dbd4f53fd388514a2ea4d2952a
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-090d088900d69f4c
  path: data/ingredients/mapped/Tomato_Juice.yaml
  label: Tomato_Juice
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Tomato_Juice.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Tomato_Juice.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Tomato_Juice.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-090d088900d69f4c
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-090d088900d69f4c
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-090d088900d69f4c
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-090d088900d69f4c
evidence:
- evidence_id: ev-b5169e9205053b1d
  kind: record_content
  reference: data/ingredients/mapped/Tomato_Juice.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1974],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:03301454","line":1976,"mapping_status":"MAPPED","ontology_id":"FOODON:03301454","preferred_term":"Tomato
    juice"}],"identifier":"FOODON:03301454","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":21,"edge_count":21,"occurrences":21},"occurrence_statistics":{"media_count":21,"total_occurrences":21},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"FOODON:03301454","ontology_label":"tomato
    juice","ontology_source":"FOODON"},"preferred_term":"Tomato juice","sssom_rows":[{"data_row":2794,"object_id":"FOODON:03301454","object_label":"tomato
    juice","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Tomato_Juice","synonym_count":2}'
  snapshot_sha256: 24513b8692d9dca0927a7d4829126cda2cd69773bedaeb2af4fb35f6f7feab17
- evidence_id: ev-d4ccd5fa28c3fc72
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1974]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-c4ee14ccc98e9b41
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Tomato_Juice; data-row positions=[2794]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2794,"object_id":"FOODON:03301454","object_label":"tomato
    juice","other":"Tomato juice (Del Monte)","predicate_id":"skos:exactMatch","subject_id":"MIM:Tomato_Juice","validation_method":"OLS:foodon|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-e0b17fe180a04569
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1976]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"FOODON:03301454","line":1976,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"21","ontology_id":"FOODON:03301454","preferred_term":"Tomato
    juice","total_occurrences":"21"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-8730319f82bcf979
  kind: prior_review
  reference: reports/yaml_record_review/Tomato_Juice.md
  locator: '`data/ingredients/mapped/Tomato_Juice.yaml`:2; Verdict:4; Identity:10;
    Validation:21; Evidence:29; Issues:37; Major: final `other` exports a brand-qualified
    source label:39; Completeness:47; Recommended Edits:54'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 349849e019385673bc399b6f50a946e493cfa5dbd4f53fd388514a2ea4d2952a
  quote: "Issues:\n\n\nMajor: final `other` exports a brand-qualified source label:\n\
    `Tomato juice (Del Monte)` is a CultureMech recipe surface that folded onto\n\
    the FOODON tomato-juice record. It is useful as occurrence provenance, but it\n\
    is not a synonym of the general FOODON class because the parenthetical text is\n\
    brand-specific. Exporting it in final SSSOM `other` violates the rule that\nfinal\
    \ synonym tokens must be true synonyms of the mapped subject.\n\nRecommended Edits:\n\
    - Keep `Tomato juice (Del Monte)` as provenance or a raw source alias, but mark\n\
    \  it so the final SSSOM `other` exporter filters it out."
- evidence_id: ev-dee970a049f1e1d0
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1295]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"24513b8692d9dca0927a7d4829126cda2cd69773bedaeb2af4fb35f6f7feab17","finding_id":"SEM:92c6518e72a9cfbeb6f3","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-c6a06d3cc49c57c5
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-090d088900d69f4c
  evidence_ids:
  - ev-b5169e9205053b1d
  - ev-d4ccd5fa28c3fc72
  - ev-c4ee14ccc98e9b41
  - ev-e0b17fe180a04569
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-2067c42cf7cfb2c9
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-090d088900d69f4c
  evidence_ids:
  - ev-8730319f82bcf979
  - ev-b5169e9205053b1d
  - ev-dee970a049f1e1d0
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T19:09:25Z;
    reviewed SHA-256=24513b8692d9dca0927a7d4829126cda2cd69773bedaeb2af4fb35f6f7feab17;
    current SHA-256=24513b8692d9dca0927a7d4829126cda2cd69773bedaeb2af4fb35f6f7feab17;
    hash_changed=False. Reports=["reports/yaml_record_review/Tomato_Juice.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The FOODON identity
    passes, but a Del Monte brand-qualified raw label leaks into final SSSOM other.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-8730319f82bcf979
    - ev-b5169e9205053b1d
  - name: legacy-native-ids
    value: '["SEM:92c6518e72a9cfbeb6f3"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-b5169e9205053b1d
    - ev-8730319f82bcf979
    - ev-dee970a049f1e1d0
findings:
- finding_id: rec-f-d606006791961266
  issue_key: mim-reconciliation-historical-review-coverage-and-r-090d088900d69f4c
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Tomato_Juice'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T19:09:25Z;
    reviewed SHA-256=24513b8692d9dca0927a7d4829126cda2cd69773bedaeb2af4fb35f6f7feab17;
    current SHA-256=24513b8692d9dca0927a7d4829126cda2cd69773bedaeb2af4fb35f6f7feab17;
    hash_changed=False. Reports=["reports/yaml_record_review/Tomato_Juice.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The FOODON identity
    passes, but a Del Monte brand-qualified raw label leaks into final SSSOM other.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-090d088900d69f4c
  evidence_ids:
  - ev-8730319f82bcf979
  - ev-b5169e9205053b1d
  - ev-dee970a049f1e1d0
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Tomato_Juice.yaml
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
