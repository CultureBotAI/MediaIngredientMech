# Per-record structured review: Beta-lactose (data/ingredients/mapped/Beta-lactose.yaml)

- Review: 20261017T083000Z-beta-lactose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Beta-lactose (data/ingredients/mapped/Beta-lactose.yaml, record-c9541151dd71c170, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Beta-lactose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Beta-lactose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-c9541151dd71c170 | data/ingredients/mapped/Beta-lactose.yaml | maintained | Beta-lactose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-c9541151dd71c170 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-c9541151dd71c170 | Role assertions on nutritional_roles[0], nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-c9541151dd71c170 | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-c9541151dd71c170.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: not_applicable. Targets: record-c9541151dd71c170.

The latest legacy review reports no outstanding finding. This run verifies local consistency only; it does not renew that earlier scientific pass.

Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-16T09:43:55Z; reviewed SHA-256=f1c39640418e71ea7999184bcb97d44bb238c7eef405a5ff7c80864e7a7bad86; current SHA-256=f1c39640418e71ea7999184bcb97d44bb238c7eef405a5ff7c80864e7a7bad86; hash_changed=False. Reports=["reports/yaml_record_review/Beta-lactose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI beta-lactose identity, CAS, exact synonym, provisional roles, structure fields, SSSOM row, and aggregate copy pass.

### Historical provisional-role concern

evidence: concern. Targets: record-c9541151dd71c170.

Current role assertions on nutritional_roles[0], nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence lists and require source-backed curation support.

## Findings

### rec-f-role-c9541151dd71c170: Reassess prediction-only or empty role support: Beta-lactose

major / open / confirmed; issue key: mim-reconciliation-role-support-c9541151dd71c170.

Prediction-only or empty evidence payloads remain on the named current role assertions (nutritional_roles[0], nutritional_roles[1]). This confirms the local evidence gap, not that the biological role is false.

## Recommended Actions And Acceptance Checks

### rec-act-role-c9541151dd71c170

Reassess prediction-only or empty role support: Beta-lactose

- Address the exact role fields and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-70a9a71a117b20d1 | data/ingredients/mapped/Beta-lactose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[581],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:36218","line":583,"mapping_status":"MAPPED","ontology_id":"CHEBI:36218","preferred_term":"Beta-Lactose"}],"identifier":"CHEBI:36218","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1,"edge_count":1,"occurrences":1},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:36218","ontology_label":"beta-lactose","ontology_source":"CHEBI"},"preferred_term":"Beta-Lactose","sssom_rows":[{"data_row":533,"object_id":"CHEBI:36218","object_label":"beta-lactose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Beta-lactose","synonym_count":3} |
| ev-6b7b088b6f99d1c3 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [581] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-1dafd4a52d1a0488 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Beta-lactose; data-row positions=[533] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":533,"object_id":"CHEBI:36218","object_label":"beta-lactose","other":"lactose&#124;beta-D-galactopyranosyl-(1-&gt;4)-beta-D-glucopyranose&#124;CAS:5965-66-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Beta-lactose","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-ae6f0803e22ac2d9 | docs/data/mapped_ingredients.csv; CSV lines=[583] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:36218","line":583,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:36218","preferred_term":"Beta-Lactose","total_occurrences":"1"}] |
| ev-aa860ecacb5e7c9c | reports/yaml_record_review/Beta-lactose.md; &#96;data/ingredients/mapped/Beta-lactose.yaml&#96;:2; Verdict:4; Identity:9; Validation:19; Evidence:29; Completeness:46; Recommended Edits:55 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-ebf41b2a9c8d8ea4 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1816,2075] | context_only | [{"current_record_sha256":"f1c39640418e71ea7999184bcb97d44bb238c7eef405a5ff7c80864e7a7bad86","finding_id":"SEM:d6cc98d35dfaefbbf93a","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"f1c39640418e71ea7999184bcb97d44bb238c7eef405a5ff7c80864e7a7bad86","finding_id":"SEM:8d6fcb779bc4dbc067ad","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-beta-lactose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Beta-lactose (data/ingredients/mapped/Beta-lactose.yaml)'
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
summary: Per-record structured review for Beta-lactose (data/ingredients/mapped/Beta-lactose.yaml,
  record-c9541151dd71c170, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Beta-lactose.yaml
    sha256: f1c39640418e71ea7999184bcb97d44bb238c7eef405a5ff7c80864e7a7bad86
    role: target
  - path: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
    sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
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
  - path: reports/yaml_record_review/Beta-lactose.md
    sha256: 582dbbbb0faf23678abda907416ffd0c6654e286099a9eccd706e77e45f1e906
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-c9541151dd71c170
  path: data/ingredients/mapped/Beta-lactose.yaml
  label: Beta-lactose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Beta-lactose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Beta-lactose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Beta-lactose.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-c9541151dd71c170
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-c9541151dd71c170
  evidence_ids:
  - ev-70a9a71a117b20d1
  - ev-6b7b088b6f99d1c3
  - ev-1dafd4a52d1a0488
  - ev-ae6f0803e22ac2d9
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0], nutritional_roles[1] rely only
    on COMPUTATIONAL_PREDICTION or empty evidence.
  target_ids:
  - record-c9541151dd71c170
  evidence_ids:
  - ev-70a9a71a117b20d1
  - ev-ebf41b2a9c8d8ea4
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-c9541151dd71c170
  evidence_ids:
  - ev-aa860ecacb5e7c9c
  - ev-ebf41b2a9c8d8ea4
evidence:
- evidence_id: ev-70a9a71a117b20d1
  kind: record_content
  reference: data/ingredients/mapped/Beta-lactose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[581],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:36218","line":583,"mapping_status":"MAPPED","ontology_id":"CHEBI:36218","preferred_term":"Beta-Lactose"}],"identifier":"CHEBI:36218","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1,"edge_count":1,"occurrences":1},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:36218","ontology_label":"beta-lactose","ontology_source":"CHEBI"},"preferred_term":"Beta-Lactose","sssom_rows":[{"data_row":533,"object_id":"CHEBI:36218","object_label":"beta-lactose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Beta-lactose","synonym_count":3}'
  snapshot_sha256: f1c39640418e71ea7999184bcb97d44bb238c7eef405a5ff7c80864e7a7bad86
