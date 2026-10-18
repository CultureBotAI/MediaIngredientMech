# Per-record structured review: Streptomycin_Sulfate_Salt (data/ingredients/mapped/Streptomycin_Sulfate_Salt.yaml)

- Review: 20261017T083000Z-streptomycin-sulfate-salt
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Streptomycin_Sulfate_Salt (data/ingredients/mapped/Streptomycin_Sulfate_Salt.yaml, record-5acbfbaed5e812df, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Streptomycin_Sulfate_Salt.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Streptomycin_Sulfate_Salt.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-5acbfbaed5e812df | data/ingredients/mapped/Streptomycin_Sulfate_Salt.yaml | maintained | Streptomycin_Sulfate_Salt |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-5acbfbaed5e812df | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-5acbfbaed5e812df | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-5acbfbaed5e812df | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-5acbfbaed5e812df.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-5acbfbaed5e812df.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:42:51Z; reviewed SHA-256=d2a1728eed516fdd0280e1005896d8952497be0e7fdb41af3c50cd8bb78681bb; current SHA-256=d2a1728eed516fdd0280e1005896d8952497be0e7fdb41af3c50cd8bb78681bb; hash_changed=False. Reports=["reports/yaml_record_review/Streptomycin_Sulfate_Salt.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:32158 sulfate identity passes, but SELECTIVE_AGENT remains a provisional name-pattern role.

### Historical provisional-role concern

evidence: concern. Targets: record-5acbfbaed5e812df.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-87049e5b18e6f97d: Reassess prediction-only role support: Streptomycin sulfate salt

major / open / confirmed; issue key: mim-reconciliation-role-support-5acbfbaed5e812df.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-87049e5b18e6f97d

Reassess prediction-only role support: Streptomycin sulfate salt

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-4e30a38d7e27d3aa | data/ingredients/mapped/Streptomycin_Sulfate_Salt.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1900],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:32158","line":1902,"mapping_status":"MAPPED","ontology_id":"CHEBI:32158","preferred_term":"Streptomycin sulfate salt"}],"identifier":"CHEBI:32158","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:32158","ontology_label":"streptomycin sulfate","ontology_source":"CHEBI"},"preferred_term":"Streptomycin sulfate salt","sssom_rows":[{"data_row":2655,"object_id":"CHEBI:32158","object_label":"streptomycin sulfate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Streptomycin_Sulfate_Salt","synonym_count":0} |
| ev-89508bd417e96f5b | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1900] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-b34062c22e4034a5 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Streptomycin_Sulfate_Salt; data-row positions=[2655] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2655,"object_id":"CHEBI:32158","object_label":"streptomycin sulfate","other":"CAS:3810-74-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Streptomycin_Sulfate_Salt","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-9943d5ea42f3079c | docs/data/mapped_ingredients.csv; CSV lines=[1902] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:32158","line":1902,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"3","ontology_id":"CHEBI:32158","preferred_term":"Streptomycin sulfate salt","total_occurrences":"3"}] |
| ev-b7dea8eae9cf84de | reports/yaml_record_review/Streptomycin_Sulfate_Salt.md; &#96;data/ingredients/mapped/Streptomycin_Sulfate_Salt.yaml&#96;:2; Verdict:4; Identity:10; Validation:21; Evidence:30; Completeness:46; Recommended Edits:56 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-dab31a6e7022a40d | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1252,1709] | context_only | [{"current_record_sha256":"d2a1728eed516fdd0280e1005896d8952497be0e7fdb41af3c50cd8bb78681bb","finding_id":"SEM:c3b6d3737e3ca4ff2aad","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"d2a1728eed516fdd0280e1005896d8952497be0e7fdb41af3c50cd8bb78681bb","finding_id":"SEM:324a2089f66992bb411a","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-5e8b6398df7df9e7 | data/ingredients/mapped/Streptomycin_Sulfate_Salt.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1900],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:32158","line":1902,"mapping_status":"MAPPED","ontology_id":"CHEBI:32158","preferred_term":"Streptomycin sulfate salt"}],"identifier":"CHEBI:32158","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:32158","ontology_label":"streptomycin sulfate","ontology_source":"CHEBI"},"preferred_term":"Streptomycin sulfate salt","sssom_rows":[{"data_row":2655,"object_id":"CHEBI:32158","object_label":"streptomycin sulfate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Streptomycin_Sulfate_Salt","synonym_count":0} |
| ev-e9e6c78372ecae10 | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml; findings[finding_id=f-87049e5b18e6f97d] | context_only | Predecessor structured review finding f-87049e5b18e6f97d in 20261011T024638Z-mim-reconcile-all-batch-11 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-streptomycin-sulfate-salt
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Streptomycin_Sulfate_Salt (data/ingredients/mapped/Streptomycin_Sulfate_Salt.yaml)'
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
summary: Per-record structured review for Streptomycin_Sulfate_Salt (data/ingredients/mapped/Streptomycin_Sulfate_Salt.yaml,
  record-5acbfbaed5e812df, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Streptomycin_Sulfate_Salt.yaml
    sha256: d2a1728eed516fdd0280e1005896d8952497be0e7fdb41af3c50cd8bb78681bb
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
  - path: reports/yaml_record_review/Streptomycin_Sulfate_Salt.md
    sha256: 5804ddc268967e12caf88433ea3942c947e5356c59ae8e2f681dd058608bd0a5
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-5acbfbaed5e812df
  path: data/ingredients/mapped/Streptomycin_Sulfate_Salt.yaml
  label: Streptomycin_Sulfate_Salt
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Streptomycin_Sulfate_Salt.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Streptomycin_Sulfate_Salt.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Streptomycin_Sulfate_Salt.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-5acbfbaed5e812df
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-5acbfbaed5e812df
  evidence_ids:
  - ev-4e30a38d7e27d3aa
  - ev-89508bd417e96f5b
  - ev-b34062c22e4034a5
  - ev-9943d5ea42f3079c
  - ev-5e8b6398df7df9e7
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-5acbfbaed5e812df
  evidence_ids:
  - ev-4e30a38d7e27d3aa
  - ev-dab31a6e7022a40d
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-5acbfbaed5e812df
  evidence_ids:
  - ev-b7dea8eae9cf84de
  - ev-dab31a6e7022a40d
  - ev-e9e6c78372ecae10
evidence:
- evidence_id: ev-4e30a38d7e27d3aa
  kind: record_content
  reference: data/ingredients/mapped/Streptomycin_Sulfate_Salt.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1900],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:32158","line":1902,"mapping_status":"MAPPED","ontology_id":"CHEBI:32158","preferred_term":"Streptomycin
    sulfate salt"}],"identifier":"CHEBI:32158","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:32158","ontology_label":"streptomycin
    sulfate","ontology_source":"CHEBI"},"preferred_term":"Streptomycin sulfate salt","sssom_rows":[{"data_row":2655,"object_id":"CHEBI:32158","object_label":"streptomycin
    sulfate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Streptomycin_Sulfate_Salt","synonym_count":0}'
  snapshot_sha256: d2a1728eed516fdd0280e1005896d8952497be0e7fdb41af3c50cd8bb78681bb
