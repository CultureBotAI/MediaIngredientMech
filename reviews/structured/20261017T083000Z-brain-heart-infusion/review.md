# Per-record structured review: Brain_Heart_Infusion (data/ingredients/mapped/Brain_Heart_Infusion.yaml)

- Review: 20261017T083000Z-brain-heart-infusion
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Brain_Heart_Infusion (data/ingredients/mapped/Brain_Heart_Infusion.yaml, record-fdd125cd992766e5, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Brain_Heart_Infusion.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Brain_Heart_Infusion.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-fdd125cd992766e5 | data/ingredients/mapped/Brain_Heart_Infusion.yaml | maintained | Brain_Heart_Infusion |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-fdd125cd992766e5 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-fdd125cd992766e5 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-fdd125cd992766e5 | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-fdd125cd992766e5.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-fdd125cd992766e5.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T10:10:47Z; reviewed SHA-256=77230cb3783ad3fbeb96695e96958441f8d0c9ac6f5a9595ac1816a72b7d86d8; current SHA-256=77230cb3783ad3fbeb96695e96958441f8d0c9ac6f5a9595ac1816a72b7d86d8; hash_changed=False. Reports=["reports/yaml_record_review/Brain_Heart_Infusion.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact MICRO brain heart infusion identity, mixture classification, protein-source role, occurrence count, SSSOM row, and aggregate copy pass, but top-level notes are stale.

### Historical provisional-role concern

evidence: concern. Targets: record-fdd125cd992766e5.

Current role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence lists and require source-backed curation support.

## Findings

### rec-f-role-fdd125cd992766e5: Reassess prediction-only or empty role support: Brain_Heart_Infusion

major / open / confirmed; issue key: mim-reconciliation-role-support-fdd125cd992766e5.

Prediction-only or empty evidence payloads remain on the named current role assertions (nutritional_roles[0]). This confirms the local evidence gap, not that the biological role is false.

## Recommended Actions And Acceptance Checks

### rec-act-role-fdd125cd992766e5

Reassess prediction-only or empty role support: Brain_Heart_Infusion

- Address the exact role fields and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-f1e9279d3cf9222d | data/ingredients/mapped/Brain_Heart_Infusion.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[601],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0000193","line":603,"mapping_status":"MAPPED","ontology_id":"MICRO:0000193","preferred_term":"Brain heart infusion"}],"identifier":"MICRO:0000193","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":29,"edge_count":29,"occurrences":29},"occurrence_statistics":{"media_count":29,"total_occurrences":29},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"MICRO:0000193","ontology_label":"brain heart infusion","ontology_source":"MICRO"},"preferred_term":"Brain heart infusion","sssom_rows":[{"data_row":577,"object_id":"MICRO:0000193","object_label":"brain heart infusion","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Brain_Heart_Infusion","synonym_count":1} |
| ev-0f5e7430dfda8972 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [601] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-768f4b1077bc3a01 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Brain_Heart_Infusion; data-row positions=[577] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":577,"object_id":"MICRO:0000193","object_label":"brain heart infusion","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Brain_Heart_Infusion","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-573043ce42402161 | docs/data/mapped_ingredients.csv; CSV lines=[603] | supports | Published identity and count rows inspected: [{"identifier":"MICRO:0000193","line":603,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"29","ontology_id":"MICRO:0000193","preferred_term":"Brain heart infusion","total_occurrences":"29"}] |
| ev-dc303e2fca3aa1f4 | reports/yaml_record_review/Brain_Heart_Infusion.md; &#96;data/ingredients/mapped/Brain_Heart_Infusion.yaml&#96;:2; Verdict:4; Identity:11; Validation:23; Evidence:34; Completeness:52; Recommended Edits:61 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-b8376941eed960d2 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[330,1964] | context_only | [{"current_record_sha256":"77230cb3783ad3fbeb96695e96958441f8d0c9ac6f5a9595ac1816a72b7d86d8","finding_id":"SEM:bed84a5d58b8a3164047","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"77230cb3783ad3fbeb96695e96958441f8d0c9ac6f5a9595ac1816a72b7d86d8","finding_id":"SEM:6303432bac4ce558acb6","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-brain-heart-infusion
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Brain_Heart_Infusion (data/ingredients/mapped/Brain_Heart_Infusion.yaml)'
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
summary: Per-record structured review for Brain_Heart_Infusion (data/ingredients/mapped/Brain_Heart_Infusion.yaml,
  record-fdd125cd992766e5, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Brain_Heart_Infusion.yaml
    sha256: 77230cb3783ad3fbeb96695e96958441f8d0c9ac6f5a9595ac1816a72b7d86d8
    role: target
  - path: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
    sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
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
  - path: reports/yaml_record_review/Brain_Heart_Infusion.md
    sha256: dccbe8fb15a4518101ed330fda276763eb870ba5f8cd2091bbf55b5d5806e07c
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-fdd125cd992766e5
  path: data/ingredients/mapped/Brain_Heart_Infusion.yaml
  label: Brain_Heart_Infusion
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Brain_Heart_Infusion.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Brain_Heart_Infusion.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Brain_Heart_Infusion.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-fdd125cd992766e5
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-fdd125cd992766e5
  evidence_ids:
  - ev-f1e9279d3cf9222d
  - ev-0f5e7430dfda8972
  - ev-768f4b1077bc3a01
  - ev-573043ce42402161
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-fdd125cd992766e5
  evidence_ids:
  - ev-f1e9279d3cf9222d
  - ev-b8376941eed960d2
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-fdd125cd992766e5
  evidence_ids:
  - ev-dc303e2fca3aa1f4
  - ev-b8376941eed960d2
evidence:
- evidence_id: ev-f1e9279d3cf9222d
  kind: record_content
  reference: data/ingredients/mapped/Brain_Heart_Infusion.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[601],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0000193","line":603,"mapping_status":"MAPPED","ontology_id":"MICRO:0000193","preferred_term":"Brain
    heart infusion"}],"identifier":"MICRO:0000193","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":29,"edge_count":29,"occurrences":29},"occurrence_statistics":{"media_count":29,"total_occurrences":29},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"MICRO:0000193","ontology_label":"brain
    heart infusion","ontology_source":"MICRO"},"preferred_term":"Brain heart infusion","sssom_rows":[{"data_row":577,"object_id":"MICRO:0000193","object_label":"brain
    heart infusion","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Brain_Heart_Infusion","synonym_count":1}'
  snapshot_sha256: 77230cb3783ad3fbeb96695e96958441f8d0c9ac6f5a9595ac1816a72b7d86d8
- evidence_id: ev-0f5e7430dfda8972
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [601]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-768f4b1077bc3a01
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Brain_Heart_Infusion; data-row positions=[577]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":577,"object_id":"MICRO:0000193","object_label":"brain
    heart infusion","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Brain_Heart_Infusion","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-573043ce42402161
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[603]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"MICRO:0000193","line":603,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"29","ontology_id":"MICRO:0000193","preferred_term":"Brain
    heart infusion","total_occurrences":"29"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-dc303e2fca3aa1f4
  kind: prior_review
  reference: reports/yaml_record_review/Brain_Heart_Infusion.md
  locator: '`data/ingredients/mapped/Brain_Heart_Infusion.yaml`:2; Verdict:4; Identity:11;
    Validation:23; Evidence:34; Completeness:52; Recommended Edits:61'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: dccbe8fb15a4518101ed330fda276763eb870ba5f8cd2091bbf55b5d5806e07c
  quote: "Recommended Edits:\n- Minor: replace the stale import note in\n  `data/ingredients/mapped/Brain_Heart_Infusion.yaml`\
    \ with a current note\n  naming the accepted MICRO mapping, then run `just sync-curated`\
    \ and focused\n  strict validation."
- evidence_id: ev-b8376941eed960d2
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[330,1964]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"77230cb3783ad3fbeb96695e96958441f8d0c9ac6f5a9595ac1816a72b7d86d8","finding_id":"SEM:bed84a5d58b8a3164047","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"77230cb3783ad3fbeb96695e96958441f8d0c9ac6f5a9595ac1816a72b7d86d8","finding_id":"SEM:6303432bac4ce558acb6","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-df9a9c2343b13022
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-fdd125cd992766e5
  evidence_ids:
  - ev-f1e9279d3cf9222d
  - ev-0f5e7430dfda8972
  - ev-768f4b1077bc3a01
  - ev-573043ce42402161
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-948b1a907eb07260
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-fdd125cd992766e5
  evidence_ids:
  - ev-dc303e2fca3aa1f4
  - ev-f1e9279d3cf9222d
  - ev-b8376941eed960d2
  details: 'Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T10:10:47Z;
    reviewed SHA-256=77230cb3783ad3fbeb96695e96958441f8d0c9ac6f5a9595ac1816a72b7d86d8;
    current SHA-256=77230cb3783ad3fbeb96695e96958441f8d0c9ac6f5a9595ac1816a72b7d86d8;
    hash_changed=False. Reports=["reports/yaml_record_review/Brain_Heart_Infusion.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    MICRO brain heart infusion identity, mixture classification, protein-source role,
    occurrence count, SSSOM row, and aggregate copy pass, but top-level notes are
    stale.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-dc303e2fca3aa1f4
    - ev-f1e9279d3cf9222d
  - name: legacy-native-ids
    value: '["SEM:bed84a5d58b8a3164047","SEM:6303432bac4ce558acb6"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-f1e9279d3cf9222d
    - ev-dc303e2fca3aa1f4
    - ev-b8376941eed960d2
- assessment_id: a-role-fdd125cd992766e5
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Current role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence lists and require source-backed curation support.
  target_ids:
  - record-fdd125cd992766e5
  evidence_ids:
  - ev-f1e9279d3cf9222d
  - ev-b8376941eed960d2
  dimensions:
  - name: legacy-disposition
    value: still_present
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f1e9279d3cf9222d
    - ev-b8376941eed960d2
findings:
- finding_id: rec-f-role-fdd125cd992766e5
  issue_key: mim-reconciliation-role-support-fdd125cd992766e5
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only or empty role support: Brain_Heart_Infusion'
  description: Prediction-only or empty evidence payloads remain on the named current
    role assertions (nutritional_roles[0]). This confirms the local evidence gap,
    not that the biological role is false.
  target_ids:
  - record-fdd125cd992766e5
  evidence_ids:
  - ev-f1e9279d3cf9222d
  - ev-b8376941eed960d2
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Brain_Heart_Infusion.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
actions:
- action_id: rec-act-role-fdd125cd992766e5
  description: 'Reassess prediction-only or empty role support: Brain_Heart_Infusion'
  finding_ids:
  - rec-f-role-fdd125cd992766e5
  target_ids:
  - record-fdd125cd992766e5
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Brain_Heart_Infusion.yaml
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
  with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.
```
