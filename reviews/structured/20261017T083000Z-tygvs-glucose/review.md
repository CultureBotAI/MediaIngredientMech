# Per-record structured review: TYGVS_Glucose (data/ingredients/mapped/TYGVS_Glucose.yaml)

- Review: 20261017T083000Z-tygvs-glucose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for TYGVS_Glucose (data/ingredients/mapped/TYGVS_Glucose.yaml, record-c80915d86df9e111, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/TYGVS_Glucose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/TYGVS_Glucose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-c80915d86df9e111 | data/ingredients/mapped/TYGVS_Glucose.yaml | maintained | TYGVS_Glucose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-c80915d86df9e111 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-c80915d86df9e111 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-c80915d86df9e111 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-c80915d86df9e111.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: not_applicable. Targets: record-c80915d86df9e111.

The latest legacy review reports no outstanding finding. This run verifies local consistency only; it does not renew that earlier scientific pass.

Latest manifest verdict=pass; severity=none; reviewed_at=2026-10-01T05:03:39Z; reviewed SHA-256=0914aecb007a71a9f4e010c08b24d55c1b02b1b522c32a8c5384bc56d5959c6e; current SHA-256=0914aecb007a71a9f4e010c08b24d55c1b02b1b522c32a8c5384bc56d5959c6e; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050339Z-TYGVS_Glucose.md","reports/yaml_record_review/TYGVS_Glucose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/TYGVS_Glucose.md&#96; after the record changed from 689fb39c671e99636488c16438ba026133be33b0421ef394f2517769911b150c to 0914aecb007a71a9f4e010c08b24d55c1b02b1b522c32a8c5384bc56d5959c6e; no prior finding is carried forward.

## Findings

### rec-f-61f12adaab38512a: Reassess component source scope: TYGVS_Glucose

major / deferred / provisional; issue key: mim-semantic-component-source-scope-c80915d86df9e111.

Expansion/interpretation is retained as an assertion, but the exact source preparation must be verified before semantic approval. UNKNOWN/PARTIAL completeness is not proof of membership. (Historical finding remains unresolved; no blanket approval.). Affected unit(s): MIM.assertion:0494118e94b8a2124f13652d7fc88be3fedf179f537d7066a9e23355a18d73c0, MIM.assertion:1e8df80a09dfe19cb4d37ff3987d9312287cb461e04c563053ad89e52bc56a5f, MIM.assertion:581ac27e57722a775a24f308f1a0c524a8ee1d6ce4a2b26e8190a45aedb29209, MIM.assertion:86b78e20020c39662b2975fee180a08ca73641172b30442c5577a9850f00650b.

Disposition: Expansion/interpretation is retained as an assertion, but the exact source preparation must be verified before semantic approval. UNKNOWN/PARTIAL completeness is not proof of membership. (Historical finding remains unresolved; no blanket approval.). Affected unit(s): MIM.assertion:0494118e94b8a2124f13652d7fc88be3fedf179f537d7066a9e23355a18d73c0, MIM.assertion:1e8df80a09dfe19cb4d37ff3987d9312287cb461e04c563053ad89e52bc56a5f, MIM.assertion:581ac27e57722a775a24f308f1a0c524a8ee1d6ce4a2b26e8190a45aedb29209, MIM.assertion:86b78e20020c39662b2975fee180a08ca73641172b30442c5577a9850f00650b.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-d29e084b822b370a | data/ingredients/mapped/TYGVS_Glucose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[64],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:tygvs_glucose","line":66,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:tygvs_glucose","preferred_term":"TYGVS + Glucose"}],"identifier":"kgmicrobe.ingredient:tygvs_glucose","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"bergey:substrates"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:tygvs_glucose","ontology_label":"TYGVS + Glucose","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"TYGVS + Glucose","sssom_rows":[{"data_row":2710,"object_id":"kgmicrobe.ingredient:tygvs_glucose","object_label":"TYGVS + Glucose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:TYGVS_Glucose","synonym_count":1} |
| ev-520c93b4efdf119d | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [64] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-f8a9df3cf3e58d5f | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:TYGVS_Glucose; data-row positions=[2710] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2710,"object_id":"kgmicrobe.ingredient:tygvs_glucose","object_label":"TYGVS + Glucose","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:TYGVS_Glucose","validation_method":"manual:move_mapped_out_of_unmapped_collection&#124;MOVED&#124;2026-08-15"}] |
| ev-040fb70ab3fc8a0f | docs/data/mapped_ingredients.csv; CSV lines=[66] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:tygvs_glucose","line":66,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:tygvs_glucose","preferred_term":"TYGVS + Glucose","total_occurrences":"0"}] |
| ev-cea20c2c8fdbb593 | reports/yaml_record_review/20261001T050339Z-TYGVS_Glucose.md; YAML Record Review: TYGVS + Glucose:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:60; Additional Notes:66 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-e8cde39fe1a8a7aa | reports/yaml_record_review/TYGVS_Glucose.md; &#96;data/ingredients/mapped/TYGVS_Glucose.yaml&#96;:2; Verdict:4; Identity:10; Validation:22; Evidence:33; Completeness:46; Recommended Edits:58 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-c26e4e71bcec3d02 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1387,1476,1631,1748] | context_only | [{"current_record_sha256":"0914aecb007a71a9f4e010c08b24d55c1b02b1b522c32a8c5384bc56d5959c6e","finding_id":"SEM:d4aee62995713389feb5","kind":"component_source_scope","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"0914aecb007a71a9f4e010c08b24d55c1b02b1b522c32a8c5384bc56d5959c6e","finding_id":"SEM:1c002b94f688721ee57c","kind":"component_source_scope","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"0914aecb007a71a9f4e010c08b24d55c1b02b1b522c32a8c5384bc56d5959c6e","finding_id":"SEM:1cfec4460ef0ccb1e1d7","kind":"component_source_scope","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"0914aecb007a71a9f4e010c08b24d55c1b02b1b522c32a8c5384bc56d5959c6e","finding_id":"SEM:6f0c9d492dbd45eff5db","kind":"component_source_scope","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-d7045ec30595bfc6 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; current_record=data/ingredients/mapped/TYGVS_Glucose.yaml | context_only | Semantic review finding dispositions ledger |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-tygvs-glucose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: TYGVS_Glucose (data/ingredients/mapped/TYGVS_Glucose.yaml)'
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
native_verdict: mapping_status=MAPPED; open=0; deferred=1
scientific_review: false
summary: Per-record structured review for TYGVS_Glucose (data/ingredients/mapped/TYGVS_Glucose.yaml,
  record-c80915d86df9e111, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/TYGVS_Glucose.yaml
    sha256: 0914aecb007a71a9f4e010c08b24d55c1b02b1b522c32a8c5384bc56d5959c6e
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
  - path: reports/yaml_record_review/20261001T050339Z-TYGVS_Glucose.md
    sha256: 46fe2b15f01674f8f8628d3edb404d263e44ac4072203f3639bac10e98f5b133
    role: context
  - path: reports/yaml_record_review/TYGVS_Glucose.md
    sha256: d0fd1b2d51dd9c225f3b761dbbc7ee64e072d0f8ffa4754c2ea5a5efce6c6cd8
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-c80915d86df9e111
  path: data/ingredients/mapped/TYGVS_Glucose.yaml
  label: TYGVS_Glucose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/TYGVS_Glucose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/TYGVS_Glucose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/TYGVS_Glucose.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-c80915d86df9e111
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-c80915d86df9e111
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-c80915d86df9e111
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-c80915d86df9e111
evidence:
- evidence_id: ev-d29e084b822b370a
  kind: record_content
  reference: data/ingredients/mapped/TYGVS_Glucose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[64],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:tygvs_glucose","line":66,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:tygvs_glucose","preferred_term":"TYGVS
    + Glucose"}],"identifier":"kgmicrobe.ingredient:tygvs_glucose","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"bergey:substrates"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:tygvs_glucose","ontology_label":"TYGVS
    + Glucose","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"TYGVS +
    Glucose","sssom_rows":[{"data_row":2710,"object_id":"kgmicrobe.ingredient:tygvs_glucose","object_label":"TYGVS
    + Glucose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:TYGVS_Glucose","synonym_count":1}'
  snapshot_sha256: 0914aecb007a71a9f4e010c08b24d55c1b02b1b522c32a8c5384bc56d5959c6e
- evidence_id: ev-520c93b4efdf119d
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [64]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-f8a9df3cf3e58d5f
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:TYGVS_Glucose; data-row positions=[2710]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2710,"object_id":"kgmicrobe.ingredient:tygvs_glucose","object_label":"TYGVS
    + Glucose","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:TYGVS_Glucose","validation_method":"manual:move_mapped_out_of_unmapped_collection|MOVED|2026-08-15"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-040fb70ab3fc8a0f
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[66]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:tygvs_glucose","line":66,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:tygvs_glucose","preferred_term":"TYGVS
    + Glucose","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-cea20c2c8fdbb593
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050339Z-TYGVS_Glucose.md
  locator: 'YAML Record Review: TYGVS + Glucose:2; Target:10; Validation:20; Identity
    and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:60; Additional Notes:66'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 46fe2b15f01674f8f8628d3edb404d263e44ac4072203f3639bac10e98f5b133
  quote: 'Findings:

    None found.


    Recommended Edits:

    - None.'
- evidence_id: ev-e8cde39fe1a8a7aa
  kind: prior_review
  reference: reports/yaml_record_review/TYGVS_Glucose.md
  locator: '`data/ingredients/mapped/TYGVS_Glucose.yaml`:2; Verdict:4; Identity:10;
    Validation:22; Evidence:33; Completeness:46; Recommended Edits:58'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: d0fd1b2d51dd9c225f3b761dbbc7ee64e072d0f8ffa4754c2ea5a5efce6c6cd8
  quote: 'Recommended Edits:

    - None.'
- evidence_id: ev-c26e4e71bcec3d02
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1387,1476,1631,1748]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"0914aecb007a71a9f4e010c08b24d55c1b02b1b522c32a8c5384bc56d5959c6e","finding_id":"SEM:d4aee62995713389feb5","kind":"component_source_scope","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"0914aecb007a71a9f4e010c08b24d55c1b02b1b522c32a8c5384bc56d5959c6e","finding_id":"SEM:1c002b94f688721ee57c","kind":"component_source_scope","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"0914aecb007a71a9f4e010c08b24d55c1b02b1b522c32a8c5384bc56d5959c6e","finding_id":"SEM:1cfec4460ef0ccb1e1d7","kind":"component_source_scope","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"0914aecb007a71a9f4e010c08b24d55c1b02b1b522c32a8c5384bc56d5959c6e","finding_id":"SEM:6f0c9d492dbd45eff5db","kind":"component_source_scope","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-d7045ec30595bfc6
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: current_record=data/ingredients/mapped/TYGVS_Glucose.yaml
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Semantic review finding dispositions ledger
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-88a0f35e36079304
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-c80915d86df9e111
  evidence_ids:
  - ev-d29e084b822b370a
  - ev-520c93b4efdf119d
  - ev-f8a9df3cf3e58d5f
  - ev-040fb70ab3fc8a0f
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-013b942e7a1b5b12
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: not_applicable
  summary: The latest legacy review reports no outstanding finding. This run verifies
    local consistency only; it does not renew that earlier scientific pass.
  target_ids:
  - record-c80915d86df9e111
  evidence_ids:
  - ev-cea20c2c8fdbb593
  - ev-e8cde39fe1a8a7aa
  - ev-d29e084b822b370a
  - ev-c26e4e71bcec3d02
  details: 'Latest manifest verdict=pass; severity=none; reviewed_at=2026-10-01T05:03:39Z;
    reviewed SHA-256=0914aecb007a71a9f4e010c08b24d55c1b02b1b522c32a8c5384bc56d5959c6e;
    current SHA-256=0914aecb007a71a9f4e010c08b24d55c1b02b1b522c32a8c5384bc56d5959c6e;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050339Z-TYGVS_Glucose.md","reports/yaml_record_review/TYGVS_Glucose.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/TYGVS_Glucose.md` after the record changed from 689fb39c671e99636488c16438ba026133be33b0421ef394f2517769911b150c
    to 0914aecb007a71a9f4e010c08b24d55c1b02b1b522c32a8c5384bc56d5959c6e; no prior
    finding is carried forward.'
  dimensions:
  - name: legacy-native-ids
    value: '["SEM:d4aee62995713389feb5","SEM:1c002b94f688721ee57c","SEM:1cfec4460ef0ccb1e1d7","SEM:6f0c9d492dbd45eff5db"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-d29e084b822b370a
    - ev-cea20c2c8fdbb593
    - ev-e8cde39fe1a8a7aa
    - ev-c26e4e71bcec3d02
findings:
- finding_id: rec-f-61f12adaab38512a
  issue_key: mim-semantic-component-source-scope-c80915d86df9e111
  category: representation
  severity: major
  status: deferred
  certainty: provisional
  title: 'Reassess component source scope: TYGVS_Glucose'
  description: 'Expansion/interpretation is retained as an assertion, but the exact
    source preparation must be verified before semantic approval. UNKNOWN/PARTIAL
    completeness is not proof of membership. (Historical finding remains unresolved;
    no blanket approval.). Affected unit(s): MIM.assertion:0494118e94b8a2124f13652d7fc88be3fedf179f537d7066a9e23355a18d73c0,
    MIM.assertion:1e8df80a09dfe19cb4d37ff3987d9312287cb461e04c563053ad89e52bc56a5f,
    MIM.assertion:581ac27e57722a775a24f308f1a0c524a8ee1d6ce4a2b26e8190a45aedb29209,
    MIM.assertion:86b78e20020c39662b2975fee180a08ca73641172b30442c5577a9850f00650b.'
  disposition_reason: 'Expansion/interpretation is retained as an assertion, but the
    exact source preparation must be verified before semantic approval. UNKNOWN/PARTIAL
    completeness is not proof of membership. (Historical finding remains unresolved;
    no blanket approval.). Affected unit(s): MIM.assertion:0494118e94b8a2124f13652d7fc88be3fedf179f537d7066a9e23355a18d73c0,
    MIM.assertion:1e8df80a09dfe19cb4d37ff3987d9312287cb461e04c563053ad89e52bc56a5f,
    MIM.assertion:581ac27e57722a775a24f308f1a0c524a8ee1d6ce4a2b26e8190a45aedb29209,
    MIM.assertion:86b78e20020c39662b2975fee180a08ca73641172b30442c5577a9850f00650b.'
  target_ids:
  - record-c80915d86df9e111
  evidence_ids:
  - ev-d29e084b822b370a
  - ev-d7045ec30595bfc6
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/TYGVS_Glucose.yaml
    role: maintained ingredient
  field_paths:
  - synonyms
  - occurrence_statistics
  tags:
  - reconciliation
  - bundle-by-owner
  - component-source-scope
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.
```
