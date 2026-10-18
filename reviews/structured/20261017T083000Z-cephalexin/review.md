# Per-record structured review: Cephalexin (data/ingredients/mapped/Cephalexin.yaml)

- Review: 20261017T083000Z-cephalexin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Cephalexin (data/ingredients/mapped/Cephalexin.yaml, record-635e7bc08e6388df, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Cephalexin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Cephalexin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-635e7bc08e6388df | data/ingredients/mapped/Cephalexin.yaml | maintained | Cephalexin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-635e7bc08e6388df | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-635e7bc08e6388df | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-635e7bc08e6388df | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-635e7bc08e6388df.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-635e7bc08e6388df.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T11:37:13Z; reviewed SHA-256=4dc424cb9b0db80ad99ec40766aedc81361bec4860f87bb87faf29ee4da378b7; current SHA-256=4dc424cb9b0db80ad99ec40766aedc81361bec4860f87bb87faf29ee4da378b7; hash_changed=False. Reports=["reports/yaml_record_review/Cephalexin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI cephalexin identity, structure fields, zero occurrence count, SSSOM row, and aggregate copy pass, but SELECTIVE_AGENT is only provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-635e7bc08e6388df.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-7dc641e69e24a8be: Reassess prediction-only role support: Cephalexin

major / open / confirmed; issue key: mim-reconciliation-role-support-635e7bc08e6388df.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-7dc641e69e24a8be

Reassess prediction-only role support: Cephalexin

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-f6fba6f5aa4c35aa | data/ingredients/mapped/Cephalexin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[691],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:3534","line":693,"mapping_status":"MAPPED","ontology_id":"CHEBI:3534","preferred_term":"Cephalexin"}],"identifier":"CHEBI:3534","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:3534","ontology_label":"cephalexin","ontology_source":"CHEBI"},"preferred_term":"Cephalexin","sssom_rows":[{"data_row":715,"object_id":"CHEBI:3534","object_label":"cephalexin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cephalexin","synonym_count":1} |
| ev-befd77c8f02c905a | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [691] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-62b4f6a52e0790ab | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Cephalexin; data-row positions=[715] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":715,"object_id":"CHEBI:3534","object_label":"cephalexin","other":"7beta-[(2R)-2-amino-2-phenylacetamido]-3-methyl-3,4-didehydrocepham-4-carboxylic acid&#124;CAS:15686-71-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Cephalexin","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-d42cf0b327951743 | docs/data/mapped_ingredients.csv; CSV lines=[693] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:3534","line":693,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:3534","preferred_term":"Cephalexin","total_occurrences":"0"}] |
| ev-6c33c22636544ac1 | reports/yaml_record_review/Cephalexin.md; &#96;data/ingredients/mapped/Cephalexin.yaml&#96;:2; Verdict:4; Identity:12; Validation:24; Evidence:39; Completeness:54; Recommended Edits:62 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-ddffd04b0e07d6cd | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[392,1584] | context_only | [{"current_record_sha256":"4dc424cb9b0db80ad99ec40766aedc81361bec4860f87bb87faf29ee4da378b7","finding_id":"SEM:9afa6d5122465546893b","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"4dc424cb9b0db80ad99ec40766aedc81361bec4860f87bb87faf29ee4da378b7","finding_id":"SEM:c9bb5cde6bf9dd43a200","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-b87bb9bd38b48ad9 | data/ingredients/mapped/Cephalexin.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}] |
| ev-32b6aa5026cd7cd2 | reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml; findings[finding_id=f-7dc641e69e24a8be] | context_only | Predecessor structured review finding f-7dc641e69e24a8be in 20261011T024632Z-mim-reconcile-all-batch-04 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-cephalexin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Cephalexin (data/ingredients/mapped/Cephalexin.yaml)'
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
summary: Per-record structured review for Cephalexin (data/ingredients/mapped/Cephalexin.yaml,
  record-635e7bc08e6388df, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Cephalexin.yaml
    sha256: 4dc424cb9b0db80ad99ec40766aedc81361bec4860f87bb87faf29ee4da378b7
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
  - path: reports/yaml_record_review/Cephalexin.md
    sha256: 16366df53cc8b6e6af7fa50e94f906d6825e094062c8c19813051970e967e7da
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-635e7bc08e6388df
  path: data/ingredients/mapped/Cephalexin.yaml
  label: Cephalexin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cephalexin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Cephalexin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Cephalexin.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-635e7bc08e6388df
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-635e7bc08e6388df
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-635e7bc08e6388df
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-635e7bc08e6388df
evidence:
- evidence_id: ev-f6fba6f5aa4c35aa
  kind: record_content
  reference: data/ingredients/mapped/Cephalexin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[691],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:3534","line":693,"mapping_status":"MAPPED","ontology_id":"CHEBI:3534","preferred_term":"Cephalexin"}],"identifier":"CHEBI:3534","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:3534","ontology_label":"cephalexin","ontology_source":"CHEBI"},"preferred_term":"Cephalexin","sssom_rows":[{"data_row":715,"object_id":"CHEBI:3534","object_label":"cephalexin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cephalexin","synonym_count":1}'
  snapshot_sha256: 4dc424cb9b0db80ad99ec40766aedc81361bec4860f87bb87faf29ee4da378b7
- evidence_id: ev-befd77c8f02c905a
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [691]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-62b4f6a52e0790ab
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Cephalexin; data-row positions=[715]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":715,"object_id":"CHEBI:3534","object_label":"cephalexin","other":"7beta-[(2R)-2-amino-2-phenylacetamido]-3-methyl-3,4-didehydrocepham-4-carboxylic
    acid|CAS:15686-71-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Cephalexin","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-d42cf0b327951743
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[693]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:3534","line":693,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:3534","preferred_term":"Cephalexin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-6c33c22636544ac1
  kind: prior_review
  reference: reports/yaml_record_review/Cephalexin.md
  locator: '`data/ingredients/mapped/Cephalexin.yaml`:2; Verdict:4; Identity:12; Validation:24;
    Evidence:39; Completeness:54; Recommended Edits:62'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 16366df53cc8b6e6af7fa50e94f906d6825e094062c8c19813051970e967e7da
  quote: "Recommended Edits:\n- Major: either replace `physicochemical_roles.SELECTIVE_AGENT`\
    \ with inspected\n  evidence for cephalexin as a selective agent in this media\
    \ scope, or remove\n  the role, then rerun strict validation, SSSOM QC, aggregate\
    \ roundtrip, and\n  `git diff --check`."
- evidence_id: ev-ddffd04b0e07d6cd
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[392,1584]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"4dc424cb9b0db80ad99ec40766aedc81361bec4860f87bb87faf29ee4da378b7","finding_id":"SEM:9afa6d5122465546893b","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"4dc424cb9b0db80ad99ec40766aedc81361bec4860f87bb87faf29ee4da378b7","finding_id":"SEM:c9bb5cde6bf9dd43a200","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-b87bb9bd38b48ad9
  kind: record_content
  reference: data/ingredients/mapped/Cephalexin.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}]'
  snapshot_sha256: 4dc424cb9b0db80ad99ec40766aedc81361bec4860f87bb87faf29ee4da378b7
- evidence_id: ev-32b6aa5026cd7cd2
  kind: prior_review
  reference: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
  locator: findings[finding_id=f-7dc641e69e24a8be]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-7dc641e69e24a8be in 20261011T024632Z-mim-reconcile-all-batch-04
  snapshot_sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
assessments:
- assessment_id: a-9ec1911cca40a29b
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-635e7bc08e6388df
  evidence_ids:
  - ev-f6fba6f5aa4c35aa
  - ev-befd77c8f02c905a
  - ev-62b4f6a52e0790ab
  - ev-d42cf0b327951743
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-0a29dcda26b35b68
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-635e7bc08e6388df
  evidence_ids:
  - ev-6c33c22636544ac1
  - ev-f6fba6f5aa4c35aa
  - ev-ddffd04b0e07d6cd
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T11:37:13Z;
    reviewed SHA-256=4dc424cb9b0db80ad99ec40766aedc81361bec4860f87bb87faf29ee4da378b7;
    current SHA-256=4dc424cb9b0db80ad99ec40766aedc81361bec4860f87bb87faf29ee4da378b7;
    hash_changed=False. Reports=["reports/yaml_record_review/Cephalexin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    cephalexin identity, structure fields, zero occurrence count, SSSOM row, and aggregate
    copy pass, but SELECTIVE_AGENT is only provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-6c33c22636544ac1
    - ev-f6fba6f5aa4c35aa
  - name: legacy-native-ids
    value: '["SEM:9afa6d5122465546893b","SEM:c9bb5cde6bf9dd43a200"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-f6fba6f5aa4c35aa
    - ev-6c33c22636544ac1
    - ev-ddffd04b0e07d6cd
- assessment_id: a-b87bb9bd38b48ad9
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-635e7bc08e6388df
  evidence_ids:
  - ev-6c33c22636544ac1
  - ev-b87bb9bd38b48ad9
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-6c33c22636544ac1
    - ev-b87bb9bd38b48ad9
findings:
- finding_id: rec-f-7dc641e69e24a8be
  issue_key: mim-reconciliation-role-support-635e7bc08e6388df
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Cephalexin'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-635e7bc08e6388df
  evidence_ids:
  - ev-6c33c22636544ac1
  - ev-b87bb9bd38b48ad9
  - ev-32b6aa5026cd7cd2
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cephalexin.yaml
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
    review_id: 20261011T024632Z-mim-reconcile-all-batch-04
    finding_id: f-7dc641e69e24a8be
actions:
- action_id: rec-action-7dc641e69e24a8be
  description: 'Reassess prediction-only role support: Cephalexin'
  finding_ids:
  - rec-f-7dc641e69e24a8be
  target_ids:
  - record-635e7bc08e6388df
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cephalexin.yaml
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
  with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.
```
