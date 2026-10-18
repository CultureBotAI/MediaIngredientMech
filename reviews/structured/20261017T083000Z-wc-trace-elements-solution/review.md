# Per-record structured review: Wc_Trace_Elements_Solution (data/ingredients/mapped/Wc_Trace_Elements_Solution.yaml)

- Review: 20261017T083000Z-wc-trace-elements-solution
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Wc_Trace_Elements_Solution (data/ingredients/mapped/Wc_Trace_Elements_Solution.yaml, record-4a445e71fe30bfaa, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Wc_Trace_Elements_Solution.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Wc_Trace_Elements_Solution.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-4a445e71fe30bfaa | data/ingredients/mapped/Wc_Trace_Elements_Solution.yaml | maintained | Wc_Trace_Elements_Solution |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-4a445e71fe30bfaa | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-4a445e71fe30bfaa | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-4a445e71fe30bfaa | Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-4a445e71fe30bfaa.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-4a445e71fe30bfaa.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:17:04Z; reviewed SHA-256=692af797eb0d2e1a83938dbdd111e8ddcadcc9d881f03696358cede40a126aee; current SHA-256=692af797eb0d2e1a83938dbdd111e8ddcadcc9d881f03696358cede40a126aee; hash_changed=False. Reports=["reports/yaml_record_review/Wc_Trace_Elements_Solution.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The named WC formulation is exact-mapped to generic MICRO:0000455, and TRACE_ELEMENT is still a provisional in-session LLM role.

### Historical provisional-role concern

evidence: concern. Targets: record-4a445e71fe30bfaa.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-5677cebe60c360cf: Reassess prediction-only role support: WC Trace Elements Solution

major / open / confirmed; issue key: mim-reconciliation-role-support-4a445e71fe30bfaa.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-5677cebe60c360cf

Reassess prediction-only role support: WC Trace Elements Solution

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-ac88dbe570e2f62e | data/ingredients/mapped/Wc_Trace_Elements_Solution.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2056],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0000455","line":2058,"mapping_status":"MAPPED","ontology_id":"MICRO:0000455","preferred_term":"WC Trace Elements Solution"}],"identifier":"MICRO:0000455","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"LEXICAL_MATCH","ontology_id":"MICRO:0000455","ontology_label":"trace elements solution","ontology_source":"MICRO"},"preferred_term":"WC Trace Elements Solution","sssom_rows":[{"data_row":2925,"object_id":"MICRO:0000455","object_label":"trace elements solution","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Wc_Trace_Elements_Solution","synonym_count":1} |
| ev-b404841a729b6ea2 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2056] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-b02e155bc694af7a | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Wc_Trace_Elements_Solution; data-row positions=[2925] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2925,"object_id":"MICRO:0000455","object_label":"trace elements solution","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Wc_Trace_Elements_Solution","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-c4d9be2abd8fcd94 | docs/data/mapped_ingredients.csv; CSV lines=[2058] | supports | Published identity and count rows inspected: [{"identifier":"MICRO:0000455","line":2058,"mapping_quality":"LEXICAL_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"MICRO:0000455","preferred_term":"WC Trace Elements Solution","total_occurrences":"2"}] |
| ev-e010475621a6d3d8 | reports/yaml_record_review/Wc_Trace_Elements_Solution.md; &#96;data/ingredients/mapped/Wc_Trace_Elements_Solution.yaml&#96;:2; Verdict:4; Identity:11; Validation:22; Evidence:33; Issues:44; Completeness:54; Recommended Edits:60 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-84b0fcbf01fcbaef | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1345,2001] | context_only | [{"current_record_sha256":"692af797eb0d2e1a83938dbdd111e8ddcadcc9d881f03696358cede40a126aee","finding_id":"SEM:f2679c98abb2072b2bd7","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"692af797eb0d2e1a83938dbdd111e8ddcadcc9d881f03696358cede40a126aee","finding_id":"SEM:84aafbc6d72c66a9660f","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-fd024e221d60d920 | data/ingredients/mapped/Wc_Trace_Elements_Solution.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2056],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0000455","line":2058,"mapping_status":"MAPPED","ontology_id":"MICRO:0000455","preferred_term":"WC Trace Elements Solution"}],"identifier":"MICRO:0000455","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"LEXICAL_MATCH","ontology_id":"MICRO:0000455","ontology_label":"trace elements solution","ontology_source":"MICRO"},"preferred_term":"WC Trace Elements Solution","sssom_rows":[{"data_row":2925,"object_id":"MICRO:0000455","object_label":"trace elements solution","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Wc_Trace_Elements_Solution","synonym_count":1} |
| ev-56fcf843f8e5ae41 | reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml; findings[finding_id=f-5677cebe60c360cf] | context_only | Predecessor structured review finding f-5677cebe60c360cf in 20261011T024639Z-mim-reconcile-all-batch-12 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-wc-trace-elements-solution
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Wc_Trace_Elements_Solution (data/ingredients/mapped/Wc_Trace_Elements_Solution.yaml)'
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
summary: Per-record structured review for Wc_Trace_Elements_Solution (data/ingredients/mapped/Wc_Trace_Elements_Solution.yaml,
  record-4a445e71fe30bfaa, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Wc_Trace_Elements_Solution.yaml
    sha256: 692af797eb0d2e1a83938dbdd111e8ddcadcc9d881f03696358cede40a126aee
    role: target
  - path: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
    sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
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
  - path: reports/yaml_record_review/Wc_Trace_Elements_Solution.md
    sha256: 7368a41efabcdd38cd1c9a5d6f5de6889faf1beb7e4ddc0be89f989bb815b651
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-4a445e71fe30bfaa
  path: data/ingredients/mapped/Wc_Trace_Elements_Solution.yaml
  label: Wc_Trace_Elements_Solution
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Wc_Trace_Elements_Solution.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Wc_Trace_Elements_Solution.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Wc_Trace_Elements_Solution.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-4a445e71fe30bfaa
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-4a445e71fe30bfaa
  evidence_ids:
  - ev-ac88dbe570e2f62e
  - ev-b404841a729b6ea2
  - ev-b02e155bc694af7a
  - ev-c4d9be2abd8fcd94
  - ev-fd024e221d60d920
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-4a445e71fe30bfaa
  evidence_ids:
  - ev-ac88dbe570e2f62e
  - ev-84b0fcbf01fcbaef
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12
    and semantic review dispositions on HEAD.
  target_ids:
  - record-4a445e71fe30bfaa
  evidence_ids:
  - ev-e010475621a6d3d8
  - ev-84b0fcbf01fcbaef
  - ev-56fcf843f8e5ae41
evidence:
- evidence_id: ev-ac88dbe570e2f62e
  kind: record_content
  reference: data/ingredients/mapped/Wc_Trace_Elements_Solution.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2056],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0000455","line":2058,"mapping_status":"MAPPED","ontology_id":"MICRO:0000455","preferred_term":"WC
    Trace Elements Solution"}],"identifier":"MICRO:0000455","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"LEXICAL_MATCH","ontology_id":"MICRO:0000455","ontology_label":"trace
    elements solution","ontology_source":"MICRO"},"preferred_term":"WC Trace Elements
    Solution","sssom_rows":[{"data_row":2925,"object_id":"MICRO:0000455","object_label":"trace
    elements solution","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Wc_Trace_Elements_Solution","synonym_count":1}'
  snapshot_sha256: 692af797eb0d2e1a83938dbdd111e8ddcadcc9d881f03696358cede40a126aee
