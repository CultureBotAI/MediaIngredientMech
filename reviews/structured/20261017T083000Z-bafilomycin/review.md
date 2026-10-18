# Per-record structured review: Bafilomycin (data/ingredients/mapped/Bafilomycin.yaml)

- Review: 20261017T083000Z-bafilomycin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Bafilomycin (data/ingredients/mapped/Bafilomycin.yaml, record-80f972d0309e79b4, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Bafilomycin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Bafilomycin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-80f972d0309e79b4 | data/ingredients/mapped/Bafilomycin.yaml | maintained | Bafilomycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-80f972d0309e79b4 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-80f972d0309e79b4 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-80f972d0309e79b4 | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-80f972d0309e79b4.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: not_applicable. Targets: record-80f972d0309e79b4.

The latest legacy review reports no outstanding finding. This run verifies local consistency only; it does not renew that earlier scientific pass.

Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-16T09:19:41Z; reviewed SHA-256=814a39a9689c6c97da65641128be5a32918c4ea61e95c8f9307aba7dfc376773; current SHA-256=814a39a9689c6c97da65641128be5a32918c4ea61e95c8f9307aba7dfc376773; hash_changed=False. Reports=["reports/yaml_record_review/Bafilomycin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The kgmicrobe.compound placeholder is intentionally retained because the OLS candidates were specific variants, not exact identity for the family label.

### Historical provisional-role concern

evidence: concern. Targets: record-80f972d0309e79b4.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-db5a6bdf7029bfba: Reassess prediction-only role support: Bafilomycin

major / open / confirmed; issue key: mim-reconciliation-role-support-80f972d0309e79b4.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-db5a6bdf7029bfba

Reassess prediction-only role support: Bafilomycin

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-30eb941935c9759f | data/ingredients/mapped/Bafilomycin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[553],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:bafilomycin","line":555,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:bafilomycin","preferred_term":"Bafilomycin"}],"identifier":"kgmicrobe.compound:bafilomycin","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:bafilomycin","ontology_label":"Bafilomycin","ontology_source":"kgmicrobe.compound"},"preferred_term":"Bafilomycin","sssom_rows":[{"data_row":483,"object_id":"kgmicrobe.compound:bafilomycin","object_label":"Bafilomycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Bafilomycin","synonym_count":0} |
| ev-afcd6bfdadca89ad | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [553] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-59ebc350fbc11ea3 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Bafilomycin; data-row positions=[483] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":483,"object_id":"kgmicrobe.compound:bafilomycin","object_label":"Bafilomycin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Bafilomycin","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-eac5e91b1df17514 | docs/data/mapped_ingredients.csv; CSV lines=[555] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:bafilomycin","line":555,"mapping_quality":"PLACEHOLDER","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.compound:bafilomycin","preferred_term":"Bafilomycin","total_occurrences":"0"}] |
| ev-77711b8951931d87 | reports/yaml_record_review/Bafilomycin.md; &#96;data/ingredients/mapped/Bafilomycin.yaml&#96;:2; Verdict:4; Identity:10; Validation:25; Evidence:36; Completeness:55; Recommended Edits:62 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-77e8e33b7939f49c | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1938] | context_only | [{"current_record_sha256":"814a39a9689c6c97da65641128be5a32918c4ea61e95c8f9307aba7dfc376773","finding_id":"SEM:8c954ef87e091bdae730","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-3b21a505fd533d8d | data/ingredients/mapped/Bafilomycin.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[553],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:bafilomycin","line":555,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:bafilomycin","preferred_term":"Bafilomycin"}],"identifier":"kgmicrobe.compound:bafilomycin","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:bafilomycin","ontology_label":"Bafilomycin","ontology_source":"kgmicrobe.compound"},"preferred_term":"Bafilomycin","sssom_rows":[{"data_row":483,"object_id":"kgmicrobe.compound:bafilomycin","object_label":"Bafilomycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Bafilomycin","synonym_count":0} |
| ev-3c13da496bc959a8 | reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml; findings[finding_id=f-db5a6bdf7029bfba] | context_only | Predecessor structured review finding f-db5a6bdf7029bfba in 20261011T024631Z-mim-reconcile-all-batch-03 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-bafilomycin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Bafilomycin (data/ingredients/mapped/Bafilomycin.yaml)'
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
summary: Per-record structured review for Bafilomycin (data/ingredients/mapped/Bafilomycin.yaml,
  record-80f972d0309e79b4, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Bafilomycin.yaml
    sha256: 814a39a9689c6c97da65641128be5a32918c4ea61e95c8f9307aba7dfc376773
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
  - path: reports/yaml_record_review/Bafilomycin.md
    sha256: 69c2e69ac0be4b1bab1ac4c51072e15aea4716050e2eee465f5e7c75c0aac311
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-80f972d0309e79b4
  path: data/ingredients/mapped/Bafilomycin.yaml
  label: Bafilomycin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bafilomycin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Bafilomycin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Bafilomycin.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-80f972d0309e79b4
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-80f972d0309e79b4
  evidence_ids:
  - ev-30eb941935c9759f
  - ev-afcd6bfdadca89ad
  - ev-59ebc350fbc11ea3
  - ev-eac5e91b1df17514
  - ev-3b21a505fd533d8d
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-80f972d0309e79b4
  evidence_ids:
  - ev-30eb941935c9759f
  - ev-77e8e33b7939f49c
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-80f972d0309e79b4
  evidence_ids:
  - ev-77711b8951931d87
  - ev-77e8e33b7939f49c
  - ev-3c13da496bc959a8
evidence:
- evidence_id: ev-30eb941935c9759f
  kind: record_content
  reference: data/ingredients/mapped/Bafilomycin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[553],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:bafilomycin","line":555,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:bafilomycin","preferred_term":"Bafilomycin"}],"identifier":"kgmicrobe.compound:bafilomycin","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:bafilomycin","ontology_label":"Bafilomycin","ontology_source":"kgmicrobe.compound"},"preferred_term":"Bafilomycin","sssom_rows":[{"data_row":483,"object_id":"kgmicrobe.compound:bafilomycin","object_label":"Bafilomycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Bafilomycin","synonym_count":0}'
  snapshot_sha256: 814a39a9689c6c97da65641128be5a32918c4ea61e95c8f9307aba7dfc376773
- evidence_id: ev-afcd6bfdadca89ad
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [553]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-59ebc350fbc11ea3
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Bafilomycin; data-row positions=[483]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":483,"object_id":"kgmicrobe.compound:bafilomycin","object_label":"Bafilomycin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Bafilomycin","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-eac5e91b1df17514
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[555]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:bafilomycin","line":555,"mapping_quality":"PLACEHOLDER","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.compound:bafilomycin","preferred_term":"Bafilomycin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-77711b8951931d87
  kind: prior_review
  reference: reports/yaml_record_review/Bafilomycin.md
  locator: '`data/ingredients/mapped/Bafilomycin.yaml`:2; Verdict:4; Identity:10;
    Validation:25; Evidence:36; Completeness:55; Recommended Edits:62'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 69c2e69ac0be4b1bab1ac4c51072e15aea4716050e2eee465f5e7c75c0aac311
  quote: 'Recommended Edits:

    - None.'
- evidence_id: ev-77e8e33b7939f49c
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1938]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"814a39a9689c6c97da65641128be5a32918c4ea61e95c8f9307aba7dfc376773","finding_id":"SEM:8c954ef87e091bdae730","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-3b21a505fd533d8d
  kind: record_content
  reference: data/ingredients/mapped/Bafilomycin.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[553],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:bafilomycin","line":555,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:bafilomycin","preferred_term":"Bafilomycin"}],"identifier":"kgmicrobe.compound:bafilomycin","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:bafilomycin","ontology_label":"Bafilomycin","ontology_source":"kgmicrobe.compound"},"preferred_term":"Bafilomycin","sssom_rows":[{"data_row":483,"object_id":"kgmicrobe.compound:bafilomycin","object_label":"Bafilomycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Bafilomycin","synonym_count":0}'
  snapshot_sha256: 814a39a9689c6c97da65641128be5a32918c4ea61e95c8f9307aba7dfc376773
- evidence_id: ev-3c13da496bc959a8
  kind: prior_review
  reference: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
  locator: findings[finding_id=f-db5a6bdf7029bfba]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-db5a6bdf7029bfba in 20261011T024631Z-mim-reconcile-all-batch-03
  snapshot_sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
assessments:
- assessment_id: a-8d87805ffccd1455
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-80f972d0309e79b4
  evidence_ids:
  - ev-30eb941935c9759f
  - ev-afcd6bfdadca89ad
  - ev-59ebc350fbc11ea3
  - ev-eac5e91b1df17514
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-5456b83aa8a3d4c8
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: not_applicable
  summary: The latest legacy review reports no outstanding finding. This run verifies
    local consistency only; it does not renew that earlier scientific pass.
  target_ids:
  - record-80f972d0309e79b4
  evidence_ids:
  - ev-77711b8951931d87
  - ev-30eb941935c9759f
  - ev-77e8e33b7939f49c
  details: 'Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-16T09:19:41Z;
    reviewed SHA-256=814a39a9689c6c97da65641128be5a32918c4ea61e95c8f9307aba7dfc376773;
    current SHA-256=814a39a9689c6c97da65641128be5a32918c4ea61e95c8f9307aba7dfc376773;
    hash_changed=False. Reports=["reports/yaml_record_review/Bafilomycin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The kgmicrobe.compound
    placeholder is intentionally retained because the OLS candidates were specific
    variants, not exact identity for the family label.'
  dimensions:
  - name: legacy-native-ids
    value: '["SEM:8c954ef87e091bdae730"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-30eb941935c9759f
    - ev-77711b8951931d87
    - ev-77e8e33b7939f49c
- assessment_id: a-3b21a505fd533d8d
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-80f972d0309e79b4
  evidence_ids:
  - ev-77711b8951931d87
  - ev-3b21a505fd533d8d
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-77711b8951931d87
    - ev-3b21a505fd533d8d
findings:
- finding_id: rec-f-db5a6bdf7029bfba
  issue_key: mim-reconciliation-role-support-80f972d0309e79b4
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Bafilomycin'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-80f972d0309e79b4
  evidence_ids:
  - ev-77711b8951931d87
  - ev-3b21a505fd533d8d
  - ev-3c13da496bc959a8
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bafilomycin.yaml
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
    review_id: 20261011T024631Z-mim-reconcile-all-batch-03
    finding_id: f-db5a6bdf7029bfba
actions:
- action_id: rec-action-db5a6bdf7029bfba
  description: 'Reassess prediction-only role support: Bafilomycin'
  finding_ids:
  - rec-f-db5a6bdf7029bfba
  target_ids:
  - record-80f972d0309e79b4
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bafilomycin.yaml
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
  with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.
```
