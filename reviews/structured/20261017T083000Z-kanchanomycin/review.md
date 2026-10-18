# Per-record structured review: Kanchanomycin (data/ingredients/mapped/Kanchanomycin.yaml)

- Review: 20261017T083000Z-kanchanomycin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Kanchanomycin (data/ingredients/mapped/Kanchanomycin.yaml, record-c49ea0051aba4657, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Kanchanomycin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Kanchanomycin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-c49ea0051aba4657 | data/ingredients/mapped/Kanchanomycin.yaml | maintained | Kanchanomycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-c49ea0051aba4657 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-c49ea0051aba4657 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-c49ea0051aba4657 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-c49ea0051aba4657.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-c49ea0051aba4657.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T21:26:49Z; reviewed SHA-256=d9032dcd0d962b99b0131a8eb6dfd1f6ba4fbfe80dc6d4e18b8eda8ac624babd; current SHA-256=d9032dcd0d962b99b0131a8eb6dfd1f6ba4fbfe80dc6d4e18b8eda8ac624babd; hash_changed=False. Reports=["reports/yaml_record_review/Kanchanomycin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The label-exact MeSH kanchanomycin identity and final SSSOM row pass, but SELECTIVE_AGENT is only provisional name-pattern evidence.

### Historical provisional-role concern

evidence: concern. Targets: record-c49ea0051aba4657.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-a2caa81c25f85e67: Reassess prediction-only role support: Kanchanomycin

major / open / confirmed; issue key: mim-reconciliation-role-support-c49ea0051aba4657.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-a2caa81c25f85e67

Reassess prediction-only role support: Kanchanomycin

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-7ace5d7ee03006e1 | data/ingredients/mapped/Kanchanomycin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1195],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C001493","line":1197,"mapping_status":"MAPPED","ontology_id":"mesh:C001493","preferred_term":"Kanchanomycin"}],"identifier":"mesh:C001493","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C001493","ontology_label":"kanchanomycin","ontology_source":"MESH"},"preferred_term":"Kanchanomycin","sssom_rows":[{"data_row":1537,"object_id":"mesh:C001493","object_label":"kanchanomycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Kanchanomycin","synonym_count":0} |
| ev-3c55ae73869ae42a | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1195] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-f2ad675ec7daefbc | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Kanchanomycin; data-row positions=[1537] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1537,"object_id":"mesh:C001493","object_label":"kanchanomycin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Kanchanomycin","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-cb752d1feffe7465 | docs/data/mapped_ingredients.csv; CSV lines=[1197] | supports | Published identity and count rows inspected: [{"identifier":"mesh:C001493","line":1197,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C001493","preferred_term":"Kanchanomycin","total_occurrences":"0"}] |
| ev-8281826aca5be749 | reports/yaml_record_review/Kanchanomycin.md; &#96;data/ingredients/mapped/Kanchanomycin.yaml&#96;:2; Verdict:4; Identity:10; Validation:20; Evidence:31; Completeness:51; Recommended Edits:58 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-5c6a81f2d85e7b38 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[767,1882] | context_only | [{"current_record_sha256":"d9032dcd0d962b99b0131a8eb6dfd1f6ba4fbfe80dc6d4e18b8eda8ac624babd","finding_id":"SEM:bda02f264ccf13f54e86","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"d9032dcd0d962b99b0131a8eb6dfd1f6ba4fbfe80dc6d4e18b8eda8ac624babd","finding_id":"SEM:e75a14faed5f822cda26","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-b4d852e62da1f645 | data/ingredients/mapped/Kanchanomycin.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1195],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C001493","line":1197,"mapping_status":"MAPPED","ontology_id":"mesh:C001493","preferred_term":"Kanchanomycin"}],"identifier":"mesh:C001493","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C001493","ontology_label":"kanchanomycin","ontology_source":"MESH"},"preferred_term":"Kanchanomycin","sssom_rows":[{"data_row":1537,"object_id":"mesh:C001493","object_label":"kanchanomycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Kanchanomycin","synonym_count":0} |
| ev-87009fb6a49c5d60 | reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml; findings[finding_id=f-a2caa81c25f85e67] | context_only | Predecessor structured review finding f-a2caa81c25f85e67 in 20261011T024635Z-mim-reconcile-all-batch-07 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-kanchanomycin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Kanchanomycin (data/ingredients/mapped/Kanchanomycin.yaml)'
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
summary: Per-record structured review for Kanchanomycin (data/ingredients/mapped/Kanchanomycin.yaml,
  record-c49ea0051aba4657, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Kanchanomycin.yaml
    sha256: d9032dcd0d962b99b0131a8eb6dfd1f6ba4fbfe80dc6d4e18b8eda8ac624babd
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
  - path: reports/yaml_record_review/Kanchanomycin.md
    sha256: c6a13d0d1e04d51d4fe28c2aa3f6098dc71e228c6f8c543622d1d72e755f09ab
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-c49ea0051aba4657
  path: data/ingredients/mapped/Kanchanomycin.yaml
  label: Kanchanomycin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Kanchanomycin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Kanchanomycin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Kanchanomycin.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-c49ea0051aba4657
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-c49ea0051aba4657
  evidence_ids:
  - ev-7ace5d7ee03006e1
  - ev-3c55ae73869ae42a
  - ev-f2ad675ec7daefbc
  - ev-cb752d1feffe7465
  - ev-b4d852e62da1f645
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-c49ea0051aba4657
  evidence_ids:
  - ev-7ace5d7ee03006e1
  - ev-5c6a81f2d85e7b38
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-c49ea0051aba4657
  evidence_ids:
  - ev-8281826aca5be749
  - ev-5c6a81f2d85e7b38
  - ev-87009fb6a49c5d60
evidence:
- evidence_id: ev-7ace5d7ee03006e1
  kind: record_content
  reference: data/ingredients/mapped/Kanchanomycin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1195],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C001493","line":1197,"mapping_status":"MAPPED","ontology_id":"mesh:C001493","preferred_term":"Kanchanomycin"}],"identifier":"mesh:C001493","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C001493","ontology_label":"kanchanomycin","ontology_source":"MESH"},"preferred_term":"Kanchanomycin","sssom_rows":[{"data_row":1537,"object_id":"mesh:C001493","object_label":"kanchanomycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Kanchanomycin","synonym_count":0}'
  snapshot_sha256: d9032dcd0d962b99b0131a8eb6dfd1f6ba4fbfe80dc6d4e18b8eda8ac624babd
