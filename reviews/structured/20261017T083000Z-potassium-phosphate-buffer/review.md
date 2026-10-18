# Per-record structured review: Potassium_Phosphate_Buffer (data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml)

- Review: 20261017T083000Z-potassium-phosphate-buffer
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Potassium_Phosphate_Buffer (data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml, record-4190c0ee5976447a, mapping_status=MAPPED). Records 1 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-4190c0ee5976447a | data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml | maintained | Potassium_Phosphate_Buffer |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-4190c0ee5976447a | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-4190c0ee5976447a | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-4190c0ee5976447a | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-4190c0ee5976447a.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-4190c0ee5976447a.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T10:16:34Z; reviewed SHA-256=9a33ce5d93f8928878ab1309f834d49f505d27abf4d5ee41e23b79a40a2ac40e; current SHA-256=9a33ce5d93f8928878ab1309f834d49f505d27abf4d5ee41e23b79a40a2ac40e; hash_changed=False. Reports=["reports/yaml_record_review/Potassium_Phosphate_Buffer.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local buffer identity passes, but final SSSOM exports pH/molarity recipe labels and BUFFER is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-4190c0ee5976447a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

### Unresolved recipe-reference or truncated-concentration synonyms

nomenclature: concern. Targets: record-4190c0ee5976447a.

Historical tokens are still present on the exact-subject SSSOM rows: [{"reason":"unresolved recipe cross-reference in a resolving synonym","token":"Potassium phosphate buffer* (see below)"}]. Truncated concentration strings and context-dependent instructions need scoped curation. This check does not reject catalog/RAW_TEXT synonyms as a class.

### Certainty correction for the exact token observation

nomenclature: unknown. Targets: record-4190c0ee5976447a.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

## Findings

### rec-f-3339000e63c2dccf: Reassess prediction-only role support: Potassium phosphate buffer

major / open / confirmed; issue key: mim-reconciliation-role-support-4190c0ee5976447a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

### rec-scope-f-f582ea830b4f370d: Adjudicate source scope of exported tokens: Potassium phosphate buffer

major / deferred / provisional; issue key: mim-reconciliation-exported-context-tokens-4190c0ee5976447a.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

Disposition: Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

## Recommended Actions And Acceptance Checks

### rec-action-3339000e63c2dccf

Reassess prediction-only role support: Potassium phosphate buffer

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-6bdceef7ba6aa436 | data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1694],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:potassium_phosphate_buffer","line":1696,"mapping_status":"MAPPED","ontology_id":"NCIT:C29321","preferred_term":"Potassium phosphate buffer"}],"identifier":"kgmicrobe.ingredient:potassium_phosphate_buffer","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":44,"edge_count":44,"occurrences":44},"occurrence_statistics":{"media_count":44,"total_occurrences":44},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"NCIT:C29321","ontology_label":"Phosphate Buffer","ontology_source":"NCIT"},"preferred_term":"Potassium phosphate buffer","sssom_rows":[{"data_row":2327,"object_id":"NCIT:C29321","object_label":"Phosphate Buffer","predicate_id":"skos:closeMatch"},{"data_row":2328,"object_id":"kgmicrobe.ingredient:potassium_phosphate_buffer","object_label":"Potassium phosphate buffer","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Potassium_Phosphate_Buffer","synonym_count":5} |
| ev-84c339f9b2e6b5d1 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1694] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-8ff94a6ea1085255 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Potassium_Phosphate_Buffer; data-row positions=[2327,2328] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2327,"object_id":"NCIT:C29321","object_label":"Phosphate Buffer","other":"Potassium phosphate buffer (0.01 M, pH 7.2)&#124;Potassium phosphate buffer (0.02 M, pH 7.0)&#124;Potassium phosphate buffer (1 M, pH 7.1)&#124;Potassium phosphate buffer* (see below)","predicate_id":"skos:closeMatch","subject_id":"MIM:Potassium_Phosphate_Buffer","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"},{"data_row":2328,"object_id":"kgmicrobe.ingredient:potassium_phosphate_buffer","object_label":"Potassium phosphate buffer","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Potassium_Phosphate_Buffer","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-5a185a31636016cb | docs/data/mapped_ingredients.csv; CSV lines=[1696] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:potassium_phosphate_buffer","line":1696,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"44","ontology_id":"NCIT:C29321","preferred_term":"Potassium phosphate buffer","total_occurrences":"44"}] |
| ev-afd6d431ee989359 | reports/yaml_record_review/Potassium_Phosphate_Buffer.md; &#96;data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-f71c711fe7c99148 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1138,1780] | context_only | [{"current_record_sha256":"9a33ce5d93f8928878ab1309f834d49f505d27abf4d5ee41e23b79a40a2ac40e","finding_id":"SEM:60203fb718c81304bf6b","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"9a33ce5d93f8928878ab1309f834d49f505d27abf4d5ee41e23b79a40a2ac40e","finding_id":"SEM:985f37eab0ffab7d93e8","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-fa016998b137038b | data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"BUFFER"}}] |
| ev-823412d1eacb6795 | MAPPING_SEMANTICS.md; Sections on REJECTED_LABEL and the damaged-label RAW_TEXT carve-out | supports | Raw spellings may remain resolvable when they denote the same substance. Wrong-identity labels must not resolve. A recipe-pointer pattern alone does not adjudicate that distinction. |
| ev-8bb59eaf8b6e66f4 | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml; findings[finding_id=f-f582ea830b4f370d] | context_only | Exact earlier occurrence has open/confirmed status, based on exported-token presence and historical report text. |
| ev-745bc0e8e18adc16 | data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml; identifier, ontology_mapping, synonyms and curation_history | partial | {"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv", "synonym_text": "Potassium phosphate buffer* (see below)", "synonym_type": "RAW_TEXT"}], "history": [{"action": "CREATED_AS_UNMAPPED", "changes": "Imported from CultureBotHT (consolidated_media.json (media-only)). Used in 2 CultureBot media; samples: Mega, TYG. No CAS-RN or CHEBI mapping available; curator review needed.", "curator": "audit_add_remaining_culturebotht", "llm_assisted": false, "new_status": "UNMAPPED", "timestamp": "2026-04-29T06:51:33.117170+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE", "changes": "set ingredient_type=STOCK_SOLUTION (name matches solution pattern 'phosphate buffer')", "curator": "auto_classify_ingredient_type", "llm_assisted": false, "timestamp": "2026-05-02T03:12:19.854401+00:00"}, {"action": "AUTO_UPGRADE_TO_NCIT", "changes": "primary UNMAPPED_0274 \u2192 NCIT:C29321 (strategy=stem-match)", "curator": "resolve_unmapped_v2", "llm_assisted": false, "timestamp": "2026-05-02T03:18:21.960132+00:00"}, {"action": "CORRECTED", "changes": "Changed identifier from NCIT:C29321 to kgmicrobe.ingredient:potassium_phosphate_buffer and retained NCIT:C29321 only as CLOSE_MATCH. Potassium phosphate buffer is a formulation variant, not identical to the generic phosphate buffer class.", "curator": "ingredient_mapping_review_2026_05_05", "llm_assisted": false, "new_status": "MAPPED", "previous_status": "MAPPED", "timestamp": "2026-05-05T00:00:00+00:00"}, {"action": "ANNOTATED", "changes": "Added media role: BUFFER (confidence: 0.80)", "curator": "infer_roles_from_name_lists", "timestamp": "2026-06-03T02:06:01.748066+00:00"}, {"action": "ANNOTATED", "changes": "Migrated legacy media_roles to role facets (#128): BUFFER -&gt; physicochemical_roles.BUFFER", "curator": "migrate_media_roles_to_facets", "timestamp": "2026-07-20T00:00:00+00:00"}, {"action": "CORRECTED", "changes": "occurrence_statistics 2/2 -&gt; 44/44 (media_count/total_occurrences), derived from distinct CultureMech recipe ids in the #337 occurrence table. The prior values came from the importer retired in #453, whose media_count counted a list truncated to 50 examples (#449). [source=ingredient_occurrences.tsv culturemech_rev=15a4da5c08 rows=194137 distinct_recipes=15257]", "curator": "refresh_occurrence_statistics", "timestamp": "2026-08-27T03:16:39.519736+00:00"}, {"action": "ADDED_SYNONYMS", "changes": "Added 4 CultureMech recipe surface form(s) that folded onto this record's published label but were absent from MIM's label index, so CultureMech could not resolve them: 'Potassium phosphate buffer (0.01 M, pH 7.2)' (x1 CultureMech mentions); 'Potassium phosphate buffer (0.02 M, pH 7.0)' (x1 CultureMech mentions); 'Potassium phosphate buffer (1 M, pH 7.1)' (x1 CultureMech mentions); 'Potassium phosphate buffer* (see below)' (x1 CultureMech mentions). Source: culturemech:output/ingredient_occurrences.tsv.", "curator": "claude_culturemech_alias_backfill", "llm_assisted": false, "timestamp": "2026-08-30T04:48:06.233536+00:00"}], "identifier": "kgmicrobe.ingredient:potassium_phosphate_buffer", "mapping": {"evidence": [{"evidence_type": "CURATOR_JUDGMENT", "notes": "Potassium phosphate buffer is a formulation variant, not identical to the generic phosphate buffer class.", "source": "ingredient_mapping_review_2026-05-05"}], "mapping_quality": "CLOSE_MATCH", "ontology_id": "NCIT:C29321", "ontology_label": "Phosphate Buffer", "ontology_source": "NCIT"}} |
| ev-7d01fe3478491965 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Potassium_Phosphate_Buffer | supports | [{"comment": "", "confidence": "0.9", "data_row": 2327, "mapping_date": "2026-08-30", "mapping_justification": "semapv:ManualMappingCuration", "object_id": "NCIT:C29321", "object_label": "Phosphate Buffer", "object_source": "obo:ncit.owl", "other": "Potassium phosphate buffer (0.01 M, pH 7.2)&#124;Potassium phosphate buffer (0.02 M, pH 7.0)&#124;Potassium phosphate buffer (1 M, pH 7.1)&#124;Potassium phosphate buffer* (see below)", "predicate_id": "skos:closeMatch", "source": "MIM:ingredient_mapping_review_2026-05-05&#124;MIM:curator=claude_culturemech_alias_backfill", "subject_id": "MIM:Potassium_Phosphate_Buffer", "subject_label": "Potassium phosphate buffer", "validation_method": "none&#124;UNKNOWN_TERM&#124;2026-07-07"}, {"comment": "Registry/identity row preserving kgmicrobe.ingredient:potassium_phosphate_buffer alongside parent NCIT:C29321.", "confidence": "0.99", "data_row": 2328, "mapping_date": "2026-08-30", "mapping_justification": "semapv:ManualMappingCuration", "object_id": "kgmicrobe.ingredient:potassium_phosphate_buffer", "object_label": "Potassium phosphate buffer", "object_source": "kgm:ingredient", "other": "", "predicate_id": "skos:exactMatch", "source": "MIM:ingredient_mapping_review_2026-05-05&#124;MIM:curator=claude_culturemech_alias_backfill", "subject_id": "MIM:Potassium_Phosphate_Buffer", "subject_label": "Potassium phosphate buffer", "validation_method": "none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-a692d3e165ce1613 | reports/yaml_record_review/Potassium_Phosphate_Buffer.md; Complete historical report, including Verdict and Recommended Edits | context_only | Historical interpretation was read in full; it is not fresh source adjudication. |
| ev-cfeb1b367b6f9c64 | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml; findings[finding_id=f-3339000e63c2dccf] | context_only | Predecessor structured review finding f-3339000e63c2dccf in 20261011T024638Z-mim-reconcile-all-batch-10 |
| ev-2915a0c7cc5ef760 | reviews/structured/20261011T030852Z-mim-token-scope-reassessment/review.yaml; findings[finding_id=scope-f-f582ea830b4f370d] | context_only | Predecessor structured review finding scope-f-f582ea830b4f370d in 20261011T030852Z-mim-token-scope-reassessment |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-10, 20261011T030852Z-mim-token-scope-reassessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-potassium-phosphate-buffer
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Potassium_Phosphate_Buffer (data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml)'
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
summary: Per-record structured review for Potassium_Phosphate_Buffer (data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml,
  record-4190c0ee5976447a, mapping_status=MAPPED). Records 1 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml
    sha256: 9a33ce5d93f8928878ab1309f834d49f505d27abf4d5ee41e23b79a40a2ac40e
    role: target
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
    sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
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
  - path: reports/yaml_record_review/Potassium_Phosphate_Buffer.md
    sha256: 884a3c1ac80ea7503bc943cac7d9eef7ff8d329cc1b7da000b75ab605e4019e0
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
  - path: MAPPING_SEMANTICS.md
    sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805
    role: context
targets:
- target_id: record-4190c0ee5976447a
  path: data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml
  label: Potassium_Phosphate_Buffer
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-4190c0ee5976447a
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-4190c0ee5976447a
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-4190c0ee5976447a
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10
    and semantic review dispositions on HEAD.
  target_ids:
  - record-4190c0ee5976447a
evidence:
- evidence_id: ev-6bdceef7ba6aa436
  kind: record_content
  reference: data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1694],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:potassium_phosphate_buffer","line":1696,"mapping_status":"MAPPED","ontology_id":"NCIT:C29321","preferred_term":"Potassium
    phosphate buffer"}],"identifier":"kgmicrobe.ingredient:potassium_phosphate_buffer","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":44,"edge_count":44,"occurrences":44},"occurrence_statistics":{"media_count":44,"total_occurrences":44},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"NCIT:C29321","ontology_label":"Phosphate
    Buffer","ontology_source":"NCIT"},"preferred_term":"Potassium phosphate buffer","sssom_rows":[{"data_row":2327,"object_id":"NCIT:C29321","object_label":"Phosphate
    Buffer","predicate_id":"skos:closeMatch"},{"data_row":2328,"object_id":"kgmicrobe.ingredient:potassium_phosphate_buffer","object_label":"Potassium
    phosphate buffer","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Potassium_Phosphate_Buffer","synonym_count":5}'
  snapshot_sha256: 9a33ce5d93f8928878ab1309f834d49f505d27abf4d5ee41e23b79a40a2ac40e
- evidence_id: ev-84c339f9b2e6b5d1
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1694]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-8ff94a6ea1085255
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Potassium_Phosphate_Buffer; data-row positions=[2327,2328]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2327,"object_id":"NCIT:C29321","object_label":"Phosphate
    Buffer","other":"Potassium phosphate buffer (0.01 M, pH 7.2)|Potassium phosphate
    buffer (0.02 M, pH 7.0)|Potassium phosphate buffer (1 M, pH 7.1)|Potassium phosphate
    buffer* (see below)","predicate_id":"skos:closeMatch","subject_id":"MIM:Potassium_Phosphate_Buffer","validation_method":"none|UNKNOWN_TERM|2026-07-07"},{"data_row":2328,"object_id":"kgmicrobe.ingredient:potassium_phosphate_buffer","object_label":"Potassium
    phosphate buffer","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Potassium_Phosphate_Buffer","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-5a185a31636016cb
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1696]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:potassium_phosphate_buffer","line":1696,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"44","ontology_id":"NCIT:C29321","preferred_term":"Potassium
    phosphate buffer","total_occurrences":"44"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-afd6d431ee989359
  kind: prior_review
  reference: reports/yaml_record_review/Potassium_Phosphate_Buffer.md
  locator: '`data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 884a3c1ac80ea7503bc943cac7d9eef7ff8d329cc1b7da000b75ab605e4019e0
