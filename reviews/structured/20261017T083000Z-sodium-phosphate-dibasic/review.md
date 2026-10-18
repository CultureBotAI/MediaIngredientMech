# Per-record structured review: Sodium_Phosphate_Dibasic (data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml)

- Review: 20261017T083000Z-sodium-phosphate-dibasic
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Sodium_Phosphate_Dibasic (data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml, record-9fb851ed17361db8, mapping_status=REJECTED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-9fb851ed17361db8 | data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml | maintained | Sodium_Phosphate_Dibasic |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-9fb851ed17361db8 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-9fb851ed17361db8 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-9fb851ed17361db8 | Reconciled against predecessor batch review 20261011T024629Z-mim-reconcile-all-batch-01 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-9fb851ed17361db8.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-9fb851ed17361db8.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=blocker; reviewed_at=2026-10-01T05:03:30Z; reviewed SHA-256=aabdf39c562aff24b8326456268b4a1e0ac1716934d4d24d428072a8e138e674; current SHA-256=b259959a7e715cd65d01e9d5b3d87af1a0028b694d96abb7d020cef96d366925; hash_changed=True. Reports=["reports/yaml_record_review/20261001T050330Z-Sodium_Phosphate_Dibasic.md","reports/yaml_record_review/Sodium_Phosphate_Dibasic.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Sodium_Phosphate_Dibasic.md&#96; after the record changed from b4e7a80f4f611b0cf35a46f701a382a49ac0b2d706eba3f5714fdeb79e13e955 to aabdf39c562aff24b8326456268b4a1e0ac1716934d4d24d428072a8e138e674; preserved the previous blocker finding floor pending targeted retirement.

### Historical provisional-role concern

evidence: unknown. Targets: record-9fb851ed17361db8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

### Retired wrong mapping / stale tombstone ontology pointer

identity: supported. Targets: record-9fb851ed17361db8.

The narrow exported-mapping/pointer defect is already fixed: REJECTED tombstone, no own-subject SSSOM rows, identifier and ontology_id agree with a live merge target. This does not retire source-count, inert chemistry, role, or synonym questions.

## Findings

### rec-f-2c4572e8aee9ba64: Reassess prediction-only role support: Sodium phosphate dibasic

minor / deferred / provisional; issue key: mim-reconciliation-role-support-9fb851ed17361db8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

Disposition: The current local observation is recorded, but the named source/context or policy decision is still required; no correction is inferred.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-b856f2456e7f1f9f | data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1864],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:34683","line":1866,"mapping_status":"REJECTED","ontology_id":"CHEBI:34683","preferred_term":"Sodium phosphate dibasic"}],"identifier":"CHEBI:34683","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":1154,"edge_count":1154,"occurrences":1157},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:34683","ontology_label":"disodium hydrogenphosphate","ontology_source":"CHEBI"},"preferred_term":"Sodium phosphate dibasic","sssom_rows":[],"sssom_subject":"MIM:Sodium_Phosphate_Dibasic","synonym_count":1} |
| ev-01023f719eb051de | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1864] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-293b21d7d58e152c | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Sodium_Phosphate_Dibasic; data-row positions=[] | context_only | Current exact-subject rows, including complete other payload: [] |
| ev-01edfa5cc0864ed4 | docs/data/mapped_ingredients.csv; CSV lines=[1866] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:34683","line":1866,"mapping_quality":"EXACT_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:34683","preferred_term":"Sodium phosphate dibasic","total_occurrences":"0"}] |
| ev-8bb1def00d80cb77 | reports/yaml_record_review/20261001T050330Z-Sodium_Phosphate_Dibasic.md; YAML Record Review: Sodium phosphate dibasic:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-bbd664bdc2f5534f | reports/yaml_record_review/Sodium_Phosphate_Dibasic.md; &#96;data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml&#96;:2; Verdict:4; Identity:12; Validation:21; Evidence:31; Completeness:49; Recommended Edits:56 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-6fbe21662187ccbb | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1229,1530] | context_only | [{"current_record_sha256":"b259959a7e715cd65d01e9d5b3d87af1a0028b694d96abb7d020cef96d366925","finding_id":"SEM:1c30eea5a9f24672b1e6","kind":"existing_record_review","resolution_reason":"Source record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"},{"current_record_sha256":"b259959a7e715cd65d01e9d5b3d87af1a0028b694d96abb7d020cef96d366925","finding_id":"SEM:51ff456b5478ebfbcd9f","kind":"role_evidence","resolution_reason":"Source record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}] |
| ev-c1c1f0e0056ab927 | data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1864],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:34683","line":1866,"mapping_status":"REJECTED","ontology_id":"CHEBI:34683","preferred_term":"Sodium phosphate dibasic"}],"identifier":"CHEBI:34683","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":1154,"edge_count":1154,"occurrences":1157},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:34683","ontology_label":"disodium hydrogenphosphate","ontology_source":"CHEBI"},"preferred_term":"Sodium phosphate dibasic","sssom_rows":[],"sssom_subject":"MIM:Sodium_Phosphate_Dibasic","synonym_count":1} |
| ev-4f8bdfebcde635f9 | data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml; identifier; ontology_mapping.ontology_id; mapping_status; curation_history | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1864],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:34683","line":1866,"mapping_status":"REJECTED","ontology_id":"CHEBI:34683","preferred_term":"Sodium phosphate dibasic"}],"identifier":"CHEBI:34683","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":1154,"edge_count":1154,"occurrences":1157},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:34683","ontology_label":"disodium hydrogenphosphate","ontology_source":"CHEBI"},"preferred_term":"Sodium phosphate dibasic","sssom_rows":[],"sssom_subject":"MIM:Sodium_Phosphate_Dibasic","synonym_count":1} |
| ev-8c33d45c256f6c4b | reviews/structured/20261011T024629Z-mim-reconcile-all-batch-01/review.yaml; findings[finding_id=f-2c4572e8aee9ba64] | context_only | Predecessor structured review finding f-2c4572e8aee9ba64 in 20261011T024629Z-mim-reconcile-all-batch-01 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024629Z-mim-reconcile-all-batch-01.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-sodium-phosphate-dibasic
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Sodium_Phosphate_Dibasic (data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml)'
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
native_verdict: mapping_status=REJECTED; open=0; deferred=1
scientific_review: false
summary: Per-record structured review for Sodium_Phosphate_Dibasic (data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml,
  record-9fb851ed17361db8, mapping_status=REJECTED). Records 0 open finding(s) and
  1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml
    sha256: b259959a7e715cd65d01e9d5b3d87af1a0028b694d96abb7d020cef96d366925
    role: target
  - path: reviews/structured/20261011T024629Z-mim-reconcile-all-batch-01/review.yaml
    sha256: f87124785da2057286555db743ccdb92b70dd4dc359294bde474b4beeb816e48
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
  - path: reports/yaml_record_review/20261001T050330Z-Sodium_Phosphate_Dibasic.md
    sha256: 6b9cdecbfb5dfa70371c846d5cd63c0c2d81ad69d3692a5b260173152782012c
    role: context
  - path: reports/yaml_record_review/Sodium_Phosphate_Dibasic.md
    sha256: a6a63ac3ab3222655b6eb0a07bcecc503c0c3eeb8fb782f295611a7a1c474038
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-9fb851ed17361db8
  path: data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml
  label: Sodium_Phosphate_Dibasic
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-9fb851ed17361db8
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-9fb851ed17361db8
  evidence_ids:
  - ev-b856f2456e7f1f9f
  - ev-01023f719eb051de
  - ev-293b21d7d58e152c
  - ev-01edfa5cc0864ed4
  - ev-c1c1f0e0056ab927
  - ev-4f8bdfebcde635f9
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-9fb851ed17361db8
  evidence_ids:
  - ev-b856f2456e7f1f9f
  - ev-6fbe21662187ccbb
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024629Z-mim-reconcile-all-batch-01
    and semantic review dispositions on HEAD.
  target_ids:
  - record-9fb851ed17361db8
  evidence_ids:
  - ev-8bb1def00d80cb77
  - ev-bbd664bdc2f5534f
  - ev-6fbe21662187ccbb
  - ev-8c33d45c256f6c4b
