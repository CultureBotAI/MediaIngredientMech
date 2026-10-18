# Per-record structured review: Trace_Mineral_Solution (data/ingredients/mapped/Trace_Mineral_Solution.yaml)

- Review: 20261017T083000Z-trace-mineral-solution
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Trace_Mineral_Solution (data/ingredients/mapped/Trace_Mineral_Solution.yaml, record-4b03942a3427132e, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Trace_Mineral_Solution.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Trace_Mineral_Solution.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-4b03942a3427132e | data/ingredients/mapped/Trace_Mineral_Solution.yaml | maintained | Trace_Mineral_Solution |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-4b03942a3427132e | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-4b03942a3427132e | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-4b03942a3427132e | Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-4b03942a3427132e.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-4b03942a3427132e.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T19:17:55Z; reviewed SHA-256=03837875ebc88c1ab82387c244b383de83a01bc77f4fd60cd75fbbecdcd31f81; current SHA-256=03837875ebc88c1ab82387c244b383de83a01bc77f4fd60cd75fbbecdcd31f81; hash_changed=False. Reports=["reports/yaml_record_review/Trace_Mineral_Solution.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local stock identity passes, but five see-Medium, see-below, or footnoted aliases leak into final SSSOM other.

### Unresolved recipe-reference or truncated-concentration synonyms

nomenclature: concern. Targets: record-4b03942a3427132e.

Historical tokens are still present on the exact-subject SSSOM rows: [{"reason":"unresolved recipe cross-reference in a resolving synonym","token":"Trace mineral solution (see Medium No. 151 )"},{"reason":"unresolved recipe cross-reference in a resolving synonym","token":"Trace mineral solution (see Medium No.852)"}]. Truncated concentration strings and context-dependent instructions need scoped curation. This check does not reject catalog/RAW_TEXT synonyms as a class.

### Certainty correction for the exact token observation

nomenclature: unknown. Targets: record-4b03942a3427132e.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

## Findings

### rec-scope-f-54e5335934e0ba03: Adjudicate source scope of exported tokens: Trace mineral solution

major / deferred / provisional; issue key: mim-reconciliation-exported-context-tokens-4b03942a3427132e.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

Disposition: Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-ceefc84dd27464ad | data/ingredients/mapped/Trace_Mineral_Solution.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2510],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:trace_mineral_solution","line":2512,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:trace_mineral_solution","preferred_term":"Trace mineral solution"}],"identifier":"kgmicrobe.ingredient:trace_mineral_solution","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:trace_mineral_solution","ontology_label":"Trace mineral solution","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Trace mineral solution","sssom_rows":[{"data_row":2809,"object_id":"kgmicrobe.ingredient:trace_mineral_solution","object_label":"Trace mineral solution","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Trace_Mineral_Solution","synonym_count":6} |
| ev-40852c4b8e4f817b | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2510] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-702e1b26f74fa1cf | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Trace_Mineral_Solution; data-row positions=[2809] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2809,"object_id":"kgmicrobe.ingredient:trace_mineral_solution","object_label":"Trace mineral solution","other":"Trace mineral solution (see Medium No. 151 )&#124;Trace mineral solution (see Medium No. 852 )&#124;Trace mineral solution (see Medium No.852)&#124;Trace mineral solution (see below)&#124;Trace mineral solution**","predicate_id":"skos:exactMatch","subject_id":"MIM:Trace_Mineral_Solution","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-09-02"}] |
| ev-4b28b132ec221ca3 | docs/data/mapped_ingredients.csv; CSV lines=[2512] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:trace_mineral_solution","line":2512,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"2","ontology_id":"kgmicrobe.ingredient:trace_mineral_solution","preferred_term":"Trace mineral solution","total_occurrences":"2"}] |
| ev-0eefc9d77ca437e5 | reports/yaml_record_review/Trace_Mineral_Solution.md; &#96;data/ingredients/mapped/Trace_Mineral_Solution.yaml&#96;:2; Verdict:4; Identity:9; Validation:21; Evidence:31; Issues:43; Major: recipe cross-references and footnotes reach final &#96;other&#96;:45; Completeness:53; Recommended Edits:61 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-9bd72ce41e674e19 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1300] | context_only | [{"current_record_sha256":"03837875ebc88c1ab82387c244b383de83a01bc77f4fd60cd75fbbecdcd31f81","finding_id":"SEM:7c1609d63523c7517ff0","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-823412d1eacb6795 | MAPPING_SEMANTICS.md; Sections on REJECTED_LABEL and the damaged-label RAW_TEXT carve-out | supports | Raw spellings may remain resolvable when they denote the same substance. Wrong-identity labels must not resolve. A recipe-pointer pattern alone does not adjudicate that distinction. |
| ev-28bce6da08c8c14e | reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml; findings[finding_id=f-54e5335934e0ba03] | context_only | Exact earlier occurrence has open/confirmed status, based on exported-token presence and historical report text. |
| ev-41b7b72cded4e05c | data/ingredients/mapped/Trace_Mineral_Solution.yaml; identifier, ontology_mapping, synonyms and curation_history | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2510],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:trace_mineral_solution","line":2512,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:trace_mineral_solution","preferred_term":"Trace mineral solution"}],"identifier":"kgmicrobe.ingredient:trace_mineral_solution","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:trace_mineral_solution","ontology_label":"Trace mineral solution","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Trace mineral solution","sssom_rows":[{"data_row":2809,"object_id":"kgmicrobe.ingredient:trace_mineral_solution","object_label":"Trace mineral solution","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Trace_Mineral_Solution","synonym_count":6} |
| ev-3f611fd20092d7d4 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Trace_Mineral_Solution; data-row positions=[2809] | supports | Current exact-subject rows, including complete other payload: [{"data_row":2809,"object_id":"kgmicrobe.ingredient:trace_mineral_solution","object_label":"Trace mineral solution","other":"Trace mineral solution (see Medium No. 151 )&#124;Trace mineral solution (see Medium No. 852 )&#124;Trace mineral solution (see Medium No.852)&#124;Trace mineral solution (see below)&#124;Trace mineral solution**","predicate_id":"skos:exactMatch","subject_id":"MIM:Trace_Mineral_Solution","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-09-02"}] |
| ev-ff886fb7448948d4 | reports/yaml_record_review/Trace_Mineral_Solution.md; Complete historical report, including Verdict and Recommended Edits | context_only | Historical interpretation was read in full; it is not fresh source adjudication. |
| ev-50f45c15b17c740a | reviews/structured/20261011T030852Z-mim-token-scope-reassessment/review.yaml; findings[finding_id=scope-f-54e5335934e0ba03] | context_only | Predecessor structured review finding scope-f-54e5335934e0ba03 in 20261011T030852Z-mim-token-scope-reassessment |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024639Z-mim-reconcile-all-batch-12, 20261011T030852Z-mim-token-scope-reassessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-trace-mineral-solution
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Trace_Mineral_Solution (data/ingredients/mapped/Trace_Mineral_Solution.yaml)'
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
summary: Per-record structured review for Trace_Mineral_Solution (data/ingredients/mapped/Trace_Mineral_Solution.yaml,
  record-4b03942a3427132e, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Trace_Mineral_Solution.yaml
    sha256: 03837875ebc88c1ab82387c244b383de83a01bc77f4fd60cd75fbbecdcd31f81
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
  - path: reports/yaml_record_review/Trace_Mineral_Solution.md
    sha256: 95f2187e644085226dc05c4e6c0a2b3fc440fc600205141bc84c41b066625b34
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
  - path: MAPPING_SEMANTICS.md
    sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805
    role: context
targets:
- target_id: record-4b03942a3427132e
  path: data/ingredients/mapped/Trace_Mineral_Solution.yaml
  label: Trace_Mineral_Solution
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trace_Mineral_Solution.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Trace_Mineral_Solution.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Trace_Mineral_Solution.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-4b03942a3427132e
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-4b03942a3427132e
  evidence_ids:
  - ev-ceefc84dd27464ad
  - ev-40852c4b8e4f817b
  - ev-702e1b26f74fa1cf
  - ev-4b28b132ec221ca3
  - ev-41b7b72cded4e05c
  - ev-3f611fd20092d7d4
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-4b03942a3427132e
  evidence_ids:
  - ev-ceefc84dd27464ad
  - ev-9bd72ce41e674e19
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12
    and semantic review dispositions on HEAD.
  target_ids:
  - record-4b03942a3427132e
  evidence_ids:
  - ev-0eefc9d77ca437e5
  - ev-9bd72ce41e674e19
  - ev-28bce6da08c8c14e
  - ev-ff886fb7448948d4
  - ev-50f45c15b17c740a
evidence:
- evidence_id: ev-ceefc84dd27464ad
  kind: record_content
  reference: data/ingredients/mapped/Trace_Mineral_Solution.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2510],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:trace_mineral_solution","line":2512,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:trace_mineral_solution","preferred_term":"Trace
    mineral solution"}],"identifier":"kgmicrobe.ingredient:trace_mineral_solution","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:trace_mineral_solution","ontology_label":"Trace
    mineral solution","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Trace
    mineral solution","sssom_rows":[{"data_row":2809,"object_id":"kgmicrobe.ingredient:trace_mineral_solution","object_label":"Trace
    mineral solution","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Trace_Mineral_Solution","synonym_count":6}'
  snapshot_sha256: 03837875ebc88c1ab82387c244b383de83a01bc77f4fd60cd75fbbecdcd31f81
- evidence_id: ev-40852c4b8e4f817b
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2510]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-702e1b26f74fa1cf
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Trace_Mineral_Solution; data-row positions=[2809]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2809,"object_id":"kgmicrobe.ingredient:trace_mineral_solution","object_label":"Trace
    mineral solution","other":"Trace mineral solution (see Medium No. 151 )|Trace
    mineral solution (see Medium No. 852 )|Trace mineral solution (see Medium No.852)|Trace
    mineral solution (see below)|Trace mineral solution**","predicate_id":"skos:exactMatch","subject_id":"MIM:Trace_Mineral_Solution","validation_method":"none|UNKNOWN_TERM|2026-09-02"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-4b28b132ec221ca3
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2512]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:trace_mineral_solution","line":2512,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"2","ontology_id":"kgmicrobe.ingredient:trace_mineral_solution","preferred_term":"Trace
    mineral solution","total_occurrences":"2"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-0eefc9d77ca437e5
  kind: prior_review
  reference: reports/yaml_record_review/Trace_Mineral_Solution.md
  locator: '`data/ingredients/mapped/Trace_Mineral_Solution.yaml`:2; Verdict:4; Identity:9;
    Validation:21; Evidence:31; Issues:43; Major: recipe cross-references and footnotes
    reach final `other`:45; Completeness:53; Recommended Edits:61'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 95f2187e644085226dc05c4e6c0a2b3fc440fc600205141bc84c41b066625b34
  quote: "Issues:\n\n\nMajor: recipe cross-references and footnotes reach final `other`:\n\
    `Trace mineral solution (see Medium No. 151 )`, `Trace mineral solution (see\n\
    Medium No. 852 )`, `Trace mineral solution (see Medium No.852)`, `Trace\nmineral\
    \ solution (see below)`, and `Trace mineral solution**` are recipe-local\ninstructions\
    \ or footnoted surfaces. They are occurrence aliases, not true\nsynonyms of the\
    \ local stock identity, and should not be exported.\n\nRecommended Edits:\n- Mark\
    \ the five CultureMech aliases as non-exportable raw source text so the\n  final\
    \ SSSOM `other` column is empty for this row."
