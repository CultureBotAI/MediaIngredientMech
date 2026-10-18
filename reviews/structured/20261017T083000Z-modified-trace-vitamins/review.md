# Per-record structured review: Modified_Trace_Vitamins (data/ingredients/mapped/Modified_Trace_Vitamins.yaml)

- Review: 20261017T083000Z-modified-trace-vitamins
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Modified_Trace_Vitamins (data/ingredients/mapped/Modified_Trace_Vitamins.yaml, record-4253636d94bcf2f1, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Modified_Trace_Vitamins.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Modified_Trace_Vitamins.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-4253636d94bcf2f1 | data/ingredients/mapped/Modified_Trace_Vitamins.yaml | maintained | Modified_Trace_Vitamins |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-4253636d94bcf2f1 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-4253636d94bcf2f1 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-4253636d94bcf2f1 | Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-4253636d94bcf2f1.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-4253636d94bcf2f1.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T03:47:06Z; reviewed SHA-256=4eedaddb0efbc29c6dead6ef2bd378ec59070ecea3146b66e77bcea55a204a2c; current SHA-256=4eedaddb0efbc29c6dead6ef2bd378ec59070ecea3146b66e77bcea55a204a2c; hash_changed=False. Reports=["reports/yaml_record_review/Modified_Trace_Vitamins.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local Modified trace vitamins stock identity, occurrence count, fallback registry mapping, and final exact row pass, but see-below recipe text still publishes in final SSSOM other.

### Unresolved recipe-reference or truncated-concentration synonyms

nomenclature: concern. Targets: record-4253636d94bcf2f1.

Historical tokens are still present on the exact-subject SSSOM rows: [{"reason":"unresolved recipe cross-reference in a resolving synonym","token":"Modified trace vitamins (see below)"}]. Truncated concentration strings and context-dependent instructions need scoped curation. This check does not reject catalog/RAW_TEXT synonyms as a class.

### Certainty correction for the exact token observation

nomenclature: unknown. Targets: record-4253636d94bcf2f1.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

## Findings

### rec-scope-f-d3696f2daf45c433: Adjudicate source scope of exported tokens: Modified trace vitamins

major / deferred / provisional; issue key: mim-reconciliation-exported-context-tokens-4253636d94bcf2f1.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

Disposition: Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-4c2dd24bad57632f | data/ingredients/mapped/Modified_Trace_Vitamins.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2498],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:modified_trace_vitamins","line":2500,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:modified_trace_vitamins","preferred_term":"Modified trace vitamins"}],"identifier":"kgmicrobe.ingredient:modified_trace_vitamins","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:modified_trace_vitamins","ontology_label":"Modified trace vitamins","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Modified trace vitamins","sssom_rows":[{"data_row":1905,"object_id":"kgmicrobe.ingredient:modified_trace_vitamins","object_label":"Modified trace vitamins","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Modified_Trace_Vitamins","synonym_count":2} |
| ev-ad1fd681bfcacb06 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2498] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-e485d8da83247c1c | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Modified_Trace_Vitamins; data-row positions=[1905] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1905,"object_id":"kgmicrobe.ingredient:modified_trace_vitamins","object_label":"Modified trace vitamins","other":"Modified trace vitamins (see below)","predicate_id":"skos:exactMatch","subject_id":"MIM:Modified_Trace_Vitamins","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-09-02"}] |
| ev-5f1ad78384afb238 | docs/data/mapped_ingredients.csv; CSV lines=[2500] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:modified_trace_vitamins","line":2500,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"2","ontology_id":"kgmicrobe.ingredient:modified_trace_vitamins","preferred_term":"Modified trace vitamins","total_occurrences":"2"}] |
| ev-a8586fb48ab7ffa9 | reports/yaml_record_review/Modified_Trace_Vitamins.md; &#96;data/ingredients/mapped/Modified_Trace_Vitamins.yaml&#96;:2; Verdict:4; Identity:12; Validation:23; Evidence:32; Completeness:43; Recommended Edits:50 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-342517d22b716860 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[954] | context_only | [{"current_record_sha256":"4eedaddb0efbc29c6dead6ef2bd378ec59070ecea3146b66e77bcea55a204a2c","finding_id":"SEM:b336554c878b13b4f95b","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-823412d1eacb6795 | MAPPING_SEMANTICS.md; Sections on REJECTED_LABEL and the damaged-label RAW_TEXT carve-out | supports | Raw spellings may remain resolvable when they denote the same substance. Wrong-identity labels must not resolve. A recipe-pointer pattern alone does not adjudicate that distinction. |
| ev-a1a7bf32cb2806bb | reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml; findings[finding_id=f-d3696f2daf45c433] | context_only | Exact earlier occurrence has open/confirmed status, based on exported-token presence and historical report text. |
| ev-5830b871d91efa8c | data/ingredients/mapped/Modified_Trace_Vitamins.yaml; identifier, ontology_mapping, synonyms and curation_history | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2498],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:modified_trace_vitamins","line":2500,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:modified_trace_vitamins","preferred_term":"Modified trace vitamins"}],"identifier":"kgmicrobe.ingredient:modified_trace_vitamins","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:modified_trace_vitamins","ontology_label":"Modified trace vitamins","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Modified trace vitamins","sssom_rows":[{"data_row":1905,"object_id":"kgmicrobe.ingredient:modified_trace_vitamins","object_label":"Modified trace vitamins","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Modified_Trace_Vitamins","synonym_count":2} |
| ev-7c6192e7f288bdf0 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Modified_Trace_Vitamins; data-row positions=[1905] | supports | Current exact-subject rows, including complete other payload: [{"data_row":1905,"object_id":"kgmicrobe.ingredient:modified_trace_vitamins","object_label":"Modified trace vitamins","other":"Modified trace vitamins (see below)","predicate_id":"skos:exactMatch","subject_id":"MIM:Modified_Trace_Vitamins","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-09-02"}] |
| ev-1659306e55f45a0b | reports/yaml_record_review/Modified_Trace_Vitamins.md; Complete historical report, including Verdict and Recommended Edits | context_only | Historical interpretation was read in full; it is not fresh source adjudication. |
| ev-9d36fb33365bc628 | reviews/structured/20261011T030852Z-mim-token-scope-reassessment/review.yaml; findings[finding_id=scope-f-d3696f2daf45c433] | context_only | Predecessor structured review finding scope-f-d3696f2daf45c433 in 20261011T030852Z-mim-token-scope-reassessment |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024636Z-mim-reconcile-all-batch-08, 20261011T030852Z-mim-token-scope-reassessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-modified-trace-vitamins
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Modified_Trace_Vitamins (data/ingredients/mapped/Modified_Trace_Vitamins.yaml)'
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
summary: Per-record structured review for Modified_Trace_Vitamins (data/ingredients/mapped/Modified_Trace_Vitamins.yaml,
  record-4253636d94bcf2f1, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Modified_Trace_Vitamins.yaml
    sha256: 4eedaddb0efbc29c6dead6ef2bd378ec59070ecea3146b66e77bcea55a204a2c
    role: target
  - path: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
    sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
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
  - path: reports/yaml_record_review/Modified_Trace_Vitamins.md
    sha256: 1bfc880ed06f1c6448af8e81cef6be73c4e8dfc3230d00e4ab8241c3de76ee7d
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
  - path: MAPPING_SEMANTICS.md
    sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805
    role: context
targets:
- target_id: record-4253636d94bcf2f1
  path: data/ingredients/mapped/Modified_Trace_Vitamins.yaml
  label: Modified_Trace_Vitamins
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Modified_Trace_Vitamins.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Modified_Trace_Vitamins.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Modified_Trace_Vitamins.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-4253636d94bcf2f1
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-4253636d94bcf2f1
  evidence_ids:
  - ev-4c2dd24bad57632f
  - ev-ad1fd681bfcacb06
  - ev-e485d8da83247c1c
  - ev-5f1ad78384afb238
  - ev-5830b871d91efa8c
  - ev-7c6192e7f288bdf0
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-4253636d94bcf2f1
  evidence_ids:
  - ev-4c2dd24bad57632f
  - ev-342517d22b716860
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08
    and semantic review dispositions on HEAD.
  target_ids:
  - record-4253636d94bcf2f1
  evidence_ids:
  - ev-a8586fb48ab7ffa9
  - ev-342517d22b716860
  - ev-a1a7bf32cb2806bb
  - ev-1659306e55f45a0b
  - ev-9d36fb33365bc628
evidence:
- evidence_id: ev-4c2dd24bad57632f
  kind: record_content
  reference: data/ingredients/mapped/Modified_Trace_Vitamins.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2498],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:modified_trace_vitamins","line":2500,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:modified_trace_vitamins","preferred_term":"Modified
    trace vitamins"}],"identifier":"kgmicrobe.ingredient:modified_trace_vitamins","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:modified_trace_vitamins","ontology_label":"Modified
    trace vitamins","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Modified
    trace vitamins","sssom_rows":[{"data_row":1905,"object_id":"kgmicrobe.ingredient:modified_trace_vitamins","object_label":"Modified
    trace vitamins","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Modified_Trace_Vitamins","synonym_count":2}'
  snapshot_sha256: 4eedaddb0efbc29c6dead6ef2bd378ec59070ecea3146b66e77bcea55a204a2c
- evidence_id: ev-ad1fd681bfcacb06
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2498]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-e485d8da83247c1c
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Modified_Trace_Vitamins; data-row positions=[1905]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1905,"object_id":"kgmicrobe.ingredient:modified_trace_vitamins","object_label":"Modified
    trace vitamins","other":"Modified trace vitamins (see below)","predicate_id":"skos:exactMatch","subject_id":"MIM:Modified_Trace_Vitamins","validation_method":"none|UNKNOWN_TERM|2026-09-02"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-5f1ad78384afb238
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2500]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:modified_trace_vitamins","line":2500,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"2","ontology_id":"kgmicrobe.ingredient:modified_trace_vitamins","preferred_term":"Modified
    trace vitamins","total_occurrences":"2"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-a8586fb48ab7ffa9
  kind: prior_review
  reference: reports/yaml_record_review/Modified_Trace_Vitamins.md
  locator: '`data/ingredients/mapped/Modified_Trace_Vitamins.yaml`:2; Verdict:4; Identity:12;
    Validation:23; Evidence:32; Completeness:43; Recommended Edits:50'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 1bfc880ed06f1c6448af8e81cef6be73c4e8dfc3230d00e4ab8241c3de76ee7d
  quote: "Recommended Edits:\n- Major: mark `Modified trace vitamins (see below)`\
    \ as `REJECTED_LABEL`, or\n  otherwise preserve it only as a resolver alias while\
    \ filtering it from final\n  SSSOM `other`."
