# Per-record structured review: Citrate (data/ingredients/mapped/Citrate.yaml)

- Review: 20261017T083000Z-citrate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Citrate (data/ingredients/mapped/Citrate.yaml, record-ee4821995ba147ea, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Citrate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Citrate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-ee4821995ba147ea | data/ingredients/mapped/Citrate.yaml | maintained | Citrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-ee4821995ba147ea | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-ee4821995ba147ea | Role assertions on nutritional_roles[0], nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-ee4821995ba147ea | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-ee4821995ba147ea.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-ee4821995ba147ea.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:01:53Z; reviewed SHA-256=3ad648773ab7cbfa86dba35c90471717003af85124f3357c995a5ce911f79668; current SHA-256=3ad648773ab7cbfa86dba35c90471717003af85124f3357c995a5ce911f79668; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050153Z-Citrate.md","reports/yaml_record_review/Citrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Citrate.md&#96; after the record changed from 3612a56f36e94fee4fe773bcfc7fcb09598032746de68d4a67e8fec6d6bb6ce5 to 3ad648773ab7cbfa86dba35c90471717003af85124f3357c995a5ce911f79668; preserved the previous major finding floor pending targeted retirement.

### Historical provisional-role concern

evidence: concern. Targets: record-ee4821995ba147ea.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-9f67575cf91c9348: Reassess prediction-only role support: Citrate

major / open / confirmed; issue key: mim-reconciliation-role-support-ee4821995ba147ea.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-9f67575cf91c9348

Reassess prediction-only role support: Citrate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-b197e22fd8f4d6f3 | data/ingredients/mapped/Citrate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[730],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16947","line":732,"mapping_status":"MAPPED","ontology_id":"CHEBI:16947","preferred_term":"Citrate"}],"identifier":"CHEBI:16947","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":63,"edge_count":63,"occurrences":63},"occurrence_statistics":{"media_count":63,"total_occurrences":63},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:16947","ontology_label":"citrate(3-)","ontology_source":"CHEBI"},"preferred_term":"Citrate","sssom_rows":[{"data_row":778,"object_id":"CHEBI:16947","object_label":"citrate(3-)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Citrate","synonym_count":2} |
| ev-0eb2ac0de047b5a9 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [730] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-ae2fa01d873e333a | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Citrate; data-row positions=[778] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":778,"object_id":"CHEBI:16947","object_label":"citrate(3-)","other":"2-hydroxypropane-1,2,3-tricarboxylate","predicate_id":"skos:exactMatch","subject_id":"MIM:Citrate","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-f103ed5338a17ec3 | docs/data/mapped_ingredients.csv; CSV lines=[732] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:16947","line":732,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"63","ontology_id":"CHEBI:16947","preferred_term":"Citrate","total_occurrences":"63"}] |
| ev-32aaa1f5b75f527f | reports/yaml_record_review/20261001T050153Z-Citrate.md; YAML Record Review: Citrate:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-7ed86050cb533a3f | reports/yaml_record_review/Citrate.md; &#96;data/ingredients/mapped/Citrate.yaml&#96;:2; Verdict:4; Identity:13; Validation:26; Evidence:43; Completeness:64; Recommended Edits:71 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-c505992cd33fd286 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[419,1490,1749] | context_only | [{"current_record_sha256":"3ad648773ab7cbfa86dba35c90471717003af85124f3357c995a5ce911f79668","finding_id":"SEM:d299e0d6b2b76b242db3","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"3ad648773ab7cbfa86dba35c90471717003af85124f3357c995a5ce911f79668","finding_id":"SEM:dd755c4edb0c57753524","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"3ad648773ab7cbfa86dba35c90471717003af85124f3357c995a5ce911f79668","finding_id":"SEM:e614338d0c5c25a74610","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-155b48346db64d4f | data/ingredients/mapped/Citrate.yaml; nutritional_roles[0], nutritional_roles[1] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[730],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16947","line":732,"mapping_status":"MAPPED","ontology_id":"CHEBI:16947","preferred_term":"Citrate"}],"identifier":"CHEBI:16947","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":63,"edge_count":63,"occurrences":63},"occurrence_statistics":{"media_count":63,"total_occurrences":63},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:16947","ontology_label":"citrate(3-)","ontology_source":"CHEBI"},"preferred_term":"Citrate","sssom_rows":[{"data_row":778,"object_id":"CHEBI:16947","object_label":"citrate(3-)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Citrate","synonym_count":2} |
| ev-07878006b249d557 | reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml; findings[finding_id=f-9f67575cf91c9348] | context_only | Predecessor structured review finding f-9f67575cf91c9348 in 20261011T024632Z-mim-reconcile-all-batch-04 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-citrate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Citrate (data/ingredients/mapped/Citrate.yaml)'
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
summary: Per-record structured review for Citrate (data/ingredients/mapped/Citrate.yaml,
  record-ee4821995ba147ea, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Citrate.yaml
    sha256: 3ad648773ab7cbfa86dba35c90471717003af85124f3357c995a5ce911f79668
    role: target
  - path: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
    sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
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
  - path: reports/yaml_record_review/20261001T050153Z-Citrate.md
    sha256: fc0d1baa0b008fc271f2e64f13480c3919b83fd35663701a2412a009920a7458
    role: context
  - path: reports/yaml_record_review/Citrate.md
    sha256: 2268fa3cef8c67d45b5c1384703d23b1baacde02438431e189e7844ee11a24cf
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-ee4821995ba147ea
  path: data/ingredients/mapped/Citrate.yaml
  label: Citrate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Citrate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Citrate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Citrate.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-ee4821995ba147ea
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-ee4821995ba147ea
  evidence_ids:
  - ev-b197e22fd8f4d6f3
  - ev-0eb2ac0de047b5a9
  - ev-ae2fa01d873e333a
  - ev-f103ed5338a17ec3
  - ev-155b48346db64d4f
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0], nutritional_roles[1] rely only
    on COMPUTATIONAL_PREDICTION or empty evidence.
  target_ids:
  - record-ee4821995ba147ea
  evidence_ids:
  - ev-b197e22fd8f4d6f3
  - ev-c505992cd33fd286
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-ee4821995ba147ea
  evidence_ids:
  - ev-32aaa1f5b75f527f
  - ev-7ed86050cb533a3f
  - ev-c505992cd33fd286
  - ev-07878006b249d557
evidence:
- evidence_id: ev-b197e22fd8f4d6f3
  kind: record_content
  reference: data/ingredients/mapped/Citrate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[730],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16947","line":732,"mapping_status":"MAPPED","ontology_id":"CHEBI:16947","preferred_term":"Citrate"}],"identifier":"CHEBI:16947","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":63,"edge_count":63,"occurrences":63},"occurrence_statistics":{"media_count":63,"total_occurrences":63},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:16947","ontology_label":"citrate(3-)","ontology_source":"CHEBI"},"preferred_term":"Citrate","sssom_rows":[{"data_row":778,"object_id":"CHEBI:16947","object_label":"citrate(3-)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Citrate","synonym_count":2}'
  snapshot_sha256: 3ad648773ab7cbfa86dba35c90471717003af85124f3357c995a5ce911f79668
- evidence_id: ev-0eb2ac0de047b5a9
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [730]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-ae2fa01d873e333a
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Citrate; data-row positions=[778]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":778,"object_id":"CHEBI:16947","object_label":"citrate(3-)","other":"2-hydroxypropane-1,2,3-tricarboxylate","predicate_id":"skos:exactMatch","subject_id":"MIM:Citrate","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-f103ed5338a17ec3
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[732]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:16947","line":732,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"63","ontology_id":"CHEBI:16947","preferred_term":"Citrate","total_occurrences":"63"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-32aaa1f5b75f527f
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050153Z-Citrate.md
  locator: 'YAML Record Review: Citrate:2; Target:10; Validation:20; Identity and
    Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: fc0d1baa0b008fc271f2e64f13480c3919b83fd35663701a2412a009920a7458
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/Citrate.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The CHEBI
    citrate(3-) identity and 63/63 count pass, but the final SSSOM publishes a trait
    phrase and the nutritional roles are only computationally supported.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Citrate.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Citrate.yaml`,
    `just validate-terms data/ingredients/mapped/Citrate.yaml` where applicable, and
    `just qc-sssom`.'
- evidence_id: ev-7ed86050cb533a3f
  kind: prior_review
  reference: reports/yaml_record_review/Citrate.md
  locator: '`data/ingredients/mapped/Citrate.yaml`:2; Verdict:4; Identity:13; Validation:26;
    Evidence:43; Completeness:64; Recommended Edits:71'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 2268fa3cef8c67d45b5c1384703d23b1baacde02438431e189e7844ee11a24cf
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Citrate.yaml`,\
    \ remove or retype\n  `assimilation: citrate` so it remains provenance only and\
    \ no longer reaches\n  `mappings/ingredient_mappings.sssom.tsv` or label-search\
    \ exports.\n- Major: either attach source evidence to `CARBON_SOURCE` and `ENERGY_SOURCE`\n\
    \  or remove the provisional role facets.\n- After the YAML edits, regenerate\
    \ the curated aggregate, final SSSOM, and docs\n  products, then rerun strict\
    \ validation and the SSSOM invariant checks."
- evidence_id: ev-c505992cd33fd286
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[419,1490,1749]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"3ad648773ab7cbfa86dba35c90471717003af85124f3357c995a5ce911f79668","finding_id":"SEM:d299e0d6b2b76b242db3","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"3ad648773ab7cbfa86dba35c90471717003af85124f3357c995a5ce911f79668","finding_id":"SEM:dd755c4edb0c57753524","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"3ad648773ab7cbfa86dba35c90471717003af85124f3357c995a5ce911f79668","finding_id":"SEM:e614338d0c5c25a74610","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-155b48346db64d4f
  kind: record_content
  reference: data/ingredients/mapped/Citrate.yaml
  locator: nutritional_roles[0], nutritional_roles[1]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[730],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16947","line":732,"mapping_status":"MAPPED","ontology_id":"CHEBI:16947","preferred_term":"Citrate"}],"identifier":"CHEBI:16947","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":63,"edge_count":63,"occurrences":63},"occurrence_statistics":{"media_count":63,"total_occurrences":63},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:16947","ontology_label":"citrate(3-)","ontology_source":"CHEBI"},"preferred_term":"Citrate","sssom_rows":[{"data_row":778,"object_id":"CHEBI:16947","object_label":"citrate(3-)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Citrate","synonym_count":2}'
  snapshot_sha256: 3ad648773ab7cbfa86dba35c90471717003af85124f3357c995a5ce911f79668
- evidence_id: ev-07878006b249d557
  kind: prior_review
  reference: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
  locator: findings[finding_id=f-9f67575cf91c9348]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-9f67575cf91c9348 in 20261011T024632Z-mim-reconcile-all-batch-04
  snapshot_sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
assessments:
- assessment_id: a-d9ffb441b3375e80
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-ee4821995ba147ea
  evidence_ids:
  - ev-b197e22fd8f4d6f3
  - ev-0eb2ac0de047b5a9
  - ev-ae2fa01d873e333a
  - ev-f103ed5338a17ec3
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-2da1bd13a72d6910
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-ee4821995ba147ea
  evidence_ids:
  - ev-32aaa1f5b75f527f
  - ev-7ed86050cb533a3f
  - ev-b197e22fd8f4d6f3
  - ev-c505992cd33fd286
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:01:53Z;
    reviewed SHA-256=3ad648773ab7cbfa86dba35c90471717003af85124f3357c995a5ce911f79668;
    current SHA-256=3ad648773ab7cbfa86dba35c90471717003af85124f3357c995a5ce911f79668;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050153Z-Citrate.md","reports/yaml_record_review/Citrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Citrate.md` after the record changed from 3612a56f36e94fee4fe773bcfc7fcb09598032746de68d4a67e8fec6d6bb6ce5
    to 3ad648773ab7cbfa86dba35c90471717003af85124f3357c995a5ce911f79668; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-32aaa1f5b75f527f
    - ev-7ed86050cb533a3f
    - ev-b197e22fd8f4d6f3
  - name: legacy-native-ids
    value: '["SEM:d299e0d6b2b76b242db3","SEM:dd755c4edb0c57753524","SEM:e614338d0c5c25a74610"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-b197e22fd8f4d6f3
    - ev-32aaa1f5b75f527f
    - ev-7ed86050cb533a3f
    - ev-c505992cd33fd286
- assessment_id: a-155b48346db64d4f
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-ee4821995ba147ea
  evidence_ids:
  - ev-32aaa1f5b75f527f
  - ev-7ed86050cb533a3f
  - ev-155b48346db64d4f
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-32aaa1f5b75f527f
    - ev-7ed86050cb533a3f
    - ev-155b48346db64d4f
findings:
- finding_id: rec-f-9f67575cf91c9348
  issue_key: mim-reconciliation-role-support-ee4821995ba147ea
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Citrate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-ee4821995ba147ea
  evidence_ids:
  - ev-32aaa1f5b75f527f
  - ev-7ed86050cb533a3f
  - ev-155b48346db64d4f
  - ev-07878006b249d557
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Citrate.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  - nutritional_roles[1]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024632Z-mim-reconcile-all-batch-04
    finding_id: f-9f67575cf91c9348
actions:
- action_id: rec-action-9f67575cf91c9348
  description: 'Reassess prediction-only role support: Citrate'
  finding_ids:
  - rec-f-9f67575cf91c9348
  target_ids:
  - record-ee4821995ba147ea
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Citrate.yaml
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
  with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.
```
