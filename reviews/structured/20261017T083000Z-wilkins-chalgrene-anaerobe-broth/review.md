# Per-record structured review: Wilkins_Chalgrene_Anaerobe_Broth (data/ingredients/unmapped/Wilkins_Chalgrene_Anaerobe_Broth.yaml)

- Review: 20261017T083000Z-wilkins-chalgrene-anaerobe-broth
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Wilkins_Chalgrene_Anaerobe_Broth (data/ingredients/unmapped/Wilkins_Chalgrene_Anaerobe_Broth.yaml, record-c15eb6b5d119a77e, mapping_status=UNMAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/unmapped/Wilkins_Chalgrene_Anaerobe_Broth.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/unmapped/Wilkins_Chalgrene_Anaerobe_Broth.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-c15eb6b5d119a77e | data/ingredients/unmapped/Wilkins_Chalgrene_Anaerobe_Broth.yaml | maintained | Wilkins_Chalgrene_Anaerobe_Broth |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-c15eb6b5d119a77e | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-c15eb6b5d119a77e | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-c15eb6b5d119a77e | Reconciled against predecessor batch review 20261011T024640Z-mim-reconcile-all-batch-13 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-c15eb6b5d119a77e.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-c15eb6b5d119a77e.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T04:50:33Z; reviewed SHA-256=62caf082e8739b58a0bafa548b0f5a8a6eff664a25b10b22839a9b5cb46d6d79; current SHA-256=62caf082e8739b58a0bafa548b0f5a8a6eff664a25b10b22839a9b5cb46d6d79; hash_changed=False. Reports=["reports/yaml_record_review/20261001T045033Z-Wilkins_Chalgrene_Anaerobe_Broth.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Named medium/formulation is intentionally left unmapped until a recipe-level CultureMech representation owns the formulation.

### Unresolved exact identity or preparation

identity: unknown. Targets: record-c15eb6b5d119a77e.

Current status=UNMAPPED; no supported promotion is established by this reconciliation. Preserve the unresolved source boundary; source-backed identity/decomposition review is still required.

## Findings

### rec-f-unmapped-c15eb6b5d119a77e: Unresolved exact identity or preparation: Wilkins_Chalgrene_Anaerobe_Broth

major / deferred / provisional; issue key: mim-reconciliation-unresolved-identity-c15eb6b5d119a77e.

Current status=UNMAPPED; no supported promotion is established by this reconciliation. Preserve the unresolved source boundary; source-backed identity/decomposition review is still required.

Disposition: Current status=UNMAPPED; no supported promotion is established by this reconciliation. Preserve the unresolved source boundary; source-backed identity/decomposition review is still required.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-cb1f62aac36314c9 | data/ingredients/unmapped/Wilkins_Chalgrene_Anaerobe_Broth.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/unmapped_ingredients.yaml","positions":[250],"raw_equal":true},"docs_rows":[{"identifier":"UNMAPPED_0578","line":252,"mapping_status":"UNMAPPED","ontology_id":"","preferred_term":"Wilkins Chalgrene Anaerobe Broth"}],"identifier":"UNMAPPED_0578","ingredient_type":"NAMED_MEDIUM","mapping_status":"UNMAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{},"preferred_term":"Wilkins Chalgrene Anaerobe Broth","sssom_rows":[],"sssom_subject":"MIM:Wilkins_Chalgrene_Anaerobe_Broth","synonym_count":1} |
| ev-54067e66a65cb398 | data/curated/unmapped_ingredients.yaml; ingredients positions (zero-based): [250] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-8b60a769fb27807d | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Wilkins_Chalgrene_Anaerobe_Broth; data-row positions=[] | context_only | Current exact-subject rows, including complete other payload: [] |
| ev-f476de4d1202971f | docs/data/unmapped_ingredients.csv; CSV lines=[252] | supports | Published identity and count rows inspected: [{"identifier":"UNMAPPED_0578","line":252,"mapping_quality":"","mapping_status":"UNMAPPED","media_count":"0","ontology_id":"","preferred_term":"Wilkins Chalgrene Anaerobe Broth","total_occurrences":"0"}] |
| ev-9303e12d342b4d5a | reports/yaml_record_review/20261001T045033Z-Wilkins_Chalgrene_Anaerobe_Broth.md; YAML Record Review: Wilkins Chalgrene Anaerobe Broth:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:45; Findings:51; Recommended Edits:55; Follow-up Checks:60; Additional Notes:66 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024640Z-mim-reconcile-all-batch-13.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-wilkins-chalgrene-anaerobe-broth
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Wilkins_Chalgrene_Anaerobe_Broth (data/ingredients/unmapped/Wilkins_Chalgrene_Anaerobe_Broth.yaml)'
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
summary: Per-record structured review for Wilkins_Chalgrene_Anaerobe_Broth (data/ingredients/unmapped/Wilkins_Chalgrene_Anaerobe_Broth.yaml,
  record-c15eb6b5d119a77e, mapping_status=UNMAPPED). Records 0 open finding(s) and
  1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/unmapped/Wilkins_Chalgrene_Anaerobe_Broth.yaml
    sha256: 62caf082e8739b58a0bafa548b0f5a8a6eff664a25b10b22839a9b5cb46d6d79
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
  - path: reports/yaml_record_review/20261001T045033Z-Wilkins_Chalgrene_Anaerobe_Broth.md
    sha256: 336ff6d7dc9d54a26dc3f8807727f662f2b88a59ce665b8d51546a21f2ba0d03
    role: context
targets:
- target_id: record-c15eb6b5d119a77e
  path: data/ingredients/unmapped/Wilkins_Chalgrene_Anaerobe_Broth.yaml
  label: Wilkins_Chalgrene_Anaerobe_Broth
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/unmapped/Wilkins_Chalgrene_Anaerobe_Broth.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/unmapped/Wilkins_Chalgrene_Anaerobe_Broth.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/unmapped/Wilkins_Chalgrene_Anaerobe_Broth.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-c15eb6b5d119a77e
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-c15eb6b5d119a77e
  evidence_ids:
  - ev-cb1f62aac36314c9
  - ev-54067e66a65cb398
  - ev-8b60a769fb27807d
  - ev-f476de4d1202971f
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-c15eb6b5d119a77e
  evidence_ids:
  - ev-cb1f62aac36314c9
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024640Z-mim-reconcile-all-batch-13
    and semantic review dispositions on HEAD.
  target_ids:
  - record-c15eb6b5d119a77e
  evidence_ids:
  - ev-9303e12d342b4d5a
evidence:
- evidence_id: ev-cb1f62aac36314c9
  kind: record_content
  reference: data/ingredients/unmapped/Wilkins_Chalgrene_Anaerobe_Broth.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/unmapped_ingredients.yaml","positions":[250],"raw_equal":true},"docs_rows":[{"identifier":"UNMAPPED_0578","line":252,"mapping_status":"UNMAPPED","ontology_id":"","preferred_term":"Wilkins
    Chalgrene Anaerobe Broth"}],"identifier":"UNMAPPED_0578","ingredient_type":"NAMED_MEDIUM","mapping_status":"UNMAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{},"preferred_term":"Wilkins
    Chalgrene Anaerobe Broth","sssom_rows":[],"sssom_subject":"MIM:Wilkins_Chalgrene_Anaerobe_Broth","synonym_count":1}'
  snapshot_sha256: 62caf082e8739b58a0bafa548b0f5a8a6eff664a25b10b22839a9b5cb46d6d79
- evidence_id: ev-54067e66a65cb398
  kind: validation
  reference: data/curated/unmapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [250]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 8f574be094e741f1d59d55618cc14bf375304644732508bd7a5cd4a817c7fce2
- evidence_id: ev-8b60a769fb27807d
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Wilkins_Chalgrene_Anaerobe_Broth; data-row positions=[]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: []'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-f476de4d1202971f
  kind: record_content
  reference: docs/data/unmapped_ingredients.csv
  locator: CSV lines=[252]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"UNMAPPED_0578","line":252,"mapping_quality":"","mapping_status":"UNMAPPED","media_count":"0","ontology_id":"","preferred_term":"Wilkins
    Chalgrene Anaerobe Broth","total_occurrences":"0"}]'
  snapshot_sha256: 58a51002c62583df7dd2c667a003f2644c84fa8e2cb549c7d7ec3ecdc163b1f7
- evidence_id: ev-9303e12d342b4d5a
  kind: prior_review
  reference: reports/yaml_record_review/20261001T045033Z-Wilkins_Chalgrene_Anaerobe_Broth.md
  locator: 'YAML Record Review: Wilkins Chalgrene Anaerobe Broth:2; Target:10; Validation:20;
    Identity and Grounding:27; Evidence:36; Completeness:45; Findings:51; Recommended
    Edits:55; Follow-up Checks:60; Additional Notes:66'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 336ff6d7dc9d54a26dc3f8807727f662f2b88a59ce665b8d51546a21f2ba0d03
  quote: 'Findings:

    - **major**: `data/ingredients/unmapped/Wilkins_Chalgrene_Anaerobe_Broth.yaml`
    remains `UNMAPPED`; the label denotes a named medium or formulation rather than
    one exact chemical substance. Do not exact-match it to a broader parent, component,
    hydrate, salt, or lookalike label.


    Recommended Edits:

    - Curate an exact same-form identity or decomposition for `data/ingredients/unmapped/Wilkins_Chalgrene_Anaerobe_Broth.yaml`
    before mapping it.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/unmapped/Wilkins_Chalgrene_Anaerobe_Broth.yaml`,
    `just validate-terms data/ingredients/unmapped/Wilkins_Chalgrene_Anaerobe_Broth.yaml`
    where applicable, and `just qc-sssom`.'
assessments:
- assessment_id: a-8ed8d8c2a3d9b470
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-c15eb6b5d119a77e
  evidence_ids:
  - ev-cb1f62aac36314c9
  - ev-54067e66a65cb398
  - ev-8b60a769fb27807d
  - ev-f476de4d1202971f
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-e979fe018d0a0bc0
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-c15eb6b5d119a77e
  evidence_ids:
  - ev-9303e12d342b4d5a
  - ev-cb1f62aac36314c9
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T04:50:33Z;
    reviewed SHA-256=62caf082e8739b58a0bafa548b0f5a8a6eff664a25b10b22839a9b5cb46d6d79;
    current SHA-256=62caf082e8739b58a0bafa548b0f5a8a6eff664a25b10b22839a9b5cb46d6d79;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T045033Z-Wilkins_Chalgrene_Anaerobe_Broth.md"].
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
    - ev-9303e12d342b4d5a
    - ev-cb1f62aac36314c9
  - name: legacy-native-ids
    value: '[]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-cb1f62aac36314c9
    - ev-9303e12d342b4d5a
- assessment_id: a-ab49dff50efaeb8e
  area: identity
  topic: Unresolved exact identity or preparation
  outcome: unknown
  summary: Current status=UNMAPPED; no supported promotion is established by this
    reconciliation. Preserve the unresolved source boundary; source-backed identity/decomposition
    review is still required.
  target_ids:
  - record-c15eb6b5d119a77e
  evidence_ids:
  - ev-9303e12d342b4d5a
  - ev-cb1f62aac36314c9
  - ev-8b60a769fb27807d
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-9303e12d342b4d5a
    - ev-cb1f62aac36314c9
    - ev-8b60a769fb27807d
findings:
- finding_id: rec-f-unmapped-c15eb6b5d119a77e
  issue_key: mim-reconciliation-unresolved-identity-c15eb6b5d119a77e
  category: identity
  severity: major
  status: deferred
  certainty: provisional
  title: 'Unresolved exact identity or preparation: Wilkins_Chalgrene_Anaerobe_Broth'
  description: Current status=UNMAPPED; no supported promotion is established by this
    reconciliation. Preserve the unresolved source boundary; source-backed identity/decomposition
    review is still required.
  disposition_reason: Current status=UNMAPPED; no supported promotion is established
    by this reconciliation. Preserve the unresolved source boundary; source-backed
    identity/decomposition review is still required.
  target_ids:
  - record-c15eb6b5d119a77e
  evidence_ids:
  - ev-9303e12d342b4d5a
  - ev-cb1f62aac36314c9
  - ev-8b60a769fb27807d
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/unmapped/Wilkins_Chalgrene_Anaerobe_Broth.yaml
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
