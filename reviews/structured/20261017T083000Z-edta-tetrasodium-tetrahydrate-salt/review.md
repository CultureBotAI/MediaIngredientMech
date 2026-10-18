# Per-record structured review: EDTA_Tetrasodium_Tetrahydrate_Salt (data/ingredients/mapped/EDTA_Tetrasodium_Tetrahydrate_Salt.yaml)

- Review: 20261017T083000Z-edta-tetrasodium-tetrahydrate-salt
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for EDTA_Tetrasodium_Tetrahydrate_Salt (data/ingredients/mapped/EDTA_Tetrasodium_Tetrahydrate_Salt.yaml, record-96b251b676c9fd27, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/EDTA_Tetrasodium_Tetrahydrate_Salt.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/EDTA_Tetrasodium_Tetrahydrate_Salt.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-96b251b676c9fd27 | data/ingredients/mapped/EDTA_Tetrasodium_Tetrahydrate_Salt.yaml | maintained | EDTA_Tetrasodium_Tetrahydrate_Salt |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-96b251b676c9fd27 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-96b251b676c9fd27 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-96b251b676c9fd27 | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-96b251b676c9fd27.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-96b251b676c9fd27.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T15:27:45Z; reviewed SHA-256=ebbc88a44ee8920c810e31101fe3a303956c5061f9265b10adea414f40bc0b6d; current SHA-256=ebbc88a44ee8920c810e31101fe3a303956c5061f9265b10adea414f40bc0b6d; hash_changed=False. Reports=["reports/yaml_record_review/EDTA_Tetrasodium_Tetrahydrate_Salt.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS hydrate identity passes, but parent/free EDTA aliases leak into final SSSOM and CHELATOR is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-96b251b676c9fd27.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-4af9ad16f02aa8fa: Reassess prediction-only role support: EDTA tetrasodium tetrahydrate salt

major / open / confirmed; issue key: mim-reconciliation-role-support-96b251b676c9fd27.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-4af9ad16f02aa8fa

Reassess prediction-only role support: EDTA tetrasodium tetrahydrate salt

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-88f232fd516de81a | data/ingredients/mapped/EDTA_Tetrasodium_Tetrahydrate_Salt.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[934],"raw_equal":true},"docs_rows":[{"identifier":"cas:13235-36-4","line":936,"mapping_status":"MAPPED","ontology_id":"CHEBI:4735","preferred_term":"EDTA tetrasodium tetrahydrate salt"}],"identifier":"cas:13235-36-4","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:4735","ontology_label":"ethylenediaminetetraacetic acid","ontology_source":"CHEBI"},"preferred_term":"EDTA tetrasodium tetrahydrate salt","sssom_rows":[{"data_row":1106,"object_id":"CHEBI:4735","object_label":"ethylenediaminetetraacetic acid","predicate_id":"skos:closeMatch"},{"data_row":1107,"object_id":"cas:13235-36-4","object_label":"EDTA tetrasodium tetrahydrate salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:EDTA_Tetrasodium_Tetrahydrate_Salt","synonym_count":1} |
| ev-444c5e223b486f46 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [934] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-cbf559cc2b061fdc | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:EDTA_Tetrasodium_Tetrahydrate_Salt; data-row positions=[1106, 1107] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1106,"object_id":"CHEBI:4735","object_label":"ethylenediaminetetraacetic acid","other":"EDTA&#124;Ethylenediamintetraacetic acid (EDTA)&#124;CAS:13235-36-4","predicate_id":"skos:closeMatch","subject_id":"MIM:EDTA_Tetrasodium_Tetrahydrate_Salt","validation_method":"OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-09-02"},{"data_row":1107,"object_id":"cas:13235-36-4","object_label":"EDTA tetrasodium tetrahydrate salt","other":"CAS:13235-36-4","predicate_id":"skos:exactMatch","subject_id":"MIM:EDTA_Tetrasodium_Tetrahydrate_Salt","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-52a0512964c4b46e | docs/data/mapped_ingredients.csv; CSV lines=[936] | supports | Published identity and count rows inspected: [{"identifier":"cas:13235-36-4","line":936,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"3","ontology_id":"CHEBI:4735","preferred_term":"EDTA tetrasodium tetrahydrate salt","total_occurrences":"3"}] |
| ev-aebb5fa2d7d63669 | reports/yaml_record_review/EDTA_Tetrasodium_Tetrahydrate_Salt.md; &#96;data/ingredients/mapped/EDTA_Tetrasodium_Tetrahydrate_Salt.yaml&#96;:2; Verdict:4; Identity:11; Validation:26; Evidence:33; Completeness:56; Recommended Edits:63 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-40d61c6b193b30fe | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[563,1641] | context_only | [{"current_record_sha256":"ebbc88a44ee8920c810e31101fe3a303956c5061f9265b10adea414f40bc0b6d","finding_id":"SEM:c7feb978074df8e15c14","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"ebbc88a44ee8920c810e31101fe3a303956c5061f9265b10adea414f40bc0b6d","finding_id":"SEM:45487521c8a999ef0b09","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-92e9094197a763e9 | data/ingredients/mapped/EDTA_Tetrasodium_Tetrahydrate_Salt.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[934],"raw_equal":true},"docs_rows":[{"identifier":"cas:13235-36-4","line":936,"mapping_status":"MAPPED","ontology_id":"CHEBI:4735","preferred_term":"EDTA tetrasodium tetrahydrate salt"}],"identifier":"cas:13235-36-4","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:4735","ontology_label":"ethylenediaminetetraacetic acid","ontology_source":"CHEBI"},"preferred_term":"EDTA tetrasodium tetrahydrate salt","sssom_rows":[{"data_row":1106,"object_id":"CHEBI:4735","object_label":"ethylenediaminetetraacetic acid","predicate_id":"skos:closeMatch"},{"data_row":1107,"object_id":"cas:13235-36-4","object_label":"EDTA tetrasodium tetrahydrate salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:EDTA_Tetrasodium_Tetrahydrate_Salt","synonym_count":1} |
| ev-12a63d4c652bc23d | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-4af9ad16f02aa8fa] | context_only | Predecessor structured review finding f-4af9ad16f02aa8fa in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-edta-tetrasodium-tetrahydrate-salt
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: EDTA_Tetrasodium_Tetrahydrate_Salt (data/ingredients/mapped/EDTA_Tetrasodium_Tetrahydrate_Salt.yaml)'
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
summary: Per-record structured review for EDTA_Tetrasodium_Tetrahydrate_Salt (data/ingredients/mapped/EDTA_Tetrasodium_Tetrahydrate_Salt.yaml,
  record-96b251b676c9fd27, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/EDTA_Tetrasodium_Tetrahydrate_Salt.yaml
    sha256: ebbc88a44ee8920c810e31101fe3a303956c5061f9265b10adea414f40bc0b6d
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
  - path: reports/yaml_record_review/EDTA_Tetrasodium_Tetrahydrate_Salt.md
    sha256: f3b86ea52022f0b2667825568de4470cdf91872d5c31985c8e5209401817f8e6
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-96b251b676c9fd27
  path: data/ingredients/mapped/EDTA_Tetrasodium_Tetrahydrate_Salt.yaml
  label: EDTA_Tetrasodium_Tetrahydrate_Salt
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/EDTA_Tetrasodium_Tetrahydrate_Salt.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/EDTA_Tetrasodium_Tetrahydrate_Salt.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/EDTA_Tetrasodium_Tetrahydrate_Salt.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-96b251b676c9fd27
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-96b251b676c9fd27
  evidence_ids:
  - ev-88f232fd516de81a
  - ev-444c5e223b486f46
  - ev-cbf559cc2b061fdc
  - ev-52a0512964c4b46e
  - ev-92e9094197a763e9
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-96b251b676c9fd27
  evidence_ids:
  - ev-88f232fd516de81a
  - ev-40d61c6b193b30fe
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-96b251b676c9fd27
  evidence_ids:
  - ev-aebb5fa2d7d63669
  - ev-40d61c6b193b30fe
  - ev-12a63d4c652bc23d
evidence:
- evidence_id: ev-88f232fd516de81a
  kind: record_content
  reference: data/ingredients/mapped/EDTA_Tetrasodium_Tetrahydrate_Salt.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[934],"raw_equal":true},"docs_rows":[{"identifier":"cas:13235-36-4","line":936,"mapping_status":"MAPPED","ontology_id":"CHEBI:4735","preferred_term":"EDTA
    tetrasodium tetrahydrate salt"}],"identifier":"cas:13235-36-4","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:4735","ontology_label":"ethylenediaminetetraacetic
    acid","ontology_source":"CHEBI"},"preferred_term":"EDTA tetrasodium tetrahydrate
    salt","sssom_rows":[{"data_row":1106,"object_id":"CHEBI:4735","object_label":"ethylenediaminetetraacetic
    acid","predicate_id":"skos:closeMatch"},{"data_row":1107,"object_id":"cas:13235-36-4","object_label":"EDTA
    tetrasodium tetrahydrate salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:EDTA_Tetrasodium_Tetrahydrate_Salt","synonym_count":1}'
  snapshot_sha256: ebbc88a44ee8920c810e31101fe3a303956c5061f9265b10adea414f40bc0b6d
- evidence_id: ev-444c5e223b486f46
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [934]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-cbf559cc2b061fdc
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:EDTA_Tetrasodium_Tetrahydrate_Salt; data-row positions=[1106,
    1107]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1106,"object_id":"CHEBI:4735","object_label":"ethylenediaminetetraacetic
    acid","other":"EDTA|Ethylenediamintetraacetic acid (EDTA)|CAS:13235-36-4","predicate_id":"skos:closeMatch","subject_id":"MIM:EDTA_Tetrasodium_Tetrahydrate_Salt","validation_method":"OLS:chebi|SYNONYM_ENRICH|2026-09-02"},{"data_row":1107,"object_id":"cas:13235-36-4","object_label":"EDTA
    tetrasodium tetrahydrate salt","other":"CAS:13235-36-4","predicate_id":"skos:exactMatch","subject_id":"MIM:EDTA_Tetrasodium_Tetrahydrate_Salt","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-52a0512964c4b46e
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[936]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:13235-36-4","line":936,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"3","ontology_id":"CHEBI:4735","preferred_term":"EDTA
    tetrasodium tetrahydrate salt","total_occurrences":"3"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-aebb5fa2d7d63669
  kind: prior_review
  reference: reports/yaml_record_review/EDTA_Tetrasodium_Tetrahydrate_Salt.md
  locator: '`data/ingredients/mapped/EDTA_Tetrasodium_Tetrahydrate_Salt.yaml`:2; Verdict:4;
    Identity:11; Validation:26; Evidence:33; Completeness:56; Recommended Edits:63'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: f3b86ea52022f0b2667825568de4470cdf91872d5c31985c8e5209401817f8e6
  quote: "Recommended Edits:\n- Major: remove `EDTA` and `Ethylenediamintetraacetic\
    \ acid (EDTA)` from the\n  active same-subject synonym surface for\n  `data/ingredients/mapped/EDTA_Tetrasodium_Tetrahydrate_Salt.yaml`,\
    \ or mark\n  them as rejected/provenance-only so the final SSSOM parent row no\
    \ longer\n  exports them in `other`.\n- Major: either replace the provisional\
    \ `physicochemical_roles.CHELATOR`\n  evidence with claim-level support for EDTA\
    \ tetrasodium tetrahydrate salt, or\n  remove the role until a supported role\
    \ can be curated.\n- After editing the per-record YAML, run `sync-curated`, rebuild\
    \ or reconcile\n  the SSSOM from the maintained source, and rerun `validate-all`,\
    \ `qc-sssom`,\n  `validate_component_partonomy.py`, and the strict validator."
- evidence_id: ev-40d61c6b193b30fe
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[563,1641]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"ebbc88a44ee8920c810e31101fe3a303956c5061f9265b10adea414f40bc0b6d","finding_id":"SEM:c7feb978074df8e15c14","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"ebbc88a44ee8920c810e31101fe3a303956c5061f9265b10adea414f40bc0b6d","finding_id":"SEM:45487521c8a999ef0b09","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-92e9094197a763e9
  kind: record_content
  reference: data/ingredients/mapped/EDTA_Tetrasodium_Tetrahydrate_Salt.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[934],"raw_equal":true},"docs_rows":[{"identifier":"cas:13235-36-4","line":936,"mapping_status":"MAPPED","ontology_id":"CHEBI:4735","preferred_term":"EDTA
    tetrasodium tetrahydrate salt"}],"identifier":"cas:13235-36-4","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:4735","ontology_label":"ethylenediaminetetraacetic
    acid","ontology_source":"CHEBI"},"preferred_term":"EDTA tetrasodium tetrahydrate
    salt","sssom_rows":[{"data_row":1106,"object_id":"CHEBI:4735","object_label":"ethylenediaminetetraacetic
    acid","predicate_id":"skos:closeMatch"},{"data_row":1107,"object_id":"cas:13235-36-4","object_label":"EDTA
    tetrasodium tetrahydrate salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:EDTA_Tetrasodium_Tetrahydrate_Salt","synonym_count":1}'
  snapshot_sha256: ebbc88a44ee8920c810e31101fe3a303956c5061f9265b10adea414f40bc0b6d
- evidence_id: ev-12a63d4c652bc23d
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-4af9ad16f02aa8fa]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-4af9ad16f02aa8fa in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-8689548deb447f90
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-96b251b676c9fd27
  evidence_ids:
  - ev-88f232fd516de81a
  - ev-444c5e223b486f46
  - ev-cbf559cc2b061fdc
  - ev-52a0512964c4b46e
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-0992221be106dbf1
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-96b251b676c9fd27
  evidence_ids:
  - ev-aebb5fa2d7d63669
  - ev-88f232fd516de81a
  - ev-40d61c6b193b30fe
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T15:27:45Z;
    reviewed SHA-256=ebbc88a44ee8920c810e31101fe3a303956c5061f9265b10adea414f40bc0b6d;
    current SHA-256=ebbc88a44ee8920c810e31101fe3a303956c5061f9265b10adea414f40bc0b6d;
    hash_changed=False. Reports=["reports/yaml_record_review/EDTA_Tetrasodium_Tetrahydrate_Salt.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS
    hydrate identity passes, but parent/free EDTA aliases leak into final SSSOM and
    CHELATOR is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-aebb5fa2d7d63669
    - ev-88f232fd516de81a
  - name: legacy-native-ids
    value: '["SEM:c7feb978074df8e15c14","SEM:45487521c8a999ef0b09"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-88f232fd516de81a
    - ev-aebb5fa2d7d63669
    - ev-40d61c6b193b30fe
- assessment_id: a-92e9094197a763e9
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-96b251b676c9fd27
  evidence_ids:
  - ev-aebb5fa2d7d63669
  - ev-92e9094197a763e9
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-aebb5fa2d7d63669
    - ev-92e9094197a763e9
findings:
- finding_id: rec-f-4af9ad16f02aa8fa
  issue_key: mim-reconciliation-role-support-96b251b676c9fd27
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: EDTA tetrasodium tetrahydrate salt'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-96b251b676c9fd27
  evidence_ids:
  - ev-aebb5fa2d7d63669
  - ev-92e9094197a763e9
  - ev-12a63d4c652bc23d
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/EDTA_Tetrasodium_Tetrahydrate_Salt.yaml
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
    review_id: 20261011T024633Z-mim-reconcile-all-batch-05
    finding_id: f-4af9ad16f02aa8fa
actions:
- action_id: rec-action-4af9ad16f02aa8fa
  description: 'Reassess prediction-only role support: EDTA tetrasodium tetrahydrate
    salt'
  finding_ids:
  - rec-f-4af9ad16f02aa8fa
  target_ids:
  - record-96b251b676c9fd27
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/EDTA_Tetrasodium_Tetrahydrate_Salt.yaml
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
