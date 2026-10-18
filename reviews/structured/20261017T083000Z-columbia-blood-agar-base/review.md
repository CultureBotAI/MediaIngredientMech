# Per-record structured review: Columbia_Blood_Agar_Base (data/ingredients/unmapped/Columbia_Blood_Agar_Base.yaml)

- Review: 20261017T083000Z-columbia-blood-agar-base
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Columbia_Blood_Agar_Base (data/ingredients/unmapped/Columbia_Blood_Agar_Base.yaml, record-d70e774f051088d5, mapping_status=UNMAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/unmapped/Columbia_Blood_Agar_Base.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/unmapped/Columbia_Blood_Agar_Base.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-d70e774f051088d5 | data/ingredients/unmapped/Columbia_Blood_Agar_Base.yaml | maintained | Columbia_Blood_Agar_Base |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-d70e774f051088d5 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-d70e774f051088d5 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-d70e774f051088d5 | Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-d70e774f051088d5.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-d70e774f051088d5.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T04:47:25Z; reviewed SHA-256=29ed63a00d3f4f7a1652beee549526d625eef231f29b40691bd128d2f7608324; current SHA-256=29ed63a00d3f4f7a1652beee549526d625eef231f29b40691bd128d2f7608324; hash_changed=False. Reports=["reports/yaml_record_review/20261001T044725Z-Columbia_Blood_Agar_Base.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Named medium/formulation is intentionally left unmapped until a recipe-level CultureMech representation owns the formulation.

### Unresolved exact identity or preparation

identity: unknown. Targets: record-d70e774f051088d5.

Current status=UNMAPPED; no supported promotion is established by this reconciliation. Preserve the unresolved source boundary; source-backed identity/decomposition review is still required.

## Findings

### rec-f-unmapped-d70e774f051088d5: Unresolved exact identity or preparation: Columbia_Blood_Agar_Base

major / deferred / provisional; issue key: mim-reconciliation-unresolved-identity-d70e774f051088d5.

Current status=UNMAPPED; no supported promotion is established by this reconciliation. Preserve the unresolved source boundary; source-backed identity/decomposition review is still required.

Disposition: Current status=UNMAPPED; no supported promotion is established by this reconciliation. Preserve the unresolved source boundary; source-backed identity/decomposition review is still required.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-a0c86bae38ce9050 | data/ingredients/unmapped/Columbia_Blood_Agar_Base.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/unmapped_ingredients.yaml","positions":[68],"raw_equal":true},"docs_rows":[{"identifier":"UNMAPPED_0118","line":70,"mapping_status":"UNMAPPED","ontology_id":"","preferred_term":"Columbia blood agar base"}],"identifier":"UNMAPPED_0118","ingredient_type":"NAMED_MEDIUM","mapping_status":"UNMAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{},"preferred_term":"Columbia blood agar base","sssom_rows":[],"sssom_subject":"MIM:Columbia_Blood_Agar_Base","synonym_count":3} |
| ev-2b338fbcc7d947a2 | data/curated/unmapped_ingredients.yaml; ingredients positions (zero-based): [68] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-cae280f8bf37c555 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Columbia_Blood_Agar_Base; data-row positions=[] | context_only | Current exact-subject rows, including complete other payload: [] |
| ev-ec80982d59e049d7 | docs/data/unmapped_ingredients.csv; CSV lines=[70] | supports | Published identity and count rows inspected: [{"identifier":"UNMAPPED_0118","line":70,"mapping_quality":"","mapping_status":"UNMAPPED","media_count":"0","ontology_id":"","preferred_term":"Columbia blood agar base","total_occurrences":"0"}] |
| ev-281a7a479930b71c | reports/yaml_record_review/20261001T044725Z-Columbia_Blood_Agar_Base.md; YAML Record Review: Columbia blood agar base:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:45; Findings:51; Recommended Edits:55; Follow-up Checks:60; Additional Notes:66 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-columbia-blood-agar-base
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Columbia_Blood_Agar_Base (data/ingredients/unmapped/Columbia_Blood_Agar_Base.yaml)'
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
summary: Per-record structured review for Columbia_Blood_Agar_Base (data/ingredients/unmapped/Columbia_Blood_Agar_Base.yaml,
  record-d70e774f051088d5, mapping_status=UNMAPPED). Records 0 open finding(s) and
  1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/unmapped/Columbia_Blood_Agar_Base.yaml
    sha256: 29ed63a00d3f4f7a1652beee549526d625eef231f29b40691bd128d2f7608324
    role: target
  - path: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
    sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
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
  - path: reports/yaml_record_review/20261001T044725Z-Columbia_Blood_Agar_Base.md
    sha256: 359fab3b303fed51e459e2b35e946510c3bac86265140e329672e1cd224c3d4e
    role: context
targets:
- target_id: record-d70e774f051088d5
  path: data/ingredients/unmapped/Columbia_Blood_Agar_Base.yaml
  label: Columbia_Blood_Agar_Base
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/unmapped/Columbia_Blood_Agar_Base.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/unmapped/Columbia_Blood_Agar_Base.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/unmapped/Columbia_Blood_Agar_Base.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-d70e774f051088d5
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-d70e774f051088d5
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-d70e774f051088d5
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12
    and semantic review dispositions on HEAD.
  target_ids:
  - record-d70e774f051088d5
evidence:
- evidence_id: ev-a0c86bae38ce9050
  kind: record_content
  reference: data/ingredients/unmapped/Columbia_Blood_Agar_Base.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/unmapped_ingredients.yaml","positions":[68],"raw_equal":true},"docs_rows":[{"identifier":"UNMAPPED_0118","line":70,"mapping_status":"UNMAPPED","ontology_id":"","preferred_term":"Columbia
    blood agar base"}],"identifier":"UNMAPPED_0118","ingredient_type":"NAMED_MEDIUM","mapping_status":"UNMAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{},"preferred_term":"Columbia
    blood agar base","sssom_rows":[],"sssom_subject":"MIM:Columbia_Blood_Agar_Base","synonym_count":3}'
  snapshot_sha256: 29ed63a00d3f4f7a1652beee549526d625eef231f29b40691bd128d2f7608324
- evidence_id: ev-2b338fbcc7d947a2
  kind: validation
  reference: data/curated/unmapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [68]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 8f574be094e741f1d59d55618cc14bf375304644732508bd7a5cd4a817c7fce2
- evidence_id: ev-cae280f8bf37c555
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Columbia_Blood_Agar_Base; data-row positions=[]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: []'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-ec80982d59e049d7
  kind: record_content
  reference: docs/data/unmapped_ingredients.csv
  locator: CSV lines=[70]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"UNMAPPED_0118","line":70,"mapping_quality":"","mapping_status":"UNMAPPED","media_count":"0","ontology_id":"","preferred_term":"Columbia
    blood agar base","total_occurrences":"0"}]'
  snapshot_sha256: 58a51002c62583df7dd2c667a003f2644c84fa8e2cb549c7d7ec3ecdc163b1f7
- evidence_id: ev-281a7a479930b71c
  kind: prior_review
  reference: reports/yaml_record_review/20261001T044725Z-Columbia_Blood_Agar_Base.md
  locator: 'YAML Record Review: Columbia blood agar base:2; Target:10; Validation:20;
    Identity and Grounding:27; Evidence:36; Completeness:45; Findings:51; Recommended
    Edits:55; Follow-up Checks:60; Additional Notes:66'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 359fab3b303fed51e459e2b35e946510c3bac86265140e329672e1cd224c3d4e
  quote: 'Findings:

    - **major**: `data/ingredients/unmapped/Columbia_Blood_Agar_Base.yaml` remains
    `UNMAPPED`; the label denotes a named medium or formulation rather than one exact
    chemical substance. Do not exact-match it to a broader parent, component, hydrate,
    salt, or lookalike label.


    Recommended Edits:

    - Curate an exact same-form identity or decomposition for `data/ingredients/unmapped/Columbia_Blood_Agar_Base.yaml`
    before mapping it.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/unmapped/Columbia_Blood_Agar_Base.yaml`,
    `just validate-terms data/ingredients/unmapped/Columbia_Blood_Agar_Base.yaml`
    where applicable, and `just qc-sssom`.'
assessments:
- assessment_id: a-ccdca2cee2fa4c5b
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-d70e774f051088d5
  evidence_ids:
  - ev-a0c86bae38ce9050
  - ev-2b338fbcc7d947a2
  - ev-cae280f8bf37c555
  - ev-ec80982d59e049d7
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-61eb9bcaf0ca5b91
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d70e774f051088d5
  evidence_ids:
  - ev-281a7a479930b71c
  - ev-a0c86bae38ce9050
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T04:47:25Z;
    reviewed SHA-256=29ed63a00d3f4f7a1652beee549526d625eef231f29b40691bd128d2f7608324;
    current SHA-256=29ed63a00d3f4f7a1652beee549526d625eef231f29b40691bd128d2f7608324;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T044725Z-Columbia_Blood_Agar_Base.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Named medium/formulation
    is intentionally left unmapped until a recipe-level CultureMech representation
    owns the formulation.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-281a7a479930b71c
    - ev-a0c86bae38ce9050
  - name: legacy-native-ids
    value: '[]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-a0c86bae38ce9050
    - ev-281a7a479930b71c
- assessment_id: a-c490337db8d3f124
  area: identity
  topic: Unresolved exact identity or preparation
  outcome: unknown
  summary: Current status=UNMAPPED; no supported promotion is established by this
    reconciliation. Preserve the unresolved source boundary; source-backed identity/decomposition
    review is still required.
  target_ids:
  - record-d70e774f051088d5
  evidence_ids:
  - ev-281a7a479930b71c
  - ev-a0c86bae38ce9050
  - ev-cae280f8bf37c555
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-281a7a479930b71c
    - ev-a0c86bae38ce9050
    - ev-cae280f8bf37c555
findings:
- finding_id: rec-f-unmapped-d70e774f051088d5
  issue_key: mim-reconciliation-unresolved-identity-d70e774f051088d5
  category: identity
  severity: major
  status: deferred
  certainty: provisional
  title: 'Unresolved exact identity or preparation: Columbia_Blood_Agar_Base'
  description: Current status=UNMAPPED; no supported promotion is established by this
    reconciliation. Preserve the unresolved source boundary; source-backed identity/decomposition
    review is still required.
  disposition_reason: Current status=UNMAPPED; no supported promotion is established
    by this reconciliation. Preserve the unresolved source boundary; source-backed
    identity/decomposition review is still required.
  target_ids:
  - record-d70e774f051088d5
  evidence_ids:
  - ev-281a7a479930b71c
  - ev-a0c86bae38ce9050
  - ev-cae280f8bf37c555
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/unmapped/Columbia_Blood_Agar_Base.yaml
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
  with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.
```
