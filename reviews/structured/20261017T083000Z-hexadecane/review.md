# Per-record structured review: Hexadecane (data/ingredients/mapped/Hexadecane.yaml)

- Review: 20261017T083000Z-hexadecane
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Hexadecane (data/ingredients/mapped/Hexadecane.yaml, record-a7f0a572e7f633ba, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Hexadecane.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Hexadecane.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-a7f0a572e7f633ba | data/ingredients/mapped/Hexadecane.yaml | maintained | Hexadecane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-a7f0a572e7f633ba | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-a7f0a572e7f633ba | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-a7f0a572e7f633ba | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-a7f0a572e7f633ba.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-a7f0a572e7f633ba.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T19:24:02Z; reviewed SHA-256=9434d50224d75f9974445e21a9e530941a569ce2133efa91e23dab641bc76dc2; current SHA-256=9434d50224d75f9974445e21a9e530941a569ce2133efa91e23dab641bc76dc2; hash_changed=False. Reports=["reports/yaml_record_review/Hexadecane.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact hexadecane identity passes, but CARBON_SOURCE is only a provisional in-session computational assertion.

### Historical provisional-role concern

evidence: concern. Targets: record-a7f0a572e7f633ba.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-df663a089ed283d7: Reassess prediction-only role support: Hexadecane

major / open / confirmed; issue key: mim-reconciliation-role-support-a7f0a572e7f633ba.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-df663a089ed283d7

Reassess prediction-only role support: Hexadecane

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-379bc8b3c89ada2b | data/ingredients/mapped/Hexadecane.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1126],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:45296","line":1128,"mapping_status":"MAPPED","ontology_id":"CHEBI:45296","preferred_term":"Hexadecane"}],"identifier":"CHEBI:45296","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":21,"edge_count":21,"occurrences":21},"occurrence_statistics":{"media_count":21,"total_occurrences":21},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:45296","ontology_label":"hexadecane","ontology_source":"CHEBI"},"preferred_term":"Hexadecane","sssom_rows":[{"data_row":1426,"object_id":"CHEBI:45296","object_label":"hexadecane","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Hexadecane","synonym_count":8} |
| ev-4e8411e437184d4a | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1126] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-328168a41e0f8b79 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Hexadecane; data-row positions=[1426] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1426,"object_id":"CHEBI:45296","object_label":"hexadecane","other":"CH3-[CH2]14-CH3&#124;Cetan&#124;Hexadekan&#124;Zetan&#124;cetane&#124;n-cetane&#124;n-hexadecane&#124;CAS:544-76-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Hexadecane","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-b32e1317ba5ccec2 | docs/data/mapped_ingredients.csv; CSV lines=[1128] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:45296","line":1128,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"21","ontology_id":"CHEBI:45296","preferred_term":"Hexadecane","total_occurrences":"21"}] |
| ev-5a896c4b80e797e1 | reports/yaml_record_review/Hexadecane.md; &#96;data/ingredients/mapped/Hexadecane.yaml&#96;:2; Verdict:4; Identity:11; Validation:24; Evidence:35; Completeness:51; Recommended Edits:59 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-9691d33191423f75 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[730,2045] | context_only | [{"current_record_sha256":"9434d50224d75f9974445e21a9e530941a569ce2133efa91e23dab641bc76dc2","finding_id":"SEM:2e7440b26dc208396d34","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"9434d50224d75f9974445e21a9e530941a569ce2133efa91e23dab641bc76dc2","finding_id":"SEM:e967e99bd54516fc8b72","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-e82a8bb1b5c01af2 | data/ingredients/mapped/Hexadecane.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional in-session LLM role assignment; review recommended.","reference_text":"Assigned by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}] |
| ev-cccee1f45502846c | reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml; findings[finding_id=f-df663a089ed283d7] | context_only | Predecessor structured review finding f-df663a089ed283d7 in 20261011T024635Z-mim-reconcile-all-batch-07 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-hexadecane
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Hexadecane (data/ingredients/mapped/Hexadecane.yaml)'
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
summary: Per-record structured review for Hexadecane (data/ingredients/mapped/Hexadecane.yaml,
  record-a7f0a572e7f633ba, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Hexadecane.yaml
    sha256: 9434d50224d75f9974445e21a9e530941a569ce2133efa91e23dab641bc76dc2
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
  - path: reports/yaml_record_review/Hexadecane.md
    sha256: d2d9e920b244e303a0ae45890586b3381d72b4dcaf4a7389e9ecd411336d511b
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-a7f0a572e7f633ba
  path: data/ingredients/mapped/Hexadecane.yaml
  label: Hexadecane
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Hexadecane.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Hexadecane.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Hexadecane.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-a7f0a572e7f633ba
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-a7f0a572e7f633ba
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-a7f0a572e7f633ba
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-a7f0a572e7f633ba
evidence:
- evidence_id: ev-379bc8b3c89ada2b
  kind: record_content
  reference: data/ingredients/mapped/Hexadecane.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1126],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:45296","line":1128,"mapping_status":"MAPPED","ontology_id":"CHEBI:45296","preferred_term":"Hexadecane"}],"identifier":"CHEBI:45296","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":21,"edge_count":21,"occurrences":21},"occurrence_statistics":{"media_count":21,"total_occurrences":21},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:45296","ontology_label":"hexadecane","ontology_source":"CHEBI"},"preferred_term":"Hexadecane","sssom_rows":[{"data_row":1426,"object_id":"CHEBI:45296","object_label":"hexadecane","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Hexadecane","synonym_count":8}'
  snapshot_sha256: 9434d50224d75f9974445e21a9e530941a569ce2133efa91e23dab641bc76dc2
- evidence_id: ev-4e8411e437184d4a
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1126]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-328168a41e0f8b79
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Hexadecane; data-row positions=[1426]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1426,"object_id":"CHEBI:45296","object_label":"hexadecane","other":"CH3-[CH2]14-CH3|Cetan|Hexadekan|Zetan|cetane|n-cetane|n-hexadecane|CAS:544-76-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Hexadecane","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-b32e1317ba5ccec2
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1128]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:45296","line":1128,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"21","ontology_id":"CHEBI:45296","preferred_term":"Hexadecane","total_occurrences":"21"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-5a896c4b80e797e1
  kind: prior_review
  reference: reports/yaml_record_review/Hexadecane.md
  locator: '`data/ingredients/mapped/Hexadecane.yaml`:2; Verdict:4; Identity:11; Validation:24;
    Evidence:35; Completeness:51; Recommended Edits:59'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: d2d9e920b244e303a0ae45890586b3381d72b4dcaf4a7389e9ecd411336d511b
  quote: "Recommended Edits:\n- Major: remove `nutritional_roles.CARBON_SOURCE` unless\
    \ an inspected\n  CultureMech source row or literature source can support hexadecane\
    \ as a\n  carbon source, then rerun strict, term, round-trip, component, id-label,\
    \ and\n  SSSOM validation."
