# Per-record structured review: Trace_Minerals (data/ingredients/mapped/Trace_Minerals.yaml)

- Review: 20261017T083000Z-trace-minerals
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Trace_Minerals (data/ingredients/mapped/Trace_Minerals.yaml, record-7c55027f9d88edd0, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Trace_Minerals.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Trace_Minerals.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-7c55027f9d88edd0 | data/ingredients/mapped/Trace_Minerals.yaml | maintained | Trace_Minerals |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-7c55027f9d88edd0 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-7c55027f9d88edd0 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-7c55027f9d88edd0 | Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-7c55027f9d88edd0.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-7c55027f9d88edd0.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T19:17:55Z; reviewed SHA-256=9a1b033572d1f6462d4de4d9f07d655e34f98fe37d82c2449d4a48cc2dadd1bc; current SHA-256=9a1b033572d1f6462d4de4d9f07d655e34f98fe37d82c2449d4a48cc2dadd1bc; hash_changed=False. Reports=["reports/yaml_record_review/Trace_Minerals.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local stock identity passes, but see-below and starred CultureMech aliases leak into final SSSOM other.

### Unresolved recipe-reference or truncated-concentration synonyms

nomenclature: concern. Targets: record-7c55027f9d88edd0.

Historical tokens are still present on the exact-subject SSSOM rows: [{"reason":"unresolved recipe cross-reference in a resolving synonym","token":"Trace minerals (see below)"}]. Truncated concentration strings and context-dependent instructions need scoped curation. This check does not reject catalog/RAW_TEXT synonyms as a class.

### Certainty correction for the exact token observation

nomenclature: unknown. Targets: record-7c55027f9d88edd0.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

## Findings

### rec-scope-f-0fa9eaef6cc34337: Adjudicate source scope of exported tokens: Trace minerals

major / deferred / provisional; issue key: mim-reconciliation-exported-context-tokens-7c55027f9d88edd0.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

Disposition: Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-736425dfd6ed1253 | data/ingredients/mapped/Trace_Minerals.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2511],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:trace_minerals","line":2513,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:trace_minerals","preferred_term":"Trace minerals"}],"identifier":"kgmicrobe.ingredient:trace_minerals","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:trace_minerals","ontology_label":"Trace minerals","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Trace minerals","sssom_rows":[{"data_row":2810,"object_id":"kgmicrobe.ingredient:trace_minerals","object_label":"Trace minerals","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Trace_Minerals","synonym_count":3} |
| ev-7826f81947721109 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2511] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-02edadefe666dbc3 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Trace_Minerals; data-row positions=[2810] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2810,"object_id":"kgmicrobe.ingredient:trace_minerals","object_label":"Trace minerals","other":"Trace minerals (see below)&#124;Trace minerals*","predicate_id":"skos:exactMatch","subject_id":"MIM:Trace_Minerals","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-09-02"}] |
| ev-54925f551ad24584 | docs/data/mapped_ingredients.csv; CSV lines=[2513] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:trace_minerals","line":2513,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"3","ontology_id":"kgmicrobe.ingredient:trace_minerals","preferred_term":"Trace minerals","total_occurrences":"3"}] |
| ev-f3047b74cd613a2a | reports/yaml_record_review/Trace_Minerals.md; &#96;data/ingredients/mapped/Trace_Minerals.yaml&#96;:2; Verdict:4; Identity:10; Validation:23; Evidence:33; Issues:42; Major: recipe notes reach final &#96;other&#96;:44; Completeness:50; Recommended Edits:58 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-164498fccd779079 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1301] | context_only | [{"current_record_sha256":"9a1b033572d1f6462d4de4d9f07d655e34f98fe37d82c2449d4a48cc2dadd1bc","finding_id":"SEM:d2d59db3d6dac794891c","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-823412d1eacb6795 | MAPPING_SEMANTICS.md; Sections on REJECTED_LABEL and the damaged-label RAW_TEXT carve-out | supports | Raw spellings may remain resolvable when they denote the same substance. Wrong-identity labels must not resolve. A recipe-pointer pattern alone does not adjudicate that distinction. |
| ev-e098338a3394e86d | reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml; findings[finding_id=f-0fa9eaef6cc34337] | context_only | Exact earlier occurrence has open/confirmed status, based on exported-token presence and historical report text. |
| ev-2c39d54a6bcf5e1b | data/ingredients/mapped/Trace_Minerals.yaml; identifier, ontology_mapping, synonyms and curation_history | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2511],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:trace_minerals","line":2513,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:trace_minerals","preferred_term":"Trace minerals"}],"identifier":"kgmicrobe.ingredient:trace_minerals","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:trace_minerals","ontology_label":"Trace minerals","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Trace minerals","sssom_rows":[{"data_row":2810,"object_id":"kgmicrobe.ingredient:trace_minerals","object_label":"Trace minerals","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Trace_Minerals","synonym_count":3} |
| ev-ec1703c8dacbdf80 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Trace_Minerals; data-row positions=[2810] | supports | Current exact-subject rows, including complete other payload: [{"data_row":2810,"object_id":"kgmicrobe.ingredient:trace_minerals","object_label":"Trace minerals","other":"Trace minerals (see below)&#124;Trace minerals*","predicate_id":"skos:exactMatch","subject_id":"MIM:Trace_Minerals","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-09-02"}] |
| ev-649d543ff1a236ba | reports/yaml_record_review/Trace_Minerals.md; Complete historical report, including Verdict and Recommended Edits | context_only | Historical interpretation was read in full; it is not fresh source adjudication. |
| ev-7f43bddd2b7e5507 | reviews/structured/20261011T030852Z-mim-token-scope-reassessment/review.yaml; findings[finding_id=scope-f-0fa9eaef6cc34337] | context_only | Predecessor structured review finding scope-f-0fa9eaef6cc34337 in 20261011T030852Z-mim-token-scope-reassessment |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024639Z-mim-reconcile-all-batch-12, 20261011T030852Z-mim-token-scope-reassessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-trace-minerals
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Trace_Minerals (data/ingredients/mapped/Trace_Minerals.yaml)'
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
summary: Per-record structured review for Trace_Minerals (data/ingredients/mapped/Trace_Minerals.yaml,
  record-7c55027f9d88edd0, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Trace_Minerals.yaml
    sha256: 9a1b033572d1f6462d4de4d9f07d655e34f98fe37d82c2449d4a48cc2dadd1bc
    role: target
  - path: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
    sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
    role: context
  - path: reviews/structured/20261011T030852Z-mim-token-scope-reassessment/review.yaml
    sha256: 42a76b000bcbd07b426f6bad61b124b11ec08d8977783a67b732b01754f7c609
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
  - path: reports/yaml_record_review/Trace_Minerals.md
    sha256: ca899d0e1e9ffdc149ed07abe32a65e07f563cffb61c30cddb9fbe01b22b47e5
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
  - path: MAPPING_SEMANTICS.md
    sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805
    role: context
targets:
- target_id: record-7c55027f9d88edd0
  path: data/ingredients/mapped/Trace_Minerals.yaml
  label: Trace_Minerals
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trace_Minerals.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Trace_Minerals.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Trace_Minerals.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-7c55027f9d88edd0
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-7c55027f9d88edd0
  evidence_ids:
  - ev-736425dfd6ed1253
  - ev-7826f81947721109
  - ev-02edadefe666dbc3
  - ev-54925f551ad24584
  - ev-2c39d54a6bcf5e1b
  - ev-ec1703c8dacbdf80
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-7c55027f9d88edd0
  evidence_ids:
  - ev-736425dfd6ed1253
  - ev-164498fccd779079
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12
    and semantic review dispositions on HEAD.
  target_ids:
  - record-7c55027f9d88edd0
  evidence_ids:
  - ev-f3047b74cd613a2a
  - ev-164498fccd779079
  - ev-e098338a3394e86d
  - ev-649d543ff1a236ba
  - ev-7f43bddd2b7e5507
evidence:
- evidence_id: ev-736425dfd6ed1253
  kind: record_content
  reference: data/ingredients/mapped/Trace_Minerals.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2511],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:trace_minerals","line":2513,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:trace_minerals","preferred_term":"Trace
    minerals"}],"identifier":"kgmicrobe.ingredient:trace_minerals","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:trace_minerals","ontology_label":"Trace
    minerals","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Trace minerals","sssom_rows":[{"data_row":2810,"object_id":"kgmicrobe.ingredient:trace_minerals","object_label":"Trace
    minerals","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Trace_Minerals","synonym_count":3}'
  snapshot_sha256: 9a1b033572d1f6462d4de4d9f07d655e34f98fe37d82c2449d4a48cc2dadd1bc
- evidence_id: ev-7826f81947721109
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2511]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-02edadefe666dbc3
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Trace_Minerals; data-row positions=[2810]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2810,"object_id":"kgmicrobe.ingredient:trace_minerals","object_label":"Trace
    minerals","other":"Trace minerals (see below)|Trace minerals*","predicate_id":"skos:exactMatch","subject_id":"MIM:Trace_Minerals","validation_method":"none|UNKNOWN_TERM|2026-09-02"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-54925f551ad24584
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2513]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:trace_minerals","line":2513,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"3","ontology_id":"kgmicrobe.ingredient:trace_minerals","preferred_term":"Trace
    minerals","total_occurrences":"3"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-f3047b74cd613a2a
  kind: prior_review
  reference: reports/yaml_record_review/Trace_Minerals.md
  locator: '`data/ingredients/mapped/Trace_Minerals.yaml`:2; Verdict:4; Identity:10;
    Validation:23; Evidence:33; Issues:42; Major: recipe notes reach final `other`:44;
    Completeness:50; Recommended Edits:58'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: ca899d0e1e9ffdc149ed07abe32a65e07f563cffb61c30cddb9fbe01b22b47e5
  quote: "Issues:\n\n\nMajor: recipe notes reach final `other`:\nBoth final `other`\
    \ tokens are raw CultureMech occurrence labels. `see below`\nis a recipe cross-reference\
    \ and `*` is a footnote marker, so neither is a true\nsynonym of the local stock\
    \ identity.\n\nRecommended Edits:\n- Mark `Trace minerals (see below)` and `Trace\
    \ minerals*` as non-exportable raw\n  source text so the final SSSOM `other` column\
    \ is empty for this row."
