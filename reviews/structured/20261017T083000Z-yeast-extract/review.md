# Per-record structured review: Yeast_Extract (data/ingredients/mapped/Yeast_Extract.yaml)

- Review: 20261017T083000Z-yeast-extract
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Yeast_Extract (data/ingredients/mapped/Yeast_Extract.yaml, record-4efe2f6907f0d4fc, mapping_status=MAPPED). Records 1 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Yeast_Extract.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Yeast_Extract.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-4efe2f6907f0d4fc | data/ingredients/mapped/Yeast_Extract.yaml | maintained | Yeast_Extract |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-4efe2f6907f0d4fc | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-4efe2f6907f0d4fc | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-4efe2f6907f0d4fc | Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-4efe2f6907f0d4fc.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-4efe2f6907f0d4fc.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:32:07Z; reviewed SHA-256=e7cdc5aa92020487a97c08814514fa48b852ff48c78a1d1890b69afaaf372d28; current SHA-256=e7cdc5aa92020487a97c08814514fa48b852ff48c78a1d1890b69afaaf372d28; hash_changed=False. Reports=["reports/yaml_record_review/Yeast_Extract.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact FoodOn yeast extract identity passes, but final SSSOM exports catalog variants and malformed labels, and PROTEIN_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-4efe2f6907f0d4fc.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

### Unresolved recipe-reference or truncated-concentration synonyms

nomenclature: concern. Targets: record-4efe2f6907f0d4fc.

Historical tokens are still present on the exact-subject SSSOM rows: [{"reason":"truncated concentration-qualified label with unbalanced parentheses","token":"Yeast Extract (0.01 %"}]. Truncated concentration strings and context-dependent instructions need scoped curation. This check does not reject catalog/RAW_TEXT synonyms as a class.

### Certainty correction for the exact token observation

nomenclature: unknown. Targets: record-4efe2f6907f0d4fc.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed. A damaged spelling is observable, but the mapping contract permits damaged raw source forms when they still resolve to the same substance; malformed punctuation alone does not settle identity scope.

## Findings

### rec-f-27fdd8e3c95cc855: Reassess prediction-only role support: Yeast extract

major / open / confirmed; issue key: mim-reconciliation-role-support-4efe2f6907f0d4fc.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

### rec-scope-f-397b1df68e373137: Adjudicate source scope of exported tokens: Yeast extract

major / deferred / provisional; issue key: mim-reconciliation-exported-context-tokens-4efe2f6907f0d4fc.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed. A damaged spelling is observable, but the mapping contract permits damaged raw source forms when they still resolve to the same substance; malformed punctuation alone does not settle identity scope.

Disposition: Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed. A damaged spelling is observable, but the mapping contract permits damaged raw source forms when they still resolve to the same substance; malformed punctuation alone does not settle identity scope.

## Recommended Actions And Acceptance Checks

### rec-action-27fdd8e3c95cc855

Reassess prediction-only role support: Yeast extract

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-b7c4416499778ebf | data/ingredients/mapped/Yeast_Extract.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2073],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:03315426","line":2075,"mapping_status":"MAPPED","ontology_id":"FOODON:03315426","preferred_term":"Yeast extract"}],"identifier":"FOODON:03315426","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7617,"edge_count":7617,"occurrences":7697},"occurrence_statistics":{"media_count":7617,"total_occurrences":7697},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"FOODON:03315426","ontology_label":"yeast extract","ontology_source":"FOODON"},"preferred_term":"Yeast extract","sssom_rows":[{"data_row":2951,"object_id":"FOODON:03315426","object_label":"yeast extract","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Yeast_Extract","synonym_count":36} |
| ev-03b76ec7595397b0 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2073] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-b4b66e47d09fff06 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Yeast_Extract; data-row positions=[2951] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2951,"object_id":"FOODON:03315426","object_label":"yeast extract","other":"Yeast extract(Bacto, Difco)&#124;Yeast extract(CAS: 8013-01-2)&#124;Yeast extract (BD-Difco)&#124;Bacto Yeast Extract (Difco)&#124;Yeast extract (OXOID)&#124;Bacto yeast extract&#124;Yeast extract (Difco)&#124;Yeast extract (BD--Difco)&#124;Yeast Extract (BD 212750)&#124;Yeast extract (Difco or Oxoid)&#124;Yeast extract (BD Bacto)&#124;Bacto Yeast  Extract (Difco)&#124;Yeast extract (BD-BBL)&#124;Yeast extract (Oxoid LP0021, BD 212750)&#124;Yeast Extract (BD 211928)&#124;Difco Bacto-yeast extract&#124;Dried yeast extract S (Wako)&#124;Yeast Extract (BD, 212750)&#124;Yeast extract(Oxoid)&#124;Yeast extract (BBL)&#124;Bacto-yeast extract&#124;Yeast Extract(Difco)&#124;yeast extract (BD Difco)&#124;yeast extract (Nacalai Tesque, Kyoto, Japan)&#124;Yeast Extract (Hardy C7340)&#124;Liquid yeast extract (Flow)&#124;Fresh Baker's Yeast Extract&#124;Yeast Extract (0.01 %&#124;Fresh Baker\u2019s Yeast Extract&#124;CAS:8013-01-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Yeast_Extract","validation_method":"OLS:foodon&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-ffa5f7d8c39bbea1 | docs/data/mapped_ingredients.csv; CSV lines=[2075] | supports | Published identity and count rows inspected: [{"identifier":"FOODON:03315426","line":2075,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"7617","ontology_id":"FOODON:03315426","preferred_term":"Yeast extract","total_occurrences":"7697"}] |
| ev-d8b50ecf394b7a07 | reports/yaml_record_review/Yeast_Extract.md; &#96;data/ingredients/mapped/Yeast_Extract.yaml&#96;:2; Verdict:4; Identity:11; Validation:25; Evidence:35; Issues:44; Completeness:58; Recommended Edits:64 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-1fc7a06886a752cf | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1358,1924] | context_only | [{"current_record_sha256":"e7cdc5aa92020487a97c08814514fa48b852ff48c78a1d1890b69afaaf372d28","finding_id":"SEM:05e832d9297c26f5a017","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"e7cdc5aa92020487a97c08814514fa48b852ff48c78a1d1890b69afaaf372d28","finding_id":"SEM:38572e0ff78bd4e180d6","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-f1dd03e810d4997b | data/ingredients/mapped/Yeast_Extract.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2073],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:03315426","line":2075,"mapping_status":"MAPPED","ontology_id":"FOODON:03315426","preferred_term":"Yeast extract"}],"identifier":"FOODON:03315426","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7617,"edge_count":7617,"occurrences":7697},"occurrence_statistics":{"media_count":7617,"total_occurrences":7697},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"FOODON:03315426","ontology_label":"yeast extract","ontology_source":"FOODON"},"preferred_term":"Yeast extract","sssom_rows":[{"data_row":2951,"object_id":"FOODON:03315426","object_label":"yeast extract","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Yeast_Extract","synonym_count":36} |
| ev-823412d1eacb6795 | MAPPING_SEMANTICS.md; Sections on REJECTED_LABEL and the damaged-label RAW_TEXT carve-out | supports | Raw spellings may remain resolvable when they denote the same substance. Wrong-identity labels must not resolve. A recipe-pointer pattern alone does not adjudicate that distinction. |
| ev-0701e78e991c4118 | reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml; findings[finding_id=f-397b1df68e373137] | context_only | Exact earlier occurrence has open/confirmed status, based on exported-token presence and historical report text. |
| ev-5175fd560468ba85 | data/ingredients/mapped/Yeast_Extract.yaml; identifier, ontology_mapping, synonyms and curation_history | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2073],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:03315426","line":2075,"mapping_status":"MAPPED","ontology_id":"FOODON:03315426","preferred_term":"Yeast extract"}],"identifier":"FOODON:03315426","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7617,"edge_count":7617,"occurrences":7697},"occurrence_statistics":{"media_count":7617,"total_occurrences":7697},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"FOODON:03315426","ontology_label":"yeast extract","ontology_source":"FOODON"},"preferred_term":"Yeast extract","sssom_rows":[{"data_row":2951,"object_id":"FOODON:03315426","object_label":"yeast extract","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Yeast_Extract","synonym_count":36} |
| ev-c84617d1a202e069 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Yeast_Extract; data-row positions=[2951] | supports | Current exact-subject rows, including complete other payload: [{"data_row":2951,"object_id":"FOODON:03315426","object_label":"yeast extract","other":"Yeast extract(Bacto, Difco)&#124;Yeast extract(CAS: 8013-01-2)&#124;Yeast extract (BD-Difco)&#124;Bacto Yeast Extract (Difco)&#124;Yeast extract (OXOID)&#124;Bacto yeast extract&#124;Yeast extract (Difco)&#124;Yeast extract (BD--Difco)&#124;Yeast Extract (BD 212750)&#124;Yeast extract (Difco or Oxoid)&#124;Yeast extract (BD Bacto)&#124;Bacto Yeast  Extract (Difco)&#124;Yeast extract (BD-BBL)&#124;Yeast extract (Oxoid LP0021, BD 212750)&#124;Yeast Extract (BD 211928)&#124;Difco Bacto-yeast extract&#124;Dried yeast extract S (Wako)&#124;Yeast Extract (BD, 212750)&#124;Yeast extract(Oxoid)&#124;Yeast extract (BBL)&#124;Bacto-yeast extract&#124;Yeast Extract(Difco)&#124;yeast extract (BD Difco)&#124;yeast extract (Nacalai Tesque, Kyoto, Japan)&#124;Yeast Extract (Hardy C7340)&#124;Liquid yeast extract (Flow)&#124;Fresh Baker's Yeast Extract&#124;Yeast Extract (0.01 %&#124;Fresh Baker\u2019s Yeast Extract&#124;CAS:8013-01-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Yeast_Extract","validation_method":"OLS:foodon&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-ef345ac5a6dc1108 | reports/yaml_record_review/Yeast_Extract.md; Complete historical report, including Verdict and Recommended Edits | context_only | Historical interpretation was read in full; it is not fresh source adjudication. |
| ev-dfd2449f4d0c27f9 | reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml; findings[finding_id=f-27fdd8e3c95cc855] | context_only | Predecessor structured review finding f-27fdd8e3c95cc855 in 20261011T024639Z-mim-reconcile-all-batch-12 |
| ev-c63305e818302650 | reviews/structured/20261011T030852Z-mim-token-scope-reassessment/review.yaml; findings[finding_id=scope-f-397b1df68e373137] | context_only | Predecessor structured review finding scope-f-397b1df68e373137 in 20261011T030852Z-mim-token-scope-reassessment |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024639Z-mim-reconcile-all-batch-12, 20261011T030852Z-mim-token-scope-reassessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-yeast-extract
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Yeast_Extract (data/ingredients/mapped/Yeast_Extract.yaml)'
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
summary: Per-record structured review for Yeast_Extract (data/ingredients/mapped/Yeast_Extract.yaml,
  record-4efe2f6907f0d4fc, mapping_status=MAPPED). Records 1 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Yeast_Extract.yaml
    sha256: e7cdc5aa92020487a97c08814514fa48b852ff48c78a1d1890b69afaaf372d28
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
  - path: reports/yaml_record_review/Yeast_Extract.md
    sha256: e1920c4292a8d9d9155fcb45d62306b5f2f645732eac0501e49b634c3d4c6d73
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
  - path: MAPPING_SEMANTICS.md
    sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805
    role: context
targets:
- target_id: record-4efe2f6907f0d4fc
  path: data/ingredients/mapped/Yeast_Extract.yaml
  label: Yeast_Extract
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Yeast_Extract.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Yeast_Extract.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Yeast_Extract.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-4efe2f6907f0d4fc
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-4efe2f6907f0d4fc
  evidence_ids:
  - ev-b7c4416499778ebf
  - ev-03b76ec7595397b0
  - ev-b4b66e47d09fff06
  - ev-ffa5f7d8c39bbea1
  - ev-f1dd03e810d4997b
  - ev-5175fd560468ba85
  - ev-c84617d1a202e069
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-4efe2f6907f0d4fc
  evidence_ids:
  - ev-b7c4416499778ebf
  - ev-1fc7a06886a752cf
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12
    and semantic review dispositions on HEAD.
  target_ids:
  - record-4efe2f6907f0d4fc
  evidence_ids:
  - ev-d8b50ecf394b7a07
  - ev-1fc7a06886a752cf
  - ev-0701e78e991c4118
  - ev-ef345ac5a6dc1108
  - ev-dfd2449f4d0c27f9
  - ev-c63305e818302650
evidence:
- evidence_id: ev-b7c4416499778ebf
  kind: record_content
  reference: data/ingredients/mapped/Yeast_Extract.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2073],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:03315426","line":2075,"mapping_status":"MAPPED","ontology_id":"FOODON:03315426","preferred_term":"Yeast
    extract"}],"identifier":"FOODON:03315426","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7617,"edge_count":7617,"occurrences":7697},"occurrence_statistics":{"media_count":7617,"total_occurrences":7697},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"FOODON:03315426","ontology_label":"yeast
    extract","ontology_source":"FOODON"},"preferred_term":"Yeast extract","sssom_rows":[{"data_row":2951,"object_id":"FOODON:03315426","object_label":"yeast
    extract","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Yeast_Extract","synonym_count":36}'
  snapshot_sha256: e7cdc5aa92020487a97c08814514fa48b852ff48c78a1d1890b69afaaf372d28
- evidence_id: ev-03b76ec7595397b0
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2073]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-b4b66e47d09fff06
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Yeast_Extract; data-row positions=[2951]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2951,"object_id":"FOODON:03315426","object_label":"yeast
    extract","other":"Yeast extract(Bacto, Difco)|Yeast extract(CAS: 8013-01-2)|Yeast
    extract (BD-Difco)|Bacto Yeast Extract (Difco)|Yeast extract (OXOID)|Bacto yeast
    extract|Yeast extract (Difco)|Yeast extract (BD--Difco)|Yeast Extract (BD 212750)|Yeast
    extract (Difco or Oxoid)|Yeast extract (BD Bacto)|Bacto Yeast  Extract (Difco)|Yeast
    extract (BD-BBL)|Yeast extract (Oxoid LP0021, BD 212750)|Yeast Extract (BD 211928)|Difco
    Bacto-yeast extract|Dried yeast extract S (Wako)|Yeast Extract (BD, 212750)|Yeast
    extract(Oxoid)|Yeast extract (BBL)|Bacto-yeast extract|Yeast Extract(Difco)|yeast
    extract (BD Difco)|yeast extract (Nacalai Tesque, Kyoto, Japan)|Yeast Extract
    (Hardy C7340)|Liquid yeast extract (Flow)|Fresh Baker''s Yeast Extract|Yeast Extract
    (0.01 %|Fresh Baker\u2019s Yeast Extract|CAS:8013-01-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Yeast_Extract","validation_method":"OLS:foodon|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-ffa5f7d8c39bbea1
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2075]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"FOODON:03315426","line":2075,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"7617","ontology_id":"FOODON:03315426","preferred_term":"Yeast
    extract","total_occurrences":"7697"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-d8b50ecf394b7a07
  kind: prior_review
  reference: reports/yaml_record_review/Yeast_Extract.md
  locator: '`data/ingredients/mapped/Yeast_Extract.yaml`:2; Verdict:4; Identity:11;
    Validation:25; Evidence:35; Issues:44; Completeness:58; Recommended Edits:64'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: e1920c4292a8d9d9155fcb45d62306b5f2f645732eac0501e49b634c3d4c6d73
  quote: "Issues:\n- Major: the final exact `FOODON:03315426` row exports many vendor/catalog\n\
    \  labels as `other` synonyms, including BD, Difco, Oxoid, BBL, Nacalai Tesque,\n\
    \  Hardy, Wako, and Flow product-specific strings.\n- Major: the same final row\
    \ exports the truncated concentration string\n  `Yeast Extract (0.01 %`, which\
    \ is not a complete or reusable synonym.\n- Major: the same final row also exports\
    \ source-decorated raw strings such as\n  `Yeast extract(CAS: 8013-01-2)` and\
    \ the duplicate Fresh Baker label with a\n  non-ASCII curly apostrophe.\n- Major:\
    \ `nutritional_roles.PROTEIN_SOURCE` rests on\n  `COMPUTATIONAL_PREDICTION` evidence\
    \ whose note says the curated name-pattern\n  rule is provisional and still needs\
    \ review.\n\nRecommended Edits:\n- Remove or suppress raw CAS-decorated, concentration-truncated,\
    \ non-ASCII\n  duplicate, and vendor/catalog-specific labels from final SSSOM\
    \ `other`.\n- Replace or remove this record's `PROTEIN_SOURCE` role; keep it only\
    \ if a\n  maintained source supports yeast extract as a protein source in media.\n\
    - Rebuild SSSOM and rerun strict validation, SSSOM invariant validation, and the\n\
    \  cross-record `other` synonym audit."
