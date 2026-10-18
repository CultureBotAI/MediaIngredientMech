# Per-record structured review: Bakers_Yeast (data/ingredients/mapped/Bakers_Yeast.yaml)

- Review: 20261017T083000Z-bakers-yeast
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Bakers_Yeast (data/ingredients/mapped/Bakers_Yeast.yaml, record-8db48844d204dc6f, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Bakers_Yeast.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Bakers_Yeast.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-8db48844d204dc6f | data/ingredients/mapped/Bakers_Yeast.yaml | maintained | Bakers_Yeast |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-8db48844d204dc6f | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-8db48844d204dc6f | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-8db48844d204dc6f | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-8db48844d204dc6f.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-8db48844d204dc6f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T09:22:18Z; reviewed SHA-256=11eda0e05a1a8abf2779d8eb421548e31e82d06387dfa388d8526b6523a0154e; current SHA-256=11eda0e05a1a8abf2779d8eb421548e31e82d06387dfa388d8526b6523a0154e; hash_changed=False. Reports=["reports/yaml_record_review/Bakers_Yeast.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact FOODON baker's yeast mapping, protein-source role, occurrence count, SSSOM row, and aggregate copy pass, but top-level notes still describe the old unmapped state.

### Historical provisional-role concern

evidence: concern. Targets: record-8db48844d204dc6f.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-481dd687371e9faa: Reassess prediction-only role support: Baker's yeast

major / open / confirmed; issue key: mim-reconciliation-role-support-8db48844d204dc6f.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-481dd687371e9faa

Reassess prediction-only role support: Baker's yeast

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-c6ffa3410d8dcb7a | data/ingredients/mapped/Bakers_Yeast.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[556],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:03413797","line":558,"mapping_status":"MAPPED","ontology_id":"FOODON:03413797","preferred_term":"Baker's yeast"}],"identifier":"FOODON:03413797","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":17,"edge_count":17,"occurrences":17},"occurrence_statistics":{"media_count":17,"total_occurrences":17},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"FOODON:03413797","ontology_label":"baker's yeast","ontology_source":"FOODON"},"preferred_term":"Baker's yeast","sssom_rows":[{"data_row":486,"object_id":"FOODON:03413797","object_label":"baker's yeast","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Bakers_Yeast","synonym_count":1} |
| ev-23861c940b1ede2b | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [556] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-81fe6cdfbbb3f2dd | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Bakers_Yeast; data-row positions=[486] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":486,"object_id":"FOODON:03413797","object_label":"baker's yeast","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Bakers_Yeast","validation_method":"OLS:foodon&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-f8dab49636b80524 | docs/data/mapped_ingredients.csv; CSV lines=[558] | supports | Published identity and count rows inspected: [{"identifier":"FOODON:03413797","line":558,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"17","ontology_id":"FOODON:03413797","preferred_term":"Baker's yeast","total_occurrences":"17"}] |
| ev-12a9c1e00030f6dd | reports/yaml_record_review/Bakers_Yeast.md; &#96;data/ingredients/mapped/Bakers_Yeast.yaml&#96;:2; Verdict:4; Identity:11; Validation:23; Evidence:33; Completeness:53; Recommended Edits:60 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-1dd2dcbfd3254dcd | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[295,1676] | context_only | [{"current_record_sha256":"11eda0e05a1a8abf2779d8eb421548e31e82d06387dfa388d8526b6523a0154e","finding_id":"SEM:eb68359056af5d50f933","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"11eda0e05a1a8abf2779d8eb421548e31e82d06387dfa388d8526b6523a0154e","finding_id":"SEM:5fd7192746ffe2a0bc7d","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-021c91b23b1d26c2 | data/ingredients/mapped/Bakers_Yeast.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"PROTEIN_SOURCE"}}] |
| ev-a61677bec1d50263 | reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml; findings[finding_id=f-481dd687371e9faa] | context_only | Predecessor structured review finding f-481dd687371e9faa in 20261011T024631Z-mim-reconcile-all-batch-03 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-bakers-yeast
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Bakers_Yeast (data/ingredients/mapped/Bakers_Yeast.yaml)'
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
summary: Per-record structured review for Bakers_Yeast (data/ingredients/mapped/Bakers_Yeast.yaml,
  record-8db48844d204dc6f, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Bakers_Yeast.yaml
    sha256: 11eda0e05a1a8abf2779d8eb421548e31e82d06387dfa388d8526b6523a0154e
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
  - path: reports/yaml_record_review/Bakers_Yeast.md
    sha256: aa2b4e8552d8c2821c221d8cec2483dd91a56c449d6c6a884bf0f64f688ce2da
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-8db48844d204dc6f
  path: data/ingredients/mapped/Bakers_Yeast.yaml
  label: Bakers_Yeast
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bakers_Yeast.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Bakers_Yeast.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Bakers_Yeast.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-8db48844d204dc6f
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-8db48844d204dc6f
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-8db48844d204dc6f
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-8db48844d204dc6f
evidence:
- evidence_id: ev-c6ffa3410d8dcb7a
  kind: record_content
  reference: data/ingredients/mapped/Bakers_Yeast.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[556],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:03413797","line":558,"mapping_status":"MAPPED","ontology_id":"FOODON:03413797","preferred_term":"Baker''s
    yeast"}],"identifier":"FOODON:03413797","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":17,"edge_count":17,"occurrences":17},"occurrence_statistics":{"media_count":17,"total_occurrences":17},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"FOODON:03413797","ontology_label":"baker''s
    yeast","ontology_source":"FOODON"},"preferred_term":"Baker''s yeast","sssom_rows":[{"data_row":486,"object_id":"FOODON:03413797","object_label":"baker''s
    yeast","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Bakers_Yeast","synonym_count":1}'
  snapshot_sha256: 11eda0e05a1a8abf2779d8eb421548e31e82d06387dfa388d8526b6523a0154e
- evidence_id: ev-23861c940b1ede2b
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [556]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-81fe6cdfbbb3f2dd
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Bakers_Yeast; data-row positions=[486]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":486,"object_id":"FOODON:03413797","object_label":"baker''s
    yeast","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Bakers_Yeast","validation_method":"OLS:foodon|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-f8dab49636b80524
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[558]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"FOODON:03413797","line":558,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"17","ontology_id":"FOODON:03413797","preferred_term":"Baker''s
    yeast","total_occurrences":"17"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-12a9c1e00030f6dd
  kind: prior_review
  reference: reports/yaml_record_review/Bakers_Yeast.md
  locator: '`data/ingredients/mapped/Bakers_Yeast.yaml`:2; Verdict:4; Identity:11;
    Validation:23; Evidence:33; Completeness:53; Recommended Edits:60'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: aa2b4e8552d8c2821c221d8cec2483dd91a56c449d6c6a884bf0f64f688ce2da
  quote: "Recommended Edits:\n- Minor: update `notes` in `data/ingredients/mapped/Bakers_Yeast.yaml`\
    \ to\n  describe the current exact FOODON mapping and refreshed CultureMech occurrence\n\
    \  count, then run `just sync-curated`."
- evidence_id: ev-1dd2dcbfd3254dcd
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[295,1676]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"11eda0e05a1a8abf2779d8eb421548e31e82d06387dfa388d8526b6523a0154e","finding_id":"SEM:eb68359056af5d50f933","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"11eda0e05a1a8abf2779d8eb421548e31e82d06387dfa388d8526b6523a0154e","finding_id":"SEM:5fd7192746ffe2a0bc7d","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-021c91b23b1d26c2
  kind: record_content
  reference: data/ingredients/mapped/Bakers_Yeast.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"PROTEIN_SOURCE"}}]'
  snapshot_sha256: 11eda0e05a1a8abf2779d8eb421548e31e82d06387dfa388d8526b6523a0154e
