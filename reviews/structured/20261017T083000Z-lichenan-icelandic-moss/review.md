# Per-record structured review: Lichenan_Icelandic_Moss (data/ingredients/mapped/Lichenan_Icelandic_Moss.yaml)

- Review: 20261017T083000Z-lichenan-icelandic-moss
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Lichenan_Icelandic_Moss (data/ingredients/mapped/Lichenan_Icelandic_Moss.yaml, record-950c80201ebea6c0, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Lichenan_Icelandic_Moss.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Lichenan_Icelandic_Moss.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-950c80201ebea6c0 | data/ingredients/mapped/Lichenan_Icelandic_Moss.yaml | maintained | Lichenan_Icelandic_Moss |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-950c80201ebea6c0 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-950c80201ebea6c0 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-950c80201ebea6c0 | Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-950c80201ebea6c0.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-950c80201ebea6c0.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T00:20:11Z; reviewed SHA-256=9721a556a6f24eee87da35d9a855d057362cb5c6e867502739939570dca56365; current SHA-256=9721a556a6f24eee87da35d9a855d057362cb5c6e867502739939570dca56365; hash_changed=False. Reports=["reports/yaml_record_review/Lichenan_Icelandic_Moss.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local identity, narrower CHEBI:6452 parent mapping, CAS payload, registry sibling rows, and final SSSOM predicates pass, but CARBON_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-950c80201ebea6c0.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-55118ec7b2e2ed90: Reassess prediction-only role support: Lichenan (icelandic moss)

major / open / confirmed; issue key: mim-reconciliation-role-support-950c80201ebea6c0.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-55118ec7b2e2ed90

Reassess prediction-only role support: Lichenan (icelandic moss)

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-f66905bc10c1093b | data/ingredients/mapped/Lichenan_Icelandic_Moss.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1300],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:lichenan_icelandic_moss","line":1302,"mapping_status":"MAPPED","ontology_id":"CHEBI:6452","preferred_term":"Lichenan (icelandic moss)"}],"identifier":"kgmicrobe.ingredient:lichenan_icelandic_moss","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:6452","ontology_label":"lichenin","ontology_source":"CHEBI"},"preferred_term":"Lichenan (icelandic moss)","sssom_rows":[{"data_row":1690,"object_id":"CHEBI:6452","object_label":"lichenin","predicate_id":"skos:broadMatch"},{"data_row":1691,"object_id":"kgmicrobe.ingredient:lichenan_icelandic_moss","object_label":"Lichenan (icelandic moss)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Lichenan_Icelandic_Moss","synonym_count":0} |
| ev-ed9cfc5327a09ad0 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1300] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-0300501341c3703b | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Lichenan_Icelandic_Moss; data-row positions=[1690, 1691] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1690,"object_id":"CHEBI:6452","object_label":"lichenin","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Lichenan_Icelandic_Moss","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":1691,"object_id":"kgmicrobe.ingredient:lichenan_icelandic_moss","object_label":"Lichenan (icelandic moss)","other":"CAS:1402-10-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Lichenan_Icelandic_Moss","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-09-02"}] |
| ev-c7c8be8bcc24ed3b | docs/data/mapped_ingredients.csv; CSV lines=[1302] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:lichenan_icelandic_moss","line":1302,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:6452","preferred_term":"Lichenan (icelandic moss)","total_occurrences":"0"}] |
| ev-87b283718a35c330 | reports/yaml_record_review/Lichenan_Icelandic_Moss.md; &#96;data/ingredients/mapped/Lichenan_Icelandic_Moss.yaml&#96;:2; Verdict:4; Identity:11; Validation:20; Evidence:28; Completeness:49; Recommended Edits:56 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-81d4e64211bfa3a0 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[861,1717] | context_only | [{"current_record_sha256":"9721a556a6f24eee87da35d9a855d057362cb5c6e867502739939570dca56365","finding_id":"SEM:fa94d23d0cf1f1c393c3","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"9721a556a6f24eee87da35d9a855d057362cb5c6e867502739939570dca56365","finding_id":"SEM:bef629fe13f78ada8b84","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-0b9b4e31049c3131 | data/ingredients/mapped/Lichenan_Icelandic_Moss.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1300],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:lichenan_icelandic_moss","line":1302,"mapping_status":"MAPPED","ontology_id":"CHEBI:6452","preferred_term":"Lichenan (icelandic moss)"}],"identifier":"kgmicrobe.ingredient:lichenan_icelandic_moss","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:6452","ontology_label":"lichenin","ontology_source":"CHEBI"},"preferred_term":"Lichenan (icelandic moss)","sssom_rows":[{"data_row":1690,"object_id":"CHEBI:6452","object_label":"lichenin","predicate_id":"skos:broadMatch"},{"data_row":1691,"object_id":"kgmicrobe.ingredient:lichenan_icelandic_moss","object_label":"Lichenan (icelandic moss)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Lichenan_Icelandic_Moss","synonym_count":0} |
| ev-f2416a41cf77f29a | reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml; findings[finding_id=f-55118ec7b2e2ed90] | context_only | Predecessor structured review finding f-55118ec7b2e2ed90 in 20261011T024636Z-mim-reconcile-all-batch-08 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-lichenan-icelandic-moss
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Lichenan_Icelandic_Moss (data/ingredients/mapped/Lichenan_Icelandic_Moss.yaml)'
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
summary: Per-record structured review for Lichenan_Icelandic_Moss (data/ingredients/mapped/Lichenan_Icelandic_Moss.yaml,
  record-950c80201ebea6c0, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Lichenan_Icelandic_Moss.yaml
    sha256: 9721a556a6f24eee87da35d9a855d057362cb5c6e867502739939570dca56365
    role: target
  - path: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
    sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
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
  - path: reports/yaml_record_review/Lichenan_Icelandic_Moss.md
    sha256: 125db95a129832acc6c2d896283f78a5723c274f9b1f390cb2518bdddb53d4be
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-950c80201ebea6c0
  path: data/ingredients/mapped/Lichenan_Icelandic_Moss.yaml
  label: Lichenan_Icelandic_Moss
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Lichenan_Icelandic_Moss.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Lichenan_Icelandic_Moss.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Lichenan_Icelandic_Moss.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-950c80201ebea6c0
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-950c80201ebea6c0
  evidence_ids:
  - ev-f66905bc10c1093b
  - ev-ed9cfc5327a09ad0
  - ev-0300501341c3703b
  - ev-c7c8be8bcc24ed3b
  - ev-0b9b4e31049c3131
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-950c80201ebea6c0
  evidence_ids:
  - ev-f66905bc10c1093b
  - ev-81d4e64211bfa3a0
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08
    and semantic review dispositions on HEAD.
  target_ids:
  - record-950c80201ebea6c0
  evidence_ids:
  - ev-87b283718a35c330
  - ev-81d4e64211bfa3a0
  - ev-f2416a41cf77f29a
evidence:
- evidence_id: ev-f66905bc10c1093b
  kind: record_content
  reference: data/ingredients/mapped/Lichenan_Icelandic_Moss.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1300],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:lichenan_icelandic_moss","line":1302,"mapping_status":"MAPPED","ontology_id":"CHEBI:6452","preferred_term":"Lichenan
    (icelandic moss)"}],"identifier":"kgmicrobe.ingredient:lichenan_icelandic_moss","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:6452","ontology_label":"lichenin","ontology_source":"CHEBI"},"preferred_term":"Lichenan
    (icelandic moss)","sssom_rows":[{"data_row":1690,"object_id":"CHEBI:6452","object_label":"lichenin","predicate_id":"skos:broadMatch"},{"data_row":1691,"object_id":"kgmicrobe.ingredient:lichenan_icelandic_moss","object_label":"Lichenan
    (icelandic moss)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Lichenan_Icelandic_Moss","synonym_count":0}'
  snapshot_sha256: 9721a556a6f24eee87da35d9a855d057362cb5c6e867502739939570dca56365
