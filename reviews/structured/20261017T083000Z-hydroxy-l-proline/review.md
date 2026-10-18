# Per-record structured review: Hydroxy-l-proline (data/ingredients/mapped/Hydroxy-l-proline.yaml)

- Review: 20261017T083000Z-hydroxy-l-proline
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Hydroxy-l-proline (data/ingredients/mapped/Hydroxy-l-proline.yaml, record-40a9ee2780df21e0, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Hydroxy-l-proline.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Hydroxy-l-proline.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-40a9ee2780df21e0 | data/ingredients/mapped/Hydroxy-l-proline.yaml | maintained | Hydroxy-l-proline |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-40a9ee2780df21e0 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-40a9ee2780df21e0 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-40a9ee2780df21e0 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-40a9ee2780df21e0.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-40a9ee2780df21e0.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T19:54:17Z; reviewed SHA-256=ececbb9977c65c454e64dc0e42104f15911e9ca87b170f847d4a4066c0e02ba8; current SHA-256=ececbb9977c65c454e64dc0e42104f15911e9ca87b170f847d4a4066c0e02ba8; hash_changed=False. Reports=["reports/yaml_record_review/Hydroxy-l-proline.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact trans-4-hydroxy-L-proline identity and final SSSOM row pass, but AMINO_ACID_SOURCE is only a provisional CHEBI-ancestry assertion.

### Historical provisional-role concern

evidence: concern. Targets: record-40a9ee2780df21e0.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-48631dadd41d1b5b: Reassess prediction-only role support: Hydroxy-L-Proline

major / open / confirmed; issue key: mim-reconciliation-role-support-40a9ee2780df21e0.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-48631dadd41d1b5b

Reassess prediction-only role support: Hydroxy-L-Proline

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-127753b01f054738 | data/ingredients/mapped/Hydroxy-l-proline.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1146],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18095","line":1148,"mapping_status":"MAPPED","ontology_id":"CHEBI:18095","preferred_term":"Hydroxy-L-Proline"}],"identifier":"CHEBI:18095","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:18095","ontology_label":"trans-4-hydroxy-L-proline","ontology_source":"CHEBI"},"preferred_term":"Hydroxy-L-Proline","sssom_rows":[{"data_row":1456,"object_id":"CHEBI:18095","object_label":"trans-4-hydroxy-L-proline","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Hydroxy-l-proline","synonym_count":11} |
| ev-8ca2b8aaf0058c05 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1146] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-1d842c570c2ae666 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Hydroxy-l-proline; data-row positions=[1456] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1456,"object_id":"CHEBI:18095","object_label":"trans-4-hydroxy-L-proline","other":"(2S,4R)-4-hydroxy-2-pyrrolidinecarboxylic acid&#124;(2S,4R)-trans-4-hydroxyproline&#124;(4R)-4-hydroxy-L-proline&#124;Hydroxyproline&#124;Hypro&#124;L-4-Hydroxyproline&#124;L-threo-4-hydroxyproline&#124;delta-hydroxyproline&#124;trans-Hydroxyproline&#124;trans-L-Hydroxyproline&#124;CAS:51-35-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Hydroxy-l-proline","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-87e503c752d68535 | docs/data/mapped_ingredients.csv; CSV lines=[1148] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:18095","line":1148,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"3","ontology_id":"CHEBI:18095","preferred_term":"Hydroxy-L-Proline","total_occurrences":"3"}] |
| ev-c7dfd27d7246519b | reports/yaml_record_review/Hydroxy-l-proline.md; &#96;data/ingredients/mapped/Hydroxy-l-proline.yaml&#96;:2; Verdict:4; Identity:10; Validation:23; Evidence:35; Completeness:52; Recommended Edits:59 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-7c1a00314a1af58a | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[742,1376] | context_only | [{"current_record_sha256":"ececbb9977c65c454e64dc0e42104f15911e9ca87b170f847d4a4066c0e02ba8","finding_id":"SEM:81fef60bd6553526a5fb","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"ececbb9977c65c454e64dc0e42104f15911e9ca87b170f847d4a4066c0e02ba8","finding_id":"SEM:dc3edf9d1ba5214268a6","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-967f4799cc43088d | data/ingredients/mapped/Hydroxy-l-proline.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1146],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18095","line":1148,"mapping_status":"MAPPED","ontology_id":"CHEBI:18095","preferred_term":"Hydroxy-L-Proline"}],"identifier":"CHEBI:18095","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:18095","ontology_label":"trans-4-hydroxy-L-proline","ontology_source":"CHEBI"},"preferred_term":"Hydroxy-L-Proline","sssom_rows":[{"data_row":1456,"object_id":"CHEBI:18095","object_label":"trans-4-hydroxy-L-proline","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Hydroxy-l-proline","synonym_count":11} |
| ev-833af64d30dcb143 | reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml; findings[finding_id=f-48631dadd41d1b5b] | context_only | Predecessor structured review finding f-48631dadd41d1b5b in 20261011T024635Z-mim-reconcile-all-batch-07 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-hydroxy-l-proline
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Hydroxy-l-proline (data/ingredients/mapped/Hydroxy-l-proline.yaml)'
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
native_verdict: mapping_status=MAPPED; open=1; deferred=0
scientific_review: false
summary: Per-record structured review for Hydroxy-l-proline (data/ingredients/mapped/Hydroxy-l-proline.yaml,
  record-40a9ee2780df21e0, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Hydroxy-l-proline.yaml
    sha256: ececbb9977c65c454e64dc0e42104f15911e9ca87b170f847d4a4066c0e02ba8
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
  - path: reports/yaml_record_review/Hydroxy-l-proline.md
    sha256: 5cc231f0f555bd1ef4980e0792c7671042f5bc5428924846a4b8bf1cb6270a5d
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-40a9ee2780df21e0
  path: data/ingredients/mapped/Hydroxy-l-proline.yaml
  label: Hydroxy-l-proline
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Hydroxy-l-proline.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Hydroxy-l-proline.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Hydroxy-l-proline.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-40a9ee2780df21e0
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-40a9ee2780df21e0
  evidence_ids:
  - ev-127753b01f054738
  - ev-8ca2b8aaf0058c05
  - ev-1d842c570c2ae666
  - ev-87e503c752d68535
  - ev-967f4799cc43088d
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-40a9ee2780df21e0
  evidence_ids:
  - ev-127753b01f054738
  - ev-7c1a00314a1af58a
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-40a9ee2780df21e0
  evidence_ids:
  - ev-c7dfd27d7246519b
  - ev-7c1a00314a1af58a
  - ev-833af64d30dcb143
evidence:
- evidence_id: ev-127753b01f054738
  kind: record_content
  reference: data/ingredients/mapped/Hydroxy-l-proline.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1146],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18095","line":1148,"mapping_status":"MAPPED","ontology_id":"CHEBI:18095","preferred_term":"Hydroxy-L-Proline"}],"identifier":"CHEBI:18095","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:18095","ontology_label":"trans-4-hydroxy-L-proline","ontology_source":"CHEBI"},"preferred_term":"Hydroxy-L-Proline","sssom_rows":[{"data_row":1456,"object_id":"CHEBI:18095","object_label":"trans-4-hydroxy-L-proline","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Hydroxy-l-proline","synonym_count":11}'
  snapshot_sha256: ececbb9977c65c454e64dc0e42104f15911e9ca87b170f847d4a4066c0e02ba8
