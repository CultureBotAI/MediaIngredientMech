# Per-record structured review: Polypeptone (data/ingredients/mapped/Polypeptone.yaml)

- Review: 20261017T083000Z-polypeptone
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Polypeptone (data/ingredients/mapped/Polypeptone.yaml, record-58c1512d939af3b2, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Polypeptone.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Polypeptone.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-58c1512d939af3b2 | data/ingredients/mapped/Polypeptone.yaml | maintained | Polypeptone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-58c1512d939af3b2 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-58c1512d939af3b2 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-58c1512d939af3b2 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-58c1512d939af3b2.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-58c1512d939af3b2.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T09:59:25Z; reviewed SHA-256=5ecabcf8a37d4c2218e12fb3112f17b79d103abfa5f0a6a64322d7bf19c56baa; current SHA-256=5ecabcf8a37d4c2218e12fb3112f17b79d103abfa5f0a6a64322d7bf19c56baa; hash_changed=False. Reports=["reports/yaml_record_review/Polypeptone.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The FOODON parent grounding erases the Polypeptone product-family identity and PROTEIN_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-58c1512d939af3b2.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-e8ce7320237ada8c: Reassess prediction-only role support: Polypeptone

major / open / confirmed; issue key: mim-reconciliation-role-support-58c1512d939af3b2.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-e8ce7320237ada8c

Reassess prediction-only role support: Polypeptone

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-a6359eecfef22a99 | data/ingredients/mapped/Polypeptone.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1683],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:03315306","line":1685,"mapping_status":"MAPPED","ontology_id":"FOODON:03315306","preferred_term":"Polypeptone"}],"identifier":"FOODON:03315306","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":135,"edge_count":135,"occurrences":135},"occurrence_statistics":{"media_count":135,"total_occurrences":135},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"FOODON:03315306","ontology_label":"protein hydrolyzates","ontology_source":"FOODON"},"preferred_term":"Polypeptone","sssom_rows":[{"data_row":2297,"object_id":"FOODON:03315306","object_label":"protein hydrolyzates","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Polypeptone","synonym_count":11} |
| ev-764fef883b937ab5 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1683] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-14056b9e50c4ad0b | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Polypeptone; data-row positions=[2297] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2297,"object_id":"FOODON:03315306","object_label":"protein hydrolyzates","other":"Polypepton&#124;Polypepton (Nihon Pharm. Co.)&#124;Polypeptone peptone (BD-BBL)&#124;Polypeptone Peptone (BD 211910)&#124;Hipolypepton&#124;Hipolypepton (Nihon seiyaku)&#124;Hipolypepton*&#124;Polypepton (Nihon Seiyaku)&#124;Polypeptone (BBL)","predicate_id":"skos:exactMatch","subject_id":"MIM:Polypeptone","validation_method":"OLS:foodon&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-ce39e7e5339a77d0 | docs/data/mapped_ingredients.csv; CSV lines=[1685] | supports | Published identity and count rows inspected: [{"identifier":"FOODON:03315306","line":1685,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"135","ontology_id":"FOODON:03315306","preferred_term":"Polypeptone","total_occurrences":"135"}] |
| ev-108aa7c88aa7ca0e | reports/yaml_record_review/Polypeptone.md; &#96;data/ingredients/mapped/Polypeptone.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-af70cf1b67991ab0 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1130,2046] | context_only | [{"current_record_sha256":"5ecabcf8a37d4c2218e12fb3112f17b79d103abfa5f0a6a64322d7bf19c56baa","finding_id":"SEM:256c5b7f1b2c16ad3a94","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"5ecabcf8a37d4c2218e12fb3112f17b79d103abfa5f0a6a64322d7bf19c56baa","finding_id":"SEM:6b4a0c66f792764beb52","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-4f83401e57b84559 | data/ingredients/mapped/Polypeptone.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"PROTEIN_SOURCE"}}] |
| ev-719bea6c9f069088 | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml; findings[finding_id=f-e8ce7320237ada8c] | context_only | Predecessor structured review finding f-e8ce7320237ada8c in 20261011T024638Z-mim-reconcile-all-batch-10 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-polypeptone
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Polypeptone (data/ingredients/mapped/Polypeptone.yaml)'
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
summary: Per-record structured review for Polypeptone (data/ingredients/mapped/Polypeptone.yaml,
  record-58c1512d939af3b2, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Polypeptone.yaml
    sha256: 5ecabcf8a37d4c2218e12fb3112f17b79d103abfa5f0a6a64322d7bf19c56baa
    role: target
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
    sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
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
  - path: reports/yaml_record_review/Polypeptone.md
    sha256: 135e75fe350f4158823923b2948317b18427859be2fbcdaf79502eb1bb2e60c2
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-58c1512d939af3b2
  path: data/ingredients/mapped/Polypeptone.yaml
  label: Polypeptone
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Polypeptone.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Polypeptone.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Polypeptone.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-58c1512d939af3b2
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-58c1512d939af3b2
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-58c1512d939af3b2
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10
    and semantic review dispositions on HEAD.
  target_ids:
  - record-58c1512d939af3b2
evidence:
- evidence_id: ev-a6359eecfef22a99
  kind: record_content
  reference: data/ingredients/mapped/Polypeptone.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1683],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:03315306","line":1685,"mapping_status":"MAPPED","ontology_id":"FOODON:03315306","preferred_term":"Polypeptone"}],"identifier":"FOODON:03315306","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":135,"edge_count":135,"occurrences":135},"occurrence_statistics":{"media_count":135,"total_occurrences":135},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"FOODON:03315306","ontology_label":"protein
    hydrolyzates","ontology_source":"FOODON"},"preferred_term":"Polypeptone","sssom_rows":[{"data_row":2297,"object_id":"FOODON:03315306","object_label":"protein
    hydrolyzates","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Polypeptone","synonym_count":11}'
  snapshot_sha256: 5ecabcf8a37d4c2218e12fb3112f17b79d103abfa5f0a6a64322d7bf19c56baa
