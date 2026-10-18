# Per-record structured review: 2-deoxyuridine (data/ingredients/mapped/2-deoxyuridine.yaml)

- Review: 20261017T083000Z-2-deoxyuridine
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 2-deoxyuridine (data/ingredients/mapped/2-deoxyuridine.yaml, record-50551c3d61855298, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/2-deoxyuridine.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/2-deoxyuridine.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-50551c3d61855298 | data/ingredients/mapped/2-deoxyuridine.yaml | maintained | 2-deoxyuridine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-50551c3d61855298 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-50551c3d61855298 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-50551c3d61855298 | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-50551c3d61855298.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-50551c3d61855298.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T05:39:45Z; reviewed SHA-256=83bfa7a3eff6ca4f5bb7075f09697ce983dd2847f19333f70a33fdf575831647; current SHA-256=83bfa7a3eff6ca4f5bb7075f09697ce983dd2847f19333f70a33fdf575831647; hash_changed=False. Reports=["reports/yaml_record_review/2-deoxyuridine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Active CAS-grounded CHEBI identity, FEBA occurrence count, SSSOM, aggregate, and docs pass; only stale advisory rows remain.

## Findings

### rec-f-dd9373e22e2d0c35: Historical review coverage and residual narrative: 2-deoxyuridine

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-50551c3d61855298.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T05:39:45Z; reviewed SHA-256=83bfa7a3eff6ca4f5bb7075f09697ce983dd2847f19333f70a33fdf575831647; current SHA-256=83bfa7a3eff6ca4f5bb7075f09697ce983dd2847f19333f70a33fdf575831647; hash_changed=False. Reports=["reports/yaml_record_review/2-deoxyuridine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Active CAS-grounded CHEBI identity, FEBA occurrence count, SSSOM, aggregate, and docs pass; only stale advisory rows remain.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-b64c89a8a5feee23 | data/ingredients/mapped/2-deoxyuridine.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[344],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16450","line":346,"mapping_status":"MAPPED","ontology_id":"CHEBI:16450","preferred_term":"2'-Deoxyuridine"}],"identifier":"CHEBI:16450","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4,"edge_count":4,"occurrences":4},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:16450","ontology_label":"2'-deoxyuridine","ontology_source":"CHEBI"},"preferred_term":"2'-Deoxyuridine","sssom_rows":[{"data_row":83,"object_id":"CHEBI:16450","object_label":"2'-deoxyuridine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:2-deoxyuridine","synonym_count":4} |
| ev-10b34f2ebabc565e | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [344] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-dd904dd95e1a237d | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:2-deoxyuridine; data-row positions=[83] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":83,"object_id":"CHEBI:16450","object_label":"2'-deoxyuridine","other":"1-(2-deoxy-beta-D-erythro-pentofuranosyl)uracil&#124;2-Deoxyuridine&#124;Deoxyuridine&#124;dU&#124;CAS:951-78-0","predicate_id":"skos:exactMatch","subject_id":"MIM:2-deoxyuridine","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-67e3f5ea65b75e12 | docs/data/mapped_ingredients.csv; CSV lines=[346] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:16450","line":346,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"4","ontology_id":"CHEBI:16450","preferred_term":"2'-Deoxyuridine","total_occurrences":"4"}] |
| ev-c82e85f302a7f961 | reports/yaml_record_review/2-deoxyuridine.md; &#96;data/ingredients/mapped/2-deoxyuridine.yaml&#96;:2; Verdict:4; Identity:10; Validation:23; Evidence:37; Completeness:50; Recommended Edits:57 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-f040c8a0df90cd74 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[65] | context_only | [{"current_record_sha256":"83bfa7a3eff6ca4f5bb7075f09697ce983dd2847f19333f70a33fdf575831647","finding_id":"SEM:26862a9ba4cdcf4ae357","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-2-deoxyuridine
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 2-deoxyuridine (data/ingredients/mapped/2-deoxyuridine.yaml)'
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
summary: Per-record structured review for 2-deoxyuridine (data/ingredients/mapped/2-deoxyuridine.yaml,
  record-50551c3d61855298, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/2-deoxyuridine.yaml
    sha256: 83bfa7a3eff6ca4f5bb7075f09697ce983dd2847f19333f70a33fdf575831647
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
  - path: reports/yaml_record_review/2-deoxyuridine.md
    sha256: ce57702fcd5fd8658ecedc174c3b6cd89246b137c21ca784b7dcee615ff49919
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-50551c3d61855298
  path: data/ingredients/mapped/2-deoxyuridine.yaml
  label: 2-deoxyuridine
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/2-deoxyuridine.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/2-deoxyuridine.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/2-deoxyuridine.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-50551c3d61855298
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-50551c3d61855298
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-50551c3d61855298
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-50551c3d61855298
evidence:
- evidence_id: ev-b64c89a8a5feee23
  kind: record_content
  reference: data/ingredients/mapped/2-deoxyuridine.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[344],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16450","line":346,"mapping_status":"MAPPED","ontology_id":"CHEBI:16450","preferred_term":"2''-Deoxyuridine"}],"identifier":"CHEBI:16450","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4,"edge_count":4,"occurrences":4},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:16450","ontology_label":"2''-deoxyuridine","ontology_source":"CHEBI"},"preferred_term":"2''-Deoxyuridine","sssom_rows":[{"data_row":83,"object_id":"CHEBI:16450","object_label":"2''-deoxyuridine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:2-deoxyuridine","synonym_count":4}'
  snapshot_sha256: 83bfa7a3eff6ca4f5bb7075f09697ce983dd2847f19333f70a33fdf575831647
- evidence_id: ev-10b34f2ebabc565e
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [344]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-dd904dd95e1a237d
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:2-deoxyuridine; data-row positions=[83]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":83,"object_id":"CHEBI:16450","object_label":"2''-deoxyuridine","other":"1-(2-deoxy-beta-D-erythro-pentofuranosyl)uracil|2-Deoxyuridine|Deoxyuridine|dU|CAS:951-78-0","predicate_id":"skos:exactMatch","subject_id":"MIM:2-deoxyuridine","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-67e3f5ea65b75e12
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[346]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:16450","line":346,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"4","ontology_id":"CHEBI:16450","preferred_term":"2''-Deoxyuridine","total_occurrences":"4"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-c82e85f302a7f961
  kind: prior_review
  reference: reports/yaml_record_review/2-deoxyuridine.md
  locator: '`data/ingredients/mapped/2-deoxyuridine.yaml`:2; Verdict:4; Identity:10;
    Validation:23; Evidence:37; Completeness:50; Recommended Edits:57'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: ce57702fcd5fd8658ecedc174c3b6cd89246b137c21ca784b7dcee615ff49919
  quote: "Recommended Edits:\n1. If `mappings/record_research_validation.tsv` is intended\
    \ to be a live queue,\n   regenerate it so stale `CHEBI:16450` uncertainty no\
    \ longer implies pending\n   work.\n2. No YAML, aggregate, SSSOM, or docs identity\
    \ edit is needed for the active\n   `2-deoxyuridine` record."
- evidence_id: ev-f040c8a0df90cd74
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[65]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"83bfa7a3eff6ca4f5bb7075f09697ce983dd2847f19333f70a33fdf575831647","finding_id":"SEM:26862a9ba4cdcf4ae357","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-369681c72b1428e5
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-50551c3d61855298
  evidence_ids:
  - ev-b64c89a8a5feee23
  - ev-10b34f2ebabc565e
  - ev-dd904dd95e1a237d
  - ev-67e3f5ea65b75e12
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-fbdadf62da435141
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-50551c3d61855298
  evidence_ids:
  - ev-c82e85f302a7f961
  - ev-b64c89a8a5feee23
  - ev-f040c8a0df90cd74
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T05:39:45Z;
    reviewed SHA-256=83bfa7a3eff6ca4f5bb7075f09697ce983dd2847f19333f70a33fdf575831647;
    current SHA-256=83bfa7a3eff6ca4f5bb7075f09697ce983dd2847f19333f70a33fdf575831647;
    hash_changed=False. Reports=["reports/yaml_record_review/2-deoxyuridine.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Active CAS-grounded
    CHEBI identity, FEBA occurrence count, SSSOM, aggregate, and docs pass; only stale
    advisory rows remain.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c82e85f302a7f961
    - ev-b64c89a8a5feee23
  - name: legacy-native-ids
    value: '["SEM:26862a9ba4cdcf4ae357"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-b64c89a8a5feee23
    - ev-c82e85f302a7f961
    - ev-f040c8a0df90cd74
findings:
- finding_id: rec-f-dd9373e22e2d0c35
  issue_key: mim-reconciliation-historical-review-coverage-and-r-50551c3d61855298
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: 2-deoxyuridine'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T05:39:45Z;
    reviewed SHA-256=83bfa7a3eff6ca4f5bb7075f09697ce983dd2847f19333f70a33fdf575831647;
    current SHA-256=83bfa7a3eff6ca4f5bb7075f09697ce983dd2847f19333f70a33fdf575831647;
    hash_changed=False. Reports=["reports/yaml_record_review/2-deoxyuridine.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Active CAS-grounded
    CHEBI identity, FEBA occurrence count, SSSOM, aggregate, and docs pass; only stale
    advisory rows remain.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-50551c3d61855298
  evidence_ids:
  - ev-c82e85f302a7f961
  - ev-b64c89a8a5feee23
  - ev-f040c8a0df90cd74
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/2-deoxyuridine.yaml
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
