# Per-record structured review: Puromycin_Dihydrochloride (data/ingredients/mapped/Puromycin_Dihydrochloride.yaml)

- Review: 20261017T083000Z-puromycin-dihydrochloride
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Puromycin_Dihydrochloride (data/ingredients/mapped/Puromycin_Dihydrochloride.yaml, record-098adafbd6c7bac1, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Puromycin_Dihydrochloride.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Puromycin_Dihydrochloride.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-098adafbd6c7bac1 | data/ingredients/mapped/Puromycin_Dihydrochloride.yaml | maintained | Puromycin_Dihydrochloride |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-098adafbd6c7bac1 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-098adafbd6c7bac1 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-098adafbd6c7bac1 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-098adafbd6c7bac1.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-098adafbd6c7bac1.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T10:53:18Z; reviewed SHA-256=104d41ec9d80fd2213875e92c3c7136a804180289680e03b9d2a549fba8f1b57; current SHA-256=104d41ec9d80fd2213875e92c3c7136a804180289680e03b9d2a549fba8f1b57; hash_changed=False. Reports=["reports/yaml_record_review/Puromycin_Dihydrochloride.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:8642 identity and final synonyms pass, but SELECTIVE_AGENT is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-098adafbd6c7bac1.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-f7bfc8825db4764b: Reassess prediction-only role support: Puromycin dihydrochloride

major / open / confirmed; issue key: mim-reconciliation-role-support-098adafbd6c7bac1.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-f7bfc8825db4764b

Reassess prediction-only role support: Puromycin dihydrochloride

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-f3ec0ff5251f2e6d | data/ingredients/mapped/Puromycin_Dihydrochloride.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1716],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:8642","line":1718,"mapping_status":"MAPPED","ontology_id":"CHEBI:8642","preferred_term":"Puromycin dihydrochloride"}],"identifier":"CHEBI:8642","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:8642","ontology_label":"puromycin dihydrochloride","ontology_source":"CHEBI"},"preferred_term":"Puromycin dihydrochloride","sssom_rows":[{"data_row":2366,"object_id":"CHEBI:8642","object_label":"puromycin dihydrochloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Puromycin_Dihydrochloride","synonym_count":1} |
| ev-bf87f4eb088e5da5 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1716] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-d22fdc3cca40777c | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Puromycin_Dihydrochloride; data-row positions=[2366] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2366,"object_id":"CHEBI:8642","object_label":"puromycin dihydrochloride","other":"3'-deoxy-N,N-dimethyl-3'-[(O-methyl-L-tyrosyl)amino]adenosine dihydrochloride&#124;CAS:58-58-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Puromycin_Dihydrochloride","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-72279669dc3f7366 | docs/data/mapped_ingredients.csv; CSV lines=[1718] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:8642","line":1718,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:8642","preferred_term":"Puromycin dihydrochloride","total_occurrences":"0"}] |
| ev-aa978690fe0ec134 | reports/yaml_record_review/Puromycin_Dihydrochloride.md; &#96;data/ingredients/mapped/Puromycin_Dihydrochloride.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-61414474c48a94ae | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1146,1905] | context_only | [{"current_record_sha256":"104d41ec9d80fd2213875e92c3c7136a804180289680e03b9d2a549fba8f1b57","finding_id":"SEM:724e47b94de37587b00f","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"104d41ec9d80fd2213875e92c3c7136a804180289680e03b9d2a549fba8f1b57","finding_id":"SEM:8d05d354f43b4c81b7bf","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-897cce35d695e86c | data/ingredients/mapped/Puromycin_Dihydrochloride.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}] |
| ev-738fee2933102001 | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml; findings[finding_id=f-f7bfc8825db4764b] | context_only | Predecessor structured review finding f-f7bfc8825db4764b in 20261011T024638Z-mim-reconcile-all-batch-10 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-puromycin-dihydrochloride
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Puromycin_Dihydrochloride (data/ingredients/mapped/Puromycin_Dihydrochloride.yaml)'
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
summary: Per-record structured review for Puromycin_Dihydrochloride (data/ingredients/mapped/Puromycin_Dihydrochloride.yaml,
  record-098adafbd6c7bac1, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Puromycin_Dihydrochloride.yaml
    sha256: 104d41ec9d80fd2213875e92c3c7136a804180289680e03b9d2a549fba8f1b57
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
  - path: reports/yaml_record_review/Puromycin_Dihydrochloride.md
    sha256: 02cbd61da266138f3386e2b1932d249dac888abb044a29581abb498134b97742
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-098adafbd6c7bac1
  path: data/ingredients/mapped/Puromycin_Dihydrochloride.yaml
  label: Puromycin_Dihydrochloride
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Puromycin_Dihydrochloride.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Puromycin_Dihydrochloride.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Puromycin_Dihydrochloride.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-098adafbd6c7bac1
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-098adafbd6c7bac1
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-098adafbd6c7bac1
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10
    and semantic review dispositions on HEAD.
  target_ids:
  - record-098adafbd6c7bac1
evidence:
- evidence_id: ev-f3ec0ff5251f2e6d
  kind: record_content
  reference: data/ingredients/mapped/Puromycin_Dihydrochloride.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1716],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:8642","line":1718,"mapping_status":"MAPPED","ontology_id":"CHEBI:8642","preferred_term":"Puromycin
    dihydrochloride"}],"identifier":"CHEBI:8642","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:8642","ontology_label":"puromycin
    dihydrochloride","ontology_source":"CHEBI"},"preferred_term":"Puromycin dihydrochloride","sssom_rows":[{"data_row":2366,"object_id":"CHEBI:8642","object_label":"puromycin
    dihydrochloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Puromycin_Dihydrochloride","synonym_count":1}'
  snapshot_sha256: 104d41ec9d80fd2213875e92c3c7136a804180289680e03b9d2a549fba8f1b57
