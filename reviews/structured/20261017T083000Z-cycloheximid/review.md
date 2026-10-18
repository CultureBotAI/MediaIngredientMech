# Per-record structured review: Cycloheximid (data/ingredients/mapped/Cycloheximid.yaml)

- Review: 20261017T083000Z-cycloheximid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Cycloheximid (data/ingredients/mapped/Cycloheximid.yaml, record-0f7a96a94e6b8dbf, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Cycloheximid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Cycloheximid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-0f7a96a94e6b8dbf | data/ingredients/mapped/Cycloheximid.yaml | maintained | Cycloheximid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-0f7a96a94e6b8dbf | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-0f7a96a94e6b8dbf | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-0f7a96a94e6b8dbf | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-0f7a96a94e6b8dbf.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-0f7a96a94e6b8dbf.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T12:57:45Z; reviewed SHA-256=252ac8771048780efc743b3a921ccadaa35e08396d1a807216c3a2763a940f2c; current SHA-256=252ac8771048780efc743b3a921ccadaa35e08396d1a807216c3a2763a940f2c; hash_changed=False. Reports=["reports/yaml_record_review/Cycloheximid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI cycloheximide identity, structure, count, and final SSSOM row pass, but the selective-agent role is only provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-0f7a96a94e6b8dbf.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-69f67efe3bb08d32: Reassess prediction-only role support: Cycloheximid

major / open / confirmed; issue key: mim-reconciliation-role-support-0f7a96a94e6b8dbf.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-69f67efe3bb08d32

Reassess prediction-only role support: Cycloheximid

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-17f1775a004958ba | data/ingredients/mapped/Cycloheximid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[785],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:27641","line":787,"mapping_status":"MAPPED","ontology_id":"CHEBI:27641","preferred_term":"Cycloheximid"}],"identifier":"CHEBI:27641","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":10,"edge_count":10,"occurrences":10},"occurrence_statistics":{"media_count":10,"total_occurrences":10},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:27641","ontology_label":"cycloheximide","ontology_source":"CHEBI"},"preferred_term":"Cycloheximid","sssom_rows":[{"data_row":860,"object_id":"CHEBI:27641","object_label":"cycloheximide","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cycloheximid","synonym_count":10} |
| ev-9c19c8e8c5c02b56 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [785] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-d28d470cb64b64a4 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Cycloheximid; data-row positions=[860] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":860,"object_id":"CHEBI:27641","object_label":"cycloheximide","other":"3-((R)-2-((1S,3S,5S)-3,5-dimethyl-2-oxocyclohexyl)-2-hydroxyethyl)glutarimide&#124;4-{(2R)-2-[(1S,3S,5S)-3,5-dimethyl-2-oxocyclohexyl]-2-hydroxyethyl}piperidine-2,6-dione&#124;Cyclohexemid&#124;Zykloheximid&#124;cicloheximida&#124;cicloheximide&#124;cicloheximidum&#124;naramycin&#124;naramycin A&#124;CAS:66-81-9","predicate_id":"skos:exactMatch","subject_id":"MIM:Cycloheximid","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-f11dd9932eef22fa | docs/data/mapped_ingredients.csv; CSV lines=[787] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:27641","line":787,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"10","ontology_id":"CHEBI:27641","preferred_term":"Cycloheximid","total_occurrences":"10"}] |
| ev-d27f08096dbc85e8 | reports/yaml_record_review/Cycloheximid.md; &#96;data/ingredients/mapped/Cycloheximid.yaml&#96;:2; Verdict:4; Identity:11; Validation:25; Evidence:45; Completeness:61; Recommended Edits:69 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-305ea110c7963a32 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[458,1504] | context_only | [{"current_record_sha256":"252ac8771048780efc743b3a921ccadaa35e08396d1a807216c3a2763a940f2c","finding_id":"SEM:f39b8af2a53c13823f2d","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"252ac8771048780efc743b3a921ccadaa35e08396d1a807216c3a2763a940f2c","finding_id":"SEM:9085d4de04109ab43180","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-416744d1ef3788e1 | data/ingredients/mapped/Cycloheximid.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional in-session LLM role assignment; review recommended.","reference_text":"Assigned by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}] |
| ev-1d13ecef04bba705 | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-69f67efe3bb08d32] | context_only | Predecessor structured review finding f-69f67efe3bb08d32 in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-cycloheximid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Cycloheximid (data/ingredients/mapped/Cycloheximid.yaml)'
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
summary: Per-record structured review for Cycloheximid (data/ingredients/mapped/Cycloheximid.yaml,
  record-0f7a96a94e6b8dbf, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Cycloheximid.yaml
    sha256: 252ac8771048780efc743b3a921ccadaa35e08396d1a807216c3a2763a940f2c
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
  - path: reports/yaml_record_review/Cycloheximid.md
    sha256: 6e6d9bf277dd0d721e1bf1a9e8721d1599a1fd46675d0fcd7231b7bc1f538f85
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-0f7a96a94e6b8dbf
  path: data/ingredients/mapped/Cycloheximid.yaml
  label: Cycloheximid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cycloheximid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Cycloheximid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Cycloheximid.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-0f7a96a94e6b8dbf
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-0f7a96a94e6b8dbf
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-0f7a96a94e6b8dbf
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-0f7a96a94e6b8dbf
evidence:
- evidence_id: ev-17f1775a004958ba
  kind: record_content
  reference: data/ingredients/mapped/Cycloheximid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[785],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:27641","line":787,"mapping_status":"MAPPED","ontology_id":"CHEBI:27641","preferred_term":"Cycloheximid"}],"identifier":"CHEBI:27641","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":10,"edge_count":10,"occurrences":10},"occurrence_statistics":{"media_count":10,"total_occurrences":10},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:27641","ontology_label":"cycloheximide","ontology_source":"CHEBI"},"preferred_term":"Cycloheximid","sssom_rows":[{"data_row":860,"object_id":"CHEBI:27641","object_label":"cycloheximide","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cycloheximid","synonym_count":10}'
  snapshot_sha256: 252ac8771048780efc743b3a921ccadaa35e08396d1a807216c3a2763a940f2c
- evidence_id: ev-9c19c8e8c5c02b56
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [785]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-d28d470cb64b64a4
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Cycloheximid; data-row positions=[860]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":860,"object_id":"CHEBI:27641","object_label":"cycloheximide","other":"3-((R)-2-((1S,3S,5S)-3,5-dimethyl-2-oxocyclohexyl)-2-hydroxyethyl)glutarimide|4-{(2R)-2-[(1S,3S,5S)-3,5-dimethyl-2-oxocyclohexyl]-2-hydroxyethyl}piperidine-2,6-dione|Cyclohexemid|Zykloheximid|cicloheximida|cicloheximide|cicloheximidum|naramycin|naramycin
    A|CAS:66-81-9","predicate_id":"skos:exactMatch","subject_id":"MIM:Cycloheximid","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-f11dd9932eef22fa
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[787]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:27641","line":787,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"10","ontology_id":"CHEBI:27641","preferred_term":"Cycloheximid","total_occurrences":"10"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-d27f08096dbc85e8
  kind: prior_review
  reference: reports/yaml_record_review/Cycloheximid.md
  locator: '`data/ingredients/mapped/Cycloheximid.yaml`:2; Verdict:4; Identity:11;
    Validation:25; Evidence:45; Completeness:61; Recommended Edits:69'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 6e6d9bf277dd0d721e1bf1a9e8721d1599a1fd46675d0fcd7231b7bc1f538f85
  quote: "Recommended Edits:\n- Major: either replace the provisional `SELECTIVE_AGENT`\
    \ role evidence with a\n  source-backed database or literature reference, or remove\
    \ the role until\n  direct use as a selective agent is curated.\n- Regenerate\
    \ synchronized products and rerun strict validation, LinkML term\n  validation,\
    \ SSSOM QC, aggregate roundtrip, and `git diff --check`."
- evidence_id: ev-305ea110c7963a32
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[458,1504]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"252ac8771048780efc743b3a921ccadaa35e08396d1a807216c3a2763a940f2c","finding_id":"SEM:f39b8af2a53c13823f2d","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"252ac8771048780efc743b3a921ccadaa35e08396d1a807216c3a2763a940f2c","finding_id":"SEM:9085d4de04109ab43180","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-416744d1ef3788e1
  kind: record_content
  reference: data/ingredients/mapped/Cycloheximid.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional
    in-session LLM role assignment; review recommended.","reference_text":"Assigned
    by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}]'
  snapshot_sha256: 252ac8771048780efc743b3a921ccadaa35e08396d1a807216c3a2763a940f2c
