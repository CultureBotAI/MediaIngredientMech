# Per-record structured review: PYG-002_Tween_80 (data/ingredients/mapped/PYG-002_Tween_80.yaml)

- Review: 20261017T083000Z-pyg-002-tween-80
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for PYG-002_Tween_80 (data/ingredients/mapped/PYG-002_Tween_80.yaml, record-37c89b14d9a70d91, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/PYG-002_Tween_80.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/PYG-002_Tween_80.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-37c89b14d9a70d91 | data/ingredients/mapped/PYG-002_Tween_80.yaml | maintained | PYG-002_Tween_80 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-37c89b14d9a70d91 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-37c89b14d9a70d91 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-37c89b14d9a70d91 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-37c89b14d9a70d91.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: not_applicable. Targets: record-37c89b14d9a70d91.

The latest legacy review reports no outstanding finding. This run verifies local consistency only; it does not renew that earlier scientific pass.

Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-17T08:19:51Z; reviewed SHA-256=39aa2fd4d32cd75ab37ad154727c197daa5303d9d40fb21771c7bad63e6e489f; current SHA-256=39aa2fd4d32cd75ab37ad154727c197daa5303d9d40fb21771c7bad63e6e489f; hash_changed=False. Reports=["reports/yaml_record_review/PYG-002_Tween_80.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local kgmicrobe.ingredient PYG plus Tween mixture identity, components, and final row pass.

## Findings

### rec-f-7fba61891af85227: Reassess component source scope: PYG-002_Tween_80

major / deferred / provisional; issue key: mim-semantic-component-source-scope-37c89b14d9a70d91.

Expansion/interpretation is retained as an assertion, but the exact source preparation must be verified before semantic approval. UNKNOWN/PARTIAL completeness is not proof of membership. (Historical finding remains unresolved; no blanket approval.). Affected unit(s): MIM.assertion:2442a24f30b32bffaf535a3ecd26f1df0c0422c4ecbd77220f813dcbc726ef57, MIM.assertion:3f8bc2fd4f35b765a1575dd6709830f6597c13966b792102168a289ecda3a833, MIM.assertion:818631ebdaa5e55174bbaade8cc1ff20fc04ea0e3d4c4a34ea31879702c6d3ec, MIM.assertion:825bbd38d4f19c6231083ca178f6e33e9a508b5ce789c47a3f98b4e0189dafa3.

Disposition: Expansion/interpretation is retained as an assertion, but the exact source preparation must be verified before semantic approval. UNKNOWN/PARTIAL completeness is not proof of membership. (Historical finding remains unresolved; no blanket approval.). Affected unit(s): MIM.assertion:2442a24f30b32bffaf535a3ecd26f1df0c0422c4ecbd77220f813dcbc726ef57, MIM.assertion:3f8bc2fd4f35b765a1575dd6709830f6597c13966b792102168a289ecda3a833, MIM.assertion:818631ebdaa5e55174bbaade8cc1ff20fc04ea0e3d4c4a34ea31879702c6d3ec, MIM.assertion:825bbd38d4f19c6231083ca178f6e33e9a508b5ce789c47a3f98b4e0189dafa3.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-24aea816164916b1 | data/ingredients/mapped/PYG-002_Tween_80.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[54],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:pyg_0_02_tween_80","line":56,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:pyg_0_02_tween_80","preferred_term":"PYG-0.02% Tween 80"}],"identifier":"kgmicrobe.ingredient:pyg_0_02_tween_80","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"bergey:substrates"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:pyg_0_02_tween_80","ontology_label":"PYG-0.02% Tween 80","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"PYG-0.02% Tween 80","sssom_rows":[{"data_row":2181,"object_id":"kgmicrobe.ingredient:pyg_0_02_tween_80","object_label":"PYG-0.02% Tween 80","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:PYG-002_Tween_80","synonym_count":1} |
| ev-918e0fda3cf96165 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [54] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-53b01bef8d890b80 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:PYG-002_Tween_80; data-row positions=[2181] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2181,"object_id":"kgmicrobe.ingredient:pyg_0_02_tween_80","object_label":"PYG-0.02% Tween 80","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:PYG-002_Tween_80","validation_method":"manual:move_mapped_out_of_unmapped_collection&#124;MOVED&#124;2026-08-15"}] |
| ev-c98f2fd9e725b171 | docs/data/mapped_ingredients.csv; CSV lines=[56] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:pyg_0_02_tween_80","line":56,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:pyg_0_02_tween_80","preferred_term":"PYG-0.02% Tween 80","total_occurrences":"0"}] |
| ev-e19dfc75391137fe | reports/yaml_record_review/PYG-002_Tween_80.md; &#96;data/ingredients/mapped/PYG-002_Tween_80.yaml&#96;:2; Verdict:4; Identity:10; Validation:22; Evidence:34; Completeness:51; Recommended Edits:58 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-4b84f49adf3e518c | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1492,1563,1729,1735] | context_only | [{"current_record_sha256":"39aa2fd4d32cd75ab37ad154727c197daa5303d9d40fb21771c7bad63e6e489f","finding_id":"SEM:9b00dba6999733399b0f","kind":"component_source_scope","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"39aa2fd4d32cd75ab37ad154727c197daa5303d9d40fb21771c7bad63e6e489f","finding_id":"SEM:7ad88e71c702b5583572","kind":"component_source_scope","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"39aa2fd4d32cd75ab37ad154727c197daa5303d9d40fb21771c7bad63e6e489f","finding_id":"SEM:ee7eb036e32825ada78e","kind":"component_source_scope","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"39aa2fd4d32cd75ab37ad154727c197daa5303d9d40fb21771c7bad63e6e489f","finding_id":"SEM:2727a56eabc39e4c1fa4","kind":"component_source_scope","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-efeae8cb2978776a | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; current_record=data/ingredients/mapped/PYG-002_Tween_80.yaml | context_only | Semantic review finding dispositions ledger |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-pyg-002-tween-80
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: PYG-002_Tween_80 (data/ingredients/mapped/PYG-002_Tween_80.yaml)'
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
summary: Per-record structured review for PYG-002_Tween_80 (data/ingredients/mapped/PYG-002_Tween_80.yaml,
  record-37c89b14d9a70d91, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/PYG-002_Tween_80.yaml
    sha256: 39aa2fd4d32cd75ab37ad154727c197daa5303d9d40fb21771c7bad63e6e489f
    role: target
  - path: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
    sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
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
  - path: reports/yaml_record_review/PYG-002_Tween_80.md
    sha256: dadd25838dba393096ff6d77a8f5e2258376e5bb4e90ce8f08e75e350244db5e
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-37c89b14d9a70d91
  path: data/ingredients/mapped/PYG-002_Tween_80.yaml
  label: PYG-002_Tween_80
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/PYG-002_Tween_80.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/PYG-002_Tween_80.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/PYG-002_Tween_80.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-37c89b14d9a70d91
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-37c89b14d9a70d91
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-37c89b14d9a70d91
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-37c89b14d9a70d91
evidence:
- evidence_id: ev-24aea816164916b1
  kind: record_content
  reference: data/ingredients/mapped/PYG-002_Tween_80.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[54],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:pyg_0_02_tween_80","line":56,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:pyg_0_02_tween_80","preferred_term":"PYG-0.02%
    Tween 80"}],"identifier":"kgmicrobe.ingredient:pyg_0_02_tween_80","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"bergey:substrates"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:pyg_0_02_tween_80","ontology_label":"PYG-0.02%
    Tween 80","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"PYG-0.02%
    Tween 80","sssom_rows":[{"data_row":2181,"object_id":"kgmicrobe.ingredient:pyg_0_02_tween_80","object_label":"PYG-0.02%
    Tween 80","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:PYG-002_Tween_80","synonym_count":1}'
  snapshot_sha256: 39aa2fd4d32cd75ab37ad154727c197daa5303d9d40fb21771c7bad63e6e489f
- evidence_id: ev-918e0fda3cf96165
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [54]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-53b01bef8d890b80
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:PYG-002_Tween_80; data-row positions=[2181]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2181,"object_id":"kgmicrobe.ingredient:pyg_0_02_tween_80","object_label":"PYG-0.02%
    Tween 80","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:PYG-002_Tween_80","validation_method":"manual:move_mapped_out_of_unmapped_collection|MOVED|2026-08-15"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-c98f2fd9e725b171
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[56]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:pyg_0_02_tween_80","line":56,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:pyg_0_02_tween_80","preferred_term":"PYG-0.02%
    Tween 80","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-e19dfc75391137fe
  kind: prior_review
  reference: reports/yaml_record_review/PYG-002_Tween_80.md
  locator: '`data/ingredients/mapped/PYG-002_Tween_80.yaml`:2; Verdict:4; Identity:10;
    Validation:22; Evidence:34; Completeness:51; Recommended Edits:58'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: dadd25838dba393096ff6d77a8f5e2258376e5bb4e90ce8f08e75e350244db5e
  quote: 'Recommended Edits:

    - None.'
- evidence_id: ev-4b84f49adf3e518c
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1492,1563,1729,1735]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"39aa2fd4d32cd75ab37ad154727c197daa5303d9d40fb21771c7bad63e6e489f","finding_id":"SEM:9b00dba6999733399b0f","kind":"component_source_scope","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"39aa2fd4d32cd75ab37ad154727c197daa5303d9d40fb21771c7bad63e6e489f","finding_id":"SEM:7ad88e71c702b5583572","kind":"component_source_scope","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"39aa2fd4d32cd75ab37ad154727c197daa5303d9d40fb21771c7bad63e6e489f","finding_id":"SEM:ee7eb036e32825ada78e","kind":"component_source_scope","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"39aa2fd4d32cd75ab37ad154727c197daa5303d9d40fb21771c7bad63e6e489f","finding_id":"SEM:2727a56eabc39e4c1fa4","kind":"component_source_scope","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-efeae8cb2978776a
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: current_record=data/ingredients/mapped/PYG-002_Tween_80.yaml
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Semantic review finding dispositions ledger
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-2e6cae436d7d3761
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-37c89b14d9a70d91
  evidence_ids:
  - ev-24aea816164916b1
  - ev-918e0fda3cf96165
  - ev-53b01bef8d890b80
  - ev-c98f2fd9e725b171
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-44cd6261b5fb136e
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: not_applicable
  summary: The latest legacy review reports no outstanding finding. This run verifies
    local consistency only; it does not renew that earlier scientific pass.
  target_ids:
  - record-37c89b14d9a70d91
  evidence_ids:
  - ev-e19dfc75391137fe
  - ev-24aea816164916b1
  - ev-4b84f49adf3e518c
  details: 'Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-17T08:19:51Z;
    reviewed SHA-256=39aa2fd4d32cd75ab37ad154727c197daa5303d9d40fb21771c7bad63e6e489f;
    current SHA-256=39aa2fd4d32cd75ab37ad154727c197daa5303d9d40fb21771c7bad63e6e489f;
    hash_changed=False. Reports=["reports/yaml_record_review/PYG-002_Tween_80.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    kgmicrobe.ingredient PYG plus Tween mixture identity, components, and final row
    pass.'
  dimensions:
  - name: legacy-native-ids
    value: '["SEM:9b00dba6999733399b0f","SEM:7ad88e71c702b5583572","SEM:ee7eb036e32825ada78e","SEM:2727a56eabc39e4c1fa4"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-24aea816164916b1
    - ev-e19dfc75391137fe
    - ev-4b84f49adf3e518c
findings:
- finding_id: rec-f-7fba61891af85227
  issue_key: mim-semantic-component-source-scope-37c89b14d9a70d91
  category: representation
  severity: major
  status: deferred
  certainty: provisional
  title: 'Reassess component source scope: PYG-002_Tween_80'
  description: 'Expansion/interpretation is retained as an assertion, but the exact
    source preparation must be verified before semantic approval. UNKNOWN/PARTIAL
    completeness is not proof of membership. (Historical finding remains unresolved;
    no blanket approval.). Affected unit(s): MIM.assertion:2442a24f30b32bffaf535a3ecd26f1df0c0422c4ecbd77220f813dcbc726ef57,
    MIM.assertion:3f8bc2fd4f35b765a1575dd6709830f6597c13966b792102168a289ecda3a833,
    MIM.assertion:818631ebdaa5e55174bbaade8cc1ff20fc04ea0e3d4c4a34ea31879702c6d3ec,
    MIM.assertion:825bbd38d4f19c6231083ca178f6e33e9a508b5ce789c47a3f98b4e0189dafa3.'
  disposition_reason: 'Expansion/interpretation is retained as an assertion, but the
    exact source preparation must be verified before semantic approval. UNKNOWN/PARTIAL
    completeness is not proof of membership. (Historical finding remains unresolved;
    no blanket approval.). Affected unit(s): MIM.assertion:2442a24f30b32bffaf535a3ecd26f1df0c0422c4ecbd77220f813dcbc726ef57,
    MIM.assertion:3f8bc2fd4f35b765a1575dd6709830f6597c13966b792102168a289ecda3a833,
    MIM.assertion:818631ebdaa5e55174bbaade8cc1ff20fc04ea0e3d4c4a34ea31879702c6d3ec,
    MIM.assertion:825bbd38d4f19c6231083ca178f6e33e9a508b5ce789c47a3f98b4e0189dafa3.'
  target_ids:
  - record-37c89b14d9a70d91
  evidence_ids:
  - ev-24aea816164916b1
  - ev-efeae8cb2978776a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/PYG-002_Tween_80.yaml
    role: maintained ingredient
  field_paths:
  - synonyms
  - occurrence_statistics
  tags:
  - reconciliation
  - bundle-by-owner
  - component-source-scope
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
  with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.
```
