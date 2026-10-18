# Per-record structured review: Beef_Heart (data/ingredients/mapped/Beef_Heart.yaml)

- Review: 20261017T083000Z-beef-heart
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Beef_Heart (data/ingredients/mapped/Beef_Heart.yaml, record-8f426816136432d7, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Beef_Heart.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Beef_Heart.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-8f426816136432d7 | data/ingredients/mapped/Beef_Heart.yaml | maintained | Beef_Heart |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-8f426816136432d7 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-8f426816136432d7 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-8f426816136432d7 | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-8f426816136432d7.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-8f426816136432d7.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T09:26:42Z; reviewed SHA-256=ca7de3785bc0a6469a5d60f48de97a49c0c7e460ea11d801bfe6367b1e76dc34; current SHA-256=ca7de3785bc0a6469a5d60f48de97a49c0c7e460ea11d801bfe6367b1e76dc34; hash_changed=False. Reports=["reports/yaml_record_review/Beef_Heart.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact FOODON beef heart mapping, protein-source role, occurrence count, SSSOM row, and aggregate copy pass, but top-level notes still describe the old unmapped state.

### Historical provisional-role concern

evidence: concern. Targets: record-8f426816136432d7.

Current role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence lists and require source-backed curation support.

## Findings

### rec-f-role-8f426816136432d7: Reassess prediction-only or empty role support: Beef_Heart

major / open / confirmed; issue key: mim-reconciliation-role-support-8f426816136432d7.

Prediction-only or empty evidence payloads remain on the named current role assertions (nutritional_roles[0]). This confirms the local evidence gap, not that the biological role is false.

## Recommended Actions And Acceptance Checks

### rec-act-role-8f426816136432d7

Reassess prediction-only or empty role support: Beef_Heart

- Address the exact role fields and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-1d3a701a83ac993a | data/ingredients/mapped/Beef_Heart.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[564],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:00004410","line":566,"mapping_status":"MAPPED","ontology_id":"FOODON:00004410","preferred_term":"Beef heart"}],"identifier":"FOODON:00004410","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":164,"edge_count":164,"occurrences":164},"occurrence_statistics":{"media_count":164,"total_occurrences":164},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"FOODON:00004410","ontology_label":"beef heart","ontology_source":"FOODON"},"preferred_term":"Beef heart","sssom_rows":[{"data_row":499,"object_id":"FOODON:00004410","object_label":"beef heart","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Beef_Heart","synonym_count":1} |
| ev-6d0f8de4a8de4604 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [564] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-208fe7cfce0ecbd5 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Beef_Heart; data-row positions=[499] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":499,"object_id":"FOODON:00004410","object_label":"beef heart","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Beef_Heart","validation_method":"OLS:foodon&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-5956813a5c4786ec | docs/data/mapped_ingredients.csv; CSV lines=[566] | supports | Published identity and count rows inspected: [{"identifier":"FOODON:00004410","line":566,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"164","ontology_id":"FOODON:00004410","preferred_term":"Beef heart","total_occurrences":"164"}] |
| ev-ef6cda82e611246d | reports/yaml_record_review/Beef_Heart.md; &#96;data/ingredients/mapped/Beef_Heart.yaml&#96;:2; Verdict:4; Identity:11; Validation:22; Evidence:32; Completeness:48; Recommended Edits:55 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-e3d354ad61e08d6e | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[299,1667] | context_only | [{"current_record_sha256":"ca7de3785bc0a6469a5d60f48de97a49c0c7e460ea11d801bfe6367b1e76dc34","finding_id":"SEM:d4cd4b05059655dd6b43","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"ca7de3785bc0a6469a5d60f48de97a49c0c7e460ea11d801bfe6367b1e76dc34","finding_id":"SEM:4411b2f3b0f3d25f01da","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-3c458356ccde1e7d | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; current_record=data/ingredients/mapped/Beef_Heart.yaml | context_only | Semantic review finding dispositions ledger |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-beef-heart
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Beef_Heart (data/ingredients/mapped/Beef_Heart.yaml)'
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
summary: Per-record structured review for Beef_Heart (data/ingredients/mapped/Beef_Heart.yaml,
  record-8f426816136432d7, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Beef_Heart.yaml
    sha256: ca7de3785bc0a6469a5d60f48de97a49c0c7e460ea11d801bfe6367b1e76dc34
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
  - path: reports/yaml_record_review/Beef_Heart.md
    sha256: decd6c92acc780c9d6ac3f466919dee56d29a8ca0d159c8b0eb7c3367d1fd95e
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-8f426816136432d7
  path: data/ingredients/mapped/Beef_Heart.yaml
  label: Beef_Heart
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Beef_Heart.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Beef_Heart.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Beef_Heart.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-8f426816136432d7
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-8f426816136432d7
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-8f426816136432d7
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-8f426816136432d7
evidence:
- evidence_id: ev-1d3a701a83ac993a
  kind: record_content
  reference: data/ingredients/mapped/Beef_Heart.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[564],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:00004410","line":566,"mapping_status":"MAPPED","ontology_id":"FOODON:00004410","preferred_term":"Beef
    heart"}],"identifier":"FOODON:00004410","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":164,"edge_count":164,"occurrences":164},"occurrence_statistics":{"media_count":164,"total_occurrences":164},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"FOODON:00004410","ontology_label":"beef
    heart","ontology_source":"FOODON"},"preferred_term":"Beef heart","sssom_rows":[{"data_row":499,"object_id":"FOODON:00004410","object_label":"beef
    heart","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Beef_Heart","synonym_count":1}'
  snapshot_sha256: ca7de3785bc0a6469a5d60f48de97a49c0c7e460ea11d801bfe6367b1e76dc34
- evidence_id: ev-6d0f8de4a8de4604
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [564]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-208fe7cfce0ecbd5
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Beef_Heart; data-row positions=[499]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":499,"object_id":"FOODON:00004410","object_label":"beef
    heart","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Beef_Heart","validation_method":"OLS:foodon|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-5956813a5c4786ec
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[566]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"FOODON:00004410","line":566,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"164","ontology_id":"FOODON:00004410","preferred_term":"Beef
    heart","total_occurrences":"164"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-ef6cda82e611246d
  kind: prior_review
  reference: reports/yaml_record_review/Beef_Heart.md
  locator: '`data/ingredients/mapped/Beef_Heart.yaml`:2; Verdict:4; Identity:11; Validation:22;
    Evidence:32; Completeness:48; Recommended Edits:55'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: decd6c92acc780c9d6ac3f466919dee56d29a8ca0d159c8b0eb7c3367d1fd95e
  quote: "Recommended Edits:\n- Minor: update `notes` in `data/ingredients/mapped/Beef_Heart.yaml`\
    \ to\n  describe the current exact FOODON mapping and refreshed CultureMech occurrence\n\
    \  count, then run `just sync-curated`."
- evidence_id: ev-e3d354ad61e08d6e
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[299,1667]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"ca7de3785bc0a6469a5d60f48de97a49c0c7e460ea11d801bfe6367b1e76dc34","finding_id":"SEM:d4cd4b05059655dd6b43","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"ca7de3785bc0a6469a5d60f48de97a49c0c7e460ea11d801bfe6367b1e76dc34","finding_id":"SEM:4411b2f3b0f3d25f01da","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-3c458356ccde1e7d
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: current_record=data/ingredients/mapped/Beef_Heart.yaml
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Semantic review finding dispositions ledger
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-68bb588508e2aab3
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-8f426816136432d7
  evidence_ids:
  - ev-1d3a701a83ac993a
  - ev-6d0f8de4a8de4604
  - ev-208fe7cfce0ecbd5
  - ev-5956813a5c4786ec
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-df9c5bc0051f925c
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-8f426816136432d7
  evidence_ids:
  - ev-ef6cda82e611246d
  - ev-1d3a701a83ac993a
  - ev-e3d354ad61e08d6e
  details: 'Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T09:26:42Z;
    reviewed SHA-256=ca7de3785bc0a6469a5d60f48de97a49c0c7e460ea11d801bfe6367b1e76dc34;
    current SHA-256=ca7de3785bc0a6469a5d60f48de97a49c0c7e460ea11d801bfe6367b1e76dc34;
    hash_changed=False. Reports=["reports/yaml_record_review/Beef_Heart.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact FOODON
    beef heart mapping, protein-source role, occurrence count, SSSOM row, and aggregate
    copy pass, but top-level notes still describe the old unmapped state.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ef6cda82e611246d
    - ev-1d3a701a83ac993a
  - name: legacy-native-ids
    value: '["SEM:d4cd4b05059655dd6b43","SEM:4411b2f3b0f3d25f01da"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-1d3a701a83ac993a
    - ev-ef6cda82e611246d
    - ev-e3d354ad61e08d6e
- assessment_id: a-role-8f426816136432d7
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Current role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence lists and require source-backed curation support.
  target_ids:
  - record-8f426816136432d7
  evidence_ids:
  - ev-1d3a701a83ac993a
  - ev-3c458356ccde1e7d
  dimensions:
  - name: legacy-disposition
    value: still_present
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-1d3a701a83ac993a
    - ev-3c458356ccde1e7d
findings:
- finding_id: rec-f-role-8f426816136432d7
  issue_key: mim-reconciliation-role-support-8f426816136432d7
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only or empty role support: Beef_Heart'
  description: Prediction-only or empty evidence payloads remain on the named current
    role assertions (nutritional_roles[0]). This confirms the local evidence gap,
    not that the biological role is false.
  target_ids:
  - record-8f426816136432d7
  evidence_ids:
  - ev-1d3a701a83ac993a
  - ev-3c458356ccde1e7d
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Beef_Heart.yaml
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
- action_id: rec-act-role-8f426816136432d7
  description: 'Reassess prediction-only or empty role support: Beef_Heart'
  finding_ids:
  - rec-f-role-8f426816136432d7
  target_ids:
  - record-8f426816136432d7
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Beef_Heart.yaml
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
