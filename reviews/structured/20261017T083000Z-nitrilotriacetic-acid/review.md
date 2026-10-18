# Per-record structured review: Nitrilotriacetic_Acid (data/ingredients/mapped/Nitrilotriacetic_Acid.yaml)

- Review: 20261017T083000Z-nitrilotriacetic-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Nitrilotriacetic_Acid (data/ingredients/mapped/Nitrilotriacetic_Acid.yaml, record-f5080b09a822a6e3, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Nitrilotriacetic_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Nitrilotriacetic_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-f5080b09a822a6e3 | data/ingredients/mapped/Nitrilotriacetic_Acid.yaml | maintained | Nitrilotriacetic_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-f5080b09a822a6e3 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-f5080b09a822a6e3 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-f5080b09a822a6e3 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-f5080b09a822a6e3.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-f5080b09a822a6e3.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T06:48:22Z; reviewed SHA-256=7e9b42c517e23a71ad8c012b4391d2a1fbb89a1fd4814799d6452af97397b392; current SHA-256=7e9b42c517e23a71ad8c012b4391d2a1fbb89a1fd4814799d6452af97397b392; hash_changed=False. Reports=["reports/yaml_record_review/Nitrilotriacetic_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:44557 nitrilotriacetic acid identity passes, but CHELATOR is backed only by Mineral role text.

## Findings

### rec-f-bc4d4d62ac7fe1ba: Historical review coverage and residual narrative: Nitrilotriacetic_Acid

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-f5080b09a822a6e3.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T06:48:22Z; reviewed SHA-256=7e9b42c517e23a71ad8c012b4391d2a1fbb89a1fd4814799d6452af97397b392; current SHA-256=7e9b42c517e23a71ad8c012b4391d2a1fbb89a1fd4814799d6452af97397b392; hash_changed=False. Reports=["reports/yaml_record_review/Nitrilotriacetic_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:44557 nitrilotriacetic acid identity passes, but CHELATOR is backed only by Mineral role text.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-6d05eed58d71f1e7 | data/ingredients/mapped/Nitrilotriacetic_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1568],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:44557","line":1570,"mapping_status":"MAPPED","ontology_id":"CHEBI:44557","preferred_term":"Nitrilotriacetic acid"}],"identifier":"CHEBI:44557","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1348,"edge_count":1348,"occurrences":1348},"occurrence_statistics":{"media_count":1348,"total_occurrences":1348},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:44557","ontology_label":"nitrilotriacetic acid","ontology_source":"CHEBI"},"preferred_term":"Nitrilotriacetic acid","sssom_rows":[{"data_row":2097,"object_id":"CHEBI:44557","object_label":"nitrilotriacetic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Nitrilotriacetic_Acid","synonym_count":17} |
| ev-cbb0fbb86b4294d3 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1568] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-152215d32af7c4f0 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Nitrilotriacetic_Acid; data-row positions=[2097] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2097,"object_id":"CHEBI:44557","object_label":"nitrilotriacetic acid","other":"Complexon I&#124;H3nta&#124;Komplexon I&#124;N(CH2-COOH)3&#124;N,N-bis(carboxymethyl)glycine&#124;Nitrilotriacetic acid (NTA)&#124;Nitrilotriessigsaeure&#124;Triglycollamic acid&#124;Trilon A&#124;alpha,alpha',alpha''-trimethylaminetricarboxylic acid&#124;nitrilo-2,2',2''-triacetic acid&#124;tri(carboxymethyl)amine&#124;triglycine&#124;CAS:139-13-9","predicate_id":"skos:exactMatch","subject_id":"MIM:Nitrilotriacetic_Acid","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-49f4cba1cbb4a80d | docs/data/mapped_ingredients.csv; CSV lines=[1570] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:44557","line":1570,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1348","ontology_id":"CHEBI:44557","preferred_term":"Nitrilotriacetic acid","total_occurrences":"1348"}] |
| ev-694fe74365c10f18 | reports/yaml_record_review/Nitrilotriacetic_Acid.md; &#96;data/ingredients/mapped/Nitrilotriacetic_Acid.yaml&#96;:2; Verdict:4; Identity:11; Validation:20; Evidence:28; Completeness:45; Recommended Edits:52 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-b6ce816a18e88e12 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1065] | context_only | [{"current_record_sha256":"7e9b42c517e23a71ad8c012b4391d2a1fbb89a1fd4814799d6452af97397b392","finding_id":"SEM:78d7c2adc35d8470254c","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-nitrilotriacetic-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Nitrilotriacetic_Acid (data/ingredients/mapped/Nitrilotriacetic_Acid.yaml)'
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
summary: Per-record structured review for Nitrilotriacetic_Acid (data/ingredients/mapped/Nitrilotriacetic_Acid.yaml,
  record-f5080b09a822a6e3, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Nitrilotriacetic_Acid.yaml
    sha256: 7e9b42c517e23a71ad8c012b4391d2a1fbb89a1fd4814799d6452af97397b392
    role: target
  - path: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
    sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
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
  - path: reports/yaml_record_review/Nitrilotriacetic_Acid.md
    sha256: 6124139ab730f81b4e76ae926b252835622fcf76b6df87bb89838602ae4d275c
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-f5080b09a822a6e3
  path: data/ingredients/mapped/Nitrilotriacetic_Acid.yaml
  label: Nitrilotriacetic_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Nitrilotriacetic_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Nitrilotriacetic_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Nitrilotriacetic_Acid.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-f5080b09a822a6e3
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-f5080b09a822a6e3
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-f5080b09a822a6e3
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-f5080b09a822a6e3
evidence:
- evidence_id: ev-6d05eed58d71f1e7
  kind: record_content
  reference: data/ingredients/mapped/Nitrilotriacetic_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1568],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:44557","line":1570,"mapping_status":"MAPPED","ontology_id":"CHEBI:44557","preferred_term":"Nitrilotriacetic
    acid"}],"identifier":"CHEBI:44557","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1348,"edge_count":1348,"occurrences":1348},"occurrence_statistics":{"media_count":1348,"total_occurrences":1348},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:44557","ontology_label":"nitrilotriacetic
    acid","ontology_source":"CHEBI"},"preferred_term":"Nitrilotriacetic acid","sssom_rows":[{"data_row":2097,"object_id":"CHEBI:44557","object_label":"nitrilotriacetic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Nitrilotriacetic_Acid","synonym_count":17}'
  snapshot_sha256: 7e9b42c517e23a71ad8c012b4391d2a1fbb89a1fd4814799d6452af97397b392