- evidence_id: ev-1d13ecef04bba705
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-69f67efe3bb08d32]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-69f67efe3bb08d32 in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-4f45ce0463a973b6
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-0f7a96a94e6b8dbf
  evidence_ids:
  - ev-17f1775a004958ba
  - ev-9c19c8e8c5c02b56
  - ev-d28d470cb64b64a4
  - ev-f11dd9932eef22fa
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-ba7c1ca1d7c8b792
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-0f7a96a94e6b8dbf
  evidence_ids:
  - ev-d27f08096dbc85e8
  - ev-17f1775a004958ba
  - ev-305ea110c7963a32
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T12:57:45Z;
    reviewed SHA-256=252ac8771048780efc743b3a921ccadaa35e08396d1a807216c3a2763a940f2c;
    current SHA-256=252ac8771048780efc743b3a921ccadaa35e08396d1a807216c3a2763a940f2c;
    hash_changed=False. Reports=["reports/yaml_record_review/Cycloheximid.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    cycloheximide identity, structure, count, and final SSSOM row pass, but the selective-agent
    role is only provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d27f08096dbc85e8
    - ev-17f1775a004958ba
  - name: legacy-native-ids
    value: '["SEM:f39b8af2a53c13823f2d","SEM:9085d4de04109ab43180"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-17f1775a004958ba
    - ev-d27f08096dbc85e8
    - ev-305ea110c7963a32
- assessment_id: a-416744d1ef3788e1
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-0f7a96a94e6b8dbf
  evidence_ids:
  - ev-d27f08096dbc85e8
  - ev-416744d1ef3788e1
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d27f08096dbc85e8
    - ev-416744d1ef3788e1
findings:
- finding_id: rec-f-69f67efe3bb08d32
  issue_key: mim-reconciliation-role-support-0f7a96a94e6b8dbf
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Cycloheximid'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-0f7a96a94e6b8dbf
  evidence_ids:
  - ev-d27f08096dbc85e8
  - ev-416744d1ef3788e1
  - ev-1d13ecef04bba705
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cycloheximid.yaml
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
    finding_id: f-69f67efe3bb08d32
actions:
- action_id: rec-action-69f67efe3bb08d32
  description: 'Reassess prediction-only role support: Cycloheximid'
  finding_ids:
  - rec-f-69f67efe3bb08d32
  target_ids:
  - record-0f7a96a94e6b8dbf
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cycloheximid.yaml
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
