# Per-record structured review: D-sorbitol (data/ingredients/mapped/D-sorbitol.yaml)

- Review: 20261017T083000Z-d-sorbitol
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for D-sorbitol (data/ingredients/mapped/D-sorbitol.yaml, record-3cabee2baf590734, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/D-sorbitol.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/D-sorbitol.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-3cabee2baf590734 | data/ingredients/mapped/D-sorbitol.yaml | maintained | D-sorbitol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-3cabee2baf590734 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-3cabee2baf590734 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-3cabee2baf590734 | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-3cabee2baf590734.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-3cabee2baf590734.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:51:49Z; reviewed SHA-256=b03dc5b410aa70e2fe4e274031b77b502c05db3c05bf44dd225f91d81f287744; current SHA-256=b03dc5b410aa70e2fe4e274031b77b502c05db3c05bf44dd225f91d81f287744; hash_changed=False. Reports=["reports/yaml_record_review/D-sorbitol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI identity, 3/3 count, CAS token, and final SSSOM synonym payload pass, but the carbon role is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-3cabee2baf590734.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-30a0305e4438e852: Reassess prediction-only role support: D-Sorbitol

major / open / confirmed; issue key: mim-reconciliation-role-support-3cabee2baf590734.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-30a0305e4438e852

Reassess prediction-only role support: D-Sorbitol

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-3c9977819d06b451 | data/ingredients/mapped/D-sorbitol.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[841],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17924","line":843,"mapping_status":"MAPPED","ontology_id":"CHEBI:17924","preferred_term":"D-Sorbitol"}],"identifier":"CHEBI:17924","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17924","ontology_label":"D-glucitol","ontology_source":"CHEBI"},"preferred_term":"D-Sorbitol","sssom_rows":[{"data_row":952,"object_id":"CHEBI:17924","object_label":"D-glucitol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-sorbitol","synonym_count":13} |
| ev-443f323953d363e2 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [841] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-945edb587e5b98bb | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:D-sorbitol; data-row positions=[952] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":952,"object_id":"CHEBI:17924","object_label":"D-glucitol","other":"(-)-D-sorbitol&#124;(-)-sorbitol&#124;(2R,3R,4R,5S)-hexane-1,2,3,4,5,6-hexol&#124;D-(-)-sorbitol&#124;D-Sorbit&#124;D-sorbitol (D-glucitol)&#124;E 420&#124;E-420&#124;E420&#124;G-ol&#124;Glc-ol&#124;L-Gulitol&#124;CAS:50-70-4","predicate_id":"skos:exactMatch","subject_id":"MIM:D-sorbitol","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-bb02726fd6cf0f1d | docs/data/mapped_ingredients.csv; CSV lines=[843] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:17924","line":843,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"3","ontology_id":"CHEBI:17924","preferred_term":"D-Sorbitol","total_occurrences":"3"}] |
| ev-cc55dd12f99f39a7 | reports/yaml_record_review/D-sorbitol.md; &#96;data/ingredients/mapped/D-sorbitol.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:37; Completeness:50; Recommended Edits:59 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-b0be1271e0cbfd47 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[506,1903] | context_only | [{"current_record_sha256":"b03dc5b410aa70e2fe4e274031b77b502c05db3c05bf44dd225f91d81f287744","finding_id":"SEM:8ef04bf3709ff91a79a1","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"b03dc5b410aa70e2fe4e274031b77b502c05db3c05bf44dd225f91d81f287744","finding_id":"SEM:dd4abb6f811151957c9b","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-82217f39a8fb2a0f | data/ingredients/mapped/D-sorbitol.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[841],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17924","line":843,"mapping_status":"MAPPED","ontology_id":"CHEBI:17924","preferred_term":"D-Sorbitol"}],"identifier":"CHEBI:17924","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17924","ontology_label":"D-glucitol","ontology_source":"CHEBI"},"preferred_term":"D-Sorbitol","sssom_rows":[{"data_row":952,"object_id":"CHEBI:17924","object_label":"D-glucitol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-sorbitol","synonym_count":13} |
| ev-219f8e76150cbce0 | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-30a0305e4438e852] | context_only | Predecessor structured review finding f-30a0305e4438e852 in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-d-sorbitol
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: D-sorbitol (data/ingredients/mapped/D-sorbitol.yaml)'
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
summary: Per-record structured review for D-sorbitol (data/ingredients/mapped/D-sorbitol.yaml,
  record-3cabee2baf590734, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/D-sorbitol.yaml
    sha256: b03dc5b410aa70e2fe4e274031b77b502c05db3c05bf44dd225f91d81f287744
    role: target
  - path: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
    sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
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
  - path: reports/yaml_record_review/D-sorbitol.md
    sha256: a24e253e802a73e8a6208cfe02ac67b2fceb9e776c35cd0909f75ad06c53aea5
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-3cabee2baf590734
  path: data/ingredients/mapped/D-sorbitol.yaml
  label: D-sorbitol
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-sorbitol.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/D-sorbitol.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/D-sorbitol.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-3cabee2baf590734
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-3cabee2baf590734
  evidence_ids:
  - ev-3c9977819d06b451
  - ev-443f323953d363e2
  - ev-945edb587e5b98bb
  - ev-bb02726fd6cf0f1d
  - ev-82217f39a8fb2a0f
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-3cabee2baf590734
  evidence_ids:
  - ev-3c9977819d06b451
  - ev-b0be1271e0cbfd47
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-3cabee2baf590734
  evidence_ids:
  - ev-cc55dd12f99f39a7
  - ev-b0be1271e0cbfd47
  - ev-219f8e76150cbce0
evidence:
- evidence_id: ev-3c9977819d06b451
  kind: record_content
  reference: data/ingredients/mapped/D-sorbitol.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[841],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17924","line":843,"mapping_status":"MAPPED","ontology_id":"CHEBI:17924","preferred_term":"D-Sorbitol"}],"identifier":"CHEBI:17924","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17924","ontology_label":"D-glucitol","ontology_source":"CHEBI"},"preferred_term":"D-Sorbitol","sssom_rows":[{"data_row":952,"object_id":"CHEBI:17924","object_label":"D-glucitol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-sorbitol","synonym_count":13}'
  snapshot_sha256: b03dc5b410aa70e2fe4e274031b77b502c05db3c05bf44dd225f91d81f287744
- evidence_id: ev-443f323953d363e2
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [841]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-945edb587e5b98bb
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:D-sorbitol; data-row positions=[952]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":952,"object_id":"CHEBI:17924","object_label":"D-glucitol","other":"(-)-D-sorbitol|(-)-sorbitol|(2R,3R,4R,5S)-hexane-1,2,3,4,5,6-hexol|D-(-)-sorbitol|D-Sorbit|D-sorbitol
    (D-glucitol)|E 420|E-420|E420|G-ol|Glc-ol|L-Gulitol|CAS:50-70-4","predicate_id":"skos:exactMatch","subject_id":"MIM:D-sorbitol","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-bb02726fd6cf0f1d
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[843]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:17924","line":843,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"3","ontology_id":"CHEBI:17924","preferred_term":"D-Sorbitol","total_occurrences":"3"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-cc55dd12f99f39a7
  kind: prior_review
  reference: reports/yaml_record_review/D-sorbitol.md
  locator: '`data/ingredients/mapped/D-sorbitol.yaml`:2; Verdict:4; Identity:11; Validation:21;
    Evidence:37; Completeness:50; Recommended Edits:59'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: a24e253e802a73e8a6208cfe02ac67b2fceb9e776c35cd0909f75ad06c53aea5
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/D-sorbitol.yaml`, remove\
    \ the provisional\n  `CARBON_SOURCE` role or replace its `COMPUTATIONAL_PREDICTION`\
    \ evidence with\n  inspected claim-level evidence.\n- Regenerate synchronized\
    \ curated and SSSOM products, then rerun\n  `uv run --frozen python scripts/validate_strict.py`,\n\
    \  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-sorbitol.yaml\
    \ -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord\
    \ --labels`,\n  `uv run --frozen python scripts/validate_id_label_correspondence.py\
    \ -c conf/id_label_targets.yaml`,\n  and `uv run --frozen python scripts/validate_sssom_invariants.py`."
- evidence_id: ev-b0be1271e0cbfd47
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[506,1903]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"b03dc5b410aa70e2fe4e274031b77b502c05db3c05bf44dd225f91d81f287744","finding_id":"SEM:8ef04bf3709ff91a79a1","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"b03dc5b410aa70e2fe4e274031b77b502c05db3c05bf44dd225f91d81f287744","finding_id":"SEM:dd4abb6f811151957c9b","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-82217f39a8fb2a0f
  kind: record_content
  reference: data/ingredients/mapped/D-sorbitol.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[841],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17924","line":843,"mapping_status":"MAPPED","ontology_id":"CHEBI:17924","preferred_term":"D-Sorbitol"}],"identifier":"CHEBI:17924","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17924","ontology_label":"D-glucitol","ontology_source":"CHEBI"},"preferred_term":"D-Sorbitol","sssom_rows":[{"data_row":952,"object_id":"CHEBI:17924","object_label":"D-glucitol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-sorbitol","synonym_count":13}'
  snapshot_sha256: b03dc5b410aa70e2fe4e274031b77b502c05db3c05bf44dd225f91d81f287744
- evidence_id: ev-219f8e76150cbce0
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-30a0305e4438e852]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-30a0305e4438e852 in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-1356c3686d455975
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-3cabee2baf590734
  evidence_ids:
  - ev-3c9977819d06b451
  - ev-443f323953d363e2
  - ev-945edb587e5b98bb
  - ev-bb02726fd6cf0f1d
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-11f8bd1e5d1422f1
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-3cabee2baf590734
  evidence_ids:
  - ev-cc55dd12f99f39a7
  - ev-3c9977819d06b451
  - ev-b0be1271e0cbfd47
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:51:49Z;
    reviewed SHA-256=b03dc5b410aa70e2fe4e274031b77b502c05db3c05bf44dd225f91d81f287744;
    current SHA-256=b03dc5b410aa70e2fe4e274031b77b502c05db3c05bf44dd225f91d81f287744;
    hash_changed=False. Reports=["reports/yaml_record_review/D-sorbitol.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    identity, 3/3 count, CAS token, and final SSSOM synonym payload pass, but the
    carbon role is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-cc55dd12f99f39a7
    - ev-3c9977819d06b451
  - name: legacy-native-ids
    value: '["SEM:8ef04bf3709ff91a79a1","SEM:dd4abb6f811151957c9b"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-3c9977819d06b451
    - ev-cc55dd12f99f39a7
    - ev-b0be1271e0cbfd47
- assessment_id: a-82217f39a8fb2a0f
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-3cabee2baf590734
  evidence_ids:
  - ev-cc55dd12f99f39a7
  - ev-82217f39a8fb2a0f
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-cc55dd12f99f39a7
    - ev-82217f39a8fb2a0f
findings:
- finding_id: rec-f-30a0305e4438e852
  issue_key: mim-reconciliation-role-support-3cabee2baf590734
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: D-Sorbitol'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-3cabee2baf590734
  evidence_ids:
  - ev-cc55dd12f99f39a7
  - ev-82217f39a8fb2a0f
  - ev-219f8e76150cbce0
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-sorbitol.yaml
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
    review_id: 20261011T024633Z-mim-reconcile-all-batch-05
    finding_id: f-30a0305e4438e852
actions:
- action_id: rec-action-30a0305e4438e852
  description: 'Reassess prediction-only role support: D-Sorbitol'
  finding_ids:
  - rec-f-30a0305e4438e852
  target_ids:
  - record-3cabee2baf590734
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-sorbitol.yaml
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
  with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.
```