- evidence_id: ev-cbb0fbb86b4294d3
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1568]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-152215d32af7c4f0
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Nitrilotriacetic_Acid; data-row positions=[2097]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2097,"object_id":"CHEBI:44557","object_label":"nitrilotriacetic
    acid","other":"Complexon I|H3nta|Komplexon I|N(CH2-COOH)3|N,N-bis(carboxymethyl)glycine|Nitrilotriacetic
    acid (NTA)|Nitrilotriessigsaeure|Triglycollamic acid|Trilon A|alpha,alpha'',alpha''''-trimethylaminetricarboxylic
    acid|nitrilo-2,2'',2''''-triacetic acid|tri(carboxymethyl)amine|triglycine|CAS:139-13-9","predicate_id":"skos:exactMatch","subject_id":"MIM:Nitrilotriacetic_Acid","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-49f4cba1cbb4a80d
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1570]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:44557","line":1570,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1348","ontology_id":"CHEBI:44557","preferred_term":"Nitrilotriacetic
    acid","total_occurrences":"1348"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-694fe74365c10f18
  kind: prior_review
  reference: reports/yaml_record_review/Nitrilotriacetic_Acid.md
  locator: '`data/ingredients/mapped/Nitrilotriacetic_Acid.yaml`:2; Verdict:4; Identity:11;
    Validation:20; Evidence:28; Completeness:45; Recommended Edits:52'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 6124139ab730f81b4e76ae926b252835622fcf76b6df87bb89838602ae4d275c
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Nitrilotriacetic_Acid.yaml`,\
    \ replace the\n  `CHELATOR` role evidence with inspected source-backed chelation\
    \ evidence, or\n  remove the role until that evidence exists.\n- Minor: remove\
    \ the auto-proposed `pmid: 34939907` evidence object from\n  `ontology_mapping`."
- evidence_id: ev-b6ce816a18e88e12
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1065]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"7e9b42c517e23a71ad8c012b4391d2a1fbb89a1fd4814799d6452af97397b392","finding_id":"SEM:78d7c2adc35d8470254c","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-a68c3731735b9dc3
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-f5080b09a822a6e3
  evidence_ids:
  - ev-6d05eed58d71f1e7
  - ev-cbb0fbb86b4294d3
  - ev-152215d32af7c4f0
  - ev-49f4cba1cbb4a80d
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-fec326d62957871e
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-f5080b09a822a6e3
  evidence_ids:
  - ev-694fe74365c10f18
  - ev-6d05eed58d71f1e7
  - ev-b6ce816a18e88e12
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T06:48:22Z;
    reviewed SHA-256=7e9b42c517e23a71ad8c012b4391d2a1fbb89a1fd4814799d6452af97397b392;
    current SHA-256=7e9b42c517e23a71ad8c012b4391d2a1fbb89a1fd4814799d6452af97397b392;
    hash_changed=False. Reports=["reports/yaml_record_review/Nitrilotriacetic_Acid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:44557 nitrilotriacetic acid identity passes, but CHELATOR is backed only
    by Mineral role text.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-694fe74365c10f18
    - ev-6d05eed58d71f1e7
  - name: legacy-native-ids
    value: '["SEM:78d7c2adc35d8470254c"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-6d05eed58d71f1e7
    - ev-694fe74365c10f18
    - ev-b6ce816a18e88e12
findings:
- finding_id: rec-f-bc4d4d62ac7fe1ba
  issue_key: mim-reconciliation-historical-review-coverage-and-r-f5080b09a822a6e3
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Nitrilotriacetic_Acid'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T06:48:22Z;
    reviewed SHA-256=7e9b42c517e23a71ad8c012b4391d2a1fbb89a1fd4814799d6452af97397b392;
    current SHA-256=7e9b42c517e23a71ad8c012b4391d2a1fbb89a1fd4814799d6452af97397b392;
    hash_changed=False. Reports=["reports/yaml_record_review/Nitrilotriacetic_Acid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:44557 nitrilotriacetic acid identity passes, but CHELATOR is backed only
    by Mineral role text.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-f5080b09a822a6e3
  evidence_ids:
  - ev-694fe74365c10f18
  - ev-6d05eed58d71f1e7
  - ev-b6ce816a18e88e12
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Nitrilotriacetic_Acid.yaml
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
  with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.
```
