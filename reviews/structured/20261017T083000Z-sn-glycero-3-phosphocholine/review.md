# Per-record structured review: Sn-glycero-3-phosphocholine (data/ingredients/mapped/Sn-glycero-3-phosphocholine.yaml)

- Review: 20261017T083000Z-sn-glycero-3-phosphocholine
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Sn-glycero-3-phosphocholine (data/ingredients/mapped/Sn-glycero-3-phosphocholine.yaml, record-2c9fd92cd6299a78, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Sn-glycero-3-phosphocholine.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Sn-glycero-3-phosphocholine.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-2c9fd92cd6299a78 | data/ingredients/mapped/Sn-glycero-3-phosphocholine.yaml | maintained | Sn-glycero-3-phosphocholine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-2c9fd92cd6299a78 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-2c9fd92cd6299a78 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-2c9fd92cd6299a78 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-2c9fd92cd6299a78.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-2c9fd92cd6299a78.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T14:26:03Z; reviewed SHA-256=307b68574fa179f22b8090a795d8368da8d3d83015930a9cd2ebe400ddaeec59; current SHA-256=307b68574fa179f22b8090a795d8368da8d3d83015930a9cd2ebe400ddaeec59; hash_changed=False. Reports=["reports/yaml_record_review/Sn-glycero-3-phosphocholine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:16870 identity, structure, CAS, and occurrence count pass, but final SSSOM exports related/non-exact kg-microbe synonyms.

## Findings

### rec-f-f619156e606fd4fc: Historical review coverage and residual narrative: Sn-glycero-3-phosphocholine

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-2c9fd92cd6299a78.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T14:26:03Z; reviewed SHA-256=307b68574fa179f22b8090a795d8368da8d3d83015930a9cd2ebe400ddaeec59; current SHA-256=307b68574fa179f22b8090a795d8368da8d3d83015930a9cd2ebe400ddaeec59; hash_changed=False. Reports=["reports/yaml_record_review/Sn-glycero-3-phosphocholine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:16870 identity, structure, CAS, and occurrence count pass, but final SSSOM exports related/non-exact kg-microbe synonyms.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-e7f02857d277de07 | data/ingredients/mapped/Sn-glycero-3-phosphocholine.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2087],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16870","line":2089,"mapping_status":"MAPPED","ontology_id":"CHEBI:16870","preferred_term":"sn-glycero-3-phosphocholine"}],"identifier":"CHEBI:16870","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":10,"edge_count":10,"occurrences":10},"occurrence_statistics":{"media_count":10,"total_occurrences":10},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:16870","ontology_label":"choline alfoscerate","ontology_source":"CHEBI"},"preferred_term":"sn-glycero-3-phosphocholine","sssom_rows":[{"data_row":2525,"object_id":"CHEBI:16870","object_label":"choline alfoscerate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sn-glycero-3-phosphocholine","synonym_count":20} |
| ev-d4a5d409d534ebde | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2087] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-ec4d2032c2fdbec5 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Sn-glycero-3-phosphocholine; data-row positions=[2525] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2525,"object_id":"CHEBI:16870","object_label":"choline alfoscerate","other":"(2R)-2,3-dihydroxypropyl 2-(trimethylammonio)ethyl phosphate&#124;(2R)-2,3-dihydroxypropyl 2-(trimethylazaniumyl)ethyl phosphate&#124;2-{[(2R)-2,3-dihydroxypropoxy](hydroxy)phosphoryloxy}-N,N,N-trimethylethanaminium&#124;Choline alphoscerate&#124;Choline glycerophosphate&#124;Cholini glycerophosphas&#124;GPCho&#124;Glicerofosfato de colina&#124;Glycerol-3-phosphatidylcholine&#124;Glycerophosphate de choline&#124;L-Choline hydroxide 2,3-dihydroxypropyl hydrogen phosphate inner salt&#124;L-alpha-Glycerophosphocholine&#124;L-alpha-Glycerophosphorylcholine&#124;alfoscerate de choline&#124;alfoscerato de colina&#124;alpha-Glycerophosphorylcholine&#124;cholini alfosceras&#124;glycerol-3-phosphocholine&#124;sn-3-GPC&#124;CAS:28319-77-9","predicate_id":"skos:exactMatch","subject_id":"MIM:Sn-glycero-3-phosphocholine","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-68ad77fa6263278b | docs/data/mapped_ingredients.csv; CSV lines=[2089] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:16870","line":2089,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"10","ontology_id":"CHEBI:16870","preferred_term":"sn-glycero-3-phosphocholine","total_occurrences":"10"}] |
| ev-3834653d9e5af031 | reports/yaml_record_review/Sn-glycero-3-phosphocholine.md; &#96;data/ingredients/mapped/Sn-glycero-3-phosphocholine.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-03d5ccf5aef5efde | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1201] | context_only | [{"current_record_sha256":"307b68574fa179f22b8090a795d8368da8d3d83015930a9cd2ebe400ddaeec59","finding_id":"SEM:2595ac5e47783a119f0b","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-sn-glycero-3-phosphocholine
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Sn-glycero-3-phosphocholine (data/ingredients/mapped/Sn-glycero-3-phosphocholine.yaml)'
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
summary: Per-record structured review for Sn-glycero-3-phosphocholine (data/ingredients/mapped/Sn-glycero-3-phosphocholine.yaml,
  record-2c9fd92cd6299a78, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Sn-glycero-3-phosphocholine.yaml
    sha256: 307b68574fa179f22b8090a795d8368da8d3d83015930a9cd2ebe400ddaeec59
    role: target
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
    sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
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
  - path: reports/yaml_record_review/Sn-glycero-3-phosphocholine.md
    sha256: b2cacdc80e0aba7e13e0fe9723321af35fec84848387d82b9d3b7dd7020d90ff
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-2c9fd92cd6299a78
  path: data/ingredients/mapped/Sn-glycero-3-phosphocholine.yaml
  label: Sn-glycero-3-phosphocholine
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sn-glycero-3-phosphocholine.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Sn-glycero-3-phosphocholine.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Sn-glycero-3-phosphocholine.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-2c9fd92cd6299a78
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-2c9fd92cd6299a78
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-2c9fd92cd6299a78
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-2c9fd92cd6299a78
evidence:
- evidence_id: ev-e7f02857d277de07
  kind: record_content
  reference: data/ingredients/mapped/Sn-glycero-3-phosphocholine.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2087],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16870","line":2089,"mapping_status":"MAPPED","ontology_id":"CHEBI:16870","preferred_term":"sn-glycero-3-phosphocholine"}],"identifier":"CHEBI:16870","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":10,"edge_count":10,"occurrences":10},"occurrence_statistics":{"media_count":10,"total_occurrences":10},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:16870","ontology_label":"choline
    alfoscerate","ontology_source":"CHEBI"},"preferred_term":"sn-glycero-3-phosphocholine","sssom_rows":[{"data_row":2525,"object_id":"CHEBI:16870","object_label":"choline
    alfoscerate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sn-glycero-3-phosphocholine","synonym_count":20}'
  snapshot_sha256: 307b68574fa179f22b8090a795d8368da8d3d83015930a9cd2ebe400ddaeec59
