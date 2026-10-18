# Per-record structured review: Cacl22h2o (data/ingredients/mapped/Cacl22h2o.yaml)

- Review: 20261017T083000Z-cacl22h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Cacl22h2o (data/ingredients/mapped/Cacl22h2o.yaml, record-c565e3fd482c8242, mapping_status=REJECTED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Cacl22h2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Cacl22h2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-c565e3fd482c8242 | data/ingredients/mapped/Cacl22h2o.yaml | maintained | Cacl22h2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-c565e3fd482c8242 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-c565e3fd482c8242 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-c565e3fd482c8242 | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-c565e3fd482c8242.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-c565e3fd482c8242.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T10:32:41Z; reviewed SHA-256=5f0a5e80a9a0bee1ccdd09234041c29a1c10fb55e52c534da6f87c0c1db6e0ed; current SHA-256=5f0a5e80a9a0bee1ccdd09234041c29a1c10fb55e52c534da6f87c0c1db6e0ed; hash_changed=False. Reports=["reports/yaml_record_review/Cacl22h2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The rejected calcium chloride dihydrate duplicate is unpublished in SSSOM, but old live-record fields remain.

## Findings

### rec-f-6561722006a0fad6: Historical review coverage and residual narrative: Cacl22h2o

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-c565e3fd482c8242.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T10:32:41Z; reviewed SHA-256=5f0a5e80a9a0bee1ccdd09234041c29a1c10fb55e52c534da6f87c0c1db6e0ed; current SHA-256=5f0a5e80a9a0bee1ccdd09234041c29a1c10fb55e52c534da6f87c0c1db6e0ed; hash_changed=False. Reports=["reports/yaml_record_review/Cacl22h2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The rejected calcium chloride dihydrate duplicate is unpublished in SSSOM, but old live-record fields remain.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-5ae1dd30f5b742d6 | data/ingredients/mapped/Cacl22h2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[621],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:86158","line":623,"mapping_status":"REJECTED","ontology_id":"CHEBI:86158","preferred_term":"CaCl22H2O"}],"identifier":"CHEBI:86158","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":5959,"edge_count":5959,"occurrences":6013},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:86158","ontology_label":"calcium chloride dihydrate","ontology_source":"CHEBI"},"preferred_term":"CaCl22H2O","sssom_rows":[],"sssom_subject":"MIM:Cacl22h2o","synonym_count":5} |
| ev-43a03e5f3a4514ea | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [621] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-ce82d83d058130c4 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Cacl22h2o; data-row positions=[] | context_only | Current exact-subject rows, including complete other payload: [] |
| ev-79ee2496114cb0bd | docs/data/mapped_ingredients.csv; CSV lines=[623] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:86158","line":623,"mapping_quality":"SYNONYM_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:86158","preferred_term":"CaCl22H2O","total_occurrences":"0"}] |
| ev-0385745d995d936e | reports/yaml_record_review/Cacl22h2o.md; &#96;data/ingredients/mapped/Cacl22h2o.yaml&#96;:2; Verdict:4; Identity:11; Validation:22; Evidence:37; Completeness:52; Recommended Edits:59 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-87388e1584303b16 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[344] | context_only | [{"current_record_sha256":"5f0a5e80a9a0bee1ccdd09234041c29a1c10fb55e52c534da6f87c0c1db6e0ed","finding_id":"SEM:79fe2d1eeb03c2b39637","kind":"existing_record_review","resolution_reason":"Source record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-cacl22h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Cacl22h2o (data/ingredients/mapped/Cacl22h2o.yaml)'
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
native_verdict: mapping_status=REJECTED; open=0; deferred=1
scientific_review: false
summary: Per-record structured review for Cacl22h2o (data/ingredients/mapped/Cacl22h2o.yaml,
  record-c565e3fd482c8242, mapping_status=REJECTED). Records 0 open finding(s) and
  1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Cacl22h2o.yaml
    sha256: 5f0a5e80a9a0bee1ccdd09234041c29a1c10fb55e52c534da6f87c0c1db6e0ed
    role: target
  - path: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
    sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
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
  - path: reports/yaml_record_review/Cacl22h2o.md
    sha256: 537514428c73eeb2d1c41f875588e80e20b6e0860f23d71f479fcfdbf1fac7d6
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-c565e3fd482c8242
  path: data/ingredients/mapped/Cacl22h2o.yaml
  label: Cacl22h2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cacl22h2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Cacl22h2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Cacl22h2o.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-c565e3fd482c8242
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-c565e3fd482c8242
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-c565e3fd482c8242
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-c565e3fd482c8242
evidence:
- evidence_id: ev-5ae1dd30f5b742d6
  kind: record_content
  reference: data/ingredients/mapped/Cacl22h2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[621],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:86158","line":623,"mapping_status":"REJECTED","ontology_id":"CHEBI:86158","preferred_term":"CaCl22H2O"}],"identifier":"CHEBI:86158","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":5959,"edge_count":5959,"occurrences":6013},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:86158","ontology_label":"calcium
    chloride dihydrate","ontology_source":"CHEBI"},"preferred_term":"CaCl22H2O","sssom_rows":[],"sssom_subject":"MIM:Cacl22h2o","synonym_count":5}'
  snapshot_sha256: 5f0a5e80a9a0bee1ccdd09234041c29a1c10fb55e52c534da6f87c0c1db6e0ed