evidence:
- evidence_id: ev-b856f2456e7f1f9f
  kind: record_content
  reference: data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1864],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:34683","line":1866,"mapping_status":"REJECTED","ontology_id":"CHEBI:34683","preferred_term":"Sodium
    phosphate dibasic"}],"identifier":"CHEBI:34683","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":1154,"edge_count":1154,"occurrences":1157},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:34683","ontology_label":"disodium
    hydrogenphosphate","ontology_source":"CHEBI"},"preferred_term":"Sodium phosphate
    dibasic","sssom_rows":[],"sssom_subject":"MIM:Sodium_Phosphate_Dibasic","synonym_count":1}'
  snapshot_sha256: b259959a7e715cd65d01e9d5b3d87af1a0028b694d96abb7d020cef96d366925
- evidence_id: ev-01023f719eb051de
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1864]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-293b21d7d58e152c
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Sodium_Phosphate_Dibasic; data-row positions=[]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: []'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-01edfa5cc0864ed4
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1866]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:34683","line":1866,"mapping_quality":"EXACT_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:34683","preferred_term":"Sodium
    phosphate dibasic","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-8bb1def00d80cb77
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050330Z-Sodium_Phosphate_Dibasic.md
  locator: 'YAML Record Review: Sodium phosphate dibasic:2; Target:10; Validation:20;
    Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended
    Edits:56; Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 6b9cdecbfb5dfa70371c846d5cd63c0c2d81ad69d3692a5b260173152782012c
  quote: 'Findings:

    - **blocker**: The previous finding set in `reports/yaml_record_review/Sodium_Phosphate_Dibasic.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: Sodium phosphate
    dibasic is exact-mapped to trisodium phosphate and exports monosodium phosphate
    as a synonym.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Sodium_Phosphate_Dibasic.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml`,
    `just validate-terms data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml` where
    applicable, and `just qc-sssom`.'
