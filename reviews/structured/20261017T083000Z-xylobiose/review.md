# Per-record structured review: Xylobiose (data/ingredients/mapped/Xylobiose.yaml)

- Review: 20261017T083000Z-xylobiose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Xylobiose (data/ingredients/mapped/Xylobiose.yaml, record-a1e5f5e4e87c449b, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Xylobiose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Xylobiose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-a1e5f5e4e87c449b | data/ingredients/mapped/Xylobiose.yaml | maintained | Xylobiose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-a1e5f5e4e87c449b | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-a1e5f5e4e87c449b | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-a1e5f5e4e87c449b | Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-a1e5f5e4e87c449b.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-a1e5f5e4e87c449b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:28:26Z; reviewed SHA-256=c0329daf6d1496687c90f0c8c1c4d27fec6629a14e2e86ca21127cb488a26e0e; current SHA-256=c0329daf6d1496687c90f0c8c1c4d27fec6629a14e2e86ca21127cb488a26e0e; hash_changed=False. Reports=["reports/yaml_record_review/Xylobiose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact ChEBI xylobiose identity passes, but CARBON_SOURCE is still a provisional ChEBI-ancestry role.

### Historical provisional-role concern

evidence: concern. Targets: record-a1e5f5e4e87c449b.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-a14d2c02d009e682: Reassess prediction-only role support: Xylobiose

major / open / confirmed; issue key: mim-reconciliation-role-support-a1e5f5e4e87c449b.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-a14d2c02d009e682

Reassess prediction-only role support: Xylobiose

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-81034ed7fc7e468c | data/ingredients/mapped/Xylobiose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2068],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:28309","line":2070,"mapping_status":"MAPPED","ontology_id":"CHEBI:28309","preferred_term":"Xylobiose"}],"identifier":"CHEBI:28309","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:28309","ontology_label":"xylobiose","ontology_source":"CHEBI"},"preferred_term":"Xylobiose","sssom_rows":[{"data_row":2941,"object_id":"CHEBI:28309","object_label":"xylobiose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Xylobiose","synonym_count":2} |
| ev-0552420fd2b619ed | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2068] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-86086adca8facfe9 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Xylobiose; data-row positions=[2941] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2941,"object_id":"CHEBI:28309","object_label":"xylobiose","other":"1-4-D-Xylobiose&#124;beta-D-xylopyranosyl-(1-&gt;4)-D-xylopyranose&#124;CAS:6860-47-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Xylobiose","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-43dfb4245b8b7085 | docs/data/mapped_ingredients.csv; CSV lines=[2070] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:28309","line":2070,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:28309","preferred_term":"Xylobiose","total_occurrences":"0"}] |
| ev-4b452be07e9a5f15 | reports/yaml_record_review/Xylobiose.md; &#96;data/ingredients/mapped/Xylobiose.yaml&#96;:2; Verdict:4; Identity:10; Validation:24; Evidence:33; Issues:40; Completeness:46; Recommended Edits:51 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-d6526c22e42370f2 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1353,2057] | context_only | [{"current_record_sha256":"c0329daf6d1496687c90f0c8c1c4d27fec6629a14e2e86ca21127cb488a26e0e","finding_id":"SEM:e94de7bee51fccf6049a","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c0329daf6d1496687c90f0c8c1c4d27fec6629a14e2e86ca21127cb488a26e0e","finding_id":"SEM:104e1baec1ee67c20c5f","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-9ca15131f288004a | data/ingredients/mapped/Xylobiose.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred from CHEBI ancestry: subclass/has_role of CHEBI:16646 (carbohydrate)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}] |
| ev-c1c3006f57e29d85 | reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml; findings[finding_id=f-a14d2c02d009e682] | context_only | Predecessor structured review finding f-a14d2c02d009e682 in 20261011T024639Z-mim-reconcile-all-batch-12 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-xylobiose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Xylobiose (data/ingredients/mapped/Xylobiose.yaml)'
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
summary: Per-record structured review for Xylobiose (data/ingredients/mapped/Xylobiose.yaml,
  record-a1e5f5e4e87c449b, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Xylobiose.yaml
    sha256: c0329daf6d1496687c90f0c8c1c4d27fec6629a14e2e86ca21127cb488a26e0e
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
  - path: reports/yaml_record_review/Xylobiose.md
    sha256: d2f2cd6ed838b46154443325934371d57081364dc52b9b881dc12b13f585676b
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-a1e5f5e4e87c449b
  path: data/ingredients/mapped/Xylobiose.yaml
  label: Xylobiose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Xylobiose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Xylobiose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Xylobiose.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-a1e5f5e4e87c449b
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-a1e5f5e4e87c449b
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-a1e5f5e4e87c449b
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12
    and semantic review dispositions on HEAD.
  target_ids:
  - record-a1e5f5e4e87c449b
evidence:
- evidence_id: ev-81034ed7fc7e468c
  kind: record_content
  reference: data/ingredients/mapped/Xylobiose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2068],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:28309","line":2070,"mapping_status":"MAPPED","ontology_id":"CHEBI:28309","preferred_term":"Xylobiose"}],"identifier":"CHEBI:28309","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:28309","ontology_label":"xylobiose","ontology_source":"CHEBI"},"preferred_term":"Xylobiose","sssom_rows":[{"data_row":2941,"object_id":"CHEBI:28309","object_label":"xylobiose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Xylobiose","synonym_count":2}'
  snapshot_sha256: c0329daf6d1496687c90f0c8c1c4d27fec6629a14e2e86ca21127cb488a26e0e
