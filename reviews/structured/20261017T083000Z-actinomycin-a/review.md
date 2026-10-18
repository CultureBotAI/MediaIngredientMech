# Per-record structured review: Actinomycin_A (data/ingredients/mapped/Actinomycin_A.yaml)

- Review: 20261017T083000Z-actinomycin-a
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Actinomycin_A (data/ingredients/mapped/Actinomycin_A.yaml, record-456d4b91f20a93ce, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Actinomycin_A.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Actinomycin_A.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-456d4b91f20a93ce | data/ingredients/mapped/Actinomycin_A.yaml | maintained | Actinomycin_A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-456d4b91f20a93ce | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-456d4b91f20a93ce | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-456d4b91f20a93ce | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-456d4b91f20a93ce.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-456d4b91f20a93ce.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:01:15Z; reviewed SHA-256=a2282b994636d7203ac5d614c8c25ebbe8ff5b0c6a52e4372a44246eb483eafe; current SHA-256=a2282b994636d7203ac5d614c8c25ebbe8ff5b0c6a52e4372a44246eb483eafe; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050115Z-Actinomycin_A.md","reports/yaml_record_review/Actinomycin_A.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Actinomycin_A.md&#96; after the record changed from 852a8e6a74392aa08d499d90034d5fb010abd24796d60e259b74ca486c7baf63 to a2282b994636d7203ac5d614c8c25ebbe8ff5b0c6a52e4372a44246eb483eafe; preserved the previous major finding floor pending targeted retirement.

### Historical provisional-role concern

evidence: concern. Targets: record-456d4b91f20a93ce.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-7ee7ed57742cfa11: Reassess prediction-only role support: Actinomycin A

major / open / confirmed; issue key: mim-reconciliation-role-support-456d4b91f20a93ce.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-7ee7ed57742cfa11

Reassess prediction-only role support: Actinomycin A

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-d8c2dbe5ce521ef5 | data/ingredients/mapped/Actinomycin_A.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[449],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:actinomycin_a","line":451,"mapping_status":"MAPPED","ontology_id":"CHEBI:15369","preferred_term":"Actinomycin A"}],"identifier":"kgmicrobe.compound:actinomycin_a","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:15369","ontology_label":"actinomycin","ontology_source":"CHEBI"},"preferred_term":"Actinomycin A","sssom_rows":[{"data_row":296,"object_id":"CHEBI:15369","object_label":"actinomycin","predicate_id":"skos:broadMatch"},{"data_row":297,"object_id":"kgmicrobe.compound:actinomycin_a","object_label":"Actinomycin A","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Actinomycin_A","synonym_count":1} |
| ev-2a13c9baba132e6b | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [449] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-de6e86fca9068fdb | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Actinomycin_A; data-row positions=[296,297] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":296,"object_id":"CHEBI:15369","object_label":"actinomycin","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Actinomycin_A","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":297,"object_id":"kgmicrobe.compound:actinomycin_a","object_label":"Actinomycin A","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Actinomycin_A","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-bbef2d2fee97d706 | docs/data/mapped_ingredients.csv; CSV lines=[451] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:actinomycin_a","line":451,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:15369","preferred_term":"Actinomycin A","total_occurrences":"0"}] |
| ev-5af04bdeb82072c0 | reports/yaml_record_review/20261001T050115Z-Actinomycin_A.md; YAML Record Review: Actinomycin A:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-8b9836f10d857c53 | reports/yaml_record_review/Actinomycin_A.md; &#96;data/ingredients/mapped/Actinomycin_A.yaml&#96;:2; Verdict:4; Identity:10; Validation:26; Evidence:45; Completeness:66; Recommended Edits:76 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-d63f4a75b83b77c7 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[206,1760] | context_only | [{"current_record_sha256":"a2282b994636d7203ac5d614c8c25ebbe8ff5b0c6a52e4372a44246eb483eafe","finding_id":"SEM:7576b3368569901930c3","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"a2282b994636d7203ac5d614c8c25ebbe8ff5b0c6a52e4372a44246eb483eafe","finding_id":"SEM:e989a532f2b25fc07bfe","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-fee05d2eff21b652 | data/ingredients/mapped/Actinomycin_A.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}] |
| ev-b48f162bfcef60cf | reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml; findings[finding_id=f-7ee7ed57742cfa11] | context_only | Predecessor structured review finding f-7ee7ed57742cfa11 in 20261011T024631Z-mim-reconcile-all-batch-03 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-actinomycin-a
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Actinomycin_A (data/ingredients/mapped/Actinomycin_A.yaml)'
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
summary: Per-record structured review for Actinomycin_A (data/ingredients/mapped/Actinomycin_A.yaml,
  record-456d4b91f20a93ce, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Actinomycin_A.yaml
    sha256: a2282b994636d7203ac5d614c8c25ebbe8ff5b0c6a52e4372a44246eb483eafe
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
  - path: reports/yaml_record_review/20261001T050115Z-Actinomycin_A.md
    sha256: 99ed484ae71cfc27e9ebfcb5d3e7f0ba32823f34c99f494b4f7d4540b5131fab
    role: context
  - path: reports/yaml_record_review/Actinomycin_A.md
    sha256: 3355dd00bac27a54928d82a6b165d6927d108ebe88ef1d90d98f289e96c96fb8
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-456d4b91f20a93ce
  path: data/ingredients/mapped/Actinomycin_A.yaml
  label: Actinomycin_A
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Actinomycin_A.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Actinomycin_A.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Actinomycin_A.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-456d4b91f20a93ce
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-456d4b91f20a93ce
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-456d4b91f20a93ce
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-456d4b91f20a93ce
evidence:
- evidence_id: ev-d8c2dbe5ce521ef5
  kind: record_content
  reference: data/ingredients/mapped/Actinomycin_A.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[449],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:actinomycin_a","line":451,"mapping_status":"MAPPED","ontology_id":"CHEBI:15369","preferred_term":"Actinomycin
    A"}],"identifier":"kgmicrobe.compound:actinomycin_a","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:15369","ontology_label":"actinomycin","ontology_source":"CHEBI"},"preferred_term":"Actinomycin
    A","sssom_rows":[{"data_row":296,"object_id":"CHEBI:15369","object_label":"actinomycin","predicate_id":"skos:broadMatch"},{"data_row":297,"object_id":"kgmicrobe.compound:actinomycin_a","object_label":"Actinomycin
    A","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Actinomycin_A","synonym_count":1}'
  snapshot_sha256: a2282b994636d7203ac5d614c8c25ebbe8ff5b0c6a52e4372a44246eb483eafe
- evidence_id: ev-2a13c9baba132e6b
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [449]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-de6e86fca9068fdb
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Actinomycin_A; data-row positions=[296,297]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":296,"object_id":"CHEBI:15369","object_label":"actinomycin","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Actinomycin_A","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":297,"object_id":"kgmicrobe.compound:actinomycin_a","object_label":"Actinomycin
    A","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Actinomycin_A","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-bbef2d2fee97d706
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[451]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:actinomycin_a","line":451,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:15369","preferred_term":"Actinomycin
    A","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-5af04bdeb82072c0
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050115Z-Actinomycin_A.md
  locator: 'YAML Record Review: Actinomycin A:2; Target:10; Validation:20; Identity
    and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 99ed484ae71cfc27e9ebfcb5d3e7f0ba32823f34c99f494b4f7d4540b5131fab
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/Actinomycin_A.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The CHEBI:15369
    narrow parent and local kgmicrobe identity are consistent, but the SELECTIVE_AGENT
    role is still only provisional computational curation.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Actinomycin_A.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Actinomycin_A.yaml`,
    `just validate-terms data/ingredients/mapped/Actinomycin_A.yaml` where applicable,
    and `just qc-sssom`.'
- evidence_id: ev-8b9836f10d857c53
  kind: prior_review
  reference: reports/yaml_record_review/Actinomycin_A.md
  locator: '`data/ingredients/mapped/Actinomycin_A.yaml`:2; Verdict:4; Identity:10;
    Validation:26; Evidence:45; Completeness:66; Recommended Edits:76'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 3355dd00bac27a54928d82a6b165d6927d108ebe88ef1d90d98f289e96c96fb8
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/Actinomycin_A.yaml`, remove\
    \ or evidence the\n  provisional `physicochemical_roles.SELECTIVE_AGENT` assertion,\
    \ then run\n  `uv run --frozen python scripts/validate_strict.py`, `uv run --frozen\
    \ python scripts/validate_component_partonomy.py`,\n  and `uv run --frozen python\
    \ scripts/validate_sssom_invariants.py`."
- evidence_id: ev-d63f4a75b83b77c7
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[206,1760]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"a2282b994636d7203ac5d614c8c25ebbe8ff5b0c6a52e4372a44246eb483eafe","finding_id":"SEM:7576b3368569901930c3","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"a2282b994636d7203ac5d614c8c25ebbe8ff5b0c6a52e4372a44246eb483eafe","finding_id":"SEM:e989a532f2b25fc07bfe","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-fee05d2eff21b652
  kind: record_content
  reference: data/ingredients/mapped/Actinomycin_A.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}]'
  snapshot_sha256: a2282b994636d7203ac5d614c8c25ebbe8ff5b0c6a52e4372a44246eb483eafe
