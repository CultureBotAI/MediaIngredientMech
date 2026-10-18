# Per-record structured review: Levofloxacin (data/ingredients/mapped/Levofloxacin.yaml)

- Review: 20261017T083000Z-levofloxacin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Levofloxacin (data/ingredients/mapped/Levofloxacin.yaml, record-3ee6fca33fec901a, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Levofloxacin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Levofloxacin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-3ee6fca33fec901a | data/ingredients/mapped/Levofloxacin.yaml | maintained | Levofloxacin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-3ee6fca33fec901a | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-3ee6fca33fec901a | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-3ee6fca33fec901a | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-3ee6fca33fec901a.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-3ee6fca33fec901a.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T00:13:53Z; reviewed SHA-256=b1fe3d0c7e5ef5378f8cfcee05cafb23ac1004d40d62118b4853b132cb1218c0; current SHA-256=b1fe3d0c7e5ef5378f8cfcee05cafb23ac1004d40d62118b4853b132cb1218c0; hash_changed=False. Reports=["reports/yaml_record_review/Levofloxacin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CultureBotHT CHEBI:63598 identity, CAS value, PubChem structure, exact synonym, and final SSSOM row pass, but SELECTIVE_AGENT is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-3ee6fca33fec901a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-3f37e714d89c225d: Reassess prediction-only role support: Levofloxacin

major / open / confirmed; issue key: mim-reconciliation-role-support-3ee6fca33fec901a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-3f37e714d89c225d

Reassess prediction-only role support: Levofloxacin

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-5cfe721843bdaf97 | data/ingredients/mapped/Levofloxacin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1296],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:63598","line":1298,"mapping_status":"MAPPED","ontology_id":"CHEBI:63598","preferred_term":"Levofloxacin"}],"identifier":"CHEBI:63598","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:63598","ontology_label":"levofloxacin","ontology_source":"CHEBI"},"preferred_term":"Levofloxacin","sssom_rows":[{"data_row":1686,"object_id":"CHEBI:63598","object_label":"levofloxacin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Levofloxacin","synonym_count":1} |
| ev-7a609a745409ca00 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1296] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-9fb5a7bc41a8d903 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Levofloxacin; data-row positions=[1686] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1686,"object_id":"CHEBI:63598","object_label":"levofloxacin","other":"(3S)-9-fluoro-3-methyl-10-(4-methylpiperazin-1-yl)-7-oxo-2,3-dihydro-7H-[1,4]oxazino[2,3,4-ij]quinoline-6-carboxylic acid&#124;CAS:100986-85-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Levofloxacin","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-8349aa8639c96dd6 | docs/data/mapped_ingredients.csv; CSV lines=[1298] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:63598","line":1298,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:63598","preferred_term":"Levofloxacin","total_occurrences":"0"}] |
| ev-4d204053ac6729d7 | reports/yaml_record_review/Levofloxacin.md; &#96;data/ingredients/mapped/Levofloxacin.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:28; Completeness:44; Recommended Edits:51 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-14609f0be50226df | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[858,1500] | context_only | [{"current_record_sha256":"b1fe3d0c7e5ef5378f8cfcee05cafb23ac1004d40d62118b4853b132cb1218c0","finding_id":"SEM:cb9807ff25e7eb181e93","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"b1fe3d0c7e5ef5378f8cfcee05cafb23ac1004d40d62118b4853b132cb1218c0","finding_id":"SEM:822d99c236565a2f57fe","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-7a7e63e24e253e08 | data/ingredients/mapped/Levofloxacin.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}] |
| ev-518b67bc3246daed | reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml; findings[finding_id=f-3f37e714d89c225d] | context_only | Predecessor structured review finding f-3f37e714d89c225d in 20261011T024635Z-mim-reconcile-all-batch-07 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-levofloxacin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Levofloxacin (data/ingredients/mapped/Levofloxacin.yaml)'
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
summary: Per-record structured review for Levofloxacin (data/ingredients/mapped/Levofloxacin.yaml,
  record-3ee6fca33fec901a, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Levofloxacin.yaml
    sha256: b1fe3d0c7e5ef5378f8cfcee05cafb23ac1004d40d62118b4853b132cb1218c0
    role: target
  - path: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
    sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
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
  - path: reports/yaml_record_review/Levofloxacin.md
    sha256: a26504ca4eed4fd1d715f938bb9c27369f83b734c393d10f71ed356d3492a078
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-3ee6fca33fec901a
  path: data/ingredients/mapped/Levofloxacin.yaml
  label: Levofloxacin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Levofloxacin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Levofloxacin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Levofloxacin.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-3ee6fca33fec901a
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-3ee6fca33fec901a
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-3ee6fca33fec901a
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-3ee6fca33fec901a
evidence:
- evidence_id: ev-5cfe721843bdaf97
  kind: record_content
  reference: data/ingredients/mapped/Levofloxacin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1296],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:63598","line":1298,"mapping_status":"MAPPED","ontology_id":"CHEBI:63598","preferred_term":"Levofloxacin"}],"identifier":"CHEBI:63598","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:63598","ontology_label":"levofloxacin","ontology_source":"CHEBI"},"preferred_term":"Levofloxacin","sssom_rows":[{"data_row":1686,"object_id":"CHEBI:63598","object_label":"levofloxacin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Levofloxacin","synonym_count":1}'
  snapshot_sha256: b1fe3d0c7e5ef5378f8cfcee05cafb23ac1004d40d62118b4853b132cb1218c0