- evidence_id: ev-1fc7a06886a752cf
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1358,1924]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"e7cdc5aa92020487a97c08814514fa48b852ff48c78a1d1890b69afaaf372d28","finding_id":"SEM:05e832d9297c26f5a017","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"e7cdc5aa92020487a97c08814514fa48b852ff48c78a1d1890b69afaaf372d28","finding_id":"SEM:38572e0ff78bd4e180d6","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-f1dd03e810d4997b
  kind: record_content
  reference: data/ingredients/mapped/Yeast_Extract.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2073],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:03315426","line":2075,"mapping_status":"MAPPED","ontology_id":"FOODON:03315426","preferred_term":"Yeast
    extract"}],"identifier":"FOODON:03315426","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7617,"edge_count":7617,"occurrences":7697},"occurrence_statistics":{"media_count":7617,"total_occurrences":7697},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"FOODON:03315426","ontology_label":"yeast
    extract","ontology_source":"FOODON"},"preferred_term":"Yeast extract","sssom_rows":[{"data_row":2951,"object_id":"FOODON:03315426","object_label":"yeast
    extract","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Yeast_Extract","synonym_count":36}'
  snapshot_sha256: e7cdc5aa92020487a97c08814514fa48b852ff48c78a1d1890b69afaaf372d28
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
- evidence_id: ev-0701e78e991c4118
  kind: prior_review
  reference: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
  locator: findings[finding_id=f-397b1df68e373137]
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Exact earlier occurrence has open/confirmed status, based on exported-token
    presence and historical report text.
  snapshot_sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
  quote: '{"category": "nomenclature", "certainty": "confirmed", "description": "Historical
    tokens are still present on the exact-subject SSSOM rows: [{\"reason\":\"truncated
    concentration-qualified label with unbalanced parentheses\",\"token\":\"Yeast
    Extract (0.01 %\"}]. Truncated concentration strings and context-dependent instructions
    need scoped curation. This check does not reject catalog/RAW_TEXT synonyms as
    a class.", "evidence_ids": ["ev-d8b50ecf394b7a07", "ev-b4b66e47d09fff06"], "external_issues":
    ["https://github.com/CultureBotAI/MediaIngredientMech/issues/718"], "field_paths":
    ["synonyms", "SSSOM.other"], "finding_id": "f-397b1df68e373137", "issue_key":
    "mim-reconciliation-exported-context-tokens-4efe2f6907f0d4fc", "owner_paths":
    [{"path": "data/ingredients/mapped/Yeast_Extract.yaml", "repository": "CultureBotAI/MediaIngredientMech",
    "role": "maintained ingredient"}], "severity": "major", "status": "open", "tags":
    ["reconciliation", "bundle-by-owner", "exported-context-tokens"], "target_ids":
    ["record-4efe2f6907f0d4fc"], "title": "Review nonportable exported tokens: Yeast
    extract"}'
- evidence_id: ev-5175fd560468ba85
  kind: record_content
  reference: data/ingredients/mapped/Yeast_Extract.yaml
  locator: identifier, ontology_mapping, synonyms and curation_history
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2073],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:03315426","line":2075,"mapping_status":"MAPPED","ontology_id":"FOODON:03315426","preferred_term":"Yeast
    extract"}],"identifier":"FOODON:03315426","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7617,"edge_count":7617,"occurrences":7697},"occurrence_statistics":{"media_count":7617,"total_occurrences":7697},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"FOODON:03315426","ontology_label":"yeast
    extract","ontology_source":"FOODON"},"preferred_term":"Yeast extract","sssom_rows":[{"data_row":2951,"object_id":"FOODON:03315426","object_label":"yeast
    extract","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Yeast_Extract","synonym_count":36}'
  snapshot_sha256: e7cdc5aa92020487a97c08814514fa48b852ff48c78a1d1890b69afaaf372d28
- evidence_id: ev-c84617d1a202e069
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Yeast_Extract; data-row positions=[2951]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2951,"object_id":"FOODON:03315426","object_label":"yeast
    extract","other":"Yeast extract(Bacto, Difco)|Yeast extract(CAS: 8013-01-2)|Yeast
    extract (BD-Difco)|Bacto Yeast Extract (Difco)|Yeast extract (OXOID)|Bacto yeast
    extract|Yeast extract (Difco)|Yeast extract (BD--Difco)|Yeast Extract (BD 212750)|Yeast
    extract (Difco or Oxoid)|Yeast extract (BD Bacto)|Bacto Yeast  Extract (Difco)|Yeast
    extract (BD-BBL)|Yeast extract (Oxoid LP0021, BD 212750)|Yeast Extract (BD 211928)|Difco
    Bacto-yeast extract|Dried yeast extract S (Wako)|Yeast Extract (BD, 212750)|Yeast
    extract(Oxoid)|Yeast extract (BBL)|Bacto-yeast extract|Yeast Extract(Difco)|yeast
    extract (BD Difco)|yeast extract (Nacalai Tesque, Kyoto, Japan)|Yeast Extract
    (Hardy C7340)|Liquid yeast extract (Flow)|Fresh Baker''s Yeast Extract|Yeast Extract
    (0.01 %|Fresh Baker\u2019s Yeast Extract|CAS:8013-01-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Yeast_Extract","validation_method":"OLS:foodon|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-ef345ac5a6dc1108
  kind: prior_review
  reference: reports/yaml_record_review/Yeast_Extract.md
  locator: Complete historical report, including Verdict and Recommended Edits
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Historical interpretation was read in full; it is not fresh source adjudication.
  snapshot_sha256: e1920c4292a8d9d9155fcb45d62306b5f2f645732eac0501e49b634c3d4c6d73
  quote: "# `data/ingredients/mapped/Yeast_Extract.yaml`\n\n## Verdict\n\nNeeds curation.\
    \ The exact `FOODON:03315426` yeast extract identity, aggregate\nrow, and final\
    \ exact SSSOM predicate pass, but final SSSOM exports many\nvendor/catalog variants\
    \ plus a truncated concentration string, and the\n`PROTEIN_SOURCE` role is still\
    \ a provisional name-pattern inference.\n\n## Identity\n\n- Reviewed record: `data/ingredients/mapped/Yeast_Extract.yaml`.\n\
    - Identifier and grounding: `identifier: FOODON:03315426` with matching\n  `ontology_mapping.ontology_id`,\
    \ label `yeast extract`, source `FOODON`,\n  `mapping_quality: EXACT_MATCH`, `mapping_status:\
    \ MAPPED`, and\n  `ingredient_type: UNDEFINED_MIXTURE`.\n- CAS RN: `8013-01-2`.\n\
    - Synonyms: raw CultureMech and MicrobeDecoder strings, exact yeast-extract\n\
    \  synonyms, related Fresh Baker labels, and many manual catalog variants.\n-\
    \ Occurrences: 7,697 total occurrences across 7,617 CultureMech media, plus 46\n\
    \  MicrobeDecoder metabolite-utilization occurrences.\n- Role: `PROTEIN_SOURCE`\
    \ with provisional curated name-pattern evidence.\n\n## Validation\n\n- `uv run\
    \ --frozen python scripts/validate_strict.py` on the 5-file batch from\n  `Xylotriose`\
    \ through `Yeast_Extract_Gluconate`: exited 0 and wrote zero ERROR\n  rows.\n\
    - Local aggregate comparison found this per-record file synchronized with its\n\
    \  keyed row in `data/curated/mapped_ingredients.yaml`.\n- Engine A label validation\
    \ was limited to the CHEBI-primary record in this\n  batch; this FoodOn row has\
    \ no CHEBI/OBO adapter for that focused check.\n\n## Evidence\n\n- Fresh OLS4\
    \ exact-label search for `yeast extract` in FoodOn found active\n  `FOODON:03315426`\
    \ with label `yeast extract`.\n- The final SSSOM row correctly has\n  `MIM:Yeast_Extract\
    \ skos:exactMatch FOODON:03315426`.\n- The final SSSOM row filters the exact duplicate\
    \ `Yeast Extract` and\n  `yeast extract` strings but still exports raw and catalog-qualified\
    \ labels.\n\n## Issues\n\n- Major: the final exact `FOODON:03315426` row exports\
    \ many vendor/catalog\n  labels as `other` synonyms, including BD, Difco, Oxoid,\
    \ BBL, Nacalai Tesque,\n  Hardy, Wako, and Flow product-specific strings.\n- Major:\
    \ the same final row exports the truncated concentration string\n  `Yeast Extract\
    \ (0.01 %`, which is not a complete or reusable synonym.\n- Major: the same final\
    \ row also exports source-decorated raw strings such as\n  `Yeast extract(CAS:\
    \ 8013-01-2)` and the duplicate Fresh Baker label with a\n  non-ASCII curly apostrophe.\n\
    - Major: `nutritional_roles.PROTEIN_SOURCE` rests on\n  `COMPUTATIONAL_PREDICTION`\
    \ evidence whose note says the curated name-pattern\n  rule is provisional and\
    \ still needs review.\n\n## Completeness\n\n- The exact FoodOn mapping, occurrence\
    \ count, aggregate copy, and final SSSOM\n  predicate agree.\n- The final synonym\
    \ set needs to be reduced to true yeast-extract labels.\n\n## Recommended Edits\n\
    \n- Remove or suppress raw CAS-decorated, concentration-truncated, non-ASCII\n\
    \  duplicate, and vendor/catalog-specific labels from final SSSOM `other`.\n-\
    \ Replace or remove this record's `PROTEIN_SOURCE` role; keep it only if a\n \
    \ maintained source supports yeast extract as a protein source in media.\n- Rebuild\
    \ SSSOM and rerun strict validation, SSSOM invariant validation, and the\n  cross-record\
    \ `other` synonym audit.\n"
- evidence_id: ev-dfd2449f4d0c27f9
  kind: prior_review
  reference: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
  locator: findings[finding_id=f-27fdd8e3c95cc855]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-27fdd8e3c95cc855 in 20261011T024639Z-mim-reconcile-all-batch-12
  snapshot_sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
- evidence_id: ev-c63305e818302650
  kind: prior_review
  reference: reviews/structured/20261011T030852Z-mim-token-scope-reassessment/review.yaml
  locator: findings[finding_id=scope-f-397b1df68e373137]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding scope-f-397b1df68e373137 in 20261011T030852Z-mim-token-scope-reassessment
  snapshot_sha256: 42a76b000bcbd07b426f6bad61b124b11ec08d8977783a67b732b01754f7c609
assessments:
- assessment_id: a-ef9d53dd36e13cd0
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-4efe2f6907f0d4fc
  evidence_ids:
  - ev-b7c4416499778ebf
  - ev-03b76ec7595397b0
  - ev-b4b66e47d09fff06
  - ev-ffa5f7d8c39bbea1
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-741c145043f4ae6c
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-4efe2f6907f0d4fc
  evidence_ids:
  - ev-d8b50ecf394b7a07
  - ev-b7c4416499778ebf
  - ev-1fc7a06886a752cf
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:32:07Z;
    reviewed SHA-256=e7cdc5aa92020487a97c08814514fa48b852ff48c78a1d1890b69afaaf372d28;
    current SHA-256=e7cdc5aa92020487a97c08814514fa48b852ff48c78a1d1890b69afaaf372d28;
    hash_changed=False. Reports=["reports/yaml_record_review/Yeast_Extract.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact FoodOn
    yeast extract identity passes, but final SSSOM exports catalog variants and malformed
    labels, and PROTEIN_SOURCE is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d8b50ecf394b7a07
    - ev-b7c4416499778ebf
  - name: legacy-native-ids
    value: '["SEM:05e832d9297c26f5a017","SEM:38572e0ff78bd4e180d6"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-b7c4416499778ebf
    - ev-d8b50ecf394b7a07
    - ev-1fc7a06886a752cf
- assessment_id: a-f1dd03e810d4997b
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-4efe2f6907f0d4fc
  evidence_ids:
  - ev-d8b50ecf394b7a07
  - ev-f1dd03e810d4997b
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d8b50ecf394b7a07
    - ev-f1dd03e810d4997b
- assessment_id: a-a6488c1a65f59bac
  area: nomenclature
  topic: Unresolved recipe-reference or truncated-concentration synonyms
  outcome: concern
  summary: 'Historical tokens are still present on the exact-subject SSSOM rows: [{"reason":"truncated
    concentration-qualified label with unbalanced parentheses","token":"Yeast Extract
    (0.01 %"}]. Truncated concentration strings and context-dependent instructions
    need scoped curation. This check does not reject catalog/RAW_TEXT synonyms as
    a class.'
  target_ids:
  - record-4efe2f6907f0d4fc
  evidence_ids:
  - ev-d8b50ecf394b7a07
  - ev-b4b66e47d09fff06
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d8b50ecf394b7a07
    - ev-b4b66e47d09fff06
- assessment_id: scope-f-397b1df68e373137
  area: nomenclature
  topic: Certainty correction for the exact token observation
  outcome: unknown
  summary: Token presence remains reproducible, but the earlier pattern-based observation
    did not establish whether the exact source label denotes this subject or a different
    preparation. Fresh source-context adjudication is required before a confirmed
    defect or label removal. This successor corrects certainty only; it does not establish
    that the token is valid or that another identity allegation is fixed. A damaged
    spelling is observable, but the mapping contract permits damaged raw source forms
    when they still resolve to the same substance; malformed punctuation alone does
    not settle identity scope.
  target_ids:
  - record-4efe2f6907f0d4fc
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-0701e78e991c4118
  - ev-5175fd560468ba85
  - ev-c84617d1a202e069
  - ev-ef345ac5a6dc1108
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Source-scope question only, not a disposition of the complete historical
      report.
    evidence_ids:
    - ev-823412d1eacb6795
    - ev-0701e78e991c4118
    - ev-5175fd560468ba85
    - ev-c84617d1a202e069
    - ev-ef345ac5a6dc1108
findings:
- finding_id: rec-f-27fdd8e3c95cc855
  issue_key: mim-reconciliation-role-support-4efe2f6907f0d4fc
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Yeast extract'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-4efe2f6907f0d4fc
  evidence_ids:
  - ev-d8b50ecf394b7a07
  - ev-f1dd03e810d4997b
  - ev-dfd2449f4d0c27f9
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Yeast_Extract.yaml
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
    review_id: 20261011T024639Z-mim-reconcile-all-batch-12
    finding_id: f-27fdd8e3c95cc855
- finding_id: rec-scope-f-397b1df68e373137
  issue_key: mim-reconciliation-exported-context-tokens-4efe2f6907f0d4fc
  category: nomenclature
  severity: major
  status: deferred
  certainty: provisional
  title: 'Adjudicate source scope of exported tokens: Yeast extract'
  description: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed. A damaged spelling is observable, but the mapping contract permits damaged
    raw source forms when they still resolve to the same substance; malformed punctuation
    alone does not settle identity scope.
  target_ids:
  - record-4efe2f6907f0d4fc
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-0701e78e991c4118
  - ev-5175fd560468ba85
  - ev-c84617d1a202e069
  - ev-ef345ac5a6dc1108
  - ev-c63305e818302650
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Yeast_Extract.yaml
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
    is fixed. A damaged spelling is observable, but the mapping contract permits damaged
    raw source forms when they still resolve to the same substance; malformed punctuation
    alone does not settle identity scope.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T030852Z-mim-token-scope-reassessment
    finding_id: scope-f-397b1df68e373137
actions:
- action_id: rec-action-27fdd8e3c95cc855
  description: 'Reassess prediction-only role support: Yeast extract'
  finding_ids:
  - rec-f-27fdd8e3c95cc855
  target_ids:
  - record-4efe2f6907f0d4fc
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Yeast_Extract.yaml
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
  with lineage to 20261011T024639Z-mim-reconcile-all-batch-12, 20261011T030852Z-mim-token-scope-reassessment.
```
