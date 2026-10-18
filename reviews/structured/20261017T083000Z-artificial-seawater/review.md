# Per-record structured review: Artificial_seawater (data/ingredients/mapped/Artificial_seawater.yaml)

- Review: 20261017T083000Z-artificial-seawater
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Artificial_seawater (data/ingredients/mapped/Artificial_seawater.yaml, record-205c79d137874075, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Artificial_seawater.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Artificial_seawater.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-205c79d137874075 | data/ingredients/mapped/Artificial_seawater.yaml | maintained | Artificial_seawater |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-205c79d137874075 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-205c79d137874075 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-205c79d137874075 | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-205c79d137874075.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: not_applicable. Targets: record-205c79d137874075.

The latest legacy review reports no outstanding finding. This run verifies local consistency only; it does not renew that earlier scientific pass.

Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-16T08:44:30Z; reviewed SHA-256=9efeac859a634d9d5daf17c7da4e058b51ce7538b0b802fa6ac2b7f6f602e708; current SHA-256=9efeac859a634d9d5daf17c7da4e058b51ce7538b0b802fa6ac2b7f6f602e708; hash_changed=False. Reports=["reports/yaml_record_review/Artificial_seawater.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CultureMech residual record exact-maps to MICRO artificial seawater and keeps parenthetical recipe labels only as raw source surfaces.

### Unresolved recipe-reference or truncated-concentration synonyms

nomenclature: concern. Targets: record-205c79d137874075.

Historical tokens are still present on the exact-subject SSSOM rows: [{"reason":"unresolved recipe cross-reference in a resolving synonym","token":"Artificial seawater (see Medium No. 736 )"},{"reason":"unresolved recipe cross-reference in a resolving synonym","token":"Artificial seawater (see below)"}]. Truncated concentration strings and context-dependent instructions need scoped curation. This check does not reject catalog/RAW_TEXT synonyms as a class.

### Certainty correction for the exact token observation

nomenclature: unknown. Targets: record-205c79d137874075.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed. The historical report actually passes the record and explicitly accepts the raw source surface; attributing an unresolved token concern to that report was incorrect. No new source evidence was supplied to overturn its scoped conclusion.

## Findings

### rec-scope-f-e1004757f90e8c13: Adjudicate source scope of exported tokens: Artificial seawater

major / deferred / provisional; issue key: mim-reconciliation-exported-context-tokens-205c79d137874075.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed. The historical report actually passes the record and explicitly accepts the raw source surface; attributing an unresolved token concern to that report was incorrect. No new source evidence was supplied to overturn its scoped conclusion.

Disposition: Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed. The historical report actually passes the record and explicitly accepts the raw source surface; attributing an unresolved token concern to that report was incorrect. No new source evidence was supplied to overturn its scoped conclusion.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-ff32a7302db1eb17 | data/ingredients/mapped/Artificial_seawater.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2537],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0001715","line":2539,"mapping_status":"MAPPED","ontology_id":"MICRO:0001715","preferred_term":"Artificial seawater"}],"identifier":"MICRO:0001715","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":19,"total_occurrences":19},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"MICRO:0001715","ontology_label":"artificial seawater","ontology_source":"MICRO"},"preferred_term":"Artificial seawater","sssom_rows":[{"data_row":435,"object_id":"MICRO:0001715","object_label":"artificial seawater","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Artificial_seawater","synonym_count":2} |
| ev-6518654aed992338 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2537] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-91c2182d00c37a4a | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Artificial_seawater; data-row positions=[435] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":435,"object_id":"MICRO:0001715","object_label":"artificial seawater","other":"Artificial seawater (see below)&#124;Artificial seawater (see Medium No. 736 )","predicate_id":"skos:exactMatch","subject_id":"MIM:Artificial_seawater","validation_method":"manual:claude_culturemech_residual_grounding&#124;CREATED&#124;2026-08-30"}] |
| ev-6a7f27c85a59a50e | docs/data/mapped_ingredients.csv; CSV lines=[2539] | supports | Published identity and count rows inspected: [{"identifier":"MICRO:0001715","line":2539,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"19","ontology_id":"MICRO:0001715","preferred_term":"Artificial seawater","total_occurrences":"19"}] |
| ev-a3370b8d14b4ebe5 | reports/yaml_record_review/Artificial_seawater.md; &#96;data/ingredients/mapped/Artificial_seawater.yaml&#96;:2; Verdict:4; Identity:9; Validation:22; Evidence:43; Completeness:57; Recommended Edits:66 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-823412d1eacb6795 | MAPPING_SEMANTICS.md; Sections on REJECTED_LABEL and the damaged-label RAW_TEXT carve-out | supports | Raw spellings may remain resolvable when they denote the same substance. Wrong-identity labels must not resolve. A recipe-pointer pattern alone does not adjudicate that distinction. |
| ev-8fab9fb02ee4454f | reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml; findings[finding_id=f-e1004757f90e8c13] | context_only | Exact earlier occurrence has open/confirmed status, based on exported-token presence and historical report text. |
| ev-f5500c887f4dc734 | data/ingredients/mapped/Artificial_seawater.yaml; identifier, ontology_mapping, synonyms and curation_history | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2537],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0001715","line":2539,"mapping_status":"MAPPED","ontology_id":"MICRO:0001715","preferred_term":"Artificial seawater"}],"identifier":"MICRO:0001715","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":19,"total_occurrences":19},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"MICRO:0001715","ontology_label":"artificial seawater","ontology_source":"MICRO"},"preferred_term":"Artificial seawater","sssom_rows":[{"data_row":435,"object_id":"MICRO:0001715","object_label":"artificial seawater","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Artificial_seawater","synonym_count":2} |
| ev-16c562c2dbdbab95 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Artificial_seawater; data-row positions=[435] | supports | Current exact-subject rows, including complete other payload: [{"data_row":435,"object_id":"MICRO:0001715","object_label":"artificial seawater","other":"Artificial seawater (see below)&#124;Artificial seawater (see Medium No. 736 )","predicate_id":"skos:exactMatch","subject_id":"MIM:Artificial_seawater","validation_method":"manual:claude_culturemech_residual_grounding&#124;CREATED&#124;2026-08-30"}] |
| ev-8ca93b32516cbb52 | reports/yaml_record_review/Artificial_seawater.md; Complete historical report, including Verdict and Recommended Edits | context_only | Historical interpretation was read in full; it is not fresh source adjudication. |
| ev-c0ba3a9bc4c527b7 | reviews/structured/20261011T030852Z-mim-token-scope-reassessment/review.yaml; findings[finding_id=scope-f-e1004757f90e8c13] | context_only | Predecessor structured review finding scope-f-e1004757f90e8c13 in 20261011T030852Z-mim-token-scope-reassessment |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03, 20261011T030852Z-mim-token-scope-reassessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-artificial-seawater
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Artificial_seawater (data/ingredients/mapped/Artificial_seawater.yaml)'
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
summary: Per-record structured review for Artificial_seawater (data/ingredients/mapped/Artificial_seawater.yaml,
  record-205c79d137874075, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Artificial_seawater.yaml
    sha256: 9efeac859a634d9d5daf17c7da4e058b51ce7538b0b802fa6ac2b7f6f602e708
    role: target
  - path: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
    sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
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
  - path: reports/yaml_record_review/Artificial_seawater.md
    sha256: 678c1882c36eb0a94f762d006e36deb3a61b751b7d424573a723abe497e8c936
    role: context
  - path: MAPPING_SEMANTICS.md
    sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805
    role: context
targets:
- target_id: record-205c79d137874075
  path: data/ingredients/mapped/Artificial_seawater.yaml
  label: Artificial_seawater
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Artificial_seawater.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Artificial_seawater.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Artificial_seawater.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-205c79d137874075
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-205c79d137874075
  evidence_ids:
  - ev-ff32a7302db1eb17
  - ev-6518654aed992338
  - ev-91c2182d00c37a4a
  - ev-6a7f27c85a59a50e
  - ev-f5500c887f4dc734
  - ev-16c562c2dbdbab95
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-205c79d137874075
  evidence_ids:
  - ev-ff32a7302db1eb17
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-205c79d137874075
  evidence_ids:
  - ev-a3370b8d14b4ebe5
  - ev-8fab9fb02ee4454f
  - ev-8ca93b32516cbb52
  - ev-c0ba3a9bc4c527b7
evidence:
- evidence_id: ev-ff32a7302db1eb17
  kind: record_content
  reference: data/ingredients/mapped/Artificial_seawater.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2537],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0001715","line":2539,"mapping_status":"MAPPED","ontology_id":"MICRO:0001715","preferred_term":"Artificial
    seawater"}],"identifier":"MICRO:0001715","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":19,"total_occurrences":19},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"MICRO:0001715","ontology_label":"artificial
    seawater","ontology_source":"MICRO"},"preferred_term":"Artificial seawater","sssom_rows":[{"data_row":435,"object_id":"MICRO:0001715","object_label":"artificial
    seawater","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Artificial_seawater","synonym_count":2}'
  snapshot_sha256: 9efeac859a634d9d5daf17c7da4e058b51ce7538b0b802fa6ac2b7f6f602e708
