# Per-record structured review: Dihydroxyacetone (data/ingredients/mapped/Dihydroxyacetone.yaml)

- Review: 20261017T083000Z-dihydroxyacetone
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Dihydroxyacetone (data/ingredients/mapped/Dihydroxyacetone.yaml, record-2328a7f6d98a2eca, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Dihydroxyacetone.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Dihydroxyacetone.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-2328a7f6d98a2eca | data/ingredients/mapped/Dihydroxyacetone.yaml | maintained | Dihydroxyacetone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-2328a7f6d98a2eca | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-2328a7f6d98a2eca | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-2328a7f6d98a2eca | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-2328a7f6d98a2eca.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-2328a7f6d98a2eca.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T14:51:37Z; reviewed SHA-256=ad512d73f33938b4dae6de352ea054be42cddde7b61ee3e71b557f2f76dfd677; current SHA-256=ad512d73f33938b4dae6de352ea054be42cddde7b61ee3e71b557f2f76dfd677; hash_changed=False. Reports=["reports/yaml_record_review/Dihydroxyacetone.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact ChEBI identity passes, but the carbon-source role is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-2328a7f6d98a2eca.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-06174fccd6f11930: Reassess prediction-only role support: Dihydroxyacetone

major / open / confirmed; issue key: mim-reconciliation-role-support-2328a7f6d98a2eca.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-06174fccd6f11930

Reassess prediction-only role support: Dihydroxyacetone

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-de39f72e1aa1b9b7 | data/ingredients/mapped/Dihydroxyacetone.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[895],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16016","line":897,"mapping_status":"MAPPED","ontology_id":"CHEBI:16016","preferred_term":"Dihydroxyacetone"}],"identifier":"CHEBI:16016","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16016","ontology_label":"dihydroxyacetone","ontology_source":"CHEBI"},"preferred_term":"Dihydroxyacetone","sssom_rows":[{"data_row":1047,"object_id":"CHEBI:16016","object_label":"dihydroxyacetone","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Dihydroxyacetone","synonym_count":1} |
| ev-e73efa384e10c518 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [895] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-7358af9e68085671 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Dihydroxyacetone; data-row positions=[1047] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1047,"object_id":"CHEBI:16016","object_label":"dihydroxyacetone","other":"1,3-Dihydroxypropan-2-one&#124;CAS:96-26-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Dihydroxyacetone","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-820adb8cee2507c5 | docs/data/mapped_ingredients.csv; CSV lines=[897] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:16016","line":897,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:16016","preferred_term":"Dihydroxyacetone","total_occurrences":"0"}] |
| ev-fadfacb76d0e0deb | reports/yaml_record_review/Dihydroxyacetone.md; &#96;data/ingredients/mapped/Dihydroxyacetone.yaml&#96;:2; Verdict:4; Identity:11; Validation:23; Evidence:39; Completeness:61; Recommended Edits:69 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-516fc22c544e9641 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[542,1900] | context_only | [{"current_record_sha256":"ad512d73f33938b4dae6de352ea054be42cddde7b61ee3e71b557f2f76dfd677","finding_id":"SEM:b322be372ef637287b7d","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"ad512d73f33938b4dae6de352ea054be42cddde7b61ee3e71b557f2f76dfd677","finding_id":"SEM:febc38d11d1b26146dbf","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-f235ebecdc7019b4 | data/ingredients/mapped/Dihydroxyacetone.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[895],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16016","line":897,"mapping_status":"MAPPED","ontology_id":"CHEBI:16016","preferred_term":"Dihydroxyacetone"}],"identifier":"CHEBI:16016","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16016","ontology_label":"dihydroxyacetone","ontology_source":"CHEBI"},"preferred_term":"Dihydroxyacetone","sssom_rows":[{"data_row":1047,"object_id":"CHEBI:16016","object_label":"dihydroxyacetone","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Dihydroxyacetone","synonym_count":1} |
| ev-b94442644ef099c9 | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-06174fccd6f11930] | context_only | Predecessor structured review finding f-06174fccd6f11930 in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-dihydroxyacetone
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Dihydroxyacetone (data/ingredients/mapped/Dihydroxyacetone.yaml)'
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
summary: Per-record structured review for Dihydroxyacetone (data/ingredients/mapped/Dihydroxyacetone.yaml,
  record-2328a7f6d98a2eca, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Dihydroxyacetone.yaml
    sha256: ad512d73f33938b4dae6de352ea054be42cddde7b61ee3e71b557f2f76dfd677
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
  - path: reports/yaml_record_review/Dihydroxyacetone.md
    sha256: 7d3aef960a4a0aae00a8f977b5541fabbc33746ed46a64ea1629dedc5282364d
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-2328a7f6d98a2eca
  path: data/ingredients/mapped/Dihydroxyacetone.yaml
  label: Dihydroxyacetone
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Dihydroxyacetone.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Dihydroxyacetone.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Dihydroxyacetone.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-2328a7f6d98a2eca
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-2328a7f6d98a2eca
  evidence_ids:
  - ev-de39f72e1aa1b9b7
  - ev-e73efa384e10c518
  - ev-7358af9e68085671
  - ev-820adb8cee2507c5
  - ev-f235ebecdc7019b4
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-2328a7f6d98a2eca
  evidence_ids:
  - ev-de39f72e1aa1b9b7
  - ev-516fc22c544e9641
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-2328a7f6d98a2eca
  evidence_ids:
  - ev-fadfacb76d0e0deb
  - ev-516fc22c544e9641
  - ev-b94442644ef099c9
evidence:
- evidence_id: ev-de39f72e1aa1b9b7
  kind: record_content
  reference: data/ingredients/mapped/Dihydroxyacetone.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[895],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16016","line":897,"mapping_status":"MAPPED","ontology_id":"CHEBI:16016","preferred_term":"Dihydroxyacetone"}],"identifier":"CHEBI:16016","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16016","ontology_label":"dihydroxyacetone","ontology_source":"CHEBI"},"preferred_term":"Dihydroxyacetone","sssom_rows":[{"data_row":1047,"object_id":"CHEBI:16016","object_label":"dihydroxyacetone","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Dihydroxyacetone","synonym_count":1}'
  snapshot_sha256: ad512d73f33938b4dae6de352ea054be42cddde7b61ee3e71b557f2f76dfd677
- evidence_id: ev-e73efa384e10c518
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [895]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-7358af9e68085671
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Dihydroxyacetone; data-row positions=[1047]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1047,"object_id":"CHEBI:16016","object_label":"dihydroxyacetone","other":"1,3-Dihydroxypropan-2-one|CAS:96-26-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Dihydroxyacetone","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-820adb8cee2507c5
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[897]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:16016","line":897,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:16016","preferred_term":"Dihydroxyacetone","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-fadfacb76d0e0deb
  kind: prior_review
  reference: reports/yaml_record_review/Dihydroxyacetone.md
  locator: '`data/ingredients/mapped/Dihydroxyacetone.yaml`:2; Verdict:4; Identity:11;
    Validation:23; Evidence:39; Completeness:61; Recommended Edits:69'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 7d3aef960a4a0aae00a8f977b5541fabbc33746ed46a64ea1629dedc5282364d
  quote: "Recommended Edits:\n- Major: replace the `CARBON_SOURCE` computational role\
    \ in\n  `data/ingredients/mapped/Dihydroxyacetone.yaml` with source-backed role\n\
    \  evidence scoped to dihydroxyacetone, or remove the role if no support is\n\
    \  available; then synchronize `data/curated/mapped_ingredients.yaml`."
- evidence_id: ev-516fc22c544e9641
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[542,1900]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"ad512d73f33938b4dae6de352ea054be42cddde7b61ee3e71b557f2f76dfd677","finding_id":"SEM:b322be372ef637287b7d","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"ad512d73f33938b4dae6de352ea054be42cddde7b61ee3e71b557f2f76dfd677","finding_id":"SEM:febc38d11d1b26146dbf","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-f235ebecdc7019b4
  kind: record_content
  reference: data/ingredients/mapped/Dihydroxyacetone.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[895],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16016","line":897,"mapping_status":"MAPPED","ontology_id":"CHEBI:16016","preferred_term":"Dihydroxyacetone"}],"identifier":"CHEBI:16016","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16016","ontology_label":"dihydroxyacetone","ontology_source":"CHEBI"},"preferred_term":"Dihydroxyacetone","sssom_rows":[{"data_row":1047,"object_id":"CHEBI:16016","object_label":"dihydroxyacetone","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Dihydroxyacetone","synonym_count":1}'
  snapshot_sha256: ad512d73f33938b4dae6de352ea054be42cddde7b61ee3e71b557f2f76dfd677
- evidence_id: ev-b94442644ef099c9
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-06174fccd6f11930]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-06174fccd6f11930 in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-7ceef9d90826d823
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-2328a7f6d98a2eca
  evidence_ids:
  - ev-de39f72e1aa1b9b7
  - ev-e73efa384e10c518
  - ev-7358af9e68085671
  - ev-820adb8cee2507c5
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-521ed3b03d3d5795
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-2328a7f6d98a2eca
  evidence_ids:
  - ev-fadfacb76d0e0deb
  - ev-de39f72e1aa1b9b7
  - ev-516fc22c544e9641
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T14:51:37Z;
    reviewed SHA-256=ad512d73f33938b4dae6de352ea054be42cddde7b61ee3e71b557f2f76dfd677;
    current SHA-256=ad512d73f33938b4dae6de352ea054be42cddde7b61ee3e71b557f2f76dfd677;
    hash_changed=False. Reports=["reports/yaml_record_review/Dihydroxyacetone.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    ChEBI identity passes, but the carbon-source role is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-fadfacb76d0e0deb
    - ev-de39f72e1aa1b9b7
  - name: legacy-native-ids
    value: '["SEM:b322be372ef637287b7d","SEM:febc38d11d1b26146dbf"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-de39f72e1aa1b9b7
    - ev-fadfacb76d0e0deb
    - ev-516fc22c544e9641
- assessment_id: a-f235ebecdc7019b4
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-2328a7f6d98a2eca
  evidence_ids:
  - ev-fadfacb76d0e0deb
  - ev-f235ebecdc7019b4
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-fadfacb76d0e0deb
    - ev-f235ebecdc7019b4
findings:
- finding_id: rec-f-06174fccd6f11930
  issue_key: mim-reconciliation-role-support-2328a7f6d98a2eca
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Dihydroxyacetone'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-2328a7f6d98a2eca
  evidence_ids:
  - ev-fadfacb76d0e0deb
  - ev-f235ebecdc7019b4
  - ev-b94442644ef099c9
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Dihydroxyacetone.yaml
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
    finding_id: f-06174fccd6f11930
actions:
- action_id: rec-action-06174fccd6f11930
  description: 'Reassess prediction-only role support: Dihydroxyacetone'
  finding_ids:
  - rec-f-06174fccd6f11930
  target_ids:
  - record-2328a7f6d98a2eca
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Dihydroxyacetone.yaml
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
