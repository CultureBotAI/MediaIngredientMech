# Per-record structured review: Dl-mevalonic_Acid (data/ingredients/mapped/Dl-mevalonic_Acid.yaml)

- Review: 20261017T083000Z-dl-mevalonic-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Dl-mevalonic_Acid (data/ingredients/mapped/Dl-mevalonic_Acid.yaml, record-28f6e3bfb163aea0, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Dl-mevalonic_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Dl-mevalonic_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-28f6e3bfb163aea0 | data/ingredients/mapped/Dl-mevalonic_Acid.yaml | maintained | Dl-mevalonic_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-28f6e3bfb163aea0 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-28f6e3bfb163aea0 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-28f6e3bfb163aea0 | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-28f6e3bfb163aea0.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-28f6e3bfb163aea0.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:10Z; reviewed SHA-256=7fd9e8630dce65d4ff8aab42622cb23d6ea695aee428a49be0fc8a63afb1c1be; current SHA-256=7fd9e8630dce65d4ff8aab42622cb23d6ea695aee428a49be0fc8a63afb1c1be; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050210Z-Dl-mevalonic_Acid.md","reports/yaml_record_review/Dl-mevalonic_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Dl-mevalonic_Acid.md&#96; after the record changed from 2286c5f2dccd7eee68191f856425771fb7d4d4bb62cfa9e37d2835cfcb128d78 to 7fd9e8630dce65d4ff8aab42622cb23d6ea695aee428a49be0fc8a63afb1c1be; preserved the previous major finding floor pending targeted retirement.

### Historical provisional-role concern

evidence: concern. Targets: record-28f6e3bfb163aea0.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-d6b66c96e0d63634: Reassess prediction-only role support: DL-mevalonic acid

major / open / confirmed; issue key: mim-reconciliation-role-support-28f6e3bfb163aea0.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-d6b66c96e0d63634

Reassess prediction-only role support: DL-mevalonic acid

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-4650818823d20f8a | data/ingredients/mapped/Dl-mevalonic_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[917],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:25351","line":919,"mapping_status":"MAPPED","ontology_id":"CHEBI:25351","preferred_term":"DL-mevalonic acid"}],"identifier":"CHEBI:25351","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":6,"edge_count":6,"occurrences":6},"occurrence_statistics":{"media_count":6,"total_occurrences":6},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:25351","ontology_label":"mevalonic acid","ontology_source":"CHEBI"},"preferred_term":"DL-mevalonic acid","sssom_rows":[{"data_row":1080,"object_id":"CHEBI:25351","object_label":"mevalonic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Dl-mevalonic_Acid","synonym_count":2} |
| ev-54c3fd96d576b5b1 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [917] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-a07d9bc1d929065e | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Dl-mevalonic_Acid; data-row positions=[1080] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1080,"object_id":"CHEBI:25351","object_label":"mevalonic acid","other":"rac-3,5-dihydroxy-3-methylpentanoic acid&#124;CAS:150-97-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Dl-mevalonic_Acid","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-7f7651d779cb0b9f | docs/data/mapped_ingredients.csv; CSV lines=[919] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:25351","line":919,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"6","ontology_id":"CHEBI:25351","preferred_term":"DL-mevalonic acid","total_occurrences":"6"}] |
| ev-faf63cd63702d63b | reports/yaml_record_review/20261001T050210Z-Dl-mevalonic_Acid.md; YAML Record Review: DL-mevalonic acid:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-dcb85f32a28dfc5f | reports/yaml_record_review/Dl-mevalonic_Acid.md; &#96;data/ingredients/mapped/Dl-mevalonic_Acid.yaml&#96;:2; Verdict:4; Identity:12; Validation:25; Evidence:41; Completeness:63; Recommended Edits:70 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-cb61523f222d606a | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[552,1954] | context_only | [{"current_record_sha256":"7fd9e8630dce65d4ff8aab42622cb23d6ea695aee428a49be0fc8a63afb1c1be","finding_id":"SEM:857ae50acfe783557ec5","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"7fd9e8630dce65d4ff8aab42622cb23d6ea695aee428a49be0fc8a63afb1c1be","finding_id":"SEM:b8d51764dbe866fa07bc","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-554640a8220e3013 | data/ingredients/mapped/Dl-mevalonic_Acid.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[917],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:25351","line":919,"mapping_status":"MAPPED","ontology_id":"CHEBI:25351","preferred_term":"DL-mevalonic acid"}],"identifier":"CHEBI:25351","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":6,"edge_count":6,"occurrences":6},"occurrence_statistics":{"media_count":6,"total_occurrences":6},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:25351","ontology_label":"mevalonic acid","ontology_source":"CHEBI"},"preferred_term":"DL-mevalonic acid","sssom_rows":[{"data_row":1080,"object_id":"CHEBI:25351","object_label":"mevalonic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Dl-mevalonic_Acid","synonym_count":2} |
| ev-7fc426689f1455fa | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-d6b66c96e0d63634] | context_only | Predecessor structured review finding f-d6b66c96e0d63634 in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-dl-mevalonic-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Dl-mevalonic_Acid (data/ingredients/mapped/Dl-mevalonic_Acid.yaml)'
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
summary: Per-record structured review for Dl-mevalonic_Acid (data/ingredients/mapped/Dl-mevalonic_Acid.yaml,
  record-28f6e3bfb163aea0, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Dl-mevalonic_Acid.yaml
    sha256: 7fd9e8630dce65d4ff8aab42622cb23d6ea695aee428a49be0fc8a63afb1c1be
    role: target
  - path: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
    sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
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
  - path: reports/yaml_record_review/20261001T050210Z-Dl-mevalonic_Acid.md
    sha256: b80ef180230a48e06da697dad5c529cdd23692ead95779b0e1327b0af9f05c8d
    role: context
  - path: reports/yaml_record_review/Dl-mevalonic_Acid.md
    sha256: d568afb4cec3ff30098cb90e53e3b3541abe645b47a4be8af0b263c88bd5a71d
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-28f6e3bfb163aea0
  path: data/ingredients/mapped/Dl-mevalonic_Acid.yaml
  label: Dl-mevalonic_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Dl-mevalonic_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Dl-mevalonic_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Dl-mevalonic_Acid.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-28f6e3bfb163aea0
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-28f6e3bfb163aea0
  evidence_ids:
  - ev-4650818823d20f8a
  - ev-54c3fd96d576b5b1
  - ev-a07d9bc1d929065e
  - ev-7f7651d779cb0b9f
  - ev-554640a8220e3013
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-28f6e3bfb163aea0
  evidence_ids:
  - ev-4650818823d20f8a
  - ev-cb61523f222d606a
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-28f6e3bfb163aea0
  evidence_ids:
  - ev-faf63cd63702d63b
  - ev-dcb85f32a28dfc5f
  - ev-cb61523f222d606a
  - ev-7fc426689f1455fa
evidence:
- evidence_id: ev-4650818823d20f8a
  kind: record_content
  reference: data/ingredients/mapped/Dl-mevalonic_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[917],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:25351","line":919,"mapping_status":"MAPPED","ontology_id":"CHEBI:25351","preferred_term":"DL-mevalonic
    acid"}],"identifier":"CHEBI:25351","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":6,"edge_count":6,"occurrences":6},"occurrence_statistics":{"media_count":6,"total_occurrences":6},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:25351","ontology_label":"mevalonic
    acid","ontology_source":"CHEBI"},"preferred_term":"DL-mevalonic acid","sssom_rows":[{"data_row":1080,"object_id":"CHEBI:25351","object_label":"mevalonic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Dl-mevalonic_Acid","synonym_count":2}'
  snapshot_sha256: 7fd9e8630dce65d4ff8aab42622cb23d6ea695aee428a49be0fc8a63afb1c1be
- evidence_id: ev-54c3fd96d576b5b1
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [917]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-a07d9bc1d929065e
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Dl-mevalonic_Acid; data-row positions=[1080]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1080,"object_id":"CHEBI:25351","object_label":"mevalonic
    acid","other":"rac-3,5-dihydroxy-3-methylpentanoic acid|CAS:150-97-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Dl-mevalonic_Acid","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-7f7651d779cb0b9f
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[919]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:25351","line":919,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"6","ontology_id":"CHEBI:25351","preferred_term":"DL-mevalonic
    acid","total_occurrences":"6"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-faf63cd63702d63b
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050210Z-Dl-mevalonic_Acid.md
  locator: 'YAML Record Review: DL-mevalonic acid:2; Target:10; Validation:20; Identity
    and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: b80ef180230a48e06da697dad5c529cdd23692ead95779b0e1327b0af9f05c8d
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/Dl-mevalonic_Acid.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The mevalonic
    acid identity passes, but an unrelated polysaccharide synonym leaks into SSSOM
    and the carbon-source role is computational.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Dl-mevalonic_Acid.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Dl-mevalonic_Acid.yaml`,
    `just validate-terms data/ingredients/mapped/Dl-mevalonic_Acid.yaml` where applicable,
    and `just qc-sssom`.'
- evidence_id: ev-dcb85f32a28dfc5f
  kind: prior_review
  reference: reports/yaml_record_review/Dl-mevalonic_Acid.md
  locator: '`data/ingredients/mapped/Dl-mevalonic_Acid.yaml`:2; Verdict:4; Identity:12;
    Validation:25; Evidence:41; Completeness:63; Recommended Edits:70'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: d568afb4cec3ff30098cb90e53e3b3541abe645b47a4be8af0b263c88bd5a71d
  quote: "Recommended Edits:\n- Major: demote the complex-polysaccharide label in\n\
    \  `data/ingredients/mapped/Dl-mevalonic_Acid.yaml` to `REJECTED_LABEL`\n  provenance\
    \ or remove it from active synonymy; then regenerate\n  `mappings/ingredient_mappings.sssom.tsv`\
    \ and synchronize\n  `data/curated/mapped_ingredients.yaml`.\n- Major: replace\
    \ the `CARBON_SOURCE` computational role with source-backed role\n  evidence scoped\
    \ to DL-mevalonic acid, or remove the role if no support is\n  available; then\
    \ synchronize `data/curated/mapped_ingredients.yaml`."
- evidence_id: ev-cb61523f222d606a
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[552,1954]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"7fd9e8630dce65d4ff8aab42622cb23d6ea695aee428a49be0fc8a63afb1c1be","finding_id":"SEM:857ae50acfe783557ec5","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"7fd9e8630dce65d4ff8aab42622cb23d6ea695aee428a49be0fc8a63afb1c1be","finding_id":"SEM:b8d51764dbe866fa07bc","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-554640a8220e3013
  kind: record_content
  reference: data/ingredients/mapped/Dl-mevalonic_Acid.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[917],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:25351","line":919,"mapping_status":"MAPPED","ontology_id":"CHEBI:25351","preferred_term":"DL-mevalonic
    acid"}],"identifier":"CHEBI:25351","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":6,"edge_count":6,"occurrences":6},"occurrence_statistics":{"media_count":6,"total_occurrences":6},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:25351","ontology_label":"mevalonic
    acid","ontology_source":"CHEBI"},"preferred_term":"DL-mevalonic acid","sssom_rows":[{"data_row":1080,"object_id":"CHEBI:25351","object_label":"mevalonic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Dl-mevalonic_Acid","synonym_count":2}'
  snapshot_sha256: 7fd9e8630dce65d4ff8aab42622cb23d6ea695aee428a49be0fc8a63afb1c1be
- evidence_id: ev-7fc426689f1455fa
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-d6b66c96e0d63634]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-d6b66c96e0d63634 in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-6dd24d0e1ff0ade3
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-28f6e3bfb163aea0
  evidence_ids:
  - ev-4650818823d20f8a
  - ev-54c3fd96d576b5b1
  - ev-a07d9bc1d929065e
  - ev-7f7651d779cb0b9f
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-e9f8cbac5c925f29
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-28f6e3bfb163aea0
  evidence_ids:
  - ev-faf63cd63702d63b
  - ev-dcb85f32a28dfc5f
  - ev-4650818823d20f8a
  - ev-cb61523f222d606a
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:10Z;
    reviewed SHA-256=7fd9e8630dce65d4ff8aab42622cb23d6ea695aee428a49be0fc8a63afb1c1be;
    current SHA-256=7fd9e8630dce65d4ff8aab42622cb23d6ea695aee428a49be0fc8a63afb1c1be;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050210Z-Dl-mevalonic_Acid.md","reports/yaml_record_review/Dl-mevalonic_Acid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Dl-mevalonic_Acid.md` after the record changed from
    2286c5f2dccd7eee68191f856425771fb7d4d4bb62cfa9e37d2835cfcb128d78 to 7fd9e8630dce65d4ff8aab42622cb23d6ea695aee428a49be0fc8a63afb1c1be;
    preserved the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-faf63cd63702d63b
    - ev-dcb85f32a28dfc5f
    - ev-4650818823d20f8a
  - name: legacy-native-ids
    value: '["SEM:857ae50acfe783557ec5","SEM:b8d51764dbe866fa07bc"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-4650818823d20f8a
    - ev-faf63cd63702d63b
    - ev-dcb85f32a28dfc5f
    - ev-cb61523f222d606a
- assessment_id: a-554640a8220e3013
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-28f6e3bfb163aea0
  evidence_ids:
  - ev-faf63cd63702d63b
  - ev-dcb85f32a28dfc5f
  - ev-554640a8220e3013
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-faf63cd63702d63b
    - ev-dcb85f32a28dfc5f
    - ev-554640a8220e3013
findings:
- finding_id: rec-f-d6b66c96e0d63634
  issue_key: mim-reconciliation-role-support-28f6e3bfb163aea0
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: DL-mevalonic acid'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-28f6e3bfb163aea0
  evidence_ids:
  - ev-faf63cd63702d63b
  - ev-dcb85f32a28dfc5f
  - ev-554640a8220e3013
  - ev-7fc426689f1455fa
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Dl-mevalonic_Acid.yaml
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
    review_id: 20261011T024633Z-mim-reconcile-all-batch-05
    finding_id: f-d6b66c96e0d63634
actions:
- action_id: rec-action-d6b66c96e0d63634
  description: 'Reassess prediction-only role support: DL-mevalonic acid'
  finding_ids:
  - rec-f-d6b66c96e0d63634
  target_ids:
  - record-28f6e3bfb163aea0
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Dl-mevalonic_Acid.yaml
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
  with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.
```
