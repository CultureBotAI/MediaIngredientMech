# Per-record structured review: Tryptophan (data/ingredients/mapped/Tryptophan.yaml)

- Review: 20261017T083000Z-tryptophan
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Tryptophan (data/ingredients/mapped/Tryptophan.yaml, record-4f6cd5e91cddf516, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Tryptophan.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Tryptophan.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-4f6cd5e91cddf516 | data/ingredients/mapped/Tryptophan.yaml | maintained | Tryptophan |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-4f6cd5e91cddf516 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-4f6cd5e91cddf516 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-4f6cd5e91cddf516 | Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-4f6cd5e91cddf516.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-4f6cd5e91cddf516.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T20:07:35Z; reviewed SHA-256=33eb945268c2de48a4141c357266d845d83c9d2eb82c121584bb1e65f5b8c543; current SHA-256=33eb945268c2de48a4141c357266d845d83c9d2eb82c121584bb1e65f5b8c543; hash_changed=False. Reports=["reports/yaml_record_review/Tryptophan.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The generic CHEBI identity passes, but the record carries and exports the L-tryptophan CAS RN already owned by the local L-tryptophan sibling.

## Findings

### rec-f-8c1f2be93f57350d: Historical review coverage and residual narrative: Tryptophan

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-4f6cd5e91cddf516.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T20:07:35Z; reviewed SHA-256=33eb945268c2de48a4141c357266d845d83c9d2eb82c121584bb1e65f5b8c543; current SHA-256=33eb945268c2de48a4141c357266d845d83c9d2eb82c121584bb1e65f5b8c543; hash_changed=False. Reports=["reports/yaml_record_review/Tryptophan.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The generic CHEBI identity passes, but the record carries and exports the L-tryptophan CAS RN already owned by the local L-tryptophan sibling.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-c4613d3c51badd70 | data/ingredients/mapped/Tryptophan.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2009],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:27897","line":2011,"mapping_status":"MAPPED","ontology_id":"CHEBI:27897","preferred_term":"Tryptophan"}],"identifier":"CHEBI:27897","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":38,"edge_count":38,"occurrences":38},"occurrence_statistics":{"media_count":38,"total_occurrences":38},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:27897","ontology_label":"tryptophan","ontology_source":"CHEBI"},"preferred_term":"Tryptophan","sssom_rows":[{"data_row":2847,"object_id":"CHEBI:27897","object_label":"tryptophan","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Tryptophan","synonym_count":9} |
| ev-7daa2057d2d0cb7f | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2009] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-8599e00715741ea4 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Tryptophan; data-row positions=[2847] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2847,"object_id":"CHEBI:27897","object_label":"tryptophan","other":"2-amino-3-(1H-indol-3-yl)propanoic acid&#124;Htrp&#124;alpha-Amino-beta-(3-indolyl)-propionic acid&#124;alpha-amino-beta-3-indolepropionic acid&#124;beta-3-indolylalanine&#124;triptofano&#124;tryptophane&#124;CAS:73-22-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Tryptophan","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-03a7d7c72f3af147 | docs/data/mapped_ingredients.csv; CSV lines=[2011] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:27897","line":2011,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"38","ontology_id":"CHEBI:27897","preferred_term":"Tryptophan","total_occurrences":"38"}] |
| ev-3a12a53150c92fa4 | reports/yaml_record_review/Tryptophan.md; &#96;data/ingredients/mapped/Tryptophan.yaml&#96;:2; Verdict:4; Identity:11; Validation:24; Evidence:34; Issues:46; Major: &#96;CAS:73-22-3&#96; belongs to the L-tryptophan sibling:48; Completeness:60; Recommended Edits:70 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-8506c764ce75166a | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1322] | context_only | [{"current_record_sha256":"33eb945268c2de48a4141c357266d845d83c9d2eb82c121584bb1e65f5b8c543","finding_id":"SEM:2a2ccc101f20598d4ae9","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-tryptophan
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Tryptophan (data/ingredients/mapped/Tryptophan.yaml)'
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
summary: Per-record structured review for Tryptophan (data/ingredients/mapped/Tryptophan.yaml,
  record-4f6cd5e91cddf516, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Tryptophan.yaml
    sha256: 33eb945268c2de48a4141c357266d845d83c9d2eb82c121584bb1e65f5b8c543
    role: target
  - path: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
    sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
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
  - path: reports/yaml_record_review/Tryptophan.md
    sha256: 04fb4a7132f9e220ec1439dca0e9f07dcb7cda17a53ee769dcc5cf9624425165
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-4f6cd5e91cddf516
  path: data/ingredients/mapped/Tryptophan.yaml
  label: Tryptophan
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Tryptophan.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Tryptophan.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Tryptophan.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-4f6cd5e91cddf516
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-4f6cd5e91cddf516
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-4f6cd5e91cddf516
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12
    and semantic review dispositions on HEAD.
  target_ids:
  - record-4f6cd5e91cddf516
evidence:
- evidence_id: ev-c4613d3c51badd70
  kind: record_content
  reference: data/ingredients/mapped/Tryptophan.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2009],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:27897","line":2011,"mapping_status":"MAPPED","ontology_id":"CHEBI:27897","preferred_term":"Tryptophan"}],"identifier":"CHEBI:27897","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":38,"edge_count":38,"occurrences":38},"occurrence_statistics":{"media_count":38,"total_occurrences":38},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:27897","ontology_label":"tryptophan","ontology_source":"CHEBI"},"preferred_term":"Tryptophan","sssom_rows":[{"data_row":2847,"object_id":"CHEBI:27897","object_label":"tryptophan","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Tryptophan","synonym_count":9}'
  snapshot_sha256: 33eb945268c2de48a4141c357266d845d83c9d2eb82c121584bb1e65f5b8c543
- evidence_id: ev-7daa2057d2d0cb7f
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2009]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-8599e00715741ea4
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Tryptophan; data-row positions=[2847]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2847,"object_id":"CHEBI:27897","object_label":"tryptophan","other":"2-amino-3-(1H-indol-3-yl)propanoic
    acid|Htrp|alpha-Amino-beta-(3-indolyl)-propionic acid|alpha-amino-beta-3-indolepropionic
    acid|beta-3-indolylalanine|triptofano|tryptophane|CAS:73-22-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Tryptophan","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-03a7d7c72f3af147
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2011]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:27897","line":2011,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"38","ontology_id":"CHEBI:27897","preferred_term":"Tryptophan","total_occurrences":"38"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-3a12a53150c92fa4
  kind: prior_review
  reference: reports/yaml_record_review/Tryptophan.md
  locator: '`data/ingredients/mapped/Tryptophan.yaml`:2; Verdict:4; Identity:11; Validation:24;
    Evidence:34; Issues:46; Major: `CAS:73-22-3` belongs to the L-tryptophan sibling:48;
    Completeness:60; Recommended Edits:70'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 04fb4a7132f9e220ec1439dca0e9f07dcb7cda17a53ee769dcc5cf9624425165
  quote: "Issues:\n\n\nMajor: `CAS:73-22-3` belongs to the L-tryptophan sibling:\n\
    `chemical_properties.cas_rn` currently contains `73-22-3`, so the final SSSOM\n\
    `other` surface publishes `CAS:73-22-3` for the generic `CHEBI:27897`\nTryptophan\
    \ record. OLS cross-references `cas:73-22-3` on the form-specific\n`CHEBI:16828`\
    \ L-tryptophan term instead; the active generic `CHEBI:27897`\nobject cross-references\
    \ a different CAS, `54-12-6`.\n\nThis leaks stereospecific registry metadata from\
    \ L-tryptophan onto the generic\ntryptophan record and duplicates the same CAS\
    \ token from the local\n`L-Tryptophan` record.\n\nRecommended Edits:\n- Re-audit\
    \ the source labels behind the generic `Tryptophan` import. If those\n  labels\
    \ should denote L-tryptophan, merge this record into the existing\n  `data/ingredients/mapped/L-tryptophan.yaml`\
    \ sibling.\n- If the record stays generic, remove `73-22-3` from\n  `chemical_properties.cas_rn`\
    \ and regenerate final SSSOM so\n  `MIM:Tryptophan` stops exporting `CAS:73-22-3`."
