# Per-record structured review: 2-dichloroethane (data/ingredients/mapped/2-dichloroethane.yaml)

- Review: 20261017T083000Z-2-dichloroethane
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 2-dichloroethane (data/ingredients/mapped/2-dichloroethane.yaml, record-995fde797ec152ab, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/2-dichloroethane.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/2-dichloroethane.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-995fde797ec152ab | data/ingredients/mapped/2-dichloroethane.yaml | maintained | 2-dichloroethane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-995fde797ec152ab | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-995fde797ec152ab | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-995fde797ec152ab | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-995fde797ec152ab.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-995fde797ec152ab.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T05:39:46Z; reviewed SHA-256=91b5fec5e528b107b7a9292f5593dc7c59e537eedc0f831e2b7c1d84e6acc281; current SHA-256=91b5fec5e528b107b7a9292f5593dc7c59e537eedc0f831e2b7c1d84e6acc281; hash_changed=False. Reports=["reports/yaml_record_review/2-dichloroethane.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Active CHEBI identity, dropped-locant repair, chemistry, SSSOM, and aggregate pass, but top-level notes still describe the pre-promotion unmapped state.

### Non-monotonic curation-history timestamps

provenance: concern. Targets: record-995fde797ec152ab.

The reported timestamp-order problem is still observable in these adjacent append-order events: [{"earlier_event":{"action":"CREATED_AS_UNMAPPED","changes":"Imported from microbedecoder (source_id=kgmicrobe.trait:2_dichloroethane); no CAS-RN or CHEBI/NCIT match. Curator review needed.","curator":"audit_import_ingredients[microbedecoder]","llm_assisted":false,"new_status":"UNMAPPED","timestamp":"2026-08-04T02:54:09.684805+00:00"},"earlier_index":0,"later_event":{"action":"PROMOTED_TO_MAPPED","changes":"Promoted UNMAPPED_0722 -&gt; CHEBI:27789 \"1,2-dichloroethane\" (EXACT_MATCH); mapping_status UNMAPPED -&gt; MAPPED, SSSOM row added.","curator":"promote_resolved_unmapped","llm_assisted":false,"new_status":"MAPPED","previous_status":"UNMAPPED","timestamp":"2026-08-04T00:00:00+00:00"},"later_index":1}]. Preserve append-only history; add an explanatory correction instead of inventing precise historical times.

## Findings

### rec-f-ed7078c6b49d144b: Explain curation-history timestamp order: 1,2-dichloroethane

minor / open / confirmed; issue key: mim-reconciliation-history-order-995fde797ec152ab.

The reported timestamp-order problem is still observable in these adjacent append-order events: [{"earlier_event":{"action":"CREATED_AS_UNMAPPED","changes":"Imported from microbedecoder (source_id=kgmicrobe.trait:2_dichloroethane); no CAS-RN or CHEBI/NCIT match. Curator review needed.","curator":"audit_import_ingredients[microbedecoder]","llm_assisted":false,"new_status":"UNMAPPED","timestamp":"2026-08-04T02:54:09.684805+00:00"},"earlier_index":0,"later_event":{"action":"PROMOTED_TO_MAPPED","changes":"Promoted UNMAPPED_0722 -&gt; CHEBI:27789 \"1,2-dichloroethane\" (EXACT_MATCH); mapping_status UNMAPPED -&gt; MAPPED, SSSOM row added.","curator":"promote_resolved_unmapped","llm_assisted":false,"new_status":"MAPPED","previous_status":"UNMAPPED","timestamp":"2026-08-04T00:00:00+00:00"},"later_index":1}]. Preserve append-only history; add an explanatory correction instead of inventing precise historical times.

## Recommended Actions And Acceptance Checks

### rec-action-ed7078c6b49d144b

Explain curation-history timestamp order: 1,2-dichloroethane

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-a478eb46f38155f8 | data/ingredients/mapped/2-dichloroethane.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[242],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:27789","line":244,"mapping_status":"MAPPED","ontology_id":"CHEBI:27789","preferred_term":"1,2-dichloroethane"}],"identifier":"CHEBI:27789","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":2,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:27789","ontology_label":"1,2-dichloroethane","ontology_source":"CHEBI"},"preferred_term":"1,2-dichloroethane","sssom_rows":[{"data_row":84,"object_id":"CHEBI:27789","object_label":"1,2-dichloroethane","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:2-dichloroethane","synonym_count":1} |
| ev-c46d493767d82e96 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [242] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-47c413b59cf16da3 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:2-dichloroethane; data-row positions=[84] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":84,"object_id":"CHEBI:27789","object_label":"1,2-dichloroethane","other":"2-dichloroethane","predicate_id":"skos:exactMatch","subject_id":"MIM:2-dichloroethane","validation_method":"manual:promote_resolved_unmapped&#124;PROMOTED&#124;2026-08-04"}] |
| ev-2c5ea2618ccf1e2f | docs/data/mapped_ingredients.csv; CSV lines=[244] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:27789","line":244,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:27789","preferred_term":"1,2-dichloroethane","total_occurrences":"0"}] |
| ev-0feffcc8ecbfd59a | reports/yaml_record_review/2-dichloroethane.md; &#96;data/ingredients/mapped/2-dichloroethane.yaml&#96;:2; Verdict:4; Identity:10; Validation:22; Evidence:35; Completeness:51; Recommended Edits:59 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-e573d9557475daeb | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[66] | context_only | [{"current_record_sha256":"91b5fec5e528b107b7a9292f5593dc7c59e537eedc0f831e2b7c1d84e6acc281","finding_id":"SEM:f27199ee678a0e83532d","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-2409de00468285d9 | reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml; findings[finding_id=f-ed7078c6b49d144b] | context_only | Predecessor structured review finding f-ed7078c6b49d144b in 20261011T024630Z-mim-reconcile-all-batch-02 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-2-dichloroethane
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 2-dichloroethane (data/ingredients/mapped/2-dichloroethane.yaml)'
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
summary: Per-record structured review for 2-dichloroethane (data/ingredients/mapped/2-dichloroethane.yaml,
  record-995fde797ec152ab, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/2-dichloroethane.yaml
    sha256: 91b5fec5e528b107b7a9292f5593dc7c59e537eedc0f831e2b7c1d84e6acc281
    role: target
  - path: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
    sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
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
  - path: reports/yaml_record_review/2-dichloroethane.md
    sha256: fdec5db31f8e0c0e59425a764daaa0df4581a625d08389aa75b37ae13142b24e
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-995fde797ec152ab
  path: data/ingredients/mapped/2-dichloroethane.yaml
  label: 2-dichloroethane
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/2-dichloroethane.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/2-dichloroethane.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/2-dichloroethane.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-995fde797ec152ab
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-995fde797ec152ab
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-995fde797ec152ab
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-995fde797ec152ab
evidence:
- evidence_id: ev-a478eb46f38155f8
  kind: record_content
  reference: data/ingredients/mapped/2-dichloroethane.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[242],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:27789","line":244,"mapping_status":"MAPPED","ontology_id":"CHEBI:27789","preferred_term":"1,2-dichloroethane"}],"identifier":"CHEBI:27789","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":2,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:27789","ontology_label":"1,2-dichloroethane","ontology_source":"CHEBI"},"preferred_term":"1,2-dichloroethane","sssom_rows":[{"data_row":84,"object_id":"CHEBI:27789","object_label":"1,2-dichloroethane","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:2-dichloroethane","synonym_count":1}'
  snapshot_sha256: 91b5fec5e528b107b7a9292f5593dc7c59e537eedc0f831e2b7c1d84e6acc281
- evidence_id: ev-c46d493767d82e96
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [242]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-47c413b59cf16da3
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:2-dichloroethane; data-row positions=[84]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":84,"object_id":"CHEBI:27789","object_label":"1,2-dichloroethane","other":"2-dichloroethane","predicate_id":"skos:exactMatch","subject_id":"MIM:2-dichloroethane","validation_method":"manual:promote_resolved_unmapped|PROMOTED|2026-08-04"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-2c5ea2618ccf1e2f
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[244]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:27789","line":244,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:27789","preferred_term":"1,2-dichloroethane","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-0feffcc8ecbfd59a
  kind: prior_review
  reference: reports/yaml_record_review/2-dichloroethane.md
  locator: '`data/ingredients/mapped/2-dichloroethane.yaml`:2; Verdict:4; Identity:10;
    Validation:22; Evidence:35; Completeness:51; Recommended Edits:59'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: fdec5db31f8e0c0e59425a764daaa0df4581a625d08389aa75b37ae13142b24e
  quote: "Recommended Edits:\n1. In `data/ingredients/mapped/2-dichloroethane.yaml`,\
    \ replace the stale `notes`\n   text with a concise statement that the microbedecoder\
    \ dropped-locant artifact\n   was resolved to `CHEBI:27789` and corrected to `1,2-dichloroethane`.\n\
    2. Run `just sync-curated`, `just validate-strict\n   data/ingredients/mapped/2-dichloroethane.yaml`,\
    \ `just validate-terms\n   data/ingredients/mapped/2-dichloroethane.yaml`, `just\
    \ qc-sssom`, and\n   `just qc-flat-coverage` after that curation edit."
- evidence_id: ev-e573d9557475daeb
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[66]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"91b5fec5e528b107b7a9292f5593dc7c59e537eedc0f831e2b7c1d84e6acc281","finding_id":"SEM:f27199ee678a0e83532d","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-2409de00468285d9
  kind: prior_review
  reference: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
  locator: findings[finding_id=f-ed7078c6b49d144b]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-ed7078c6b49d144b in 20261011T024630Z-mim-reconcile-all-batch-02
  snapshot_sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
assessments:
- assessment_id: a-8f35553159b9cbc5
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-995fde797ec152ab
  evidence_ids:
  - ev-a478eb46f38155f8
  - ev-c46d493767d82e96
  - ev-47c413b59cf16da3
  - ev-2c5ea2618ccf1e2f
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-39f0b9a85cb57fa6
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-995fde797ec152ab
  evidence_ids:
  - ev-0feffcc8ecbfd59a
  - ev-a478eb46f38155f8
  - ev-e573d9557475daeb
  details: 'Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T05:39:46Z;
    reviewed SHA-256=91b5fec5e528b107b7a9292f5593dc7c59e537eedc0f831e2b7c1d84e6acc281;
    current SHA-256=91b5fec5e528b107b7a9292f5593dc7c59e537eedc0f831e2b7c1d84e6acc281;
    hash_changed=False. Reports=["reports/yaml_record_review/2-dichloroethane.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Active CHEBI
    identity, dropped-locant repair, chemistry, SSSOM, and aggregate pass, but top-level
    notes still describe the pre-promotion unmapped state.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0feffcc8ecbfd59a
    - ev-a478eb46f38155f8
  - name: legacy-native-ids
    value: '["SEM:f27199ee678a0e83532d"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-a478eb46f38155f8
    - ev-0feffcc8ecbfd59a
    - ev-e573d9557475daeb
- assessment_id: a-6b83c8b66f747292
  area: provenance
  topic: Non-monotonic curation-history timestamps
  outcome: concern
  summary: 'The reported timestamp-order problem is still observable in these adjacent
    append-order events: [{"earlier_event":{"action":"CREATED_AS_UNMAPPED","changes":"Imported
    from microbedecoder (source_id=kgmicrobe.trait:2_dichloroethane); no CAS-RN or
    CHEBI/NCIT match. Curator review needed.","curator":"audit_import_ingredients[microbedecoder]","llm_assisted":false,"new_status":"UNMAPPED","timestamp":"2026-08-04T02:54:09.684805+00:00"},"earlier_index":0,"later_event":{"action":"PROMOTED_TO_MAPPED","changes":"Promoted
    UNMAPPED_0722 -> CHEBI:27789 \"1,2-dichloroethane\" (EXACT_MATCH); mapping_status
    UNMAPPED -> MAPPED, SSSOM row added.","curator":"promote_resolved_unmapped","llm_assisted":false,"new_status":"MAPPED","previous_status":"UNMAPPED","timestamp":"2026-08-04T00:00:00+00:00"},"later_index":1}].
    Preserve append-only history; add an explanatory correction instead of inventing
    precise historical times.'
  target_ids:
  - record-995fde797ec152ab
  evidence_ids:
  - ev-0feffcc8ecbfd59a
  - ev-a478eb46f38155f8
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0feffcc8ecbfd59a
    - ev-a478eb46f38155f8
findings:
- finding_id: rec-f-ed7078c6b49d144b
  issue_key: mim-reconciliation-history-order-995fde797ec152ab
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: 'Explain curation-history timestamp order: 1,2-dichloroethane'
  description: 'The reported timestamp-order problem is still observable in these
    adjacent append-order events: [{"earlier_event":{"action":"CREATED_AS_UNMAPPED","changes":"Imported
    from microbedecoder (source_id=kgmicrobe.trait:2_dichloroethane); no CAS-RN or
    CHEBI/NCIT match. Curator review needed.","curator":"audit_import_ingredients[microbedecoder]","llm_assisted":false,"new_status":"UNMAPPED","timestamp":"2026-08-04T02:54:09.684805+00:00"},"earlier_index":0,"later_event":{"action":"PROMOTED_TO_MAPPED","changes":"Promoted
    UNMAPPED_0722 -> CHEBI:27789 \"1,2-dichloroethane\" (EXACT_MATCH); mapping_status
    UNMAPPED -> MAPPED, SSSOM row added.","curator":"promote_resolved_unmapped","llm_assisted":false,"new_status":"MAPPED","previous_status":"UNMAPPED","timestamp":"2026-08-04T00:00:00+00:00"},"later_index":1}].
    Preserve append-only history; add an explanatory correction instead of inventing
    precise historical times.'
  target_ids:
  - record-995fde797ec152ab
  evidence_ids:
  - ev-0feffcc8ecbfd59a
  - ev-a478eb46f38155f8
  - ev-2409de00468285d9
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/2-dichloroethane.yaml
    role: maintained ingredient
  field_paths:
  - curation_history
  tags:
  - reconciliation
  - bundle-by-owner
  - history-order
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024630Z-mim-reconcile-all-batch-02
    finding_id: f-ed7078c6b49d144b
actions:
- action_id: rec-action-ed7078c6b49d144b
  description: 'Explain curation-history timestamp order: 1,2-dichloroethane'
  finding_ids:
  - rec-f-ed7078c6b49d144b
  target_ids:
  - record-995fde797ec152ab
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/2-dichloroethane.yaml
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
  with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.
```
