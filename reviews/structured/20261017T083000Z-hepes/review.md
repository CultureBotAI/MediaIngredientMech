# Per-record structured review: Hepes (data/ingredients/mapped/Hepes.yaml)

- Review: 20261017T083000Z-hepes
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Hepes (data/ingredients/mapped/Hepes.yaml, record-6c405ebbdd8b687a, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Hepes.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Hepes.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-6c405ebbdd8b687a | data/ingredients/mapped/Hepes.yaml | maintained | Hepes |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-6c405ebbdd8b687a | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-6c405ebbdd8b687a | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-6c405ebbdd8b687a | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-6c405ebbdd8b687a.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-6c405ebbdd8b687a.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T19:19:37Z; reviewed SHA-256=7d92365f64808ffb589155a60d8ba407ca6025c3dfda5aea396ac0c724ad4320; current SHA-256=7d92365f64808ffb589155a60d8ba407ca6025c3dfda5aea396ac0c724ad4320; hash_changed=False. Reports=["reports/yaml_record_review/Hepes.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact HEPES identity and buffer role pass, but final SSSOM exports concentration, CAS-decorated, and catalog-decorated aliases as exact synonyms.

## Findings

### rec-f-dfb21ba65d48248c: Historical review coverage and residual narrative: Hepes

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-6c405ebbdd8b687a.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T19:19:37Z; reviewed SHA-256=7d92365f64808ffb589155a60d8ba407ca6025c3dfda5aea396ac0c724ad4320; current SHA-256=7d92365f64808ffb589155a60d8ba407ca6025c3dfda5aea396ac0c724ad4320; hash_changed=False. Reports=["reports/yaml_record_review/Hepes.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact HEPES identity and buffer role pass, but final SSSOM exports concentration, CAS-decorated, and catalog-decorated aliases as exact synonyms.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-8a5cdd7f8db46abf | data/ingredients/mapped/Hepes.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1119],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:42334","line":1121,"mapping_status":"MAPPED","ontology_id":"CHEBI:42334","preferred_term":"HEPES"}],"identifier":"CHEBI:42334","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":251,"edge_count":251,"occurrences":251},"occurrence_statistics":{"media_count":251,"total_occurrences":251},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:42334","ontology_label":"2-[4-(2-hydroxyethyl)piperazin-1-yl]ethanesulfonic acid","ontology_source":"CHEBI"},"preferred_term":"HEPES","sssom_rows":[{"data_row":1419,"object_id":"CHEBI:42334","object_label":"2-[4-(2-hydroxyethyl)piperazin-1-yl]ethanesulfonic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Hepes","synonym_count":13} |
| ev-cd871703e2872b0d | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1119] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-493da9faff83e603 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Hepes; data-row positions=[1419] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1419,"object_id":"CHEBI:42334","object_label":"2-[4-(2-hydroxyethyl)piperazin-1-yl]ethanesulfonic acid","other":"HEPES buffer&#124;HEPES buffer(CAS: 7365-45-9)&#124;HEPES buffer(Sigma H-3375)&#124;4-2-hydroxyethyl-1-piperazineethanesulfonic acid&#124;4-(2-Hydroxyethyl)-1-piperazineethane sulfonic acid&#124;4-(2-hydroxyethyl)-1-piperazineethanesulfonic acid&#124;HEPES (10mM)&#124;CAS:7365-45-9","predicate_id":"skos:exactMatch","subject_id":"MIM:Hepes","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-f8213409babd7bc0 | docs/data/mapped_ingredients.csv; CSV lines=[1121] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:42334","line":1121,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"251","ontology_id":"CHEBI:42334","preferred_term":"HEPES","total_occurrences":"251"}] |
| ev-b640fcf3cbac80f2 | reports/yaml_record_review/Hepes.md; &#96;data/ingredients/mapped/Hepes.yaml&#96;:2; Verdict:4; Identity:10; Validation:23; Evidence:34; Completeness:53; Recommended Edits:61 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-8707e0128be66011 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[728] | context_only | [{"current_record_sha256":"7d92365f64808ffb589155a60d8ba407ca6025c3dfda5aea396ac0c724ad4320","finding_id":"SEM:8d80d3757bf93c16b9a2","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-hepes
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Hepes (data/ingredients/mapped/Hepes.yaml)'
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
summary: Per-record structured review for Hepes (data/ingredients/mapped/Hepes.yaml,
  record-6c405ebbdd8b687a, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Hepes.yaml
    sha256: 7d92365f64808ffb589155a60d8ba407ca6025c3dfda5aea396ac0c724ad4320
    role: target
  - path: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
    sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
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
  - path: reports/yaml_record_review/Hepes.md
    sha256: e598c1bb7b5b956379de57410a72852737812c696d764804c1435a52274b3817
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-6c405ebbdd8b687a
  path: data/ingredients/mapped/Hepes.yaml
  label: Hepes
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Hepes.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Hepes.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Hepes.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-6c405ebbdd8b687a
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-6c405ebbdd8b687a
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-6c405ebbdd8b687a
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-6c405ebbdd8b687a
evidence:
- evidence_id: ev-8a5cdd7f8db46abf
  kind: record_content
  reference: data/ingredients/mapped/Hepes.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1119],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:42334","line":1121,"mapping_status":"MAPPED","ontology_id":"CHEBI:42334","preferred_term":"HEPES"}],"identifier":"CHEBI:42334","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":251,"edge_count":251,"occurrences":251},"occurrence_statistics":{"media_count":251,"total_occurrences":251},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:42334","ontology_label":"2-[4-(2-hydroxyethyl)piperazin-1-yl]ethanesulfonic
    acid","ontology_source":"CHEBI"},"preferred_term":"HEPES","sssom_rows":[{"data_row":1419,"object_id":"CHEBI:42334","object_label":"2-[4-(2-hydroxyethyl)piperazin-1-yl]ethanesulfonic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Hepes","synonym_count":13}'
  snapshot_sha256: 7d92365f64808ffb589155a60d8ba407ca6025c3dfda5aea396ac0c724ad4320
