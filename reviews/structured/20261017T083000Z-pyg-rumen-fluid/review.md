# Per-record structured review: PYG_Rumen_Fluid (data/ingredients/mapped/PYG_Rumen_Fluid.yaml)

- Review: 20261017T083000Z-pyg-rumen-fluid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for PYG_Rumen_Fluid (data/ingredients/mapped/PYG_Rumen_Fluid.yaml, record-84a25f8ea3406283, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/PYG_Rumen_Fluid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/PYG_Rumen_Fluid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-84a25f8ea3406283 | data/ingredients/mapped/PYG_Rumen_Fluid.yaml | maintained | PYG_Rumen_Fluid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-84a25f8ea3406283 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-84a25f8ea3406283 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-84a25f8ea3406283 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-84a25f8ea3406283.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: not_applicable. Targets: record-84a25f8ea3406283.

The latest legacy review reports no outstanding finding. This run verifies local consistency only; it does not renew that earlier scientific pass.

Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-17T08:24:27Z; reviewed SHA-256=833d1bf421b60fb474361c29a35f88d5702c790d5385221d6fa6757199801c01; current SHA-256=833d1bf421b60fb474361c29a35f88d5702c790d5385221d6fa6757199801c01; hash_changed=False. Reports=["reports/yaml_record_review/PYG_Rumen_Fluid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local kgmicrobe.ingredient PYG plus Rumen Fluid mixture identity, components, and final row pass.

## Findings

### rec-f-9251e0249b28cd08: Reassess component source scope: PYG_Rumen_Fluid

major / deferred / provisional; issue key: mim-semantic-component-source-scope-84a25f8ea3406283.

Expansion/interpretation is retained as an assertion, but the exact source preparation must be verified before semantic approval. UNKNOWN/PARTIAL completeness is not proof of membership. (Historical finding remains unresolved; no blanket approval.). Affected unit(s): MIM.assertion:0a7afbe75791ceb4c426bc9e0f5b45ee7c2392c674a261ce3571668e3ed94371, MIM.assertion:50571b3571770ebbc7cfadadfacf5052f9499b73f1d3ade276066fbf23d65c2c, MIM.assertion:b669cdd82153e54b5be9fd650e716be2d26b9decfe913e894c3900fe5d6da39b, MIM.assertion:c60809e252ca0c3ebfacc92025767dbfc94b23717414f11310c2ab05943ff4f7.

Disposition: Expansion/interpretation is retained as an assertion, but the exact source preparation must be verified before semantic approval. UNKNOWN/PARTIAL completeness is not proof of membership. (Historical finding remains unresolved; no blanket approval.). Affected unit(s): MIM.assertion:0a7afbe75791ceb4c426bc9e0f5b45ee7c2392c674a261ce3571668e3ed94371, MIM.assertion:50571b3571770ebbc7cfadadfacf5052f9499b73f1d3ade276066fbf23d65c2c, MIM.assertion:b669cdd82153e54b5be9fd650e716be2d26b9decfe913e894c3900fe5d6da39b, MIM.assertion:c60809e252ca0c3ebfacc92025767dbfc94b23717414f11310c2ab05943ff4f7.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-c1ac67a89ae3450a | data/ingredients/mapped/PYG_Rumen_Fluid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[57],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:pyg_rumen_fluid","line":59,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:pyg_rumen_fluid","preferred_term":"PYG + Rumen Fluid"}],"identifier":"kgmicrobe.ingredient:pyg_rumen_fluid","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"bergey:substrates"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:pyg_rumen_fluid","ontology_label":"PYG + Rumen Fluid","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"PYG + Rumen Fluid","sssom_rows":[{"data_row":2184,"object_id":"kgmicrobe.ingredient:pyg_rumen_fluid","object_label":"PYG + Rumen Fluid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:PYG_Rumen_Fluid","synonym_count":1} |
| ev-226d457a2ba09a27 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [57] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-57e706baa6baaf74 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:PYG_Rumen_Fluid; data-row positions=[2184] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2184,"object_id":"kgmicrobe.ingredient:pyg_rumen_fluid","object_label":"PYG + Rumen Fluid","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:PYG_Rumen_Fluid","validation_method":"manual:move_mapped_out_of_unmapped_collection&#124;MOVED&#124;2026-08-15"}] |
| ev-bf4ebcd7d21936b5 | docs/data/mapped_ingredients.csv; CSV lines=[59] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:pyg_rumen_fluid","line":59,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:pyg_rumen_fluid","preferred_term":"PYG + Rumen Fluid","total_occurrences":"0"}] |
| ev-5697d539107eb694 | reports/yaml_record_review/PYG_Rumen_Fluid.md; &#96;data/ingredients/mapped/PYG_Rumen_Fluid.yaml&#96;:2; Verdict:4; Identity:10; Validation:22; Evidence:34; Completeness:49; Recommended Edits:56 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-9ef228b826d762ac | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1404,1614,1892,1939] | context_only | [{"current_record_sha256":"833d1bf421b60fb474361c29a35f88d5702c790d5385221d6fa6757199801c01","finding_id":"SEM:edafdd3e7e62162992cd","kind":"component_source_scope","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"833d1bf421b60fb474361c29a35f88d5702c790d5385221d6fa6757199801c01","finding_id":"SEM:822e6f9214192679b159","kind":"component_source_scope","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"833d1bf421b60fb474361c29a35f88d5702c790d5385221d6fa6757199801c01","finding_id":"SEM:ad9fd4c1ccd576bfe991","kind":"component_source_scope","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"833d1bf421b60fb474361c29a35f88d5702c790d5385221d6fa6757199801c01","finding_id":"SEM:1bdf40abc89d8724a79e","kind":"component_source_scope","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-827558932bab4e20 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; current_record=data/ingredients/mapped/PYG_Rumen_Fluid.yaml | context_only | Semantic review finding dispositions ledger |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-pyg-rumen-fluid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: PYG_Rumen_Fluid (data/ingredients/mapped/PYG_Rumen_Fluid.yaml)'
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
summary: Per-record structured review for PYG_Rumen_Fluid (data/ingredients/mapped/PYG_Rumen_Fluid.yaml,
  record-84a25f8ea3406283, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/PYG_Rumen_Fluid.yaml
    sha256: 833d1bf421b60fb474361c29a35f88d5702c790d5385221d6fa6757199801c01
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
  - path: reports/yaml_record_review/PYG_Rumen_Fluid.md
    sha256: 3e9ea2a465146f295d9e90fe0de1b755eb8083992fdc3d68c560c0dd57ffa226
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-84a25f8ea3406283
  path: data/ingredients/mapped/PYG_Rumen_Fluid.yaml
  label: PYG_Rumen_Fluid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/PYG_Rumen_Fluid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/PYG_Rumen_Fluid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/PYG_Rumen_Fluid.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-84a25f8ea3406283
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-84a25f8ea3406283
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-84a25f8ea3406283
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-84a25f8ea3406283
evidence:
- evidence_id: ev-c1ac67a89ae3450a
  kind: record_content
  reference: data/ingredients/mapped/PYG_Rumen_Fluid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[57],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:pyg_rumen_fluid","line":59,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:pyg_rumen_fluid","preferred_term":"PYG
    + Rumen Fluid"}],"identifier":"kgmicrobe.ingredient:pyg_rumen_fluid","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"bergey:substrates"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:pyg_rumen_fluid","ontology_label":"PYG
    + Rumen Fluid","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"PYG
    + Rumen Fluid","sssom_rows":[{"data_row":2184,"object_id":"kgmicrobe.ingredient:pyg_rumen_fluid","object_label":"PYG
    + Rumen Fluid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:PYG_Rumen_Fluid","synonym_count":1}'
  snapshot_sha256: 833d1bf421b60fb474361c29a35f88d5702c790d5385221d6fa6757199801c01
- evidence_id: ev-226d457a2ba09a27
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [57]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-57e706baa6baaf74
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:PYG_Rumen_Fluid; data-row positions=[2184]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2184,"object_id":"kgmicrobe.ingredient:pyg_rumen_fluid","object_label":"PYG
    + Rumen Fluid","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:PYG_Rumen_Fluid","validation_method":"manual:move_mapped_out_of_unmapped_collection|MOVED|2026-08-15"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-bf4ebcd7d21936b5
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[59]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:pyg_rumen_fluid","line":59,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:pyg_rumen_fluid","preferred_term":"PYG
    + Rumen Fluid","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-5697d539107eb694
  kind: prior_review
  reference: reports/yaml_record_review/PYG_Rumen_Fluid.md
  locator: '`data/ingredients/mapped/PYG_Rumen_Fluid.yaml`:2; Verdict:4; Identity:10;
    Validation:22; Evidence:34; Completeness:49; Recommended Edits:56'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 3e9ea2a465146f295d9e90fe0de1b755eb8083992fdc3d68c560c0dd57ffa226
  quote: 'Recommended Edits:

    - None.'
- evidence_id: ev-9ef228b826d762ac
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1404,1614,1892,1939]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"833d1bf421b60fb474361c29a35f88d5702c790d5385221d6fa6757199801c01","finding_id":"SEM:edafdd3e7e62162992cd","kind":"component_source_scope","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"833d1bf421b60fb474361c29a35f88d5702c790d5385221d6fa6757199801c01","finding_id":"SEM:822e6f9214192679b159","kind":"component_source_scope","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"833d1bf421b60fb474361c29a35f88d5702c790d5385221d6fa6757199801c01","finding_id":"SEM:ad9fd4c1ccd576bfe991","kind":"component_source_scope","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"833d1bf421b60fb474361c29a35f88d5702c790d5385221d6fa6757199801c01","finding_id":"SEM:1bdf40abc89d8724a79e","kind":"component_source_scope","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-827558932bab4e20
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: current_record=data/ingredients/mapped/PYG_Rumen_Fluid.yaml
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Semantic review finding dispositions ledger
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-6358e76fd4b84ce5
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-84a25f8ea3406283
  evidence_ids:
  - ev-c1ac67a89ae3450a
  - ev-226d457a2ba09a27
  - ev-57e706baa6baaf74
  - ev-bf4ebcd7d21936b5
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-570b31d96ccdc6b2
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: not_applicable
  summary: The latest legacy review reports no outstanding finding. This run verifies
    local consistency only; it does not renew that earlier scientific pass.
  target_ids:
  - record-84a25f8ea3406283
  evidence_ids:
  - ev-5697d539107eb694
  - ev-c1ac67a89ae3450a
  - ev-9ef228b826d762ac
  details: 'Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-17T08:24:27Z;
    reviewed SHA-256=833d1bf421b60fb474361c29a35f88d5702c790d5385221d6fa6757199801c01;
    current SHA-256=833d1bf421b60fb474361c29a35f88d5702c790d5385221d6fa6757199801c01;
    hash_changed=False. Reports=["reports/yaml_record_review/PYG_Rumen_Fluid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    kgmicrobe.ingredient PYG plus Rumen Fluid mixture identity, components, and final
    row pass.'
  dimensions:
  - name: legacy-native-ids
    value: '["SEM:edafdd3e7e62162992cd","SEM:822e6f9214192679b159","SEM:ad9fd4c1ccd576bfe991","SEM:1bdf40abc89d8724a79e"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-c1ac67a89ae3450a
    - ev-5697d539107eb694
    - ev-9ef228b826d762ac
findings:
- finding_id: rec-f-9251e0249b28cd08
  issue_key: mim-semantic-component-source-scope-84a25f8ea3406283
  category: representation
  severity: major
  status: deferred
  certainty: provisional
  title: 'Reassess component source scope: PYG_Rumen_Fluid'
  description: 'Expansion/interpretation is retained as an assertion, but the exact
    source preparation must be verified before semantic approval. UNKNOWN/PARTIAL
    completeness is not proof of membership. (Historical finding remains unresolved;
    no blanket approval.). Affected unit(s): MIM.assertion:0a7afbe75791ceb4c426bc9e0f5b45ee7c2392c674a261ce3571668e3ed94371,
    MIM.assertion:50571b3571770ebbc7cfadadfacf5052f9499b73f1d3ade276066fbf23d65c2c,
    MIM.assertion:b669cdd82153e54b5be9fd650e716be2d26b9decfe913e894c3900fe5d6da39b,
    MIM.assertion:c60809e252ca0c3ebfacc92025767dbfc94b23717414f11310c2ab05943ff4f7.'
  disposition_reason: 'Expansion/interpretation is retained as an assertion, but the
    exact source preparation must be verified before semantic approval. UNKNOWN/PARTIAL
    completeness is not proof of membership. (Historical finding remains unresolved;
    no blanket approval.). Affected unit(s): MIM.assertion:0a7afbe75791ceb4c426bc9e0f5b45ee7c2392c674a261ce3571668e3ed94371,
    MIM.assertion:50571b3571770ebbc7cfadadfacf5052f9499b73f1d3ade276066fbf23d65c2c,
    MIM.assertion:b669cdd82153e54b5be9fd650e716be2d26b9decfe913e894c3900fe5d6da39b,
    MIM.assertion:c60809e252ca0c3ebfacc92025767dbfc94b23717414f11310c2ab05943ff4f7.'
  target_ids:
  - record-84a25f8ea3406283
  evidence_ids:
  - ev-c1ac67a89ae3450a
  - ev-827558932bab4e20
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/PYG_Rumen_Fluid.yaml
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
