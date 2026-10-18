# Per-record structured review: Glutaric_Acid (data/ingredients/mapped/Glutaric_Acid.yaml)

- Review: 20261017T083000Z-glutaric-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Glutaric_Acid (data/ingredients/mapped/Glutaric_Acid.yaml, record-1eaa6d3513b9e617, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Glutaric_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Glutaric_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-1eaa6d3513b9e617 | data/ingredients/mapped/Glutaric_Acid.yaml | maintained | Glutaric_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-1eaa6d3513b9e617 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-1eaa6d3513b9e617 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-1eaa6d3513b9e617 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-1eaa6d3513b9e617.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-1eaa6d3513b9e617.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T18:02:48Z; reviewed SHA-256=727a6ea75ee2da6c4bc8c0ab9bef77ad41001166727c27bb430e4e05dc26b7c3; current SHA-256=727a6ea75ee2da6c4bc8c0ab9bef77ad41001166727c27bb430e4e05dc26b7c3; hash_changed=False. Reports=["reports/yaml_record_review/Glutaric_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact glutaric acid identity and final SSSOM row pass, but CARBON_SOURCE is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-1eaa6d3513b9e617.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-5f0413eed13438e8: Reassess prediction-only role support: Glutaric acid

major / open / confirmed; issue key: mim-reconciliation-role-support-1eaa6d3513b9e617.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-5f0413eed13438e8

Reassess prediction-only role support: Glutaric acid

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-6ba998b31f107ed6 | data/ingredients/mapped/Glutaric_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1063],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17859","line":1065,"mapping_status":"MAPPED","ontology_id":"CHEBI:17859","preferred_term":"Glutaric acid"}],"identifier":"CHEBI:17859","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17859","ontology_label":"glutaric acid","ontology_source":"CHEBI"},"preferred_term":"Glutaric acid","sssom_rows":[{"data_row":1325,"object_id":"CHEBI:17859","object_label":"glutaric acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glutaric_Acid","synonym_count":1} |
| ev-aaa61b4144b6aebc | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1063] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-b805b18a8be36e51 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Glutaric_Acid; data-row positions=[1325] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1325,"object_id":"CHEBI:17859","object_label":"glutaric acid","other":"Pentanedioic acid&#124;CAS:110-94-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Glutaric_Acid","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-a2269d69c1ac824f | docs/data/mapped_ingredients.csv; CSV lines=[1065] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:17859","line":1065,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:17859","preferred_term":"Glutaric acid","total_occurrences":"0"}] |
| ev-967baf2ce9d63e79 | reports/yaml_record_review/Glutaric_Acid.md; &#96;data/ingredients/mapped/Glutaric_Acid.yaml&#96;:2; Verdict:4; Identity:11; Validation:22; Evidence:34; Completeness:56; Recommended Edits:62 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-9eb6b96ad9457278 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[682,1576] | context_only | [{"current_record_sha256":"727a6ea75ee2da6c4bc8c0ab9bef77ad41001166727c27bb430e4e05dc26b7c3","finding_id":"SEM:f263626cc4a533fc0caf","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"727a6ea75ee2da6c4bc8c0ab9bef77ad41001166727c27bb430e4e05dc26b7c3","finding_id":"SEM:c48adabf69b367aabd32","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-2545873977cfcddb | data/ingredients/mapped/Glutaric_Acid.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}] |
| ev-87dc715fbde89644 | reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml; findings[finding_id=f-5f0413eed13438e8] | context_only | Predecessor structured review finding f-5f0413eed13438e8 in 20261011T024634Z-mim-reconcile-all-batch-06 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-glutaric-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Glutaric_Acid (data/ingredients/mapped/Glutaric_Acid.yaml)'
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
summary: Per-record structured review for Glutaric_Acid (data/ingredients/mapped/Glutaric_Acid.yaml,
  record-1eaa6d3513b9e617, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Glutaric_Acid.yaml
    sha256: 727a6ea75ee2da6c4bc8c0ab9bef77ad41001166727c27bb430e4e05dc26b7c3
    role: target
  - path: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
    sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
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
  - path: reports/yaml_record_review/Glutaric_Acid.md
    sha256: 6a2e2ae410a1d45f6b8ae05f6383eb5ef9c6c7ff253f73d3667ad91642ec996b
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-1eaa6d3513b9e617
  path: data/ingredients/mapped/Glutaric_Acid.yaml
  label: Glutaric_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glutaric_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Glutaric_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Glutaric_Acid.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-1eaa6d3513b9e617
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-1eaa6d3513b9e617
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-1eaa6d3513b9e617
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-1eaa6d3513b9e617
evidence:
- evidence_id: ev-6ba998b31f107ed6
  kind: record_content
  reference: data/ingredients/mapped/Glutaric_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1063],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17859","line":1065,"mapping_status":"MAPPED","ontology_id":"CHEBI:17859","preferred_term":"Glutaric
    acid"}],"identifier":"CHEBI:17859","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17859","ontology_label":"glutaric
    acid","ontology_source":"CHEBI"},"preferred_term":"Glutaric acid","sssom_rows":[{"data_row":1325,"object_id":"CHEBI:17859","object_label":"glutaric
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glutaric_Acid","synonym_count":1}'
  snapshot_sha256: 727a6ea75ee2da6c4bc8c0ab9bef77ad41001166727c27bb430e4e05dc26b7c3
