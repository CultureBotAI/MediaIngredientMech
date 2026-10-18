# Per-record structured review: Riboflavin (data/ingredients/mapped/Riboflavin.yaml)

- Review: 20261017T083000Z-riboflavin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Riboflavin (data/ingredients/mapped/Riboflavin.yaml, record-59776f859c41300d, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Riboflavin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Riboflavin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-59776f859c41300d | data/ingredients/mapped/Riboflavin.yaml | maintained | Riboflavin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-59776f859c41300d | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-59776f859c41300d | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-59776f859c41300d | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-59776f859c41300d.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-59776f859c41300d.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T12:11:07Z; reviewed SHA-256=b79fe5e134e627e7c95d6190e54c52b04f9d81a61ad381cb136b986430d80644; current SHA-256=b79fe5e134e627e7c95d6190e54c52b04f9d81a61ad381cb136b986430d80644; hash_changed=False. Reports=["reports/yaml_record_review/Riboflavin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:17015 identity passes, but final SSSOM exports raw concentration and recipe-pointer labels.

### Unresolved recipe-reference or truncated-concentration synonyms

nomenclature: concern. Targets: record-59776f859c41300d.

Historical tokens are still present on the exact-subject SSSOM rows: [{"reason":"unresolved recipe cross-reference in a resolving synonym","token":"Riboflavin (see below)"}]. Truncated concentration strings and context-dependent instructions need scoped curation. This check does not reject catalog/RAW_TEXT synonyms as a class.

### Certainty correction for the exact token observation

nomenclature: unknown. Targets: record-59776f859c41300d.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

## Findings

### rec-scope-f-b7808e84d7886285: Adjudicate source scope of exported tokens: Riboflavin

major / deferred / provisional; issue key: mim-reconciliation-exported-context-tokens-59776f859c41300d.

Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

Disposition: Token presence remains reproducible, but the earlier pattern-based observation did not establish whether the exact source label denotes this subject or a different preparation. Fresh source-context adjudication is required before a confirmed defect or label removal. This successor corrects certainty only; it does not establish that the token is valid or that another identity allegation is fixed.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-d3d0489bafd99d25 | data/ingredients/mapped/Riboflavin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1754],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17015","line":1756,"mapping_status":"MAPPED","ontology_id":"CHEBI:17015","preferred_term":"Riboflavin"}],"identifier":"CHEBI:17015","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2122,"edge_count":2122,"occurrences":2123},"occurrence_statistics":{"media_count":2122,"total_occurrences":2123},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17015","ontology_label":"riboflavin","ontology_source":"CHEBI"},"preferred_term":"Riboflavin","sssom_rows":[{"data_row":2431,"object_id":"CHEBI:17015","object_label":"riboflavin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Riboflavin","synonym_count":30} |
| ev-b27fdb501afeac8d | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1754] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-659fa61b579bfe7b | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Riboflavin; data-row positions=[2431] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2431,"object_id":"CHEBI:17015","object_label":"riboflavin","other":"1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol&#124;1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)pentitol&#124;5-deoxy-5-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol&#124;6,7-dimethyl-9-D-ribitylisoalloxazine&#124;7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)benzo[g]pteridine-2,4(3H,10H)-dione&#124;7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)isoalloxazine&#124;7,8-dimethyl-10-[(2S,3S,4R)-2,3,4,5-tetrahydroxypentyl]benzo[g]pteridine-2,4(3H,10H)-dione&#124;7,8-dimethyl-10-ribitylisoalloxazine&#124;Aqua-Flave&#124;Beflavin&#124;Beflavine&#124;Bisulase&#124;Dermadram&#124;E101&#124;Fiboflavin&#124;Flavaxin&#124;Flavin Bb&#124;Flaxain&#124;Hyflavin&#124;Riboflavine&#124;Riboflavine (B2)&#124;Riboflavin (Vitamine B2)&#124;Riboflavin (Vitamin B2)&#124;Riboflavin (0.2 mg/ml)&#124;Riboflavin (see below)&#124;Riboflavin (0.05 \u03bcg/mL)&#124;CAS:83-88-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Riboflavin","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-d1039d9220e809dc | docs/data/mapped_ingredients.csv; CSV lines=[1756] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:17015","line":1756,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2122","ontology_id":"CHEBI:17015","preferred_term":"Riboflavin","total_occurrences":"2123"}] |
| ev-b92552c1f537a179 | reports/yaml_record_review/Riboflavin.md; &#96;data/ingredients/mapped/Riboflavin.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-5ea4dcc66c61e646 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1174] | context_only | [{"current_record_sha256":"b79fe5e134e627e7c95d6190e54c52b04f9d81a61ad381cb136b986430d80644","finding_id":"SEM:dd7810d3410ad8889d59","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-823412d1eacb6795 | MAPPING_SEMANTICS.md; Sections on REJECTED_LABEL and the damaged-label RAW_TEXT carve-out | supports | Raw spellings may remain resolvable when they denote the same substance. Wrong-identity labels must not resolve. A recipe-pointer pattern alone does not adjudicate that distinction. |
| ev-032b61a7a21ed47b | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml; findings[finding_id=f-b7808e84d7886285] | context_only | Exact earlier occurrence has open/confirmed status, based on exported-token presence and historical report text. |
| ev-d59510b4ad4c4456 | data/ingredients/mapped/Riboflavin.yaml; identifier, ontology_mapping, synonyms and curation_history | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1754],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17015","line":1756,"mapping_status":"MAPPED","ontology_id":"CHEBI:17015","preferred_term":"Riboflavin"}],"identifier":"CHEBI:17015","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2122,"edge_count":2122,"occurrences":2123},"occurrence_statistics":{"media_count":2122,"total_occurrences":2123},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17015","ontology_label":"riboflavin","ontology_source":"CHEBI"},"preferred_term":"Riboflavin","sssom_rows":[{"data_row":2431,"object_id":"CHEBI:17015","object_label":"riboflavin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Riboflavin","synonym_count":30} |
| ev-1dfdb8319038a4fb | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Riboflavin; data-row positions=[2431] | supports | Current exact-subject rows, including complete other payload: [{"data_row":2431,"object_id":"CHEBI:17015","object_label":"riboflavin","other":"1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol&#124;1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)pentitol&#124;5-deoxy-5-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol&#124;6,7-dimethyl-9-D-ribitylisoalloxazine&#124;7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)benzo[g]pteridine-2,4(3H,10H)-dione&#124;7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)isoalloxazine&#124;7,8-dimethyl-10-[(2S,3S,4R)-2,3,4,5-tetrahydroxypentyl]benzo[g]pteridine-2,4(3H,10H)-dione&#124;7,8-dimethyl-10-ribitylisoalloxazine&#124;Aqua-Flave&#124;Beflavin&#124;Beflavine&#124;Bisulase&#124;Dermadram&#124;E101&#124;Fiboflavin&#124;Flavaxin&#124;Flavin Bb&#124;Flaxain&#124;Hyflavin&#124;Riboflavine&#124;Riboflavine (B2)&#124;Riboflavin (Vitamine B2)&#124;Riboflavin (Vitamin B2)&#124;Riboflavin (0.2 mg/ml)&#124;Riboflavin (see below)&#124;Riboflavin (0.05 \u03bcg/mL)&#124;CAS:83-88-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Riboflavin","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-a809b48a4c5a84c5 | reports/yaml_record_review/Riboflavin.md; Complete historical report, including Verdict and Recommended Edits | context_only | Historical interpretation was read in full; it is not fresh source adjudication. |
| ev-df08850b91d69e41 | reviews/structured/20261011T030852Z-mim-token-scope-reassessment/review.yaml; findings[finding_id=scope-f-b7808e84d7886285] | context_only | Predecessor structured review finding scope-f-b7808e84d7886285 in 20261011T030852Z-mim-token-scope-reassessment |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-10, 20261011T030852Z-mim-token-scope-reassessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-riboflavin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Riboflavin (data/ingredients/mapped/Riboflavin.yaml)'
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
summary: Per-record structured review for Riboflavin (data/ingredients/mapped/Riboflavin.yaml,
  record-59776f859c41300d, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Riboflavin.yaml
    sha256: b79fe5e134e627e7c95d6190e54c52b04f9d81a61ad381cb136b986430d80644
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
  - path: reports/yaml_record_review/Riboflavin.md
    sha256: 9dd8b2a901c40593a896669ad82303310aafb787ae2f8c505cbaa93fd256e8fc
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
  - path: MAPPING_SEMANTICS.md
    sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805
    role: context
targets:
- target_id: record-59776f859c41300d
  path: data/ingredients/mapped/Riboflavin.yaml
  label: Riboflavin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Riboflavin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Riboflavin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Riboflavin.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-59776f859c41300d
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-59776f859c41300d
  evidence_ids:
  - ev-d3d0489bafd99d25
  - ev-b27fdb501afeac8d
  - ev-659fa61b579bfe7b
  - ev-d1039d9220e809dc
  - ev-d59510b4ad4c4456
  - ev-1dfdb8319038a4fb
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-59776f859c41300d
  evidence_ids:
  - ev-d3d0489bafd99d25
  - ev-5ea4dcc66c61e646
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10
    and semantic review dispositions on HEAD.
  target_ids:
  - record-59776f859c41300d
  evidence_ids:
  - ev-b92552c1f537a179
  - ev-5ea4dcc66c61e646
  - ev-032b61a7a21ed47b
  - ev-a809b48a4c5a84c5
  - ev-df08850b91d69e41
evidence:
- evidence_id: ev-d3d0489bafd99d25
  kind: record_content
  reference: data/ingredients/mapped/Riboflavin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1754],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17015","line":1756,"mapping_status":"MAPPED","ontology_id":"CHEBI:17015","preferred_term":"Riboflavin"}],"identifier":"CHEBI:17015","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2122,"edge_count":2122,"occurrences":2123},"occurrence_statistics":{"media_count":2122,"total_occurrences":2123},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17015","ontology_label":"riboflavin","ontology_source":"CHEBI"},"preferred_term":"Riboflavin","sssom_rows":[{"data_row":2431,"object_id":"CHEBI:17015","object_label":"riboflavin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Riboflavin","synonym_count":30}'
  snapshot_sha256: b79fe5e134e627e7c95d6190e54c52b04f9d81a61ad381cb136b986430d80644
- evidence_id: ev-b27fdb501afeac8d
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1754]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-659fa61b579bfe7b
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Riboflavin; data-row positions=[2431]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2431,"object_id":"CHEBI:17015","object_label":"riboflavin","other":"1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol|1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)pentitol|5-deoxy-5-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol|6,7-dimethyl-9-D-ribitylisoalloxazine|7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)benzo[g]pteridine-2,4(3H,10H)-dione|7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)isoalloxazine|7,8-dimethyl-10-[(2S,3S,4R)-2,3,4,5-tetrahydroxypentyl]benzo[g]pteridine-2,4(3H,10H)-dione|7,8-dimethyl-10-ribitylisoalloxazine|Aqua-Flave|Beflavin|Beflavine|Bisulase|Dermadram|E101|Fiboflavin|Flavaxin|Flavin
    Bb|Flaxain|Hyflavin|Riboflavine|Riboflavine (B2)|Riboflavin (Vitamine B2)|Riboflavin
    (Vitamin B2)|Riboflavin (0.2 mg/ml)|Riboflavin (see below)|Riboflavin (0.05 \u03bcg/mL)|CAS:83-88-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Riboflavin","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-d1039d9220e809dc
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1756]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:17015","line":1756,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2122","ontology_id":"CHEBI:17015","preferred_term":"Riboflavin","total_occurrences":"2123"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-b92552c1f537a179
  kind: prior_review
  reference: reports/yaml_record_review/Riboflavin.md
  locator: '`data/ingredients/mapped/Riboflavin.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 9dd8b2a901c40593a896669ad82303310aafb787ae2f8c505cbaa93fd256e8fc