- evidence_id: ev-bf87f4eb088e5da5
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1716]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-d22fdc3cca40777c
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Puromycin_Dihydrochloride; data-row positions=[2366]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2366,"object_id":"CHEBI:8642","object_label":"puromycin
    dihydrochloride","other":"3''-deoxy-N,N-dimethyl-3''-[(O-methyl-L-tyrosyl)amino]adenosine
    dihydrochloride|CAS:58-58-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Puromycin_Dihydrochloride","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-72279669dc3f7366
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1718]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:8642","line":1718,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:8642","preferred_term":"Puromycin
    dihydrochloride","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-aa978690fe0ec134
  kind: prior_review
  reference: reports/yaml_record_review/Puromycin_Dihydrochloride.md
  locator: '`data/ingredients/mapped/Puromycin_Dihydrochloride.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 02cbd61da266138f3386e2b1932d249dac888abb044a29581abb498134b97742
- evidence_id: ev-61414474c48a94ae
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1146,1905]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"104d41ec9d80fd2213875e92c3c7136a804180289680e03b9d2a549fba8f1b57","finding_id":"SEM:724e47b94de37587b00f","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"104d41ec9d80fd2213875e92c3c7136a804180289680e03b9d2a549fba8f1b57","finding_id":"SEM:8d05d354f43b4c81b7bf","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-897cce35d695e86c
  kind: record_content
  reference: data/ingredients/mapped/Puromycin_Dihydrochloride.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}]'
  snapshot_sha256: 104d41ec9d80fd2213875e92c3c7136a804180289680e03b9d2a549fba8f1b57
- evidence_id: ev-738fee2933102001
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
  locator: findings[finding_id=f-f7bfc8825db4764b]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-f7bfc8825db4764b in 20261011T024638Z-mim-reconcile-all-batch-10
  snapshot_sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
assessments:
- assessment_id: a-3c438b137ff44ebb
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-098adafbd6c7bac1
  evidence_ids:
  - ev-f3ec0ff5251f2e6d
  - ev-bf87f4eb088e5da5
  - ev-d22fdc3cca40777c
  - ev-72279669dc3f7366
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-4d2269bc92cf043d
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-098adafbd6c7bac1
  evidence_ids:
  - ev-aa978690fe0ec134
  - ev-f3ec0ff5251f2e6d
  - ev-61414474c48a94ae
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T10:53:18Z;
    reviewed SHA-256=104d41ec9d80fd2213875e92c3c7136a804180289680e03b9d2a549fba8f1b57;
    current SHA-256=104d41ec9d80fd2213875e92c3c7136a804180289680e03b9d2a549fba8f1b57;
    hash_changed=False. Reports=["reports/yaml_record_review/Puromycin_Dihydrochloride.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:8642 identity and final synonyms pass, but SELECTIVE_AGENT is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-aa978690fe0ec134
    - ev-f3ec0ff5251f2e6d
  - name: legacy-native-ids
    value: '["SEM:724e47b94de37587b00f","SEM:8d05d354f43b4c81b7bf"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-f3ec0ff5251f2e6d
    - ev-aa978690fe0ec134
    - ev-61414474c48a94ae
- assessment_id: a-897cce35d695e86c
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-098adafbd6c7bac1
  evidence_ids:
  - ev-aa978690fe0ec134
  - ev-897cce35d695e86c
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-aa978690fe0ec134
    - ev-897cce35d695e86c
findings:
- finding_id: rec-f-f7bfc8825db4764b
  issue_key: mim-reconciliation-role-support-098adafbd6c7bac1
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Puromycin dihydrochloride'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-098adafbd6c7bac1
  evidence_ids:
  - ev-aa978690fe0ec134
  - ev-897cce35d695e86c
  - ev-738fee2933102001
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Puromycin_Dihydrochloride.yaml
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
    review_id: 20261011T024638Z-mim-reconcile-all-batch-10
    finding_id: f-f7bfc8825db4764b
actions:
- action_id: rec-action-f7bfc8825db4764b
  description: 'Reassess prediction-only role support: Puromycin dihydrochloride'
  finding_ids:
  - rec-f-f7bfc8825db4764b
  target_ids:
  - record-098adafbd6c7bac1
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Puromycin_Dihydrochloride.yaml
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