- evidence_id: ev-164498fccd779079
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1301]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"9a1b033572d1f6462d4de4d9f07d655e34f98fe37d82c2449d4a48cc2dadd1bc","finding_id":"SEM:d2d59db3d6dac794891c","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-823412d1eacb6795
  kind: record_content
  reference: MAPPING_SEMANTICS.md
  locator: Sections on REJECTED_LABEL and the damaged-label RAW_TEXT carve-out
  accessed_at: '2026-10-11T03:08:52Z'
  support: supports
  summary: Raw spellings may remain resolvable when they denote the same substance.
    Wrong-identity labels must not resolve. A recipe-pointer pattern alone does not
    adjudicate that distinction.
  snapshot_sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805
- evidence_id: ev-e098338a3394e86d
  kind: prior_review
  reference: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
  locator: findings[finding_id=f-0fa9eaef6cc34337]
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Exact earlier occurrence has open/confirmed status, based on exported-token
    presence and historical report text.
  snapshot_sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
  quote: '{"category": "nomenclature", "certainty": "confirmed", "description": "Historical
    tokens are still present on the exact-subject SSSOM rows: [{\"reason\":\"unresolved
    recipe cross-reference in a resolving synonym\",\"token\":\"Trace minerals (see
    below)\"}]. Truncated concentration strings and context-dependent instructions
    need scoped curation. This check does not reject catalog/RAW_TEXT synonyms as
    a class.", "evidence_ids": ["ev-f3047b74cd613a2a", "ev-02edadefe666dbc3"], "external_issues":
    ["https://github.com/CultureBotAI/MediaIngredientMech/issues/718"], "field_paths":
    ["synonyms", "SSSOM.other"], "finding_id": "f-0fa9eaef6cc34337", "issue_key":
    "mim-reconciliation-exported-context-tokens-7c55027f9d88edd0", "owner_paths":
    [{"path": "data/ingredients/mapped/Trace_Minerals.yaml", "repository": "CultureBotAI/MediaIngredientMech",
    "role": "maintained ingredient"}], "severity": "major", "status": "open", "tags":
    ["reconciliation", "bundle-by-owner", "exported-context-tokens"], "target_ids":
    ["record-7c55027f9d88edd0"], "title": "Review nonportable exported tokens: Trace
    minerals"}'
- evidence_id: ev-2c39d54a6bcf5e1b
  kind: record_content
  reference: data/ingredients/mapped/Trace_Minerals.yaml
  locator: identifier, ontology_mapping, synonyms and curation_history
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2511],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:trace_minerals","line":2513,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:trace_minerals","preferred_term":"Trace
    minerals"}],"identifier":"kgmicrobe.ingredient:trace_minerals","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:trace_minerals","ontology_label":"Trace
    minerals","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Trace minerals","sssom_rows":[{"data_row":2810,"object_id":"kgmicrobe.ingredient:trace_minerals","object_label":"Trace
    minerals","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Trace_Minerals","synonym_count":3}'
  snapshot_sha256: 9a1b033572d1f6462d4de4d9f07d655e34f98fe37d82c2449d4a48cc2dadd1bc