- evidence_id: ev-6b7b088b6f99d1c3
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [581]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-1dafd4a52d1a0488
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Beta-lactose; data-row positions=[533]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":533,"object_id":"CHEBI:36218","object_label":"beta-lactose","other":"lactose|beta-D-galactopyranosyl-(1->4)-beta-D-glucopyranose|CAS:5965-66-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Beta-lactose","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-ae6f0803e22ac2d9
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[583]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:36218","line":583,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:36218","preferred_term":"Beta-Lactose","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-aa860ecacb5e7c9c
  kind: prior_review
  reference: reports/yaml_record_review/Beta-lactose.md
  locator: '`data/ingredients/mapped/Beta-lactose.yaml`:2; Verdict:4; Identity:9;
    Validation:19; Evidence:29; Completeness:46; Recommended Edits:55'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 582dbbbb0faf23678abda907416ffd0c6654e286099a9eccd706e77e45f1e906
  quote: 'Recommended Edits:

    - None.'
- evidence_id: ev-ebf41b2a9c8d8ea4
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1816,2075]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"f1c39640418e71ea7999184bcb97d44bb238c7eef405a5ff7c80864e7a7bad86","finding_id":"SEM:d6cc98d35dfaefbbf93a","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"f1c39640418e71ea7999184bcb97d44bb238c7eef405a5ff7c80864e7a7bad86","finding_id":"SEM:8d6fcb779bc4dbc067ad","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-106d41be3255ef94
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-c9541151dd71c170
  evidence_ids:
  - ev-70a9a71a117b20d1
  - ev-6b7b088b6f99d1c3
  - ev-1dafd4a52d1a0488
  - ev-ae6f0803e22ac2d9
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-c8f7255e636bcd1f
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: not_applicable
  summary: The latest legacy review reports no outstanding finding. This run verifies
    local consistency only; it does not renew that earlier scientific pass.
  target_ids:
  - record-c9541151dd71c170
  evidence_ids:
  - ev-aa860ecacb5e7c9c
  - ev-70a9a71a117b20d1
  - ev-ebf41b2a9c8d8ea4
  details: 'Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-16T09:43:55Z;
    reviewed SHA-256=f1c39640418e71ea7999184bcb97d44bb238c7eef405a5ff7c80864e7a7bad86;
    current SHA-256=f1c39640418e71ea7999184bcb97d44bb238c7eef405a5ff7c80864e7a7bad86;
    hash_changed=False. Reports=["reports/yaml_record_review/Beta-lactose.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    beta-lactose identity, CAS, exact synonym, provisional roles, structure fields,
    SSSOM row, and aggregate copy pass.'
  dimensions:
  - name: legacy-native-ids
    value: '["SEM:d6cc98d35dfaefbbf93a","SEM:8d6fcb779bc4dbc067ad"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-70a9a71a117b20d1
    - ev-aa860ecacb5e7c9c
    - ev-ebf41b2a9c8d8ea4
- assessment_id: a-role-c9541151dd71c170
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Current role assertions on nutritional_roles[0], nutritional_roles[1] rely
    only on COMPUTATIONAL_PREDICTION or empty evidence lists and require source-backed
    curation support.
  target_ids:
  - record-c9541151dd71c170
  evidence_ids:
  - ev-70a9a71a117b20d1
  - ev-ebf41b2a9c8d8ea4
  dimensions:
  - name: legacy-disposition
    value: still_present
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-70a9a71a117b20d1
    - ev-ebf41b2a9c8d8ea4
findings:
- finding_id: rec-f-role-c9541151dd71c170
  issue_key: mim-reconciliation-role-support-c9541151dd71c170
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only or empty role support: Beta-lactose'
  description: Prediction-only or empty evidence payloads remain on the named current
    role assertions (nutritional_roles[0], nutritional_roles[1]). This confirms the
    local evidence gap, not that the biological role is false.
  target_ids:
  - record-c9541151dd71c170
  evidence_ids:
  - ev-70a9a71a117b20d1
  - ev-ebf41b2a9c8d8ea4
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Beta-lactose.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  - nutritional_roles[1]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
actions:
- action_id: rec-act-role-c9541151dd71c170
  description: 'Reassess prediction-only or empty role support: Beta-lactose'
  finding_ids:
  - rec-f-role-c9541151dd71c170
  target_ids:
  - record-c9541151dd71c170
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Beta-lactose.yaml
    role: maintained ingredient
  acceptance_checks:
  - Address the exact role fields and evidence gap described in this finding; preserve
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
  with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.
```
