# Per-record structured review: Betaine_X_H2o (data/ingredients/mapped/Betaine_X_H2o.yaml)

- Review: 20261017T083000Z-betaine-x-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Betaine_X_H2o (data/ingredients/mapped/Betaine_X_H2o.yaml, record-c5f266d9bae4724f, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Betaine_X_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Betaine_X_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-c5f266d9bae4724f | data/ingredients/mapped/Betaine_X_H2o.yaml | maintained | Betaine_X_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-c5f266d9bae4724f | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-c5f266d9bae4724f | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-c5f266d9bae4724f | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-c5f266d9bae4724f.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-c5f266d9bae4724f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T09:47:04Z; reviewed SHA-256=30e8e68f84a2fb6e866ce4356a4514f21701286b04a0f70847d6bf9cb2a0320f; current SHA-256=30e8e68f84a2fb6e866ce4356a4514f21701286b04a0f70847d6bf9cb2a0320f; hash_changed=False. Reports=["reports/yaml_record_review/Betaine_X_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI glycine betaine hydrate identity, hydrate structure fields, CAS, SSSOM row, and aggregate copy pass, but active mapping evidence still carries superseded parent/registry notes.

## Findings

### rec-f-d9d83927fea018a1: Historical review coverage and residual narrative: Betaine_X_H2o

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-c5f266d9bae4724f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T09:47:04Z; reviewed SHA-256=30e8e68f84a2fb6e866ce4356a4514f21701286b04a0f70847d6bf9cb2a0320f; current SHA-256=30e8e68f84a2fb6e866ce4356a4514f21701286b04a0f70847d6bf9cb2a0320f; hash_changed=False. Reports=["reports/yaml_record_review/Betaine_X_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI glycine betaine hydrate identity, hydrate structure fields, CAS, SSSOM row, and aggregate copy pass, but active mapping evidence still carries superseded parent/registry notes.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-e64aafad673c87de | data/ingredients/mapped/Betaine_X_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[583],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:91242","line":585,"mapping_status":"MAPPED","ontology_id":"CHEBI:91242","preferred_term":"Betaine x H2O"}],"identifier":"CHEBI:91242","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":40,"edge_count":40,"occurrences":40},"occurrence_statistics":{"media_count":40,"total_occurrences":40},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:91242","ontology_label":"glycine betaine hydrate","ontology_source":"CHEBI"},"preferred_term":"Betaine x H2O","sssom_rows":[{"data_row":538,"object_id":"CHEBI:91242","object_label":"glycine betaine hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Betaine_X_H2o","synonym_count":4} |
| ev-5b364b3d801ef8cf | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [583] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-cad9116d0c990c18 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Betaine_X_H2o; data-row positions=[538] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":538,"object_id":"CHEBI:91242","object_label":"glycine betaine hydrate","other":"(trimethylazaniumyl)acetate--water (1/1)&#124;carboxy-N,N,N-trimethylmethanaminium hydroxide&#124;CAS:590-47-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Betaine_X_H2o","validation_method":""}] |
| ev-7383ea0508702242 | docs/data/mapped_ingredients.csv; CSV lines=[585] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:91242","line":585,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"40","ontology_id":"CHEBI:91242","preferred_term":"Betaine x H2O","total_occurrences":"40"}] |
| ev-e6a7f2c353acf4ba | reports/yaml_record_review/Betaine_X_H2o.md; &#96;data/ingredients/mapped/Betaine_X_H2o.yaml&#96;:2; Verdict:4; Identity:12; Validation:24; Evidence:37; Completeness:53; Recommended Edits:63 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-462ba14e726fb65d | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[312] | context_only | [{"current_record_sha256":"30e8e68f84a2fb6e866ce4356a4514f21701286b04a0f70847d6bf9cb2a0320f","finding_id":"SEM:017902c6c3ff4d2375ca","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-betaine-x-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Betaine_X_H2o (data/ingredients/mapped/Betaine_X_H2o.yaml)'
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
summary: Per-record structured review for Betaine_X_H2o (data/ingredients/mapped/Betaine_X_H2o.yaml,
  record-c5f266d9bae4724f, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Betaine_X_H2o.yaml
    sha256: 30e8e68f84a2fb6e866ce4356a4514f21701286b04a0f70847d6bf9cb2a0320f
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
  - path: reports/yaml_record_review/Betaine_X_H2o.md
    sha256: e03ace15ffb7a260b5d89e18f9faeba249a981340f756942266ea0a9ef74d8e0
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-c5f266d9bae4724f
  path: data/ingredients/mapped/Betaine_X_H2o.yaml
  label: Betaine_X_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Betaine_X_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Betaine_X_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Betaine_X_H2o.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-c5f266d9bae4724f
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-c5f266d9bae4724f
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-c5f266d9bae4724f
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-c5f266d9bae4724f
evidence:
- evidence_id: ev-e64aafad673c87de
  kind: record_content
  reference: data/ingredients/mapped/Betaine_X_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[583],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:91242","line":585,"mapping_status":"MAPPED","ontology_id":"CHEBI:91242","preferred_term":"Betaine
    x H2O"}],"identifier":"CHEBI:91242","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":40,"edge_count":40,"occurrences":40},"occurrence_statistics":{"media_count":40,"total_occurrences":40},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:91242","ontology_label":"glycine
    betaine hydrate","ontology_source":"CHEBI"},"preferred_term":"Betaine x H2O","sssom_rows":[{"data_row":538,"object_id":"CHEBI:91242","object_label":"glycine
    betaine hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Betaine_X_H2o","synonym_count":4}'
  snapshot_sha256: 30e8e68f84a2fb6e866ce4356a4514f21701286b04a0f70847d6bf9cb2a0320f
- evidence_id: ev-5b364b3d801ef8cf
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [583]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-cad9116d0c990c18
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Betaine_X_H2o; data-row positions=[538]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":538,"object_id":"CHEBI:91242","object_label":"glycine
    betaine hydrate","other":"(trimethylazaniumyl)acetate--water (1/1)|carboxy-N,N,N-trimethylmethanaminium
    hydroxide|CAS:590-47-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Betaine_X_H2o","validation_method":""}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-7383ea0508702242
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[585]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:91242","line":585,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"40","ontology_id":"CHEBI:91242","preferred_term":"Betaine
    x H2O","total_occurrences":"40"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-e6a7f2c353acf4ba
  kind: prior_review
  reference: reports/yaml_record_review/Betaine_X_H2o.md
  locator: '`data/ingredients/mapped/Betaine_X_H2o.yaml`:2; Verdict:4; Identity:12;
    Validation:24; Evidence:37; Completeness:53; Recommended Edits:63'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: e03ace15ffb7a260b5d89e18f9faeba249a981340f756942266ea0a9ef74d8e0
  quote: "Recommended Edits:\n- Minor: prune the superseded #321/#334/#342 parent\
    \ evidence from\n  `data/ingredients/mapped/Betaine_X_H2o.yaml` and keep only\
    \ evidence that\n  supports the current exact `CHEBI:91242` identity. Then run\n\
    \  `just sync-curated` and focused strict/term validation."
- evidence_id: ev-462ba14e726fb65d
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[312]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"30e8e68f84a2fb6e866ce4356a4514f21701286b04a0f70847d6bf9cb2a0320f","finding_id":"SEM:017902c6c3ff4d2375ca","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-1985a07532990cb1
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-c5f266d9bae4724f
  evidence_ids:
  - ev-e64aafad673c87de
  - ev-5b364b3d801ef8cf
  - ev-cad9116d0c990c18
  - ev-7383ea0508702242
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-28ce244f7d8ecd29
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-c5f266d9bae4724f
  evidence_ids:
  - ev-e6a7f2c353acf4ba
  - ev-e64aafad673c87de
  - ev-462ba14e726fb65d
  details: 'Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T09:47:04Z;
    reviewed SHA-256=30e8e68f84a2fb6e866ce4356a4514f21701286b04a0f70847d6bf9cb2a0320f;
    current SHA-256=30e8e68f84a2fb6e866ce4356a4514f21701286b04a0f70847d6bf9cb2a0320f;
    hash_changed=False. Reports=["reports/yaml_record_review/Betaine_X_H2o.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    glycine betaine hydrate identity, hydrate structure fields, CAS, SSSOM row, and
    aggregate copy pass, but active mapping evidence still carries superseded parent/registry
    notes.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-e6a7f2c353acf4ba
    - ev-e64aafad673c87de
  - name: legacy-native-ids
    value: '["SEM:017902c6c3ff4d2375ca"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-e64aafad673c87de
    - ev-e6a7f2c353acf4ba
    - ev-462ba14e726fb65d
findings:
- finding_id: rec-f-d9d83927fea018a1
  issue_key: mim-reconciliation-historical-review-coverage-and-r-c5f266d9bae4724f
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Betaine_X_H2o'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T09:47:04Z;
    reviewed SHA-256=30e8e68f84a2fb6e866ce4356a4514f21701286b04a0f70847d6bf9cb2a0320f;
    current SHA-256=30e8e68f84a2fb6e866ce4356a4514f21701286b04a0f70847d6bf9cb2a0320f;
    hash_changed=False. Reports=["reports/yaml_record_review/Betaine_X_H2o.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    glycine betaine hydrate identity, hydrate structure fields, CAS, SSSOM row, and
    aggregate copy pass, but active mapping evidence still carries superseded parent/registry
    notes.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-c5f266d9bae4724f
  evidence_ids:
  - ev-e6a7f2c353acf4ba
  - ev-e64aafad673c87de
  - ev-462ba14e726fb65d
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Betaine_X_H2o.yaml
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
  with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.
```