- evidence_id: ev-8506c764ce75166a
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1322]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"33eb945268c2de48a4141c357266d845d83c9d2eb82c121584bb1e65f5b8c543","finding_id":"SEM:2a2ccc101f20598d4ae9","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-4fe815a0365dc3ad
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-4f6cd5e91cddf516
  evidence_ids:
  - ev-c4613d3c51badd70
  - ev-7daa2057d2d0cb7f
  - ev-8599e00715741ea4
  - ev-03a7d7c72f3af147
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-b1ff3b4e438dd4f4
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-4f6cd5e91cddf516
  evidence_ids:
  - ev-3a12a53150c92fa4
  - ev-c4613d3c51badd70
  - ev-8506c764ce75166a
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T20:07:35Z;
    reviewed SHA-256=33eb945268c2de48a4141c357266d845d83c9d2eb82c121584bb1e65f5b8c543;
    current SHA-256=33eb945268c2de48a4141c357266d845d83c9d2eb82c121584bb1e65f5b8c543;
    hash_changed=False. Reports=["reports/yaml_record_review/Tryptophan.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The generic CHEBI
    identity passes, but the record carries and exports the L-tryptophan CAS RN already
    owned by the local L-tryptophan sibling.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-3a12a53150c92fa4
    - ev-c4613d3c51badd70
  - name: legacy-native-ids
    value: '["SEM:2a2ccc101f20598d4ae9"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-c4613d3c51badd70
    - ev-3a12a53150c92fa4
    - ev-8506c764ce75166a
findings:
- finding_id: rec-f-8c1f2be93f57350d
  issue_key: mim-reconciliation-historical-review-coverage-and-r-4f6cd5e91cddf516
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Tryptophan'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T20:07:35Z;
    reviewed SHA-256=33eb945268c2de48a4141c357266d845d83c9d2eb82c121584bb1e65f5b8c543;
    current SHA-256=33eb945268c2de48a4141c357266d845d83c9d2eb82c121584bb1e65f5b8c543;
    hash_changed=False. Reports=["reports/yaml_record_review/Tryptophan.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The generic CHEBI
    identity passes, but the record carries and exports the L-tryptophan CAS RN already
    owned by the local L-tryptophan sibling.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-4f6cd5e91cddf516
  evidence_ids:
  - ev-3a12a53150c92fa4
  - ev-c4613d3c51badd70
  - ev-8506c764ce75166a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Tryptophan.yaml
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
  with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.
```
