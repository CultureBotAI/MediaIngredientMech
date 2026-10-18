# Per-record structured review: Colistin_Sulfate_Salt (data/ingredients/mapped/Colistin_Sulfate_Salt.yaml)

- Review: 20261017T083000Z-colistin-sulfate-salt
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Colistin_Sulfate_Salt (data/ingredients/mapped/Colistin_Sulfate_Salt.yaml, record-55aca043bdc28359, mapping_status=REJECTED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Colistin_Sulfate_Salt.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Colistin_Sulfate_Salt.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-55aca043bdc28359 | data/ingredients/mapped/Colistin_Sulfate_Salt.yaml | maintained | Colistin_Sulfate_Salt |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-55aca043bdc28359 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-55aca043bdc28359 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-55aca043bdc28359 | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-55aca043bdc28359.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-55aca043bdc28359.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T12:27:40Z; reviewed SHA-256=fda6a3ac8454102f9da57d09cb9821d5807782acb6ee6ead2f0b158ad6ae9f32; current SHA-256=fda6a3ac8454102f9da57d09cb9821d5807782acb6ee6ead2f0b158ad6ae9f32; hash_changed=False. Reports=["reports/yaml_record_review/Colistin_Sulfate_Salt.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The rejected colistin sulfate duplicate has no active SSSOM row, but stale ingredient_type and provisional role fields remain.

### Historical provisional-role concern

evidence: unknown. Targets: record-55aca043bdc28359.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-e1b43606bacb2f33: Reassess prediction-only role support: Colistin sulfate salt

minor / deferred / provisional; issue key: mim-reconciliation-role-support-55aca043bdc28359.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

Disposition: The current local observation is recorded, but the named source/context or policy decision is still required; no correction is inferred.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-708e7a770e5859de | data/ingredients/mapped/Colistin_Sulfate_Salt.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[749],"raw_equal":true},"docs_rows":[{"identifier":"NCIT:C386","line":751,"mapping_status":"REJECTED","ontology_id":"NCIT:C386","preferred_term":"Colistin sulfate salt"}],"identifier":"NCIT:C386","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"NCIT:C386","ontology_label":"Colistin Sulfate","ontology_source":"NCIT"},"preferred_term":"Colistin sulfate salt","sssom_rows":[],"sssom_subject":"MIM:Colistin_Sulfate_Salt","synonym_count":0} |
| ev-019dba59f9f0f10e | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [749] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-72a56158617241c6 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Colistin_Sulfate_Salt; data-row positions=[] | context_only | Current exact-subject rows, including complete other payload: [] |
| ev-a3234651eb3477f7 | docs/data/mapped_ingredients.csv; CSV lines=[751] | supports | Published identity and count rows inspected: [{"identifier":"NCIT:C386","line":751,"mapping_quality":"EXACT_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"NCIT:C386","preferred_term":"Colistin sulfate salt","total_occurrences":"0"}] |
| ev-40c61dc7c4ea49c0 | reports/yaml_record_review/Colistin_Sulfate_Salt.md; &#96;data/ingredients/mapped/Colistin_Sulfate_Salt.yaml&#96;:2; Verdict:4; Identity:12; Validation:27; Evidence:47; Completeness:66; Recommended Edits:73 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-70f567594ea7ef53 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[437] | context_only | [{"current_record_sha256":"fda6a3ac8454102f9da57d09cb9821d5807782acb6ee6ead2f0b158ad6ae9f32","finding_id":"SEM:2476b414d6d11073c4a9","kind":"existing_record_review","resolution_reason":"Source record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}] |
| ev-ff49d03986239fc2 | data/ingredients/mapped/Colistin_Sulfate_Salt.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}] |
| ev-fed83d9263d22f6c | reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml; findings[finding_id=f-e1b43606bacb2f33] | context_only | Predecessor structured review finding f-e1b43606bacb2f33 in 20261011T024632Z-mim-reconcile-all-batch-04 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-colistin-sulfate-salt
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Colistin_Sulfate_Salt (data/ingredients/mapped/Colistin_Sulfate_Salt.yaml)'
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
summary: Per-record structured review for Colistin_Sulfate_Salt (data/ingredients/mapped/Colistin_Sulfate_Salt.yaml,
  record-55aca043bdc28359, mapping_status=REJECTED). Records 0 open finding(s) and
  1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Colistin_Sulfate_Salt.yaml
    sha256: fda6a3ac8454102f9da57d09cb9821d5807782acb6ee6ead2f0b158ad6ae9f32
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
  - path: reports/yaml_record_review/Colistin_Sulfate_Salt.md
    sha256: 1064d772fea1b63f3c1a3aeecac44007e36e45a50745ced0b52ef2c8afd11ed3
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-55aca043bdc28359
  path: data/ingredients/mapped/Colistin_Sulfate_Salt.yaml
  label: Colistin_Sulfate_Salt
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Colistin_Sulfate_Salt.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Colistin_Sulfate_Salt.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Colistin_Sulfate_Salt.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-55aca043bdc28359
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-55aca043bdc28359
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-55aca043bdc28359
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-55aca043bdc28359
evidence:
- evidence_id: ev-708e7a770e5859de
  kind: record_content
  reference: data/ingredients/mapped/Colistin_Sulfate_Salt.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[749],"raw_equal":true},"docs_rows":[{"identifier":"NCIT:C386","line":751,"mapping_status":"REJECTED","ontology_id":"NCIT:C386","preferred_term":"Colistin
    sulfate salt"}],"identifier":"NCIT:C386","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"NCIT:C386","ontology_label":"Colistin
    Sulfate","ontology_source":"NCIT"},"preferred_term":"Colistin sulfate salt","sssom_rows":[],"sssom_subject":"MIM:Colistin_Sulfate_Salt","synonym_count":0}'
  snapshot_sha256: fda6a3ac8454102f9da57d09cb9821d5807782acb6ee6ead2f0b158ad6ae9f32
- evidence_id: ev-019dba59f9f0f10e
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [749]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-72a56158617241c6
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Colistin_Sulfate_Salt; data-row positions=[]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: []'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-a3234651eb3477f7
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[751]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"NCIT:C386","line":751,"mapping_quality":"EXACT_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"NCIT:C386","preferred_term":"Colistin
    sulfate salt","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-40c61dc7c4ea49c0
  kind: prior_review
  reference: reports/yaml_record_review/Colistin_Sulfate_Salt.md
  locator: '`data/ingredients/mapped/Colistin_Sulfate_Salt.yaml`:2; Verdict:4; Identity:12;
    Validation:27; Evidence:47; Completeness:66; Recommended Edits:73'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 1064d772fea1b63f3c1a3aeecac44007e36e45a50745ced0b52ef2c8afd11ed3
  quote: "Recommended Edits:\n- Minor: in `data/ingredients/mapped/Colistin_Sulfate_Salt.yaml`,\
    \ remove the\n  residual `ingredient_type` and `physicochemical_roles` from the\
    \ rejected\n  duplicate.\n- Regenerate synchronized products and rerun strict\
    \ validation, SSSOM QC,\n  aggregate roundtrip, and `git diff --check`."
- evidence_id: ev-70f567594ea7ef53
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[437]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"fda6a3ac8454102f9da57d09cb9821d5807782acb6ee6ead2f0b158ad6ae9f32","finding_id":"SEM:2476b414d6d11073c4a9","kind":"existing_record_review","resolution_reason":"Source
    record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-ff49d03986239fc2
  kind: record_content
  reference: data/ingredients/mapped/Colistin_Sulfate_Salt.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}]'
  snapshot_sha256: fda6a3ac8454102f9da57d09cb9821d5807782acb6ee6ead2f0b158ad6ae9f32
