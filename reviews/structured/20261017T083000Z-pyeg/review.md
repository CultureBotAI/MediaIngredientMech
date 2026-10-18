# Per-record structured review: PYEG (data/ingredients/mapped/PYEG.yaml)

- Review: 20261017T083000Z-pyeg
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for PYEG (data/ingredients/mapped/PYEG.yaml, record-da8361cb445541aa, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/PYEG.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/PYEG.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-da8361cb445541aa | data/ingredients/mapped/PYEG.yaml | maintained | PYEG |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-da8361cb445541aa | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-da8361cb445541aa | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-da8361cb445541aa | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-da8361cb445541aa.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: not_applicable. Targets: record-da8361cb445541aa.

The latest legacy review reports no outstanding finding. This run verifies local consistency only; it does not renew that earlier scientific pass.

Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-17T08:19:51Z; reviewed SHA-256=59aa22d3f741cba3f712bb3294adc7abc1f1e6933dad74b9d79001299c88dd0a; current SHA-256=59aa22d3f741cba3f712bb3294adc7abc1f1e6933dad74b9d79001299c88dd0a; hash_changed=False. Reports=["reports/yaml_record_review/PYEG.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local kgmicrobe.ingredient PYEG mixture identity, components, and final row pass.

## Findings

### rec-f-a19fa4136979a400: Reassess component source scope: PYEG

major / deferred / provisional; issue key: mim-semantic-component-source-scope-da8361cb445541aa.

Expansion/interpretation is retained as an assertion, but the exact source preparation must be verified before semantic approval. UNKNOWN/PARTIAL completeness is not proof of membership. (Historical finding remains unresolved; no blanket approval.). Affected unit(s): MIM.assertion:0b62d870ea596b6fdf8422d9dc3369e5a9e493e96251f2c419964aabc6b78c94, MIM.assertion:5a448065c5aadef456609bcae202b3e3d80ca08573425c376b09b61664dfc622, MIM.assertion:aa7a1d60bae0087006a060ed42ae4467a9780bcb2b319dec77868ef911504bac.

Disposition: Expansion/interpretation is retained as an assertion, but the exact source preparation must be verified before semantic approval. UNKNOWN/PARTIAL completeness is not proof of membership. (Historical finding remains unresolved; no blanket approval.). Affected unit(s): MIM.assertion:0b62d870ea596b6fdf8422d9dc3369e5a9e493e96251f2c419964aabc6b78c94, MIM.assertion:5a448065c5aadef456609bcae202b3e3d80ca08573425c376b09b61664dfc622, MIM.assertion:aa7a1d60bae0087006a060ed42ae4467a9780bcb2b319dec77868ef911504bac.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-bc9e8f73f90b7fd9 | data/ingredients/mapped/PYEG.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[53],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:pyeg","line":55,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:pyeg","preferred_term":"PYEG"}],"identifier":"kgmicrobe.ingredient:pyeg","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:pyeg","ontology_label":"PYEG","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"PYEG","sssom_rows":[{"data_row":2182,"object_id":"kgmicrobe.ingredient:pyeg","object_label":"PYEG","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:PYEG","synonym_count":1} |
| ev-dfab73497a79e5c5 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [53] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-82d5140ab9053fe8 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:PYEG; data-row positions=[2182] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2182,"object_id":"kgmicrobe.ingredient:pyeg","object_label":"PYEG","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:PYEG","validation_method":"manual:move_mapped_out_of_unmapped_collection&#124;MOVED&#124;2026-08-15"}] |
| ev-6cba4ff15eae8167 | docs/data/mapped_ingredients.csv; CSV lines=[55] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:pyeg","line":55,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:pyeg","preferred_term":"PYEG","total_occurrences":"0"}] |
| ev-7623942f51f519f6 | reports/yaml_record_review/PYEG.md; &#96;data/ingredients/mapped/PYEG.yaml&#96;:2; Verdict:4; Identity:10; Validation:20; Evidence:31; Completeness:46; Recommended Edits:54 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-4fb026243fc9a634 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1410,1637,1856] | context_only | [{"current_record_sha256":"59aa22d3f741cba3f712bb3294adc7abc1f1e6933dad74b9d79001299c88dd0a","finding_id":"SEM:64f76c455631e72adfc2","kind":"component_source_scope","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"59aa22d3f741cba3f712bb3294adc7abc1f1e6933dad74b9d79001299c88dd0a","finding_id":"SEM:7723b5e4c1662a22a282","kind":"component_source_scope","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"59aa22d3f741cba3f712bb3294adc7abc1f1e6933dad74b9d79001299c88dd0a","finding_id":"SEM:9f075631effcf8c12579","kind":"component_source_scope","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-pyeg
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: PYEG (data/ingredients/mapped/PYEG.yaml)'
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
summary: Per-record structured review for PYEG (data/ingredients/mapped/PYEG.yaml,
  record-da8361cb445541aa, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/PYEG.yaml
    sha256: 59aa22d3f741cba3f712bb3294adc7abc1f1e6933dad74b9d79001299c88dd0a
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
  - path: reports/yaml_record_review/PYEG.md
    sha256: 6977a457f1ae9ee76a81a8d2ea53c7cb70e392df42702cbdf86dd951bc3daa78
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-da8361cb445541aa
  path: data/ingredients/mapped/PYEG.yaml
  label: PYEG
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/PYEG.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/PYEG.yaml covering
    current record state, role evidence support, published surfaces, and residual
    historical review claims.
  selection: Single record data/ingredients/mapped/PYEG.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-da8361cb445541aa
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-da8361cb445541aa
  evidence_ids:
  - ev-bc9e8f73f90b7fd9
  - ev-dfab73497a79e5c5
  - ev-82d5140ab9053fe8
  - ev-6cba4ff15eae8167
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-da8361cb445541aa
  evidence_ids:
  - ev-bc9e8f73f90b7fd9
  - ev-4fb026243fc9a634
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-da8361cb445541aa
  evidence_ids:
  - ev-7623942f51f519f6
  - ev-4fb026243fc9a634
evidence:
- evidence_id: ev-bc9e8f73f90b7fd9
  kind: record_content
  reference: data/ingredients/mapped/PYEG.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[53],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:pyeg","line":55,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:pyeg","preferred_term":"PYEG"}],"identifier":"kgmicrobe.ingredient:pyeg","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:pyeg","ontology_label":"PYEG","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"PYEG","sssom_rows":[{"data_row":2182,"object_id":"kgmicrobe.ingredient:pyeg","object_label":"PYEG","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:PYEG","synonym_count":1}'
  snapshot_sha256: 59aa22d3f741cba3f712bb3294adc7abc1f1e6933dad74b9d79001299c88dd0a
