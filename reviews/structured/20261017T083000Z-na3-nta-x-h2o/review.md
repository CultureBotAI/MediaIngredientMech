# Per-record structured review: Na3-NTA_X_H2O (data/ingredients/unmapped/Na3-NTA_X_H2O.yaml)

- Review: 20261017T083000Z-na3-nta-x-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Na3-NTA_X_H2O (data/ingredients/unmapped/Na3-NTA_X_H2O.yaml, record-f39e346112836a3b, mapping_status=UNMAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/unmapped/Na3-NTA_X_H2O.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/unmapped/Na3-NTA_X_H2O.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-f39e346112836a3b | data/ingredients/unmapped/Na3-NTA_X_H2O.yaml | maintained | Na3-NTA_X_H2O |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-f39e346112836a3b | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-f39e346112836a3b | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-f39e346112836a3b | Reconciled against predecessor batch review 20261011T024640Z-mim-reconcile-all-batch-13 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-f39e346112836a3b.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-f39e346112836a3b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T04:49:12Z; reviewed SHA-256=9a83196f39aaf6cf563af23cabe5336be49445e5aa55d19d19608761055a3992; current SHA-256=9a83196f39aaf6cf563af23cabe5336be49445e5aa55d19d19608761055a3992; hash_changed=False. Reports=["reports/yaml_record_review/20261001T044912Z-Na3-NTA_X_H2O.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Specific single-ingredient residual remains unresolved: current evidence does not support an exact ontology or stable-registry identity.

### Unresolved exact identity or preparation

identity: unknown. Targets: record-f39e346112836a3b.

Current status=UNMAPPED; no supported promotion is established by this reconciliation. Preserve the unresolved source boundary; source-backed identity/decomposition review is still required.

## Findings

### rec-f-unmapped-f39e346112836a3b: Unresolved exact identity or preparation: Na3-NTA_X_H2O

major / deferred / provisional; issue key: mim-reconciliation-unresolved-identity-f39e346112836a3b.

Current status=UNMAPPED; no supported promotion is established by this reconciliation. Preserve the unresolved source boundary; source-backed identity/decomposition review is still required.

Disposition: Current status=UNMAPPED; no supported promotion is established by this reconciliation. Preserve the unresolved source boundary; source-backed identity/decomposition review is still required.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-6902bc2f07dcbc65 | data/ingredients/unmapped/Na3-NTA_X_H2O.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/unmapped_ingredients.yaml","positions":[170],"raw_equal":true},"docs_rows":[{"identifier":"UNMAPPED_0475","line":172,"mapping_status":"UNMAPPED","ontology_id":"","preferred_term":"Na3-NTA x H2O"}],"identifier":"UNMAPPED_0475","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"UNMAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{},"preferred_term":"Na3-NTA x H2O","sssom_rows":[],"sssom_subject":"MIM:Na3-NTA_X_H2O","synonym_count":1} |
| ev-8c18286e45533b46 | data/curated/unmapped_ingredients.yaml; ingredients positions (zero-based): [170] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-628005bced1a6c67 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Na3-NTA_X_H2O; data-row positions=[] | context_only | Current exact-subject rows, including complete other payload: [] |
| ev-a4190cca5bea6bf6 | docs/data/unmapped_ingredients.csv; CSV lines=[172] | supports | Published identity and count rows inspected: [{"identifier":"UNMAPPED_0475","line":172,"mapping_quality":"","mapping_status":"UNMAPPED","media_count":"0","ontology_id":"","preferred_term":"Na3-NTA x H2O","total_occurrences":"0"}] |
| ev-d5d04b6fc20be8bf | reports/yaml_record_review/20261001T044912Z-Na3-NTA_X_H2O.md; YAML Record Review: Na3-NTA x H2O:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:45; Findings:51; Recommended Edits:55; Follow-up Checks:60; Additional Notes:66 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024640Z-mim-reconcile-all-batch-13.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-na3-nta-x-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Na3-NTA_X_H2O (data/ingredients/unmapped/Na3-NTA_X_H2O.yaml)'
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
native_verdict: mapping_status=UNMAPPED; open=0; deferred=1
scientific_review: false
summary: Per-record structured review for Na3-NTA_X_H2O (data/ingredients/unmapped/Na3-NTA_X_H2O.yaml,
  record-f39e346112836a3b, mapping_status=UNMAPPED). Records 0 open finding(s) and
  1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/unmapped/Na3-NTA_X_H2O.yaml
    sha256: 9a83196f39aaf6cf563af23cabe5336be49445e5aa55d19d19608761055a3992
    role: target
  - path: reviews/structured/20261011T024640Z-mim-reconcile-all-batch-13/review.yaml
    sha256: 59cac14400d959b07cc323af966582e4f2dc3bafb95a044f47b6752bb4c20dbb
    role: context
  - path: data/curated/unmapped_ingredients.yaml
    sha256: 8f574be094e741f1d59d55618cc14bf375304644732508bd7a5cd4a817c7fce2
    role: context
  - path: mappings/ingredient_mappings.sssom.tsv
    sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
    role: context
  - path: docs/data/unmapped_ingredients.csv
    sha256: 58a51002c62583df7dd2c667a003f2644c84fa8e2cb549c7d7ec3ecdc163b1f7
    role: context
  - path: reports/yaml_record_review/20261001T044912Z-Na3-NTA_X_H2O.md
    sha256: c1b12adb4b17ec34f2e377841eaf71a2b71227c3257c157c3ee4d71f7f5bddd2
    role: context
targets:
- target_id: record-f39e346112836a3b
  path: data/ingredients/unmapped/Na3-NTA_X_H2O.yaml
  label: Na3-NTA_X_H2O
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/unmapped/Na3-NTA_X_H2O.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/unmapped/Na3-NTA_X_H2O.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/unmapped/Na3-NTA_X_H2O.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-f39e346112836a3b
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-f39e346112836a3b
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-f39e346112836a3b
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024640Z-mim-reconcile-all-batch-13
    and semantic review dispositions on HEAD.
  target_ids:
  - record-f39e346112836a3b
evidence:
- evidence_id: ev-6902bc2f07dcbc65
  kind: record_content
  reference: data/ingredients/unmapped/Na3-NTA_X_H2O.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/unmapped_ingredients.yaml","positions":[170],"raw_equal":true},"docs_rows":[{"identifier":"UNMAPPED_0475","line":172,"mapping_status":"UNMAPPED","ontology_id":"","preferred_term":"Na3-NTA
    x H2O"}],"identifier":"UNMAPPED_0475","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"UNMAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{},"preferred_term":"Na3-NTA
    x H2O","sssom_rows":[],"sssom_subject":"MIM:Na3-NTA_X_H2O","synonym_count":1}'
  snapshot_sha256: 9a83196f39aaf6cf563af23cabe5336be49445e5aa55d19d19608761055a3992
- evidence_id: ev-8c18286e45533b46
  kind: validation
  reference: data/curated/unmapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [170]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 8f574be094e741f1d59d55618cc14bf375304644732508bd7a5cd4a817c7fce2
- evidence_id: ev-628005bced1a6c67
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Na3-NTA_X_H2O; data-row positions=[]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: []'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-a4190cca5bea6bf6
  kind: record_content
  reference: docs/data/unmapped_ingredients.csv
  locator: CSV lines=[172]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"UNMAPPED_0475","line":172,"mapping_quality":"","mapping_status":"UNMAPPED","media_count":"0","ontology_id":"","preferred_term":"Na3-NTA
    x H2O","total_occurrences":"0"}]'
  snapshot_sha256: 58a51002c62583df7dd2c667a003f2644c84fa8e2cb549c7d7ec3ecdc163b1f7
- evidence_id: ev-d5d04b6fc20be8bf
  kind: prior_review
  reference: reports/yaml_record_review/20261001T044912Z-Na3-NTA_X_H2O.md
  locator: 'YAML Record Review: Na3-NTA x H2O:2; Target:10; Validation:20; Identity
    and Grounding:27; Evidence:36; Completeness:45; Findings:51; Recommended Edits:55;
    Follow-up Checks:60; Additional Notes:66'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: c1b12adb4b17ec34f2e377841eaf71a2b71227c3257c157c3ee4d71f7f5bddd2
  quote: 'Findings:

    - **major**: `data/ingredients/unmapped/Na3-NTA_X_H2O.yaml` remains `UNMAPPED`;
    no exact ontology term or independently supported registry identity is recorded.
    Do not exact-match it to a broader parent, component, hydrate, salt, or lookalike
    label.


    Recommended Edits:

    - Curate an exact same-form identity or decomposition for `data/ingredients/unmapped/Na3-NTA_X_H2O.yaml`
    before mapping it.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/unmapped/Na3-NTA_X_H2O.yaml`,
    `just validate-terms data/ingredients/unmapped/Na3-NTA_X_H2O.yaml` where applicable,
    and `just qc-sssom`.'
assessments:
- assessment_id: a-4d41d8a1419cf98b
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-f39e346112836a3b
  evidence_ids:
  - ev-6902bc2f07dcbc65
  - ev-8c18286e45533b46
  - ev-628005bced1a6c67
  - ev-a4190cca5bea6bf6
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-59cb9b9f58caec21
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-f39e346112836a3b
  evidence_ids:
  - ev-d5d04b6fc20be8bf
  - ev-6902bc2f07dcbc65
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T04:49:12Z;
    reviewed SHA-256=9a83196f39aaf6cf563af23cabe5336be49445e5aa55d19d19608761055a3992;
    current SHA-256=9a83196f39aaf6cf563af23cabe5336be49445e5aa55d19d19608761055a3992;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T044912Z-Na3-NTA_X_H2O.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Specific
    single-ingredient residual remains unresolved: current evidence does not support
    an exact ontology or stable-registry identity.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d5d04b6fc20be8bf
    - ev-6902bc2f07dcbc65
  - name: legacy-native-ids
    value: '[]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-6902bc2f07dcbc65
    - ev-d5d04b6fc20be8bf
- assessment_id: a-5a6b75d9d27581fa
  area: identity
  topic: Unresolved exact identity or preparation
  outcome: unknown
  summary: Current status=UNMAPPED; no supported promotion is established by this
    reconciliation. Preserve the unresolved source boundary; source-backed identity/decomposition
    review is still required.
  target_ids:
  - record-f39e346112836a3b
  evidence_ids:
  - ev-d5d04b6fc20be8bf
  - ev-6902bc2f07dcbc65
  - ev-628005bced1a6c67
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d5d04b6fc20be8bf
    - ev-6902bc2f07dcbc65
    - ev-628005bced1a6c67
findings:
- finding_id: rec-f-unmapped-f39e346112836a3b
  issue_key: mim-reconciliation-unresolved-identity-f39e346112836a3b
  category: identity
  severity: major
  status: deferred
  certainty: provisional
  title: 'Unresolved exact identity or preparation: Na3-NTA_X_H2O'
  description: Current status=UNMAPPED; no supported promotion is established by this
    reconciliation. Preserve the unresolved source boundary; source-backed identity/decomposition
    review is still required.
  disposition_reason: Current status=UNMAPPED; no supported promotion is established
    by this reconciliation. Preserve the unresolved source boundary; source-backed
    identity/decomposition review is still required.
  target_ids:
  - record-f39e346112836a3b
  evidence_ids:
  - ev-d5d04b6fc20be8bf
  - ev-6902bc2f07dcbc65
  - ev-628005bced1a6c67
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/unmapped/Na3-NTA_X_H2O.yaml
    role: maintained ingredient
  field_paths:
  - mapping_status
  - ontology_id
  tags:
  - reconciliation
  - bundle-by-owner
  - unresolved-identity
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
  with lineage to 20261011T024640Z-mim-reconcile-all-batch-13.
```