- evidence_id: ev-b404841a729b6ea2
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2056]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-b02e155bc694af7a
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Wc_Trace_Elements_Solution; data-row positions=[2925]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2925,"object_id":"MICRO:0000455","object_label":"trace
    elements solution","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Wc_Trace_Elements_Solution","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-c4d9be2abd8fcd94
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2058]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"MICRO:0000455","line":2058,"mapping_quality":"LEXICAL_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"MICRO:0000455","preferred_term":"WC
    Trace Elements Solution","total_occurrences":"2"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-e010475621a6d3d8
  kind: prior_review
  reference: reports/yaml_record_review/Wc_Trace_Elements_Solution.md
  locator: '`data/ingredients/mapped/Wc_Trace_Elements_Solution.yaml`:2; Verdict:4;
    Identity:11; Validation:22; Evidence:33; Issues:44; Completeness:54; Recommended
    Edits:60'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 7368a41efabcdd38cd1c9a5d6f5de6889faf1beb7e4ddc0be89f989bb815b651
  quote: "Issues:\n- Major: the exact primary mapping collapses the named WC formulation\
    \ onto the\n  generic MicrO `trace elements solution` term. This should preserve\
    \ an exact\n  local identity for WC Trace Elements Solution rather than asserting\
    \ that the\n  WC formulation is identical to the generic MicrO bucket.\n- Major:\
    \ `nutritional_roles.TRACE_ELEMENT` rests on\n  `COMPUTATIONAL_PREDICTION` evidence\
    \ whose note says it was assigned by\n  in-session Claude reasoning with no external\
    \ API and still needs review.\n\nRecommended Edits:\n- Replace the primary identifier\
    \ with a `kgmicrobe.ingredient` exact identity\n  for WC Trace Elements Solution\
    \ and keep `MICRO:0000455` only as a broader or\n  close generic trace-elements-solution\
    \ parent if useful.\n- Replace or remove the provisional `TRACE_ELEMENT` role\
    \ evidence.\n- Rebuild SSSOM and rerun strict validation, SSSOM invariant validation,\
    \ and\n  the trace-elements exact-to-generic audit."