- evidence_id: ev-dfab73497a79e5c5
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [53]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-82d5140ab9053fe8
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:PYEG; data-row positions=[2182]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2182,"object_id":"kgmicrobe.ingredient:pyeg","object_label":"PYEG","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:PYEG","validation_method":"manual:move_mapped_out_of_unmapped_collection|MOVED|2026-08-15"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-6cba4ff15eae8167
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[55]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:pyeg","line":55,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:pyeg","preferred_term":"PYEG","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-7623942f51f519f6
  kind: prior_review
  reference: reports/yaml_record_review/PYEG.md
  locator: '`data/ingredients/mapped/PYEG.yaml`:2; Verdict:4; Identity:10; Validation:20;
    Evidence:31; Completeness:46; Recommended Edits:54'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 6977a457f1ae9ee76a81a8d2ea53c7cb70e392df42702cbdf86dd951bc3daa78
  quote: 'Recommended Edits:

    - None.'
- evidence_id: ev-4fb026243fc9a634
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1410,1637,1856]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"59aa22d3f741cba3f712bb3294adc7abc1f1e6933dad74b9d79001299c88dd0a","finding_id":"SEM:64f76c455631e72adfc2","kind":"component_source_scope","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"59aa22d3f741cba3f712bb3294adc7abc1f1e6933dad74b9d79001299c88dd0a","finding_id":"SEM:7723b5e4c1662a22a282","kind":"component_source_scope","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"59aa22d3f741cba3f712bb3294adc7abc1f1e6933dad74b9d79001299c88dd0a","finding_id":"SEM:9f075631effcf8c12579","kind":"component_source_scope","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-47a455444c5a3578
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-da8361cb445541aa
  evidence_ids:
  - ev-bc9e8f73f90b7fd9
  - ev-dfab73497a79e5c5
  - ev-82d5140ab9053fe8
  - ev-6cba4ff15eae8167
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-6c848d7b9d9fb011
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: not_applicable
  summary: The latest legacy review reports no outstanding finding. This run verifies
    local consistency only; it does not renew that earlier scientific pass.
  target_ids:
  - record-da8361cb445541aa
  evidence_ids:
  - ev-7623942f51f519f6
  - ev-bc9e8f73f90b7fd9
  - ev-4fb026243fc9a634
  details: 'Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-17T08:19:51Z;
    reviewed SHA-256=59aa22d3f741cba3f712bb3294adc7abc1f1e6933dad74b9d79001299c88dd0a;
    current SHA-256=59aa22d3f741cba3f712bb3294adc7abc1f1e6933dad74b9d79001299c88dd0a;
    hash_changed=False. Reports=["reports/yaml_record_review/PYEG.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The local kgmicrobe.ingredient
    PYEG mixture identity, components, and final row pass.'
  dimensions:
  - name: legacy-native-ids
    value: '["SEM:64f76c455631e72adfc2","SEM:7723b5e4c1662a22a282","SEM:9f075631effcf8c12579"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-bc9e8f73f90b7fd9
    - ev-7623942f51f519f6
    - ev-4fb026243fc9a634
findings:
- finding_id: rec-f-a19fa4136979a400
  issue_key: mim-semantic-component-source-scope-da8361cb445541aa
  category: representation
  severity: major
  status: deferred
  certainty: provisional
  title: 'Reassess component source scope: PYEG'
  description: 'Expansion/interpretation is retained as an assertion, but the exact
    source preparation must be verified before semantic approval. UNKNOWN/PARTIAL
    completeness is not proof of membership. (Historical finding remains unresolved;
    no blanket approval.). Affected unit(s): MIM.assertion:0b62d870ea596b6fdf8422d9dc3369e5a9e493e96251f2c419964aabc6b78c94,
    MIM.assertion:5a448065c5aadef456609bcae202b3e3d80ca08573425c376b09b61664dfc622,
    MIM.assertion:aa7a1d60bae0087006a060ed42ae4467a9780bcb2b319dec77868ef911504bac.'
  disposition_reason: 'Expansion/interpretation is retained as an assertion, but the
    exact source preparation must be verified before semantic approval. UNKNOWN/PARTIAL
    completeness is not proof of membership. (Historical finding remains unresolved;
    no blanket approval.). Affected unit(s): MIM.assertion:0b62d870ea596b6fdf8422d9dc3369e5a9e493e96251f2c419964aabc6b78c94,
    MIM.assertion:5a448065c5aadef456609bcae202b3e3d80ca08573425c376b09b61664dfc622,
    MIM.assertion:aa7a1d60bae0087006a060ed42ae4467a9780bcb2b319dec77868ef911504bac.'
  target_ids:
  - record-da8361cb445541aa
  evidence_ids:
  - ev-bc9e8f73f90b7fd9
  - ev-4fb026243fc9a634
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/PYEG.yaml
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