- evidence_id: ev-0552420fd2b619ed
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2068]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-86086adca8facfe9
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Xylobiose; data-row positions=[2941]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2941,"object_id":"CHEBI:28309","object_label":"xylobiose","other":"1-4-D-Xylobiose|beta-D-xylopyranosyl-(1->4)-D-xylopyranose|CAS:6860-47-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Xylobiose","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-43dfb4245b8b7085
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2070]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:28309","line":2070,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:28309","preferred_term":"Xylobiose","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-4b452be07e9a5f15
  kind: prior_review
  reference: reports/yaml_record_review/Xylobiose.md
  locator: '`data/ingredients/mapped/Xylobiose.yaml`:2; Verdict:4; Identity:10; Validation:24;
    Evidence:33; Issues:40; Completeness:46; Recommended Edits:51'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: d2f2cd6ed838b46154443325934371d57081364dc52b9b881dc12b13f585676b
  quote: "Issues:\n- Major: `nutritional_roles.CARBON_SOURCE` rests on\n  `COMPUTATIONAL_PREDICTION`\
    \ evidence whose note says the ChEBI-ancestry role\n  was provisional and still\
    \ needs review.\n\nRecommended Edits:\n- Replace or remove this record's `CARBON_SOURCE`\
    \ role; keep it only if a\n  maintained source supports xylobiose as a carbon\
    \ source in media.\n- Rerun strict validation and SSSOM invariant validation after\
    \ curation."
- evidence_id: ev-d6526c22e42370f2
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1353,2057]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"c0329daf6d1496687c90f0c8c1c4d27fec6629a14e2e86ca21127cb488a26e0e","finding_id":"SEM:e94de7bee51fccf6049a","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c0329daf6d1496687c90f0c8c1c4d27fec6629a14e2e86ca21127cb488a26e0e","finding_id":"SEM:104e1baec1ee67c20c5f","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-9ca15131f288004a
  kind: record_content
  reference: data/ingredients/mapped/Xylobiose.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred
    from CHEBI ancestry: subclass/has_role of CHEBI:16646 (carbohydrate)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}]'
  snapshot_sha256: c0329daf6d1496687c90f0c8c1c4d27fec6629a14e2e86ca21127cb488a26e0e
- evidence_id: ev-c1c3006f57e29d85
  kind: prior_review
  reference: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
  locator: findings[finding_id=f-a14d2c02d009e682]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-a14d2c02d009e682 in 20261011T024639Z-mim-reconcile-all-batch-12
  snapshot_sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
assessments:
- assessment_id: a-a99c65f9e0f9ab7b
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-a1e5f5e4e87c449b
  evidence_ids:
  - ev-81034ed7fc7e468c
  - ev-0552420fd2b619ed
  - ev-86086adca8facfe9
  - ev-43dfb4245b8b7085
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-de00bec992cbb68f
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-a1e5f5e4e87c449b
  evidence_ids:
  - ev-4b452be07e9a5f15
  - ev-81034ed7fc7e468c
  - ev-d6526c22e42370f2
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:28:26Z;
    reviewed SHA-256=c0329daf6d1496687c90f0c8c1c4d27fec6629a14e2e86ca21127cb488a26e0e;
    current SHA-256=c0329daf6d1496687c90f0c8c1c4d27fec6629a14e2e86ca21127cb488a26e0e;
    hash_changed=False. Reports=["reports/yaml_record_review/Xylobiose.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact ChEBI
    xylobiose identity passes, but CARBON_SOURCE is still a provisional ChEBI-ancestry
    role.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-4b452be07e9a5f15
    - ev-81034ed7fc7e468c
  - name: legacy-native-ids
    value: '["SEM:e94de7bee51fccf6049a","SEM:104e1baec1ee67c20c5f"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-81034ed7fc7e468c
    - ev-4b452be07e9a5f15
    - ev-d6526c22e42370f2
- assessment_id: a-9ca15131f288004a
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-a1e5f5e4e87c449b
  evidence_ids:
  - ev-4b452be07e9a5f15
  - ev-9ca15131f288004a
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-4b452be07e9a5f15
    - ev-9ca15131f288004a
findings:
- finding_id: rec-f-a14d2c02d009e682
  issue_key: mim-reconciliation-role-support-a1e5f5e4e87c449b
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Xylobiose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-a1e5f5e4e87c449b
  evidence_ids:
  - ev-4b452be07e9a5f15
  - ev-9ca15131f288004a
  - ev-c1c3006f57e29d85
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Xylobiose.yaml
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
    finding_id: f-a14d2c02d009e682
actions:
- action_id: rec-action-a14d2c02d009e682
  description: 'Reassess prediction-only role support: Xylobiose'
  finding_ids:
  - rec-f-a14d2c02d009e682
  target_ids:
  - record-a1e5f5e4e87c449b
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Xylobiose.yaml
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