- evidence_id: ev-43a03e5f3a4514ea
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [621]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-ce82d83d058130c4
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Cacl22h2o; data-row positions=[]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: []'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-79ee2496114cb0bd
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[623]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:86158","line":623,"mapping_quality":"SYNONYM_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:86158","preferred_term":"CaCl22H2O","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-0385745d995d936e
  kind: prior_review
  reference: reports/yaml_record_review/Cacl22h2o.md
  locator: '`data/ingredients/mapped/Cacl22h2o.yaml`:2; Verdict:4; Identity:11; Validation:22;
    Evidence:37; Completeness:52; Recommended Edits:59'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 537514428c73eeb2d1c41f875588e80e20b6e0860f23d71f479fcfdbf1fac7d6
  quote: "Recommended Edits:\n- Minor: compact `data/ingredients/mapped/Cacl22h2o.yaml`\
    \ to a pure rejected\n  duplicate tombstone by removing the stale role and, if\
    \ tombstones are not\n  meant to carry duplicate structures, the copied `chemical_properties`;\
    \ keep\n  the merge history pointing to `data/ingredients/mapped/Cacl2_X_2_H2o.yaml`,\n\
    \  then run `just sync-curated` and focused strict/SSSOM validation."
- evidence_id: ev-87388e1584303b16
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[344]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"5f0a5e80a9a0bee1ccdd09234041c29a1c10fb55e52c534da6f87c0c1db6e0ed","finding_id":"SEM:79fe2d1eeb03c2b39637","kind":"existing_record_review","resolution_reason":"Source
    record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-df5242870ca4216c
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-c565e3fd482c8242
  evidence_ids:
  - ev-5ae1dd30f5b742d6
  - ev-43a03e5f3a4514ea
  - ev-ce82d83d058130c4
  - ev-79ee2496114cb0bd
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-2c10b07cb973eb18
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-c565e3fd482c8242
  evidence_ids:
  - ev-0385745d995d936e
  - ev-5ae1dd30f5b742d6
  - ev-87388e1584303b16
  details: 'Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T10:32:41Z;
    reviewed SHA-256=5f0a5e80a9a0bee1ccdd09234041c29a1c10fb55e52c534da6f87c0c1db6e0ed;
    current SHA-256=5f0a5e80a9a0bee1ccdd09234041c29a1c10fb55e52c534da6f87c0c1db6e0ed;
    hash_changed=False. Reports=["reports/yaml_record_review/Cacl22h2o.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The rejected calcium
    chloride dihydrate duplicate is unpublished in SSSOM, but old live-record fields
    remain.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0385745d995d936e
    - ev-5ae1dd30f5b742d6
  - name: legacy-native-ids
    value: '["SEM:79fe2d1eeb03c2b39637"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-5ae1dd30f5b742d6
    - ev-0385745d995d936e
    - ev-87388e1584303b16
findings:
- finding_id: rec-f-6561722006a0fad6
  issue_key: mim-reconciliation-historical-review-coverage-and-r-c565e3fd482c8242
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Cacl22h2o'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T10:32:41Z;
    reviewed SHA-256=5f0a5e80a9a0bee1ccdd09234041c29a1c10fb55e52c534da6f87c0c1db6e0ed;
    current SHA-256=5f0a5e80a9a0bee1ccdd09234041c29a1c10fb55e52c534da6f87c0c1db6e0ed;
    hash_changed=False. Reports=["reports/yaml_record_review/Cacl22h2o.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The rejected calcium
    chloride dihydrate duplicate is unpublished in SSSOM, but old live-record fields
    remain.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-c565e3fd482c8242
  evidence_ids:
  - ev-0385745d995d936e
  - ev-5ae1dd30f5b742d6
  - ev-87388e1584303b16
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cacl22h2o.yaml
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
  with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.
```