- evidence_id: ev-d4a5d409d534ebde
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2087]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-ec4d2032c2fdbec5
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Sn-glycero-3-phosphocholine; data-row positions=[2525]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2525,"object_id":"CHEBI:16870","object_label":"choline
    alfoscerate","other":"(2R)-2,3-dihydroxypropyl 2-(trimethylammonio)ethyl phosphate|(2R)-2,3-dihydroxypropyl
    2-(trimethylazaniumyl)ethyl phosphate|2-{[(2R)-2,3-dihydroxypropoxy](hydroxy)phosphoryloxy}-N,N,N-trimethylethanaminium|Choline
    alphoscerate|Choline glycerophosphate|Cholini glycerophosphas|GPCho|Glicerofosfato
    de colina|Glycerol-3-phosphatidylcholine|Glycerophosphate de choline|L-Choline
    hydroxide 2,3-dihydroxypropyl hydrogen phosphate inner salt|L-alpha-Glycerophosphocholine|L-alpha-Glycerophosphorylcholine|alfoscerate
    de choline|alfoscerato de colina|alpha-Glycerophosphorylcholine|cholini alfosceras|glycerol-3-phosphocholine|sn-3-GPC|CAS:28319-77-9","predicate_id":"skos:exactMatch","subject_id":"MIM:Sn-glycero-3-phosphocholine","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-68ad77fa6263278b
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2089]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:16870","line":2089,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"10","ontology_id":"CHEBI:16870","preferred_term":"sn-glycero-3-phosphocholine","total_occurrences":"10"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-3834653d9e5af031
  kind: prior_review
  reference: reports/yaml_record_review/Sn-glycero-3-phosphocholine.md
  locator: '`data/ingredients/mapped/Sn-glycero-3-phosphocholine.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: b2cacdc80e0aba7e13e0fe9723321af35fec84848387d82b9d3b7dd7020d90ff
