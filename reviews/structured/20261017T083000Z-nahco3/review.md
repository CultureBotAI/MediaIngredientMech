# Per-record structured review: Nahco3 (data/ingredients/mapped/Nahco3.yaml)

- Review: 20261017T083000Z-nahco3
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Nahco3 (data/ingredients/mapped/Nahco3.yaml, record-e6750d2537cb73aa, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Nahco3.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Nahco3.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-e6750d2537cb73aa | data/ingredients/mapped/Nahco3.yaml | maintained | Nahco3 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-e6750d2537cb73aa | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-e6750d2537cb73aa | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-e6750d2537cb73aa | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-e6750d2537cb73aa.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-e6750d2537cb73aa.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:57:05Z; reviewed SHA-256=97cc3f952982f9f22d0024c4ccb5aaa942c22edb5332782c69aee96d7b744998; current SHA-256=97cc3f952982f9f22d0024c4ccb5aaa942c22edb5332782c69aee96d7b744998; hash_changed=False. Reports=["reports/yaml_record_review/Nahco3.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:32139 sodium hydrogencarbonate identity passes, but final other has malformed, vendor, and concentration labels.

## Findings

### rec-f-5e2311f0c310bbd2: Historical review coverage and residual narrative: Nahco3

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-e6750d2537cb73aa.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:57:05Z; reviewed SHA-256=97cc3f952982f9f22d0024c4ccb5aaa942c22edb5332782c69aee96d7b744998; current SHA-256=97cc3f952982f9f22d0024c4ccb5aaa942c22edb5332782c69aee96d7b744998; hash_changed=False. Reports=["reports/yaml_record_review/Nahco3.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:32139 sodium hydrogencarbonate identity passes, but final other has malformed, vendor, and concentration labels.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-7686d351de824d65 | data/ingredients/mapped/Nahco3.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1525],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:32139","line":1527,"mapping_status":"MAPPED","ontology_id":"CHEBI:32139","preferred_term":"NaHCO3"}],"identifier":"CHEBI:32139","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3163,"edge_count":3163,"occurrences":3168},"occurrence_statistics":{"media_count":3163,"total_occurrences":3168},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:32139","ontology_label":"sodium hydrogencarbonate","ontology_source":"CHEBI"},"preferred_term":"NaHCO3","sssom_rows":[{"data_row":2035,"object_id":"CHEBI:32139","object_label":"sodium hydrogencarbonate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Nahco3","synonym_count":26} |
| ev-6fcd88cfeb256d0b | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1525] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-cb1407c477a70ddb | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Nahco3; data-row positions=[2035] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2035,"object_id":"CHEBI:32139","object_label":"sodium hydrogencarbonate","other":"E 500&#124;E-500&#124;E500&#124;NaHCO&#124;Natriumhydrogenkarbonat&#124;Sodium Bicarbonate&#124;baking soda&#124;bicarbonate of soda&#124;carbonic acid monosodium salt&#124;sodium acid carbonate&#124;sodium hydrogen carbonate&#124;NaHCO3(Fisher S 233)&#124;NaHCO3 (10% (w/v))&#124;NaHCO3 (10%, w/v)&#124;NaHCO3 (1 M)&#124;NaHCO3 (3% (w/v))&#124;NaHCO3 (5%, w/v)&#124;NaHCO3 (7.5% w/v in water)&#124;CAS:144-55-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Nahco3","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-0e97617fe475d3db | docs/data/mapped_ingredients.csv; CSV lines=[1527] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:32139","line":1527,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"3163","ontology_id":"CHEBI:32139","preferred_term":"NaHCO3","total_occurrences":"3168"}] |
| ev-c09ed573da2bee14 | reports/yaml_record_review/Nahco3.md; &#96;data/ingredients/mapped/Nahco3.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:29; Completeness:46; Recommended Edits:54 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-5e4688b75ad369d9 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1028] | context_only | [{"current_record_sha256":"97cc3f952982f9f22d0024c4ccb5aaa942c22edb5332782c69aee96d7b744998","finding_id":"SEM:b4194209c49349640761","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-nahco3
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Nahco3 (data/ingredients/mapped/Nahco3.yaml)'
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
summary: Per-record structured review for Nahco3 (data/ingredients/mapped/Nahco3.yaml,
  record-e6750d2537cb73aa, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Nahco3.yaml
    sha256: 97cc3f952982f9f22d0024c4ccb5aaa942c22edb5332782c69aee96d7b744998
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
  - path: reports/yaml_record_review/Nahco3.md
    sha256: a0bcb79f56668a6e6b7c9042bb038d5e407a92e86bf5b13952b297d73dee4bef
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-e6750d2537cb73aa
  path: data/ingredients/mapped/Nahco3.yaml
  label: Nahco3
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Nahco3.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Nahco3.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Nahco3.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-e6750d2537cb73aa
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-e6750d2537cb73aa
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-e6750d2537cb73aa
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-e6750d2537cb73aa
evidence:
- evidence_id: ev-7686d351de824d65
  kind: record_content
  reference: data/ingredients/mapped/Nahco3.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1525],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:32139","line":1527,"mapping_status":"MAPPED","ontology_id":"CHEBI:32139","preferred_term":"NaHCO3"}],"identifier":"CHEBI:32139","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3163,"edge_count":3163,"occurrences":3168},"occurrence_statistics":{"media_count":3163,"total_occurrences":3168},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:32139","ontology_label":"sodium
    hydrogencarbonate","ontology_source":"CHEBI"},"preferred_term":"NaHCO3","sssom_rows":[{"data_row":2035,"object_id":"CHEBI:32139","object_label":"sodium
    hydrogencarbonate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Nahco3","synonym_count":26}'
  snapshot_sha256: 97cc3f952982f9f22d0024c4ccb5aaa942c22edb5332782c69aee96d7b744998
