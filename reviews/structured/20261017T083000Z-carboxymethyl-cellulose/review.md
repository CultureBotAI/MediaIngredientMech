# Per-record structured review: Carboxymethyl_Cellulose (data/ingredients/mapped/Carboxymethyl_Cellulose.yaml)

- Review: 20261017T083000Z-carboxymethyl-cellulose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Carboxymethyl_Cellulose (data/ingredients/mapped/Carboxymethyl_Cellulose.yaml, record-62750a20d269331c, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Carboxymethyl_Cellulose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Carboxymethyl_Cellulose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-62750a20d269331c | data/ingredients/mapped/Carboxymethyl_Cellulose.yaml | maintained | Carboxymethyl_Cellulose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-62750a20d269331c | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-62750a20d269331c | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-62750a20d269331c | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-62750a20d269331c.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-62750a20d269331c.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T10:57:17Z; reviewed SHA-256=39c13e1211c19e8973469abed34afb21c2b4b42fdb90abaabebb2f6c1a77a0d8; current SHA-256=39c13e1211c19e8973469abed34afb21c2b4b42fdb90abaabebb2f6c1a77a0d8; hash_changed=False. Reports=["reports/yaml_record_review/Carboxymethyl_Cellulose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CHEBI sodium-salt identity passes, but CARBON_SOURCE is only a provisional name-pattern prediction.

### Historical provisional-role concern

evidence: concern. Targets: record-62750a20d269331c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-eb71ecd9acf27634: Reassess prediction-only role support: Carboxymethyl cellulose

major / open / confirmed; issue key: mim-reconciliation-role-support-62750a20d269331c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-eb71ecd9acf27634

Reassess prediction-only role support: Carboxymethyl cellulose

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-74321e80bdbdd9bb | data/ingredients/mapped/Carboxymethyl_Cellulose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[654],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:234035","line":656,"mapping_status":"MAPPED","ontology_id":"CHEBI:234035","preferred_term":"Carboxymethyl cellulose"}],"identifier":"CHEBI:234035","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7,"edge_count":7,"occurrences":7},"occurrence_statistics":{"media_count":7,"total_occurrences":7},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:234035","ontology_label":"carboxymethylcellulose sodium salt","ontology_source":"CHEBI"},"preferred_term":"Carboxymethyl cellulose","sssom_rows":[{"data_row":641,"object_id":"CHEBI:234035","object_label":"carboxymethylcellulose sodium salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Carboxymethyl_Cellulose","synonym_count":18} |
| ev-033e3aa9de0738b9 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [654] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-48055f1043f986ee | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Carboxymethyl_Cellulose; data-row positions=[641] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":641,"object_id":"CHEBI:234035","object_label":"carboxymethylcellulose sodium salt","other":"CMC&#124;Carboximethylcellulosum&#124;Carboxymethylcellulose&#124;Carboxymethylcellulosum&#124;Celluloseglycolic acid&#124;Glycolic acid cellulose ether&#124;carmellosum&#124;carmelosa&#124;croscarmellose&#124;croscarmellosum&#124;croscarmelosa&#124;Carboxymethyl cellulose (sodium salt)&#124;Carboxymethylcellulose sodium&#124;CMC-Na&#124;Carboxymethyl cellulose, sodium salt&#124;Carmellose&#124;CAS:9004-32-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Carboxymethyl_Cellulose","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-027220966ba0012a | docs/data/mapped_ingredients.csv; CSV lines=[656] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:234035","line":656,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"7","ontology_id":"CHEBI:234035","preferred_term":"Carboxymethyl cellulose","total_occurrences":"7"}] |
| ev-6498a75b33cc8c36 | reports/yaml_record_review/Carboxymethyl_Cellulose.md; &#96;data/ingredients/mapped/Carboxymethyl_Cellulose.yaml&#96;:2; Verdict:4; Identity:12; Validation:28; Evidence:46; Completeness:62; Recommended Edits:69 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-431a3a4a31410726 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[359,1426] | context_only | [{"current_record_sha256":"39c13e1211c19e8973469abed34afb21c2b4b42fdb90abaabebb2f6c1a77a0d8","finding_id":"SEM:642dac3b664336a8fa06","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"39c13e1211c19e8973469abed34afb21c2b4b42fdb90abaabebb2f6c1a77a0d8","finding_id":"SEM:cb43fdbdd2dd2e0fd9a0","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-df4f5069ed4cd16d | data/ingredients/mapped/Carboxymethyl_Cellulose.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[654],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:234035","line":656,"mapping_status":"MAPPED","ontology_id":"CHEBI:234035","preferred_term":"Carboxymethyl cellulose"}],"identifier":"CHEBI:234035","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7,"edge_count":7,"occurrences":7},"occurrence_statistics":{"media_count":7,"total_occurrences":7},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:234035","ontology_label":"carboxymethylcellulose sodium salt","ontology_source":"CHEBI"},"preferred_term":"Carboxymethyl cellulose","sssom_rows":[{"data_row":641,"object_id":"CHEBI:234035","object_label":"carboxymethylcellulose sodium salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Carboxymethyl_Cellulose","synonym_count":18} |
| ev-6125b667f81dc91b | reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml; findings[finding_id=f-eb71ecd9acf27634] | context_only | Predecessor structured review finding f-eb71ecd9acf27634 in 20261011T024632Z-mim-reconcile-all-batch-04 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-carboxymethyl-cellulose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Carboxymethyl_Cellulose (data/ingredients/mapped/Carboxymethyl_Cellulose.yaml)'
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
native_verdict: mapping_status=MAPPED; open=1; deferred=0
scientific_review: false
summary: Per-record structured review for Carboxymethyl_Cellulose (data/ingredients/mapped/Carboxymethyl_Cellulose.yaml,
  record-62750a20d269331c, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Carboxymethyl_Cellulose.yaml
    sha256: 39c13e1211c19e8973469abed34afb21c2b4b42fdb90abaabebb2f6c1a77a0d8
    role: target
  - path: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
    sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
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
  - path: reports/yaml_record_review/Carboxymethyl_Cellulose.md
    sha256: 343dcc2ff10306ca7f2c3221944d8a5acded8d81d6bbc469fcf74334ea894581
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-62750a20d269331c
  path: data/ingredients/mapped/Carboxymethyl_Cellulose.yaml
  label: Carboxymethyl_Cellulose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Carboxymethyl_Cellulose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Carboxymethyl_Cellulose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Carboxymethyl_Cellulose.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-62750a20d269331c
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-62750a20d269331c
  evidence_ids:
  - ev-74321e80bdbdd9bb
  - ev-033e3aa9de0738b9
  - ev-48055f1043f986ee
  - ev-027220966ba0012a
  - ev-df4f5069ed4cd16d
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-62750a20d269331c
  evidence_ids:
  - ev-74321e80bdbdd9bb
  - ev-431a3a4a31410726
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-62750a20d269331c
  evidence_ids:
  - ev-6498a75b33cc8c36
  - ev-431a3a4a31410726
  - ev-6125b667f81dc91b
evidence:
- evidence_id: ev-74321e80bdbdd9bb
  kind: record_content
  reference: data/ingredients/mapped/Carboxymethyl_Cellulose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[654],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:234035","line":656,"mapping_status":"MAPPED","ontology_id":"CHEBI:234035","preferred_term":"Carboxymethyl
    cellulose"}],"identifier":"CHEBI:234035","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7,"edge_count":7,"occurrences":7},"occurrence_statistics":{"media_count":7,"total_occurrences":7},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:234035","ontology_label":"carboxymethylcellulose
    sodium salt","ontology_source":"CHEBI"},"preferred_term":"Carboxymethyl cellulose","sssom_rows":[{"data_row":641,"object_id":"CHEBI:234035","object_label":"carboxymethylcellulose
    sodium salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Carboxymethyl_Cellulose","synonym_count":18}'
  snapshot_sha256: 39c13e1211c19e8973469abed34afb21c2b4b42fdb90abaabebb2f6c1a77a0d8
- evidence_id: ev-033e3aa9de0738b9
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [654]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-48055f1043f986ee
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Carboxymethyl_Cellulose; data-row positions=[641]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":641,"object_id":"CHEBI:234035","object_label":"carboxymethylcellulose
    sodium salt","other":"CMC|Carboximethylcellulosum|Carboxymethylcellulose|Carboxymethylcellulosum|Celluloseglycolic
    acid|Glycolic acid cellulose ether|carmellosum|carmelosa|croscarmellose|croscarmellosum|croscarmelosa|Carboxymethyl
    cellulose (sodium salt)|Carboxymethylcellulose sodium|CMC-Na|Carboxymethyl cellulose,
    sodium salt|Carmellose|CAS:9004-32-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Carboxymethyl_Cellulose","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-027220966ba0012a
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[656]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:234035","line":656,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"7","ontology_id":"CHEBI:234035","preferred_term":"Carboxymethyl
    cellulose","total_occurrences":"7"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-6498a75b33cc8c36
  kind: prior_review
  reference: reports/yaml_record_review/Carboxymethyl_Cellulose.md
  locator: '`data/ingredients/mapped/Carboxymethyl_Cellulose.yaml`:2; Verdict:4; Identity:12;
    Validation:28; Evidence:46; Completeness:62; Recommended Edits:69'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 343dcc2ff10306ca7f2c3221944d8a5acded8d81d6bbc469fcf74334ea894581
  quote: "Recommended Edits:\n- Major: either replace the provisional `nutritional_roles.CARBON_SOURCE`\n\
    \  evidence in `data/ingredients/mapped/Carboxymethyl_Cellulose.yaml` with\n \
    \ inspected evidence for this sodium-salt record and source scope, or remove\n\
    \  the role, then rerun strict validation, SSSOM QC, aggregate roundtrip, and\n\
    \  `git diff --check`."
- evidence_id: ev-431a3a4a31410726
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[359,1426]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"39c13e1211c19e8973469abed34afb21c2b4b42fdb90abaabebb2f6c1a77a0d8","finding_id":"SEM:642dac3b664336a8fa06","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"39c13e1211c19e8973469abed34afb21c2b4b42fdb90abaabebb2f6c1a77a0d8","finding_id":"SEM:cb43fdbdd2dd2e0fd9a0","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-df4f5069ed4cd16d
  kind: record_content
  reference: data/ingredients/mapped/Carboxymethyl_Cellulose.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[654],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:234035","line":656,"mapping_status":"MAPPED","ontology_id":"CHEBI:234035","preferred_term":"Carboxymethyl
    cellulose"}],"identifier":"CHEBI:234035","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7,"edge_count":7,"occurrences":7},"occurrence_statistics":{"media_count":7,"total_occurrences":7},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:234035","ontology_label":"carboxymethylcellulose
    sodium salt","ontology_source":"CHEBI"},"preferred_term":"Carboxymethyl cellulose","sssom_rows":[{"data_row":641,"object_id":"CHEBI:234035","object_label":"carboxymethylcellulose
    sodium salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Carboxymethyl_Cellulose","synonym_count":18}'
  snapshot_sha256: 39c13e1211c19e8973469abed34afb21c2b4b42fdb90abaabebb2f6c1a77a0d8