- evidence_id: ev-03d5ccf5aef5efde
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1201]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"307b68574fa179f22b8090a795d8368da8d3d83015930a9cd2ebe400ddaeec59","finding_id":"SEM:2595ac5e47783a119f0b","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-31e7b832cb9f2b22
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-2c9fd92cd6299a78
  evidence_ids:
  - ev-e7f02857d277de07
  - ev-d4a5d409d534ebde
  - ev-ec4d2032c2fdbec5
  - ev-68ad77fa6263278b
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-dbe6bbe10d612758
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-2c9fd92cd6299a78
  evidence_ids:
  - ev-3834653d9e5af031
  - ev-e7f02857d277de07
  - ev-03d5ccf5aef5efde
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T14:26:03Z;
    reviewed SHA-256=307b68574fa179f22b8090a795d8368da8d3d83015930a9cd2ebe400ddaeec59;
    current SHA-256=307b68574fa179f22b8090a795d8368da8d3d83015930a9cd2ebe400ddaeec59;
    hash_changed=False. Reports=["reports/yaml_record_review/Sn-glycero-3-phosphocholine.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:16870 identity, structure, CAS, and occurrence count pass, but final SSSOM
    exports related/non-exact kg-microbe synonyms.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-3834653d9e5af031
    - ev-e7f02857d277de07
  - name: legacy-native-ids
    value: '["SEM:2595ac5e47783a119f0b"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-e7f02857d277de07
    - ev-3834653d9e5af031
    - ev-03d5ccf5aef5efde
findings:
- finding_id: rec-f-f619156e606fd4fc
  issue_key: mim-reconciliation-historical-review-coverage-and-r-2c9fd92cd6299a78
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Sn-glycero-3-phosphocholine'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T14:26:03Z;
    reviewed SHA-256=307b68574fa179f22b8090a795d8368da8d3d83015930a9cd2ebe400ddaeec59;
    current SHA-256=307b68574fa179f22b8090a795d8368da8d3d83015930a9cd2ebe400ddaeec59;
    hash_changed=False. Reports=["reports/yaml_record_review/Sn-glycero-3-phosphocholine.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:16870 identity, structure, CAS, and occurrence count pass, but final SSSOM
    exports related/non-exact kg-microbe synonyms.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-2c9fd92cd6299a78
  evidence_ids:
  - ev-3834653d9e5af031
  - ev-e7f02857d277de07
  - ev-03d5ccf5aef5efde
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sn-glycero-3-phosphocholine.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.
```