- evidence_id: ev-ed9cfc5327a09ad0
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1300]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-0300501341c3703b
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Lichenan_Icelandic_Moss; data-row positions=[1690, 1691]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1690,"object_id":"CHEBI:6452","object_label":"lichenin","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Lichenan_Icelandic_Moss","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":1691,"object_id":"kgmicrobe.ingredient:lichenan_icelandic_moss","object_label":"Lichenan
    (icelandic moss)","other":"CAS:1402-10-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Lichenan_Icelandic_Moss","validation_method":"none|UNKNOWN_TERM|2026-09-02"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-c7c8be8bcc24ed3b
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1302]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:lichenan_icelandic_moss","line":1302,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:6452","preferred_term":"Lichenan
    (icelandic moss)","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-87b283718a35c330
  kind: prior_review
  reference: reports/yaml_record_review/Lichenan_Icelandic_Moss.md
  locator: '`data/ingredients/mapped/Lichenan_Icelandic_Moss.yaml`:2; Verdict:4; Identity:11;
    Validation:20; Evidence:28; Completeness:49; Recommended Edits:56'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 125db95a129832acc6c2d896283f78a5723c274f9b1f390cb2518bdddb53d4be
  quote: "Recommended Edits:\n- Major: either replace `nutritional_roles.CARBON_SOURCE`\
    \ in\n  `data/ingredients/mapped/Lichenan_Icelandic_Moss.yaml` with inspected\
    \ source\n  evidence for exact lichenan from Icelandic moss use, or remove the\
    \ provisional\n  role.\n- Sync the aggregate copy and regenerate final SSSOM after\
    \ the YAML change;\n  rerun strict, term, round-trip, component, and SSSOM validation."