- evidence_id: ev-aaa61b4144b6aebc
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1063]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-b805b18a8be36e51
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Glutaric_Acid; data-row positions=[1325]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1325,"object_id":"CHEBI:17859","object_label":"glutaric
    acid","other":"Pentanedioic acid|CAS:110-94-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Glutaric_Acid","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-a2269d69c1ac824f
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1065]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:17859","line":1065,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:17859","preferred_term":"Glutaric
    acid","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-967baf2ce9d63e79
  kind: prior_review
  reference: reports/yaml_record_review/Glutaric_Acid.md
  locator: '`data/ingredients/mapped/Glutaric_Acid.yaml`:2; Verdict:4; Identity:11;
    Validation:22; Evidence:34; Completeness:56; Recommended Edits:62'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 6a2e2ae410a1d45f6b8ae05f6383eb5ef9c6c7ff253f73d3667ad91642ec996b
  quote: "Recommended Edits:\n- Major: remove `nutritional_roles.CARBON_SOURCE` from\n\
    \  `data/ingredients/mapped/Glutaric_Acid.yaml`, or replace the provisional\n\
    \  name-pattern evidence with inspected source evidence that specifically\n  supports\
    \ glutaric acid as a carbon source."
- evidence_id: ev-9eb6b96ad9457278
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[682,1576]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"727a6ea75ee2da6c4bc8c0ab9bef77ad41001166727c27bb430e4e05dc26b7c3","finding_id":"SEM:f263626cc4a533fc0caf","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"727a6ea75ee2da6c4bc8c0ab9bef77ad41001166727c27bb430e4e05dc26b7c3","finding_id":"SEM:c48adabf69b367aabd32","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-2545873977cfcddb
  kind: record_content
  reference: data/ingredients/mapped/Glutaric_Acid.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}]'
  snapshot_sha256: 727a6ea75ee2da6c4bc8c0ab9bef77ad41001166727c27bb430e4e05dc26b7c3
- evidence_id: ev-87dc715fbde89644
  kind: prior_review
  reference: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
  locator: findings[finding_id=f-5f0413eed13438e8]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-5f0413eed13438e8 in 20261011T024634Z-mim-reconcile-all-batch-06
  snapshot_sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
assessments:
- assessment_id: a-6e714437a7cada7d
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-1eaa6d3513b9e617
  evidence_ids:
  - ev-6ba998b31f107ed6
  - ev-aaa61b4144b6aebc
  - ev-b805b18a8be36e51
  - ev-a2269d69c1ac824f
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-11385a703fdf94e8
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-1eaa6d3513b9e617
  evidence_ids:
  - ev-967baf2ce9d63e79
  - ev-6ba998b31f107ed6
  - ev-9eb6b96ad9457278
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T18:02:48Z;
    reviewed SHA-256=727a6ea75ee2da6c4bc8c0ab9bef77ad41001166727c27bb430e4e05dc26b7c3;
    current SHA-256=727a6ea75ee2da6c4bc8c0ab9bef77ad41001166727c27bb430e4e05dc26b7c3;
    hash_changed=False. Reports=["reports/yaml_record_review/Glutaric_Acid.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact glutaric
    acid identity and final SSSOM row pass, but CARBON_SOURCE is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-967baf2ce9d63e79
    - ev-6ba998b31f107ed6
  - name: legacy-native-ids
    value: '["SEM:f263626cc4a533fc0caf","SEM:c48adabf69b367aabd32"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-6ba998b31f107ed6
    - ev-967baf2ce9d63e79
    - ev-9eb6b96ad9457278
- assessment_id: a-2545873977cfcddb
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-1eaa6d3513b9e617
  evidence_ids:
  - ev-967baf2ce9d63e79
  - ev-2545873977cfcddb
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-967baf2ce9d63e79
    - ev-2545873977cfcddb
findings:
- finding_id: rec-f-5f0413eed13438e8
  issue_key: mim-reconciliation-role-support-1eaa6d3513b9e617
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Glutaric acid'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-1eaa6d3513b9e617
  evidence_ids:
  - ev-967baf2ce9d63e79
  - ev-2545873977cfcddb
  - ev-87dc715fbde89644
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glutaric_Acid.yaml
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
    review_id: 20261011T024634Z-mim-reconcile-all-batch-06
    finding_id: f-5f0413eed13438e8
actions:
- action_id: rec-action-5f0413eed13438e8
  description: 'Reassess prediction-only role support: Glutaric acid'
  finding_ids:
  - rec-f-5f0413eed13438e8
  target_ids:
  - record-1eaa6d3513b9e617
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glutaric_Acid.yaml
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
  with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.
```
