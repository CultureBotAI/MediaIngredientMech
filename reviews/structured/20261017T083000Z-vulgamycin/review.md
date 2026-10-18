# Per-record structured review: Vulgamycin (data/ingredients/mapped/Vulgamycin.yaml)

- Review: 20261017T083000Z-vulgamycin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Vulgamycin (data/ingredients/mapped/Vulgamycin.yaml, record-98948e989daadbb5, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Vulgamycin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Vulgamycin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-98948e989daadbb5 | data/ingredients/mapped/Vulgamycin.yaml | maintained | Vulgamycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-98948e989daadbb5 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-98948e989daadbb5 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-98948e989daadbb5 | Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-98948e989daadbb5.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-98948e989daadbb5.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:12:17Z; reviewed SHA-256=a602884e4b0ada6c719c9fb22b0e8163ead1943ff7c5abbd9ebdb4cfe2b50dbe; current SHA-256=a602884e4b0ada6c719c9fb22b0e8163ead1943ff7c5abbd9ebdb4cfe2b50dbe; hash_changed=False. Reports=["reports/yaml_record_review/Vulgamycin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact MeSH enterocin synonym identity passes, but SELECTIVE_AGENT is still a provisional name-pattern role.

### Historical provisional-role concern

evidence: concern. Targets: record-98948e989daadbb5.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-11ce4e4b85c2397a: Reassess prediction-only role support: Vulgamycin

major / open / confirmed; issue key: mim-reconciliation-role-support-98948e989daadbb5.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-11ce4e4b85c2397a

Reassess prediction-only role support: Vulgamycin

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-fb9a245806e7cc40 | data/ingredients/mapped/Vulgamycin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2054],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C012306","line":2056,"mapping_status":"MAPPED","ontology_id":"mesh:C012306","preferred_term":"Vulgamycin"}],"identifier":"mesh:C012306","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C012306","ontology_label":"enterocin","ontology_source":"MESH"},"preferred_term":"Vulgamycin","sssom_rows":[{"data_row":2919,"object_id":"mesh:C012306","object_label":"enterocin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Vulgamycin","synonym_count":0} |
| ev-829c13b5122a59c7 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2054] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-88df70b9460dbf71 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Vulgamycin; data-row positions=[2919] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2919,"object_id":"mesh:C012306","object_label":"enterocin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Vulgamycin","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-226165023b0faa04 | docs/data/mapped_ingredients.csv; CSV lines=[2056] | supports | Published identity and count rows inspected: [{"identifier":"mesh:C012306","line":2056,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C012306","preferred_term":"Vulgamycin","total_occurrences":"0"}] |
| ev-ac90dac65b7e6a18 | reports/yaml_record_review/Vulgamycin.md; &#96;data/ingredients/mapped/Vulgamycin.yaml&#96;:2; Verdict:4; Identity:10; Validation:21; Evidence:30; Issues:38; Completeness:44; Recommended Edits:48 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-b03a7ebadd8eb22c | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1344,1443] | context_only | [{"current_record_sha256":"a602884e4b0ada6c719c9fb22b0e8163ead1943ff7c5abbd9ebdb4cfe2b50dbe","finding_id":"SEM:c8ec0784669fd69f4c78","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"a602884e4b0ada6c719c9fb22b0e8163ead1943ff7c5abbd9ebdb4cfe2b50dbe","finding_id":"SEM:976c14b8ff4ae35efae1","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-fe7a77fe757e49c4 | data/ingredients/mapped/Vulgamycin.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}] |
| ev-bbd3e57c2413b7b3 | reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml; findings[finding_id=f-11ce4e4b85c2397a] | context_only | Predecessor structured review finding f-11ce4e4b85c2397a in 20261011T024639Z-mim-reconcile-all-batch-12 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-vulgamycin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Vulgamycin (data/ingredients/mapped/Vulgamycin.yaml)'
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
summary: Per-record structured review for Vulgamycin (data/ingredients/mapped/Vulgamycin.yaml,
  record-98948e989daadbb5, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Vulgamycin.yaml
    sha256: a602884e4b0ada6c719c9fb22b0e8163ead1943ff7c5abbd9ebdb4cfe2b50dbe
    role: target
  - path: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
    sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
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
  - path: reports/yaml_record_review/Vulgamycin.md
    sha256: 2dd27c4dc4050be2cd1b9c51be8618a3f12400ba1a9eb80c8972b14d0180032c
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-98948e989daadbb5
  path: data/ingredients/mapped/Vulgamycin.yaml
  label: Vulgamycin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Vulgamycin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Vulgamycin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Vulgamycin.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-98948e989daadbb5
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-98948e989daadbb5
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-98948e989daadbb5
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12
    and semantic review dispositions on HEAD.
  target_ids:
  - record-98948e989daadbb5
evidence:
- evidence_id: ev-fb9a245806e7cc40
  kind: record_content
  reference: data/ingredients/mapped/Vulgamycin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2054],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C012306","line":2056,"mapping_status":"MAPPED","ontology_id":"mesh:C012306","preferred_term":"Vulgamycin"}],"identifier":"mesh:C012306","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C012306","ontology_label":"enterocin","ontology_source":"MESH"},"preferred_term":"Vulgamycin","sssom_rows":[{"data_row":2919,"object_id":"mesh:C012306","object_label":"enterocin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Vulgamycin","synonym_count":0}'
  snapshot_sha256: a602884e4b0ada6c719c9fb22b0e8163ead1943ff7c5abbd9ebdb4cfe2b50dbe
