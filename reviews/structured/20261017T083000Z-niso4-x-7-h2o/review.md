# Per-record structured review: Niso4_X_7_H2o (data/ingredients/mapped/Niso4_X_7_H2o.yaml)

- Review: 20261017T083000Z-niso4-x-7-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Niso4_X_7_H2o (data/ingredients/mapped/Niso4_X_7_H2o.yaml, record-19b63a6ad1ce6109, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Niso4_X_7_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Niso4_X_7_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-19b63a6ad1ce6109 | data/ingredients/mapped/Niso4_X_7_H2o.yaml | maintained | Niso4_X_7_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-19b63a6ad1ce6109 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-19b63a6ad1ce6109 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-19b63a6ad1ce6109 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-19b63a6ad1ce6109.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-19b63a6ad1ce6109.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:03:04Z; reviewed SHA-256=18aac3d02606aacb2241a62f07e243436a4aa616685b826333d87f04caee75ff; current SHA-256=18aac3d02606aacb2241a62f07e243436a4aa616685b826333d87f04caee75ff; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050304Z-Niso4_X_7_H2o.md","reports/yaml_record_review/Niso4_X_7_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Niso4_X_7_H2o.md&#96; after the record changed from b7887a8dc671584afe8ae7652ec8266f78ddd646fa4b41d9c20dfa210c228cf3 to 18aac3d02606aacb2241a62f07e243436a4aa616685b826333d87f04caee75ff; preserved the previous major finding floor pending targeted retirement.

### Historical provisional-role concern

evidence: concern. Targets: record-19b63a6ad1ce6109.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-413db41429a7056c: Reassess prediction-only role support: NiSO4 x 7 H2O

major / open / confirmed; issue key: mim-reconciliation-role-support-19b63a6ad1ce6109.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-413db41429a7056c

Reassess prediction-only role support: NiSO4 x 7 H2O

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-d4e3432235f8e6d1 | data/ingredients/mapped/Niso4_X_7_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1565],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:53504","line":1567,"mapping_status":"MAPPED","ontology_id":"CHEBI:53504","preferred_term":"NiSO4 x 7 H2O"}],"identifier":"CHEBI:53504","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":9,"edge_count":9,"occurrences":9},"occurrence_statistics":{"media_count":9,"total_occurrences":9},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:53504","ontology_label":"nickel sulfate heptahydrate","ontology_source":"CHEBI"},"preferred_term":"NiSO4 x 7 H2O","sssom_rows":[{"data_row":2096,"object_id":"CHEBI:53504","object_label":"nickel sulfate heptahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Niso4_X_7_H2o","synonym_count":6} |
| ev-06ec8c7927b7b5ea | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1565] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-409b8ccd783e0269 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Niso4_X_7_H2o; data-row positions=[2096] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2096,"object_id":"CHEBI:53504","object_label":"nickel sulfate heptahydrate","other":"NiSO4\u30fb7H2O","predicate_id":"skos:exactMatch","subject_id":"MIM:Niso4_X_7_H2o","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-54a928f471cc1947 | docs/data/mapped_ingredients.csv; CSV lines=[1567] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:53504","line":1567,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"9","ontology_id":"CHEBI:53504","preferred_term":"NiSO4 x 7 H2O","total_occurrences":"9"}] |
| ev-fc0c467df9da6bd7 | reports/yaml_record_review/20261001T050304Z-Niso4_X_7_H2o.md; YAML Record Review: NiSO4 x 7 H2O:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-dd3d507c5231015c | reports/yaml_record_review/Niso4_X_7_H2o.md; &#96;data/ingredients/mapped/Niso4_X_7_H2o.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:29; Completeness:44; Recommended Edits:51 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-5a68d43680dc9e8e | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1063,1565] | context_only | [{"current_record_sha256":"18aac3d02606aacb2241a62f07e243436a4aa616685b826333d87f04caee75ff","finding_id":"SEM:1971ff4d47b066a4339f","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"18aac3d02606aacb2241a62f07e243436a4aa616685b826333d87f04caee75ff","finding_id":"SEM:db276e2e3eae5d2442dc","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-2564d771adfd1b6b | data/ingredients/mapped/Niso4_X_7_H2o.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1565],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:53504","line":1567,"mapping_status":"MAPPED","ontology_id":"CHEBI:53504","preferred_term":"NiSO4 x 7 H2O"}],"identifier":"CHEBI:53504","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":9,"edge_count":9,"occurrences":9},"occurrence_statistics":{"media_count":9,"total_occurrences":9},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:53504","ontology_label":"nickel sulfate heptahydrate","ontology_source":"CHEBI"},"preferred_term":"NiSO4 x 7 H2O","sssom_rows":[{"data_row":2096,"object_id":"CHEBI:53504","object_label":"nickel sulfate heptahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Niso4_X_7_H2o","synonym_count":6} |
| ev-f6454d069cd8a1be | reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml; findings[finding_id=f-413db41429a7056c] | context_only | Predecessor structured review finding f-413db41429a7056c in 20261011T024637Z-mim-reconcile-all-batch-09 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-niso4-x-7-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Niso4_X_7_H2o (data/ingredients/mapped/Niso4_X_7_H2o.yaml)'
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
summary: Per-record structured review for Niso4_X_7_H2o (data/ingredients/mapped/Niso4_X_7_H2o.yaml,
  record-19b63a6ad1ce6109, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Niso4_X_7_H2o.yaml
    sha256: 18aac3d02606aacb2241a62f07e243436a4aa616685b826333d87f04caee75ff
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
  - path: reports/yaml_record_review/20261001T050304Z-Niso4_X_7_H2o.md
    sha256: c1f7a54b37d3fdc22a31b5a6e6db18ea441a91e1565ef7eab1cfef4759a1ea32
    role: context
  - path: reports/yaml_record_review/Niso4_X_7_H2o.md
    sha256: 093ad65a36679f928feaa95034c92a5ccd1f5b07db8e81e05ac5e3b66f430855
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-19b63a6ad1ce6109
  path: data/ingredients/mapped/Niso4_X_7_H2o.yaml
  label: Niso4_X_7_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Niso4_X_7_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Niso4_X_7_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Niso4_X_7_H2o.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-19b63a6ad1ce6109
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-19b63a6ad1ce6109
  evidence_ids:
  - ev-d4e3432235f8e6d1
  - ev-06ec8c7927b7b5ea
  - ev-409b8ccd783e0269
  - ev-54a928f471cc1947
  - ev-2564d771adfd1b6b
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-19b63a6ad1ce6109
  evidence_ids:
  - ev-d4e3432235f8e6d1
  - ev-5a68d43680dc9e8e
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-19b63a6ad1ce6109
  evidence_ids:
  - ev-fc0c467df9da6bd7
  - ev-dd3d507c5231015c
  - ev-5a68d43680dc9e8e
  - ev-f6454d069cd8a1be
evidence:
- evidence_id: ev-d4e3432235f8e6d1
  kind: record_content
  reference: data/ingredients/mapped/Niso4_X_7_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1565],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:53504","line":1567,"mapping_status":"MAPPED","ontology_id":"CHEBI:53504","preferred_term":"NiSO4
    x 7 H2O"}],"identifier":"CHEBI:53504","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":9,"edge_count":9,"occurrences":9},"occurrence_statistics":{"media_count":9,"total_occurrences":9},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:53504","ontology_label":"nickel
    sulfate heptahydrate","ontology_source":"CHEBI"},"preferred_term":"NiSO4 x 7 H2O","sssom_rows":[{"data_row":2096,"object_id":"CHEBI:53504","object_label":"nickel
    sulfate heptahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Niso4_X_7_H2o","synonym_count":6}'
  snapshot_sha256: 18aac3d02606aacb2241a62f07e243436a4aa616685b826333d87f04caee75ff
