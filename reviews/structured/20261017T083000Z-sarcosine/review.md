# Per-record structured review: Sarcosine (data/ingredients/mapped/Sarcosine.yaml)

- Review: 20261017T083000Z-sarcosine
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Sarcosine (data/ingredients/mapped/Sarcosine.yaml, record-be4455dad7eee11c, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Sarcosine.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Sarcosine.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-be4455dad7eee11c | data/ingredients/mapped/Sarcosine.yaml | maintained | Sarcosine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-be4455dad7eee11c | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-be4455dad7eee11c | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-be4455dad7eee11c | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-be4455dad7eee11c.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-be4455dad7eee11c.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T13:26:45Z; reviewed SHA-256=1039cd8624ebbce704d2524c09230043ecc9aac1ed02e757b1451f88d08aa72f; current SHA-256=1039cd8624ebbce704d2524c09230043ecc9aac1ed02e757b1451f88d08aa72f; hash_changed=False. Reports=["reports/yaml_record_review/Sarcosine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:15611 identity, structure, CAS, and final SSSOM row pass, but AMINO_ACID_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-be4455dad7eee11c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-d8405687a3ed4fc1: Reassess prediction-only role support: sarcosine

major / open / confirmed; issue key: mim-reconciliation-role-support-be4455dad7eee11c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-d8405687a3ed4fc1

Reassess prediction-only role support: sarcosine

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-9b4b6e996905bed7 | data/ingredients/mapped/Sarcosine.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1780],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15611","line":1782,"mapping_status":"MAPPED","ontology_id":"CHEBI:15611","preferred_term":"sarcosine"}],"identifier":"CHEBI:15611","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15611","ontology_label":"sarcosine","ontology_source":"CHEBI"},"preferred_term":"sarcosine","sssom_rows":[{"data_row":2483,"object_id":"CHEBI:15611","object_label":"sarcosine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sarcosine","synonym_count":0} |
| ev-dd39f5b9a533ccf2 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1780] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-d9bfe6f924515bd1 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Sarcosine; data-row positions=[2483] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2483,"object_id":"CHEBI:15611","object_label":"sarcosine","other":"CAS:107-97-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Sarcosine","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-ddfa18c8c9061b72 | docs/data/mapped_ingredients.csv; CSV lines=[1782] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:15611","line":1782,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:15611","preferred_term":"sarcosine","total_occurrences":"0"}] |
| ev-ad40a538b670997f | reports/yaml_record_review/Sarcosine.md; &#96;data/ingredients/mapped/Sarcosine.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-024e4039aeb554ff | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1185,2078] | context_only | [{"current_record_sha256":"1039cd8624ebbce704d2524c09230043ecc9aac1ed02e757b1451f88d08aa72f","finding_id":"SEM:7982fda79c40e6055abc","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"1039cd8624ebbce704d2524c09230043ecc9aac1ed02e757b1451f88d08aa72f","finding_id":"SEM:044e54b64764882ad768","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-f6876d4314324e02 | data/ingredients/mapped/Sarcosine.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1780],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15611","line":1782,"mapping_status":"MAPPED","ontology_id":"CHEBI:15611","preferred_term":"sarcosine"}],"identifier":"CHEBI:15611","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15611","ontology_label":"sarcosine","ontology_source":"CHEBI"},"preferred_term":"sarcosine","sssom_rows":[{"data_row":2483,"object_id":"CHEBI:15611","object_label":"sarcosine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sarcosine","synonym_count":0} |
| ev-c56775d71fc12b36 | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml; findings[finding_id=f-d8405687a3ed4fc1] | context_only | Predecessor structured review finding f-d8405687a3ed4fc1 in 20261011T024638Z-mim-reconcile-all-batch-10 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-sarcosine
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Sarcosine (data/ingredients/mapped/Sarcosine.yaml)'
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
summary: Per-record structured review for Sarcosine (data/ingredients/mapped/Sarcosine.yaml,
  record-be4455dad7eee11c, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Sarcosine.yaml
    sha256: 1039cd8624ebbce704d2524c09230043ecc9aac1ed02e757b1451f88d08aa72f
    role: target
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
    sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
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
  - path: reports/yaml_record_review/Sarcosine.md
    sha256: a3bd34ae980f54a0ed4882f5566e8a89520c41942a433ce436d931b07ad09e26
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-be4455dad7eee11c
  path: data/ingredients/mapped/Sarcosine.yaml
  label: Sarcosine
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sarcosine.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Sarcosine.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Sarcosine.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-be4455dad7eee11c
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-be4455dad7eee11c
  evidence_ids:
  - ev-9b4b6e996905bed7
  - ev-dd39f5b9a533ccf2
  - ev-d9bfe6f924515bd1
  - ev-ddfa18c8c9061b72
  - ev-f6876d4314324e02
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-be4455dad7eee11c
  evidence_ids:
  - ev-9b4b6e996905bed7
  - ev-024e4039aeb554ff
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10
    and semantic review dispositions on HEAD.
  target_ids:
  - record-be4455dad7eee11c
  evidence_ids:
  - ev-ad40a538b670997f
  - ev-024e4039aeb554ff
  - ev-c56775d71fc12b36
evidence:
- evidence_id: ev-9b4b6e996905bed7
  kind: record_content
  reference: data/ingredients/mapped/Sarcosine.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1780],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15611","line":1782,"mapping_status":"MAPPED","ontology_id":"CHEBI:15611","preferred_term":"sarcosine"}],"identifier":"CHEBI:15611","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15611","ontology_label":"sarcosine","ontology_source":"CHEBI"},"preferred_term":"sarcosine","sssom_rows":[{"data_row":2483,"object_id":"CHEBI:15611","object_label":"sarcosine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sarcosine","synonym_count":0}'
  snapshot_sha256: 1039cd8624ebbce704d2524c09230043ecc9aac1ed02e757b1451f88d08aa72f