- evidence_id: ev-b48f162bfcef60cf
  kind: prior_review
  reference: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
  locator: findings[finding_id=f-7ee7ed57742cfa11]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-7ee7ed57742cfa11 in 20261011T024631Z-mim-reconcile-all-batch-03
  snapshot_sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
assessments:
- assessment_id: a-7e1915c35081e262
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-456d4b91f20a93ce
  evidence_ids:
  - ev-d8c2dbe5ce521ef5
  - ev-2a13c9baba132e6b
  - ev-de6e86fca9068fdb
  - ev-bbef2d2fee97d706
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-09c4c9745cb413f1
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-456d4b91f20a93ce
  evidence_ids:
  - ev-5af04bdeb82072c0
  - ev-8b9836f10d857c53
  - ev-d8c2dbe5ce521ef5
  - ev-d63f4a75b83b77c7
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:01:15Z;
    reviewed SHA-256=a2282b994636d7203ac5d614c8c25ebbe8ff5b0c6a52e4372a44246eb483eafe;
    current SHA-256=a2282b994636d7203ac5d614c8c25ebbe8ff5b0c6a52e4372a44246eb483eafe;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050115Z-Actinomycin_A.md","reports/yaml_record_review/Actinomycin_A.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Actinomycin_A.md` after the record changed from 852a8e6a74392aa08d499d90034d5fb010abd24796d60e259b74ca486c7baf63
    to a2282b994636d7203ac5d614c8c25ebbe8ff5b0c6a52e4372a44246eb483eafe; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-5af04bdeb82072c0
    - ev-8b9836f10d857c53
    - ev-d8c2dbe5ce521ef5
  - name: legacy-native-ids
    value: '["SEM:7576b3368569901930c3","SEM:e989a532f2b25fc07bfe"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-d8c2dbe5ce521ef5
    - ev-5af04bdeb82072c0
    - ev-8b9836f10d857c53
    - ev-d63f4a75b83b77c7
- assessment_id: a-fee05d2eff21b652
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-456d4b91f20a93ce
  evidence_ids:
  - ev-5af04bdeb82072c0
  - ev-8b9836f10d857c53
  - ev-fee05d2eff21b652
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-5af04bdeb82072c0
    - ev-8b9836f10d857c53
    - ev-fee05d2eff21b652
findings:
- finding_id: rec-f-7ee7ed57742cfa11
  issue_key: mim-reconciliation-role-support-456d4b91f20a93ce
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Actinomycin A'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-456d4b91f20a93ce
  evidence_ids:
  - ev-5af04bdeb82072c0
  - ev-8b9836f10d857c53
  - ev-fee05d2eff21b652
  - ev-b48f162bfcef60cf
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Actinomycin_A.yaml
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
    review_id: 20261011T024631Z-mim-reconcile-all-batch-03
    finding_id: f-7ee7ed57742cfa11
actions:
- action_id: rec-action-7ee7ed57742cfa11
  description: 'Reassess prediction-only role support: Actinomycin A'
  finding_ids:
  - rec-f-7ee7ed57742cfa11
  target_ids:
  - record-456d4b91f20a93ce
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Actinomycin_A.yaml
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
