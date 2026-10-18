# Per-record structured review: 20AA_mix (data/ingredients/mapped/20AA_mix.yaml)

- Review: 20261017T083000Z-20aa-mix
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 20AA_mix (data/ingredients/mapped/20AA_mix.yaml, record-a1f7771e08b49b89, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/20AA_mix.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/20AA_mix.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-a1f7771e08b49b89 | data/ingredients/mapped/20AA_mix.yaml | maintained | 20AA_mix |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-a1f7771e08b49b89 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-a1f7771e08b49b89 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-a1f7771e08b49b89 | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-a1f7771e08b49b89.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-a1f7771e08b49b89.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T05:48:52Z; reviewed SHA-256=a96a0f5565fdace2f151b345f8809f4375ce8c9d43c9e9b5ed8773a6ac939faa; current SHA-256=a96a0f5565fdace2f151b345f8809f4375ce8c9d43c9e9b5ed8773a6ac939faa; hash_changed=False. Reports=["reports/yaml_record_review/20AA_mix.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Local stock-solution identity, single CultureBotHT occurrence, SSSOM, aggregate, and docs pass; only stale local-CURIE advisory rows remain.

## Findings

### rec-f-0e617a3731d49e82: Historical review coverage and residual narrative: 20AA_mix

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-a1f7771e08b49b89.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T05:48:52Z; reviewed SHA-256=a96a0f5565fdace2f151b345f8809f4375ce8c9d43c9e9b5ed8773a6ac939faa; current SHA-256=a96a0f5565fdace2f151b345f8809f4375ce8c9d43c9e9b5ed8773a6ac939faa; hash_changed=False. Reports=["reports/yaml_record_review/20AA_mix.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Local stock-solution identity, single CultureBotHT occurrence, SSSOM, aggregate, and docs pass; only stale local-CURIE advisory rows remain.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-b9aafef23fd9ffe1 | data/ingredients/mapped/20AA_mix.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[114],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:20aa_mix","line":116,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:20aa_mix","preferred_term":"20AA_mix"}],"identifier":"kgmicrobe.ingredient:20aa_mix","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:20aa_mix","ontology_label":"20AA_mix","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"20AA_mix","sssom_rows":[{"data_row":103,"object_id":"kgmicrobe.ingredient:20aa_mix","object_label":"20AA_mix","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:20AA_mix","synonym_count":1} |
| ev-492b35f994105b86 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [114] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-7cf913de0a433bd8 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:20AA_mix; data-row positions=[103] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":103,"object_id":"kgmicrobe.ingredient:20aa_mix","object_label":"20AA_mix","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:20AA_mix","validation_method":"manual:promote_resolved_unmapped&#124;PROMOTED&#124;2026-08-06"}] |
| ev-a3472ece7ce093fb | docs/data/mapped_ingredients.csv; CSV lines=[116] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:20aa_mix","line":116,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"1","ontology_id":"kgmicrobe.ingredient:20aa_mix","preferred_term":"20AA_mix","total_occurrences":"1"}] |
| ev-0007056e16bc2f11 | reports/yaml_record_review/20AA_mix.md; &#96;data/ingredients/mapped/20AA_mix.yaml&#96;:2; Verdict:4; Identity:10; Validation:20; Evidence:35; Completeness:50; Recommended Edits:57 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-f71520e4b459ac0d | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[84] | context_only | [{"current_record_sha256":"a96a0f5565fdace2f151b345f8809f4375ce8c9d43c9e9b5ed8773a6ac939faa","finding_id":"SEM:fd41deb0ce52fe883af6","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-20aa-mix
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 20AA_mix (data/ingredients/mapped/20AA_mix.yaml)'
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
native_verdict: mapping_status=MAPPED; open=0; deferred=1
scientific_review: false
summary: Per-record structured review for 20AA_mix (data/ingredients/mapped/20AA_mix.yaml,
  record-a1f7771e08b49b89, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/20AA_mix.yaml
    sha256: a96a0f5565fdace2f151b345f8809f4375ce8c9d43c9e9b5ed8773a6ac939faa
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
  - path: reports/yaml_record_review/20AA_mix.md
    sha256: 95ffdf370da23fd56eafa615c080b54d1c16c0a953c5e0fceabbae53588a3e06
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-a1f7771e08b49b89
  path: data/ingredients/mapped/20AA_mix.yaml
  label: 20AA_mix
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/20AA_mix.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/20AA_mix.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/20AA_mix.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-a1f7771e08b49b89
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-a1f7771e08b49b89
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-a1f7771e08b49b89
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-a1f7771e08b49b89
evidence:
- evidence_id: ev-b9aafef23fd9ffe1
  kind: record_content
  reference: data/ingredients/mapped/20AA_mix.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[114],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:20aa_mix","line":116,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:20aa_mix","preferred_term":"20AA_mix"}],"identifier":"kgmicrobe.ingredient:20aa_mix","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:20aa_mix","ontology_label":"20AA_mix","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"20AA_mix","sssom_rows":[{"data_row":103,"object_id":"kgmicrobe.ingredient:20aa_mix","object_label":"20AA_mix","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:20AA_mix","synonym_count":1}'
  snapshot_sha256: a96a0f5565fdace2f151b345f8809f4375ce8c9d43c9e9b5ed8773a6ac939faa
- evidence_id: ev-492b35f994105b86
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [114]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-7cf913de0a433bd8
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:20AA_mix; data-row positions=[103]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":103,"object_id":"kgmicrobe.ingredient:20aa_mix","object_label":"20AA_mix","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:20AA_mix","validation_method":"manual:promote_resolved_unmapped|PROMOTED|2026-08-06"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-a3472ece7ce093fb
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[116]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:20aa_mix","line":116,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"1","ontology_id":"kgmicrobe.ingredient:20aa_mix","preferred_term":"20AA_mix","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-0007056e16bc2f11
  kind: prior_review
  reference: reports/yaml_record_review/20AA_mix.md
  locator: '`data/ingredients/mapped/20AA_mix.yaml`:2; Verdict:4; Identity:10; Validation:20;
    Evidence:35; Completeness:50; Recommended Edits:57'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 95ffdf370da23fd56eafa615c080b54d1c16c0a953c5e0fceabbae53588a3e06
  quote: "Recommended Edits:\n1. No curation edit is required for `data/ingredients/mapped/20AA_mix.yaml`.\n\
    2. When stale advisory artifacts are next regenerated, confirm the obsolete\n\
    \   local-CURIE findings drop out for this record."
- evidence_id: ev-f71520e4b459ac0d
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[84]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"a96a0f5565fdace2f151b345f8809f4375ce8c9d43c9e9b5ed8773a6ac939faa","finding_id":"SEM:fd41deb0ce52fe883af6","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-4c97799242ce79c7
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-a1f7771e08b49b89
  evidence_ids:
  - ev-b9aafef23fd9ffe1
  - ev-492b35f994105b86
  - ev-7cf913de0a433bd8
  - ev-a3472ece7ce093fb
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-2e1bff63f3f7a0dd
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-a1f7771e08b49b89
  evidence_ids:
  - ev-0007056e16bc2f11
  - ev-b9aafef23fd9ffe1
  - ev-f71520e4b459ac0d
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T05:48:52Z;
    reviewed SHA-256=a96a0f5565fdace2f151b345f8809f4375ce8c9d43c9e9b5ed8773a6ac939faa;
    current SHA-256=a96a0f5565fdace2f151b345f8809f4375ce8c9d43c9e9b5ed8773a6ac939faa;
    hash_changed=False. Reports=["reports/yaml_record_review/20AA_mix.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: Local stock-solution identity,
    single CultureBotHT occurrence, SSSOM, aggregate, and docs pass; only stale local-CURIE
    advisory rows remain.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0007056e16bc2f11
    - ev-b9aafef23fd9ffe1
  - name: legacy-native-ids
    value: '["SEM:fd41deb0ce52fe883af6"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-b9aafef23fd9ffe1
    - ev-0007056e16bc2f11
    - ev-f71520e4b459ac0d
findings:
- finding_id: rec-f-0e617a3731d49e82
  issue_key: mim-reconciliation-historical-review-coverage-and-r-a1f7771e08b49b89
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: 20AA_mix'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T05:48:52Z;
    reviewed SHA-256=a96a0f5565fdace2f151b345f8809f4375ce8c9d43c9e9b5ed8773a6ac939faa;
    current SHA-256=a96a0f5565fdace2f151b345f8809f4375ce8c9d43c9e9b5ed8773a6ac939faa;
    hash_changed=False. Reports=["reports/yaml_record_review/20AA_mix.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: Local stock-solution identity,
    single CultureBotHT occurrence, SSSOM, aggregate, and docs pass; only stale local-CURIE
    advisory rows remain.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-a1f7771e08b49b89
  evidence_ids:
  - ev-0007056e16bc2f11
  - ev-b9aafef23fd9ffe1
  - ev-f71520e4b459ac0d
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/20AA_mix.yaml
    role: maintained ingredient
  field_paths:
  - curation_history
  tags:
  - reconciliation
  - bundle-by-owner
  - historical-review-coverage-and-r
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
actions: []
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
