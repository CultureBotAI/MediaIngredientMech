# Per-record structured review: Bromophenol_blue (data/ingredients/mapped/Bromophenol_blue.yaml)

- Review: 20261017T083000Z-bromophenol-blue
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Bromophenol_blue (data/ingredients/mapped/Bromophenol_blue.yaml, record-d6158d5742f497b0, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Bromophenol_blue.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Bromophenol_blue.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-d6158d5742f497b0 | data/ingredients/mapped/Bromophenol_blue.yaml | maintained | Bromophenol_blue |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-d6158d5742f497b0 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-d6158d5742f497b0 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-d6158d5742f497b0 | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-d6158d5742f497b0.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-d6158d5742f497b0.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T10:13:50Z; reviewed SHA-256=d5d34a198e984d6df91daf305f57c413c57314469edbb4e600756498cde2047d; current SHA-256=d5d34a198e984d6df91daf305f57c413c57314469edbb4e600756498cde2047d; hash_changed=False. Reports=["reports/yaml_record_review/Bromophenol_blue.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI bromophenol blue identity, restored CultureMech evidence, KOH-solution alias, SSSOM row, and aggregate copy pass, but occurrence statistics look stale.

## Findings

### rec-f-17d40890e4f2dd31: Historical review coverage and residual narrative: Bromophenol_blue

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-d6158d5742f497b0.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T10:13:50Z; reviewed SHA-256=d5d34a198e984d6df91daf305f57c413c57314469edbb4e600756498cde2047d; current SHA-256=d5d34a198e984d6df91daf305f57c413c57314469edbb4e600756498cde2047d; hash_changed=False. Reports=["reports/yaml_record_review/Bromophenol_blue.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI bromophenol blue identity, restored CultureMech evidence, KOH-solution alias, SSSOM row, and aggregate copy pass, but occurrence statistics look stale.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-03ba1d63e157d20a | data/ingredients/mapped/Bromophenol_blue.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2546],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:59424","line":2548,"mapping_status":"MAPPED","ontology_id":"CHEBI:59424","preferred_term":"Bromophenol blue"}],"identifier":"CHEBI:59424","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","match_level":"EXACT","ontology_id":"CHEBI:59424","ontology_label":"bromophenol blue","ontology_source":"CHEBI"},"preferred_term":"Bromophenol blue","sssom_rows":[{"data_row":582,"object_id":"CHEBI:59424","object_label":"bromophenol blue","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Bromophenol_blue","synonym_count":1} |
| ev-c41bc224a8d84d4b | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2546] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-51990733358a985d | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Bromophenol_blue; data-row positions=[582] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":582,"object_id":"CHEBI:59424","object_label":"bromophenol blue","other":"Bromophenol blue (0.5% in 0.2N KOH)","predicate_id":"skos:exactMatch","subject_id":"MIM:Bromophenol_blue","validation_method":"manual:claude_culturemech_residual_grounding&#124;CREATED&#124;2026-08-30"}] |
| ev-5a6aafc4cf2299c3 | docs/data/mapped_ingredients.csv; CSV lines=[2548] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:59424","line":2548,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:59424","preferred_term":"Bromophenol blue","total_occurrences":"1"}] |
| ev-9ccbd61e0edfea18 | reports/yaml_record_review/Bromophenol_blue.md; &#96;data/ingredients/mapped/Bromophenol_blue.yaml&#96;:2; Verdict:4; Identity:11; Validation:24; Evidence:34; Completeness:53; Recommended Edits:61 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-7dfa26f30fbfb82e | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[333] | context_only | [{"current_record_sha256":"d5d34a198e984d6df91daf305f57c413c57314469edbb4e600756498cde2047d","finding_id":"SEM:3ef34e6eb9e1adc7219d","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-bromophenol-blue
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Bromophenol_blue (data/ingredients/mapped/Bromophenol_blue.yaml)'
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
summary: Per-record structured review for Bromophenol_blue (data/ingredients/mapped/Bromophenol_blue.yaml,
  record-d6158d5742f497b0, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Bromophenol_blue.yaml
    sha256: d5d34a198e984d6df91daf305f57c413c57314469edbb4e600756498cde2047d
    role: target
  - path: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
    sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
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
  - path: reports/yaml_record_review/Bromophenol_blue.md
    sha256: 4c6513b51a1f115c64221ea97067e34592a4033f27902cbb5ebfddb765be28a7
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-d6158d5742f497b0
  path: data/ingredients/mapped/Bromophenol_blue.yaml
  label: Bromophenol_blue
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bromophenol_blue.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Bromophenol_blue.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Bromophenol_blue.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-d6158d5742f497b0
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-d6158d5742f497b0
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-d6158d5742f497b0
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-d6158d5742f497b0
evidence:
- evidence_id: ev-03ba1d63e157d20a
  kind: record_content
  reference: data/ingredients/mapped/Bromophenol_blue.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2546],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:59424","line":2548,"mapping_status":"MAPPED","ontology_id":"CHEBI:59424","preferred_term":"Bromophenol
    blue"}],"identifier":"CHEBI:59424","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","match_level":"EXACT","ontology_id":"CHEBI:59424","ontology_label":"bromophenol
    blue","ontology_source":"CHEBI"},"preferred_term":"Bromophenol blue","sssom_rows":[{"data_row":582,"object_id":"CHEBI:59424","object_label":"bromophenol
    blue","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Bromophenol_blue","synonym_count":1}'
  snapshot_sha256: d5d34a198e984d6df91daf305f57c413c57314469edbb4e600756498cde2047d