- evidence_id: ev-342517d22b716860
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[954]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"4eedaddb0efbc29c6dead6ef2bd378ec59070ecea3146b66e77bcea55a204a2c","finding_id":"SEM:b336554c878b13b4f95b","kind":"existing_record_review","resolution_reason":"Historical
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
- evidence_id: ev-a1a7bf32cb2806bb
  kind: prior_review
  reference: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
  locator: findings[finding_id=f-d3696f2daf45c433]
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Exact earlier occurrence has open/confirmed status, based on exported-token
    presence and historical report text.
  snapshot_sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
  quote: '{"category": "nomenclature", "certainty": "confirmed", "description": "Historical
    tokens are still present on the exact-subject SSSOM rows: [{\"reason\":\"unresolved
    recipe cross-reference in a resolving synonym\",\"token\":\"Modified trace vitamins
    (see below)\"}]. Truncated concentration strings and context-dependent instructions
    need scoped curation. This check does not reject catalog/RAW_TEXT synonyms as
    a class.", "evidence_ids": ["ev-a8586fb48ab7ffa9", "ev-e485d8da83247c1c"], "external_issues":
    ["https://github.com/CultureBotAI/MediaIngredientMech/issues/718"], "field_paths":
    ["synonyms", "SSSOM.other"], "finding_id": "f-d3696f2daf45c433", "issue_key":
    "mim-reconciliation-exported-context-tokens-4253636d94bcf2f1", "owner_paths":
    [{"path": "data/ingredients/mapped/Modified_Trace_Vitamins.yaml", "repository":
    "CultureBotAI/MediaIngredientMech", "role": "maintained ingredient"}], "severity":
    "major", "status": "open", "tags": ["reconciliation", "bundle-by-owner", "exported-context-tokens"],
    "target_ids": ["record-4253636d94bcf2f1"], "title": "Review nonportable exported
    tokens: Modified trace vitamins"}'
- evidence_id: ev-5830b871d91efa8c
  kind: record_content
  reference: data/ingredients/mapped/Modified_Trace_Vitamins.yaml
  locator: identifier, ontology_mapping, synonyms and curation_history
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2498],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:modified_trace_vitamins","line":2500,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:modified_trace_vitamins","preferred_term":"Modified
    trace vitamins"}],"identifier":"kgmicrobe.ingredient:modified_trace_vitamins","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:modified_trace_vitamins","ontology_label":"Modified
    trace vitamins","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Modified
    trace vitamins","sssom_rows":[{"data_row":1905,"object_id":"kgmicrobe.ingredient:modified_trace_vitamins","object_label":"Modified
    trace vitamins","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Modified_Trace_Vitamins","synonym_count":2}'
  snapshot_sha256: 4eedaddb0efbc29c6dead6ef2bd378ec59070ecea3146b66e77bcea55a204a2c
- evidence_id: ev-7c6192e7f288bdf0
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Modified_Trace_Vitamins; data-row positions=[1905]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1905,"object_id":"kgmicrobe.ingredient:modified_trace_vitamins","object_label":"Modified
    trace vitamins","other":"Modified trace vitamins (see below)","predicate_id":"skos:exactMatch","subject_id":"MIM:Modified_Trace_Vitamins","validation_method":"none|UNKNOWN_TERM|2026-09-02"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-1659306e55f45a0b
  kind: prior_review
  reference: reports/yaml_record_review/Modified_Trace_Vitamins.md
  locator: Complete historical report, including Verdict and Recommended Edits
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Historical interpretation was read in full; it is not fresh source adjudication.
  snapshot_sha256: 1bfc880ed06f1c6448af8e81cef6be73c4e8dfc3230d00e4ab8241c3de76ee7d
  quote: "# `data/ingredients/mapped/Modified_Trace_Vitamins.yaml`\n\n## Verdict\n\
    \nNeeds curation. The local Modified trace vitamins stock identity, occurrence\n\
    count, fallback registry mapping, and final exact row pass, but `see below`\n\
    recipe text still publishes in final SSSOM `other`.\n\nSeverity: major.\n\n##\
    \ Identity\n\n- Reviewed record: `data/ingredients/mapped/Modified_Trace_Vitamins.yaml`.\n\
    - Identifier and grounding:\n  `identifier: kgmicrobe.ingredient:modified_trace_vitamins`\
    \ with\n  `ontology_mapping.ontology_id:\n  kgmicrobe.ingredient:modified_trace_vitamins`,\
    \ source\n  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,\n  `mapping_status:\
    \ MAPPED`, and `ingredient_type: STOCK_SOLUTION`.\n- Occurrences: two CultureMech\
    \ recipe occurrences.\n\n## Validation\n\n- `uv run --frozen python scripts/validate_strict.py`\
    \ on the 5-file batch from\n  `Mnso4_X_7_H2o` through `Modified_Trace_Vitamins`:\
    \ exited 0 and wrote zero\n  ERROR rows.\n- Direct Engine A term validation was\
    \ skipped for this local registry record\n  because its primary `kgmicrobe.ingredient`\
    \ identifier is outside the OBO\n  subset used for the batch.\n\n## Evidence\n\
    \n- `mappings/unmapped_ingredients_ols_exact_audit.tsv` recorded no exact OLS\
    \ hit\n  before the fallback registry promotion.\n- #288 curation kept this as\
    \ a local mint because the label denotes a named\n  multi-component vitamin preparation\
    \ rather than an external ontology\n  substance.\n- A fresh exact EBI OLS4 lookup\
    \ returned no same-label external class.\n- The final SSSOM publishes one `skos:exactMatch`\
    \ row from\n  `MIM:Modified_Trace_Vitamins` to the local registry identifier.\n\
    \n## Completeness\n\n- The local stock identity, 2/2 occurrence count, fallback\
    \ registry rationale,\n  and final exact row agree.\n- The final SSSOM `other`\
    \ field still exports `Modified trace vitamins (see\n  below)`, which is recipe\
    \ navigation text rather than a clean synonym.\n\n## Recommended Edits\n\n- Major:\
    \ mark `Modified trace vitamins (see below)` as `REJECTED_LABEL`, or\n  otherwise\
    \ preserve it only as a resolver alias while filtering it from final\n  SSSOM\
    \ `other`.\n"
- evidence_id: ev-9d36fb33365bc628
  kind: prior_review
  reference: reviews/structured/20261011T030852Z-mim-token-scope-reassessment/review.yaml
  locator: findings[finding_id=scope-f-d3696f2daf45c433]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding scope-f-d3696f2daf45c433 in 20261011T030852Z-mim-token-scope-reassessment
  snapshot_sha256: 42a76b000bcbd07b426f6bad61b124b11ec08d8977783a67b732b01754f7c609
assessments:
- assessment_id: a-05517998b34667d8
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-4253636d94bcf2f1
  evidence_ids:
  - ev-4c2dd24bad57632f
  - ev-ad1fd681bfcacb06
  - ev-e485d8da83247c1c
  - ev-5f1ad78384afb238
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-73c771b3b3c783fb
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-4253636d94bcf2f1
  evidence_ids:
  - ev-a8586fb48ab7ffa9
  - ev-4c2dd24bad57632f
  - ev-342517d22b716860
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T03:47:06Z;
    reviewed SHA-256=4eedaddb0efbc29c6dead6ef2bd378ec59070ecea3146b66e77bcea55a204a2c;
    current SHA-256=4eedaddb0efbc29c6dead6ef2bd378ec59070ecea3146b66e77bcea55a204a2c;
    hash_changed=False. Reports=["reports/yaml_record_review/Modified_Trace_Vitamins.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    Modified trace vitamins stock identity, occurrence count, fallback registry mapping,
    and final exact row pass, but see-below recipe text still publishes in final SSSOM
    other.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-a8586fb48ab7ffa9
    - ev-4c2dd24bad57632f
  - name: legacy-native-ids
    value: '["SEM:b336554c878b13b4f95b"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-4c2dd24bad57632f
    - ev-a8586fb48ab7ffa9
    - ev-342517d22b716860
- assessment_id: a-de905dce6f8aa98c
  area: nomenclature
  topic: Unresolved recipe-reference or truncated-concentration synonyms
  outcome: concern
  summary: 'Historical tokens are still present on the exact-subject SSSOM rows: [{"reason":"unresolved
    recipe cross-reference in a resolving synonym","token":"Modified trace vitamins
    (see below)"}]. Truncated concentration strings and context-dependent instructions
    need scoped curation. This check does not reject catalog/RAW_TEXT synonyms as
    a class.'
  target_ids:
  - record-4253636d94bcf2f1
  evidence_ids:
  - ev-a8586fb48ab7ffa9
  - ev-e485d8da83247c1c
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-a8586fb48ab7ffa9
    - ev-e485d8da83247c1c
- assessment_id: scope-f-d3696f2daf45c433
  area: nomenclature
  topic: Certainty correction for the exact token observation
  outcome: unknown
  summary: Token presence remains reproducible, but the earlier pattern-based observation
    did not establish whether the exact source label denotes this subject or a different
    preparation. Fresh source-context adjudication is required before a confirmed
    defect or label removal. This successor corrects certainty only; it does not establish
    that the token is valid or that another identity allegation is fixed.
  target_ids:
  - record-4253636d94bcf2f1
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-a1a7bf32cb2806bb
  - ev-5830b871d91efa8c
  - ev-7c6192e7f288bdf0
  - ev-1659306e55f45a0b
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Source-scope question only, not a disposition of the complete historical
      report.
    evidence_ids:
    - ev-823412d1eacb6795
    - ev-a1a7bf32cb2806bb
    - ev-5830b871d91efa8c
    - ev-7c6192e7f288bdf0
    - ev-1659306e55f45a0b
findings:
- finding_id: rec-scope-f-d3696f2daf45c433
  issue_key: mim-reconciliation-exported-context-tokens-4253636d94bcf2f1
  category: nomenclature
  severity: major
  status: deferred
  certainty: provisional
  title: 'Adjudicate source scope of exported tokens: Modified trace vitamins'
  description: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed.
  target_ids:
  - record-4253636d94bcf2f1
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-a1a7bf32cb2806bb
  - ev-5830b871d91efa8c
  - ev-7c6192e7f288bdf0
  - ev-1659306e55f45a0b
  - ev-9d36fb33365bc628
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Modified_Trace_Vitamins.yaml
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
    finding_id: scope-f-d3696f2daf45c433
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
  with lineage to 20261011T024636Z-mim-reconcile-all-batch-08, 20261011T030852Z-mim-token-scope-reassessment.
```
