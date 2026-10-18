# Per-record structured review: Avocatin_B (data/ingredients/mapped/Avocatin_B.yaml)

- Review: 20261017T083000Z-avocatin-b
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Avocatin_B (data/ingredients/mapped/Avocatin_B.yaml, record-914fe71e4fae200a, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Avocatin_B.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Avocatin_B.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-914fe71e4fae200a | data/ingredients/mapped/Avocatin_B.yaml | maintained | Avocatin_B |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-914fe71e4fae200a | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-914fe71e4fae200a | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-914fe71e4fae200a | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-914fe71e4fae200a.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-914fe71e4fae200a.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T09:01:51Z; reviewed SHA-256=74b94f83e54dbb8d62a8b1df69917ebdc2bb4de8dea53a8f913a67f61949ae48; current SHA-256=74b94f83e54dbb8d62a8b1df69917ebdc2bb4de8dea53a8f913a67f61949ae48; hash_changed=False. Reports=["reports/yaml_record_review/Avocatin_B.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact MeSH Avocatin B identity passes, but its 1:1 Avocadene/Avocadyne composition is not modeled.

## Findings

### rec-f-d69d8d768a62cdbb: Historical review coverage and residual narrative: Avocatin_B

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-914fe71e4fae200a.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T09:01:51Z; reviewed SHA-256=74b94f83e54dbb8d62a8b1df69917ebdc2bb4de8dea53a8f913a67f61949ae48; current SHA-256=74b94f83e54dbb8d62a8b1df69917ebdc2bb4de8dea53a8f913a67f61949ae48; hash_changed=False. Reports=["reports/yaml_record_review/Avocatin_B.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact MeSH Avocatin B identity passes, but its 1:1 Avocadene/Avocadyne composition is not modeled.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-34b9d1b1764c66f9 | data/ingredients/mapped/Avocatin_B.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[532],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C000709627","line":534,"mapping_status":"MAPPED","ontology_id":"mesh:C000709627","preferred_term":"Avocatin B"}],"identifier":"mesh:C000709627","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C000709627","ontology_label":"avocatin B","ontology_source":"MESH"},"preferred_term":"Avocatin B","sssom_rows":[{"data_row":456,"object_id":"mesh:C000709627","object_label":"avocatin B","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Avocatin_B","synonym_count":1} |
| ev-650c161d6a4174c0 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [532] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-ffd1df130816e61e | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Avocatin_B; data-row positions=[456] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":456,"object_id":"mesh:C000709627","object_label":"avocatin B","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Avocatin_B","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-3b54c6ada4637dba | docs/data/mapped_ingredients.csv; CSV lines=[534] | supports | Published identity and count rows inspected: [{"identifier":"mesh:C000709627","line":534,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C000709627","preferred_term":"Avocatin B","total_occurrences":"0"}] |
| ev-99a06ffad1654652 | reports/yaml_record_review/Avocatin_B.md; &#96;data/ingredients/mapped/Avocatin_B.yaml&#96;:2; Verdict:4; Identity:10; Validation:23; Evidence:38; Completeness:56; Recommended Edits:66 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-e81fa17d76e63e29 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[284] | context_only | [{"current_record_sha256":"74b94f83e54dbb8d62a8b1df69917ebdc2bb4de8dea53a8f913a67f61949ae48","finding_id":"SEM:26567b75d4c91ad33437","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-avocatin-b
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Avocatin_B (data/ingredients/mapped/Avocatin_B.yaml)'
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
summary: Per-record structured review for Avocatin_B (data/ingredients/mapped/Avocatin_B.yaml,
  record-914fe71e4fae200a, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Avocatin_B.yaml
    sha256: 74b94f83e54dbb8d62a8b1df69917ebdc2bb4de8dea53a8f913a67f61949ae48
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
  - path: reports/yaml_record_review/Avocatin_B.md
    sha256: d4eeeaacab891bc01e10c44068806aab3526c9bd0951fb3ac58e0e19b088ce6a
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-914fe71e4fae200a
  path: data/ingredients/mapped/Avocatin_B.yaml
  label: Avocatin_B
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Avocatin_B.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Avocatin_B.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Avocatin_B.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-914fe71e4fae200a
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-914fe71e4fae200a
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-914fe71e4fae200a
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-914fe71e4fae200a
evidence:
- evidence_id: ev-34b9d1b1764c66f9
  kind: record_content
  reference: data/ingredients/mapped/Avocatin_B.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[532],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C000709627","line":534,"mapping_status":"MAPPED","ontology_id":"mesh:C000709627","preferred_term":"Avocatin
    B"}],"identifier":"mesh:C000709627","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C000709627","ontology_label":"avocatin
    B","ontology_source":"MESH"},"preferred_term":"Avocatin B","sssom_rows":[{"data_row":456,"object_id":"mesh:C000709627","object_label":"avocatin
    B","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Avocatin_B","synonym_count":1}'
  snapshot_sha256: 74b94f83e54dbb8d62a8b1df69917ebdc2bb4de8dea53a8f913a67f61949ae48
- evidence_id: ev-650c161d6a4174c0
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [532]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-ffd1df130816e61e
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Avocatin_B; data-row positions=[456]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":456,"object_id":"mesh:C000709627","object_label":"avocatin
    B","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Avocatin_B","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-3b54c6ada4637dba
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[534]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"mesh:C000709627","line":534,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C000709627","preferred_term":"Avocatin
    B","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-99a06ffad1654652
  kind: prior_review
  reference: reports/yaml_record_review/Avocatin_B.md
  locator: '`data/ingredients/mapped/Avocatin_B.yaml`:2; Verdict:4; Identity:10; Validation:23;
    Evidence:38; Completeness:56; Recommended Edits:66'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: d4eeeaacab891bc01e10c44068806aab3526c9bd0951fb3ac58e0e19b088ce6a
  quote: "Recommended Edits:\n- Set `ingredient_type` to the repository's mixture/decomposition\
    \ value for a\n  two-component compound and add 1:1 components for\n  `data/ingredients/mapped/Avocadene.yaml`\
    \ and\n  `data/ingredients/mapped/Avocadyne.yaml`.\n- Remove or retype the redundant\
    \ `Avocatin B` raw synonym if local synonym\n  policy treats a preferred-term\
    \ echo as noise.\n- Synchronize the aggregate, regenerate affected flat outputs,\
    \ and rerun focused\n  strict validation, component partonomy, SSSOM invariants,\
    \ and flat-export\n  coverage."
- evidence_id: ev-e81fa17d76e63e29
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[284]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"74b94f83e54dbb8d62a8b1df69917ebdc2bb4de8dea53a8f913a67f61949ae48","finding_id":"SEM:26567b75d4c91ad33437","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-f4cd3a7ab367df6a
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-914fe71e4fae200a
  evidence_ids:
  - ev-34b9d1b1764c66f9
  - ev-650c161d6a4174c0
  - ev-ffd1df130816e61e
  - ev-3b54c6ada4637dba
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-4513f1e85386f9f3
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-914fe71e4fae200a
  evidence_ids:
  - ev-99a06ffad1654652
  - ev-34b9d1b1764c66f9
  - ev-e81fa17d76e63e29
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T09:01:51Z;
    reviewed SHA-256=74b94f83e54dbb8d62a8b1df69917ebdc2bb4de8dea53a8f913a67f61949ae48;
    current SHA-256=74b94f83e54dbb8d62a8b1df69917ebdc2bb4de8dea53a8f913a67f61949ae48;
    hash_changed=False. Reports=["reports/yaml_record_review/Avocatin_B.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact MeSH
    Avocatin B identity passes, but its 1:1 Avocadene/Avocadyne composition is not
    modeled.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-99a06ffad1654652
    - ev-34b9d1b1764c66f9
  - name: legacy-native-ids
    value: '["SEM:26567b75d4c91ad33437"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-34b9d1b1764c66f9
    - ev-99a06ffad1654652
    - ev-e81fa17d76e63e29
findings:
- finding_id: rec-f-d69d8d768a62cdbb
  issue_key: mim-reconciliation-historical-review-coverage-and-r-914fe71e4fae200a
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Avocatin_B'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T09:01:51Z;
    reviewed SHA-256=74b94f83e54dbb8d62a8b1df69917ebdc2bb4de8dea53a8f913a67f61949ae48;
    current SHA-256=74b94f83e54dbb8d62a8b1df69917ebdc2bb4de8dea53a8f913a67f61949ae48;
    hash_changed=False. Reports=["reports/yaml_record_review/Avocatin_B.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact MeSH
    Avocatin B identity passes, but its 1:1 Avocadene/Avocadyne composition is not
    modeled.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-914fe71e4fae200a
  evidence_ids:
  - ev-99a06ffad1654652
  - ev-34b9d1b1764c66f9
  - ev-e81fa17d76e63e29
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Avocatin_B.yaml
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
