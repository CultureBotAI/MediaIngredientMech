# Per-record structured review: Algal_Trace_Elements_Solution (data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml)

- Review: 20261017T083000Z-algal-trace-elements-solution
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Algal_Trace_Elements_Solution (data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml, record-9fa8e3d2bfde3386, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-9fa8e3d2bfde3386 | data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml | maintained | Algal_Trace_Elements_Solution |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-9fa8e3d2bfde3386 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-9fa8e3d2bfde3386 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-9fa8e3d2bfde3386 | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-9fa8e3d2bfde3386.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-9fa8e3d2bfde3386.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:01:17Z; reviewed SHA-256=44d6579cade933d4544f51f7aadd20aef899337b28b5d55d50f8f07d47897d0f; current SHA-256=44d6579cade933d4544f51f7aadd20aef899337b28b5d55d50f8f07d47897d0f; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050117Z-Algal_Trace_Elements_Solution.md","reports/yaml_record_review/Algal_Trace_Elements_Solution.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Algal_Trace_Elements_Solution.md&#96; after the record changed from 3f3ae6752048a4120c5c2accff72118a4a546bd2d1bdb1e675be4415b8a9ffbc to 44d6579cade933d4544f51f7aadd20aef899337b28b5d55d50f8f07d47897d0f; preserved the previous major finding floor pending targeted retirement.

### Historical provisional-role concern

evidence: concern. Targets: record-9fa8e3d2bfde3386.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-057cb8a94aa9e597: Reassess prediction-only role support: Algal Trace Elements Solution

major / open / confirmed; issue key: mim-reconciliation-role-support-9fa8e3d2bfde3386.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-057cb8a94aa9e597

Reassess prediction-only role support: Algal Trace Elements Solution

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-5d6261bff9979478 | data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2653],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:algal_trace_elements_solution","line":2655,"mapping_status":"MAPPED","ontology_id":"MICRO:0000455","preferred_term":"Algal Trace Elements Solution"}],"identifier":"kgmicrobe.ingredient:algal_trace_elements_solution","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"MICRO:0000455","ontology_label":"trace elements solution","ontology_source":"MICRO"},"preferred_term":"Algal Trace Elements Solution","sssom_rows":[{"data_row":324,"object_id":"MICRO:0000455","object_label":"trace elements solution","predicate_id":"skos:broadMatch"},{"data_row":2978,"object_id":"kgmicrobe.ingredient:algal_trace_elements_solution","object_label":"Algal Trace Elements Solution","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Algal_Trace_Elements_Solution","synonym_count":1} |
| ev-7596bc5b98e10251 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2653] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-3797625ed7eb69f6 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Algal_Trace_Elements_Solution; data-row positions=[324,2978] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":324,"object_id":"MICRO:0000455","object_label":"trace elements solution","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Algal_Trace_Elements_Solution","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-22"},{"data_row":2978,"object_id":"kgmicrobe.ingredient:algal_trace_elements_solution","object_label":"Algal Trace Elements Solution","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Algal_Trace_Elements_Solution","validation_method":"manual:apply_312_batch3&#124;REGISTRY&#124;2026-09-22"}] |
| ev-6da2a8e5a62bd89d | docs/data/mapped_ingredients.csv; CSV lines=[2655] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:algal_trace_elements_solution","line":2655,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"MICRO:0000455","preferred_term":"Algal Trace Elements Solution","total_occurrences":"1"}] |
| ev-d638a56829b0e5a5 | reports/yaml_record_review/20261001T050117Z-Algal_Trace_Elements_Solution.md; YAML Record Review: Algal Trace Elements Solution:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-bbecb0161b1fcfae | reports/yaml_record_review/Algal_Trace_Elements_Solution.md; &#96;data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml&#96;:2; Verdict:4; Identity:11; Validation:22; Evidence:35; Completeness:58; Recommended Edits:68 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-9d91c875fe82c1b3 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[229,1509] | context_only | [{"current_record_sha256":"44d6579cade933d4544f51f7aadd20aef899337b28b5d55d50f8f07d47897d0f","finding_id":"SEM:c7c67701e68c214a9e61","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"44d6579cade933d4544f51f7aadd20aef899337b28b5d55d50f8f07d47897d0f","finding_id":"SEM:bd4db1d6c2023234a6ce","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-68fa242d4cea407d | data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional in-session LLM role assignment; review recommended.","reference_text":"Assigned by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"TRACE_ELEMENT"}}] |
| ev-0529a32e8a50f2ea | reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml; findings[finding_id=f-057cb8a94aa9e597] | context_only | Predecessor structured review finding f-057cb8a94aa9e597 in 20261011T024631Z-mim-reconcile-all-batch-03 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-algal-trace-elements-solution
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Algal_Trace_Elements_Solution (data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml)'
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
native_verdict: mapping_status=MAPPED; open=1; deferred=0
scientific_review: false
summary: Per-record structured review for Algal_Trace_Elements_Solution (data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml,
  record-9fa8e3d2bfde3386, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml
    sha256: 44d6579cade933d4544f51f7aadd20aef899337b28b5d55d50f8f07d47897d0f
    role: target
  - path: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
    sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
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
  - path: reports/yaml_record_review/20261001T050117Z-Algal_Trace_Elements_Solution.md
    sha256: 554a17d4dedd6a0f83add234d8ddbfebc1ddfb81487a63b0b69f2105766b4b6b
    role: context
  - path: reports/yaml_record_review/Algal_Trace_Elements_Solution.md
    sha256: 0b688d2e5012c3cc13cede1dc5779fa2b1417c0a1b928813ba0229a3327a98d3
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-9fa8e3d2bfde3386
  path: data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml
  label: Algal_Trace_Elements_Solution
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-9fa8e3d2bfde3386
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-9fa8e3d2bfde3386
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-9fa8e3d2bfde3386
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-9fa8e3d2bfde3386
evidence:
- evidence_id: ev-5d6261bff9979478
  kind: record_content
  reference: data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2653],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:algal_trace_elements_solution","line":2655,"mapping_status":"MAPPED","ontology_id":"MICRO:0000455","preferred_term":"Algal
    Trace Elements Solution"}],"identifier":"kgmicrobe.ingredient:algal_trace_elements_solution","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"MICRO:0000455","ontology_label":"trace
    elements solution","ontology_source":"MICRO"},"preferred_term":"Algal Trace Elements
    Solution","sssom_rows":[{"data_row":324,"object_id":"MICRO:0000455","object_label":"trace
    elements solution","predicate_id":"skos:broadMatch"},{"data_row":2978,"object_id":"kgmicrobe.ingredient:algal_trace_elements_solution","object_label":"Algal
    Trace Elements Solution","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Algal_Trace_Elements_Solution","synonym_count":1}'
  snapshot_sha256: 44d6579cade933d4544f51f7aadd20aef899337b28b5d55d50f8f07d47897d0f
