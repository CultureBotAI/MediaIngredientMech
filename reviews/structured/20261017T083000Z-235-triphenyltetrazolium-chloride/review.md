# Per-record structured review: 235-Triphenyltetrazolium_Chloride (data/ingredients/mapped/235-Triphenyltetrazolium_Chloride.yaml)

- Review: 20261017T083000Z-235-triphenyltetrazolium-chloride
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 235-Triphenyltetrazolium_Chloride (data/ingredients/mapped/235-Triphenyltetrazolium_Chloride.yaml, record-87bec2cf1d99aef4, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/235-Triphenyltetrazolium_Chloride.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/235-Triphenyltetrazolium_Chloride.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-87bec2cf1d99aef4 | data/ingredients/mapped/235-Triphenyltetrazolium_Chloride.yaml | maintained | 235-Triphenyltetrazolium_Chloride |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-87bec2cf1d99aef4 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-87bec2cf1d99aef4 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-87bec2cf1d99aef4 | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-87bec2cf1d99aef4.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-87bec2cf1d99aef4.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T05:50:46Z; reviewed SHA-256=e2e49590efc40f1fc35fac9bac181d270ac48fc91c3dc3bdebde72904eebc7ae; current SHA-256=e2e49590efc40f1fc35fac9bac181d270ac48fc91c3dc3bdebde72904eebc7ae; hash_changed=False. Reports=["reports/yaml_record_review/235-Triphenyltetrazolium_Chloride.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Active CHEBI identity, chemistry, CultureBotHT occurrence count, SSSOM, and aggregate pass, but REDOX_INDICATOR is only supported by in-session LLM evidence.

### Historical provisional-role concern

evidence: concern. Targets: record-87bec2cf1d99aef4.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-f40810bb6fc4abbf: Reassess prediction-only role support: 2,3,5-Triphenyltetrazolium chloride

major / open / confirmed; issue key: mim-reconciliation-role-support-87bec2cf1d99aef4.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-f40810bb6fc4abbf

Reassess prediction-only role support: 2,3,5-Triphenyltetrazolium chloride

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-c1a9079d2e89a16b | data/ingredients/mapped/235-Triphenyltetrazolium_Chloride.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[339],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:78019","line":341,"mapping_status":"MAPPED","ontology_id":"CHEBI:78019","preferred_term":"2,3,5-Triphenyltetrazolium chloride"}],"identifier":"CHEBI:78019","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":10,"total_occurrences":10},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:78019","ontology_label":"2,3,5-triphenyltetrazolium chloride","ontology_source":"CHEBI"},"preferred_term":"2,3,5-Triphenyltetrazolium chloride","sssom_rows":[{"data_row":109,"object_id":"CHEBI:78019","object_label":"2,3,5-triphenyltetrazolium chloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:235-Triphenyltetrazolium_Chloride","synonym_count":2} |
| ev-875b322674443561 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [339] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-de6f1aa7e62d3d26 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:235-Triphenyltetrazolium_Chloride; data-row positions=[109] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":109,"object_id":"CHEBI:78019","object_label":"2,3,5-triphenyltetrazolium chloride","other":"2,3,5-triphenyl-2H-tetrazol-3-ium chloride&#124;Triphenyltetrazolium Chloride&#124;CAS:298-96-4","predicate_id":"skos:exactMatch","subject_id":"MIM:235-Triphenyltetrazolium_Chloride","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-506024e33578d6d3 | docs/data/mapped_ingredients.csv; CSV lines=[341] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:78019","line":341,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"10","ontology_id":"CHEBI:78019","preferred_term":"2,3,5-Triphenyltetrazolium chloride","total_occurrences":"10"}] |
| ev-408ed2bf548e971e | reports/yaml_record_review/235-Triphenyltetrazolium_Chloride.md; &#96;data/ingredients/mapped/235-Triphenyltetrazolium_Chloride.yaml&#96;:2; Verdict:4; Identity:11; Validation:27; Evidence:42; Completeness:58; Recommended Edits:65 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-0d1c40cfcf43b47a | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[90,1659] | context_only | [{"current_record_sha256":"e2e49590efc40f1fc35fac9bac181d270ac48fc91c3dc3bdebde72904eebc7ae","finding_id":"SEM:92563e5cef0f5eee4fbd","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"e2e49590efc40f1fc35fac9bac181d270ac48fc91c3dc3bdebde72904eebc7ae","finding_id":"SEM:aecd8439a79a08e7ba68","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-7f1000c284caa799 | data/ingredients/mapped/235-Triphenyltetrazolium_Chloride.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[339],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:78019","line":341,"mapping_status":"MAPPED","ontology_id":"CHEBI:78019","preferred_term":"2,3,5-Triphenyltetrazolium chloride"}],"identifier":"CHEBI:78019","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":10,"total_occurrences":10},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:78019","ontology_label":"2,3,5-triphenyltetrazolium chloride","ontology_source":"CHEBI"},"preferred_term":"2,3,5-Triphenyltetrazolium chloride","sssom_rows":[{"data_row":109,"object_id":"CHEBI:78019","object_label":"2,3,5-triphenyltetrazolium chloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:235-Triphenyltetrazolium_Chloride","synonym_count":2} |
| ev-c66808753c3600ed | reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml; findings[finding_id=f-f40810bb6fc4abbf] | context_only | Predecessor structured review finding f-f40810bb6fc4abbf in 20261011T024630Z-mim-reconcile-all-batch-02 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-235-triphenyltetrazolium-chloride
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 235-Triphenyltetrazolium_Chloride (data/ingredients/mapped/235-Triphenyltetrazolium_Chloride.yaml)'
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
summary: Per-record structured review for 235-Triphenyltetrazolium_Chloride (data/ingredients/mapped/235-Triphenyltetrazolium_Chloride.yaml,
  record-87bec2cf1d99aef4, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/235-Triphenyltetrazolium_Chloride.yaml
    sha256: e2e49590efc40f1fc35fac9bac181d270ac48fc91c3dc3bdebde72904eebc7ae
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
  - path: reports/yaml_record_review/235-Triphenyltetrazolium_Chloride.md
    sha256: 97a8a8f5a62339a99ea990a6424d36afe2a3d66fbc769b340d2ee2792a8598f3
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-87bec2cf1d99aef4
  path: data/ingredients/mapped/235-Triphenyltetrazolium_Chloride.yaml
  label: 235-Triphenyltetrazolium_Chloride
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/235-Triphenyltetrazolium_Chloride.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/235-Triphenyltetrazolium_Chloride.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/235-Triphenyltetrazolium_Chloride.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-87bec2cf1d99aef4
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-87bec2cf1d99aef4
  evidence_ids:
  - ev-c1a9079d2e89a16b
  - ev-875b322674443561
  - ev-de6f1aa7e62d3d26
  - ev-506024e33578d6d3
  - ev-7f1000c284caa799
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-87bec2cf1d99aef4
  evidence_ids:
  - ev-c1a9079d2e89a16b
  - ev-0d1c40cfcf43b47a
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-87bec2cf1d99aef4
  evidence_ids:
  - ev-408ed2bf548e971e
  - ev-0d1c40cfcf43b47a
  - ev-c66808753c3600ed
evidence:
- evidence_id: ev-c1a9079d2e89a16b
  kind: record_content
  reference: data/ingredients/mapped/235-Triphenyltetrazolium_Chloride.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[339],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:78019","line":341,"mapping_status":"MAPPED","ontology_id":"CHEBI:78019","preferred_term":"2,3,5-Triphenyltetrazolium
    chloride"}],"identifier":"CHEBI:78019","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":10,"total_occurrences":10},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:78019","ontology_label":"2,3,5-triphenyltetrazolium
    chloride","ontology_source":"CHEBI"},"preferred_term":"2,3,5-Triphenyltetrazolium
    chloride","sssom_rows":[{"data_row":109,"object_id":"CHEBI:78019","object_label":"2,3,5-triphenyltetrazolium
    chloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:235-Triphenyltetrazolium_Chloride","synonym_count":2}'
  snapshot_sha256: e2e49590efc40f1fc35fac9bac181d270ac48fc91c3dc3bdebde72904eebc7ae
- evidence_id: ev-875b322674443561
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [339]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-de6f1aa7e62d3d26
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:235-Triphenyltetrazolium_Chloride; data-row positions=[109]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":109,"object_id":"CHEBI:78019","object_label":"2,3,5-triphenyltetrazolium
    chloride","other":"2,3,5-triphenyl-2H-tetrazol-3-ium chloride|Triphenyltetrazolium
    Chloride|CAS:298-96-4","predicate_id":"skos:exactMatch","subject_id":"MIM:235-Triphenyltetrazolium_Chloride","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-506024e33578d6d3
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[341]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:78019","line":341,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"10","ontology_id":"CHEBI:78019","preferred_term":"2,3,5-Triphenyltetrazolium
    chloride","total_occurrences":"10"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-408ed2bf548e971e
  kind: prior_review
  reference: reports/yaml_record_review/235-Triphenyltetrazolium_Chloride.md
  locator: '`data/ingredients/mapped/235-Triphenyltetrazolium_Chloride.yaml`:2; Verdict:4;
    Identity:11; Validation:27; Evidence:42; Completeness:58; Recommended Edits:65'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 97a8a8f5a62339a99ea990a6424d36afe2a3d66fbc769b340d2ee2792a8598f3
  quote: "Recommended Edits:\n1. Either remove `REDOX_INDICATOR` or replace it with\
    \ inspected\n   formulation-specific evidence that directly supports this exact\
    \ ingredient\n   as a redox indicator.\n2. Regenerate `data/curated/mapped_ingredients.yaml`,\n\
    \   `mappings/ingredient_mappings.sssom.tsv`, and docs from the maintained YAML.\n\
    3. Re-run the focused strict/LinkML validators, role/evidence checks,\n   `just\
    \ qc-sssom`, and `just qc-flat-coverage` after those edits."
- evidence_id: ev-0d1c40cfcf43b47a
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[90,1659]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"e2e49590efc40f1fc35fac9bac181d270ac48fc91c3dc3bdebde72904eebc7ae","finding_id":"SEM:92563e5cef0f5eee4fbd","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"e2e49590efc40f1fc35fac9bac181d270ac48fc91c3dc3bdebde72904eebc7ae","finding_id":"SEM:aecd8439a79a08e7ba68","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-7f1000c284caa799
  kind: record_content
  reference: data/ingredients/mapped/235-Triphenyltetrazolium_Chloride.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[339],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:78019","line":341,"mapping_status":"MAPPED","ontology_id":"CHEBI:78019","preferred_term":"2,3,5-Triphenyltetrazolium
    chloride"}],"identifier":"CHEBI:78019","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":10,"total_occurrences":10},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:78019","ontology_label":"2,3,5-triphenyltetrazolium
    chloride","ontology_source":"CHEBI"},"preferred_term":"2,3,5-Triphenyltetrazolium
    chloride","sssom_rows":[{"data_row":109,"object_id":"CHEBI:78019","object_label":"2,3,5-triphenyltetrazolium
    chloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:235-Triphenyltetrazolium_Chloride","synonym_count":2}'
  snapshot_sha256: e2e49590efc40f1fc35fac9bac181d270ac48fc91c3dc3bdebde72904eebc7ae
- evidence_id: ev-c66808753c3600ed
  kind: prior_review
  reference: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
  locator: findings[finding_id=f-f40810bb6fc4abbf]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-f40810bb6fc4abbf in 20261011T024630Z-mim-reconcile-all-batch-02
  snapshot_sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
assessments:
- assessment_id: a-6f62877b7975acd0
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-87bec2cf1d99aef4
  evidence_ids:
  - ev-c1a9079d2e89a16b
  - ev-875b322674443561
  - ev-de6f1aa7e62d3d26
  - ev-506024e33578d6d3
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-2bf4628a00fee61d
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-87bec2cf1d99aef4
  evidence_ids:
  - ev-408ed2bf548e971e
  - ev-c1a9079d2e89a16b
  - ev-0d1c40cfcf43b47a
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T05:50:46Z;
    reviewed SHA-256=e2e49590efc40f1fc35fac9bac181d270ac48fc91c3dc3bdebde72904eebc7ae;
    current SHA-256=e2e49590efc40f1fc35fac9bac181d270ac48fc91c3dc3bdebde72904eebc7ae;
    hash_changed=False. Reports=["reports/yaml_record_review/235-Triphenyltetrazolium_Chloride.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Active CHEBI
    identity, chemistry, CultureBotHT occurrence count, SSSOM, and aggregate pass,
    but REDOX_INDICATOR is only supported by in-session LLM evidence.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-408ed2bf548e971e
    - ev-c1a9079d2e89a16b
  - name: legacy-native-ids
    value: '["SEM:92563e5cef0f5eee4fbd","SEM:aecd8439a79a08e7ba68"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-c1a9079d2e89a16b
    - ev-408ed2bf548e971e
    - ev-0d1c40cfcf43b47a
- assessment_id: a-7f1000c284caa799
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-87bec2cf1d99aef4
  evidence_ids:
  - ev-408ed2bf548e971e
  - ev-7f1000c284caa799
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-408ed2bf548e971e
    - ev-7f1000c284caa799
findings:
- finding_id: rec-f-f40810bb6fc4abbf
  issue_key: mim-reconciliation-role-support-87bec2cf1d99aef4
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: 2,3,5-Triphenyltetrazolium chloride'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-87bec2cf1d99aef4
  evidence_ids:
  - ev-408ed2bf548e971e
  - ev-7f1000c284caa799
  - ev-c66808753c3600ed
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/235-Triphenyltetrazolium_Chloride.yaml
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
    review_id: 20261011T024630Z-mim-reconcile-all-batch-02
    finding_id: f-f40810bb6fc4abbf
actions:
- action_id: rec-action-f40810bb6fc4abbf
  description: 'Reassess prediction-only role support: 2,3,5-Triphenyltetrazolium
    chloride'
  finding_ids:
  - rec-f-f40810bb6fc4abbf
  target_ids:
  - record-87bec2cf1d99aef4
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/235-Triphenyltetrazolium_Chloride.yaml
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