- evidence_id: ev-7a609a745409ca00
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1296]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-9fb5a7bc41a8d903
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Levofloxacin; data-row positions=[1686]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1686,"object_id":"CHEBI:63598","object_label":"levofloxacin","other":"(3S)-9-fluoro-3-methyl-10-(4-methylpiperazin-1-yl)-7-oxo-2,3-dihydro-7H-[1,4]oxazino[2,3,4-ij]quinoline-6-carboxylic
    acid|CAS:100986-85-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Levofloxacin","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-8349aa8639c96dd6
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1298]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:63598","line":1298,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:63598","preferred_term":"Levofloxacin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-4d204053ac6729d7
  kind: prior_review
  reference: reports/yaml_record_review/Levofloxacin.md
  locator: '`data/ingredients/mapped/Levofloxacin.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:28; Completeness:44; Recommended Edits:51'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: a26504ca4eed4fd1d715f938bb9c27369f83b734c393d10f71ed356d3492a078
  quote: "Recommended Edits:\n- Major: either replace `physicochemical_roles.SELECTIVE_AGENT`\
    \ in\n  `data/ingredients/mapped/Levofloxacin.yaml` with inspected source evidence\
    \ for\n  exact levofloxacin use as a selective agent, or remove the provisional\
    \ role.\n- Sync the aggregate copy and regenerate derived products after the YAML\n\
    \  change; rerun strict, term, round-trip, component, and SSSOM validation."
- evidence_id: ev-14609f0be50226df
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[858,1500]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"b1fe3d0c7e5ef5378f8cfcee05cafb23ac1004d40d62118b4853b132cb1218c0","finding_id":"SEM:cb9807ff25e7eb181e93","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"b1fe3d0c7e5ef5378f8cfcee05cafb23ac1004d40d62118b4853b132cb1218c0","finding_id":"SEM:822d99c236565a2f57fe","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-7a7e63e24e253e08
  kind: record_content
  reference: data/ingredients/mapped/Levofloxacin.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}]'
  snapshot_sha256: b1fe3d0c7e5ef5378f8cfcee05cafb23ac1004d40d62118b4853b132cb1218c0
- evidence_id: ev-518b67bc3246daed
  kind: prior_review
  reference: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
  locator: findings[finding_id=f-3f37e714d89c225d]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-3f37e714d89c225d in 20261011T024635Z-mim-reconcile-all-batch-07
  snapshot_sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
assessments:
- assessment_id: a-1b349f743afe7261
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-3ee6fca33fec901a
  evidence_ids:
  - ev-5cfe721843bdaf97
  - ev-7a609a745409ca00
  - ev-9fb5a7bc41a8d903
  - ev-8349aa8639c96dd6
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-6f776a54f9e1a4d8
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-3ee6fca33fec901a
  evidence_ids:
  - ev-4d204053ac6729d7
  - ev-5cfe721843bdaf97
  - ev-14609f0be50226df
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T00:13:53Z;
    reviewed SHA-256=b1fe3d0c7e5ef5378f8cfcee05cafb23ac1004d40d62118b4853b132cb1218c0;
    current SHA-256=b1fe3d0c7e5ef5378f8cfcee05cafb23ac1004d40d62118b4853b132cb1218c0;
    hash_changed=False. Reports=["reports/yaml_record_review/Levofloxacin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The CultureBotHT
    CHEBI:63598 identity, CAS value, PubChem structure, exact synonym, and final SSSOM
    row pass, but SELECTIVE_AGENT is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-4d204053ac6729d7
    - ev-5cfe721843bdaf97
  - name: legacy-native-ids
    value: '["SEM:cb9807ff25e7eb181e93","SEM:822d99c236565a2f57fe"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-5cfe721843bdaf97
    - ev-4d204053ac6729d7
    - ev-14609f0be50226df
- assessment_id: a-7a7e63e24e253e08
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-3ee6fca33fec901a
  evidence_ids:
  - ev-4d204053ac6729d7
  - ev-7a7e63e24e253e08
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-4d204053ac6729d7
    - ev-7a7e63e24e253e08
findings:
- finding_id: rec-f-3f37e714d89c225d
  issue_key: mim-reconciliation-role-support-3ee6fca33fec901a
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Levofloxacin'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-3ee6fca33fec901a
  evidence_ids:
  - ev-4d204053ac6729d7
  - ev-7a7e63e24e253e08
  - ev-518b67bc3246daed
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Levofloxacin.yaml
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
    review_id: 20261011T024635Z-mim-reconcile-all-batch-07
    finding_id: f-3f37e714d89c225d
actions:
- action_id: rec-action-3f37e714d89c225d
  description: 'Reassess prediction-only role support: Levofloxacin'
  finding_ids:
  - rec-f-3f37e714d89c225d
  target_ids:
  - record-3ee6fca33fec901a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Levofloxacin.yaml
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
  with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.
```
