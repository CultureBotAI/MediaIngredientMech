# Per-record structured review: D-_-lyxose (data/ingredients/mapped/D-_-lyxose.yaml)

- Review: 20261017T083000Z-d-lyxose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for D-_-lyxose (data/ingredients/mapped/D-_-lyxose.yaml, record-26db4b94c97aabed, mapping_status=REJECTED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/D-_-lyxose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/D-_-lyxose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-26db4b94c97aabed | data/ingredients/mapped/D-_-lyxose.yaml | maintained | D-_-lyxose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-26db4b94c97aabed | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-26db4b94c97aabed | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-26db4b94c97aabed | Reconciled against predecessor batch review 20261011T024629Z-mim-reconcile-all-batch-01 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-26db4b94c97aabed.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-26db4b94c97aabed.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T13:23:22Z; reviewed SHA-256=39b02cd43bdadb3fb76b6e05e83da0e1595572741fae2f4d3e6af59a050fc701; current SHA-256=90de548740ec18dec54e38cf165e804a1353547bd1e2c7ce0c5a131bcd7ef14a; hash_changed=True. Reports=["reports/yaml_record_review/D-_-lyxose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The rejected aldehydo tombstone correctly drops final SSSOM and points at D-lyxose, but inert stale chemistry/role data and an unreviewed cross-record baseline row remain.

### Historical provisional-role concern

evidence: unknown. Targets: record-26db4b94c97aabed.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

### Retired wrong mapping / stale tombstone ontology pointer

identity: supported. Targets: record-26db4b94c97aabed.

The narrow exported-mapping/pointer defect is already fixed: REJECTED tombstone, no own-subject SSSOM rows, identifier and ontology_id agree with a live merge target. This does not retire source-count, inert chemistry, role, or synonym questions.

## Findings

### rec-f-021e3723b7ad50fd: Reassess prediction-only role support: D-(-)-lyxose

minor / deferred / provisional; issue key: mim-reconciliation-role-support-26db4b94c97aabed.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

Disposition: The current local observation is recorded, but the named source/context or policy decision is still required; no correction is inferred.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-cf95a68be557e18a | data/ingredients/mapped/D-_-lyxose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[802],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:62318","line":804,"mapping_status":"REJECTED","ontology_id":"CHEBI:62318","preferred_term":"D-(-)-lyxose"}],"identifier":"CHEBI:62318","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:62318","ontology_label":"D-lyxose","ontology_source":"CHEBI"},"preferred_term":"D-(-)-lyxose","sssom_rows":[],"sssom_subject":"MIM:D-_-lyxose","synonym_count":2} |
| ev-fc5ac5e405c631db | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [802] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-b172a2d697478a64 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:D-_-lyxose; data-row positions=[] | context_only | Current exact-subject rows, including complete other payload: [] |
| ev-2f0bca96872dd59c | docs/data/mapped_ingredients.csv; CSV lines=[804] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:62318","line":804,"mapping_quality":"SYNONYM_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:62318","preferred_term":"D-(-)-lyxose","total_occurrences":"0"}] |
| ev-ba0a155c673a7661 | reports/yaml_record_review/D-_-lyxose.md; &#96;data/ingredients/mapped/D-_-lyxose.yaml&#96;:2; Verdict:4; Identity:13; Validation:29; Evidence:48; Completeness:62; Recommended Edits:73 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-fc73952a5dc8d42e | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[482] | context_only | [{"current_record_sha256":"90de548740ec18dec54e38cf165e804a1353547bd1e2c7ce0c5a131bcd7ef14a","finding_id":"SEM:3cd7092c7ec9685ec9af","kind":"existing_record_review","resolution_reason":"Source record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}] |
| ev-a15bffce40ab7317 | data/ingredients/mapped/D-_-lyxose.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[802],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:62318","line":804,"mapping_status":"REJECTED","ontology_id":"CHEBI:62318","preferred_term":"D-(-)-lyxose"}],"identifier":"CHEBI:62318","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:62318","ontology_label":"D-lyxose","ontology_source":"CHEBI"},"preferred_term":"D-(-)-lyxose","sssom_rows":[],"sssom_subject":"MIM:D-_-lyxose","synonym_count":2} |
| ev-09c57710cd75f921 | data/ingredients/mapped/D-_-lyxose.yaml; identifier; ontology_mapping.ontology_id; mapping_status; curation_history | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[802],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:62318","line":804,"mapping_status":"REJECTED","ontology_id":"CHEBI:62318","preferred_term":"D-(-)-lyxose"}],"identifier":"CHEBI:62318","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:62318","ontology_label":"D-lyxose","ontology_source":"CHEBI"},"preferred_term":"D-(-)-lyxose","sssom_rows":[],"sssom_subject":"MIM:D-_-lyxose","synonym_count":2} |
| ev-034279f78ffb83be | reviews/structured/20261011T024629Z-mim-reconcile-all-batch-01/review.yaml; findings[finding_id=f-021e3723b7ad50fd] | context_only | Predecessor structured review finding f-021e3723b7ad50fd in 20261011T024629Z-mim-reconcile-all-batch-01 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024629Z-mim-reconcile-all-batch-01.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-d-lyxose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: D-_-lyxose (data/ingredients/mapped/D-_-lyxose.yaml)'
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
summary: Per-record structured review for D-_-lyxose (data/ingredients/mapped/D-_-lyxose.yaml,
  record-26db4b94c97aabed, mapping_status=REJECTED). Records 0 open finding(s) and
  1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/D-_-lyxose.yaml
    sha256: 90de548740ec18dec54e38cf165e804a1353547bd1e2c7ce0c5a131bcd7ef14a
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
  - path: reports/yaml_record_review/D-_-lyxose.md
    sha256: be0aad62a395320d83cb55ddee3145de547bc40b9af286089b075d97110644b7
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-26db4b94c97aabed
  path: data/ingredients/mapped/D-_-lyxose.yaml
  label: D-_-lyxose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-_-lyxose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/D-_-lyxose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/D-_-lyxose.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-26db4b94c97aabed
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-26db4b94c97aabed
  evidence_ids:
  - ev-cf95a68be557e18a
  - ev-fc5ac5e405c631db
  - ev-b172a2d697478a64
  - ev-2f0bca96872dd59c
  - ev-a15bffce40ab7317
  - ev-09c57710cd75f921
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-26db4b94c97aabed
  evidence_ids:
  - ev-cf95a68be557e18a
  - ev-fc73952a5dc8d42e
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024629Z-mim-reconcile-all-batch-01
    and semantic review dispositions on HEAD.
  target_ids:
  - record-26db4b94c97aabed
  evidence_ids:
  - ev-ba0a155c673a7661
  - ev-fc73952a5dc8d42e
  - ev-034279f78ffb83be
evidence:
- evidence_id: ev-cf95a68be557e18a
  kind: record_content
  reference: data/ingredients/mapped/D-_-lyxose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[802],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:62318","line":804,"mapping_status":"REJECTED","ontology_id":"CHEBI:62318","preferred_term":"D-(-)-lyxose"}],"identifier":"CHEBI:62318","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:62318","ontology_label":"D-lyxose","ontology_source":"CHEBI"},"preferred_term":"D-(-)-lyxose","sssom_rows":[],"sssom_subject":"MIM:D-_-lyxose","synonym_count":2}'
  snapshot_sha256: 90de548740ec18dec54e38cf165e804a1353547bd1e2c7ce0c5a131bcd7ef14a
- evidence_id: ev-fc5ac5e405c631db
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [802]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-b172a2d697478a64
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:D-_-lyxose; data-row positions=[]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: []'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-2f0bca96872dd59c
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[804]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:62318","line":804,"mapping_quality":"SYNONYM_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:62318","preferred_term":"D-(-)-lyxose","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-ba0a155c673a7661
  kind: prior_review
  reference: reports/yaml_record_review/D-_-lyxose.md
  locator: '`data/ingredients/mapped/D-_-lyxose.yaml`:2; Verdict:4; Identity:13; Validation:29;
    Evidence:48; Completeness:62; Recommended Edits:73'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: be0aad62a395320d83cb55ddee3145de547bc40b9af286089b075d97110644b7
  quote: "Recommended Edits:\n- Optionally refresh `mappings/other_cross_record_baseline.tsv`\
    \ so the\n  `MIM:~282~29-D-lyxose` to `MIM:D-_-lyxose` duplicate is no longer\n\
    \  `UNREVIEWED`, and prune stale chemistry/role fields from the rejected\n  tombstone\
    \ if tombstones are no longer expected to retain inert pre-merge\n  facts. No\
    \ final SSSOM row change is required for this tombstone."
- evidence_id: ev-fc73952a5dc8d42e
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[482]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"90de548740ec18dec54e38cf165e804a1353547bd1e2c7ce0c5a131bcd7ef14a","finding_id":"SEM:3cd7092c7ec9685ec9af","kind":"existing_record_review","resolution_reason":"Source
    record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-a15bffce40ab7317
  kind: record_content
  reference: data/ingredients/mapped/D-_-lyxose.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[802],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:62318","line":804,"mapping_status":"REJECTED","ontology_id":"CHEBI:62318","preferred_term":"D-(-)-lyxose"}],"identifier":"CHEBI:62318","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:62318","ontology_label":"D-lyxose","ontology_source":"CHEBI"},"preferred_term":"D-(-)-lyxose","sssom_rows":[],"sssom_subject":"MIM:D-_-lyxose","synonym_count":2}'
  snapshot_sha256: 90de548740ec18dec54e38cf165e804a1353547bd1e2c7ce0c5a131bcd7ef14a
- evidence_id: ev-09c57710cd75f921
  kind: record_content
  reference: data/ingredients/mapped/D-_-lyxose.yaml
  locator: identifier; ontology_mapping.ontology_id; mapping_status; curation_history
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[802],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:62318","line":804,"mapping_status":"REJECTED","ontology_id":"CHEBI:62318","preferred_term":"D-(-)-lyxose"}],"identifier":"CHEBI:62318","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:62318","ontology_label":"D-lyxose","ontology_source":"CHEBI"},"preferred_term":"D-(-)-lyxose","sssom_rows":[],"sssom_subject":"MIM:D-_-lyxose","synonym_count":2}'
  snapshot_sha256: 90de548740ec18dec54e38cf165e804a1353547bd1e2c7ce0c5a131bcd7ef14a
- evidence_id: ev-034279f78ffb83be
  kind: prior_review
  reference: reviews/structured/20261011T024629Z-mim-reconcile-all-batch-01/review.yaml
  locator: findings[finding_id=f-021e3723b7ad50fd]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-021e3723b7ad50fd in 20261011T024629Z-mim-reconcile-all-batch-01
  snapshot_sha256: f87124785da2057286555db743ccdb92b70dd4dc359294bde474b4beeb816e48
assessments:
- assessment_id: a-920d086afdaf8d35
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-26db4b94c97aabed
  evidence_ids:
  - ev-cf95a68be557e18a
  - ev-fc5ac5e405c631db
  - ev-b172a2d697478a64
  - ev-2f0bca96872dd59c
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-3b95bfd375690b39
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-26db4b94c97aabed
  evidence_ids:
  - ev-ba0a155c673a7661
  - ev-cf95a68be557e18a
  - ev-fc73952a5dc8d42e
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T13:23:22Z;
    reviewed SHA-256=39b02cd43bdadb3fb76b6e05e83da0e1595572741fae2f4d3e6af59a050fc701;
    current SHA-256=90de548740ec18dec54e38cf165e804a1353547bd1e2c7ce0c5a131bcd7ef14a;
    hash_changed=True. Reports=["reports/yaml_record_review/D-_-lyxose.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The rejected aldehydo
    tombstone correctly drops final SSSOM and points at D-lyxose, but inert stale
    chemistry/role data and an unreviewed cross-record baseline row remain.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ba0a155c673a7661
    - ev-cf95a68be557e18a
  - name: legacy-native-ids
    value: '["SEM:3cd7092c7ec9685ec9af"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-cf95a68be557e18a
    - ev-ba0a155c673a7661
    - ev-fc73952a5dc8d42e
- assessment_id: a-a15bffce40ab7317
  area: evidence
  topic: Historical provisional-role concern
  outcome: unknown
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-26db4b94c97aabed
  evidence_ids:
  - ev-ba0a155c673a7661
  - ev-a15bffce40ab7317
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ba0a155c673a7661
    - ev-a15bffce40ab7317
- assessment_id: a-3a28e74bd1f1e23b
  area: identity
  topic: Retired wrong mapping / stale tombstone ontology pointer
  outcome: supported
  summary: 'The narrow exported-mapping/pointer defect is already fixed: REJECTED
    tombstone, no own-subject SSSOM rows, identifier and ontology_id agree with a
    live merge target. This does not retire source-count, inert chemistry, role, or
    synonym questions.'
  target_ids:
  - record-26db4b94c97aabed
  evidence_ids:
  - ev-ba0a155c673a7661
  - ev-09c57710cd75f921
  - ev-cf95a68be557e18a
  dimensions:
  - name: legacy-disposition
    value: already_fixed
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ba0a155c673a7661
    - ev-09c57710cd75f921
    - ev-cf95a68be557e18a
findings:
- finding_id: rec-f-021e3723b7ad50fd
  issue_key: mim-reconciliation-role-support-26db4b94c97aabed
  category: evidence
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Reassess prediction-only role support: D-(-)-lyxose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-26db4b94c97aabed
  evidence_ids:
  - ev-ba0a155c673a7661
  - ev-a15bffce40ab7317
  - ev-034279f78ffb83be
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-_-lyxose.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
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
    finding_id: f-021e3723b7ad50fd
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
