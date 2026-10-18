# Per-record structured review: 4-Methyl-2-oxovaleric_Acid (data/ingredients/mapped/4-Methyl-2-oxovaleric_Acid.yaml)

- Review: 20261017T083000Z-4-methyl-2-oxovaleric-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 4-Methyl-2-oxovaleric_Acid (data/ingredients/mapped/4-Methyl-2-oxovaleric_Acid.yaml, record-fcf8cee8dc62381f, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/4-Methyl-2-oxovaleric_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/4-Methyl-2-oxovaleric_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-fcf8cee8dc62381f | data/ingredients/mapped/4-Methyl-2-oxovaleric_Acid.yaml | maintained | 4-Methyl-2-oxovaleric_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-fcf8cee8dc62381f | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-fcf8cee8dc62381f | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-fcf8cee8dc62381f | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-fcf8cee8dc62381f.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-fcf8cee8dc62381f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T06:18:15Z; reviewed SHA-256=8de711f4ed9b972971a6ecce2fcb1e7e790b245b92efadbe48dc854a5f601c8b; current SHA-256=8de711f4ed9b972971a6ecce2fcb1e7e790b245b92efadbe48dc854a5f601c8b; hash_changed=False. Reports=["reports/yaml_record_review/4-Methyl-2-oxovaleric_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The neutral CHEBI identity and chemistry pass, but the conjugate-base anion remains an exact synonym and publishes through SSSOM.

## Findings

### rec-f-1e49669461c14e37: Historical review coverage and residual narrative: 4-Methyl-2-oxovaleric_Acid

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-fcf8cee8dc62381f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T06:18:15Z; reviewed SHA-256=8de711f4ed9b972971a6ecce2fcb1e7e790b245b92efadbe48dc854a5f601c8b; current SHA-256=8de711f4ed9b972971a6ecce2fcb1e7e790b245b92efadbe48dc854a5f601c8b; hash_changed=False. Reports=["reports/yaml_record_review/4-Methyl-2-oxovaleric_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The neutral CHEBI identity and chemistry pass, but the conjugate-base anion remains an exact synonym and publishes through SSSOM.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-a2fda6e1609f0c69 | data/ingredients/mapped/4-Methyl-2-oxovaleric_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[385],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:48430","line":387,"mapping_status":"MAPPED","ontology_id":"CHEBI:48430","preferred_term":"4-Methyl-2-oxovaleric acid"}],"identifier":"CHEBI:48430","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:48430","ontology_label":"4-methyl-2-oxopentanoic acid","ontology_source":"CHEBI"},"preferred_term":"4-Methyl-2-oxovaleric acid","sssom_rows":[{"data_row":187,"object_id":"CHEBI:48430","object_label":"4-methyl-2-oxopentanoic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:4-Methyl-2-oxovaleric_Acid","synonym_count":1} |
| ev-a9d2cc4e13dae9ce | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [385] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-7df264d781cdfab0 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:4-Methyl-2-oxovaleric_Acid; data-row positions=[187] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":187,"object_id":"CHEBI:48430","object_label":"4-methyl-2-oxopentanoic acid","other":"4-Methyl-2-oxopentanoate&#124;CAS:816-66-0","predicate_id":"skos:exactMatch","subject_id":"MIM:4-Methyl-2-oxovaleric_Acid","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-de989d968877495f | docs/data/mapped_ingredients.csv; CSV lines=[387] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:48430","line":387,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:48430","preferred_term":"4-Methyl-2-oxovaleric acid","total_occurrences":"0"}] |
| ev-994e0b0e6a434543 | reports/yaml_record_review/4-Methyl-2-oxovaleric_Acid.md; &#96;data/ingredients/mapped/4-Methyl-2-oxovaleric_Acid.yaml&#96;:2; Verdict:4; Identity:10; Validation:24; Evidence:35; Completeness:52; Recommended Edits:58 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-39890bbb472d9ec9 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[148] | context_only | [{"current_record_sha256":"8de711f4ed9b972971a6ecce2fcb1e7e790b245b92efadbe48dc854a5f601c8b","finding_id":"SEM:52edb806faa358d29eb8","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-4-methyl-2-oxovaleric-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 4-Methyl-2-oxovaleric_Acid (data/ingredients/mapped/4-Methyl-2-oxovaleric_Acid.yaml)'
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
summary: Per-record structured review for 4-Methyl-2-oxovaleric_Acid (data/ingredients/mapped/4-Methyl-2-oxovaleric_Acid.yaml,
  record-fcf8cee8dc62381f, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/4-Methyl-2-oxovaleric_Acid.yaml
    sha256: 8de711f4ed9b972971a6ecce2fcb1e7e790b245b92efadbe48dc854a5f601c8b
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
  - path: reports/yaml_record_review/4-Methyl-2-oxovaleric_Acid.md
    sha256: 8f728d85c65dc2ae4ddd6dce394a3238b35b9bee58df8ff866142726560c6edc
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-fcf8cee8dc62381f
  path: data/ingredients/mapped/4-Methyl-2-oxovaleric_Acid.yaml
  label: 4-Methyl-2-oxovaleric_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/4-Methyl-2-oxovaleric_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/4-Methyl-2-oxovaleric_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/4-Methyl-2-oxovaleric_Acid.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-fcf8cee8dc62381f
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-fcf8cee8dc62381f
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-fcf8cee8dc62381f
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-fcf8cee8dc62381f
evidence:
- evidence_id: ev-a2fda6e1609f0c69
  kind: record_content
  reference: data/ingredients/mapped/4-Methyl-2-oxovaleric_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[385],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:48430","line":387,"mapping_status":"MAPPED","ontology_id":"CHEBI:48430","preferred_term":"4-Methyl-2-oxovaleric
    acid"}],"identifier":"CHEBI:48430","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:48430","ontology_label":"4-methyl-2-oxopentanoic
    acid","ontology_source":"CHEBI"},"preferred_term":"4-Methyl-2-oxovaleric acid","sssom_rows":[{"data_row":187,"object_id":"CHEBI:48430","object_label":"4-methyl-2-oxopentanoic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:4-Methyl-2-oxovaleric_Acid","synonym_count":1}'
  snapshot_sha256: 8de711f4ed9b972971a6ecce2fcb1e7e790b245b92efadbe48dc854a5f601c8b
- evidence_id: ev-a9d2cc4e13dae9ce
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [385]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-7df264d781cdfab0
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:4-Methyl-2-oxovaleric_Acid; data-row positions=[187]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":187,"object_id":"CHEBI:48430","object_label":"4-methyl-2-oxopentanoic
    acid","other":"4-Methyl-2-oxopentanoate|CAS:816-66-0","predicate_id":"skos:exactMatch","subject_id":"MIM:4-Methyl-2-oxovaleric_Acid","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-de989d968877495f
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[387]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:48430","line":387,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:48430","preferred_term":"4-Methyl-2-oxovaleric
    acid","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-994e0b0e6a434543
  kind: prior_review
  reference: reports/yaml_record_review/4-Methyl-2-oxovaleric_Acid.md
  locator: '`data/ingredients/mapped/4-Methyl-2-oxovaleric_Acid.yaml`:2; Verdict:4;
    Identity:10; Validation:24; Evidence:35; Completeness:52; Recommended Edits:58'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 8f728d85c65dc2ae4ddd6dce394a3238b35b9bee58df8ff866142726560c6edc
  quote: 'Recommended Edits:

    Remove or demote `4-Methyl-2-oxopentanoate` so the anion no longer publishes as

    an exact neutral-acid synonym, then resync the aggregate and rebuild SSSOM/docs.'
- evidence_id: ev-39890bbb472d9ec9
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[148]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"8de711f4ed9b972971a6ecce2fcb1e7e790b245b92efadbe48dc854a5f601c8b","finding_id":"SEM:52edb806faa358d29eb8","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-20817546f278eb6e
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-fcf8cee8dc62381f
  evidence_ids:
  - ev-a2fda6e1609f0c69
  - ev-a9d2cc4e13dae9ce
  - ev-7df264d781cdfab0
  - ev-de989d968877495f
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-fe6e8531496608fd
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-fcf8cee8dc62381f
  evidence_ids:
  - ev-994e0b0e6a434543
  - ev-a2fda6e1609f0c69
  - ev-39890bbb472d9ec9
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T06:18:15Z;
    reviewed SHA-256=8de711f4ed9b972971a6ecce2fcb1e7e790b245b92efadbe48dc854a5f601c8b;
    current SHA-256=8de711f4ed9b972971a6ecce2fcb1e7e790b245b92efadbe48dc854a5f601c8b;
    hash_changed=False. Reports=["reports/yaml_record_review/4-Methyl-2-oxovaleric_Acid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The neutral
    CHEBI identity and chemistry pass, but the conjugate-base anion remains an exact
    synonym and publishes through SSSOM.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-994e0b0e6a434543
    - ev-a2fda6e1609f0c69
  - name: legacy-native-ids
    value: '["SEM:52edb806faa358d29eb8"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-a2fda6e1609f0c69
    - ev-994e0b0e6a434543
    - ev-39890bbb472d9ec9
findings:
- finding_id: rec-f-1e49669461c14e37
  issue_key: mim-reconciliation-historical-review-coverage-and-r-fcf8cee8dc62381f
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: 4-Methyl-2-oxovaleric_Acid'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T06:18:15Z;
    reviewed SHA-256=8de711f4ed9b972971a6ecce2fcb1e7e790b245b92efadbe48dc854a5f601c8b;
    current SHA-256=8de711f4ed9b972971a6ecce2fcb1e7e790b245b92efadbe48dc854a5f601c8b;
    hash_changed=False. Reports=["reports/yaml_record_review/4-Methyl-2-oxovaleric_Acid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The neutral
    CHEBI identity and chemistry pass, but the conjugate-base anion remains an exact
    synonym and publishes through SSSOM.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-fcf8cee8dc62381f
  evidence_ids:
  - ev-994e0b0e6a434543
  - ev-a2fda6e1609f0c69
  - ev-39890bbb472d9ec9
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/4-Methyl-2-oxovaleric_Acid.yaml
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