- evidence_id: ev-bbd664bdc2f5534f
  kind: prior_review
  reference: reports/yaml_record_review/Sodium_Phosphate_Dibasic.md
  locator: '`data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml`:2; Verdict:4;
    Identity:12; Validation:21; Evidence:31; Completeness:49; Recommended Edits:56'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: a6a63ac3ab3222655b6eb0a07bcecc503c0c3eeb8fb782f295611a7a1c474038
  quote: "Recommended Edits:\n- Blocker: reground `data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml`\
    \ to\n  a disodium phosphate identity, using an exact ontology term if one resolves\n\
    \  and otherwise a CAS or kg-microbe registry identity.\n- Blocker: remove the\
    \ active `Sodium dihydrogen phosphate` synonym and rebuild\n  final SSSOM so `MIM:Sodium_Phosphate_Dibasic`\
    \ stops publishing it in `other`.\n- Major: remove `physicochemical_roles.BUFFER`\
    \ unless a checked source supports\n  the buffer role for the regrounded record."
- evidence_id: ev-6fbe21662187ccbb
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1229,1530]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"b259959a7e715cd65d01e9d5b3d87af1a0028b694d96abb7d020cef96d366925","finding_id":"SEM:1c30eea5a9f24672b1e6","kind":"existing_record_review","resolution_reason":"Source
    record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"},{"current_record_sha256":"b259959a7e715cd65d01e9d5b3d87af1a0028b694d96abb7d020cef96d366925","finding_id":"SEM:51ff456b5478ebfbcd9f","kind":"role_evidence","resolution_reason":"Source
    record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-c1c1f0e0056ab927
  kind: record_content
  reference: data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1864],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:34683","line":1866,"mapping_status":"REJECTED","ontology_id":"CHEBI:34683","preferred_term":"Sodium
    phosphate dibasic"}],"identifier":"CHEBI:34683","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":1154,"edge_count":1154,"occurrences":1157},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:34683","ontology_label":"disodium
    hydrogenphosphate","ontology_source":"CHEBI"},"preferred_term":"Sodium phosphate
    dibasic","sssom_rows":[],"sssom_subject":"MIM:Sodium_Phosphate_Dibasic","synonym_count":1}'
  snapshot_sha256: b259959a7e715cd65d01e9d5b3d87af1a0028b694d96abb7d020cef96d366925
- evidence_id: ev-4f8bdfebcde635f9
  kind: record_content
  reference: data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml
  locator: identifier; ontology_mapping.ontology_id; mapping_status; curation_history
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1864],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:34683","line":1866,"mapping_status":"REJECTED","ontology_id":"CHEBI:34683","preferred_term":"Sodium
    phosphate dibasic"}],"identifier":"CHEBI:34683","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":1154,"edge_count":1154,"occurrences":1157},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:34683","ontology_label":"disodium
    hydrogenphosphate","ontology_source":"CHEBI"},"preferred_term":"Sodium phosphate
    dibasic","sssom_rows":[],"sssom_subject":"MIM:Sodium_Phosphate_Dibasic","synonym_count":1}'
  snapshot_sha256: b259959a7e715cd65d01e9d5b3d87af1a0028b694d96abb7d020cef96d366925