- evidence_id: ev-3c55ae73869ae42a
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1195]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-f2ad675ec7daefbc
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Kanchanomycin; data-row positions=[1537]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1537,"object_id":"mesh:C001493","object_label":"kanchanomycin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Kanchanomycin","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-cb752d1feffe7465
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1197]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"mesh:C001493","line":1197,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C001493","preferred_term":"Kanchanomycin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-8281826aca5be749
  kind: prior_review
  reference: reports/yaml_record_review/Kanchanomycin.md
  locator: '`data/ingredients/mapped/Kanchanomycin.yaml`:2; Verdict:4; Identity:10;
    Validation:20; Evidence:31; Completeness:51; Recommended Edits:58'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: c6a13d0d1e04d51d4fe28c2aa3f6098dc71e228c6f8c543622d1d72e755f09ab
  quote: "Recommended Edits:\n- Major: remove `physicochemical_roles.SELECTIVE_AGENT`\
    \ unless an inspected\n  CultureMech, FEBA, Hans80, or literature source can support\
    \ kanchanomycin as a\n  selective agent, then rerun strict, term, round-trip,\
    \ component, and SSSOM\n  validation."
- evidence_id: ev-5c6a81f2d85e7b38
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[767,1882]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"d9032dcd0d962b99b0131a8eb6dfd1f6ba4fbfe80dc6d4e18b8eda8ac624babd","finding_id":"SEM:bda02f264ccf13f54e86","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"d9032dcd0d962b99b0131a8eb6dfd1f6ba4fbfe80dc6d4e18b8eda8ac624babd","finding_id":"SEM:e75a14faed5f822cda26","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-b4d852e62da1f645
  kind: record_content
  reference: data/ingredients/mapped/Kanchanomycin.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1195],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C001493","line":1197,"mapping_status":"MAPPED","ontology_id":"mesh:C001493","preferred_term":"Kanchanomycin"}],"identifier":"mesh:C001493","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C001493","ontology_label":"kanchanomycin","ontology_source":"MESH"},"preferred_term":"Kanchanomycin","sssom_rows":[{"data_row":1537,"object_id":"mesh:C001493","object_label":"kanchanomycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Kanchanomycin","synonym_count":0}'
  snapshot_sha256: d9032dcd0d962b99b0131a8eb6dfd1f6ba4fbfe80dc6d4e18b8eda8ac624babd
- evidence_id: ev-87009fb6a49c5d60
  kind: prior_review
  reference: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
  locator: findings[finding_id=f-a2caa81c25f85e67]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-a2caa81c25f85e67 in 20261011T024635Z-mim-reconcile-all-batch-07
  snapshot_sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
assessments:
- assessment_id: a-e82aacd3a30d7e86
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-c49ea0051aba4657
  evidence_ids:
  - ev-7ace5d7ee03006e1
  - ev-3c55ae73869ae42a
  - ev-f2ad675ec7daefbc
  - ev-cb752d1feffe7465
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-1f302343f5460e4d
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-c49ea0051aba4657
  evidence_ids:
  - ev-8281826aca5be749
  - ev-7ace5d7ee03006e1
  - ev-5c6a81f2d85e7b38
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T21:26:49Z;
    reviewed SHA-256=d9032dcd0d962b99b0131a8eb6dfd1f6ba4fbfe80dc6d4e18b8eda8ac624babd;
    current SHA-256=d9032dcd0d962b99b0131a8eb6dfd1f6ba4fbfe80dc6d4e18b8eda8ac624babd;
    hash_changed=False. Reports=["reports/yaml_record_review/Kanchanomycin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The label-exact
    MeSH kanchanomycin identity and final SSSOM row pass, but SELECTIVE_AGENT is only
    provisional name-pattern evidence.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-8281826aca5be749
    - ev-7ace5d7ee03006e1
  - name: legacy-native-ids
    value: '["SEM:bda02f264ccf13f54e86","SEM:e75a14faed5f822cda26"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-7ace5d7ee03006e1
    - ev-8281826aca5be749
    - ev-5c6a81f2d85e7b38
- assessment_id: a-b4d852e62da1f645
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-c49ea0051aba4657
  evidence_ids:
  - ev-8281826aca5be749
  - ev-b4d852e62da1f645
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-8281826aca5be749
    - ev-b4d852e62da1f645
findings:
- finding_id: rec-f-a2caa81c25f85e67
  issue_key: mim-reconciliation-role-support-c49ea0051aba4657
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Kanchanomycin'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-c49ea0051aba4657
  evidence_ids:
  - ev-8281826aca5be749
  - ev-b4d852e62da1f645
  - ev-87009fb6a49c5d60
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Kanchanomycin.yaml
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
    finding_id: f-a2caa81c25f85e67
actions:
- action_id: rec-action-a2caa81c25f85e67
  description: 'Reassess prediction-only role support: Kanchanomycin'
  finding_ids:
  - rec-f-a2caa81c25f85e67
  target_ids:
  - record-c49ea0051aba4657
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Kanchanomycin.yaml
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