- evidence_id: ev-6518654aed992338
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2537]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-91c2182d00c37a4a
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Artificial_seawater; data-row positions=[435]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":435,"object_id":"MICRO:0001715","object_label":"artificial
    seawater","other":"Artificial seawater (see below)|Artificial seawater (see Medium
    No. 736 )","predicate_id":"skos:exactMatch","subject_id":"MIM:Artificial_seawater","validation_method":"manual:claude_culturemech_residual_grounding|CREATED|2026-08-30"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-6a7f27c85a59a50e
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2539]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"MICRO:0001715","line":2539,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"19","ontology_id":"MICRO:0001715","preferred_term":"Artificial
    seawater","total_occurrences":"19"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-a3370b8d14b4ebe5
  kind: prior_review
  reference: reports/yaml_record_review/Artificial_seawater.md
  locator: '`data/ingredients/mapped/Artificial_seawater.yaml`:2; Verdict:4; Identity:9;
    Validation:22; Evidence:43; Completeness:57; Recommended Edits:66'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 678c1882c36eb0a94f762d006e36deb3a61b751b7d424573a723abe497e8c936
  quote: 'Recommended Edits:

    - None.'
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
- evidence_id: ev-8fab9fb02ee4454f
  kind: prior_review
  reference: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
  locator: findings[finding_id=f-e1004757f90e8c13]
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Exact earlier occurrence has open/confirmed status, based on exported-token
    presence and historical report text.
  snapshot_sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
  quote: '{"category": "nomenclature", "certainty": "confirmed", "description": "Historical
    tokens are still present on the exact-subject SSSOM rows: [{\"reason\":\"unresolved
    recipe cross-reference in a resolving synonym\",\"token\":\"Artificial seawater
    (see Medium No. 736 )\"},{\"reason\":\"unresolved recipe cross-reference in a
    resolving synonym\",\"token\":\"Artificial seawater (see below)\"}]. Truncated
    concentration strings and context-dependent instructions need scoped curation.
    This check does not reject catalog/RAW_TEXT synonyms as a class.", "evidence_ids":
    ["ev-a3370b8d14b4ebe5", "ev-91c2182d00c37a4a"], "external_issues": ["https://github.com/CultureBotAI/MediaIngredientMech/issues/718"],
    "field_paths": ["synonyms", "SSSOM.other"], "finding_id": "f-e1004757f90e8c13",
    "issue_key": "mim-reconciliation-exported-context-tokens-205c79d137874075", "owner_paths":
    [{"path": "data/ingredients/mapped/Artificial_seawater.yaml", "repository": "CultureBotAI/MediaIngredientMech",
    "role": "maintained ingredient"}], "severity": "major", "status": "open", "tags":
    ["reconciliation", "bundle-by-owner", "exported-context-tokens"], "target_ids":
    ["record-205c79d137874075"], "title": "Review nonportable exported tokens: Artificial
    seawater"}'
- evidence_id: ev-f5500c887f4dc734
  kind: record_content
  reference: data/ingredients/mapped/Artificial_seawater.yaml
  locator: identifier, ontology_mapping, synonyms and curation_history
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2537],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0001715","line":2539,"mapping_status":"MAPPED","ontology_id":"MICRO:0001715","preferred_term":"Artificial
    seawater"}],"identifier":"MICRO:0001715","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":19,"total_occurrences":19},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"MICRO:0001715","ontology_label":"artificial
    seawater","ontology_source":"MICRO"},"preferred_term":"Artificial seawater","sssom_rows":[{"data_row":435,"object_id":"MICRO:0001715","object_label":"artificial
    seawater","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Artificial_seawater","synonym_count":2}'
  snapshot_sha256: 9efeac859a634d9d5daf17c7da4e058b51ce7538b0b802fa6ac2b7f6f602e708
- evidence_id: ev-16c562c2dbdbab95
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Artificial_seawater; data-row positions=[435]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":435,"object_id":"MICRO:0001715","object_label":"artificial
    seawater","other":"Artificial seawater (see below)|Artificial seawater (see Medium
    No. 736 )","predicate_id":"skos:exactMatch","subject_id":"MIM:Artificial_seawater","validation_method":"manual:claude_culturemech_residual_grounding|CREATED|2026-08-30"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-8ca93b32516cbb52
  kind: prior_review
  reference: reports/yaml_record_review/Artificial_seawater.md
  locator: Complete historical report, including Verdict and Recommended Edits
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Historical interpretation was read in full; it is not fresh source adjudication.
  snapshot_sha256: 678c1882c36eb0a94f762d006e36deb3a61b751b7d424573a723abe497e8c936
  quote: "# `data/ingredients/mapped/Artificial_seawater.yaml`\n\n## Verdict\n\nPass.\
    \ The record exactly denotes MICRO `artificial seawater`, and its raw\nCultureMech\
    \ variants are retained only as source surface forms.\n\n## Identity\n\n- Reviewed\
    \ record: `data/ingredients/mapped/Artificial_seawater.yaml`.\n- Identifier and\
    \ grounding: `identifier: MICRO:0001715` with\n  `ontology_mapping.ontology_id:\
    \ MICRO:0001715`, `ontology_source: MICRO`,\n  `mapping_quality: EXACT_MATCH`,\
    \ `match_level: EXACT`, and\n  `mapping_status: MAPPED`.\n- OLS resolves `MICRO:0001715`\
    \ to non-obsolete `artificial seawater` with a\n  definition for an inorganic\
    \ salts solution that mimics sea water and the\n  exact synonym `synthetic seawater`.\n\
    - The two synonyms are raw CultureMech labels with parenthetical recipe\n  navigation\
    \ text; they are not asserted as exact ontology aliases.\n\n## Validation\n\n\
    - `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Arsenate.yaml\
    \ data/ingredients/mapped/Artepaulin.yaml data/ingredients/mapped/Artificial_Sea_Salt.yaml\
    \ data/ingredients/mapped/Artificial_seawater.yaml data/ingredients/mapped/Ascomycin.yaml`:\n\
    \  passed; 5 files scanned, 0 ERROR rows.\n- `uv run linkml-term-validator validate-data\
    \ data/ingredients/mapped/Artificial_seawater.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml\
    \ -t IngredientRecord --labels`:\n  failed in the MICRO sqlite adapter with `sqlite3.OperationalError:\
    \ no such\n  table: rdfs_label_statement`. This matches the repository contract:\n\
    \  `just validate-terms` skips MICRO and leaves it to Engine B/product\n  validation\
    \ or explicit OLS checks.\n- OLS4 lookup for `MICRO:0001715`: resolved the exact\
    \ stored term and label.\n- `uv run --frozen python scripts/validate_component_partonomy.py`:\
    \ passed;\n  2951 records, 83 decompositions, 505 components, 0 violations.\n\
    - `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules\n\
    \  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because\n\
    \  the sibling kg-microbe ontology transforms were absent.\n- `uv run --frozen\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:\n\
    \  passed; all id/label pairs corresponded and 104 non-blocking plausibility\n\
    \  warnings were reported.\n- `uv run --frozen python scripts/check_flat_export_coverage.py`:\
    \ passed; docs\n  data were fresh and every curated label was resolvable.\n\n\
    ## Evidence\n\n- `mappings/culturemech_residual_groundings.tsv` has the maintained\
    \ residual\n  decisions that folded `Artificial seawater`,\n  `Artificial seawater\
    \ (see below)`, `Artificial Seawater`, and\n  `Artificial seawater (see Medium\
    \ No. 736 )` to `MICRO:0001715`.\n- `mappings/ingredient_mappings.sssom.tsv` row\
    \ 482 maps\n  `MIM:Artificial_seawater` to `MICRO:0001715` with `skos:exactMatch`\
    \ and keeps\n  the two parenthetical strings in `other`.\n- A hidden, ignored-inclusive\
    \ search across the active checkout, excluding\n  stale `data/curated/backups`\
    \ and review output, found the same identity in\n  the per-record YAML, aggregate\
    \ YAML, SSSOM, CultureMech residual TSVs, and\n  generated docs products.\n\n\
    ## Completeness\n\n- Occurrence counts are populated: 19 total mentions across\
    \ 19 CultureMech\n  recipes.\n- The record correctly leaves components, roles,\
    \ environment, datasets, and\n  discussions empty; it is only publishing a resolved\
    \ CultureMech residual\n  ingredient and two raw label variants.\n- No CAS or\
    \ chemical structure fields are expected for this MICRO mixture.\n\n## Recommended\
    \ Edits\n\n- None.\n"
- evidence_id: ev-c0ba3a9bc4c527b7
  kind: prior_review
  reference: reviews/structured/20261011T030852Z-mim-token-scope-reassessment/review.yaml
  locator: findings[finding_id=scope-f-e1004757f90e8c13]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding scope-f-e1004757f90e8c13 in 20261011T030852Z-mim-token-scope-reassessment
  snapshot_sha256: 42a76b000bcbd07b426f6bad61b124b11ec08d8977783a67b732b01754f7c609
assessments:
- assessment_id: a-dc7c05c54d4ef45f
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-205c79d137874075
  evidence_ids:
  - ev-ff32a7302db1eb17
  - ev-6518654aed992338
  - ev-91c2182d00c37a4a
  - ev-6a7f27c85a59a50e
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-e8e219665f131e4e
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: not_applicable
  summary: The latest legacy review reports no outstanding finding. This run verifies
    local consistency only; it does not renew that earlier scientific pass.
  target_ids:
  - record-205c79d137874075
  evidence_ids:
  - ev-a3370b8d14b4ebe5
  - ev-ff32a7302db1eb17
  details: 'Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-16T08:44:30Z;
    reviewed SHA-256=9efeac859a634d9d5daf17c7da4e058b51ce7538b0b802fa6ac2b7f6f602e708;
    current SHA-256=9efeac859a634d9d5daf17c7da4e058b51ce7538b0b802fa6ac2b7f6f602e708;
    hash_changed=False. Reports=["reports/yaml_record_review/Artificial_seawater.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CultureMech
    residual record exact-maps to MICRO artificial seawater and keeps parenthetical
    recipe labels only as raw source surfaces.'
  dimensions:
  - name: legacy-native-ids
    value: '[]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-ff32a7302db1eb17
    - ev-a3370b8d14b4ebe5
- assessment_id: a-6e088ed1313e9fdd
  area: nomenclature
  topic: Unresolved recipe-reference or truncated-concentration synonyms
  outcome: concern
  summary: 'Historical tokens are still present on the exact-subject SSSOM rows: [{"reason":"unresolved
    recipe cross-reference in a resolving synonym","token":"Artificial seawater (see
    Medium No. 736 )"},{"reason":"unresolved recipe cross-reference in a resolving
    synonym","token":"Artificial seawater (see below)"}]. Truncated concentration
    strings and context-dependent instructions need scoped curation. This check does
    not reject catalog/RAW_TEXT synonyms as a class.'
  target_ids:
  - record-205c79d137874075
  evidence_ids:
  - ev-a3370b8d14b4ebe5
  - ev-91c2182d00c37a4a
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-a3370b8d14b4ebe5
    - ev-91c2182d00c37a4a
- assessment_id: scope-f-e1004757f90e8c13
  area: nomenclature
  topic: Certainty correction for the exact token observation
  outcome: unknown
  summary: Token presence remains reproducible, but the earlier pattern-based observation
    did not establish whether the exact source label denotes this subject or a different
    preparation. Fresh source-context adjudication is required before a confirmed
    defect or label removal. This successor corrects certainty only; it does not establish
    that the token is valid or that another identity allegation is fixed. The historical
    report actually passes the record and explicitly accepts the raw source surface;
    attributing an unresolved token concern to that report was incorrect. No new source
    evidence was supplied to overturn its scoped conclusion.
  target_ids:
  - record-205c79d137874075
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-8fab9fb02ee4454f
  - ev-f5500c887f4dc734
  - ev-16c562c2dbdbab95
  - ev-8ca93b32516cbb52
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Source-scope question only, not a disposition of the complete historical
      report.
    evidence_ids:
    - ev-823412d1eacb6795
    - ev-8fab9fb02ee4454f
    - ev-f5500c887f4dc734
    - ev-16c562c2dbdbab95
    - ev-8ca93b32516cbb52
findings:
- finding_id: rec-scope-f-e1004757f90e8c13
  issue_key: mim-reconciliation-exported-context-tokens-205c79d137874075
  category: nomenclature
  severity: major
  status: deferred
  certainty: provisional
  title: 'Adjudicate source scope of exported tokens: Artificial seawater'
  description: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed. The historical report actually passes the record and explicitly accepts
    the raw source surface; attributing an unresolved token concern to that report
    was incorrect. No new source evidence was supplied to overturn its scoped conclusion.
  target_ids:
  - record-205c79d137874075
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-8fab9fb02ee4454f
  - ev-f5500c887f4dc734
  - ev-16c562c2dbdbab95
  - ev-8ca93b32516cbb52
  - ev-c0ba3a9bc4c527b7
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Artificial_seawater.yaml
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
    is fixed. The historical report actually passes the record and explicitly accepts
    the raw source surface; attributing an unresolved token concern to that report
    was incorrect. No new source evidence was supplied to overturn its scoped conclusion.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T030852Z-mim-token-scope-reassessment
    finding_id: scope-f-e1004757f90e8c13
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
  with lineage to 20261011T024631Z-mim-reconcile-all-batch-03, 20261011T030852Z-mim-token-scope-reassessment.
```
