# Per-record structured review: 4-Hydroxybenzaldehyde (data/ingredients/mapped/4-Hydroxybenzaldehyde.yaml)

- Review: 20261017T083000Z-4-hydroxybenzaldehyde
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 4-Hydroxybenzaldehyde (data/ingredients/mapped/4-Hydroxybenzaldehyde.yaml, record-1b45012527209bfe, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/4-Hydroxybenzaldehyde.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/4-Hydroxybenzaldehyde.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-1b45012527209bfe | data/ingredients/mapped/4-Hydroxybenzaldehyde.yaml | maintained | 4-Hydroxybenzaldehyde |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-1b45012527209bfe | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-1b45012527209bfe | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-1b45012527209bfe | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-1b45012527209bfe.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-1b45012527209bfe.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T06:16:09Z; reviewed SHA-256=26708596b1e101638e7244d761c1ca228529d533069bd6e2ebad6985e61b0744; current SHA-256=26708596b1e101638e7244d761c1ca228529d533069bd6e2ebad6985e61b0744; hash_changed=False. Reports=["reports/yaml_record_review/4-Hydroxybenzaldehyde.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Official CHEBI and PubChem identity, CAS, chemistry, SSSOM, and aggregate pass; only stale advisory rows remain.

## Findings

### rec-f-90690b3203384180: Historical review coverage and residual narrative: 4-Hydroxybenzaldehyde

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-1b45012527209bfe.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T06:16:09Z; reviewed SHA-256=26708596b1e101638e7244d761c1ca228529d533069bd6e2ebad6985e61b0744; current SHA-256=26708596b1e101638e7244d761c1ca228529d533069bd6e2ebad6985e61b0744; hash_changed=False. Reports=["reports/yaml_record_review/4-Hydroxybenzaldehyde.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Official CHEBI and PubChem identity, CAS, chemistry, SSSOM, and aggregate pass; only stale advisory rows remain.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-68fd3ba4a7fb7547 | data/ingredients/mapped/4-Hydroxybenzaldehyde.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[379],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17597","line":381,"mapping_status":"MAPPED","ontology_id":"CHEBI:17597","preferred_term":"4-Hydroxybenzaldehyde"}],"identifier":"CHEBI:17597","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17597","ontology_label":"4-hydroxybenzaldehyde","ontology_source":"CHEBI"},"preferred_term":"4-Hydroxybenzaldehyde","sssom_rows":[{"data_row":176,"object_id":"CHEBI:17597","object_label":"4-hydroxybenzaldehyde","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:4-Hydroxybenzaldehyde","synonym_count":0} |
| ev-acc70f83583d4550 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [379] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-c2f1f1ed692f99b5 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:4-Hydroxybenzaldehyde; data-row positions=[176] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":176,"object_id":"CHEBI:17597","object_label":"4-hydroxybenzaldehyde","other":"CAS:123-08-0","predicate_id":"skos:exactMatch","subject_id":"MIM:4-Hydroxybenzaldehyde","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-0d021272d9a31938 | docs/data/mapped_ingredients.csv; CSV lines=[381] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:17597","line":381,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:17597","preferred_term":"4-Hydroxybenzaldehyde","total_occurrences":"2"}] |
| ev-5db3b05b3cbb733b | reports/yaml_record_review/4-Hydroxybenzaldehyde.md; &#96;data/ingredients/mapped/4-Hydroxybenzaldehyde.yaml&#96;:2; Verdict:4; Identity:10; Validation:23; Evidence:34; Completeness:50; Recommended Edits:58 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-857b030110a071e5 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[143] | context_only | [{"current_record_sha256":"26708596b1e101638e7244d761c1ca228529d533069bd6e2ebad6985e61b0744","finding_id":"SEM:3983e8120f7fddd0f305","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-4-hydroxybenzaldehyde
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 4-Hydroxybenzaldehyde (data/ingredients/mapped/4-Hydroxybenzaldehyde.yaml)'
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
summary: Per-record structured review for 4-Hydroxybenzaldehyde (data/ingredients/mapped/4-Hydroxybenzaldehyde.yaml,
  record-1b45012527209bfe, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/4-Hydroxybenzaldehyde.yaml
    sha256: 26708596b1e101638e7244d761c1ca228529d533069bd6e2ebad6985e61b0744
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
  - path: reports/yaml_record_review/4-Hydroxybenzaldehyde.md
    sha256: 84d375c2c0c5d81416b045a7a1dd69a22bd679d3f8c92dc38945c948eb2ddbb2
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-1b45012527209bfe
  path: data/ingredients/mapped/4-Hydroxybenzaldehyde.yaml
  label: 4-Hydroxybenzaldehyde
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/4-Hydroxybenzaldehyde.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/4-Hydroxybenzaldehyde.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/4-Hydroxybenzaldehyde.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-1b45012527209bfe
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-1b45012527209bfe
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-1b45012527209bfe
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-1b45012527209bfe
evidence:
- evidence_id: ev-68fd3ba4a7fb7547
  kind: record_content
  reference: data/ingredients/mapped/4-Hydroxybenzaldehyde.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[379],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17597","line":381,"mapping_status":"MAPPED","ontology_id":"CHEBI:17597","preferred_term":"4-Hydroxybenzaldehyde"}],"identifier":"CHEBI:17597","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17597","ontology_label":"4-hydroxybenzaldehyde","ontology_source":"CHEBI"},"preferred_term":"4-Hydroxybenzaldehyde","sssom_rows":[{"data_row":176,"object_id":"CHEBI:17597","object_label":"4-hydroxybenzaldehyde","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:4-Hydroxybenzaldehyde","synonym_count":0}'
  snapshot_sha256: 26708596b1e101638e7244d761c1ca228529d533069bd6e2ebad6985e61b0744
- evidence_id: ev-acc70f83583d4550
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [379]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-c2f1f1ed692f99b5
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:4-Hydroxybenzaldehyde; data-row positions=[176]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":176,"object_id":"CHEBI:17597","object_label":"4-hydroxybenzaldehyde","other":"CAS:123-08-0","predicate_id":"skos:exactMatch","subject_id":"MIM:4-Hydroxybenzaldehyde","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-0d021272d9a31938
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[381]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:17597","line":381,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:17597","preferred_term":"4-Hydroxybenzaldehyde","total_occurrences":"2"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-5db3b05b3cbb733b
  kind: prior_review
  reference: reports/yaml_record_review/4-Hydroxybenzaldehyde.md
  locator: '`data/ingredients/mapped/4-Hydroxybenzaldehyde.yaml`:2; Verdict:4; Identity:10;
    Validation:23; Evidence:34; Completeness:50; Recommended Edits:58'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 84d375c2c0c5d81416b045a7a1dd69a22bd679d3f8c92dc38945c948eb2ddbb2
  quote: 'Recommended Edits:

    No YAML edit is required for this record. If the stale advisory TSVs are ever

    regenerated, their `4-Hydroxybenzaldehyde` warnings should disappear.'
- evidence_id: ev-857b030110a071e5
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[143]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"26708596b1e101638e7244d761c1ca228529d533069bd6e2ebad6985e61b0744","finding_id":"SEM:3983e8120f7fddd0f305","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-016d77dcbd19c914
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-1b45012527209bfe
  evidence_ids:
  - ev-68fd3ba4a7fb7547
  - ev-acc70f83583d4550
  - ev-c2f1f1ed692f99b5
  - ev-0d021272d9a31938
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-af60940caf75ceb7
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-1b45012527209bfe
  evidence_ids:
  - ev-5db3b05b3cbb733b
  - ev-68fd3ba4a7fb7547
  - ev-857b030110a071e5
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T06:16:09Z;
    reviewed SHA-256=26708596b1e101638e7244d761c1ca228529d533069bd6e2ebad6985e61b0744;
    current SHA-256=26708596b1e101638e7244d761c1ca228529d533069bd6e2ebad6985e61b0744;
    hash_changed=False. Reports=["reports/yaml_record_review/4-Hydroxybenzaldehyde.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Official
    CHEBI and PubChem identity, CAS, chemistry, SSSOM, and aggregate pass; only stale
    advisory rows remain.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-5db3b05b3cbb733b
    - ev-68fd3ba4a7fb7547
  - name: legacy-native-ids
    value: '["SEM:3983e8120f7fddd0f305"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-68fd3ba4a7fb7547
    - ev-5db3b05b3cbb733b
    - ev-857b030110a071e5
findings:
- finding_id: rec-f-90690b3203384180
  issue_key: mim-reconciliation-historical-review-coverage-and-r-1b45012527209bfe
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: 4-Hydroxybenzaldehyde'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T06:16:09Z;
    reviewed SHA-256=26708596b1e101638e7244d761c1ca228529d533069bd6e2ebad6985e61b0744;
    current SHA-256=26708596b1e101638e7244d761c1ca228529d533069bd6e2ebad6985e61b0744;
    hash_changed=False. Reports=["reports/yaml_record_review/4-Hydroxybenzaldehyde.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Official
    CHEBI and PubChem identity, CAS, chemistry, SSSOM, and aggregate pass; only stale
    advisory rows remain.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-1b45012527209bfe
  evidence_ids:
  - ev-5db3b05b3cbb733b
  - ev-68fd3ba4a7fb7547
  - ev-857b030110a071e5
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/4-Hydroxybenzaldehyde.yaml
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