- evidence_id: ev-7596bc5b98e10251
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2653]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-3797625ed7eb69f6
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Algal_Trace_Elements_Solution; data-row positions=[324,2978]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":324,"object_id":"MICRO:0000455","object_label":"trace
    elements solution","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Algal_Trace_Elements_Solution","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-22"},{"data_row":2978,"object_id":"kgmicrobe.ingredient:algal_trace_elements_solution","object_label":"Algal
    Trace Elements Solution","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Algal_Trace_Elements_Solution","validation_method":"manual:apply_312_batch3|REGISTRY|2026-09-22"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-6da2a8e5a62bd89d
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2655]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:algal_trace_elements_solution","line":2655,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"MICRO:0000455","preferred_term":"Algal
    Trace Elements Solution","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-d638a56829b0e5a5
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050117Z-Algal_Trace_Elements_Solution.md
  locator: 'YAML Record Review: Algal Trace Elements Solution:2; Target:10; Validation:20;
    Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended
    Edits:56; Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 554a17d4dedd6a0f83add234d8ddbfebc1ddfb81487a63b0b69f2105766b4b6b
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/Algal_Trace_Elements_Solution.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The MICRO
    term resolves, but Algal and WC trace-elements solutions share the same generic
    MICRO:0000455 exact identity and this stock solution needs its own exact ID and
    components.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Algal_Trace_Elements_Solution.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml`,
    `just validate-terms data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml`
    where applicable, and `just qc-sssom`.'
- evidence_id: ev-bbecb0161b1fcfae
  kind: prior_review
  reference: reports/yaml_record_review/Algal_Trace_Elements_Solution.md
  locator: '`data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml`:2; Verdict:4;
    Identity:11; Validation:22; Evidence:35; Completeness:58; Recommended Edits:68'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 0b688d2e5012c3cc13cede1dc5779fa2b1417c0a1b928813ba0229a3327a98d3
  quote: "Recommended Edits:\n- Mint or assign a distinct exact identity for\n  `data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml`,\
    \ demoting\n  `MICRO:0000455` to a parent mapping if generic `trace elements solution`\n\
    \  remains useful.\n- Add component rows for the stock solution when the source\
    \ recipe defines them,\n  and remove the stale duplicate with `WC Trace Elements\
    \ Solution`.\n- Recompute CultureMech membership/occurrence outputs and either\
    \ curate\n  claim-level evidence for `nutritional_roles.TRACE_ELEMENT` or remove\
    \ the\n  provisional role.\n- Regenerate synchronized products, then rerun\n \
    \ `uv run --frozen python scripts/validate_strict.py`,\n  `uv run --frozen python\
    \ scripts/validate_component_partonomy.py`, and\n  `uv run --frozen python scripts/validate_sssom_invariants.py`."
- evidence_id: ev-9d91c875fe82c1b3
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[229,1509]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"44d6579cade933d4544f51f7aadd20aef899337b28b5d55d50f8f07d47897d0f","finding_id":"SEM:c7c67701e68c214a9e61","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"44d6579cade933d4544f51f7aadd20aef899337b28b5d55d50f8f07d47897d0f","finding_id":"SEM:bd4db1d6c2023234a6ce","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-68fa242d4cea407d
  kind: record_content
  reference: data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional
    in-session LLM role assignment; review recommended.","reference_text":"Assigned
    by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"TRACE_ELEMENT"}}]'
  snapshot_sha256: 44d6579cade933d4544f51f7aadd20aef899337b28b5d55d50f8f07d47897d0f
- evidence_id: ev-0529a32e8a50f2ea
  kind: prior_review
  reference: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
  locator: findings[finding_id=f-057cb8a94aa9e597]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-057cb8a94aa9e597 in 20261011T024631Z-mim-reconcile-all-batch-03
  snapshot_sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
assessments:
- assessment_id: a-1181c771506f2c0d
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-9fa8e3d2bfde3386
  evidence_ids:
  - ev-5d6261bff9979478
  - ev-7596bc5b98e10251
  - ev-3797625ed7eb69f6
  - ev-6da2a8e5a62bd89d
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-30d4b160f50c3ce6
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-9fa8e3d2bfde3386
  evidence_ids:
  - ev-d638a56829b0e5a5
  - ev-bbecb0161b1fcfae
  - ev-5d6261bff9979478
  - ev-9d91c875fe82c1b3
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:01:17Z;
    reviewed SHA-256=44d6579cade933d4544f51f7aadd20aef899337b28b5d55d50f8f07d47897d0f;
    current SHA-256=44d6579cade933d4544f51f7aadd20aef899337b28b5d55d50f8f07d47897d0f;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050117Z-Algal_Trace_Elements_Solution.md","reports/yaml_record_review/Algal_Trace_Elements_Solution.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Algal_Trace_Elements_Solution.md` after the record
    changed from 3f3ae6752048a4120c5c2accff72118a4a546bd2d1bdb1e675be4415b8a9ffbc
    to 44d6579cade933d4544f51f7aadd20aef899337b28b5d55d50f8f07d47897d0f; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d638a56829b0e5a5
    - ev-bbecb0161b1fcfae
    - ev-5d6261bff9979478
  - name: legacy-native-ids
    value: '["SEM:c7c67701e68c214a9e61","SEM:bd4db1d6c2023234a6ce"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-5d6261bff9979478
    - ev-d638a56829b0e5a5
    - ev-bbecb0161b1fcfae
    - ev-9d91c875fe82c1b3