- evidence_id: ev-dd39f5b9a533ccf2
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1780]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-d9bfe6f924515bd1
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Sarcosine; data-row positions=[2483]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2483,"object_id":"CHEBI:15611","object_label":"sarcosine","other":"CAS:107-97-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Sarcosine","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-ddfa18c8c9061b72
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1782]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:15611","line":1782,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:15611","preferred_term":"sarcosine","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-ad40a538b670997f
  kind: prior_review
  reference: reports/yaml_record_review/Sarcosine.md
  locator: '`data/ingredients/mapped/Sarcosine.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: a3bd34ae980f54a0ed4882f5566e8a89520c41942a433ce436d931b07ad09e26
- evidence_id: ev-024e4039aeb554ff
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1185,2078]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"1039cd8624ebbce704d2524c09230043ecc9aac1ed02e757b1451f88d08aa72f","finding_id":"SEM:7982fda79c40e6055abc","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"1039cd8624ebbce704d2524c09230043ecc9aac1ed02e757b1451f88d08aa72f","finding_id":"SEM:044e54b64764882ad768","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-f6876d4314324e02
  kind: record_content
  reference: data/ingredients/mapped/Sarcosine.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1780],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15611","line":1782,"mapping_status":"MAPPED","ontology_id":"CHEBI:15611","preferred_term":"sarcosine"}],"identifier":"CHEBI:15611","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15611","ontology_label":"sarcosine","ontology_source":"CHEBI"},"preferred_term":"sarcosine","sssom_rows":[{"data_row":2483,"object_id":"CHEBI:15611","object_label":"sarcosine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sarcosine","synonym_count":0}'
  snapshot_sha256: 1039cd8624ebbce704d2524c09230043ecc9aac1ed02e757b1451f88d08aa72f
- evidence_id: ev-c56775d71fc12b36
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
  locator: findings[finding_id=f-d8405687a3ed4fc1]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-d8405687a3ed4fc1 in 20261011T024638Z-mim-reconcile-all-batch-10
  snapshot_sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
assessments:
- assessment_id: a-84e82723a3920fe7
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-be4455dad7eee11c
  evidence_ids:
  - ev-9b4b6e996905bed7
  - ev-dd39f5b9a533ccf2
  - ev-d9bfe6f924515bd1
  - ev-ddfa18c8c9061b72
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-040085ccfe2bbdd3
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-be4455dad7eee11c
  evidence_ids:
  - ev-ad40a538b670997f
  - ev-9b4b6e996905bed7
  - ev-024e4039aeb554ff
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T13:26:45Z;
    reviewed SHA-256=1039cd8624ebbce704d2524c09230043ecc9aac1ed02e757b1451f88d08aa72f;
    current SHA-256=1039cd8624ebbce704d2524c09230043ecc9aac1ed02e757b1451f88d08aa72f;
    hash_changed=False. Reports=["reports/yaml_record_review/Sarcosine.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI:15611
    identity, structure, CAS, and final SSSOM row pass, but AMINO_ACID_SOURCE is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ad40a538b670997f
    - ev-9b4b6e996905bed7
  - name: legacy-native-ids
    value: '["SEM:7982fda79c40e6055abc","SEM:044e54b64764882ad768"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-9b4b6e996905bed7
    - ev-ad40a538b670997f
    - ev-024e4039aeb554ff
- assessment_id: a-f6876d4314324e02
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-be4455dad7eee11c
  evidence_ids:
  - ev-ad40a538b670997f
  - ev-f6876d4314324e02
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ad40a538b670997f
    - ev-f6876d4314324e02
findings:
- finding_id: rec-f-d8405687a3ed4fc1
  issue_key: mim-reconciliation-role-support-be4455dad7eee11c
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: sarcosine'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-be4455dad7eee11c
  evidence_ids:
  - ev-ad40a538b670997f
  - ev-f6876d4314324e02
  - ev-c56775d71fc12b36
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sarcosine.yaml
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
    review_id: 20261011T024638Z-mim-reconcile-all-batch-10
    finding_id: f-d8405687a3ed4fc1
actions:
- action_id: rec-action-d8405687a3ed4fc1
  description: 'Reassess prediction-only role support: sarcosine'
  finding_ids:
  - rec-f-d8405687a3ed4fc1
  target_ids:
  - record-be4455dad7eee11c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sarcosine.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.
```
