# Per-record structured review: Stachyose_-_70 (data/ingredients/mapped/Stachyose_-_70.yaml)

- Review: 20261017T083000Z-stachyose-70
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Stachyose_-_70 (data/ingredients/mapped/Stachyose_-_70.yaml, record-bedfc824f9f602aa, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Stachyose_-_70.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Stachyose_-_70.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-bedfc824f9f602aa | data/ingredients/mapped/Stachyose_-_70.yaml | maintained | Stachyose_-_70 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-bedfc824f9f602aa | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-bedfc824f9f602aa | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-bedfc824f9f602aa | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-bedfc824f9f602aa.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-bedfc824f9f602aa.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:23:59Z; reviewed SHA-256=1a8a006b5d391e6b72f240c7e38e59491976b19d65f91216620bb2935d4d5605; current SHA-256=1a8a006b5d391e6b72f240c7e38e59491976b19d65f91216620bb2935d4d5605; hash_changed=False. Reports=["reports/yaml_record_review/Stachyose_-_70.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The 70% stachyose row exact-maps a qualified preparation, exports Stachyose hydrate, and has a provisional CARBON_SOURCE role.

### Historical provisional-role concern

evidence: concern. Targets: record-bedfc824f9f602aa.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-daed55dde87c7afd: Reassess prediction-only role support: Stachyose - 70%

major / open / confirmed; issue key: mim-reconciliation-role-support-bedfc824f9f602aa.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-daed55dde87c7afd

Reassess prediction-only role support: Stachyose - 70%

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-445c3705010cbf61 | data/ingredients/mapped/Stachyose_-_70.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1893],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17164","line":1895,"mapping_status":"MAPPED","ontology_id":"CHEBI:17164","preferred_term":"Stachyose - 70%"}],"identifier":"CHEBI:17164","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17164","ontology_label":"stachyose","ontology_source":"CHEBI"},"preferred_term":"Stachyose - 70%","sssom_rows":[{"data_row":2642,"object_id":"CHEBI:17164","object_label":"stachyose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Stachyose_-_70","synonym_count":1} |
| ev-734604da326e89f9 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1893] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-fa70562baa8c1154 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Stachyose_-_70; data-row positions=[2642] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2642,"object_id":"CHEBI:17164","object_label":"stachyose","other":"Stachyose hydrate&#124;beta-D-fructofuranosyl alpha-D-galactopyranosyl-(1-&gt;6)-alpha-D-galactopyranosyl-(1-&gt;6)-alpha-D-glucopyranoside&#124;CAS:470-55-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Stachyose_-_70","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-06fe3ebf74ce4e3a | docs/data/mapped_ingredients.csv; CSV lines=[1895] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:17164","line":1895,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:17164","preferred_term":"Stachyose - 70%","total_occurrences":"0"}] |
| ev-08c62b91430fe090 | reports/yaml_record_review/Stachyose_-_70.md; &#96;data/ingredients/mapped/Stachyose_-_70.yaml&#96;:2; Verdict:4; Identity:10; Validation:20; Evidence:29; Completeness:45; Recommended Edits:51 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-0319aa4188a3c54d | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1246,1692] | context_only | [{"current_record_sha256":"1a8a006b5d391e6b72f240c7e38e59491976b19d65f91216620bb2935d4d5605","finding_id":"SEM:55c06ddf3067d41c7dd7","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"1a8a006b5d391e6b72f240c7e38e59491976b19d65f91216620bb2935d4d5605","finding_id":"SEM:5c40c4ae1e96d348918d","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-1f0ac1c262dfb4fa | data/ingredients/mapped/Stachyose_-_70.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1893],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17164","line":1895,"mapping_status":"MAPPED","ontology_id":"CHEBI:17164","preferred_term":"Stachyose - 70%"}],"identifier":"CHEBI:17164","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17164","ontology_label":"stachyose","ontology_source":"CHEBI"},"preferred_term":"Stachyose - 70%","sssom_rows":[{"data_row":2642,"object_id":"CHEBI:17164","object_label":"stachyose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Stachyose_-_70","synonym_count":1} |
| ev-d2664c436d2ab360 | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml; findings[finding_id=f-daed55dde87c7afd] | context_only | Predecessor structured review finding f-daed55dde87c7afd in 20261011T024638Z-mim-reconcile-all-batch-11 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-stachyose-70
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Stachyose_-_70 (data/ingredients/mapped/Stachyose_-_70.yaml)'
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
summary: Per-record structured review for Stachyose_-_70 (data/ingredients/mapped/Stachyose_-_70.yaml,
  record-bedfc824f9f602aa, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Stachyose_-_70.yaml
    sha256: 1a8a006b5d391e6b72f240c7e38e59491976b19d65f91216620bb2935d4d5605
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
  - path: reports/yaml_record_review/Stachyose_-_70.md
    sha256: b9286c995d770e4be7d0a4ec952a7bc47f55d622f5f1ec74d9bc236f21a2be5e
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-bedfc824f9f602aa
  path: data/ingredients/mapped/Stachyose_-_70.yaml
  label: Stachyose_-_70
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Stachyose_-_70.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Stachyose_-_70.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Stachyose_-_70.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-bedfc824f9f602aa
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-bedfc824f9f602aa
  evidence_ids:
  - ev-445c3705010cbf61
  - ev-734604da326e89f9
  - ev-fa70562baa8c1154
  - ev-06fe3ebf74ce4e3a
  - ev-1f0ac1c262dfb4fa
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-bedfc824f9f602aa
  evidence_ids:
  - ev-445c3705010cbf61
  - ev-0319aa4188a3c54d
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-bedfc824f9f602aa
  evidence_ids:
  - ev-08c62b91430fe090
  - ev-0319aa4188a3c54d
  - ev-d2664c436d2ab360
evidence:
- evidence_id: ev-445c3705010cbf61
  kind: record_content
  reference: data/ingredients/mapped/Stachyose_-_70.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1893],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17164","line":1895,"mapping_status":"MAPPED","ontology_id":"CHEBI:17164","preferred_term":"Stachyose
    - 70%"}],"identifier":"CHEBI:17164","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17164","ontology_label":"stachyose","ontology_source":"CHEBI"},"preferred_term":"Stachyose
    - 70%","sssom_rows":[{"data_row":2642,"object_id":"CHEBI:17164","object_label":"stachyose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Stachyose_-_70","synonym_count":1}'
  snapshot_sha256: 1a8a006b5d391e6b72f240c7e38e59491976b19d65f91216620bb2935d4d5605