- evidence_id: ev-829c13b5122a59c7
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2054]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-88df70b9460dbf71
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Vulgamycin; data-row positions=[2919]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2919,"object_id":"mesh:C012306","object_label":"enterocin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Vulgamycin","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-226165023b0faa04
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2056]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"mesh:C012306","line":2056,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C012306","preferred_term":"Vulgamycin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-ac90dac65b7e6a18
  kind: prior_review
  reference: reports/yaml_record_review/Vulgamycin.md
  locator: '`data/ingredients/mapped/Vulgamycin.yaml`:2; Verdict:4; Identity:10; Validation:21;
    Evidence:30; Issues:38; Completeness:44; Recommended Edits:48'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 2dd27c4dc4050be2cd1b9c51be8618a3f12400ba1a9eb80c8972b14d0180032c
  quote: "Issues:\n- Major: `physicochemical_roles.SELECTIVE_AGENT` rests on\n  `COMPUTATIONAL_PREDICTION`\
    \ evidence whose note says the curated name-pattern\n  rule is provisional and\
    \ still needs review.\n\nRecommended Edits:\n- Replace or remove this record's\
    \ `physicochemical_roles.SELECTIVE_AGENT`; keep\n  it only if a maintained source\
    \ supports Vulgamycin as a selective agent in\n  media.\n- Rerun strict validation\
    \ and SSSOM invariant validation after curation."
- evidence_id: ev-b03a7ebadd8eb22c
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1344,1443]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"a602884e4b0ada6c719c9fb22b0e8163ead1943ff7c5abbd9ebdb4cfe2b50dbe","finding_id":"SEM:c8ec0784669fd69f4c78","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"a602884e4b0ada6c719c9fb22b0e8163ead1943ff7c5abbd9ebdb4cfe2b50dbe","finding_id":"SEM:976c14b8ff4ae35efae1","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-fe7a77fe757e49c4
  kind: record_content
  reference: data/ingredients/mapped/Vulgamycin.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}]'
  snapshot_sha256: a602884e4b0ada6c719c9fb22b0e8163ead1943ff7c5abbd9ebdb4cfe2b50dbe
- evidence_id: ev-bbd3e57c2413b7b3
  kind: prior_review
  reference: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
  locator: findings[finding_id=f-11ce4e4b85c2397a]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-11ce4e4b85c2397a in 20261011T024639Z-mim-reconcile-all-batch-12
  snapshot_sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
assessments:
- assessment_id: a-382f7c7b94037d86
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-98948e989daadbb5
  evidence_ids:
  - ev-fb9a245806e7cc40
  - ev-829c13b5122a59c7
  - ev-88df70b9460dbf71
  - ev-226165023b0faa04
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-2ded3f05294d75ea
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-98948e989daadbb5
  evidence_ids:
  - ev-ac90dac65b7e6a18
  - ev-fb9a245806e7cc40
  - ev-b03a7ebadd8eb22c
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:12:17Z;
    reviewed SHA-256=a602884e4b0ada6c719c9fb22b0e8163ead1943ff7c5abbd9ebdb4cfe2b50dbe;
    current SHA-256=a602884e4b0ada6c719c9fb22b0e8163ead1943ff7c5abbd9ebdb4cfe2b50dbe;
    hash_changed=False. Reports=["reports/yaml_record_review/Vulgamycin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact MeSH
    enterocin synonym identity passes, but SELECTIVE_AGENT is still a provisional
    name-pattern role.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ac90dac65b7e6a18
    - ev-fb9a245806e7cc40
  - name: legacy-native-ids
    value: '["SEM:c8ec0784669fd69f4c78","SEM:976c14b8ff4ae35efae1"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-fb9a245806e7cc40
    - ev-ac90dac65b7e6a18
    - ev-b03a7ebadd8eb22c
- assessment_id: a-fe7a77fe757e49c4
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-98948e989daadbb5
  evidence_ids:
  - ev-ac90dac65b7e6a18
  - ev-fe7a77fe757e49c4
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ac90dac65b7e6a18
    - ev-fe7a77fe757e49c4
findings:
- finding_id: rec-f-11ce4e4b85c2397a
  issue_key: mim-reconciliation-role-support-98948e989daadbb5
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Vulgamycin'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-98948e989daadbb5
  evidence_ids:
  - ev-ac90dac65b7e6a18
  - ev-fe7a77fe757e49c4
  - ev-bbd3e57c2413b7b3
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Vulgamycin.yaml
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
    review_id: 20261011T024639Z-mim-reconcile-all-batch-12
    finding_id: f-11ce4e4b85c2397a
actions:
- action_id: rec-action-11ce4e4b85c2397a
  description: 'Reassess prediction-only role support: Vulgamycin'
  finding_ids:
  - rec-f-11ce4e4b85c2397a
  target_ids:
  - record-98948e989daadbb5
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Vulgamycin.yaml
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
  with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.
```
