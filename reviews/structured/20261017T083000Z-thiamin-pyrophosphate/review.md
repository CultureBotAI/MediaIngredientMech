# Per-record structured review: Thiamin_Pyrophosphate (data/ingredients/mapped/Thiamin_Pyrophosphate.yaml)

- Review: 20261017T083000Z-thiamin-pyrophosphate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Thiamin_Pyrophosphate (data/ingredients/mapped/Thiamin_Pyrophosphate.yaml, record-dff17523de241273, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Thiamin_Pyrophosphate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Thiamin_Pyrophosphate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-dff17523de241273 | data/ingredients/mapped/Thiamin_Pyrophosphate.yaml | maintained | Thiamin_Pyrophosphate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-dff17523de241273 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-dff17523de241273 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-dff17523de241273 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-dff17523de241273.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-dff17523de241273.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T18:32:01Z; reviewed SHA-256=db23730b8e0c69f8f3711697b971f39a2203f5105ba91610992f925df8bc07bf; current SHA-256=db23730b8e0c69f8f3711697b971f39a2203f5105ba91610992f925df8bc07bf; hash_changed=False. Reports=["reports/yaml_record_review/Thiamin_Pyrophosphate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The synonym match to CHEBI:45931, CAS RN, structure fields, aggregate row, and final SSSOM row pass, but VITAMIN_SOURCE is still provisional ChEBI-ancestry evidence.

### Historical provisional-role concern

evidence: concern. Targets: record-dff17523de241273.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-7aa96d9cdc46e89b: Reassess prediction-only role support: Thiamin pyrophosphate

major / open / confirmed; issue key: mim-reconciliation-role-support-dff17523de241273.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-7aa96d9cdc46e89b

Reassess prediction-only role support: Thiamin pyrophosphate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-168708c633faf5b1 | data/ingredients/mapped/Thiamin_Pyrophosphate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1952],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:45931","line":1954,"mapping_status":"MAPPED","ontology_id":"CHEBI:45931","preferred_term":"Thiamin pyrophosphate"}],"identifier":"CHEBI:45931","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:45931","ontology_label":"thiamine(1+) diphosphate(1-)","ontology_source":"CHEBI"},"preferred_term":"Thiamin pyrophosphate","sssom_rows":[{"data_row":2761,"object_id":"CHEBI:45931","object_label":"thiamine(1+) diphosphate(1-)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Thiamin_Pyrophosphate","synonym_count":1} |
| ev-02c37d5ca95a62cd | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1952] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-f71f78c3fb347a5a | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Thiamin_Pyrophosphate; data-row positions=[2761] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2761,"object_id":"CHEBI:45931","object_label":"thiamine(1+) diphosphate(1-)","other":"2-{3-[(4-amino-2-methylpyrimidin-5-yl)methyl]-4-methyl-1,3-thiazol-3-ium-5-yl}ethyl dihydrogen diphosphate&#124;CAS:136-09-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Thiamin_Pyrophosphate","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-747bc7904213e78b | docs/data/mapped_ingredients.csv; CSV lines=[1954] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:45931","line":1954,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:45931","preferred_term":"Thiamin pyrophosphate","total_occurrences":"2"}] |
| ev-bf700e968266d8b1 | reports/yaml_record_review/Thiamin_Pyrophosphate.md; &#96;data/ingredients/mapped/Thiamin_Pyrophosphate.yaml&#96;:2; Verdict:4; Identity:11; Validation:23; Evidence:36; Completeness:51; Recommended Edits:62 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-3c143d3a986966db | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1280,1650] | context_only | [{"current_record_sha256":"db23730b8e0c69f8f3711697b971f39a2203f5105ba91610992f925df8bc07bf","finding_id":"SEM:33f76305788497ff7ce0","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"db23730b8e0c69f8f3711697b971f39a2203f5105ba91610992f925df8bc07bf","finding_id":"SEM:abca2d130dfc5bb9e1cf","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-1ee8f8829d7f50b5 | data/ingredients/mapped/Thiamin_Pyrophosphate.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1952],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:45931","line":1954,"mapping_status":"MAPPED","ontology_id":"CHEBI:45931","preferred_term":"Thiamin pyrophosphate"}],"identifier":"CHEBI:45931","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:45931","ontology_label":"thiamine(1+) diphosphate(1-)","ontology_source":"CHEBI"},"preferred_term":"Thiamin pyrophosphate","sssom_rows":[{"data_row":2761,"object_id":"CHEBI:45931","object_label":"thiamine(1+) diphosphate(1-)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Thiamin_Pyrophosphate","synonym_count":1} |
| ev-9b53ba2403d554d4 | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml; findings[finding_id=f-7aa96d9cdc46e89b] | context_only | Predecessor structured review finding f-7aa96d9cdc46e89b in 20261011T024638Z-mim-reconcile-all-batch-11 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-thiamin-pyrophosphate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Thiamin_Pyrophosphate (data/ingredients/mapped/Thiamin_Pyrophosphate.yaml)'
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
summary: Per-record structured review for Thiamin_Pyrophosphate (data/ingredients/mapped/Thiamin_Pyrophosphate.yaml,
  record-dff17523de241273, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Thiamin_Pyrophosphate.yaml
    sha256: db23730b8e0c69f8f3711697b971f39a2203f5105ba91610992f925df8bc07bf
    role: target
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
    sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
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
  - path: reports/yaml_record_review/Thiamin_Pyrophosphate.md
    sha256: e08e2758c5c2205d705108d83c9901faadfbaa7c2e52c50676775b11e62d5179
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-dff17523de241273
  path: data/ingredients/mapped/Thiamin_Pyrophosphate.yaml
  label: Thiamin_Pyrophosphate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Thiamin_Pyrophosphate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Thiamin_Pyrophosphate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Thiamin_Pyrophosphate.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-dff17523de241273
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-dff17523de241273
  evidence_ids:
  - ev-168708c633faf5b1
  - ev-02c37d5ca95a62cd
  - ev-f71f78c3fb347a5a
  - ev-747bc7904213e78b
  - ev-1ee8f8829d7f50b5
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-dff17523de241273
  evidence_ids:
  - ev-168708c633faf5b1
  - ev-3c143d3a986966db
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-dff17523de241273
  evidence_ids:
  - ev-bf700e968266d8b1
  - ev-3c143d3a986966db
  - ev-9b53ba2403d554d4
evidence:
- evidence_id: ev-168708c633faf5b1
  kind: record_content
  reference: data/ingredients/mapped/Thiamin_Pyrophosphate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1952],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:45931","line":1954,"mapping_status":"MAPPED","ontology_id":"CHEBI:45931","preferred_term":"Thiamin
    pyrophosphate"}],"identifier":"CHEBI:45931","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:45931","ontology_label":"thiamine(1+)
    diphosphate(1-)","ontology_source":"CHEBI"},"preferred_term":"Thiamin pyrophosphate","sssom_rows":[{"data_row":2761,"object_id":"CHEBI:45931","object_label":"thiamine(1+)
    diphosphate(1-)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Thiamin_Pyrophosphate","synonym_count":1}'
  snapshot_sha256: db23730b8e0c69f8f3711697b971f39a2203f5105ba91610992f925df8bc07bf
