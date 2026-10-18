# Per-record structured review: Chitin (data/ingredients/mapped/Chitin.yaml)

- Review: 20261017T083000Z-chitin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Chitin (data/ingredients/mapped/Chitin.yaml, record-ad80bdbfa81b52e6, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Chitin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Chitin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-ad80bdbfa81b52e6 | data/ingredients/mapped/Chitin.yaml | maintained | Chitin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-ad80bdbfa81b52e6 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-ad80bdbfa81b52e6 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-ad80bdbfa81b52e6 | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-ad80bdbfa81b52e6.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-ad80bdbfa81b52e6.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:01:50Z; reviewed SHA-256=e44f5916dd8c17179b37da69d6ddd22906a1f4e80c5542b7c5aa9141d2e53612; current SHA-256=e44f5916dd8c17179b37da69d6ddd22906a1f4e80c5542b7c5aa9141d2e53612; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050150Z-Chitin.md","reports/yaml_record_review/Chitin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Chitin.md&#96; after the record changed from ffc63b43e3e87324e112d45d4fab3f7d3d69f19b4a1bdfe91c17cbea4e613c57 to e44f5916dd8c17179b37da69d6ddd22906a1f4e80c5542b7c5aa9141d2e53612; preserved the previous major finding floor pending targeted retirement.

### Historical provisional-role concern

evidence: concern. Targets: record-ad80bdbfa81b52e6.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-08e183f665b1509a: Reassess prediction-only role support: Chitin

major / open / confirmed; issue key: mim-reconciliation-role-support-ad80bdbfa81b52e6.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-08e183f665b1509a

Reassess prediction-only role support: Chitin

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-3f7b67425af143bc | data/ingredients/mapped/Chitin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[706],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17029","line":708,"mapping_status":"MAPPED","ontology_id":"CHEBI:17029","preferred_term":"Chitin"}],"identifier":"CHEBI:17029","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":12,"edge_count":12,"occurrences":12},"occurrence_statistics":{"media_count":12,"total_occurrences":12},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17029","ontology_label":"chitin","ontology_source":"CHEBI"},"preferred_term":"Chitin","sssom_rows":[{"data_row":737,"object_id":"CHEBI:17029","object_label":"chitin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Chitin","synonym_count":2} |
| ev-5cb82b6050e216a9 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [706] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-fb017338084fea3a | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Chitin; data-row positions=[737] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":737,"object_id":"CHEBI:17029","object_label":"chitin","other":"(1-&gt;4)-2-acetamido-2-deoxy-beta-D-glucan","predicate_id":"skos:exactMatch","subject_id":"MIM:Chitin","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-e52a672e944ef83a | docs/data/mapped_ingredients.csv; CSV lines=[708] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:17029","line":708,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"12","ontology_id":"CHEBI:17029","preferred_term":"Chitin","total_occurrences":"12"}] |
| ev-7cfac59b94fa535d | reports/yaml_record_review/20261001T050150Z-Chitin.md; YAML Record Review: Chitin:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-8f115a877535e437 | reports/yaml_record_review/Chitin.md; &#96;data/ingredients/mapped/Chitin.yaml&#96;:2; Verdict:4; Identity:12; Validation:24; Evidence:39; Completeness:56; Recommended Edits:66 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-63487389c2dfed31 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[403,1400] | context_only | [{"current_record_sha256":"e44f5916dd8c17179b37da69d6ddd22906a1f4e80c5542b7c5aa9141d2e53612","finding_id":"SEM:eed0121d17b026085e6a","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"e44f5916dd8c17179b37da69d6ddd22906a1f4e80c5542b7c5aa9141d2e53612","finding_id":"SEM:b0fe32a0b55c50e2aff6","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-4b972c1d3352fae2 | data/ingredients/mapped/Chitin.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[706],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17029","line":708,"mapping_status":"MAPPED","ontology_id":"CHEBI:17029","preferred_term":"Chitin"}],"identifier":"CHEBI:17029","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":12,"edge_count":12,"occurrences":12},"occurrence_statistics":{"media_count":12,"total_occurrences":12},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17029","ontology_label":"chitin","ontology_source":"CHEBI"},"preferred_term":"Chitin","sssom_rows":[{"data_row":737,"object_id":"CHEBI:17029","object_label":"chitin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Chitin","synonym_count":2} |
| ev-e4af2f3abaecb2d5 | reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml; findings[finding_id=f-08e183f665b1509a] | context_only | Predecessor structured review finding f-08e183f665b1509a in 20261011T024632Z-mim-reconcile-all-batch-04 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-chitin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Chitin (data/ingredients/mapped/Chitin.yaml)'
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
summary: Per-record structured review for Chitin (data/ingredients/mapped/Chitin.yaml,
  record-ad80bdbfa81b52e6, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Chitin.yaml
    sha256: e44f5916dd8c17179b37da69d6ddd22906a1f4e80c5542b7c5aa9141d2e53612
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
  - path: reports/yaml_record_review/20261001T050150Z-Chitin.md
    sha256: 69a0d46de24c9efabfce92de757c7a6bf7f5ccd55c9d326f27922daace079623
    role: context
  - path: reports/yaml_record_review/Chitin.md
    sha256: 64776dc0f49b25721b427326fb48fa35890ea811465ef20542b2b170568a887e
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-ad80bdbfa81b52e6
  path: data/ingredients/mapped/Chitin.yaml
  label: Chitin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Chitin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Chitin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Chitin.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-ad80bdbfa81b52e6
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-ad80bdbfa81b52e6
  evidence_ids:
  - ev-3f7b67425af143bc
  - ev-5cb82b6050e216a9
  - ev-fb017338084fea3a
  - ev-e52a672e944ef83a
  - ev-4b972c1d3352fae2
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-ad80bdbfa81b52e6
  evidence_ids:
  - ev-3f7b67425af143bc
  - ev-63487389c2dfed31
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-ad80bdbfa81b52e6
  evidence_ids:
  - ev-7cfac59b94fa535d
  - ev-8f115a877535e437
  - ev-63487389c2dfed31
  - ev-e4af2f3abaecb2d5
evidence:
- evidence_id: ev-3f7b67425af143bc
  kind: record_content
  reference: data/ingredients/mapped/Chitin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[706],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17029","line":708,"mapping_status":"MAPPED","ontology_id":"CHEBI:17029","preferred_term":"Chitin"}],"identifier":"CHEBI:17029","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":12,"edge_count":12,"occurrences":12},"occurrence_statistics":{"media_count":12,"total_occurrences":12},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17029","ontology_label":"chitin","ontology_source":"CHEBI"},"preferred_term":"Chitin","sssom_rows":[{"data_row":737,"object_id":"CHEBI:17029","object_label":"chitin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Chitin","synonym_count":2}'
  snapshot_sha256: e44f5916dd8c17179b37da69d6ddd22906a1f4e80c5542b7c5aa9141d2e53612
- evidence_id: ev-5cb82b6050e216a9
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [706]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-fb017338084fea3a
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Chitin; data-row positions=[737]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":737,"object_id":"CHEBI:17029","object_label":"chitin","other":"(1->4)-2-acetamido-2-deoxy-beta-D-glucan","predicate_id":"skos:exactMatch","subject_id":"MIM:Chitin","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-e52a672e944ef83a
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[708]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:17029","line":708,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"12","ontology_id":"CHEBI:17029","preferred_term":"Chitin","total_occurrences":"12"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-7cfac59b94fa535d
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050150Z-Chitin.md
  locator: 'YAML Record Review: Chitin:2; Target:10; Validation:20; Identity and Grounding:27;
    Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61;
    Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 69a0d46de24c9efabfce92de757c7a6bf7f5ccd55c9d326f27922daace079623
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/Chitin.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The exact
    CHEBI chitin identity, structure fields, and 12/12 occurrence count pass, but
    a hydrolysis source statement is exported as a synonym and CARBON_SOURCE is only
    provisional.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Chitin.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Chitin.yaml`,
    `just validate-terms data/ingredients/mapped/Chitin.yaml` where applicable, and
    `just qc-sssom`.'
- evidence_id: ev-8f115a877535e437
  kind: prior_review
  reference: reports/yaml_record_review/Chitin.md
  locator: '`data/ingredients/mapped/Chitin.yaml`:2; Verdict:4; Identity:12; Validation:24;
    Evidence:39; Completeness:56; Recommended Edits:66'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 64776dc0f49b25721b427326fb48fa35890ea811465ef20542b2b170568a887e
  quote: "Recommended Edits:\n- Major: either remove `hydrolysis: crab shell chitin`\
    \ from\n  `data/ingredients/mapped/Chitin.yaml` or extend\n  `src/mediaingredientmech/synonym_policy.py`\
    \ so `hydrolysis:` source\n  statements stay in provenance without resolving as\
    \ ingredient synonyms.\n- Major: either replace `nutritional_roles.CARBON_SOURCE`\
    \ with inspected\n  evidence for chitin as a carbon source in this media scope,\
    \ or remove the\n  role.\n- Regenerate synchronized outputs and rerun strict validation,\
    \ SSSOM QC,\n  aggregate roundtrip, docs generation, and `git diff --check`."
- evidence_id: ev-63487389c2dfed31
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[403,1400]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"e44f5916dd8c17179b37da69d6ddd22906a1f4e80c5542b7c5aa9141d2e53612","finding_id":"SEM:eed0121d17b026085e6a","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"e44f5916dd8c17179b37da69d6ddd22906a1f4e80c5542b7c5aa9141d2e53612","finding_id":"SEM:b0fe32a0b55c50e2aff6","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-4b972c1d3352fae2
  kind: record_content
  reference: data/ingredients/mapped/Chitin.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[706],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17029","line":708,"mapping_status":"MAPPED","ontology_id":"CHEBI:17029","preferred_term":"Chitin"}],"identifier":"CHEBI:17029","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":12,"edge_count":12,"occurrences":12},"occurrence_statistics":{"media_count":12,"total_occurrences":12},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17029","ontology_label":"chitin","ontology_source":"CHEBI"},"preferred_term":"Chitin","sssom_rows":[{"data_row":737,"object_id":"CHEBI:17029","object_label":"chitin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Chitin","synonym_count":2}'
  snapshot_sha256: e44f5916dd8c17179b37da69d6ddd22906a1f4e80c5542b7c5aa9141d2e53612
- evidence_id: ev-e4af2f3abaecb2d5
  kind: prior_review
  reference: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
  locator: findings[finding_id=f-08e183f665b1509a]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-08e183f665b1509a in 20261011T024632Z-mim-reconcile-all-batch-04
  snapshot_sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
assessments:
- assessment_id: a-625b7d9d26036655
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-ad80bdbfa81b52e6
  evidence_ids:
  - ev-3f7b67425af143bc
  - ev-5cb82b6050e216a9
  - ev-fb017338084fea3a
  - ev-e52a672e944ef83a
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-b3ffcb86f4befd0d
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-ad80bdbfa81b52e6
  evidence_ids:
  - ev-7cfac59b94fa535d
  - ev-8f115a877535e437
  - ev-3f7b67425af143bc
  - ev-63487389c2dfed31
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:01:50Z;
    reviewed SHA-256=e44f5916dd8c17179b37da69d6ddd22906a1f4e80c5542b7c5aa9141d2e53612;
    current SHA-256=e44f5916dd8c17179b37da69d6ddd22906a1f4e80c5542b7c5aa9141d2e53612;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050150Z-Chitin.md","reports/yaml_record_review/Chitin.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Chitin.md` after the record changed from ffc63b43e3e87324e112d45d4fab3f7d3d69f19b4a1bdfe91c17cbea4e613c57
    to e44f5916dd8c17179b37da69d6ddd22906a1f4e80c5542b7c5aa9141d2e53612; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-7cfac59b94fa535d
    - ev-8f115a877535e437
    - ev-3f7b67425af143bc
  - name: legacy-native-ids
    value: '["SEM:eed0121d17b026085e6a","SEM:b0fe32a0b55c50e2aff6"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-3f7b67425af143bc
    - ev-7cfac59b94fa535d
    - ev-8f115a877535e437
    - ev-63487389c2dfed31
- assessment_id: a-4b972c1d3352fae2
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-ad80bdbfa81b52e6
  evidence_ids:
  - ev-7cfac59b94fa535d
  - ev-8f115a877535e437
  - ev-4b972c1d3352fae2
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-7cfac59b94fa535d
    - ev-8f115a877535e437
    - ev-4b972c1d3352fae2
findings:
- finding_id: rec-f-08e183f665b1509a
  issue_key: mim-reconciliation-role-support-ad80bdbfa81b52e6
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Chitin'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-ad80bdbfa81b52e6
  evidence_ids:
  - ev-7cfac59b94fa535d
  - ev-8f115a877535e437
  - ev-4b972c1d3352fae2
  - ev-e4af2f3abaecb2d5
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Chitin.yaml
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
    finding_id: f-08e183f665b1509a
actions:
- action_id: rec-action-08e183f665b1509a
  description: 'Reassess prediction-only role support: Chitin'
  finding_ids:
  - rec-f-08e183f665b1509a
  target_ids:
  - record-ad80bdbfa81b52e6
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Chitin.yaml
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