- evidence_id: ev-5ea4dcc66c61e646
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1174]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"b79fe5e134e627e7c95d6190e54c52b04f9d81a61ad381cb136b986430d80644","finding_id":"SEM:dd7810d3410ad8889d59","kind":"existing_record_review","resolution_reason":"Historical
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
- evidence_id: ev-032b61a7a21ed47b
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
  locator: findings[finding_id=f-b7808e84d7886285]
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Exact earlier occurrence has open/confirmed status, based on exported-token
    presence and historical report text.
  snapshot_sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
  quote: '{"category": "nomenclature", "certainty": "confirmed", "description": "Historical
    tokens are still present on the exact-subject SSSOM rows: [{\"reason\":\"unresolved
    recipe cross-reference in a resolving synonym\",\"token\":\"Riboflavin (see below)\"}].
    Truncated concentration strings and context-dependent instructions need scoped
    curation. This check does not reject catalog/RAW_TEXT synonyms as a class.", "evidence_ids":
    ["ev-b92552c1f537a179", "ev-659fa61b579bfe7b"], "external_issues": ["https://github.com/CultureBotAI/MediaIngredientMech/issues/718"],
    "field_paths": ["synonyms", "SSSOM.other"], "finding_id": "f-b7808e84d7886285",
    "issue_key": "mim-reconciliation-exported-context-tokens-59776f859c41300d", "owner_paths":
    [{"path": "data/ingredients/mapped/Riboflavin.yaml", "repository": "CultureBotAI/MediaIngredientMech",
    "role": "maintained ingredient"}], "severity": "major", "status": "open", "tags":
    ["reconciliation", "bundle-by-owner", "exported-context-tokens"], "target_ids":
    ["record-59776f859c41300d"], "title": "Review nonportable exported tokens: Riboflavin"}'
- evidence_id: ev-d59510b4ad4c4456
  kind: record_content
  reference: data/ingredients/mapped/Riboflavin.yaml
  locator: identifier, ontology_mapping, synonyms and curation_history
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1754],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17015","line":1756,"mapping_status":"MAPPED","ontology_id":"CHEBI:17015","preferred_term":"Riboflavin"}],"identifier":"CHEBI:17015","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2122,"edge_count":2122,"occurrences":2123},"occurrence_statistics":{"media_count":2122,"total_occurrences":2123},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17015","ontology_label":"riboflavin","ontology_source":"CHEBI"},"preferred_term":"Riboflavin","sssom_rows":[{"data_row":2431,"object_id":"CHEBI:17015","object_label":"riboflavin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Riboflavin","synonym_count":30}'
  snapshot_sha256: b79fe5e134e627e7c95d6190e54c52b04f9d81a61ad381cb136b986430d80644