- evidence_id: ev-ec1703c8dacbdf80
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Trace_Minerals; data-row positions=[2810]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2810,"object_id":"kgmicrobe.ingredient:trace_minerals","object_label":"Trace
    minerals","other":"Trace minerals (see below)|Trace minerals*","predicate_id":"skos:exactMatch","subject_id":"MIM:Trace_Minerals","validation_method":"none|UNKNOWN_TERM|2026-09-02"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-649d543ff1a236ba
  kind: prior_review
  reference: reports/yaml_record_review/Trace_Minerals.md
  locator: Complete historical report, including Verdict and Recommended Edits
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Historical interpretation was read in full; it is not fresh source adjudication.
  snapshot_sha256: ca899d0e1e9ffdc149ed07abe32a65e07f563cffb61c30cddb9fbe01b22b47e5
  quote: "# `data/ingredients/mapped/Trace_Minerals.yaml`\n\n## Verdict\n\nNeeds curation,\
    \ major. The local trace-mineral stock/pre-mix identity is\nsynchronized, but\
    \ `see below` and starred raw source labels leak into final\nSSSOM `other`.\n\n\
    ## Identity\n\n- Reviewed record: `data/ingredients/mapped/Trace_Minerals.yaml`.\n\
    - Identifier and grounding: `identifier:\n  kgmicrobe.ingredient:trace_minerals`\
    \ with matching\n  `ontology_mapping.ontology_id`, label `Trace minerals`, source\n\
    \  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,\n  `mapping_status:\
    \ MAPPED`, `ingredient_type: STOCK_SOLUTION`, and\n  `solution_type: TRACE_METAL_MIX`.\n\
    - Synonyms: raw mim-queue source form plus raw CultureMech forms `Trace\n  minerals\
    \ (see below)` and `Trace minerals*`.\n- Occurrences: 3 CultureMech recipe occurrences\
    \ in 3 media.\n\n## Validation\n\n- `uv run --frozen python scripts/validate_strict.py`\
    \ on the 5-file batch from\n  `Trace_Mineral_Solution` through `Trans-aconitic_Acid`:\
    \ exited 0 and wrote\n  zero ERROR rows.\n- Direct old Engine A/OBO term validation\
    \ was skipped for this row because\n  `kgmicrobe.ingredient` is a non-OBO local\
    \ registry prefix.\n- Local aggregate comparison found this per-record file synchronized\
    \ with its\n  keyed row in `data/curated/mapped_ingredients.yaml`.\n\n## Evidence\n\
    \n- The May review rejected identity to the broad MeSH `Trace Elements` class,\n\
    \  and the August issue 288 curation minted a local identity for this\n  trace-mineral\
    \ stock/pre-mix.\n- The final SSSOM row has\n  `MIM:Trace_Minerals skos:exactMatch\
    \ kgmicrobe.ingredient:trace_minerals`\n  and exports `Trace minerals (see below)|Trace\
    \ minerals*` in `other`.\n\n## Issues\n\n### Major: recipe notes reach final `other`\n\
    \nBoth final `other` tokens are raw CultureMech occurrence labels. `see below`\n\
    is a recipe cross-reference and `*` is a footnote marker, so neither is a true\n\
    synonym of the local stock identity.\n\n## Completeness\n\n- The local identity,\
    \ fallback registry mapping, occurrence count, aggregate\n  copy, and final exact\
    \ row agree.\n- No roles, components, parent ontology rows, or chemical properties\
    \ are\n  asserted.\n- The only issue is the leaked raw CultureMech aliases.\n\n\
    ## Recommended Edits\n\n- Mark `Trace minerals (see below)` and `Trace minerals*`\
    \ as non-exportable raw\n  source text so the final SSSOM `other` column is empty\
    \ for this row.\n"
