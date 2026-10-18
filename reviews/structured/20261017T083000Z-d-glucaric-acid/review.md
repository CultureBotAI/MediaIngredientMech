# Per-record structured review: D-Glucaric_Acid (data/ingredients/mapped/D-Glucaric_Acid.yaml)

- Review: 20261017T083000Z-d-glucaric-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for D-Glucaric_Acid (data/ingredients/mapped/D-Glucaric_Acid.yaml, record-93fe177438927dbe, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/D-Glucaric_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/D-Glucaric_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-93fe177438927dbe | data/ingredients/mapped/D-Glucaric_Acid.yaml | maintained | D-Glucaric_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-93fe177438927dbe | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-93fe177438927dbe | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-93fe177438927dbe | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-93fe177438927dbe.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-93fe177438927dbe.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:11:29Z; reviewed SHA-256=28cb4957cd4826f99337d6b52f18de2844e52af42d728a893dc307967f90d8db; current SHA-256=28cb4957cd4826f99337d6b52f18de2844e52af42d728a893dc307967f90d8db; hash_changed=False. Reports=["reports/yaml_record_review/D-Glucaric_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI identity, structure fields, 0/0 count, and final SSSOM row pass, but the carbon role is only computationally supported.

### Historical provisional-role concern

evidence: concern. Targets: record-93fe177438927dbe.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-8ce517cc461bb7c5: Reassess prediction-only role support: D-Glucaric acid

major / open / confirmed; issue key: mim-reconciliation-role-support-93fe177438927dbe.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-8ce517cc461bb7c5

Reassess prediction-only role support: D-Glucaric acid

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-146ee72a6948e066 | data/ingredients/mapped/D-Glucaric_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[810],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16002","line":812,"mapping_status":"MAPPED","ontology_id":"CHEBI:16002","preferred_term":"D-Glucaric acid"}],"identifier":"CHEBI:16002","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16002","ontology_label":"D-glucaric acid","ontology_source":"CHEBI"},"preferred_term":"D-Glucaric acid","sssom_rows":[{"data_row":883,"object_id":"CHEBI:16002","object_label":"D-glucaric acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-Glucaric_Acid","synonym_count":1} |
| ev-74d31be78b76af36 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [810] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-41405558cdc4bfdf | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:D-Glucaric_Acid; data-row positions=[883] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":883,"object_id":"CHEBI:16002","object_label":"D-glucaric acid","other":"(2R,3S,4S,5S)-2,3,4,5-tetrahydroxyhexanedioic acid&#124;CAS:87-73-0","predicate_id":"skos:exactMatch","subject_id":"MIM:D-Glucaric_Acid","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-4db0620e603f3171 | docs/data/mapped_ingredients.csv; CSV lines=[812] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:16002","line":812,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:16002","preferred_term":"D-Glucaric acid","total_occurrences":"0"}] |
| ev-c6c2776e2567078d | reports/yaml_record_review/D-Glucaric_Acid.md; &#96;data/ingredients/mapped/D-Glucaric_Acid.yaml&#96;:2; Verdict:4; Identity:12; Validation:25; Evidence:45; Completeness:62; Recommended Edits:71 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-e3d7dccf045cc767 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[466,1861] | context_only | [{"current_record_sha256":"28cb4957cd4826f99337d6b52f18de2844e52af42d728a893dc307967f90d8db","finding_id":"SEM:9da2d6491b56f7bd83fb","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"28cb4957cd4826f99337d6b52f18de2844e52af42d728a893dc307967f90d8db","finding_id":"SEM:c868bbb8adc9980771b2","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-8e02d120abee6d65 | data/ingredients/mapped/D-Glucaric_Acid.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[810],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16002","line":812,"mapping_status":"MAPPED","ontology_id":"CHEBI:16002","preferred_term":"D-Glucaric acid"}],"identifier":"CHEBI:16002","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16002","ontology_label":"D-glucaric acid","ontology_source":"CHEBI"},"preferred_term":"D-Glucaric acid","sssom_rows":[{"data_row":883,"object_id":"CHEBI:16002","object_label":"D-glucaric acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-Glucaric_Acid","synonym_count":1} |
| ev-e62959ebbd218410 | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-8ce517cc461bb7c5] | context_only | Predecessor structured review finding f-8ce517cc461bb7c5 in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-d-glucaric-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: D-Glucaric_Acid (data/ingredients/mapped/D-Glucaric_Acid.yaml)'
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
summary: Per-record structured review for D-Glucaric_Acid (data/ingredients/mapped/D-Glucaric_Acid.yaml,
  record-93fe177438927dbe, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/D-Glucaric_Acid.yaml
    sha256: 28cb4957cd4826f99337d6b52f18de2844e52af42d728a893dc307967f90d8db
    role: target
  - path: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
    sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
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
  - path: reports/yaml_record_review/D-Glucaric_Acid.md
    sha256: b7987fcb3df254718a8e09e89434aacdf6840817031c58bedd2f0c420c8f1dcc
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-93fe177438927dbe
  path: data/ingredients/mapped/D-Glucaric_Acid.yaml
  label: D-Glucaric_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-Glucaric_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/D-Glucaric_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/D-Glucaric_Acid.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-93fe177438927dbe
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-93fe177438927dbe
  evidence_ids:
  - ev-146ee72a6948e066
  - ev-74d31be78b76af36
  - ev-41405558cdc4bfdf
  - ev-4db0620e603f3171
  - ev-8e02d120abee6d65
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-93fe177438927dbe
  evidence_ids:
  - ev-146ee72a6948e066
  - ev-e3d7dccf045cc767
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-93fe177438927dbe
  evidence_ids:
  - ev-c6c2776e2567078d
  - ev-e3d7dccf045cc767
  - ev-e62959ebbd218410
evidence:
- evidence_id: ev-146ee72a6948e066
  kind: record_content
  reference: data/ingredients/mapped/D-Glucaric_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[810],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16002","line":812,"mapping_status":"MAPPED","ontology_id":"CHEBI:16002","preferred_term":"D-Glucaric
    acid"}],"identifier":"CHEBI:16002","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16002","ontology_label":"D-glucaric
    acid","ontology_source":"CHEBI"},"preferred_term":"D-Glucaric acid","sssom_rows":[{"data_row":883,"object_id":"CHEBI:16002","object_label":"D-glucaric
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-Glucaric_Acid","synonym_count":1}'
  snapshot_sha256: 28cb4957cd4826f99337d6b52f18de2844e52af42d728a893dc307967f90d8db
- evidence_id: ev-74d31be78b76af36
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [810]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-41405558cdc4bfdf
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:D-Glucaric_Acid; data-row positions=[883]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":883,"object_id":"CHEBI:16002","object_label":"D-glucaric
    acid","other":"(2R,3S,4S,5S)-2,3,4,5-tetrahydroxyhexanedioic acid|CAS:87-73-0","predicate_id":"skos:exactMatch","subject_id":"MIM:D-Glucaric_Acid","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-4db0620e603f3171
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[812]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:16002","line":812,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:16002","preferred_term":"D-Glucaric
    acid","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-c6c2776e2567078d
  kind: prior_review
  reference: reports/yaml_record_review/D-Glucaric_Acid.md
  locator: '`data/ingredients/mapped/D-Glucaric_Acid.yaml`:2; Verdict:4; Identity:12;
    Validation:25; Evidence:45; Completeness:62; Recommended Edits:71'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: b7987fcb3df254718a8e09e89434aacdf6840817031c58bedd2f0c420c8f1dcc
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/D-Glucaric_Acid.yaml`,\
    \ either replace the\n  computational `CARBON_SOURCE` evidence with direct source-backed\
    \ media-role\n  evidence for this ingredient, or remove the role facet; then rerun\
    \ strict\n  validation and the final SSSOM build."
- evidence_id: ev-e3d7dccf045cc767
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[466,1861]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"28cb4957cd4826f99337d6b52f18de2844e52af42d728a893dc307967f90d8db","finding_id":"SEM:9da2d6491b56f7bd83fb","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"28cb4957cd4826f99337d6b52f18de2844e52af42d728a893dc307967f90d8db","finding_id":"SEM:c868bbb8adc9980771b2","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-8e02d120abee6d65
  kind: record_content
  reference: data/ingredients/mapped/D-Glucaric_Acid.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[810],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16002","line":812,"mapping_status":"MAPPED","ontology_id":"CHEBI:16002","preferred_term":"D-Glucaric
    acid"}],"identifier":"CHEBI:16002","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16002","ontology_label":"D-glucaric
    acid","ontology_source":"CHEBI"},"preferred_term":"D-Glucaric acid","sssom_rows":[{"data_row":883,"object_id":"CHEBI:16002","object_label":"D-glucaric
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-Glucaric_Acid","synonym_count":1}'
  snapshot_sha256: 28cb4957cd4826f99337d6b52f18de2844e52af42d728a893dc307967f90d8db
- evidence_id: ev-e62959ebbd218410
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-8ce517cc461bb7c5]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-8ce517cc461bb7c5 in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-52876a127393d345
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-93fe177438927dbe
  evidence_ids:
  - ev-146ee72a6948e066
  - ev-74d31be78b76af36
  - ev-41405558cdc4bfdf
  - ev-4db0620e603f3171
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-845d3f6f9a4800ef
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-93fe177438927dbe
  evidence_ids:
  - ev-c6c2776e2567078d
  - ev-146ee72a6948e066
  - ev-e3d7dccf045cc767
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:11:29Z;
    reviewed SHA-256=28cb4957cd4826f99337d6b52f18de2844e52af42d728a893dc307967f90d8db;
    current SHA-256=28cb4957cd4826f99337d6b52f18de2844e52af42d728a893dc307967f90d8db;
    hash_changed=False. Reports=["reports/yaml_record_review/D-Glucaric_Acid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI identity, structure fields, 0/0 count, and final SSSOM row pass, but the
    carbon role is only computationally supported.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c6c2776e2567078d
    - ev-146ee72a6948e066
  - name: legacy-native-ids
    value: '["SEM:9da2d6491b56f7bd83fb","SEM:c868bbb8adc9980771b2"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-146ee72a6948e066
    - ev-c6c2776e2567078d
    - ev-e3d7dccf045cc767
- assessment_id: a-8e02d120abee6d65
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-93fe177438927dbe
  evidence_ids:
  - ev-c6c2776e2567078d
  - ev-8e02d120abee6d65
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c6c2776e2567078d
    - ev-8e02d120abee6d65
findings:
- finding_id: rec-f-8ce517cc461bb7c5
  issue_key: mim-reconciliation-role-support-93fe177438927dbe
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: D-Glucaric acid'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-93fe177438927dbe
  evidence_ids:
  - ev-c6c2776e2567078d
  - ev-8e02d120abee6d65
  - ev-e62959ebbd218410
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-Glucaric_Acid.yaml
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
    review_id: 20261011T024633Z-mim-reconcile-all-batch-05
    finding_id: f-8ce517cc461bb7c5
actions:
- action_id: rec-action-8ce517cc461bb7c5
  description: 'Reassess prediction-only role support: D-Glucaric acid'
  finding_ids:
  - rec-f-8ce517cc461bb7c5
  target_ids:
  - record-93fe177438927dbe
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-Glucaric_Acid.yaml
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
  with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.
```
