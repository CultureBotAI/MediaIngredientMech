# Per-record structured review: Bacto_Brain_Heart_Infusion (data/ingredients/mapped/Bacto_Brain_Heart_Infusion.yaml)

- Review: 20261017T083000Z-bacto-brain-heart-infusion
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Bacto_Brain_Heart_Infusion (data/ingredients/mapped/Bacto_Brain_Heart_Infusion.yaml, record-6cc4e3d057baf45c, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Bacto_Brain_Heart_Infusion.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Bacto_Brain_Heart_Infusion.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-6cc4e3d057baf45c | data/ingredients/mapped/Bacto_Brain_Heart_Infusion.yaml | maintained | Bacto_Brain_Heart_Infusion |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-6cc4e3d057baf45c | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-6cc4e3d057baf45c | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-6cc4e3d057baf45c | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-6cc4e3d057baf45c.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-6cc4e3d057baf45c.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T09:16:44Z; reviewed SHA-256=022df020b7f4660ac46d19baf0847df3ba868608398e97b2f027bb73be58b2f5; current SHA-256=022df020b7f4660ac46d19baf0847df3ba868608398e97b2f027bb73be58b2f5; hash_changed=False. Reports=["reports/yaml_record_review/Bacto_Brain_Heart_Infusion.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The MICRO brain heart infusion mapping, protein-source role, occurrence count, SSSOM row, and aggregate copy pass, but top-level notes still describe the old unmapped state.

### Historical provisional-role concern

evidence: concern. Targets: record-6cc4e3d057baf45c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-a9a56f118b3d7819: Reassess prediction-only role support: Bacto brain heart infusion

major / open / confirmed; issue key: mim-reconciliation-role-support-6cc4e3d057baf45c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-a9a56f118b3d7819

Reassess prediction-only role support: Bacto brain heart infusion

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-69773b60504b5bb5 | data/ingredients/mapped/Bacto_Brain_Heart_Infusion.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[546],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0000193","line":548,"mapping_status":"MAPPED","ontology_id":"MICRO:0000193","preferred_term":"Bacto brain heart infusion"}],"identifier":"MICRO:0000193","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":29,"edge_count":29,"occurrences":29},"occurrence_statistics":{"media_count":29,"total_occurrences":29},"ontology_mapping":{"mapping_quality":"LEXICAL_MATCH","ontology_id":"MICRO:0000193","ontology_label":"brain heart infusion","ontology_source":"MICRO"},"preferred_term":"Bacto brain heart infusion","sssom_rows":[{"data_row":479,"object_id":"MICRO:0000193","object_label":"brain heart infusion","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Bacto_Brain_Heart_Infusion","synonym_count":1} |
| ev-a8c0208ad3d4b66b | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [546] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-064da54573e21e3c | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Bacto_Brain_Heart_Infusion; data-row positions=[479] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":479,"object_id":"MICRO:0000193","object_label":"brain heart infusion","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Bacto_Brain_Heart_Infusion","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-541fda13ee8a0c7e | docs/data/mapped_ingredients.csv; CSV lines=[548] | supports | Published identity and count rows inspected: [{"identifier":"MICRO:0000193","line":548,"mapping_quality":"LEXICAL_MATCH","mapping_status":"MAPPED","media_count":"29","ontology_id":"MICRO:0000193","preferred_term":"Bacto brain heart infusion","total_occurrences":"29"}] |
| ev-b125a6f8a5dfadfb | reports/yaml_record_review/Bacto_Brain_Heart_Infusion.md; &#96;data/ingredients/mapped/Bacto_Brain_Heart_Infusion.yaml&#96;:2; Verdict:4; Identity:11; Validation:23; Evidence:36; Completeness:50; Recommended Edits:58 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-9c52916223b9b3d4 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[291,1886] | context_only | [{"current_record_sha256":"022df020b7f4660ac46d19baf0847df3ba868608398e97b2f027bb73be58b2f5","finding_id":"SEM:2752b85e045e7bebbfb8","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"022df020b7f4660ac46d19baf0847df3ba868608398e97b2f027bb73be58b2f5","finding_id":"SEM:de7a2231fb844c4241d9","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-e1b1be003b9fa318 | data/ingredients/mapped/Bacto_Brain_Heart_Infusion.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"PROTEIN_SOURCE"}}] |
| ev-c433d224ad56574b | reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml; findings[finding_id=f-a9a56f118b3d7819] | context_only | Predecessor structured review finding f-a9a56f118b3d7819 in 20261011T024631Z-mim-reconcile-all-batch-03 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-bacto-brain-heart-infusion
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Bacto_Brain_Heart_Infusion (data/ingredients/mapped/Bacto_Brain_Heart_Infusion.yaml)'
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
summary: Per-record structured review for Bacto_Brain_Heart_Infusion (data/ingredients/mapped/Bacto_Brain_Heart_Infusion.yaml,
  record-6cc4e3d057baf45c, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Bacto_Brain_Heart_Infusion.yaml
    sha256: 022df020b7f4660ac46d19baf0847df3ba868608398e97b2f027bb73be58b2f5
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
  - path: reports/yaml_record_review/Bacto_Brain_Heart_Infusion.md
    sha256: 91651238eccb715b3048ea1c5d83ee808e5fc418a3c349a7bbabcfdf9c7fab11
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-6cc4e3d057baf45c
  path: data/ingredients/mapped/Bacto_Brain_Heart_Infusion.yaml
  label: Bacto_Brain_Heart_Infusion
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bacto_Brain_Heart_Infusion.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Bacto_Brain_Heart_Infusion.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Bacto_Brain_Heart_Infusion.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-6cc4e3d057baf45c
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-6cc4e3d057baf45c
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-6cc4e3d057baf45c
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-6cc4e3d057baf45c
evidence:
- evidence_id: ev-69773b60504b5bb5
  kind: record_content
  reference: data/ingredients/mapped/Bacto_Brain_Heart_Infusion.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[546],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0000193","line":548,"mapping_status":"MAPPED","ontology_id":"MICRO:0000193","preferred_term":"Bacto
    brain heart infusion"}],"identifier":"MICRO:0000193","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":29,"edge_count":29,"occurrences":29},"occurrence_statistics":{"media_count":29,"total_occurrences":29},"ontology_mapping":{"mapping_quality":"LEXICAL_MATCH","ontology_id":"MICRO:0000193","ontology_label":"brain
    heart infusion","ontology_source":"MICRO"},"preferred_term":"Bacto brain heart
    infusion","sssom_rows":[{"data_row":479,"object_id":"MICRO:0000193","object_label":"brain
    heart infusion","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Bacto_Brain_Heart_Infusion","synonym_count":1}'
  snapshot_sha256: 022df020b7f4660ac46d19baf0847df3ba868608398e97b2f027bb73be58b2f5
- evidence_id: ev-a8c0208ad3d4b66b
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [546]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-064da54573e21e3c
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Bacto_Brain_Heart_Infusion; data-row positions=[479]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":479,"object_id":"MICRO:0000193","object_label":"brain
    heart infusion","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Bacto_Brain_Heart_Infusion","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-541fda13ee8a0c7e
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[548]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"MICRO:0000193","line":548,"mapping_quality":"LEXICAL_MATCH","mapping_status":"MAPPED","media_count":"29","ontology_id":"MICRO:0000193","preferred_term":"Bacto
    brain heart infusion","total_occurrences":"29"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-b125a6f8a5dfadfb
  kind: prior_review
  reference: reports/yaml_record_review/Bacto_Brain_Heart_Infusion.md
  locator: '`data/ingredients/mapped/Bacto_Brain_Heart_Infusion.yaml`:2; Verdict:4;
    Identity:11; Validation:23; Evidence:36; Completeness:50; Recommended Edits:58'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 91651238eccb715b3048ea1c5d83ee808e5fc418a3c349a7bbabcfdf9c7fab11
  quote: "Recommended Edits:\n- Remove or rewrite the top-level `notes` in\n  `data/ingredients/mapped/Bacto_Brain_Heart_Infusion.yaml`,\
    \ synchronize\n  `data/curated/mapped_ingredients.yaml`, and rerun focused strict\
    \ validation,\n  SSSOM invariants, product id/label correspondence, and flat-export\
    \ coverage."
- evidence_id: ev-9c52916223b9b3d4
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[291,1886]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"022df020b7f4660ac46d19baf0847df3ba868608398e97b2f027bb73be58b2f5","finding_id":"SEM:2752b85e045e7bebbfb8","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"022df020b7f4660ac46d19baf0847df3ba868608398e97b2f027bb73be58b2f5","finding_id":"SEM:de7a2231fb844c4241d9","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-e1b1be003b9fa318
  kind: record_content
  reference: data/ingredients/mapped/Bacto_Brain_Heart_Infusion.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"PROTEIN_SOURCE"}}]'
  snapshot_sha256: 022df020b7f4660ac46d19baf0847df3ba868608398e97b2f027bb73be58b2f5