- evidence_id: ev-6125b667f81dc91b
  kind: prior_review
  reference: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
  locator: findings[finding_id=f-eb71ecd9acf27634]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-eb71ecd9acf27634 in 20261011T024632Z-mim-reconcile-all-batch-04
  snapshot_sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
assessments:
- assessment_id: a-4a0ef571200554ab
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-62750a20d269331c
  evidence_ids:
  - ev-74321e80bdbdd9bb
  - ev-033e3aa9de0738b9
  - ev-48055f1043f986ee
  - ev-027220966ba0012a
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-422095e2b1d083f8
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-62750a20d269331c
  evidence_ids:
  - ev-6498a75b33cc8c36
  - ev-74321e80bdbdd9bb
  - ev-431a3a4a31410726
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T10:57:17Z;
    reviewed SHA-256=39c13e1211c19e8973469abed34afb21c2b4b42fdb90abaabebb2f6c1a77a0d8;
    current SHA-256=39c13e1211c19e8973469abed34afb21c2b4b42fdb90abaabebb2f6c1a77a0d8;
    hash_changed=False. Reports=["reports/yaml_record_review/Carboxymethyl_Cellulose.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CHEBI
    sodium-salt identity passes, but CARBON_SOURCE is only a provisional name-pattern
    prediction.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-6498a75b33cc8c36
    - ev-74321e80bdbdd9bb
  - name: legacy-native-ids
    value: '["SEM:642dac3b664336a8fa06","SEM:cb43fdbdd2dd2e0fd9a0"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-74321e80bdbdd9bb
    - ev-6498a75b33cc8c36
    - ev-431a3a4a31410726
- assessment_id: a-df4f5069ed4cd16d
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-62750a20d269331c
  evidence_ids:
  - ev-6498a75b33cc8c36
  - ev-df4f5069ed4cd16d
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-6498a75b33cc8c36
    - ev-df4f5069ed4cd16d
findings:
- finding_id: rec-f-eb71ecd9acf27634
  issue_key: mim-reconciliation-role-support-62750a20d269331c
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Carboxymethyl cellulose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-62750a20d269331c
  evidence_ids:
  - ev-6498a75b33cc8c36
  - ev-df4f5069ed4cd16d
  - ev-6125b667f81dc91b
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Carboxymethyl_Cellulose.yaml
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
    review_id: 20261011T024632Z-mim-reconcile-all-batch-04
    finding_id: f-eb71ecd9acf27634
actions:
- action_id: rec-action-eb71ecd9acf27634
  description: 'Reassess prediction-only role support: Carboxymethyl cellulose'
  finding_ids:
  - rec-f-eb71ecd9acf27634
  target_ids:
  - record-62750a20d269331c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Carboxymethyl_Cellulose.yaml
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
  with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.
```
