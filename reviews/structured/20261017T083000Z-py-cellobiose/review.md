# Per-record structured review: PY-cellobiose (data/ingredients/mapped/PY-cellobiose.yaml)

- Review: 20261017T083000Z-py-cellobiose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for PY-cellobiose (data/ingredients/mapped/PY-cellobiose.yaml, record-170106107e972596, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/PY-cellobiose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/PY-cellobiose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-170106107e972596 | data/ingredients/mapped/PY-cellobiose.yaml | maintained | PY-cellobiose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-170106107e972596 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-170106107e972596 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-170106107e972596 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-170106107e972596.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: not_applicable. Targets: record-170106107e972596.

The latest legacy review reports no outstanding finding. This run verifies local consistency only; it does not renew that earlier scientific pass.

Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-17T08:11:44Z; reviewed SHA-256=43affad15730fa118b5a490edeb105cc9ca4b3967851eede7a94addf4746683f; current SHA-256=43affad15730fa118b5a490edeb105cc9ca4b3967851eede7a94addf4746683f; hash_changed=False. Reports=["reports/yaml_record_review/PY-cellobiose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local kgmicrobe.ingredient PY-cellobiose mixture identity, components, and final row pass.

## Findings

### rec-f-1495466b7c7e58a4: Reassess component source scope: PY-cellobiose

major / deferred / provisional; issue key: mim-semantic-component-source-scope-170106107e972596.

Expansion/interpretation is retained as an assertion, but the exact source preparation must be verified before semantic approval. UNKNOWN/PARTIAL completeness is not proof of membership. (Historical finding remains unresolved; no blanket approval.). Affected unit(s): MIM.assertion:b6214b75d798ea125d49d7c382b742444aadf9eff5c91cd57a302945975c4e6d, MIM.assertion:bfe68ab1c8b4963716327220045a81950c0618b06c96c07eccef903ef2734925, MIM.assertion:ec4147dc51c9455c8870bf56c4a708c6f2eb63edb23e48b5bd46ef0a4041991f.

Disposition: Expansion/interpretation is retained as an assertion, but the exact source preparation must be verified before semantic approval. UNKNOWN/PARTIAL completeness is not proof of membership. (Historical finding remains unresolved; no blanket approval.). Affected unit(s): MIM.assertion:b6214b75d798ea125d49d7c382b742444aadf9eff5c91cd57a302945975c4e6d, MIM.assertion:bfe68ab1c8b4963716327220045a81950c0618b06c96c07eccef903ef2734925, MIM.assertion:ec4147dc51c9455c8870bf56c4a708c6f2eb63edb23e48b5bd46ef0a4041991f.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-c7b6a2958228443b | data/ingredients/mapped/PY-cellobiose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[48],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:py_cellobiose","line":50,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:py_cellobiose","preferred_term":"PY-cellobiose"}],"identifier":"kgmicrobe.ingredient:py_cellobiose","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:py_cellobiose","ontology_label":"PY-cellobiose","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"PY-cellobiose","sssom_rows":[{"data_row":2177,"object_id":"kgmicrobe.ingredient:py_cellobiose","object_label":"PY-cellobiose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:PY-cellobiose","synonym_count":1} |
| ev-050976d168d5c907 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [48] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-759c3b6679b165ed | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:PY-cellobiose; data-row positions=[2177] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2177,"object_id":"kgmicrobe.ingredient:py_cellobiose","object_label":"PY-cellobiose","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:PY-cellobiose","validation_method":"manual:move_mapped_out_of_unmapped_collection&#124;MOVED&#124;2026-08-15"}] |
| ev-c042efd0c65caf90 | docs/data/mapped_ingredients.csv; CSV lines=[50] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:py_cellobiose","line":50,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:py_cellobiose","preferred_term":"PY-cellobiose","total_occurrences":"0"}] |
| ev-34b7e1f074931d26 | reports/yaml_record_review/PY-cellobiose.md; &#96;data/ingredients/mapped/PY-cellobiose.yaml&#96;:2; Verdict:4; Identity:10; Validation:22; Evidence:32; Completeness:47; Recommended Edits:56 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-34432035eb9d8f2a | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1891,1918,2055] | context_only | [{"current_record_sha256":"43affad15730fa118b5a490edeb105cc9ca4b3967851eede7a94addf4746683f","finding_id":"SEM:ef2f4b09031d5dcc6e85","kind":"component_source_scope","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"43affad15730fa118b5a490edeb105cc9ca4b3967851eede7a94addf4746683f","finding_id":"SEM:a37958ac62d0b582c545","kind":"component_source_scope","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"43affad15730fa118b5a490edeb105cc9ca4b3967851eede7a94addf4746683f","finding_id":"SEM:1a6a77befba289728a02","kind":"component_source_scope","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-py-cellobiose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: PY-cellobiose (data/ingredients/mapped/PY-cellobiose.yaml)'
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
summary: Per-record structured review for PY-cellobiose (data/ingredients/mapped/PY-cellobiose.yaml,
  record-170106107e972596, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/PY-cellobiose.yaml
    sha256: 43affad15730fa118b5a490edeb105cc9ca4b3967851eede7a94addf4746683f
    role: target
  - path: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
    sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
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
  - path: reports/yaml_record_review/PY-cellobiose.md
    sha256: c7ce06273cb09b1cae699267cd145cb845ac99ac2651c5d80d25b1e66a01b5d0
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-170106107e972596
  path: data/ingredients/mapped/PY-cellobiose.yaml
  label: PY-cellobiose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/PY-cellobiose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/PY-cellobiose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/PY-cellobiose.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-170106107e972596
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-170106107e972596
  evidence_ids:
  - ev-c7b6a2958228443b
  - ev-050976d168d5c907
  - ev-759c3b6679b165ed
  - ev-c042efd0c65caf90
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-170106107e972596
  evidence_ids:
  - ev-c7b6a2958228443b
  - ev-34432035eb9d8f2a
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-170106107e972596
  evidence_ids:
  - ev-34b7e1f074931d26
  - ev-34432035eb9d8f2a
evidence:
- evidence_id: ev-c7b6a2958228443b
  kind: record_content
  reference: data/ingredients/mapped/PY-cellobiose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[48],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:py_cellobiose","line":50,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:py_cellobiose","preferred_term":"PY-cellobiose"}],"identifier":"kgmicrobe.ingredient:py_cellobiose","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:py_cellobiose","ontology_label":"PY-cellobiose","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"PY-cellobiose","sssom_rows":[{"data_row":2177,"object_id":"kgmicrobe.ingredient:py_cellobiose","object_label":"PY-cellobiose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:PY-cellobiose","synonym_count":1}'
  snapshot_sha256: 43affad15730fa118b5a490edeb105cc9ca4b3967851eede7a94addf4746683f