- evidence_id: ev-8ca2b8aaf0058c05
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1146]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-1d842c570c2ae666
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Hydroxy-l-proline; data-row positions=[1456]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1456,"object_id":"CHEBI:18095","object_label":"trans-4-hydroxy-L-proline","other":"(2S,4R)-4-hydroxy-2-pyrrolidinecarboxylic
    acid|(2S,4R)-trans-4-hydroxyproline|(4R)-4-hydroxy-L-proline|Hydroxyproline|Hypro|L-4-Hydroxyproline|L-threo-4-hydroxyproline|delta-hydroxyproline|trans-Hydroxyproline|trans-L-Hydroxyproline|CAS:51-35-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Hydroxy-l-proline","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-87e503c752d68535
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1148]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:18095","line":1148,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"3","ontology_id":"CHEBI:18095","preferred_term":"Hydroxy-L-Proline","total_occurrences":"3"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-c7dfd27d7246519b
  kind: prior_review
  reference: reports/yaml_record_review/Hydroxy-l-proline.md
  locator: '`data/ingredients/mapped/Hydroxy-l-proline.yaml`:2; Verdict:4; Identity:10;
    Validation:23; Evidence:35; Completeness:52; Recommended Edits:59'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 5cc231f0f555bd1ef4980e0792c7671042f5bc5428924846a4b8bf1cb6270a5d
  quote: "Recommended Edits:\n- Major: remove `nutritional_roles.AMINO_ACID_SOURCE`\
    \ unless an inspected FEBA\n  source or literature source can support hydroxy-L-proline\
    \ as an amino acid\n  source, then rerun strict, term, round-trip, id-label, component,\
    \ and SSSOM\n  validation."
