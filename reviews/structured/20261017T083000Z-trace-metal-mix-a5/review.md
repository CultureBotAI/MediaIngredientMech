# Per-record structured review: Trace_Metal_Mix_A5 (data/ingredients/mapped/Trace_Metal_Mix_A5.yaml)

- Review: 20261017T083000Z-trace-metal-mix-a5
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Trace_Metal_Mix_A5 (data/ingredients/mapped/Trace_Metal_Mix_A5.yaml, record-78ea6a14a080dbf0, mapping_status=MAPPED). Records 1 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Trace_Metal_Mix_A5.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Trace_Metal_Mix_A5.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-78ea6a14a080dbf0 | data/ingredients/mapped/Trace_Metal_Mix_A5.yaml | maintained | Trace_Metal_Mix_A5 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-78ea6a14a080dbf0 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-78ea6a14a080dbf0 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-78ea6a14a080dbf0 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-78ea6a14a080dbf0.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-78ea6a14a080dbf0.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T19:13:37Z; reviewed SHA-256=5982838d016b9e668006fa6cd8108c3930358970b2156b2a1596425af3ab4ef2; current SHA-256=5982838d016b9e668006fa6cd8108c3930358970b2156b2a1596425af3ab4ef2; hash_changed=False. Reports=["reports/yaml_record_review/Trace_Metal_Mix_A5.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact MICRO identity passes, but a see-below alias leaks into final SSSOM other and TRACE_ELEMENT is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-78ea6a14a080dbf0.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

### Unresolved recipe-reference or truncated-concentration synonyms

nomenclature: concern. Targets: record-78ea6a14a080dbf0.

Historical tokens are still present on the exact-subject SSSOM rows: [{"reason":"unresolved recipe cross-reference in a resolving synonym","token":"Trace Metal Mix A5 (see below)"}]. Truncated concentration strings and context-dependent instructions need scoped curation. This check does not reject catalog/RAW_TEXT synonyms as a class.

### Certainty correction for the exact token observation

nomenclature: unknown. Targets: record-78ea6a14a080dbf0.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

## Findings

### rec-f-f651e0b3023ee4ef: Reassess prediction-only role support: Trace metal mix A5

major / open / confirmed; issue key: mim-reconciliation-role-support-78ea6a14a080dbf0.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

### rec-scope-f-612aa67bad26d26a: Adjudicate source scope of exported tokens: Trace metal mix A5

major / deferred / provisional; issue key: mim-reconciliation-exported-context-tokens-78ea6a14a080dbf0.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

Disposition: Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

## Recommended Actions And Acceptance Checks

### rec-action-f651e0b3023ee4ef

Reassess prediction-only role support: Trace metal mix A5

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-1417aa945298d84c | data/ingredients/mapped/Trace_Metal_Mix_A5.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1978],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0001349","line":1980,"mapping_status":"MAPPED","ontology_id":"MICRO:0001349","preferred_term":"Trace metal mix A5"}],"identifier":"MICRO:0001349","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"MICRO:0001349","ontology_label":"trace metal mix A5","ontology_source":"MICRO"},"preferred_term":"Trace metal mix A5","sssom_rows":[{"data_row":2804,"object_id":"MICRO:0001349","object_label":"trace metal mix A5","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Trace_Metal_Mix_A5","synonym_count":2} |
| ev-a3b10bf539d20308 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1978] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-23742d2f5e375858 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Trace_Metal_Mix_A5; data-row positions=[2804] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2804,"object_id":"MICRO:0001349","object_label":"trace metal mix A5","other":"Trace Metal Mix A5 (see below)","predicate_id":"skos:exactMatch","subject_id":"MIM:Trace_Metal_Mix_A5","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-747a9d9758c8ae7b | docs/data/mapped_ingredients.csv; CSV lines=[1980] | supports | Published identity and count rows inspected: [{"identifier":"MICRO:0001349","line":1980,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"MICRO:0001349","preferred_term":"Trace metal mix A5","total_occurrences":"2"}] |
| ev-8a6a1ce8b70c223e | reports/yaml_record_review/Trace_Metal_Mix_A5.md; &#96;data/ingredients/mapped/Trace_Metal_Mix_A5.yaml&#96;:2; Verdict:4; Identity:10; Validation:22; Evidence:32; Issues:40; Major: &#96;see below&#96; is not a true synonym:42; Major: &#96;TRACE_ELEMENT&#96; is provisional LLM evidence:47; Completeness:54; Recommended Edits:60 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-2d24a67f6ac25674 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1298,1525] | context_only | [{"current_record_sha256":"5982838d016b9e668006fa6cd8108c3930358970b2156b2a1596425af3ab4ef2","finding_id":"SEM:52d89e526ec296e08a34","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"5982838d016b9e668006fa6cd8108c3930358970b2156b2a1596425af3ab4ef2","finding_id":"SEM:1ae32b1fcc01a6786612","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-b0bef49e2ca23441 | data/ingredients/mapped/Trace_Metal_Mix_A5.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional in-session LLM role assignment; review recommended.","reference_text":"Assigned by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"TRACE_ELEMENT"}}] |
| ev-823412d1eacb6795 | MAPPING_SEMANTICS.md; Sections on REJECTED_LABEL and the damaged-label RAW_TEXT carve-out | supports | Raw spellings may remain resolvable when they denote the same substance. Wrong-identity labels must not resolve. A recipe-pointer pattern alone does not adjudicate that distinction. |
| ev-666a0e05df6eee3c | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml; findings[finding_id=f-612aa67bad26d26a] | context_only | Exact earlier occurrence has open/confirmed status, based on exported-token presence and historical report text. |
| ev-995ddb5e1dd7c309 | data/ingredients/mapped/Trace_Metal_Mix_A5.yaml; identifier, ontology_mapping, synonyms and curation_history | partial | {"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv", "synonym_text": "Trace Metal Mix A5 (see below)", "synonym_type": "RAW_TEXT"}], "history": [{"action": "CREATED_AS_UNMAPPED", "changes": "Imported from CultureBotHT (consolidated_media.json (media-only)). Used in 7 CultureBot media; samples: BG11C, BG11, BG11R\u2026. No CAS-RN or CHEBI mapping available; curator review needed.", "curator": "audit_add_remaining_culturebotht", "llm_assisted": false, "new_status": "UNMAPPED", "timestamp": "2026-04-29T06:51:33.117170+00:00"}, {"action": "AUTO_UPGRADE_TO_MICRO", "changes": "primary UNMAPPED_0258 \u2192 MICRO:0001349 via name normalization to 'Trace metal mix A5'", "curator": "resolve_unmapped", "llm_assisted": false, "timestamp": "2026-05-02T00:41:18.463553+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE", "changes": "set ingredient_type=STOCK_SOLUTION (name matches solution pattern 'Trace metal')", "curator": "auto_classify_ingredient_type", "llm_assisted": false, "timestamp": "2026-05-02T03:12:18.924925+00:00"}, {"action": "ANNOTATED", "changes": "Added media role: TRACE_ELEMENT (confidence: 0.60)", "curator": "claude_in_session_curation", "timestamp": "2026-06-09T04:56:30.248262+00:00"}, {"action": "ANNOTATED", "changes": "Migrated legacy media_roles to role facets (#128): TRACE_ELEMENT -&gt; nutritional_roles.TRACE_ELEMENT", "curator": "migrate_media_roles_to_facets", "timestamp": "2026-07-20T00:00:00+00:00"}, {"action": "CORRECTED", "changes": "occurrence_statistics 7/7 -&gt; 2/2 (media_count/total_occurrences), derived from distinct CultureMech recipe ids in the #337 occurrence table. The prior values came from the importer retired in #453, whose media_count counted a list truncated to 50 examples (#449). [source=ingredient_occurrences.tsv culturemech_rev=15a4da5c08 rows=194137 distinct_recipes=15257]", "curator": "refresh_occurrence_statistics", "timestamp": "2026-08-27T03:16:39.519991+00:00"}, {"action": "ADDED_SYNONYMS", "changes": "Added 1 CultureMech recipe surface form(s) that folded onto this record's published label but were absent from MIM's label index, so CultureMech could not resolve them: 'Trace Metal Mix A5 (see below)' (x1 CultureMech mentions). Source: culturemech:output/ingredient_occurrences.tsv.", "curator": "claude_culturemech_alias_backfill", "llm_assisted": false, "timestamp": "2026-08-30T04:48:06.233536+00:00"}], "identifier": "MICRO:0001349", "mapping": {"evidence": [{"evidence_type": "DATABASE_MATCH", "notes": "Auto-upgraded from UNMAPPED_0258; matched via 'Trace metal mix A5' (name normalization); label-exact", "source": "MICRO via OLS search (resolve_unmapped)"}], "mapping_quality": "EXACT_MATCH", "ontology_id": "MICRO:0001349", "ontology_label": "trace metal mix A5", "ontology_source": "MICRO"}} |
| ev-3e284f13241fa94e | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Trace_Metal_Mix_A5 | supports | [{"comment": "", "confidence": "0.99", "data_row": 2804, "mapping_date": "2026-08-30", "mapping_justification": "semapv:LexicalMatching", "object_id": "MICRO:0001349", "object_label": "trace metal mix A5", "object_source": "obo:micro.owl", "other": "Trace Metal Mix A5 (see below)", "predicate_id": "skos:exactMatch", "source": "MIM:MICRO via OLS search (resolve_unmapped)&#124;MIM:curator=claude_culturemech_alias_backfill", "subject_id": "MIM:Trace_Metal_Mix_A5", "subject_label": "Trace metal mix A5", "validation_method": "none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-a6e7432b5d0fbcfb | reports/yaml_record_review/Trace_Metal_Mix_A5.md; Complete historical report, including Verdict and Recommended Edits | context_only | Historical interpretation was read in full; it is not fresh source adjudication. |
| ev-0502b137369a5f75 | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml; findings[finding_id=f-f651e0b3023ee4ef] | context_only | Predecessor structured review finding f-f651e0b3023ee4ef in 20261011T024638Z-mim-reconcile-all-batch-11 |
| ev-78319506630627fa | reviews/structured/20261011T030852Z-mim-token-scope-reassessment/review.yaml; findings[finding_id=scope-f-612aa67bad26d26a] | context_only | Predecessor structured review finding scope-f-612aa67bad26d26a in 20261011T030852Z-mim-token-scope-reassessment |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11, 20261011T030852Z-mim-token-scope-reassessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-trace-metal-mix-a5
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Trace_Metal_Mix_A5 (data/ingredients/mapped/Trace_Metal_Mix_A5.yaml)'
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
native_verdict: mapping_status=MAPPED; open=1; deferred=1
scientific_review: false
summary: Per-record structured review for Trace_Metal_Mix_A5 (data/ingredients/mapped/Trace_Metal_Mix_A5.yaml,
  record-78ea6a14a080dbf0, mapping_status=MAPPED). Records 1 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Trace_Metal_Mix_A5.yaml
    sha256: 5982838d016b9e668006fa6cd8108c3930358970b2156b2a1596425af3ab4ef2
    role: target
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
    sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
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
  - path: reports/yaml_record_review/Trace_Metal_Mix_A5.md
    sha256: fd88d90adbbb3033d82b606fa92e4793b6a9590f36d8bae2ac5819b09aa09534
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
  - path: MAPPING_SEMANTICS.md
    sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805
    role: context
targets:
- target_id: record-78ea6a14a080dbf0
  path: data/ingredients/mapped/Trace_Metal_Mix_A5.yaml
  label: Trace_Metal_Mix_A5
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trace_Metal_Mix_A5.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Trace_Metal_Mix_A5.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Trace_Metal_Mix_A5.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-78ea6a14a080dbf0
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-78ea6a14a080dbf0
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-78ea6a14a080dbf0
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-78ea6a14a080dbf0
evidence:
- evidence_id: ev-1417aa945298d84c
  kind: record_content
  reference: data/ingredients/mapped/Trace_Metal_Mix_A5.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1978],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0001349","line":1980,"mapping_status":"MAPPED","ontology_id":"MICRO:0001349","preferred_term":"Trace
    metal mix A5"}],"identifier":"MICRO:0001349","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"MICRO:0001349","ontology_label":"trace
    metal mix A5","ontology_source":"MICRO"},"preferred_term":"Trace metal mix A5","sssom_rows":[{"data_row":2804,"object_id":"MICRO:0001349","object_label":"trace
    metal mix A5","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Trace_Metal_Mix_A5","synonym_count":2}'
  snapshot_sha256: 5982838d016b9e668006fa6cd8108c3930358970b2156b2a1596425af3ab4ef2
- evidence_id: ev-a3b10bf539d20308
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1978]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-23742d2f5e375858
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Trace_Metal_Mix_A5; data-row positions=[2804]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2804,"object_id":"MICRO:0001349","object_label":"trace
    metal mix A5","other":"Trace Metal Mix A5 (see below)","predicate_id":"skos:exactMatch","subject_id":"MIM:Trace_Metal_Mix_A5","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-747a9d9758c8ae7b
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1980]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"MICRO:0001349","line":1980,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"MICRO:0001349","preferred_term":"Trace
    metal mix A5","total_occurrences":"2"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-8a6a1ce8b70c223e
  kind: prior_review
  reference: reports/yaml_record_review/Trace_Metal_Mix_A5.md
  locator: '`data/ingredients/mapped/Trace_Metal_Mix_A5.yaml`:2; Verdict:4; Identity:10;
    Validation:22; Evidence:32; Issues:40; Major: `see below` is not a true synonym:42;
    Major: `TRACE_ELEMENT` is provisional LLM evidence:47; Completeness:54; Recommended
    Edits:60'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: fd88d90adbbb3033d82b606fa92e4793b6a9590f36d8bae2ac5819b09aa09534
  quote: "Issues:\n\n\nMajor: `see below` is not a true synonym:\nThe final `other`\
    \ token `Trace Metal Mix A5 (see below)` is a recipe-local\ninstruction, not an\
    \ alternate label for the MICRO stock-solution term.\n\nMajor: `TRACE_ELEMENT`\
    \ is provisional LLM evidence:\nThe only role assertion is still the June in-session\
    \ Claude prediction with the\ncurator note `Provisional in-session LLM role assignment;\
    \ review recommended.`\nThe exact MICRO identity establishes the stock solution\
    \ label, but it does not\nprovide independent role evidence.\n\nRecommended Edits:\n\
    - Filter `Trace Metal Mix A5 (see below)` out of final SSSOM `other`.\n- Replace\
    \ the provisional role evidence with curated recipe or ontology\n  evidence, or\
    \ remove `nutritional_roles` until that evidence is available."