- assessment_id: a-68fa242d4cea407d
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-9fa8e3d2bfde3386
  evidence_ids:
  - ev-d638a56829b0e5a5
  - ev-bbecb0161b1fcfae
  - ev-68fa242d4cea407d
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d638a56829b0e5a5
    - ev-bbecb0161b1fcfae
    - ev-68fa242d4cea407d
findings:
- finding_id: rec-f-057cb8a94aa9e597
  issue_key: mim-reconciliation-role-support-9fa8e3d2bfde3386
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Algal Trace Elements Solution'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-9fa8e3d2bfde3386
  evidence_ids:
  - ev-d638a56829b0e5a5
  - ev-bbecb0161b1fcfae
  - ev-68fa242d4cea407d
  - ev-0529a32e8a50f2ea
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024631Z-mim-reconcile-all-batch-03
    finding_id: f-057cb8a94aa9e597
actions:
- action_id: rec-action-057cb8a94aa9e597
  description: 'Reassess prediction-only role support: Algal Trace Elements Solution'
  finding_ids:
  - rec-f-057cb8a94aa9e597
  target_ids:
  - record-9fa8e3d2bfde3386
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml
    role: maintained ingredient
  acceptance_checks:
  - Address the exact fields/tokens and evidence gap described in this finding; preserve
    unrelated source labels and audit history.
  - Inspect the original preparation, organism, or mapping evidence where needed;
    do not promote a label/name-pattern inference to proof.
  - For an authorized fix, synchronize maintained surfaces, run focused validation,
    and save an evidence-backed successor citing this finding.
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
  with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.
```