- evidence_id: ev-764fef883b937ab5
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1683]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-14056b9e50c4ad0b
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Polypeptone; data-row positions=[2297]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2297,"object_id":"FOODON:03315306","object_label":"protein
    hydrolyzates","other":"Polypepton|Polypepton (Nihon Pharm. Co.)|Polypeptone peptone
    (BD-BBL)|Polypeptone Peptone (BD 211910)|Hipolypepton|Hipolypepton (Nihon seiyaku)|Hipolypepton*|Polypepton
    (Nihon Seiyaku)|Polypeptone (BBL)","predicate_id":"skos:exactMatch","subject_id":"MIM:Polypeptone","validation_method":"OLS:foodon|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-ce39e7e5339a77d0
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1685]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"FOODON:03315306","line":1685,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"135","ontology_id":"FOODON:03315306","preferred_term":"Polypeptone","total_occurrences":"135"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-108aa7c88aa7ca0e
  kind: prior_review
  reference: reports/yaml_record_review/Polypeptone.md
  locator: '`data/ingredients/mapped/Polypeptone.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 135e75fe350f4158823923b2948317b18427859be2fbcdaf79502eb1bb2e60c2
- evidence_id: ev-af70cf1b67991ab0
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1130,2046]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"5ecabcf8a37d4c2218e12fb3112f17b79d103abfa5f0a6a64322d7bf19c56baa","finding_id":"SEM:256c5b7f1b2c16ad3a94","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"5ecabcf8a37d4c2218e12fb3112f17b79d103abfa5f0a6a64322d7bf19c56baa","finding_id":"SEM:6b4a0c66f792764beb52","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-4f83401e57b84559
  kind: record_content
  reference: data/ingredients/mapped/Polypeptone.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"PROTEIN_SOURCE"}}]'
  snapshot_sha256: 5ecabcf8a37d4c2218e12fb3112f17b79d103abfa5f0a6a64322d7bf19c56baa
- evidence_id: ev-719bea6c9f069088
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
  locator: findings[finding_id=f-e8ce7320237ada8c]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-e8ce7320237ada8c in 20261011T024638Z-mim-reconcile-all-batch-10
  snapshot_sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
assessments:
- assessment_id: a-a8c2816c935a9fab
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-58c1512d939af3b2
  evidence_ids:
  - ev-a6359eecfef22a99
  - ev-764fef883b937ab5
  - ev-14056b9e50c4ad0b
  - ev-ce39e7e5339a77d0
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-062a9211f6a882d4
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-58c1512d939af3b2
  evidence_ids:
  - ev-108aa7c88aa7ca0e
  - ev-a6359eecfef22a99
  - ev-af70cf1b67991ab0
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T09:59:25Z;
    reviewed SHA-256=5ecabcf8a37d4c2218e12fb3112f17b79d103abfa5f0a6a64322d7bf19c56baa;
    current SHA-256=5ecabcf8a37d4c2218e12fb3112f17b79d103abfa5f0a6a64322d7bf19c56baa;
    hash_changed=False. Reports=["reports/yaml_record_review/Polypeptone.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The FOODON parent
    grounding erases the Polypeptone product-family identity and PROTEIN_SOURCE is
    provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-108aa7c88aa7ca0e
    - ev-a6359eecfef22a99
  - name: legacy-native-ids
    value: '["SEM:256c5b7f1b2c16ad3a94","SEM:6b4a0c66f792764beb52"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-a6359eecfef22a99
    - ev-108aa7c88aa7ca0e
    - ev-af70cf1b67991ab0
- assessment_id: a-4f83401e57b84559
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-58c1512d939af3b2
  evidence_ids:
  - ev-108aa7c88aa7ca0e
  - ev-4f83401e57b84559
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-108aa7c88aa7ca0e
    - ev-4f83401e57b84559
findings:
- finding_id: rec-f-e8ce7320237ada8c
  issue_key: mim-reconciliation-role-support-58c1512d939af3b2
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Polypeptone'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-58c1512d939af3b2
  evidence_ids:
  - ev-108aa7c88aa7ca0e
  - ev-4f83401e57b84559
  - ev-719bea6c9f069088
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Polypeptone.yaml
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
    review_id: 20261011T024638Z-mim-reconcile-all-batch-10
    finding_id: f-e8ce7320237ada8c
actions:
- action_id: rec-action-e8ce7320237ada8c
  description: 'Reassess prediction-only role support: Polypeptone'
  finding_ids:
  - rec-f-e8ce7320237ada8c
  target_ids:
  - record-58c1512d939af3b2
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Polypeptone.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.
```