- evidence_id: ev-2d24a67f6ac25674
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1298,1525]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"5982838d016b9e668006fa6cd8108c3930358970b2156b2a1596425af3ab4ef2","finding_id":"SEM:52d89e526ec296e08a34","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"5982838d016b9e668006fa6cd8108c3930358970b2156b2a1596425af3ab4ef2","finding_id":"SEM:1ae32b1fcc01a6786612","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-b0bef49e2ca23441
  kind: record_content
  reference: data/ingredients/mapped/Trace_Metal_Mix_A5.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional
    in-session LLM role assignment; review recommended.","reference_text":"Assigned
    by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"TRACE_ELEMENT"}}]'
  snapshot_sha256: 5982838d016b9e668006fa6cd8108c3930358970b2156b2a1596425af3ab4ef2
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
- evidence_id: ev-666a0e05df6eee3c
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
  locator: findings[finding_id=f-612aa67bad26d26a]
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Exact earlier occurrence has open/confirmed status, based on exported-token
    presence and historical report text.
  snapshot_sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
  quote: '{"category": "nomenclature", "certainty": "confirmed", "description": "Historical
    tokens are still present on the exact-subject SSSOM rows: [{\"reason\":\"unresolved
    recipe cross-reference in a resolving synonym\",\"token\":\"Trace Metal Mix A5
    (see below)\"}]. Truncated concentration strings and context-dependent instructions
    need scoped curation. This check does not reject catalog/RAW_TEXT synonyms as
    a class.", "evidence_ids": ["ev-8a6a1ce8b70c223e", "ev-23742d2f5e375858"], "external_issues":
    ["https://github.com/CultureBotAI/MediaIngredientMech/issues/718"], "field_paths":
    ["synonyms", "SSSOM.other"], "finding_id": "f-612aa67bad26d26a", "issue_key":
    "mim-reconciliation-exported-context-tokens-78ea6a14a080dbf0", "owner_paths":
    [{"path": "data/ingredients/mapped/Trace_Metal_Mix_A5.yaml", "repository": "CultureBotAI/MediaIngredientMech",
    "role": "maintained ingredient"}], "severity": "major", "status": "open", "tags":
    ["reconciliation", "bundle-by-owner", "exported-context-tokens"], "target_ids":
    ["record-78ea6a14a080dbf0"], "title": "Review nonportable exported tokens: Trace
    metal mix A5"}'
- evidence_id: ev-995ddb5e1dd7c309
  kind: record_content
  reference: data/ingredients/mapped/Trace_Metal_Mix_A5.yaml
  locator: identifier, ontology_mapping, synonyms and curation_history
  accessed_at: '2026-10-11T03:08:52Z'
  support: partial
  summary: '{"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv",
    "synonym_text": "Trace Metal Mix A5 (see below)", "synonym_type": "RAW_TEXT"}],
    "history": [{"action": "CREATED_AS_UNMAPPED", "changes": "Imported from CultureBotHT
    (consolidated_media.json (media-only)). Used in 7 CultureBot media; samples: BG11C,
    BG11, BG11R\u2026. No CAS-RN or CHEBI mapping available; curator review needed.",
    "curator": "audit_add_remaining_culturebotht", "llm_assisted": false, "new_status":
    "UNMAPPED", "timestamp": "2026-04-29T06:51:33.117170+00:00"}, {"action": "AUTO_UPGRADE_TO_MICRO",
    "changes": "primary UNMAPPED_0258 \u2192 MICRO:0001349 via name normalization
    to ''Trace metal mix A5''", "curator": "resolve_unmapped", "llm_assisted": false,
    "timestamp": "2026-05-02T00:41:18.463553+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE",
    "changes": "set ingredient_type=STOCK_SOLUTION (name matches solution pattern
    ''Trace metal'')", "curator": "auto_classify_ingredient_type", "llm_assisted":
    false, "timestamp": "2026-05-02T03:12:18.924925+00:00"}, {"action": "ANNOTATED",
    "changes": "Added media role: TRACE_ELEMENT (confidence: 0.60)", "curator": "claude_in_session_curation",
    "timestamp": "2026-06-09T04:56:30.248262+00:00"}, {"action": "ANNOTATED", "changes":
    "Migrated legacy media_roles to role facets (#128): TRACE_ELEMENT -> nutritional_roles.TRACE_ELEMENT",
    "curator": "migrate_media_roles_to_facets", "timestamp": "2026-07-20T00:00:00+00:00"},
    {"action": "CORRECTED", "changes": "occurrence_statistics 7/7 -> 2/2 (media_count/total_occurrences),
    derived from distinct CultureMech recipe ids in the #337 occurrence table. The
    prior values came from the importer retired in #453, whose media_count counted
    a list truncated to 50 examples (#449). [source=ingredient_occurrences.tsv culturemech_rev=15a4da5c08
    rows=194137 distinct_recipes=15257]", "curator": "refresh_occurrence_statistics",
    "timestamp": "2026-08-27T03:16:39.519991+00:00"}, {"action": "ADDED_SYNONYMS",
    "changes": "Added 1 CultureMech recipe surface form(s) that folded onto this record''s
    published label but were absent from MIM''s label index, so CultureMech could
    not resolve them: ''Trace Metal Mix A5 (see below)'' (x1 CultureMech mentions).
    Source: culturemech:output/ingredient_occurrences.tsv.", "curator": "claude_culturemech_alias_backfill",
    "llm_assisted": false, "timestamp": "2026-08-30T04:48:06.233536+00:00"}], "identifier":
    "MICRO:0001349", "mapping": {"evidence": [{"evidence_type": "DATABASE_MATCH",
    "notes": "Auto-upgraded from UNMAPPED_0258; matched via ''Trace metal mix A5''
    (name normalization); label-exact", "source": "MICRO via OLS search (resolve_unmapped)"}],
    "mapping_quality": "EXACT_MATCH", "ontology_id": "MICRO:0001349", "ontology_label":
    "trace metal mix A5", "ontology_source": "MICRO"}}'
  snapshot_sha256: 5982838d016b9e668006fa6cd8108c3930358970b2156b2a1596425af3ab4ef2
- evidence_id: ev-3e284f13241fa94e
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Trace_Metal_Mix_A5
  accessed_at: '2026-10-11T03:08:52Z'
  support: supports
  summary: '[{"comment": "", "confidence": "0.99", "data_row": 2804, "mapping_date":
    "2026-08-30", "mapping_justification": "semapv:LexicalMatching", "object_id":
    "MICRO:0001349", "object_label": "trace metal mix A5", "object_source": "obo:micro.owl",
    "other": "Trace Metal Mix A5 (see below)", "predicate_id": "skos:exactMatch",
    "source": "MIM:MICRO via OLS search (resolve_unmapped)|MIM:curator=claude_culturemech_alias_backfill",
    "subject_id": "MIM:Trace_Metal_Mix_A5", "subject_label": "Trace metal mix A5",
    "validation_method": "none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-a6e7432b5d0fbcfb
  kind: prior_review
  reference: reports/yaml_record_review/Trace_Metal_Mix_A5.md
  locator: Complete historical report, including Verdict and Recommended Edits
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Historical interpretation was read in full; it is not fresh source adjudication.
  snapshot_sha256: fd88d90adbbb3033d82b606fa92e4793b6a9590f36d8bae2ac5819b09aa09534
  quote: "# `data/ingredients/mapped/Trace_Metal_Mix_A5.yaml`\n\n## Verdict\n\nNeeds\
    \ curation, major. The exact MICRO identity and occurrence count are\nsynchronized,\
    \ but a `see below` source alias leaks into final SSSOM and the\n`TRACE_ELEMENT`\
    \ role is still provisional in-session LLM evidence.\n\n## Identity\n\n- Reviewed\
    \ record: `data/ingredients/mapped/Trace_Metal_Mix_A5.yaml`.\n- Identifier and\
    \ grounding: `identifier: MICRO:0001349` with matching\n  `ontology_mapping.ontology_id`,\
    \ label `trace metal mix A5`, source `MICRO`,\n  `mapping_quality: EXACT_MATCH`,\
    \ `mapping_status: MAPPED`, and\n  `ingredient_type: STOCK_SOLUTION`.\n- Synonyms:\
    \ raw CultureBotHT source form plus raw CultureMech source form\n  `Trace Metal\
    \ Mix A5 (see below)`.\n- Occurrences: 2 CultureMech recipe occurrences in 2 media.\n\
    - Roles: one `nutritional_roles.TRACE_ELEMENT` facet at confidence `0.6`.\n\n\
    ## Validation\n\n- `uv run --frozen python scripts/validate_strict.py` on the\
    \ 5-file batch from\n  `Trace_Element_Solution_SL-10` through `Trace_Metals_Solution`:\
    \ exited 0 and\n  wrote zero ERROR rows.\n- Direct old Engine A/OBO term validation\
    \ was skipped for this MICRO row\n  because `MICRO` is outside the CHEBI-focused\
    \ OBO term subset.\n- Local aggregate comparison found this per-record file synchronized\
    \ with its\n  keyed row in `data/curated/mapped_ingredients.yaml`.\n\n## Evidence\n\
    \n- Fresh exact OLS4 search for `Trace metal mix A5` returns `MICRO:0001349` with\n\
    \  label `trace metal mix A5`.\n- The final SSSOM row has\n  `MIM:Trace_Metal_Mix_A5\
    \ skos:exactMatch MICRO:0001349` and exports\n  `Trace Metal Mix A5 (see below)`\
    \ in `other`.\n\n## Issues\n\n### Major: `see below` is not a true synonym\n\n\
    The final `other` token `Trace Metal Mix A5 (see below)` is a recipe-local\ninstruction,\
    \ not an alternate label for the MICRO stock-solution term.\n\n### Major: `TRACE_ELEMENT`\
    \ is provisional LLM evidence\n\nThe only role assertion is still the June in-session\
    \ Claude prediction with the\ncurator note `Provisional in-session LLM role assignment;\
    \ review recommended.`\nThe exact MICRO identity establishes the stock solution\
    \ label, but it does not\nprovide independent role evidence.\n\n## Completeness\n\
    \n- The MICRO identity, occurrence count, aggregate row, and final SSSOM row\n\
    \  agree.\n- The final raw alias and provisional role facet still require curation.\n\
    \n## Recommended Edits\n\n- Filter `Trace Metal Mix A5 (see below)` out of final\
    \ SSSOM `other`.\n- Replace the provisional role evidence with curated recipe\
    \ or ontology\n  evidence, or remove `nutritional_roles` until that evidence is\
    \ available.\n"
- evidence_id: ev-0502b137369a5f75
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
  locator: findings[finding_id=f-f651e0b3023ee4ef]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-f651e0b3023ee4ef in 20261011T024638Z-mim-reconcile-all-batch-11
  snapshot_sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
- evidence_id: ev-78319506630627fa
  kind: prior_review
  reference: reviews/structured/20261011T030852Z-mim-token-scope-reassessment/review.yaml
  locator: findings[finding_id=scope-f-612aa67bad26d26a]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding scope-f-612aa67bad26d26a in 20261011T030852Z-mim-token-scope-reassessment
  snapshot_sha256: 42a76b000bcbd07b426f6bad61b124b11ec08d8977783a67b732b01754f7c609
assessments:
- assessment_id: a-8872b978eb8f6ac0
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-78ea6a14a080dbf0
  evidence_ids:
  - ev-1417aa945298d84c
  - ev-a3b10bf539d20308
  - ev-23742d2f5e375858
  - ev-747a9d9758c8ae7b
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-ea2bb3471a979da0
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-78ea6a14a080dbf0
  evidence_ids:
  - ev-8a6a1ce8b70c223e
  - ev-1417aa945298d84c
  - ev-2d24a67f6ac25674
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T19:13:37Z;
    reviewed SHA-256=5982838d016b9e668006fa6cd8108c3930358970b2156b2a1596425af3ab4ef2;
    current SHA-256=5982838d016b9e668006fa6cd8108c3930358970b2156b2a1596425af3ab4ef2;
    hash_changed=False. Reports=["reports/yaml_record_review/Trace_Metal_Mix_A5.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    MICRO identity passes, but a see-below alias leaks into final SSSOM other and
    TRACE_ELEMENT is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-8a6a1ce8b70c223e
    - ev-1417aa945298d84c
  - name: legacy-native-ids
    value: '["SEM:52d89e526ec296e08a34","SEM:1ae32b1fcc01a6786612"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-1417aa945298d84c
    - ev-8a6a1ce8b70c223e
    - ev-2d24a67f6ac25674
- assessment_id: a-b0bef49e2ca23441
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-78ea6a14a080dbf0
  evidence_ids:
  - ev-8a6a1ce8b70c223e
  - ev-b0bef49e2ca23441
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-8a6a1ce8b70c223e
    - ev-b0bef49e2ca23441
- assessment_id: a-38ad48dcdbcb887e
  area: nomenclature
  topic: Unresolved recipe-reference or truncated-concentration synonyms
  outcome: concern
  summary: 'Historical tokens are still present on the exact-subject SSSOM rows: [{"reason":"unresolved
    recipe cross-reference in a resolving synonym","token":"Trace Metal Mix A5 (see
    below)"}]. Truncated concentration strings and context-dependent instructions
    need scoped curation. This check does not reject catalog/RAW_TEXT synonyms as
    a class.'
  target_ids:
  - record-78ea6a14a080dbf0
  evidence_ids:
  - ev-8a6a1ce8b70c223e
  - ev-23742d2f5e375858
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-8a6a1ce8b70c223e
    - ev-23742d2f5e375858
- assessment_id: scope-f-612aa67bad26d26a
  area: nomenclature
  topic: Certainty correction for the exact token observation
  outcome: unknown
  summary: Token presence remains reproducible, but the earlier pattern-based observation
    did not establish whether the exact source label denotes this subject or a different
    preparation. Fresh source-context adjudication is required before a confirmed
    defect or label removal. This successor corrects certainty only; it does not establish
    that the token is valid or that another identity allegation is fixed.
  target_ids:
  - record-78ea6a14a080dbf0
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-666a0e05df6eee3c
  - ev-995ddb5e1dd7c309
  - ev-3e284f13241fa94e
  - ev-a6e7432b5d0fbcfb
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Source-scope question only, not a disposition of the complete historical
      report.
    evidence_ids:
    - ev-823412d1eacb6795
    - ev-666a0e05df6eee3c
    - ev-995ddb5e1dd7c309
    - ev-3e284f13241fa94e
    - ev-a6e7432b5d0fbcfb
findings:
- finding_id: rec-f-f651e0b3023ee4ef
  issue_key: mim-reconciliation-role-support-78ea6a14a080dbf0
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Trace metal mix A5'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-78ea6a14a080dbf0
  evidence_ids:
  - ev-8a6a1ce8b70c223e
  - ev-b0bef49e2ca23441
  - ev-0502b137369a5f75
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trace_Metal_Mix_A5.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024638Z-mim-reconcile-all-batch-11
    finding_id: f-f651e0b3023ee4ef
- finding_id: rec-scope-f-612aa67bad26d26a
  issue_key: mim-reconciliation-exported-context-tokens-78ea6a14a080dbf0
  category: nomenclature
  severity: major
  status: deferred
  certainty: provisional
  title: 'Adjudicate source scope of exported tokens: Trace metal mix A5'
  description: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed.
  target_ids:
  - record-78ea6a14a080dbf0
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-666a0e05df6eee3c
  - ev-995ddb5e1dd7c309
  - ev-3e284f13241fa94e
  - ev-a6e7432b5d0fbcfb
  - ev-78319506630627fa
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trace_Metal_Mix_A5.yaml
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
    finding_id: scope-f-612aa67bad26d26a
actions:
- action_id: rec-action-f651e0b3023ee4ef
  description: 'Reassess prediction-only role support: Trace metal mix A5'
  finding_ids:
  - rec-f-f651e0b3023ee4ef
  target_ids:
  - record-78ea6a14a080dbf0
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trace_Metal_Mix_A5.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-11, 20261011T030852Z-mim-token-scope-reassessment.
```