- evidence_id: ev-84b0fcbf01fcbaef
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1345,2001]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"692af797eb0d2e1a83938dbdd111e8ddcadcc9d881f03696358cede40a126aee","finding_id":"SEM:f2679c98abb2072b2bd7","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"692af797eb0d2e1a83938dbdd111e8ddcadcc9d881f03696358cede40a126aee","finding_id":"SEM:84aafbc6d72c66a9660f","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-fd024e221d60d920
  kind: record_content
  reference: data/ingredients/mapped/Wc_Trace_Elements_Solution.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2056],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0000455","line":2058,"mapping_status":"MAPPED","ontology_id":"MICRO:0000455","preferred_term":"WC
    Trace Elements Solution"}],"identifier":"MICRO:0000455","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"LEXICAL_MATCH","ontology_id":"MICRO:0000455","ontology_label":"trace
    elements solution","ontology_source":"MICRO"},"preferred_term":"WC Trace Elements
    Solution","sssom_rows":[{"data_row":2925,"object_id":"MICRO:0000455","object_label":"trace
    elements solution","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Wc_Trace_Elements_Solution","synonym_count":1}'
  snapshot_sha256: 692af797eb0d2e1a83938dbdd111e8ddcadcc9d881f03696358cede40a126aee
- evidence_id: ev-56fcf843f8e5ae41
  kind: prior_review
  reference: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
  locator: findings[finding_id=f-5677cebe60c360cf]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-5677cebe60c360cf in 20261011T024639Z-mim-reconcile-all-batch-12
  snapshot_sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
assessments:
- assessment_id: a-3d547ec194638112
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-4a445e71fe30bfaa
  evidence_ids:
  - ev-ac88dbe570e2f62e
  - ev-b404841a729b6ea2
  - ev-b02e155bc694af7a
  - ev-c4d9be2abd8fcd94
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-5195a8f04c109cb1
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-4a445e71fe30bfaa
  evidence_ids:
  - ev-e010475621a6d3d8
  - ev-ac88dbe570e2f62e
  - ev-84b0fcbf01fcbaef
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:17:04Z;
    reviewed SHA-256=692af797eb0d2e1a83938dbdd111e8ddcadcc9d881f03696358cede40a126aee;
    current SHA-256=692af797eb0d2e1a83938dbdd111e8ddcadcc9d881f03696358cede40a126aee;
    hash_changed=False. Reports=["reports/yaml_record_review/Wc_Trace_Elements_Solution.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The named
    WC formulation is exact-mapped to generic MICRO:0000455, and TRACE_ELEMENT is
    still a provisional in-session LLM role.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-e010475621a6d3d8
    - ev-ac88dbe570e2f62e
  - name: legacy-native-ids
    value: '["SEM:f2679c98abb2072b2bd7","SEM:84aafbc6d72c66a9660f"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-ac88dbe570e2f62e
    - ev-e010475621a6d3d8
    - ev-84b0fcbf01fcbaef
- assessment_id: a-fd024e221d60d920
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-4a445e71fe30bfaa
  evidence_ids:
  - ev-e010475621a6d3d8
  - ev-fd024e221d60d920
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-e010475621a6d3d8
    - ev-fd024e221d60d920
findings:
- finding_id: rec-f-5677cebe60c360cf
  issue_key: mim-reconciliation-role-support-4a445e71fe30bfaa
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: WC Trace Elements Solution'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-4a445e71fe30bfaa
  evidence_ids:
  - ev-e010475621a6d3d8
  - ev-fd024e221d60d920
  - ev-56fcf843f8e5ae41
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Wc_Trace_Elements_Solution.yaml
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
    review_id: 20261011T024639Z-mim-reconcile-all-batch-12
    finding_id: f-5677cebe60c360cf
actions:
- action_id: rec-action-5677cebe60c360cf
  description: 'Reassess prediction-only role support: WC Trace Elements Solution'
  finding_ids:
  - rec-f-5677cebe60c360cf
  target_ids:
  - record-4a445e71fe30bfaa
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Wc_Trace_Elements_Solution.yaml
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
  with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.
```