- evidence_id: ev-1dfdb8319038a4fb
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Riboflavin; data-row positions=[2431]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2431,"object_id":"CHEBI:17015","object_label":"riboflavin","other":"1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol|1-deoxy-1-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)pentitol|5-deoxy-5-(7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[g]pteridin-10(2H)-yl)-D-ribitol|6,7-dimethyl-9-D-ribitylisoalloxazine|7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)benzo[g]pteridine-2,4(3H,10H)-dione|7,8-dimethyl-10-(D-ribo-2,3,4,5-tetrahydroxypentyl)isoalloxazine|7,8-dimethyl-10-[(2S,3S,4R)-2,3,4,5-tetrahydroxypentyl]benzo[g]pteridine-2,4(3H,10H)-dione|7,8-dimethyl-10-ribitylisoalloxazine|Aqua-Flave|Beflavin|Beflavine|Bisulase|Dermadram|E101|Fiboflavin|Flavaxin|Flavin
    Bb|Flaxain|Hyflavin|Riboflavine|Riboflavine (B2)|Riboflavin (Vitamine B2)|Riboflavin
    (Vitamin B2)|Riboflavin (0.2 mg/ml)|Riboflavin (see below)|Riboflavin (0.05 \u03bcg/mL)|CAS:83-88-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Riboflavin","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-a809b48a4c5a84c5
  kind: prior_review
  reference: reports/yaml_record_review/Riboflavin.md
  locator: Complete historical report, including Verdict and Recommended Edits
  accessed_at: '2026-10-11T03:08:52Z'
  support: context_only
  summary: Historical interpretation was read in full; it is not fresh source adjudication.
  snapshot_sha256: 9dd8b2a901c40593a896669ad82303310aafb787ae2f8c505cbaa93fd256e8fc
  quote: '# `data/ingredients/mapped/Riboflavin.yaml`


    **Verdict**: needs curation, major issue.


    **Identity**: `Riboflavin` maps exactly to active, defining `CHEBI:17015` /

    `riboflavin`. Fresh OLS4 lookup resolved the ChEBI term with CAS `83-88-5`,

    formula `C17H20N4O6`, and the same InChI as the YAML; fresh PubChem lookup by

    the stored CAS resolved CID 493570 with the same formula and InChI.


    **Validation**: `uv run --frozen python scripts/validate_strict.py

    data/ingredients/mapped/Rhodomycin_A.yaml

    data/ingredients/mapped/Rhodomycin_B.yaml data/ingredients/mapped/Ribitol.yaml

    data/ingredients/mapped/Riboflavin.yaml

    data/ingredients/mapped/Ribonucleic_Acid_From_Torula_Yeast_Type_VI.yaml` passed

    for the 5-file batch with 0 ERROR rows. Direct

    `linkml-term-validator validate-data` with `--labels` passed for the same 5

    files.


    **Evidence**: The exact ChEBI identity, CAS, chemical properties, refreshed

    2123-occurrence count, and CultureMech `VITAMIN_SOURCE` role pass. The

    per-record YAML also agrees with the regenerated aggregate row when keyed by

    `(identifier, preferred_term)`.


    Final SSSOM row 2507 still exports raw recipe labels in `other`: `Riboflavin

    (0.2 mg/ml)`, `Riboflavin (see below)`, and the raw 0.05 microgram/mL

    CultureMech label. These are concentration- or recipe-pointer strings, not

    true alternate names for `CHEBI:17015`.


    The auto-proposed PMID 40609532 mapping evidence is also out of scope. PubMed

    resolves the article to a 2025 Cell Metabolism study of microbial riboflavin,

    ceramide synthase 3, and colorectal cancer; it mentions riboflavin, but it does

    not support this CultureMech ingredient-to-ChEBI identity claim.


    **Completeness**: The exact chemical identity is complete enough, and the

    vitamin role has CultureMech database evidence. The unsafe data is confined to

    three raw occurrence synonyms plus the irrelevant PubMed mapping-evidence row.


    **Recommended Edits**: Remove the concentration-qualified and `see below`

    CultureMech labels from active exported synonyms and drop or replace the

    auto-proposed PubMed evidence under `ontology_mapping.evidence`. Regenerate

    final SSSOM and confirm row 2507 no longer exports non-synonym recipe text in

    `other`.

    '