- evidence_id: ev-734604da326e89f9
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1893]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-fa70562baa8c1154
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Stachyose_-_70; data-row positions=[2642]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2642,"object_id":"CHEBI:17164","object_label":"stachyose","other":"Stachyose
    hydrate|beta-D-fructofuranosyl alpha-D-galactopyranosyl-(1->6)-alpha-D-galactopyranosyl-(1->6)-alpha-D-glucopyranoside|CAS:470-55-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Stachyose_-_70","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-06fe3ebf74ce4e3a
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1895]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:17164","line":1895,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:17164","preferred_term":"Stachyose
    - 70%","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-08c62b91430fe090
  kind: prior_review
  reference: reports/yaml_record_review/Stachyose_-_70.md
  locator: '`data/ingredients/mapped/Stachyose_-_70.yaml`:2; Verdict:4; Identity:10;
    Validation:20; Evidence:29; Completeness:45; Recommended Edits:51'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: b9286c995d770e4be7d0a4ec952a7bc47f55d622f5f1ec74d9bc236f21a2be5e
  quote: "Recommended Edits:\n- Major: re-evaluate whether `Stachyose - 70%` should\
    \ merge into an anhydrous\n  stachyose record as source provenance, become a distinct\
    \ local preparation,\n  or be retired in favor of the hydrate record; then update\
    \ the exact mapping\n  and regenerated SSSOM row accordingly.\n- Major: remove\
    \ `Stachyose hydrate` from this record's exported synonym set so\n  the anhydrous/purity-qualified\
    \ row does not claim its sibling hydrate as a\n  same-subject alias.\n- Major:\
    \ remove `nutritional_roles.CARBON_SOURCE` or replace the provisional\n  carbohydrate-ancestry\
    \ assertion with source evidence that uses this supplied\n  stachyose form as\
    \ a carbon source."