- evidence_id: ev-89508bd417e96f5b
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1900]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-b34062c22e4034a5
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Streptomycin_Sulfate_Salt; data-row positions=[2655]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2655,"object_id":"CHEBI:32158","object_label":"streptomycin
    sulfate","other":"CAS:3810-74-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Streptomycin_Sulfate_Salt","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-9943d5ea42f3079c
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1902]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:32158","line":1902,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"3","ontology_id":"CHEBI:32158","preferred_term":"Streptomycin
    sulfate salt","total_occurrences":"3"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-b7dea8eae9cf84de
  kind: prior_review
  reference: reports/yaml_record_review/Streptomycin_Sulfate_Salt.md
  locator: '`data/ingredients/mapped/Streptomycin_Sulfate_Salt.yaml`:2; Verdict:4;
    Identity:10; Validation:21; Evidence:30; Completeness:46; Recommended Edits:56'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 5804ddc268967e12caf88433ea3942c947e5356c59ae8e2f681dd058608bd0a5
  quote: "Recommended Edits:\n- Major: either remove `physicochemical_roles.SELECTIVE_AGENT`\
    \ from\n  `data/ingredients/mapped/Streptomycin_Sulfate_Salt.yaml`, or replace\
    \ the\n  name-pattern evidence with an inspected source showing that streptomycin\n\
    \  sulfate is acting as a selective agent in a culture medium."
