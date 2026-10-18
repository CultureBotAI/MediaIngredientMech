# Per-record structured review: Na-stearate (data/ingredients/mapped/Na-stearate.yaml)

- Review: 20261017T083000Z-na-stearate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Na-stearate (data/ingredients/mapped/Na-stearate.yaml, record-9fd515657847bbc7, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Na-stearate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Na-stearate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-9fd515657847bbc7 | data/ingredients/mapped/Na-stearate.yaml | maintained | Na-stearate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-9fd515657847bbc7 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-9fd515657847bbc7 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-9fd515657847bbc7 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-9fd515657847bbc7.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-9fd515657847bbc7.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:01:32Z; reviewed SHA-256=51532547e6cc93a873def26898ab576bb34fafd988d3254f4a91b7fe810c558d; current SHA-256=51532547e6cc93a873def26898ab576bb34fafd988d3254f4a91b7fe810c558d; hash_changed=False. Reports=["reports/yaml_record_review/Na-stearate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:132109 sodium octadecanoate identity, CAS-backed structure, occurrence count, synonyms, and final exact row pass, but SURFACTANT is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-9fd515657847bbc7.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-641361f3ac015a6b: Reassess prediction-only role support: Na-stearate

major / open / confirmed; issue key: mim-reconciliation-role-support-9fd515657847bbc7.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-641361f3ac015a6b

Reassess prediction-only role support: Na-stearate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-77c50f268bf68643 | data/ingredients/mapped/Na-stearate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1473],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:132109","line":1475,"mapping_status":"MAPPED","ontology_id":"CHEBI:132109","preferred_term":"Na-stearate"}],"identifier":"CHEBI:132109","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:132109","ontology_label":"sodium octadecanoate","ontology_source":"CHEBI"},"preferred_term":"Na-stearate","sssom_rows":[{"data_row":1980,"object_id":"CHEBI:132109","object_label":"sodium octadecanoate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na-stearate","synonym_count":4} |
| ev-241ac0d895554099 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1473] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-5cd38a039413c16c | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Na-stearate; data-row positions=[1980] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1980,"object_id":"CHEBI:132109","object_label":"sodium octadecanoate","other":"Octadecanoic acid, sodium salt&#124;Stearic acid, sodium salt&#124;sodium stearate&#124;CAS:822-16-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Na-stearate","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-a265d8e6833510d2 | docs/data/mapped_ingredients.csv; CSV lines=[1475] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:132109","line":1475,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"3","ontology_id":"CHEBI:132109","preferred_term":"Na-stearate","total_occurrences":"3"}] |
| ev-ac320132f18b68b1 | reports/yaml_record_review/Na-stearate.md; &#96;data/ingredients/mapped/Na-stearate.yaml&#96;:2; Verdict:4; Identity:11; Validation:20; Evidence:27; Completeness:38; Recommended Edits:44 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-f002acfe33c6878a | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[981,2011] | context_only | [{"current_record_sha256":"51532547e6cc93a873def26898ab576bb34fafd988d3254f4a91b7fe810c558d","finding_id":"SEM:7a8b966bc50379e6d716","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"51532547e6cc93a873def26898ab576bb34fafd988d3254f4a91b7fe810c558d","finding_id":"SEM:87ac51213bd0f4e75c3f","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-d01deb166a9b6c98 | data/ingredients/mapped/Na-stearate.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1473],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:132109","line":1475,"mapping_status":"MAPPED","ontology_id":"CHEBI:132109","preferred_term":"Na-stearate"}],"identifier":"CHEBI:132109","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:132109","ontology_label":"sodium octadecanoate","ontology_source":"CHEBI"},"preferred_term":"Na-stearate","sssom_rows":[{"data_row":1980,"object_id":"CHEBI:132109","object_label":"sodium octadecanoate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na-stearate","synonym_count":4} |
| ev-105e2ff6a695a8a9 | reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml; findings[finding_id=f-641361f3ac015a6b] | context_only | Predecessor structured review finding f-641361f3ac015a6b in 20261011T024637Z-mim-reconcile-all-batch-09 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-na-stearate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Na-stearate (data/ingredients/mapped/Na-stearate.yaml)'
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
summary: Per-record structured review for Na-stearate (data/ingredients/mapped/Na-stearate.yaml,
  record-9fd515657847bbc7, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Na-stearate.yaml
    sha256: 51532547e6cc93a873def26898ab576bb34fafd988d3254f4a91b7fe810c558d
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
  - path: reports/yaml_record_review/Na-stearate.md
    sha256: 28f7fbebd5554ade9119f077bbb97058ee00084edeea0d9fb28d55e07af6b5f1
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-9fd515657847bbc7
  path: data/ingredients/mapped/Na-stearate.yaml
  label: Na-stearate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na-stearate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Na-stearate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Na-stearate.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-9fd515657847bbc7
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-9fd515657847bbc7
  evidence_ids:
  - ev-77c50f268bf68643
  - ev-241ac0d895554099
  - ev-5cd38a039413c16c
  - ev-a265d8e6833510d2
  - ev-d01deb166a9b6c98
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-9fd515657847bbc7
  evidence_ids:
  - ev-77c50f268bf68643
  - ev-f002acfe33c6878a
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-9fd515657847bbc7
  evidence_ids:
  - ev-ac320132f18b68b1
  - ev-f002acfe33c6878a
  - ev-105e2ff6a695a8a9
evidence:
- evidence_id: ev-77c50f268bf68643
  kind: record_content
  reference: data/ingredients/mapped/Na-stearate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1473],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:132109","line":1475,"mapping_status":"MAPPED","ontology_id":"CHEBI:132109","preferred_term":"Na-stearate"}],"identifier":"CHEBI:132109","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:132109","ontology_label":"sodium
    octadecanoate","ontology_source":"CHEBI"},"preferred_term":"Na-stearate","sssom_rows":[{"data_row":1980,"object_id":"CHEBI:132109","object_label":"sodium
    octadecanoate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na-stearate","synonym_count":4}'
  snapshot_sha256: 51532547e6cc93a873def26898ab576bb34fafd988d3254f4a91b7fe810c558d