- evidence_id: ev-a61677bec1d50263
  kind: prior_review
  reference: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
  locator: findings[finding_id=f-481dd687371e9faa]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-481dd687371e9faa in 20261011T024631Z-mim-reconcile-all-batch-03
  snapshot_sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
assessments:
- assessment_id: a-ce4dcafac3179dfb
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-8db48844d204dc6f
  evidence_ids:
  - ev-c6ffa3410d8dcb7a
  - ev-23861c940b1ede2b
  - ev-81fe6cdfbbb3f2dd
  - ev-f8dab49636b80524
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-0dd4162a61e6f4ef
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-8db48844d204dc6f
  evidence_ids:
  - ev-12a9c1e00030f6dd
  - ev-c6ffa3410d8dcb7a
  - ev-1dd2dcbfd3254dcd
  details: 'Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T09:22:18Z;
    reviewed SHA-256=11eda0e05a1a8abf2779d8eb421548e31e82d06387dfa388d8526b6523a0154e;
    current SHA-256=11eda0e05a1a8abf2779d8eb421548e31e82d06387dfa388d8526b6523a0154e;
    hash_changed=False. Reports=["reports/yaml_record_review/Bakers_Yeast.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact FOODON
    baker''s yeast mapping, protein-source role, occurrence count, SSSOM row, and
    aggregate copy pass, but top-level notes still describe the old unmapped state.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-12a9c1e00030f6dd
    - ev-c6ffa3410d8dcb7a
  - name: legacy-native-ids
    value: '["SEM:eb68359056af5d50f933","SEM:5fd7192746ffe2a0bc7d"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-c6ffa3410d8dcb7a
    - ev-12a9c1e00030f6dd
    - ev-1dd2dcbfd3254dcd
- assessment_id: a-021c91b23b1d26c2
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-8db48844d204dc6f
  evidence_ids:
  - ev-12a9c1e00030f6dd
  - ev-021c91b23b1d26c2
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-12a9c1e00030f6dd
    - ev-021c91b23b1d26c2
findings:
- finding_id: rec-f-481dd687371e9faa
  issue_key: mim-reconciliation-role-support-8db48844d204dc6f
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Baker''s yeast'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-8db48844d204dc6f
  evidence_ids:
  - ev-12a9c1e00030f6dd
  - ev-021c91b23b1d26c2
  - ev-a61677bec1d50263
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bakers_Yeast.yaml
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
    review_id: 20261011T024631Z-mim-reconcile-all-batch-03
    finding_id: f-481dd687371e9faa
actions:
- action_id: rec-action-481dd687371e9faa
  description: 'Reassess prediction-only role support: Baker''s yeast'
  finding_ids:
  - rec-f-481dd687371e9faa
  target_ids:
  - record-8db48844d204dc6f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bakers_Yeast.yaml
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