- evidence_id: ev-c433d224ad56574b
  kind: prior_review
  reference: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
  locator: findings[finding_id=f-a9a56f118b3d7819]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-a9a56f118b3d7819 in 20261011T024631Z-mim-reconcile-all-batch-03
  snapshot_sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
assessments:
- assessment_id: a-7482ac9a6e1b4d60
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-6cc4e3d057baf45c
  evidence_ids:
  - ev-69773b60504b5bb5
  - ev-a8c0208ad3d4b66b
  - ev-064da54573e21e3c
  - ev-541fda13ee8a0c7e
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-3c67449f562dfa46
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-6cc4e3d057baf45c
  evidence_ids:
  - ev-b125a6f8a5dfadfb
  - ev-69773b60504b5bb5
  - ev-9c52916223b9b3d4
  details: 'Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T09:16:44Z;
    reviewed SHA-256=022df020b7f4660ac46d19baf0847df3ba868608398e97b2f027bb73be58b2f5;
    current SHA-256=022df020b7f4660ac46d19baf0847df3ba868608398e97b2f027bb73be58b2f5;
    hash_changed=False. Reports=["reports/yaml_record_review/Bacto_Brain_Heart_Infusion.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The MICRO
    brain heart infusion mapping, protein-source role, occurrence count, SSSOM row,
    and aggregate copy pass, but top-level notes still describe the old unmapped state.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b125a6f8a5dfadfb
    - ev-69773b60504b5bb5
  - name: legacy-native-ids
    value: '["SEM:2752b85e045e7bebbfb8","SEM:de7a2231fb844c4241d9"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-69773b60504b5bb5
    - ev-b125a6f8a5dfadfb
    - ev-9c52916223b9b3d4
- assessment_id: a-e1b1be003b9fa318
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-6cc4e3d057baf45c
  evidence_ids:
  - ev-b125a6f8a5dfadfb
  - ev-e1b1be003b9fa318
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b125a6f8a5dfadfb
    - ev-e1b1be003b9fa318
findings:
- finding_id: rec-f-a9a56f118b3d7819
  issue_key: mim-reconciliation-role-support-6cc4e3d057baf45c
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Bacto brain heart infusion'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-6cc4e3d057baf45c
  evidence_ids:
  - ev-b125a6f8a5dfadfb
  - ev-e1b1be003b9fa318
  - ev-c433d224ad56574b
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bacto_Brain_Heart_Infusion.yaml
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
    finding_id: f-a9a56f118b3d7819
actions:
- action_id: rec-action-a9a56f118b3d7819
  description: 'Reassess prediction-only role support: Bacto brain heart infusion'
  finding_ids:
  - rec-f-a9a56f118b3d7819
  target_ids:
  - record-6cc4e3d057baf45c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bacto_Brain_Heart_Infusion.yaml
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