- evidence_id: ev-f71c711fe7c99148
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1138,1780]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"9a33ce5d93f8928878ab1309f834d49f505d27abf4d5ee41e23b79a40a2ac40e","finding_id":"SEM:60203fb718c81304bf6b","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"9a33ce5d93f8928878ab1309f834d49f505d27abf4d5ee41e23b79a40a2ac40e","finding_id":"SEM:985f37eab0ffab7d93e8","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-fa016998b137038b
  kind: record_content
  reference: data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"BUFFER"}}]'
  snapshot_sha256: 9a33ce5d93f8928878ab1309f834d49f505d27abf4d5ee41e23b79a40a2ac40e
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
- evidence_id: ev-8bb59eaf8b6e66f4
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
  locator: findings[finding_id=f-f582ea830b4f370d]
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Exact earlier occurrence has open/confirmed status, based on exported-token
    presence and historical report text.
  snapshot_sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
  quote: '{"category": "nomenclature", "certainty": "confirmed", "description": "Historical
    tokens are still present on the exact-subject SSSOM rows: [{\"reason\":\"unresolved
    recipe cross-reference in a resolving synonym\",\"token\":\"Potassium phosphate
    buffer* (see below)\"}]. Truncated concentration strings and context-dependent
    instructions need scoped curation. This check does not reject catalog/RAW_TEXT
    synonyms as a class.", "evidence_ids": ["ev-afd6d431ee989359", "ev-8ff94a6ea1085255"],
    "external_issues": ["https://github.com/CultureBotAI/MediaIngredientMech/issues/718"],
    "field_paths": ["synonyms", "SSSOM.other"], "finding_id": "f-f582ea830b4f370d",
    "issue_key": "mim-reconciliation-exported-context-tokens-4190c0ee5976447a", "owner_paths":
    [{"path": "data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml", "repository":
    "CultureBotAI/MediaIngredientMech", "role": "maintained ingredient"}], "severity":
    "major", "status": "open", "tags": ["reconciliation", "bundle-by-owner", "exported-context-tokens"],
    "target_ids": ["record-4190c0ee5976447a"], "title": "Review nonportable exported
    tokens: Potassium phosphate buffer"}'
- evidence_id: ev-745bc0e8e18adc16
  kind: record_content
  reference: data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml
  locator: identifier, ontology_mapping, synonyms and curation_history
  accessed_at: '2026-10-11T03:08:52Z'
  support: partial
  summary: '{"candidate_labels": [{"source": "culturemech:output/ingredient_occurrences.tsv",
    "synonym_text": "Potassium phosphate buffer* (see below)", "synonym_type": "RAW_TEXT"}],
    "history": [{"action": "CREATED_AS_UNMAPPED", "changes": "Imported from CultureBotHT
    (consolidated_media.json (media-only)). Used in 2 CultureBot media; samples: Mega,
    TYG. No CAS-RN or CHEBI mapping available; curator review needed.", "curator":
    "audit_add_remaining_culturebotht", "llm_assisted": false, "new_status": "UNMAPPED",
    "timestamp": "2026-04-29T06:51:33.117170+00:00"}, {"action": "AUTO_CLASSIFY_INGREDIENT_TYPE",
    "changes": "set ingredient_type=STOCK_SOLUTION (name matches solution pattern
    ''phosphate buffer'')", "curator": "auto_classify_ingredient_type", "llm_assisted":
    false, "timestamp": "2026-05-02T03:12:19.854401+00:00"}, {"action": "AUTO_UPGRADE_TO_NCIT",
    "changes": "primary UNMAPPED_0274 \u2192 NCIT:C29321 (strategy=stem-match)", "curator":
    "resolve_unmapped_v2", "llm_assisted": false, "timestamp": "2026-05-02T03:18:21.960132+00:00"},
    {"action": "CORRECTED", "changes": "Changed identifier from NCIT:C29321 to kgmicrobe.ingredient:potassium_phosphate_buffer
    and retained NCIT:C29321 only as CLOSE_MATCH. Potassium phosphate buffer is a
    formulation variant, not identical to the generic phosphate buffer class.", "curator":
    "ingredient_mapping_review_2026_05_05", "llm_assisted": false, "new_status": "MAPPED",
    "previous_status": "MAPPED", "timestamp": "2026-05-05T00:00:00+00:00"}, {"action":
    "ANNOTATED", "changes": "Added media role: BUFFER (confidence: 0.80)", "curator":
    "infer_roles_from_name_lists", "timestamp": "2026-06-03T02:06:01.748066+00:00"},
    {"action": "ANNOTATED", "changes": "Migrated legacy media_roles to role facets
    (#128): BUFFER -> physicochemical_roles.BUFFER", "curator": "migrate_media_roles_to_facets",
    "timestamp": "2026-07-20T00:00:00+00:00"}, {"action": "CORRECTED", "changes":
    "occurrence_statistics 2/2 -> 44/44 (media_count/total_occurrences), derived from
    distinct CultureMech recipe ids in the #337 occurrence table. The prior values
    came from the importer retired in #453, whose media_count counted a list truncated
    to 50 examples (#449). [source=ingredient_occurrences.tsv culturemech_rev=15a4da5c08
    rows=194137 distinct_recipes=15257]", "curator": "refresh_occurrence_statistics",
    "timestamp": "2026-08-27T03:16:39.519736+00:00"}, {"action": "ADDED_SYNONYMS",
    "changes": "Added 4 CultureMech recipe surface form(s) that folded onto this record''s
    published label but were absent from MIM''s label index, so CultureMech could
    not resolve them: ''Potassium phosphate buffer (0.01 M, pH 7.2)'' (x1 CultureMech
    mentions); ''Potassium phosphate buffer (0.02 M, pH 7.0)'' (x1 CultureMech mentions);
    ''Potassium phosphate buffer (1 M, pH 7.1)'' (x1 CultureMech mentions); ''Potassium
    phosphate buffer* (see below)'' (x1 CultureMech mentions). Source: culturemech:output/ingredient_occurrences.tsv.",
    "curator": "claude_culturemech_alias_backfill", "llm_assisted": false, "timestamp":
    "2026-08-30T04:48:06.233536+00:00"}], "identifier": "kgmicrobe.ingredient:potassium_phosphate_buffer",
    "mapping": {"evidence": [{"evidence_type": "CURATOR_JUDGMENT", "notes": "Potassium
    phosphate buffer is a formulation variant, not identical to the generic phosphate
    buffer class.", "source": "ingredient_mapping_review_2026-05-05"}], "mapping_quality":
    "CLOSE_MATCH", "ontology_id": "NCIT:C29321", "ontology_label": "Phosphate Buffer",
    "ontology_source": "NCIT"}}'
  snapshot_sha256: 9a33ce5d93f8928878ab1309f834d49f505d27abf4d5ee41e23b79a40a2ac40e
- evidence_id: ev-7d01fe3478491965
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Potassium_Phosphate_Buffer
  accessed_at: '2026-10-11T03:08:52Z'
  support: supports
  summary: '[{"comment": "", "confidence": "0.9", "data_row": 2327, "mapping_date":
    "2026-08-30", "mapping_justification": "semapv:ManualMappingCuration", "object_id":
    "NCIT:C29321", "object_label": "Phosphate Buffer", "object_source": "obo:ncit.owl",
    "other": "Potassium phosphate buffer (0.01 M, pH 7.2)|Potassium phosphate buffer
    (0.02 M, pH 7.0)|Potassium phosphate buffer (1 M, pH 7.1)|Potassium phosphate
    buffer* (see below)", "predicate_id": "skos:closeMatch", "source": "MIM:ingredient_mapping_review_2026-05-05|MIM:curator=claude_culturemech_alias_backfill",
    "subject_id": "MIM:Potassium_Phosphate_Buffer", "subject_label": "Potassium phosphate
    buffer", "validation_method": "none|UNKNOWN_TERM|2026-07-07"}, {"comment": "Registry/identity
    row preserving kgmicrobe.ingredient:potassium_phosphate_buffer alongside parent
    NCIT:C29321.", "confidence": "0.99", "data_row": 2328, "mapping_date": "2026-08-30",
    "mapping_justification": "semapv:ManualMappingCuration", "object_id": "kgmicrobe.ingredient:potassium_phosphate_buffer",
    "object_label": "Potassium phosphate buffer", "object_source": "kgm:ingredient",
    "other": "", "predicate_id": "skos:exactMatch", "source": "MIM:ingredient_mapping_review_2026-05-05|MIM:curator=claude_culturemech_alias_backfill",
    "subject_id": "MIM:Potassium_Phosphate_Buffer", "subject_label": "Potassium phosphate
    buffer", "validation_method": "none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-a692d3e165ce1613
  kind: prior_review
  reference: reports/yaml_record_review/Potassium_Phosphate_Buffer.md
  locator: Complete historical report, including Verdict and Recommended Edits
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Historical interpretation was read in full; it is not fresh source adjudication.
  snapshot_sha256: 884a3c1ac80ea7503bc943cac7d9eef7ff8d329cc1b7da000b75ab605e4019e0
  quote: '# `data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml`


    **Verdict**: needs curation, major issue.


    **Identity**: `Potassium phosphate buffer` is preserved as the local exact identity
    `kgmicrobe.ingredient:potassium_phosphate_buffer` with a `CLOSE_MATCH` parent
    row to `NCIT:C29321` / `Phosphate Buffer`. That row shape correctly avoids equating
    a potassium-buffer formulation family with the generic NCIT phosphate-buffer class.


    **Validation**: `uv run --frozen python scripts/validate_strict.py ... Potassium_Phosphate_Buffer.yaml
    ...` passed for the 5-file batch with 0 ERROR rows. `uv run --frozen linkml-term-validator
    validate-data data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml
    -t IngredientRecord --labels` passed.


    **Evidence**: The 2026-05-05 curation event supports keeping the local exact identity
    plus NCIT close row, and final SSSOM rows 2401 and 2402 preserve both surfaces.
    However, row 2401 still exports concentration- and pH-qualified recipe text, plus
    `Potassium phosphate buffer* (see below)`, as `other` synonyms. Those labels are
    formulation-specific recipe surfaces, not general names for the exact local registry
    subject. The active `physicochemical_roles.BUFFER` assertion is still only a `COMPUTATIONAL_PREDICTION`
    from the `infer_roles_from_name_lists` rule with the curator note `Provisional
    role from a curated name-pattern rule; review recommended.`


    **Completeness**: The record has 44 source occurrences and the correct local identity
    shape, but it has no component or concentration model that can represent the distinct
    0.01 M, 0.02 M, and 1 M pH-specific formulations now living as raw synonyms. An
    ignored/hidden local search over `data/ingredients`, `data/curated`, `mappings`,
    `reports`, `scripts`, `src`, `tests`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv`
    found the expected final NCIT close row, local exact row, and corresponding Sodium_Potassium_Phosphate_Buffer
    sibling pattern.


    **Recommended Edits**: In `data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml`,
    move the pH- and molarity-qualified labels out of active synonyms or teach the
    SSSOM builder to filter them from `other`. Replace the provisional `BUFFER` role
    with source-backed evidence or remove it, and add component/concentration recipes
    if a source can define each buffer formulation. Synchronize `data/curated/mapped_ingredients.yaml`,
    regenerate SSSOM, and rerun strict validation plus `scripts/validate_sssom_invariants.py`.

    '
- evidence_id: ev-cfeb1b367b6f9c64
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
  locator: findings[finding_id=f-3339000e63c2dccf]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-3339000e63c2dccf in 20261011T024638Z-mim-reconcile-all-batch-10
  snapshot_sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
- evidence_id: ev-2915a0c7cc5ef760
  kind: prior_review
  reference: reviews/structured/20261011T030852Z-mim-token-scope-reassessment/review.yaml
  locator: findings[finding_id=scope-f-f582ea830b4f370d]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding scope-f-f582ea830b4f370d in 20261011T030852Z-mim-token-scope-reassessment
  snapshot_sha256: 42a76b000bcbd07b426f6bad61b124b11ec08d8977783a67b732b01754f7c609
assessments:
- assessment_id: a-673c9c948ee00a8e
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-4190c0ee5976447a
  evidence_ids:
  - ev-6bdceef7ba6aa436
  - ev-84c339f9b2e6b5d1
  - ev-8ff94a6ea1085255
  - ev-5a185a31636016cb
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-09f8a6809f0c3399
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-4190c0ee5976447a
  evidence_ids:
  - ev-afd6d431ee989359
  - ev-6bdceef7ba6aa436
  - ev-f71c711fe7c99148
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T10:16:34Z;
    reviewed SHA-256=9a33ce5d93f8928878ab1309f834d49f505d27abf4d5ee41e23b79a40a2ac40e;
    current SHA-256=9a33ce5d93f8928878ab1309f834d49f505d27abf4d5ee41e23b79a40a2ac40e;
    hash_changed=False. Reports=["reports/yaml_record_review/Potassium_Phosphate_Buffer.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    buffer identity passes, but final SSSOM exports pH/molarity recipe labels and
    BUFFER is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-afd6d431ee989359
    - ev-6bdceef7ba6aa436
  - name: legacy-native-ids
    value: '["SEM:60203fb718c81304bf6b","SEM:985f37eab0ffab7d93e8"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-6bdceef7ba6aa436
    - ev-afd6d431ee989359
    - ev-f71c711fe7c99148
- assessment_id: a-fa016998b137038b
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-4190c0ee5976447a
  evidence_ids:
  - ev-afd6d431ee989359
  - ev-fa016998b137038b
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-afd6d431ee989359
    - ev-fa016998b137038b
- assessment_id: a-532b6872ec163537
  area: nomenclature
  topic: Unresolved recipe-reference or truncated-concentration synonyms
  outcome: concern
  summary: 'Historical tokens are still present on the exact-subject SSSOM rows: [{"reason":"unresolved
    recipe cross-reference in a resolving synonym","token":"Potassium phosphate buffer*
    (see below)"}]. Truncated concentration strings and context-dependent instructions
    need scoped curation. This check does not reject catalog/RAW_TEXT synonyms as
    a class.'
  target_ids:
  - record-4190c0ee5976447a
  evidence_ids:
  - ev-afd6d431ee989359
  - ev-8ff94a6ea1085255
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-afd6d431ee989359
    - ev-8ff94a6ea1085255
- assessment_id: scope-f-f582ea830b4f370d
  area: nomenclature
  topic: Certainty correction for the exact token observation
  outcome: unknown
  summary: Token presence remains reproducible, but the earlier pattern-based observation
    did not establish whether the exact source label denotes this subject or a different
    preparation. Fresh source-context adjudication is required before a confirmed
    defect or label removal. This successor corrects certainty only; it does not establish
    that the token is valid or that another identity allegation is fixed.
  target_ids:
  - record-4190c0ee5976447a
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-8bb59eaf8b6e66f4
  - ev-745bc0e8e18adc16
  - ev-7d01fe3478491965
  - ev-a692d3e165ce1613
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Source-scope question only, not a disposition of the complete historical
      report.
    evidence_ids:
    - ev-823412d1eacb6795
    - ev-8bb59eaf8b6e66f4
    - ev-745bc0e8e18adc16
    - ev-7d01fe3478491965
    - ev-a692d3e165ce1613
findings:
- finding_id: rec-f-3339000e63c2dccf
  issue_key: mim-reconciliation-role-support-4190c0ee5976447a
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Potassium phosphate buffer'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-4190c0ee5976447a
  evidence_ids:
  - ev-afd6d431ee989359
  - ev-fa016998b137038b
  - ev-cfeb1b367b6f9c64
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml
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
    review_id: 20261011T024638Z-mim-reconcile-all-batch-10
    finding_id: f-3339000e63c2dccf
- finding_id: rec-scope-f-f582ea830b4f370d
  issue_key: mim-reconciliation-exported-context-tokens-4190c0ee5976447a
  category: nomenclature
  severity: major
  status: deferred
  certainty: provisional
  title: 'Adjudicate source scope of exported tokens: Potassium phosphate buffer'
  description: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed.
  target_ids:
  - record-4190c0ee5976447a
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-8bb59eaf8b6e66f4
  - ev-745bc0e8e18adc16
  - ev-7d01fe3478491965
  - ev-a692d3e165ce1613
  - ev-2915a0c7cc5ef760
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml
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
    finding_id: scope-f-f582ea830b4f370d
actions:
- action_id: rec-action-3339000e63c2dccf
  description: 'Reassess prediction-only role support: Potassium phosphate buffer'
  finding_ids:
  - rec-f-3339000e63c2dccf
  target_ids:
  - record-4190c0ee5976447a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Potassium_Phosphate_Buffer.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-10, 20261011T030852Z-mim-token-scope-reassessment.
```