- evidence_id: ev-81d4e64211bfa3a0
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[861,1717]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"9721a556a6f24eee87da35d9a855d057362cb5c6e867502739939570dca56365","finding_id":"SEM:fa94d23d0cf1f1c393c3","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"9721a556a6f24eee87da35d9a855d057362cb5c6e867502739939570dca56365","finding_id":"SEM:bef629fe13f78ada8b84","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-0b9b4e31049c3131
  kind: record_content
  reference: data/ingredients/mapped/Lichenan_Icelandic_Moss.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1300],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:lichenan_icelandic_moss","line":1302,"mapping_status":"MAPPED","ontology_id":"CHEBI:6452","preferred_term":"Lichenan
    (icelandic moss)"}],"identifier":"kgmicrobe.ingredient:lichenan_icelandic_moss","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:6452","ontology_label":"lichenin","ontology_source":"CHEBI"},"preferred_term":"Lichenan
    (icelandic moss)","sssom_rows":[{"data_row":1690,"object_id":"CHEBI:6452","object_label":"lichenin","predicate_id":"skos:broadMatch"},{"data_row":1691,"object_id":"kgmicrobe.ingredient:lichenan_icelandic_moss","object_label":"Lichenan
    (icelandic moss)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Lichenan_Icelandic_Moss","synonym_count":0}'
  snapshot_sha256: 9721a556a6f24eee87da35d9a855d057362cb5c6e867502739939570dca56365
- evidence_id: ev-f2416a41cf77f29a
  kind: prior_review
  reference: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
  locator: findings[finding_id=f-55118ec7b2e2ed90]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-55118ec7b2e2ed90 in 20261011T024636Z-mim-reconcile-all-batch-08
  snapshot_sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
assessments:
- assessment_id: a-a3a9a5aa0c05ae1f
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-950c80201ebea6c0
  evidence_ids:
  - ev-f66905bc10c1093b
  - ev-ed9cfc5327a09ad0
  - ev-0300501341c3703b
  - ev-c7c8be8bcc24ed3b
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-f4d3c359e90eb2a1
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-950c80201ebea6c0
  evidence_ids:
  - ev-87b283718a35c330
  - ev-f66905bc10c1093b
  - ev-81d4e64211bfa3a0
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T00:20:11Z;
    reviewed SHA-256=9721a556a6f24eee87da35d9a855d057362cb5c6e867502739939570dca56365;
    current SHA-256=9721a556a6f24eee87da35d9a855d057362cb5c6e867502739939570dca56365;
    hash_changed=False. Reports=["reports/yaml_record_review/Lichenan_Icelandic_Moss.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    identity, narrower CHEBI:6452 parent mapping, CAS payload, registry sibling rows,
    and final SSSOM predicates pass, but CARBON_SOURCE is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-87b283718a35c330
    - ev-f66905bc10c1093b
  - name: legacy-native-ids
    value: '["SEM:fa94d23d0cf1f1c393c3","SEM:bef629fe13f78ada8b84"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-f66905bc10c1093b
    - ev-87b283718a35c330
    - ev-81d4e64211bfa3a0
- assessment_id: a-0b9b4e31049c3131
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-950c80201ebea6c0
  evidence_ids:
  - ev-87b283718a35c330
  - ev-0b9b4e31049c3131
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-87b283718a35c330
    - ev-0b9b4e31049c3131
findings:
- finding_id: rec-f-55118ec7b2e2ed90
  issue_key: mim-reconciliation-role-support-950c80201ebea6c0
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Lichenan (icelandic moss)'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-950c80201ebea6c0
  evidence_ids:
  - ev-87b283718a35c330
  - ev-0b9b4e31049c3131
  - ev-f2416a41cf77f29a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Lichenan_Icelandic_Moss.yaml
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
    review_id: 20261011T024636Z-mim-reconcile-all-batch-08
    finding_id: f-55118ec7b2e2ed90
actions:
- action_id: rec-action-55118ec7b2e2ed90
  description: 'Reassess prediction-only role support: Lichenan (icelandic moss)'
  finding_ids:
  - rec-f-55118ec7b2e2ed90
  target_ids:
  - record-950c80201ebea6c0
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Lichenan_Icelandic_Moss.yaml
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
  with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.
```