- evidence_id: ev-050976d168d5c907
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [48]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-759c3b6679b165ed
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:PY-cellobiose; data-row positions=[2177]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2177,"object_id":"kgmicrobe.ingredient:py_cellobiose","object_label":"PY-cellobiose","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:PY-cellobiose","validation_method":"manual:move_mapped_out_of_unmapped_collection|MOVED|2026-08-15"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-c042efd0c65caf90
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[50]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:py_cellobiose","line":50,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:py_cellobiose","preferred_term":"PY-cellobiose","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-34b7e1f074931d26
  kind: prior_review
  reference: reports/yaml_record_review/PY-cellobiose.md
  locator: '`data/ingredients/mapped/PY-cellobiose.yaml`:2; Verdict:4; Identity:10;
    Validation:22; Evidence:32; Completeness:47; Recommended Edits:56'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: c7ce06273cb09b1cae699267cd145cb845ac99ac2651c5d80d25b1e66a01b5d0
  quote: 'Recommended Edits:

    - None.'
- evidence_id: ev-34432035eb9d8f2a
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1891,1918,2055]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"43affad15730fa118b5a490edeb105cc9ca4b3967851eede7a94addf4746683f","finding_id":"SEM:ef2f4b09031d5dcc6e85","kind":"component_source_scope","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"43affad15730fa118b5a490edeb105cc9ca4b3967851eede7a94addf4746683f","finding_id":"SEM:a37958ac62d0b582c545","kind":"component_source_scope","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"43affad15730fa118b5a490edeb105cc9ca4b3967851eede7a94addf4746683f","finding_id":"SEM:1a6a77befba289728a02","kind":"component_source_scope","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-d6baac15407697ec
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-170106107e972596
  evidence_ids:
  - ev-c7b6a2958228443b
  - ev-050976d168d5c907
  - ev-759c3b6679b165ed
  - ev-c042efd0c65caf90
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-a03a01819d9eec42
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: not_applicable
  summary: The latest legacy review reports no outstanding finding. This run verifies
    local consistency only; it does not renew that earlier scientific pass.
  target_ids:
  - record-170106107e972596
  evidence_ids:
  - ev-34b7e1f074931d26
  - ev-c7b6a2958228443b
  - ev-34432035eb9d8f2a
  details: 'Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-17T08:11:44Z;
    reviewed SHA-256=43affad15730fa118b5a490edeb105cc9ca4b3967851eede7a94addf4746683f;
    current SHA-256=43affad15730fa118b5a490edeb105cc9ca4b3967851eede7a94addf4746683f;
    hash_changed=False. Reports=["reports/yaml_record_review/PY-cellobiose.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The local kgmicrobe.ingredient
    PY-cellobiose mixture identity, components, and final row pass.'
  dimensions:
  - name: legacy-native-ids
    value: '["SEM:ef2f4b09031d5dcc6e85","SEM:a37958ac62d0b582c545","SEM:1a6a77befba289728a02"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-c7b6a2958228443b
    - ev-34b7e1f074931d26
    - ev-34432035eb9d8f2a
findings:
- finding_id: rec-f-1495466b7c7e58a4
  issue_key: mim-semantic-component-source-scope-170106107e972596
  category: representation
  severity: major
  status: deferred
  certainty: provisional
  title: 'Reassess component source scope: PY-cellobiose'
  description: 'Expansion/interpretation is retained as an assertion, but the exact
    source preparation must be verified before semantic approval. UNKNOWN/PARTIAL
    completeness is not proof of membership. (Historical finding remains unresolved;
    no blanket approval.). Affected unit(s): MIM.assertion:b6214b75d798ea125d49d7c382b742444aadf9eff5c91cd57a302945975c4e6d,
    MIM.assertion:bfe68ab1c8b4963716327220045a81950c0618b06c96c07eccef903ef2734925,
    MIM.assertion:ec4147dc51c9455c8870bf56c4a708c6f2eb63edb23e48b5bd46ef0a4041991f.'
  disposition_reason: 'Expansion/interpretation is retained as an assertion, but the
    exact source preparation must be verified before semantic approval. UNKNOWN/PARTIAL
    completeness is not proof of membership. (Historical finding remains unresolved;
    no blanket approval.). Affected unit(s): MIM.assertion:b6214b75d798ea125d49d7c382b742444aadf9eff5c91cd57a302945975c4e6d,
    MIM.assertion:bfe68ab1c8b4963716327220045a81950c0618b06c96c07eccef903ef2734925,
    MIM.assertion:ec4147dc51c9455c8870bf56c4a708c6f2eb63edb23e48b5bd46ef0a4041991f.'
  target_ids:
  - record-170106107e972596
  evidence_ids:
  - ev-c7b6a2958228443b
  - ev-34432035eb9d8f2a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/PY-cellobiose.yaml
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
  with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.
```
