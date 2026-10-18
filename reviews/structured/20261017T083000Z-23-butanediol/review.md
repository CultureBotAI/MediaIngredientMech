# Per-record structured review: 23-butanediol (data/ingredients/mapped/23-butanediol.yaml)

- Review: 20261017T083000Z-23-butanediol
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 23-butanediol (data/ingredients/mapped/23-butanediol.yaml, record-47db0822025e761e, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/23-butanediol.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/23-butanediol.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-47db0822025e761e | data/ingredients/mapped/23-butanediol.yaml | maintained | 23-butanediol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-47db0822025e761e | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-47db0822025e761e | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-47db0822025e761e | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-47db0822025e761e.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-47db0822025e761e.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T05:50:44Z; reviewed SHA-256=476b395efe0252e40793bfb62b9ac213f6892b7fe7957b2dbba6359cccd88b08; current SHA-256=476b395efe0252e40793bfb62b9ac213f6892b7fe7957b2dbba6359cccd88b08; hash_changed=False. Reports=["reports/yaml_record_review/23-butanediol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Active CHEBI identity, chemistry, occurrence count, SSSOM, aggregate, and CultureMech-backed CARBON_SOURCE pass, but non-label role/property text remains in synonyms.

## Findings

### rec-f-ff4078d4b669aeff: Historical review coverage and residual narrative: 23-butanediol

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-47db0822025e761e.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T05:50:44Z; reviewed SHA-256=476b395efe0252e40793bfb62b9ac213f6892b7fe7957b2dbba6359cccd88b08; current SHA-256=476b395efe0252e40793bfb62b9ac213f6892b7fe7957b2dbba6359cccd88b08; hash_changed=False. Reports=["reports/yaml_record_review/23-butanediol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Active CHEBI identity, chemistry, occurrence count, SSSOM, aggregate, and CultureMech-backed CARBON_SOURCE pass, but non-label role/property text remains in synonyms.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-0a1be1bffa028351 | data/ingredients/mapped/23-butanediol.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[338],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:62064","line":340,"mapping_status":"MAPPED","ontology_id":"CHEBI:62064","preferred_term":"2,3-butanediol"}],"identifier":"CHEBI:62064","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7,"edge_count":7,"occurrences":7},"occurrence_statistics":{"media_count":7,"total_occurrences":7},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:62064","ontology_label":"butane-2,3-diol","ontology_source":"CHEBI"},"preferred_term":"2,3-butanediol","sssom_rows":[{"data_row":107,"object_id":"CHEBI:62064","object_label":"butane-2,3-diol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:23-butanediol","synonym_count":9} |
| ev-43b84eb8fcb58842 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [338] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-6f1673d6a397832b | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:23-butanediol; data-row positions=[107] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":107,"object_id":"CHEBI:62064","object_label":"butane-2,3-diol","other":"2,3-Butylene glycol&#124;2,3-Dihydroxybutane&#124;Dimethylene glycol&#124;Dimethylethylene glycol&#124;Pseudobutylene glycol&#124;Sym-dimethylethylene glycol&#124;3-butanediol&#124;CAS:513-85-9","predicate_id":"skos:exactMatch","subject_id":"MIM:23-butanediol","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-8f7fc86577547828 | docs/data/mapped_ingredients.csv; CSV lines=[340] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:62064","line":340,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"7","ontology_id":"CHEBI:62064","preferred_term":"2,3-butanediol","total_occurrences":"7"}] |
| ev-a2e5daea9faf2739 | reports/yaml_record_review/23-butanediol.md; &#96;data/ingredients/mapped/23-butanediol.yaml&#96;:2; Verdict:4; Identity:11; Validation:27; Evidence:41; Completeness:61; Recommended Edits:69 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-afc9048033475f14 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[88] | context_only | [{"current_record_sha256":"476b395efe0252e40793bfb62b9ac213f6892b7fe7957b2dbba6359cccd88b08","finding_id":"SEM:201fd3622c95d3f079ca","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-23-butanediol
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 23-butanediol (data/ingredients/mapped/23-butanediol.yaml)'
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
summary: Per-record structured review for 23-butanediol (data/ingredients/mapped/23-butanediol.yaml,
  record-47db0822025e761e, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/23-butanediol.yaml
    sha256: 476b395efe0252e40793bfb62b9ac213f6892b7fe7957b2dbba6359cccd88b08
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
  - path: reports/yaml_record_review/23-butanediol.md
    sha256: 0f43f584a45e3b49ea9553dcd3df49adcae24a77eca91fa796e185012b21d4e3
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-47db0822025e761e
  path: data/ingredients/mapped/23-butanediol.yaml
  label: 23-butanediol
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/23-butanediol.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/23-butanediol.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/23-butanediol.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-47db0822025e761e
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-47db0822025e761e
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-47db0822025e761e
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-47db0822025e761e
evidence:
- evidence_id: ev-0a1be1bffa028351
  kind: record_content
  reference: data/ingredients/mapped/23-butanediol.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[338],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:62064","line":340,"mapping_status":"MAPPED","ontology_id":"CHEBI:62064","preferred_term":"2,3-butanediol"}],"identifier":"CHEBI:62064","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7,"edge_count":7,"occurrences":7},"occurrence_statistics":{"media_count":7,"total_occurrences":7},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:62064","ontology_label":"butane-2,3-diol","ontology_source":"CHEBI"},"preferred_term":"2,3-butanediol","sssom_rows":[{"data_row":107,"object_id":"CHEBI:62064","object_label":"butane-2,3-diol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:23-butanediol","synonym_count":9}'
  snapshot_sha256: 476b395efe0252e40793bfb62b9ac213f6892b7fe7957b2dbba6359cccd88b08
- evidence_id: ev-43b84eb8fcb58842
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [338]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-6f1673d6a397832b
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:23-butanediol; data-row positions=[107]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":107,"object_id":"CHEBI:62064","object_label":"butane-2,3-diol","other":"2,3-Butylene
    glycol|2,3-Dihydroxybutane|Dimethylene glycol|Dimethylethylene glycol|Pseudobutylene
    glycol|Sym-dimethylethylene glycol|3-butanediol|CAS:513-85-9","predicate_id":"skos:exactMatch","subject_id":"MIM:23-butanediol","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-8f7fc86577547828
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[340]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:62064","line":340,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"7","ontology_id":"CHEBI:62064","preferred_term":"2,3-butanediol","total_occurrences":"7"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-a2e5daea9faf2739
  kind: prior_review
  reference: reports/yaml_record_review/23-butanediol.md
  locator: '`data/ingredients/mapped/23-butanediol.yaml`:2; Verdict:4; Identity:11;
    Validation:27; Evidence:41; Completeness:61; Recommended Edits:69'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 0f43f584a45e3b49ea9553dcd3df49adcae24a77eca91fa796e185012b21d4e3
  quote: "Recommended Edits:\n1. Remove `Role: Carbon source; Properties: Organic\
    \ compound, Defined component,\n   Simple component` from `data/ingredients/mapped/23-butanediol.yaml`\n\
    \   `synonyms`.\n2. Regenerate `data/curated/mapped_ingredients.yaml`,\n   `mappings/ingredient_mappings.sssom.tsv`,\
    \ and docs from the maintained YAML.\n3. Re-run the focused strict/LinkML validators,\
    \ synonym review,\n   `just qc-sssom`, and `just qc-flat-coverage` after those\
    \ edits."
- evidence_id: ev-afc9048033475f14
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[88]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"476b395efe0252e40793bfb62b9ac213f6892b7fe7957b2dbba6359cccd88b08","finding_id":"SEM:201fd3622c95d3f079ca","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-253f0174037a37f8
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-47db0822025e761e
  evidence_ids:
  - ev-0a1be1bffa028351
  - ev-43b84eb8fcb58842
  - ev-6f1673d6a397832b
  - ev-8f7fc86577547828
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-456c5b43577340dc
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-47db0822025e761e
  evidence_ids:
  - ev-a2e5daea9faf2739
  - ev-0a1be1bffa028351
  - ev-afc9048033475f14
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T05:50:44Z;
    reviewed SHA-256=476b395efe0252e40793bfb62b9ac213f6892b7fe7957b2dbba6359cccd88b08;
    current SHA-256=476b395efe0252e40793bfb62b9ac213f6892b7fe7957b2dbba6359cccd88b08;
    hash_changed=False. Reports=["reports/yaml_record_review/23-butanediol.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: Active CHEBI identity,
    chemistry, occurrence count, SSSOM, aggregate, and CultureMech-backed CARBON_SOURCE
    pass, but non-label role/property text remains in synonyms.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-a2e5daea9faf2739
    - ev-0a1be1bffa028351
  - name: legacy-native-ids
    value: '["SEM:201fd3622c95d3f079ca"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-0a1be1bffa028351
    - ev-a2e5daea9faf2739
    - ev-afc9048033475f14
findings:
- finding_id: rec-f-ff4078d4b669aeff
  issue_key: mim-reconciliation-historical-review-coverage-and-r-47db0822025e761e
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: 23-butanediol'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T05:50:44Z;
    reviewed SHA-256=476b395efe0252e40793bfb62b9ac213f6892b7fe7957b2dbba6359cccd88b08;
    current SHA-256=476b395efe0252e40793bfb62b9ac213f6892b7fe7957b2dbba6359cccd88b08;
    hash_changed=False. Reports=["reports/yaml_record_review/23-butanediol.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: Active CHEBI identity,
    chemistry, occurrence count, SSSOM, aggregate, and CultureMech-backed CARBON_SOURCE
    pass, but non-label role/property text remains in synonyms.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-47db0822025e761e
  evidence_ids:
  - ev-a2e5daea9faf2739
  - ev-0a1be1bffa028351
  - ev-afc9048033475f14
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/23-butanediol.yaml
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