- evidence_id: ev-fed83d9263d22f6c
  kind: prior_review
  reference: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
  locator: findings[finding_id=f-e1b43606bacb2f33]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-e1b43606bacb2f33 in 20261011T024632Z-mim-reconcile-all-batch-04
  snapshot_sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
assessments:
- assessment_id: a-b3b774c67ebe16d6
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-55aca043bdc28359
  evidence_ids:
  - ev-708e7a770e5859de
  - ev-019dba59f9f0f10e
  - ev-72a56158617241c6
  - ev-a3234651eb3477f7
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-794a99641d3cc10b
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-55aca043bdc28359
  evidence_ids:
  - ev-40c61dc7c4ea49c0
  - ev-708e7a770e5859de
  - ev-70f567594ea7ef53
  details: 'Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T12:27:40Z;
    reviewed SHA-256=fda6a3ac8454102f9da57d09cb9821d5807782acb6ee6ead2f0b158ad6ae9f32;
    current SHA-256=fda6a3ac8454102f9da57d09cb9821d5807782acb6ee6ead2f0b158ad6ae9f32;
    hash_changed=False. Reports=["reports/yaml_record_review/Colistin_Sulfate_Salt.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The rejected
    colistin sulfate duplicate has no active SSSOM row, but stale ingredient_type
    and provisional role fields remain.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-40c61dc7c4ea49c0
    - ev-708e7a770e5859de
  - name: legacy-native-ids
    value: '["SEM:2476b414d6d11073c4a9"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-708e7a770e5859de
    - ev-40c61dc7c4ea49c0
    - ev-70f567594ea7ef53
- assessment_id: a-ff49d03986239fc2
  area: evidence
  topic: Historical provisional-role concern
  outcome: unknown
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-55aca043bdc28359
  evidence_ids:
  - ev-40c61dc7c4ea49c0
  - ev-ff49d03986239fc2
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-40c61dc7c4ea49c0
    - ev-ff49d03986239fc2
findings:
- finding_id: rec-f-e1b43606bacb2f33
  issue_key: mim-reconciliation-role-support-55aca043bdc28359
  category: evidence
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Reassess prediction-only role support: Colistin sulfate salt'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-55aca043bdc28359
  evidence_ids:
  - ev-40c61dc7c4ea49c0
  - ev-ff49d03986239fc2
  - ev-fed83d9263d22f6c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Colistin_Sulfate_Salt.yaml
    role: maintained ingredient
  field_paths:
  - physicochemical_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  disposition_reason: The current local observation is recorded, but the named source/context
    or policy decision is still required; no correction is inferred.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024632Z-mim-reconcile-all-batch-04
    finding_id: f-e1b43606bacb2f33
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