- evidence_id: ev-df08850b91d69e41
  kind: prior_review
  reference: reviews/structured/20261011T030852Z-mim-token-scope-reassessment/review.yaml
  locator: findings[finding_id=scope-f-b7808e84d7886285]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding scope-f-b7808e84d7886285 in 20261011T030852Z-mim-token-scope-reassessment
  snapshot_sha256: 42a76b000bcbd07b426f6bad61b124b11ec08d8977783a67b732b01754f7c609
assessments:
- assessment_id: a-ec3393c99d2f2581
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-59776f859c41300d
  evidence_ids:
  - ev-d3d0489bafd99d25
  - ev-b27fdb501afeac8d
  - ev-659fa61b579bfe7b
  - ev-d1039d9220e809dc
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-d8fb521a6f503f97
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-59776f859c41300d
  evidence_ids:
  - ev-b92552c1f537a179
  - ev-d3d0489bafd99d25
  - ev-5ea4dcc66c61e646
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T12:11:07Z;
    reviewed SHA-256=b79fe5e134e627e7c95d6190e54c52b04f9d81a61ad381cb136b986430d80644;
    current SHA-256=b79fe5e134e627e7c95d6190e54c52b04f9d81a61ad381cb136b986430d80644;
    hash_changed=False. Reports=["reports/yaml_record_review/Riboflavin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI:17015
    identity passes, but final SSSOM exports raw concentration and recipe-pointer
    labels.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b92552c1f537a179
    - ev-d3d0489bafd99d25
  - name: legacy-native-ids
    value: '["SEM:dd7810d3410ad8889d59"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-d3d0489bafd99d25
    - ev-b92552c1f537a179
    - ev-5ea4dcc66c61e646
- assessment_id: a-6b8f17df534ab0ae
  area: nomenclature
  topic: Unresolved recipe-reference or truncated-concentration synonyms
  outcome: concern
  summary: 'Historical tokens are still present on the exact-subject SSSOM rows: [{"reason":"unresolved
    recipe cross-reference in a resolving synonym","token":"Riboflavin (see below)"}].
    Truncated concentration strings and context-dependent instructions need scoped
    curation. This check does not reject catalog/RAW_TEXT synonyms as a class.'
  target_ids:
  - record-59776f859c41300d
  evidence_ids:
  - ev-b92552c1f537a179
  - ev-659fa61b579bfe7b
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b92552c1f537a179
    - ev-659fa61b579bfe7b
- assessment_id: scope-f-b7808e84d7886285
  area: nomenclature
  topic: Certainty correction for the exact token observation
  outcome: unknown
  summary: Token presence remains reproducible, but the earlier pattern-based observation
    did not establish whether the exact source label denotes this subject or a different
    preparation. Fresh source-context adjudication is required before a confirmed
    defect or label removal. This successor corrects certainty only; it does not establish
    that the token is valid or that another identity allegation is fixed.
  target_ids:
  - record-59776f859c41300d
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-032b61a7a21ed47b
  - ev-d59510b4ad4c4456
  - ev-1dfdb8319038a4fb
  - ev-a809b48a4c5a84c5
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Source-scope question only, not a disposition of the complete historical
      report.
    evidence_ids:
    - ev-823412d1eacb6795
    - ev-032b61a7a21ed47b
    - ev-d59510b4ad4c4456
    - ev-1dfdb8319038a4fb
    - ev-a809b48a4c5a84c5
findings:
- finding_id: rec-scope-f-b7808e84d7886285
  issue_key: mim-reconciliation-exported-context-tokens-59776f859c41300d
  category: nomenclature
  severity: major
  status: deferred
  certainty: provisional
  title: 'Adjudicate source scope of exported tokens: Riboflavin'
  description: Token presence remains reproducible, but the earlier pattern-based
    observation did not establish whether the exact source label denotes this subject
    or a different preparation. Fresh source-context adjudication is required before
    a confirmed defect or label removal. This successor corrects certainty only; it
    does not establish that the token is valid or that another identity allegation
    is fixed.
  target_ids:
  - record-59776f859c41300d
  evidence_ids:
  - ev-823412d1eacb6795
  - ev-032b61a7a21ed47b
  - ev-d59510b4ad4c4456
  - ev-1dfdb8319038a4fb
  - ev-a809b48a4c5a84c5
  - ev-df08850b91d69e41
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Riboflavin.yaml
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
    finding_id: scope-f-b7808e84d7886285
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-10, 20261011T030852Z-mim-token-scope-reassessment.
```