- evidence_id: ev-02c37d5ca95a62cd
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1952]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-f71f78c3fb347a5a
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Thiamin_Pyrophosphate; data-row positions=[2761]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2761,"object_id":"CHEBI:45931","object_label":"thiamine(1+)
    diphosphate(1-)","other":"2-{3-[(4-amino-2-methylpyrimidin-5-yl)methyl]-4-methyl-1,3-thiazol-3-ium-5-yl}ethyl
    dihydrogen diphosphate|CAS:136-09-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Thiamin_Pyrophosphate","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-747bc7904213e78b
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1954]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:45931","line":1954,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:45931","preferred_term":"Thiamin
    pyrophosphate","total_occurrences":"2"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-bf700e968266d8b1
  kind: prior_review
  reference: reports/yaml_record_review/Thiamin_Pyrophosphate.md
  locator: '`data/ingredients/mapped/Thiamin_Pyrophosphate.yaml`:2; Verdict:4; Identity:11;
    Validation:23; Evidence:36; Completeness:51; Recommended Edits:62'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: e08e2758c5c2205d705108d83c9901faadfbaa7c2e52c50676775b11e62d5179
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Thiamin_Pyrophosphate.yaml`,\
    \ either verify\n  `VITAMIN_SOURCE` against an inspected database or literature\
    \ source and\n  replace the provisional `COMPUTATIONAL_PREDICTION`, or remove\
    \ the role. Then\n  rerun strict validation, term validation, SSSOM publication,\
    \ and\n  `scripts/validate_sssom_invariants.py`."
- evidence_id: ev-3c143d3a986966db
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1280,1650]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"db23730b8e0c69f8f3711697b971f39a2203f5105ba91610992f925df8bc07bf","finding_id":"SEM:33f76305788497ff7ce0","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"db23730b8e0c69f8f3711697b971f39a2203f5105ba91610992f925df8bc07bf","finding_id":"SEM:abca2d130dfc5bb9e1cf","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-1ee8f8829d7f50b5
  kind: record_content
  reference: data/ingredients/mapped/Thiamin_Pyrophosphate.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1952],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:45931","line":1954,"mapping_status":"MAPPED","ontology_id":"CHEBI:45931","preferred_term":"Thiamin
    pyrophosphate"}],"identifier":"CHEBI:45931","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:45931","ontology_label":"thiamine(1+)
    diphosphate(1-)","ontology_source":"CHEBI"},"preferred_term":"Thiamin pyrophosphate","sssom_rows":[{"data_row":2761,"object_id":"CHEBI:45931","object_label":"thiamine(1+)
    diphosphate(1-)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Thiamin_Pyrophosphate","synonym_count":1}'
  snapshot_sha256: db23730b8e0c69f8f3711697b971f39a2203f5105ba91610992f925df8bc07bf
- evidence_id: ev-9b53ba2403d554d4
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
  locator: findings[finding_id=f-7aa96d9cdc46e89b]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-7aa96d9cdc46e89b in 20261011T024638Z-mim-reconcile-all-batch-11
  snapshot_sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
assessments:
- assessment_id: a-4ee0d9556478875d
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-dff17523de241273
  evidence_ids:
  - ev-168708c633faf5b1
  - ev-02c37d5ca95a62cd
  - ev-f71f78c3fb347a5a
  - ev-747bc7904213e78b
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-11c17a3c4ef229ac
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-dff17523de241273
  evidence_ids:
  - ev-bf700e968266d8b1
  - ev-168708c633faf5b1
  - ev-3c143d3a986966db
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T18:32:01Z;
    reviewed SHA-256=db23730b8e0c69f8f3711697b971f39a2203f5105ba91610992f925df8bc07bf;
    current SHA-256=db23730b8e0c69f8f3711697b971f39a2203f5105ba91610992f925df8bc07bf;
    hash_changed=False. Reports=["reports/yaml_record_review/Thiamin_Pyrophosphate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The synonym
    match to CHEBI:45931, CAS RN, structure fields, aggregate row, and final SSSOM
    row pass, but VITAMIN_SOURCE is still provisional ChEBI-ancestry evidence.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-bf700e968266d8b1
    - ev-168708c633faf5b1
  - name: legacy-native-ids
    value: '["SEM:33f76305788497ff7ce0","SEM:abca2d130dfc5bb9e1cf"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-168708c633faf5b1
    - ev-bf700e968266d8b1
    - ev-3c143d3a986966db
- assessment_id: a-1ee8f8829d7f50b5
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-dff17523de241273
  evidence_ids:
  - ev-bf700e968266d8b1
  - ev-1ee8f8829d7f50b5
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-bf700e968266d8b1
    - ev-1ee8f8829d7f50b5
findings:
- finding_id: rec-f-7aa96d9cdc46e89b
  issue_key: mim-reconciliation-role-support-dff17523de241273
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Thiamin pyrophosphate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-dff17523de241273
  evidence_ids:
  - ev-bf700e968266d8b1
  - ev-1ee8f8829d7f50b5
  - ev-9b53ba2403d554d4
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Thiamin_Pyrophosphate.yaml
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
    finding_id: f-7aa96d9cdc46e89b
actions:
- action_id: rec-action-7aa96d9cdc46e89b
  description: 'Reassess prediction-only role support: Thiamin pyrophosphate'
  finding_ids:
  - rec-f-7aa96d9cdc46e89b
  target_ids:
  - record-dff17523de241273
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Thiamin_Pyrophosphate.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.
```