- evidence_id: ev-8c33d45c256f6c4b
  kind: prior_review
  reference: reviews/structured/20261011T024629Z-mim-reconcile-all-batch-01/review.yaml
  locator: findings[finding_id=f-2c4572e8aee9ba64]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-2c4572e8aee9ba64 in 20261011T024629Z-mim-reconcile-all-batch-01
  snapshot_sha256: f87124785da2057286555db743ccdb92b70dd4dc359294bde474b4beeb816e48
assessments:
- assessment_id: a-837a58f198078242
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-9fb851ed17361db8
  evidence_ids:
  - ev-b856f2456e7f1f9f
  - ev-01023f719eb051de
  - ev-293b21d7d58e152c
  - ev-01edfa5cc0864ed4
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-09f54b8a87288e96
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-9fb851ed17361db8
  evidence_ids:
  - ev-8bb1def00d80cb77
  - ev-bbd664bdc2f5534f
  - ev-b856f2456e7f1f9f
  - ev-6fbe21662187ccbb
  details: 'Latest manifest verdict=needs_curation; severity=blocker; reviewed_at=2026-10-01T05:03:30Z;
    reviewed SHA-256=aabdf39c562aff24b8326456268b4a1e0ac1716934d4d24d428072a8e138e674;
    current SHA-256=b259959a7e715cd65d01e9d5b3d87af1a0028b694d96abb7d020cef96d366925;
    hash_changed=True. Reports=["reports/yaml_record_review/20261001T050330Z-Sodium_Phosphate_Dibasic.md","reports/yaml_record_review/Sodium_Phosphate_Dibasic.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Sodium_Phosphate_Dibasic.md` after the record changed
    from b4e7a80f4f611b0cf35a46f701a382a49ac0b2d706eba3f5714fdeb79e13e955 to aabdf39c562aff24b8326456268b4a1e0ac1716934d4d24d428072a8e138e674;
    preserved the previous blocker finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-8bb1def00d80cb77
    - ev-bbd664bdc2f5534f
    - ev-b856f2456e7f1f9f
  - name: legacy-native-ids
    value: '["SEM:1c30eea5a9f24672b1e6","SEM:51ff456b5478ebfbcd9f"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-b856f2456e7f1f9f
    - ev-8bb1def00d80cb77
    - ev-bbd664bdc2f5534f
    - ev-6fbe21662187ccbb
- assessment_id: a-c1c1f0e0056ab927
  area: evidence
  topic: Historical provisional-role concern
  outcome: unknown
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-9fb851ed17361db8
  evidence_ids:
  - ev-8bb1def00d80cb77
  - ev-bbd664bdc2f5534f
  - ev-c1c1f0e0056ab927
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-8bb1def00d80cb77
    - ev-bbd664bdc2f5534f
    - ev-c1c1f0e0056ab927
- assessment_id: a-1fc1ec7f0b8b3261
  area: identity
  topic: Retired wrong mapping / stale tombstone ontology pointer
  outcome: supported
  summary: 'The narrow exported-mapping/pointer defect is already fixed: REJECTED
    tombstone, no own-subject SSSOM rows, identifier and ontology_id agree with a
    live merge target. This does not retire source-count, inert chemistry, role, or
    synonym questions.'
  target_ids:
  - record-9fb851ed17361db8
  evidence_ids:
  - ev-8bb1def00d80cb77
  - ev-bbd664bdc2f5534f
  - ev-4f8bdfebcde635f9
  - ev-b856f2456e7f1f9f
  dimensions:
  - name: legacy-disposition
    value: already_fixed
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-8bb1def00d80cb77
    - ev-bbd664bdc2f5534f
    - ev-4f8bdfebcde635f9
    - ev-b856f2456e7f1f9f
findings:
- finding_id: rec-f-2c4572e8aee9ba64
  issue_key: mim-reconciliation-role-support-9fb851ed17361db8
  category: evidence
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Reassess prediction-only role support: Sodium phosphate dibasic'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-9fb851ed17361db8
  evidence_ids:
  - ev-8bb1def00d80cb77
  - ev-bbd664bdc2f5534f
  - ev-c1c1f0e0056ab927
  - ev-8c33d45c256f6c4b
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_Phosphate_Dibasic.yaml
    role: maintained ingredient
  field_paths:
  - physicochemical_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  disposition_reason: The current local observation is recorded, but the named source/context
    or policy decision is still required; no correction is inferred.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024629Z-mim-reconcile-all-batch-01
    finding_id: f-2c4572e8aee9ba64
actions: []
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
  with lineage to 20261011T024629Z-mim-reconcile-all-batch-01.
```