- evidence_id: ev-7c1a00314a1af58a
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[742,1376]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"ececbb9977c65c454e64dc0e42104f15911e9ca87b170f847d4a4066c0e02ba8","finding_id":"SEM:81fef60bd6553526a5fb","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"ececbb9977c65c454e64dc0e42104f15911e9ca87b170f847d4a4066c0e02ba8","finding_id":"SEM:dc3edf9d1ba5214268a6","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-967f4799cc43088d
  kind: record_content
  reference: data/ingredients/mapped/Hydroxy-l-proline.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1146],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18095","line":1148,"mapping_status":"MAPPED","ontology_id":"CHEBI:18095","preferred_term":"Hydroxy-L-Proline"}],"identifier":"CHEBI:18095","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:18095","ontology_label":"trans-4-hydroxy-L-proline","ontology_source":"CHEBI"},"preferred_term":"Hydroxy-L-Proline","sssom_rows":[{"data_row":1456,"object_id":"CHEBI:18095","object_label":"trans-4-hydroxy-L-proline","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Hydroxy-l-proline","synonym_count":11}'
  snapshot_sha256: ececbb9977c65c454e64dc0e42104f15911e9ca87b170f847d4a4066c0e02ba8
- evidence_id: ev-833af64d30dcb143
  kind: prior_review
  reference: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
  locator: findings[finding_id=f-48631dadd41d1b5b]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-48631dadd41d1b5b in 20261011T024635Z-mim-reconcile-all-batch-07
  snapshot_sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
assessments:
- assessment_id: a-4a9e9871a1a57e17
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-40a9ee2780df21e0
  evidence_ids:
  - ev-127753b01f054738
  - ev-8ca2b8aaf0058c05
  - ev-1d842c570c2ae666
  - ev-87e503c752d68535
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-20399b7ef7801c41
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-40a9ee2780df21e0
  evidence_ids:
  - ev-c7dfd27d7246519b
  - ev-127753b01f054738
  - ev-7c1a00314a1af58a
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T19:54:17Z;
    reviewed SHA-256=ececbb9977c65c454e64dc0e42104f15911e9ca87b170f847d4a4066c0e02ba8;
    current SHA-256=ececbb9977c65c454e64dc0e42104f15911e9ca87b170f847d4a4066c0e02ba8;
    hash_changed=False. Reports=["reports/yaml_record_review/Hydroxy-l-proline.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    trans-4-hydroxy-L-proline identity and final SSSOM row pass, but AMINO_ACID_SOURCE
    is only a provisional CHEBI-ancestry assertion.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c7dfd27d7246519b
    - ev-127753b01f054738
  - name: legacy-native-ids
    value: '["SEM:81fef60bd6553526a5fb","SEM:dc3edf9d1ba5214268a6"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-127753b01f054738
    - ev-c7dfd27d7246519b
    - ev-7c1a00314a1af58a
- assessment_id: a-967f4799cc43088d
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-40a9ee2780df21e0
  evidence_ids:
  - ev-c7dfd27d7246519b
  - ev-967f4799cc43088d
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c7dfd27d7246519b
    - ev-967f4799cc43088d
findings:
- finding_id: rec-f-48631dadd41d1b5b
  issue_key: mim-reconciliation-role-support-40a9ee2780df21e0
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Hydroxy-L-Proline'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-40a9ee2780df21e0
  evidence_ids:
  - ev-c7dfd27d7246519b
  - ev-967f4799cc43088d
  - ev-833af64d30dcb143
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Hydroxy-l-proline.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024635Z-mim-reconcile-all-batch-07
    finding_id: f-48631dadd41d1b5b
actions:
- action_id: rec-action-48631dadd41d1b5b
  description: 'Reassess prediction-only role support: Hydroxy-L-Proline'
  finding_ids:
  - rec-f-48631dadd41d1b5b
  target_ids:
  - record-40a9ee2780df21e0
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Hydroxy-l-proline.yaml
    role: maintained ingredient
  acceptance_checks:
  - Address the exact fields/tokens and evidence gap described in this finding; preserve
    unrelated source labels and audit history.
  - Inspect the original preparation, organism, or mapping evidence where needed;
    do not promote a label/name-pattern inference to proof.
  - For an authorized fix, synchronize maintained surfaces, run focused validation,
    and save an evidence-backed successor citing this finding.
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
