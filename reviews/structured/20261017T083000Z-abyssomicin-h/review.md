# Per-record structured review: Abyssomicin_H (data/ingredients/mapped/Abyssomicin_H.yaml)

- Review: 20261017T083000Z-abyssomicin-h
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Abyssomicin_H (data/ingredients/mapped/Abyssomicin_H.yaml, record-bfa0fd3f8e644ade, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Abyssomicin_H.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Abyssomicin_H.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-bfa0fd3f8e644ade | data/ingredients/mapped/Abyssomicin_H.yaml | maintained | Abyssomicin_H |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-bfa0fd3f8e644ade | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-bfa0fd3f8e644ade | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-bfa0fd3f8e644ade | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-bfa0fd3f8e644ade.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-bfa0fd3f8e644ade.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T06:59:02Z; reviewed SHA-256=06abd4f73cfcd093312622a2d40c84e6f7f5121381559b57f7682de478726c8d; current SHA-256=06abd4f73cfcd093312622a2d40c84e6f7f5121381559b57f7682de478726c8d; hash_changed=False. Reports=["reports/yaml_record_review/Abyssomicin_H.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The placeholder kgmicrobe identity is intentionally retained pending exact ontology identity; OLS candidate review found no exact match, but the selective-agent role is still only provisional computational curation.

### Historical provisional-role concern

evidence: concern. Targets: record-bfa0fd3f8e644ade.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-4d5433329f7afa93: Reassess prediction-only role support: Abyssomicin H

major / open / confirmed; issue key: mim-reconciliation-role-support-bfa0fd3f8e644ade.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-4d5433329f7afa93

Reassess prediction-only role support: Abyssomicin H

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-dd543473682e90e0 | data/ingredients/mapped/Abyssomicin_H.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[434],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:abyssomicin_h","line":436,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:abyssomicin_h","preferred_term":"Abyssomicin H"}],"identifier":"kgmicrobe.compound:abyssomicin_h","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:abyssomicin_h","ontology_label":"Abyssomicin H","ontology_source":"kgmicrobe.compound"},"preferred_term":"Abyssomicin H","sssom_rows":[{"data_row":275,"object_id":"kgmicrobe.compound:abyssomicin_h","object_label":"Abyssomicin H","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Abyssomicin_H","synonym_count":0} |
| ev-27e63e3ab2cdc2ac | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [434] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-38c565967318deef | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Abyssomicin_H; data-row positions=[275] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":275,"object_id":"kgmicrobe.compound:abyssomicin_h","object_label":"Abyssomicin H","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Abyssomicin_H","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-4568f0319abf9f21 | docs/data/mapped_ingredients.csv; CSV lines=[436] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:abyssomicin_h","line":436,"mapping_quality":"PLACEHOLDER","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.compound:abyssomicin_h","preferred_term":"Abyssomicin H","total_occurrences":"0"}] |
| ev-382857f1bc834099 | reports/yaml_record_review/Abyssomicin_H.md; &#96;data/ingredients/mapped/Abyssomicin_H.yaml&#96;:2; Verdict:4; Identity:11; Validation:27; Evidence:40; Completeness:58; Recommended Edits:66 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-bfbec2f55af14289 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[192,1431] | context_only | [{"current_record_sha256":"06abd4f73cfcd093312622a2d40c84e6f7f5121381559b57f7682de478726c8d","finding_id":"SEM:10f9d72353b33e78bf7e","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"06abd4f73cfcd093312622a2d40c84e6f7f5121381559b57f7682de478726c8d","finding_id":"SEM:2723e9cae2241a16bab0","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-de56f594687a1cd8 | data/ingredients/mapped/Abyssomicin_H.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[434],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:abyssomicin_h","line":436,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:abyssomicin_h","preferred_term":"Abyssomicin H"}],"identifier":"kgmicrobe.compound:abyssomicin_h","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:abyssomicin_h","ontology_label":"Abyssomicin H","ontology_source":"kgmicrobe.compound"},"preferred_term":"Abyssomicin H","sssom_rows":[{"data_row":275,"object_id":"kgmicrobe.compound:abyssomicin_h","object_label":"Abyssomicin H","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Abyssomicin_H","synonym_count":0} |
| ev-982496d0b66bf22a | reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml; findings[finding_id=f-4d5433329f7afa93] | context_only | Predecessor structured review finding f-4d5433329f7afa93 in 20261011T024630Z-mim-reconcile-all-batch-02 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-abyssomicin-h
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Abyssomicin_H (data/ingredients/mapped/Abyssomicin_H.yaml)'
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
summary: Per-record structured review for Abyssomicin_H (data/ingredients/mapped/Abyssomicin_H.yaml,
  record-bfa0fd3f8e644ade, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Abyssomicin_H.yaml
    sha256: 06abd4f73cfcd093312622a2d40c84e6f7f5121381559b57f7682de478726c8d
    role: target
  - path: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
    sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
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
  - path: reports/yaml_record_review/Abyssomicin_H.md
    sha256: 33ccfb050b015d60932a6744ed37b8c0861b37fe9e922b7208c31f8b1961fa2c
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-bfa0fd3f8e644ade
  path: data/ingredients/mapped/Abyssomicin_H.yaml
  label: Abyssomicin_H
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Abyssomicin_H.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Abyssomicin_H.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Abyssomicin_H.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-bfa0fd3f8e644ade
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-bfa0fd3f8e644ade
  evidence_ids:
  - ev-dd543473682e90e0
  - ev-27e63e3ab2cdc2ac
  - ev-38c565967318deef
  - ev-4568f0319abf9f21
  - ev-de56f594687a1cd8
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-bfa0fd3f8e644ade
  evidence_ids:
  - ev-dd543473682e90e0
  - ev-bfbec2f55af14289
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-bfa0fd3f8e644ade
  evidence_ids:
  - ev-382857f1bc834099
  - ev-bfbec2f55af14289
  - ev-982496d0b66bf22a
evidence:
- evidence_id: ev-dd543473682e90e0
  kind: record_content
  reference: data/ingredients/mapped/Abyssomicin_H.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[434],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:abyssomicin_h","line":436,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:abyssomicin_h","preferred_term":"Abyssomicin
    H"}],"identifier":"kgmicrobe.compound:abyssomicin_h","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:abyssomicin_h","ontology_label":"Abyssomicin
    H","ontology_source":"kgmicrobe.compound"},"preferred_term":"Abyssomicin H","sssom_rows":[{"data_row":275,"object_id":"kgmicrobe.compound:abyssomicin_h","object_label":"Abyssomicin
    H","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Abyssomicin_H","synonym_count":0}'
  snapshot_sha256: 06abd4f73cfcd093312622a2d40c84e6f7f5121381559b57f7682de478726c8d
- evidence_id: ev-27e63e3ab2cdc2ac
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [434]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-38c565967318deef
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Abyssomicin_H; data-row positions=[275]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":275,"object_id":"kgmicrobe.compound:abyssomicin_h","object_label":"Abyssomicin
    H","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Abyssomicin_H","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-4568f0319abf9f21
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[436]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:abyssomicin_h","line":436,"mapping_quality":"PLACEHOLDER","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.compound:abyssomicin_h","preferred_term":"Abyssomicin
    H","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-382857f1bc834099
  kind: prior_review
  reference: reports/yaml_record_review/Abyssomicin_H.md
  locator: '`data/ingredients/mapped/Abyssomicin_H.yaml`:2; Verdict:4; Identity:11;
    Validation:27; Evidence:40; Completeness:58; Recommended Edits:66'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 33ccfb050b015d60932a6744ed37b8c0861b37fe9e922b7208c31f8b1961fa2c
  quote: "Recommended Edits:\n- Replace or remove\n  `data/ingredients/mapped/Abyssomicin_H.yaml`'s\n\
    \  `physicochemical_roles.SELECTIVE_AGENT` entry after inspecting evidence that\n\
    \  specifically supports Abyssomicin H as a selective agent. Re-run\n  `scripts/validate_strict.py`\
    \ and `scripts/validate_sssom_invariants.py`.\n- Leave `kgmicrobe.compound:abyssomicin_h`\
    \ in place unless a future exact\n  external ontology identity is found."
- evidence_id: ev-bfbec2f55af14289
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[192,1431]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"06abd4f73cfcd093312622a2d40c84e6f7f5121381559b57f7682de478726c8d","finding_id":"SEM:10f9d72353b33e78bf7e","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"06abd4f73cfcd093312622a2d40c84e6f7f5121381559b57f7682de478726c8d","finding_id":"SEM:2723e9cae2241a16bab0","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-de56f594687a1cd8
  kind: record_content
  reference: data/ingredients/mapped/Abyssomicin_H.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[434],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:abyssomicin_h","line":436,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:abyssomicin_h","preferred_term":"Abyssomicin
    H"}],"identifier":"kgmicrobe.compound:abyssomicin_h","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:abyssomicin_h","ontology_label":"Abyssomicin
    H","ontology_source":"kgmicrobe.compound"},"preferred_term":"Abyssomicin H","sssom_rows":[{"data_row":275,"object_id":"kgmicrobe.compound:abyssomicin_h","object_label":"Abyssomicin
    H","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Abyssomicin_H","synonym_count":0}'
  snapshot_sha256: 06abd4f73cfcd093312622a2d40c84e6f7f5121381559b57f7682de478726c8d
- evidence_id: ev-982496d0b66bf22a
  kind: prior_review
  reference: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
  locator: findings[finding_id=f-4d5433329f7afa93]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-4d5433329f7afa93 in 20261011T024630Z-mim-reconcile-all-batch-02
  snapshot_sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
assessments:
- assessment_id: a-a42f0cdd16c20455
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-bfa0fd3f8e644ade
  evidence_ids:
  - ev-dd543473682e90e0
  - ev-27e63e3ab2cdc2ac
  - ev-38c565967318deef
  - ev-4568f0319abf9f21
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-7fc392eabcbadcbc
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-bfa0fd3f8e644ade
  evidence_ids:
  - ev-382857f1bc834099
  - ev-dd543473682e90e0
  - ev-bfbec2f55af14289
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T06:59:02Z;
    reviewed SHA-256=06abd4f73cfcd093312622a2d40c84e6f7f5121381559b57f7682de478726c8d;
    current SHA-256=06abd4f73cfcd093312622a2d40c84e6f7f5121381559b57f7682de478726c8d;
    hash_changed=False. Reports=["reports/yaml_record_review/Abyssomicin_H.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The placeholder
    kgmicrobe identity is intentionally retained pending exact ontology identity;
    OLS candidate review found no exact match, but the selective-agent role is still
    only provisional computational curation.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-382857f1bc834099
    - ev-dd543473682e90e0
  - name: legacy-native-ids
    value: '["SEM:10f9d72353b33e78bf7e","SEM:2723e9cae2241a16bab0"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-dd543473682e90e0
    - ev-382857f1bc834099
    - ev-bfbec2f55af14289
- assessment_id: a-de56f594687a1cd8
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-bfa0fd3f8e644ade
  evidence_ids:
  - ev-382857f1bc834099
  - ev-de56f594687a1cd8
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-382857f1bc834099
    - ev-de56f594687a1cd8
findings:
- finding_id: rec-f-4d5433329f7afa93
  issue_key: mim-reconciliation-role-support-bfa0fd3f8e644ade
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Abyssomicin H'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-bfa0fd3f8e644ade
  evidence_ids:
  - ev-382857f1bc834099
  - ev-de56f594687a1cd8
  - ev-982496d0b66bf22a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Abyssomicin_H.yaml
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
    review_id: 20261011T024630Z-mim-reconcile-all-batch-02
    finding_id: f-4d5433329f7afa93
actions:
- action_id: rec-action-4d5433329f7afa93
  description: 'Reassess prediction-only role support: Abyssomicin H'
  finding_ids:
  - rec-f-4d5433329f7afa93
  target_ids:
  - record-bfa0fd3f8e644ade
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Abyssomicin_H.yaml
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
  with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.
```