- evidence_id: ev-cd871703e2872b0d
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1119]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-493da9faff83e603
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Hepes; data-row positions=[1419]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1419,"object_id":"CHEBI:42334","object_label":"2-[4-(2-hydroxyethyl)piperazin-1-yl]ethanesulfonic
    acid","other":"HEPES buffer|HEPES buffer(CAS: 7365-45-9)|HEPES buffer(Sigma H-3375)|4-2-hydroxyethyl-1-piperazineethanesulfonic
    acid|4-(2-Hydroxyethyl)-1-piperazineethane sulfonic acid|4-(2-hydroxyethyl)-1-piperazineethanesulfonic
    acid|HEPES (10mM)|CAS:7365-45-9","predicate_id":"skos:exactMatch","subject_id":"MIM:Hepes","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-f8213409babd7bc0
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1121]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:42334","line":1121,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"251","ontology_id":"CHEBI:42334","preferred_term":"HEPES","total_occurrences":"251"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-b640fcf3cbac80f2
  kind: prior_review
  reference: reports/yaml_record_review/Hepes.md
  locator: '`data/ingredients/mapped/Hepes.yaml`:2; Verdict:4; Identity:10; Validation:23;
    Evidence:34; Completeness:53; Recommended Edits:61'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: e598c1bb7b5b956379de57410a72852737812c696d764804c1435a52274b3817
  quote: "Recommended Edits:\n- Major: suppress or retype `HEPES (10mM)`,\n  `HEPES\
    \ buffer(CAS: 7365-45-9)`, and `HEPES buffer(Sigma H-3375)` so they are\n  retained\
    \ only as provenance and no longer exported as final exact synonyms."
- evidence_id: ev-8707e0128be66011
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[728]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"7d92365f64808ffb589155a60d8ba407ca6025c3dfda5aea396ac0c724ad4320","finding_id":"SEM:8d80d3757bf93c16b9a2","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-89a0de7814ba18db
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-6c405ebbdd8b687a
  evidence_ids:
  - ev-8a5cdd7f8db46abf
  - ev-cd871703e2872b0d
  - ev-493da9faff83e603
  - ev-f8213409babd7bc0
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-2aafb14882817540
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-6c405ebbdd8b687a
  evidence_ids:
  - ev-b640fcf3cbac80f2
  - ev-8a5cdd7f8db46abf
  - ev-8707e0128be66011
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T19:19:37Z;
    reviewed SHA-256=7d92365f64808ffb589155a60d8ba407ca6025c3dfda5aea396ac0c724ad4320;
    current SHA-256=7d92365f64808ffb589155a60d8ba407ca6025c3dfda5aea396ac0c724ad4320;
    hash_changed=False. Reports=["reports/yaml_record_review/Hepes.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact HEPES identity
    and buffer role pass, but final SSSOM exports concentration, CAS-decorated, and
    catalog-decorated aliases as exact synonyms.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b640fcf3cbac80f2
    - ev-8a5cdd7f8db46abf
  - name: legacy-native-ids
    value: '["SEM:8d80d3757bf93c16b9a2"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-8a5cdd7f8db46abf
    - ev-b640fcf3cbac80f2
    - ev-8707e0128be66011
findings:
- finding_id: rec-f-dfb21ba65d48248c
  issue_key: mim-reconciliation-historical-review-coverage-and-r-6c405ebbdd8b687a
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Hepes'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T19:19:37Z;
    reviewed SHA-256=7d92365f64808ffb589155a60d8ba407ca6025c3dfda5aea396ac0c724ad4320;
    current SHA-256=7d92365f64808ffb589155a60d8ba407ca6025c3dfda5aea396ac0c724ad4320;
    hash_changed=False. Reports=["reports/yaml_record_review/Hepes.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact HEPES identity
    and buffer role pass, but final SSSOM exports concentration, CAS-decorated, and
    catalog-decorated aliases as exact synonyms.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-6c405ebbdd8b687a
  evidence_ids:
  - ev-b640fcf3cbac80f2
  - ev-8a5cdd7f8db46abf
  - ev-8707e0128be66011
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Hepes.yaml
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
  with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.
```