- evidence_id: ev-241ac0d895554099
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1473]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-5cd38a039413c16c
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Na-stearate; data-row positions=[1980]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1980,"object_id":"CHEBI:132109","object_label":"sodium
    octadecanoate","other":"Octadecanoic acid, sodium salt|Stearic acid, sodium salt|sodium
    stearate|CAS:822-16-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Na-stearate","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-a265d8e6833510d2
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1475]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:132109","line":1475,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"3","ontology_id":"CHEBI:132109","preferred_term":"Na-stearate","total_occurrences":"3"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-ac320132f18b68b1
  kind: prior_review
  reference: reports/yaml_record_review/Na-stearate.md
  locator: '`data/ingredients/mapped/Na-stearate.yaml`:2; Verdict:4; Identity:11;
    Validation:20; Evidence:27; Completeness:38; Recommended Edits:44'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 28f7fbebd5554ade9119f077bbb97058ee00084edeea0d9fb28d55e07af6b5f1
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Na-stearate.yaml`,\
    \ either remove\n  `physicochemical_roles.SURFACTANT` or replace its ChEBI-ancestry\
    \ placeholder\n  with source-backed evidence from a maintained role-text or literature\
    \ input.\n  Rerun strict validation and the role/output SSSOM checks after the\
    \ role facet\n  changes."
- evidence_id: ev-f002acfe33c6878a
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[981,2011]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"51532547e6cc93a873def26898ab576bb34fafd988d3254f4a91b7fe810c558d","finding_id":"SEM:7a8b966bc50379e6d716","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"51532547e6cc93a873def26898ab576bb34fafd988d3254f4a91b7fe810c558d","finding_id":"SEM:87ac51213bd0f4e75c3f","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-d01deb166a9b6c98
  kind: record_content
  reference: data/ingredients/mapped/Na-stearate.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1473],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:132109","line":1475,"mapping_status":"MAPPED","ontology_id":"CHEBI:132109","preferred_term":"Na-stearate"}],"identifier":"CHEBI:132109","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:132109","ontology_label":"sodium
    octadecanoate","ontology_source":"CHEBI"},"preferred_term":"Na-stearate","sssom_rows":[{"data_row":1980,"object_id":"CHEBI:132109","object_label":"sodium
    octadecanoate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na-stearate","synonym_count":4}'
  snapshot_sha256: 51532547e6cc93a873def26898ab576bb34fafd988d3254f4a91b7fe810c558d
- evidence_id: ev-105e2ff6a695a8a9
  kind: prior_review
  reference: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
  locator: findings[finding_id=f-641361f3ac015a6b]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-641361f3ac015a6b in 20261011T024637Z-mim-reconcile-all-batch-09
  snapshot_sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
assessments:
- assessment_id: a-0345beceb6b0b0dc
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-9fd515657847bbc7
  evidence_ids:
  - ev-77c50f268bf68643
  - ev-241ac0d895554099
  - ev-5cd38a039413c16c
  - ev-a265d8e6833510d2
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-3267f6066bf30d63
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-9fd515657847bbc7
  evidence_ids:
  - ev-ac320132f18b68b1
  - ev-77c50f268bf68643
  - ev-f002acfe33c6878a
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:01:32Z;
    reviewed SHA-256=51532547e6cc93a873def26898ab576bb34fafd988d3254f4a91b7fe810c558d;
    current SHA-256=51532547e6cc93a873def26898ab576bb34fafd988d3254f4a91b7fe810c558d;
    hash_changed=False. Reports=["reports/yaml_record_review/Na-stearate.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI:132109
    sodium octadecanoate identity, CAS-backed structure, occurrence count, synonyms,
    and final exact row pass, but SURFACTANT is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ac320132f18b68b1
    - ev-77c50f268bf68643
  - name: legacy-native-ids
    value: '["SEM:7a8b966bc50379e6d716","SEM:87ac51213bd0f4e75c3f"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-77c50f268bf68643
    - ev-ac320132f18b68b1
    - ev-f002acfe33c6878a
- assessment_id: a-d01deb166a9b6c98
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-9fd515657847bbc7
  evidence_ids:
  - ev-ac320132f18b68b1
  - ev-d01deb166a9b6c98
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ac320132f18b68b1
    - ev-d01deb166a9b6c98
findings:
- finding_id: rec-f-641361f3ac015a6b
  issue_key: mim-reconciliation-role-support-9fd515657847bbc7
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Na-stearate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-9fd515657847bbc7
  evidence_ids:
  - ev-ac320132f18b68b1
  - ev-d01deb166a9b6c98
  - ev-105e2ff6a695a8a9
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na-stearate.yaml
    role: maintained ingredient
  field_paths:
  - physicochemical_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024637Z-mim-reconcile-all-batch-09
    finding_id: f-641361f3ac015a6b
actions:
- action_id: rec-action-641361f3ac015a6b
  description: 'Reassess prediction-only role support: Na-stearate'
  finding_ids:
  - rec-f-641361f3ac015a6b
  target_ids:
  - record-9fd515657847bbc7
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na-stearate.yaml
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
  with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.
```