- evidence_id: ev-0319aa4188a3c54d
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1246,1692]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"1a8a006b5d391e6b72f240c7e38e59491976b19d65f91216620bb2935d4d5605","finding_id":"SEM:55c06ddf3067d41c7dd7","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"1a8a006b5d391e6b72f240c7e38e59491976b19d65f91216620bb2935d4d5605","finding_id":"SEM:5c40c4ae1e96d348918d","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-1f0ac1c262dfb4fa
  kind: record_content
  reference: data/ingredients/mapped/Stachyose_-_70.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1893],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17164","line":1895,"mapping_status":"MAPPED","ontology_id":"CHEBI:17164","preferred_term":"Stachyose
    - 70%"}],"identifier":"CHEBI:17164","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17164","ontology_label":"stachyose","ontology_source":"CHEBI"},"preferred_term":"Stachyose
    - 70%","sssom_rows":[{"data_row":2642,"object_id":"CHEBI:17164","object_label":"stachyose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Stachyose_-_70","synonym_count":1}'
  snapshot_sha256: 1a8a006b5d391e6b72f240c7e38e59491976b19d65f91216620bb2935d4d5605
- evidence_id: ev-d2664c436d2ab360
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
  locator: findings[finding_id=f-daed55dde87c7afd]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-daed55dde87c7afd in 20261011T024638Z-mim-reconcile-all-batch-11
  snapshot_sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
assessments:
- assessment_id: a-0d80b55205205e9e
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-bedfc824f9f602aa
  evidence_ids:
  - ev-445c3705010cbf61
  - ev-734604da326e89f9
  - ev-fa70562baa8c1154
  - ev-06fe3ebf74ce4e3a
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-88a14076abdb1c33
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-bedfc824f9f602aa
  evidence_ids:
  - ev-08c62b91430fe090
  - ev-445c3705010cbf61
  - ev-0319aa4188a3c54d
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:23:59Z;
    reviewed SHA-256=1a8a006b5d391e6b72f240c7e38e59491976b19d65f91216620bb2935d4d5605;
    current SHA-256=1a8a006b5d391e6b72f240c7e38e59491976b19d65f91216620bb2935d4d5605;
    hash_changed=False. Reports=["reports/yaml_record_review/Stachyose_-_70.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The 70%
    stachyose row exact-maps a qualified preparation, exports Stachyose hydrate, and
    has a provisional CARBON_SOURCE role.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-08c62b91430fe090
    - ev-445c3705010cbf61
  - name: legacy-native-ids
    value: '["SEM:55c06ddf3067d41c7dd7","SEM:5c40c4ae1e96d348918d"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-445c3705010cbf61
    - ev-08c62b91430fe090
    - ev-0319aa4188a3c54d
- assessment_id: a-1f0ac1c262dfb4fa
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-bedfc824f9f602aa
  evidence_ids:
  - ev-08c62b91430fe090
  - ev-1f0ac1c262dfb4fa
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-08c62b91430fe090
    - ev-1f0ac1c262dfb4fa
findings:
- finding_id: rec-f-daed55dde87c7afd
  issue_key: mim-reconciliation-role-support-bedfc824f9f602aa
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Stachyose - 70%'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-bedfc824f9f602aa
  evidence_ids:
  - ev-08c62b91430fe090
  - ev-1f0ac1c262dfb4fa
  - ev-d2664c436d2ab360
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Stachyose_-_70.yaml
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
    review_id: 20261011T024638Z-mim-reconcile-all-batch-11
    finding_id: f-daed55dde87c7afd
actions:
- action_id: rec-action-daed55dde87c7afd
  description: 'Reassess prediction-only role support: Stachyose - 70%'
  finding_ids:
  - rec-f-daed55dde87c7afd
  target_ids:
  - record-bedfc824f9f602aa
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Stachyose_-_70.yaml
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