- evidence_id: ev-06ec8c7927b7b5ea
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1565]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-409b8ccd783e0269
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Niso4_X_7_H2o; data-row positions=[2096]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2096,"object_id":"CHEBI:53504","object_label":"nickel
    sulfate heptahydrate","other":"NiSO4\u30fb7H2O","predicate_id":"skos:exactMatch","subject_id":"MIM:Niso4_X_7_H2o","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-54a928f471cc1947
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1567]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:53504","line":1567,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"9","ontology_id":"CHEBI:53504","preferred_term":"NiSO4
    x 7 H2O","total_occurrences":"9"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-fc0c467df9da6bd7
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050304Z-Niso4_X_7_H2o.md
  locator: 'YAML Record Review: NiSO4 x 7 H2O:2; Target:10; Validation:20; Identity
    and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: c1f7a54b37d3fdc22a31b5a6e6db18ea441a91e1565ef7eab1cfef4759a1ea32
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/Niso4_X_7_H2o.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The exact
    CHEBI:53504 heptahydrate identity passes, but stale anhydrous structure, parent
    synonyms, and a provisional TRACE_ELEMENT role remain.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Niso4_X_7_H2o.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Niso4_X_7_H2o.yaml`,
    `just validate-terms data/ingredients/mapped/Niso4_X_7_H2o.yaml` where applicable,
    and `just qc-sssom`.'
- evidence_id: ev-dd3d507c5231015c
  kind: prior_review
  reference: reports/yaml_record_review/Niso4_X_7_H2o.md
  locator: '`data/ingredients/mapped/Niso4_X_7_H2o.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:29; Completeness:44; Recommended Edits:51'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 093ad65a36679f928feaa95034c92a5ccd1f5b07db8e81e05ac5e3b66f430855
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Niso4_X_7_H2o.yaml`,\
    \ either replace the\n  stale anhydrous InChI/SMILES with ChEBI heptahydrate structure\
    \ values or\n  clear them until that evidence is synchronized.\n- Major: reject\
    \ or demote `nickel(2+) sulfate`, then rebuild final SSSOM so the\n  heptahydrate\
    \ row does not publish an anhydrous parent synonym.\n- Major: replace the provisional\
    \ `TRACE_ELEMENT` role with inspected\n  claim-level evidence or remove it."
- evidence_id: ev-5a68d43680dc9e8e
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1063,1565]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"18aac3d02606aacb2241a62f07e243436a4aa616685b826333d87f04caee75ff","finding_id":"SEM:1971ff4d47b066a4339f","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"18aac3d02606aacb2241a62f07e243436a4aa616685b826333d87f04caee75ff","finding_id":"SEM:db276e2e3eae5d2442dc","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-2564d771adfd1b6b
  kind: record_content
  reference: data/ingredients/mapped/Niso4_X_7_H2o.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1565],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:53504","line":1567,"mapping_status":"MAPPED","ontology_id":"CHEBI:53504","preferred_term":"NiSO4
    x 7 H2O"}],"identifier":"CHEBI:53504","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":9,"edge_count":9,"occurrences":9},"occurrence_statistics":{"media_count":9,"total_occurrences":9},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:53504","ontology_label":"nickel
    sulfate heptahydrate","ontology_source":"CHEBI"},"preferred_term":"NiSO4 x 7 H2O","sssom_rows":[{"data_row":2096,"object_id":"CHEBI:53504","object_label":"nickel
    sulfate heptahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Niso4_X_7_H2o","synonym_count":6}'
  snapshot_sha256: 18aac3d02606aacb2241a62f07e243436a4aa616685b826333d87f04caee75ff
- evidence_id: ev-f6454d069cd8a1be
  kind: prior_review
  reference: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
  locator: findings[finding_id=f-413db41429a7056c]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-413db41429a7056c in 20261011T024637Z-mim-reconcile-all-batch-09
  snapshot_sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
assessments:
- assessment_id: a-70b741afa6f9492a
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-19b63a6ad1ce6109
  evidence_ids:
  - ev-d4e3432235f8e6d1
  - ev-06ec8c7927b7b5ea
  - ev-409b8ccd783e0269
  - ev-54a928f471cc1947
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-d8eed7ab877750d7
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-19b63a6ad1ce6109
  evidence_ids:
  - ev-fc0c467df9da6bd7
  - ev-dd3d507c5231015c
  - ev-d4e3432235f8e6d1
  - ev-5a68d43680dc9e8e
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:03:04Z;
    reviewed SHA-256=18aac3d02606aacb2241a62f07e243436a4aa616685b826333d87f04caee75ff;
    current SHA-256=18aac3d02606aacb2241a62f07e243436a4aa616685b826333d87f04caee75ff;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050304Z-Niso4_X_7_H2o.md","reports/yaml_record_review/Niso4_X_7_H2o.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Niso4_X_7_H2o.md` after the record changed from b7887a8dc671584afe8ae7652ec8266f78ddd646fa4b41d9c20dfa210c228cf3
    to 18aac3d02606aacb2241a62f07e243436a4aa616685b826333d87f04caee75ff; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-fc0c467df9da6bd7
    - ev-dd3d507c5231015c
    - ev-d4e3432235f8e6d1
  - name: legacy-native-ids
    value: '["SEM:1971ff4d47b066a4339f","SEM:db276e2e3eae5d2442dc"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-d4e3432235f8e6d1
    - ev-fc0c467df9da6bd7
    - ev-dd3d507c5231015c
    - ev-5a68d43680dc9e8e
- assessment_id: a-2564d771adfd1b6b
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-19b63a6ad1ce6109
  evidence_ids:
  - ev-fc0c467df9da6bd7
  - ev-dd3d507c5231015c
  - ev-2564d771adfd1b6b
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-fc0c467df9da6bd7
    - ev-dd3d507c5231015c
    - ev-2564d771adfd1b6b
findings:
- finding_id: rec-f-413db41429a7056c
  issue_key: mim-reconciliation-role-support-19b63a6ad1ce6109
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: NiSO4 x 7 H2O'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-19b63a6ad1ce6109
  evidence_ids:
  - ev-fc0c467df9da6bd7
  - ev-dd3d507c5231015c
  - ev-2564d771adfd1b6b
  - ev-f6454d069cd8a1be
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Niso4_X_7_H2o.yaml
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
    review_id: 20261011T024637Z-mim-reconcile-all-batch-09
    finding_id: f-413db41429a7056c
actions:
- action_id: rec-action-413db41429a7056c
  description: 'Reassess prediction-only role support: NiSO4 x 7 H2O'
  finding_ids:
  - rec-f-413db41429a7056c
  target_ids:
  - record-19b63a6ad1ce6109
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Niso4_X_7_H2o.yaml
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
  with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.
```