- evidence_id: ev-7f43bddd2b7e5507
  kind: prior_review
  reference: reviews/structured/20261011T030852Z-mim-token-scope-reassessment/review.yaml
  locator: findings[finding_id=scope-f-0fa9eaef6cc34337]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding scope-f-0fa9eaef6cc34337 in 20261011T030852Z-mim-token-scope-reassessment
  snapshot_sha256: 42a76b000bcbd07b426f6bad61b124b11ec08d8977783a67b732b01754f7c609
assessments:
- assessment_id: a-5d338fbfbb5a0851
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-7c55027f9d88edd0
  evidence_ids:
  - ev-736425dfd6ed1253
  - ev-7826f81947721109
  - ev-02edadefe666dbc3
  - ev-54925f551ad24584
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-cd336e2f30320da1
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-7c55027f9d88edd0
  evidence_ids:
  - ev-f3047b74cd613a2a
  - ev-736425dfd6ed1253
  - ev-164498fccd779079
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T19:17:55Z;
    reviewed SHA-256=9a1b033572d1f6462d4de4d9f07d655e34f98fe37d82c2449d4a48cc2dadd1bc;
    current SHA-256=9a1b033572d1f6462d4de4d9f07d655e34f98fe37d82c2449d4a48cc2dadd1bc;
    hash_changed=False. Reports=["reports/yaml_record_review/Trace_Minerals.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    stock identity passes, but see-below and starred CultureMech aliases leak into
    final SSSOM other.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f3047b74cd613a2a
    - ev-736425dfd6ed1253
  - name: legacy-native-ids
    value: '["SEM:d2d59db3d6dac794891c"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-736425dfd6ed1253
    - ev-f3047b74cd613a2a
    - ev-164498fccd779079
- assessment_id: a-64c9a6ac7d486248
  area: nomenclature
  topic: Unresolved recipe-reference or truncated-concentration synonyms
  outcome: concern
  summary: 'Historical tokens are still present on the exact-subject SSSOM rows: [{"reason":"unresolved
    recipe cross-reference in a resolving synonym","token":"Trace minerals (see below)"}].
    Truncated concentration strings and context-dependent instructions need scoped
    curation. This check does not reject catalog/RAW_TEXT synonyms as a class.'
  target_ids:
  - record-7c55027f9d88edd0
  evidence_ids:
  - ev-f3047b74cd613a2a
  - ev-02edadefe666dbc3
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f3047b74cd613a2a
    - ev-02edadefe666dbc3
- assessment_id: scope-f-0fa9eaef6cc34337
  area: nomenclature
  topic: Certainty correction for the exact token observation
  outcome: unknown
  summary: Token presence remains reproducible, but the earlier pattern-based observation
    did not establish whether the exact source label denotes this subject or a different
    preparation. Fresh source-context adjudication is required before a confirmed
    defect or label removal. This successor corrects certainty only; it does not establish
    that the token is valid or that another identity allegation is fixed.
  target_ids:
  - record-7c55027f9d88edd0
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-e098338a3394e86d
  - ev-2c39d54a6bcf5e1b
  - ev-ec1703c8dacbdf80
  - ev-649d543ff1a236ba
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Source-scope question only, not a disposition of the complete historical
      report.
    evidence_ids:
    - ev-823412d1eacb6795
    - ev-e098338a3394e86d
    - ev-2c39d54a6bcf5e1b
    - ev-ec1703c8dacbdf80
    - ev-649d543ff1a236ba
findings:
- finding_id: rec-scope-f-0fa9eaef6cc34337
  issue_key: mim-reconciliation-exported-context-tokens-7c55027f9d88edd0
  category: nomenclature
  severity: major
  status: deferred
  certainty: provisional
  title: 'Adjudicate source scope of exported tokens: Trace minerals'
  description: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed.
  target_ids:
  - record-7c55027f9d88edd0
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-e098338a3394e86d
  - ev-2c39d54a6bcf5e1b
  - ev-ec1703c8dacbdf80
  - ev-649d543ff1a236ba
  - ev-7f43bddd2b7e5507
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trace_Minerals.yaml
    role: maintained ingredient
  field_paths:
  - synonyms
  - SSSOM.other
  tags:
  - reconciliation
  - bundle-by-owner
  - exported-context-tokens
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/861
  disposition_reason: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T030852Z-mim-token-scope-reassessment
    finding_id: scope-f-0fa9eaef6cc34337
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
  with lineage to 20261011T024639Z-mim-reconcile-all-batch-12, 20261011T030852Z-mim-token-scope-reassessment.
```