- evidence_id: ev-9691d33191423f75
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[730,2045]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"9434d50224d75f9974445e21a9e530941a569ce2133efa91e23dab641bc76dc2","finding_id":"SEM:2e7440b26dc208396d34","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"9434d50224d75f9974445e21a9e530941a569ce2133efa91e23dab641bc76dc2","finding_id":"SEM:e967e99bd54516fc8b72","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-e82a8bb1b5c01af2
  kind: record_content
  reference: data/ingredients/mapped/Hexadecane.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional
    in-session LLM role assignment; review recommended.","reference_text":"Assigned
    by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}]'
  snapshot_sha256: 9434d50224d75f9974445e21a9e530941a569ce2133efa91e23dab641bc76dc2
- evidence_id: ev-cccee1f45502846c
  kind: prior_review
  reference: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
  locator: findings[finding_id=f-df663a089ed283d7]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-df663a089ed283d7 in 20261011T024635Z-mim-reconcile-all-batch-07
  snapshot_sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
assessments:
- assessment_id: a-1a632fef7ff569f5
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-a7f0a572e7f633ba
  evidence_ids:
  - ev-379bc8b3c89ada2b
  - ev-4e8411e437184d4a
  - ev-328168a41e0f8b79
  - ev-b32e1317ba5ccec2
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-dda165ccfb9c24a1
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-a7f0a572e7f633ba
  evidence_ids:
  - ev-5a896c4b80e797e1
  - ev-379bc8b3c89ada2b
  - ev-9691d33191423f75
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T19:24:02Z;
    reviewed SHA-256=9434d50224d75f9974445e21a9e530941a569ce2133efa91e23dab641bc76dc2;
    current SHA-256=9434d50224d75f9974445e21a9e530941a569ce2133efa91e23dab641bc76dc2;
    hash_changed=False. Reports=["reports/yaml_record_review/Hexadecane.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact hexadecane
    identity passes, but CARBON_SOURCE is only a provisional in-session computational
    assertion.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-5a896c4b80e797e1
    - ev-379bc8b3c89ada2b
  - name: legacy-native-ids
    value: '["SEM:2e7440b26dc208396d34","SEM:e967e99bd54516fc8b72"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-379bc8b3c89ada2b
    - ev-5a896c4b80e797e1
    - ev-9691d33191423f75
- assessment_id: a-e82a8bb1b5c01af2
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-a7f0a572e7f633ba
  evidence_ids:
  - ev-5a896c4b80e797e1
  - ev-e82a8bb1b5c01af2
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-5a896c4b80e797e1
    - ev-e82a8bb1b5c01af2
findings:
- finding_id: rec-f-df663a089ed283d7
  issue_key: mim-reconciliation-role-support-a7f0a572e7f633ba
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Hexadecane'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-a7f0a572e7f633ba
  evidence_ids:
  - ev-5a896c4b80e797e1
  - ev-e82a8bb1b5c01af2
  - ev-cccee1f45502846c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Hexadecane.yaml
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
    review_id: 20261011T024635Z-mim-reconcile-all-batch-07
    finding_id: f-df663a089ed283d7
actions:
- action_id: rec-action-df663a089ed283d7
  description: 'Reassess prediction-only role support: Hexadecane'
  finding_ids:
  - rec-f-df663a089ed283d7
  target_ids:
  - record-a7f0a572e7f633ba
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Hexadecane.yaml
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