- evidence_id: ev-9bd72ce41e674e19
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1300]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"03837875ebc88c1ab82387c244b383de83a01bc77f4fd60cd75fbbecdcd31f81","finding_id":"SEM:7c1609d63523c7517ff0","kind":"existing_record_review","resolution_reason":"Historical
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
- evidence_id: ev-28bce6da08c8c14e
  kind: prior_review
  reference: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
  locator: findings[finding_id=f-54e5335934e0ba03]
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Exact earlier occurrence has open/confirmed status, based on exported-token
    presence and historical report text.
  snapshot_sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
  quote: '{"category": "nomenclature", "certainty": "confirmed", "description": "Historical
    tokens are still present on the exact-subject SSSOM rows: [{\"reason\":\"unresolved
    recipe cross-reference in a resolving synonym\",\"token\":\"Trace mineral solution
    (see Medium No. 151 )\"},{\"reason\":\"unresolved recipe cross-reference in a
    resolving synonym\",\"token\":\"Trace mineral solution (see Medium No.852)\"}].
    Truncated concentration strings and context-dependent instructions need scoped
    curation. This check does not reject catalog/RAW_TEXT synonyms as a class.", "evidence_ids":
    ["ev-0eefc9d77ca437e5", "ev-702e1b26f74fa1cf"], "external_issues": ["https://github.com/CultureBotAI/MediaIngredientMech/issues/718"],
    "field_paths": ["synonyms", "SSSOM.other"], "finding_id": "f-54e5335934e0ba03",
    "issue_key": "mim-reconciliation-exported-context-tokens-4b03942a3427132e", "owner_paths":
    [{"path": "data/ingredients/mapped/Trace_Mineral_Solution.yaml", "repository":
    "CultureBotAI/MediaIngredientMech", "role": "maintained ingredient"}], "severity":
    "major", "status": "open", "tags": ["reconciliation", "bundle-by-owner", "exported-context-tokens"],
    "target_ids": ["record-4b03942a3427132e"], "title": "Review nonportable exported
    tokens: Trace mineral solution"}'
- evidence_id: ev-41b7b72cded4e05c
  kind: record_content
  reference: data/ingredients/mapped/Trace_Mineral_Solution.yaml
  locator: identifier, ontology_mapping, synonyms and curation_history
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2510],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:trace_mineral_solution","line":2512,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:trace_mineral_solution","preferred_term":"Trace
    mineral solution"}],"identifier":"kgmicrobe.ingredient:trace_mineral_solution","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:trace_mineral_solution","ontology_label":"Trace
    mineral solution","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Trace
    mineral solution","sssom_rows":[{"data_row":2809,"object_id":"kgmicrobe.ingredient:trace_mineral_solution","object_label":"Trace
    mineral solution","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Trace_Mineral_Solution","synonym_count":6}'
  snapshot_sha256: 03837875ebc88c1ab82387c244b383de83a01bc77f4fd60cd75fbbecdcd31f81
- evidence_id: ev-3f611fd20092d7d4
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Trace_Mineral_Solution; data-row positions=[2809]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2809,"object_id":"kgmicrobe.ingredient:trace_mineral_solution","object_label":"Trace
    mineral solution","other":"Trace mineral solution (see Medium No. 151 )|Trace
    mineral solution (see Medium No. 852 )|Trace mineral solution (see Medium No.852)|Trace
    mineral solution (see below)|Trace mineral solution**","predicate_id":"skos:exactMatch","subject_id":"MIM:Trace_Mineral_Solution","validation_method":"none|UNKNOWN_TERM|2026-09-02"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-ff886fb7448948d4
  kind: prior_review
  reference: reports/yaml_record_review/Trace_Mineral_Solution.md
  locator: Complete historical report, including Verdict and Recommended Edits
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Historical interpretation was read in full; it is not fresh source adjudication.
  snapshot_sha256: 95f2187e644085226dc05c4e6c0a2b3fc440fc600205141bc84c41b066625b34
  quote: "# `data/ingredients/mapped/Trace_Mineral_Solution.yaml`\n\n## Verdict\n\n\
    Needs curation, major. The local stock-solution identity is synchronized, but\n\
    all five raw CultureMech note variants leak into final SSSOM `other`.\n\n## Identity\n\
    \n- Reviewed record: `data/ingredients/mapped/Trace_Mineral_Solution.yaml`.\n\
    - Identifier and grounding: `identifier:\n  kgmicrobe.ingredient:trace_mineral_solution`\
    \ with matching\n  `ontology_mapping.ontology_id`, label `Trace mineral solution`,\
    \ source\n  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,\n  `mapping_status:\
    \ MAPPED`, and `ingredient_type: STOCK_SOLUTION`.\n- Synonyms: raw mim-queue source\
    \ form plus five raw CultureMech forms carrying\n  `see Medium`, `see below`,\
    \ or double-asterisk recipe notes.\n- Occurrences: 2 CultureMech recipe occurrences\
    \ in 2 media.\n\n## Validation\n\n- `uv run --frozen python scripts/validate_strict.py`\
    \ on the 5-file batch from\n  `Trace_Mineral_Solution` through `Trans-aconitic_Acid`:\
    \ exited 0 and wrote\n  zero ERROR rows.\n- Direct old Engine A/OBO term validation\
    \ was skipped for this row because\n  `kgmicrobe.ingredient` is a non-OBO local\
    \ registry prefix.\n- Local aggregate comparison found this per-record file synchronized\
    \ with its\n  keyed row in `data/curated/mapped_ingredients.yaml`.\n\n## Evidence\n\
    \n- The August issue 288 curation minted a local `kgmicrobe.ingredient` identity\n\
    \  after searching ChEBI, NCIT, MeSH, FOODON, and ENVO and retaining no parent\n\
    \  because a generic trace-mineral solution is a named multi-component\n  preparation.\n\
    - The final SSSOM row has\n  `MIM:Trace_Mineral_Solution skos:exactMatch\n  kgmicrobe.ingredient:trace_mineral_solution`\
    \ and exports five raw\n  CultureMech labels in `other`, including Medium No.\
    \ 151, Medium No. 852,\n  `see below`, and double-asterisk variants.\n\n## Issues\n\
    \n### Major: recipe cross-references and footnotes reach final `other`\n\n`Trace\
    \ mineral solution (see Medium No. 151 )`, `Trace mineral solution (see\nMedium\
    \ No. 852 )`, `Trace mineral solution (see Medium No.852)`, `Trace\nmineral solution\
    \ (see below)`, and `Trace mineral solution**` are recipe-local\ninstructions\
    \ or footnoted surfaces. They are occurrence aliases, not true\nsynonyms of the\
    \ local stock identity, and should not be exported.\n\n## Completeness\n\n- The\
    \ local identity, fallback registry mapping, occurrence count, aggregate\n  copy,\
    \ and final exact row agree.\n- No roles, components, parent ontology rows, or\
    \ chemical properties are\n  asserted.\n- The only issue is the leaked raw CultureMech\
    \ aliases.\n\n## Recommended Edits\n\n- Mark the five CultureMech aliases as non-exportable\
    \ raw source text so the\n  final SSSOM `other` column is empty for this row.\n"
- evidence_id: ev-50f45c15b17c740a
  kind: prior_review
  reference: reviews/structured/20261011T030852Z-mim-token-scope-reassessment/review.yaml
  locator: findings[finding_id=scope-f-54e5335934e0ba03]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding scope-f-54e5335934e0ba03 in 20261011T030852Z-mim-token-scope-reassessment
  snapshot_sha256: 42a76b000bcbd07b426f6bad61b124b11ec08d8977783a67b732b01754f7c609
assessments:
- assessment_id: a-cfed618df75db194
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-4b03942a3427132e
  evidence_ids:
  - ev-ceefc84dd27464ad
  - ev-40852c4b8e4f817b
  - ev-702e1b26f74fa1cf
  - ev-4b28b132ec221ca3
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-bdb4172b81ca915c
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-4b03942a3427132e
  evidence_ids:
  - ev-0eefc9d77ca437e5
  - ev-ceefc84dd27464ad
  - ev-9bd72ce41e674e19
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T19:17:55Z;
    reviewed SHA-256=03837875ebc88c1ab82387c244b383de83a01bc77f4fd60cd75fbbecdcd31f81;
    current SHA-256=03837875ebc88c1ab82387c244b383de83a01bc77f4fd60cd75fbbecdcd31f81;
    hash_changed=False. Reports=["reports/yaml_record_review/Trace_Mineral_Solution.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    stock identity passes, but five see-Medium, see-below, or footnoted aliases leak
    into final SSSOM other.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0eefc9d77ca437e5
    - ev-ceefc84dd27464ad
  - name: legacy-native-ids
    value: '["SEM:7c1609d63523c7517ff0"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-ceefc84dd27464ad
    - ev-0eefc9d77ca437e5
    - ev-9bd72ce41e674e19
- assessment_id: a-3826bc410b6b89a6
  area: nomenclature
  topic: Unresolved recipe-reference or truncated-concentration synonyms
  outcome: concern
  summary: 'Historical tokens are still present on the exact-subject SSSOM rows: [{"reason":"unresolved
    recipe cross-reference in a resolving synonym","token":"Trace mineral solution
    (see Medium No. 151 )"},{"reason":"unresolved recipe cross-reference in a resolving
    synonym","token":"Trace mineral solution (see Medium No.852)"}]. Truncated concentration
    strings and context-dependent instructions need scoped curation. This check does
    not reject catalog/RAW_TEXT synonyms as a class.'
  target_ids:
  - record-4b03942a3427132e
  evidence_ids:
  - ev-0eefc9d77ca437e5
  - ev-702e1b26f74fa1cf
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0eefc9d77ca437e5
    - ev-702e1b26f74fa1cf
- assessment_id: scope-f-54e5335934e0ba03
  area: nomenclature
  topic: Certainty correction for the exact token observation
  outcome: unknown
  summary: Token presence remains reproducible, but the earlier pattern-based observation
    did not establish whether the exact source label denotes this subject or a different
    preparation. Fresh source-context adjudication is required before a confirmed
    defect or label removal. This successor corrects certainty only; it does not establish
    that the token is valid or that another identity allegation is fixed.
  target_ids:
  - record-4b03942a3427132e
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-28bce6da08c8c14e
  - ev-41b7b72cded4e05c
  - ev-3f611fd20092d7d4
  - ev-ff886fb7448948d4
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Source-scope question only, not a disposition of the complete historical
      report.
    evidence_ids:
    - ev-823412d1eacb6795
    - ev-28bce6da08c8c14e
    - ev-41b7b72cded4e05c
    - ev-3f611fd20092d7d4
    - ev-ff886fb7448948d4
findings:
- finding_id: rec-scope-f-54e5335934e0ba03
  issue_key: mim-reconciliation-exported-context-tokens-4b03942a3427132e
  category: nomenclature
  severity: major
  status: deferred
  certainty: provisional
  title: 'Adjudicate source scope of exported tokens: Trace mineral solution'
  description: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed.
  target_ids:
  - record-4b03942a3427132e
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-28bce6da08c8c14e
  - ev-41b7b72cded4e05c
  - ev-3f611fd20092d7d4
  - ev-ff886fb7448948d4
  - ev-50f45c15b17c740a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trace_Mineral_Solution.yaml
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
    finding_id: scope-f-54e5335934e0ba03
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