- evidence_id: ev-6fcd88cfeb256d0b
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1525]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-cb1407c477a70ddb
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Nahco3; data-row positions=[2035]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2035,"object_id":"CHEBI:32139","object_label":"sodium
    hydrogencarbonate","other":"E 500|E-500|E500|NaHCO|Natriumhydrogenkarbonat|Sodium
    Bicarbonate|baking soda|bicarbonate of soda|carbonic acid monosodium salt|sodium
    acid carbonate|sodium hydrogen carbonate|NaHCO3(Fisher S 233)|NaHCO3 (10% (w/v))|NaHCO3
    (10%, w/v)|NaHCO3 (1 M)|NaHCO3 (3% (w/v))|NaHCO3 (5%, w/v)|NaHCO3 (7.5% w/v in
    water)|CAS:144-55-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Nahco3","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-0e97617fe475d3db
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1527]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:32139","line":1527,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"3163","ontology_id":"CHEBI:32139","preferred_term":"NaHCO3","total_occurrences":"3168"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-c09ed573da2bee14
  kind: prior_review
  reference: reports/yaml_record_review/Nahco3.md
  locator: '`data/ingredients/mapped/Nahco3.yaml`:2; Verdict:4; Identity:11; Validation:21;
    Evidence:29; Completeness:46; Recommended Edits:54'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: a0bcb79f56668a6e6b7c9042bb038d5e407a92e86bf5b13952b297d73dee4bef
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Nahco3.yaml`, reject\
    \ or delete `NaHCO`,\n  `NaHCO3(Fisher S 233)`, and the concentration-qualified\
    \ `NaHCO3 (...)`\n  synonyms from the CultureMech alias backfill.\n- Minor: remove\
    \ `pmid: 39954419` from\n  `ontology_mapping.evidence` unless a curator finds\
    \ it materially supports\n  the identity decision better than the existing database\
    \ evidence."
- evidence_id: ev-5e4688b75ad369d9
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1028]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"97cc3f952982f9f22d0024c4ccb5aaa942c22edb5332782c69aee96d7b744998","finding_id":"SEM:b4194209c49349640761","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-e82726eb9b2a614a
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-e6750d2537cb73aa
  evidence_ids:
  - ev-7686d351de824d65
  - ev-6fcd88cfeb256d0b
  - ev-cb1407c477a70ddb
  - ev-0e97617fe475d3db
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-1b7d90b9ee843a02
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-e6750d2537cb73aa
  evidence_ids:
  - ev-c09ed573da2bee14
  - ev-7686d351de824d65
  - ev-5e4688b75ad369d9
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:57:05Z;
    reviewed SHA-256=97cc3f952982f9f22d0024c4ccb5aaa942c22edb5332782c69aee96d7b744998;
    current SHA-256=97cc3f952982f9f22d0024c4ccb5aaa942c22edb5332782c69aee96d7b744998;
    hash_changed=False. Reports=["reports/yaml_record_review/Nahco3.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI:32139 sodium
    hydrogencarbonate identity passes, but final other has malformed, vendor, and
    concentration labels.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c09ed573da2bee14
    - ev-7686d351de824d65
  - name: legacy-native-ids
    value: '["SEM:b4194209c49349640761"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-7686d351de824d65
    - ev-c09ed573da2bee14
    - ev-5e4688b75ad369d9
findings:
- finding_id: rec-f-5e2311f0c310bbd2
  issue_key: mim-reconciliation-historical-review-coverage-and-r-e6750d2537cb73aa
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Nahco3'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:57:05Z;
    reviewed SHA-256=97cc3f952982f9f22d0024c4ccb5aaa942c22edb5332782c69aee96d7b744998;
    current SHA-256=97cc3f952982f9f22d0024c4ccb5aaa942c22edb5332782c69aee96d7b744998;
    hash_changed=False. Reports=["reports/yaml_record_review/Nahco3.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI:32139 sodium
    hydrogencarbonate identity passes, but final other has malformed, vendor, and
    concentration labels.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-e6750d2537cb73aa
  evidence_ids:
  - ev-c09ed573da2bee14
  - ev-7686d351de824d65
  - ev-5e4688b75ad369d9
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Nahco3.yaml
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
