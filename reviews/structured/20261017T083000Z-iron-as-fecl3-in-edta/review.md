# Per-record structured review: Iron_As_Fecl3_In_Edta (data/ingredients/unmapped/Iron_As_Fecl3_In_Edta.yaml)

- Review: 20261017T083000Z-iron-as-fecl3-in-edta
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Iron_As_Fecl3_In_Edta (data/ingredients/unmapped/Iron_As_Fecl3_In_Edta.yaml, record-98c71e771669bad7, mapping_status=UNMAPPED). Records 0 open finding(s) and 2 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/unmapped/Iron_As_Fecl3_In_Edta.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/unmapped/Iron_As_Fecl3_In_Edta.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-98c71e771669bad7 | data/ingredients/unmapped/Iron_As_Fecl3_In_Edta.yaml | maintained | Iron_As_Fecl3_In_Edta |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-98c71e771669bad7 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-98c71e771669bad7 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-98c71e771669bad7 | Reconciled against predecessor batch review 20261011T024640Z-mim-reconcile-all-batch-13 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-98c71e771669bad7.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-98c71e771669bad7.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T04:48:32Z; reviewed SHA-256=ef281b8231d437e1edab7555aa1fa785388a67b748d0a6902483862b93075ac6; current SHA-256=ef281b8231d437e1edab7555aa1fa785388a67b748d0a6902483862b93075ac6; hash_changed=False. Reports=["reports/yaml_record_review/20261001T044832Z-Iron_As_Fecl3_In_Edta.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Specific single-ingredient residual remains unresolved: current evidence does not support an exact ontology or stable-registry identity.

### Unresolved exact identity or preparation

identity: unknown. Targets: record-98c71e771669bad7.

Current status=UNMAPPED; no supported promotion is established by this reconciliation. Preserve the unresolved source boundary; source-backed identity/decomposition review is still required.

## Findings

### rec-f-a82fd6f60ae904bd: Reassess unmapped parent scope: Iron_As_Fecl3_In_Edta

major / deferred / provisional; issue key: mim-semantic-unmapped-parent-scope-98c71e771669bad7.

A component, related compound, or polymer source does not establish a kind-of relationship for the whole ingredient. (Historical finding remains unresolved; no blanket approval.). Affected unit(s): ontology_mapping.

Disposition: A component, related compound, or polymer source does not establish a kind-of relationship for the whole ingredient. (Historical finding remains unresolved; no blanket approval.). Affected unit(s): ontology_mapping.

### rec-f-unmapped-98c71e771669bad7: Unresolved exact identity or preparation: Iron_As_Fecl3_In_Edta

major / deferred / provisional; issue key: mim-reconciliation-unresolved-identity-98c71e771669bad7.

Current status=UNMAPPED; no supported promotion is established by this reconciliation. Preserve the unresolved source boundary; source-backed identity/decomposition review is still required.

Disposition: Current status=UNMAPPED; no supported promotion is established by this reconciliation. Preserve the unresolved source boundary; source-backed identity/decomposition review is still required.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-fcb59576f18a3e70 | data/ingredients/unmapped/Iron_As_Fecl3_In_Edta.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/unmapped_ingredients.yaml","positions":[131],"raw_equal":true},"docs_rows":[{"identifier":"UNMAPPED_0604","line":133,"mapping_status":"UNMAPPED","ontology_id":"NCIT:C598","preferred_term":"Iron (as FeCl3 in EDTA)"}],"identifier":"UNMAPPED_0604","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"UNMAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"NCIT:C598","ontology_label":"Iron","ontology_source":"NCIT"},"preferred_term":"Iron (as FeCl3 in EDTA)","sssom_rows":[],"sssom_subject":"MIM:Iron_As_Fecl3_In_Edta","synonym_count":1} |
| ev-d2868a9dbcb2a64e | data/curated/unmapped_ingredients.yaml; ingredients positions (zero-based): [131] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-a05feb40b8bd9fca | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Iron_As_Fecl3_In_Edta; data-row positions=[] | context_only | Current exact-subject rows, including complete other payload: [] |
| ev-445d1a1198422174 | docs/data/unmapped_ingredients.csv; CSV lines=[133] | supports | Published identity and count rows inspected: [{"identifier":"UNMAPPED_0604","line":133,"mapping_quality":"NARROW_MATCH","mapping_status":"UNMAPPED","media_count":"0","ontology_id":"NCIT:C598","preferred_term":"Iron (as FeCl3 in EDTA)","total_occurrences":"0"}] |
| ev-ae9949c8cba5cee4 | reports/yaml_record_review/20261001T044832Z-Iron_As_Fecl3_In_Edta.md; YAML Record Review: Iron (as FeCl3 in EDTA):2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:45; Findings:51; Recommended Edits:55; Follow-up Checks:60; Additional Notes:66 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-a7ffdf9122472c24 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1369] | context_only | [{"current_record_sha256":"ef281b8231d437e1edab7555aa1fa785388a67b748d0a6902483862b93075ac6","finding_id":"SEM:f423639345025a1a26d6","kind":"unmapped_parent_scope","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-5aaf0da363a2554f | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; current_record=data/ingredients/unmapped/Iron_As_Fecl3_In_Edta.yaml | context_only | Semantic review finding dispositions ledger |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024640Z-mim-reconcile-all-batch-13.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-iron-as-fecl3-in-edta
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Iron_As_Fecl3_In_Edta (data/ingredients/unmapped/Iron_As_Fecl3_In_Edta.yaml)'
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
native_verdict: mapping_status=UNMAPPED; open=0; deferred=2
scientific_review: false
summary: Per-record structured review for Iron_As_Fecl3_In_Edta (data/ingredients/unmapped/Iron_As_Fecl3_In_Edta.yaml,
  record-98c71e771669bad7, mapping_status=UNMAPPED). Records 0 open finding(s) and
  2 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/unmapped/Iron_As_Fecl3_In_Edta.yaml
    sha256: ef281b8231d437e1edab7555aa1fa785388a67b748d0a6902483862b93075ac6
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
  - path: reports/yaml_record_review/20261001T044832Z-Iron_As_Fecl3_In_Edta.md
    sha256: 0ef54160b1596e75e6e3ddba8fced991d17c9e54f4c68005d90dc2fc2abdfce8
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-98c71e771669bad7
  path: data/ingredients/unmapped/Iron_As_Fecl3_In_Edta.yaml
  label: Iron_As_Fecl3_In_Edta
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/unmapped/Iron_As_Fecl3_In_Edta.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/unmapped/Iron_As_Fecl3_In_Edta.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/unmapped/Iron_As_Fecl3_In_Edta.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-98c71e771669bad7
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-98c71e771669bad7
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-98c71e771669bad7
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024640Z-mim-reconcile-all-batch-13
    and semantic review dispositions on HEAD.
  target_ids:
  - record-98c71e771669bad7
evidence:
- evidence_id: ev-fcb59576f18a3e70
  kind: record_content
  reference: data/ingredients/unmapped/Iron_As_Fecl3_In_Edta.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/unmapped_ingredients.yaml","positions":[131],"raw_equal":true},"docs_rows":[{"identifier":"UNMAPPED_0604","line":133,"mapping_status":"UNMAPPED","ontology_id":"NCIT:C598","preferred_term":"Iron
    (as FeCl3 in EDTA)"}],"identifier":"UNMAPPED_0604","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"UNMAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"NCIT:C598","ontology_label":"Iron","ontology_source":"NCIT"},"preferred_term":"Iron
    (as FeCl3 in EDTA)","sssom_rows":[],"sssom_subject":"MIM:Iron_As_Fecl3_In_Edta","synonym_count":1}'
  snapshot_sha256: ef281b8231d437e1edab7555aa1fa785388a67b748d0a6902483862b93075ac6
- evidence_id: ev-d2868a9dbcb2a64e
  kind: validation
  reference: data/curated/unmapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [131]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 8f574be094e741f1d59d55618cc14bf375304644732508bd7a5cd4a817c7fce2
- evidence_id: ev-a05feb40b8bd9fca
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Iron_As_Fecl3_In_Edta; data-row positions=[]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: []'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-445d1a1198422174
  kind: record_content
  reference: docs/data/unmapped_ingredients.csv
  locator: CSV lines=[133]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"UNMAPPED_0604","line":133,"mapping_quality":"NARROW_MATCH","mapping_status":"UNMAPPED","media_count":"0","ontology_id":"NCIT:C598","preferred_term":"Iron
    (as FeCl3 in EDTA)","total_occurrences":"0"}]'
  snapshot_sha256: 58a51002c62583df7dd2c667a003f2644c84fa8e2cb549c7d7ec3ecdc163b1f7
- evidence_id: ev-ae9949c8cba5cee4
  kind: prior_review
  reference: reports/yaml_record_review/20261001T044832Z-Iron_As_Fecl3_In_Edta.md
  locator: 'YAML Record Review: Iron (as FeCl3 in EDTA):2; Target:10; Validation:20;
    Identity and Grounding:27; Evidence:36; Completeness:45; Findings:51; Recommended
    Edits:55; Follow-up Checks:60; Additional Notes:66'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 0ef54160b1596e75e6e3ddba8fced991d17c9e54f4c68005d90dc2fc2abdfce8
  quote: 'Findings:

    - **major**: `data/ingredients/unmapped/Iron_As_Fecl3_In_Edta.yaml` remains `UNMAPPED`;
    no exact ontology term or independently supported registry identity is recorded.
    Do not exact-match it to a broader parent, component, hydrate, salt, or lookalike
    label.


    Recommended Edits:

    - Curate an exact same-form identity or decomposition for `data/ingredients/unmapped/Iron_As_Fecl3_In_Edta.yaml`
    before mapping it.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/unmapped/Iron_As_Fecl3_In_Edta.yaml`,
    `just validate-terms data/ingredients/unmapped/Iron_As_Fecl3_In_Edta.yaml` where
    applicable, and `just qc-sssom`.'
- evidence_id: ev-a7ffdf9122472c24
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1369]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"ef281b8231d437e1edab7555aa1fa785388a67b748d0a6902483862b93075ac6","finding_id":"SEM:f423639345025a1a26d6","kind":"unmapped_parent_scope","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-5aaf0da363a2554f
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: current_record=data/ingredients/unmapped/Iron_As_Fecl3_In_Edta.yaml
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Semantic review finding dispositions ledger
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-0ba1166a56ae2cba
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-98c71e771669bad7
  evidence_ids:
  - ev-fcb59576f18a3e70
  - ev-d2868a9dbcb2a64e
  - ev-a05feb40b8bd9fca
  - ev-445d1a1198422174
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-1fafaeae90c9640f
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-98c71e771669bad7
  evidence_ids:
  - ev-ae9949c8cba5cee4
  - ev-fcb59576f18a3e70
  - ev-a7ffdf9122472c24
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T04:48:32Z;
    reviewed SHA-256=ef281b8231d437e1edab7555aa1fa785388a67b748d0a6902483862b93075ac6;
    current SHA-256=ef281b8231d437e1edab7555aa1fa785388a67b748d0a6902483862b93075ac6;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T044832Z-Iron_As_Fecl3_In_Edta.md"].
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
    - ev-ae9949c8cba5cee4
    - ev-fcb59576f18a3e70
  - name: legacy-native-ids
    value: '["SEM:f423639345025a1a26d6"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-fcb59576f18a3e70
    - ev-ae9949c8cba5cee4
    - ev-a7ffdf9122472c24
- assessment_id: a-7b7d01b13627e5fa
  area: identity
  topic: Unresolved exact identity or preparation
  outcome: unknown
  summary: Current status=UNMAPPED; no supported promotion is established by this
    reconciliation. Preserve the unresolved source boundary; source-backed identity/decomposition
    review is still required.
  target_ids:
  - record-98c71e771669bad7
  evidence_ids:
  - ev-ae9949c8cba5cee4
  - ev-fcb59576f18a3e70
  - ev-a05feb40b8bd9fca
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ae9949c8cba5cee4
    - ev-fcb59576f18a3e70
    - ev-a05feb40b8bd9fca
findings:
- finding_id: rec-f-a82fd6f60ae904bd
  issue_key: mim-semantic-unmapped-parent-scope-98c71e771669bad7
  category: grounding
  severity: major
  status: deferred
  certainty: provisional
  title: 'Reassess unmapped parent scope: Iron_As_Fecl3_In_Edta'
  description: 'A component, related compound, or polymer source does not establish
    a kind-of relationship for the whole ingredient. (Historical finding remains unresolved;
    no blanket approval.). Affected unit(s): ontology_mapping.'
  disposition_reason: 'A component, related compound, or polymer source does not establish
    a kind-of relationship for the whole ingredient. (Historical finding remains unresolved;
    no blanket approval.). Affected unit(s): ontology_mapping.'
  target_ids:
  - record-98c71e771669bad7
  evidence_ids:
  - ev-fcb59576f18a3e70
  - ev-5aaf0da363a2554f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/unmapped/Iron_As_Fecl3_In_Edta.yaml
    role: maintained ingredient
  field_paths:
  - mapping_status
  - ontology_id
  tags:
  - reconciliation
  - bundle-by-owner
  - unmapped-parent-scope
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
- finding_id: rec-f-unmapped-98c71e771669bad7
  issue_key: mim-reconciliation-unresolved-identity-98c71e771669bad7
  category: identity
  severity: major
  status: deferred
  certainty: provisional
  title: 'Unresolved exact identity or preparation: Iron_As_Fecl3_In_Edta'
  description: Current status=UNMAPPED; no supported promotion is established by this
    reconciliation. Preserve the unresolved source boundary; source-backed identity/decomposition
    review is still required.
  disposition_reason: Current status=UNMAPPED; no supported promotion is established
    by this reconciliation. Preserve the unresolved source boundary; source-backed
    identity/decomposition review is still required.
  target_ids:
  - record-98c71e771669bad7
  evidence_ids:
  - ev-ae9949c8cba5cee4
  - ev-fcb59576f18a3e70
  - ev-a05feb40b8bd9fca
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/unmapped/Iron_As_Fecl3_In_Edta.yaml
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