- evidence_id: ev-dab31a6e7022a40d
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1252,1709]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"d2a1728eed516fdd0280e1005896d8952497be0e7fdb41af3c50cd8bb78681bb","finding_id":"SEM:c3b6d3737e3ca4ff2aad","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"d2a1728eed516fdd0280e1005896d8952497be0e7fdb41af3c50cd8bb78681bb","finding_id":"SEM:324a2089f66992bb411a","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-5e8b6398df7df9e7
  kind: record_content
  reference: data/ingredients/mapped/Streptomycin_Sulfate_Salt.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1900],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:32158","line":1902,"mapping_status":"MAPPED","ontology_id":"CHEBI:32158","preferred_term":"Streptomycin
    sulfate salt"}],"identifier":"CHEBI:32158","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:32158","ontology_label":"streptomycin
    sulfate","ontology_source":"CHEBI"},"preferred_term":"Streptomycin sulfate salt","sssom_rows":[{"data_row":2655,"object_id":"CHEBI:32158","object_label":"streptomycin
    sulfate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Streptomycin_Sulfate_Salt","synonym_count":0}'
  snapshot_sha256: d2a1728eed516fdd0280e1005896d8952497be0e7fdb41af3c50cd8bb78681bb
- evidence_id: ev-e9e6c78372ecae10
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
  locator: findings[finding_id=f-87049e5b18e6f97d]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-87049e5b18e6f97d in 20261011T024638Z-mim-reconcile-all-batch-11
  snapshot_sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
assessments:
- assessment_id: a-a66b38306def42bc
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-5acbfbaed5e812df
  evidence_ids:
  - ev-4e30a38d7e27d3aa
  - ev-89508bd417e96f5b
  - ev-b34062c22e4034a5
  - ev-9943d5ea42f3079c
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-1963050ecbb67ccf
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-5acbfbaed5e812df
  evidence_ids:
  - ev-b7dea8eae9cf84de
  - ev-4e30a38d7e27d3aa
  - ev-dab31a6e7022a40d
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:42:51Z;
    reviewed SHA-256=d2a1728eed516fdd0280e1005896d8952497be0e7fdb41af3c50cd8bb78681bb;
    current SHA-256=d2a1728eed516fdd0280e1005896d8952497be0e7fdb41af3c50cd8bb78681bb;
    hash_changed=False. Reports=["reports/yaml_record_review/Streptomycin_Sulfate_Salt.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:32158 sulfate identity passes, but SELECTIVE_AGENT remains a provisional
    name-pattern role.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b7dea8eae9cf84de
    - ev-4e30a38d7e27d3aa
  - name: legacy-native-ids
    value: '["SEM:c3b6d3737e3ca4ff2aad","SEM:324a2089f66992bb411a"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-4e30a38d7e27d3aa
    - ev-b7dea8eae9cf84de
    - ev-dab31a6e7022a40d
- assessment_id: a-5e8b6398df7df9e7
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-5acbfbaed5e812df
  evidence_ids:
  - ev-b7dea8eae9cf84de
  - ev-5e8b6398df7df9e7
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b7dea8eae9cf84de
    - ev-5e8b6398df7df9e7
findings:
- finding_id: rec-f-87049e5b18e6f97d
  issue_key: mim-reconciliation-role-support-5acbfbaed5e812df
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Streptomycin sulfate salt'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-5acbfbaed5e812df
  evidence_ids:
  - ev-b7dea8eae9cf84de
  - ev-5e8b6398df7df9e7
  - ev-e9e6c78372ecae10
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Streptomycin_Sulfate_Salt.yaml
    role: maintained ingredient
  field_paths:
  - physicochemical_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024638Z-mim-reconcile-all-batch-11
    finding_id: f-87049e5b18e6f97d
actions:
- action_id: rec-action-87049e5b18e6f97d
  description: 'Reassess prediction-only role support: Streptomycin sulfate salt'
  finding_ids:
  - rec-f-87049e5b18e6f97d
  target_ids:
  - record-5acbfbaed5e812df
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Streptomycin_Sulfate_Salt.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.
```