- evidence_id: ev-c41bc224a8d84d4b
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2546]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-51990733358a985d
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Bromophenol_blue; data-row positions=[582]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":582,"object_id":"CHEBI:59424","object_label":"bromophenol
    blue","other":"Bromophenol blue (0.5% in 0.2N KOH)","predicate_id":"skos:exactMatch","subject_id":"MIM:Bromophenol_blue","validation_method":"manual:claude_culturemech_residual_grounding|CREATED|2026-08-30"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-5a6aafc4cf2299c3
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2548]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:59424","line":2548,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:59424","preferred_term":"Bromophenol
    blue","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-9ccbd61e0edfea18
  kind: prior_review
  reference: reports/yaml_record_review/Bromophenol_blue.md
  locator: '`data/ingredients/mapped/Bromophenol_blue.yaml`:2; Verdict:4; Identity:11;
    Validation:24; Evidence:34; Completeness:53; Recommended Edits:61'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 4c6513b51a1f115c64221ea97067e34592a4033f27902cbb5ebfddb765be28a7
  quote: "Recommended Edits:\n- Minor: refresh `data/ingredients/mapped/Bromophenol_blue.yaml`\
    \ occurrence\n  statistics from the maintained CultureMech occurrence table and\
    \ add a\n  `supplied_form` or note for the 0.5% bromophenol blue in 0.2 N KOH\
    \ source\n  surface if that concentration/solvent should remain attached to the\
    \ compound\n  record; then run `just sync-curated` and focused strict/term validation."
- evidence_id: ev-7dfa26f30fbfb82e
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[333]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"d5d34a198e984d6df91daf305f57c413c57314469edbb4e600756498cde2047d","finding_id":"SEM:3ef34e6eb9e1adc7219d","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-2bdf1b9ceb4e6b3c
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-d6158d5742f497b0
  evidence_ids:
  - ev-03ba1d63e157d20a
  - ev-c41bc224a8d84d4b
  - ev-51990733358a985d
  - ev-5a6aafc4cf2299c3
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-0634f5053b3813f8
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d6158d5742f497b0
  evidence_ids:
  - ev-9ccbd61e0edfea18
  - ev-03ba1d63e157d20a
  - ev-7dfa26f30fbfb82e
  details: 'Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T10:13:50Z;
    reviewed SHA-256=d5d34a198e984d6df91daf305f57c413c57314469edbb4e600756498cde2047d;
    current SHA-256=d5d34a198e984d6df91daf305f57c413c57314469edbb4e600756498cde2047d;
    hash_changed=False. Reports=["reports/yaml_record_review/Bromophenol_blue.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI bromophenol blue identity, restored CultureMech evidence, KOH-solution alias,
    SSSOM row, and aggregate copy pass, but occurrence statistics look stale.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-9ccbd61e0edfea18
    - ev-03ba1d63e157d20a
  - name: legacy-native-ids
    value: '["SEM:3ef34e6eb9e1adc7219d"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-03ba1d63e157d20a
    - ev-9ccbd61e0edfea18
    - ev-7dfa26f30fbfb82e
findings:
- finding_id: rec-f-17d40890e4f2dd31
  issue_key: mim-reconciliation-historical-review-coverage-and-r-d6158d5742f497b0
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Bromophenol_blue'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T10:13:50Z;
    reviewed SHA-256=d5d34a198e984d6df91daf305f57c413c57314469edbb4e600756498cde2047d;
    current SHA-256=d5d34a198e984d6df91daf305f57c413c57314469edbb4e600756498cde2047d;
    hash_changed=False. Reports=["reports/yaml_record_review/Bromophenol_blue.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI bromophenol blue identity, restored CultureMech evidence, KOH-solution alias,
    SSSOM row, and aggregate copy pass, but occurrence statistics look stale.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d6158d5742f497b0
  evidence_ids:
  - ev-9ccbd61e0edfea18
  - ev-03ba1d63e157d20a
  - ev-7dfa26f30fbfb82e
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bromophenol_blue.yaml
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
  with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.
```
