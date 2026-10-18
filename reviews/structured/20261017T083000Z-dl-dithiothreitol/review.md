# Per-record structured review: Dl-dithiothreitol (data/ingredients/mapped/Dl-dithiothreitol.yaml)

- Review: 20261017T083000Z-dl-dithiothreitol
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Dl-dithiothreitol (data/ingredients/mapped/Dl-dithiothreitol.yaml, record-b9e47fdd6cf3a713, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Dl-dithiothreitol.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Dl-dithiothreitol.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-b9e47fdd6cf3a713 | data/ingredients/mapped/Dl-dithiothreitol.yaml | maintained | Dl-dithiothreitol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-b9e47fdd6cf3a713 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-b9e47fdd6cf3a713 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-b9e47fdd6cf3a713 | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-b9e47fdd6cf3a713.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-b9e47fdd6cf3a713.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T15:10:20Z; reviewed SHA-256=ae26a9801b8dbb495ff4e03952847516a9724042c0cfdcab273e159de0e77f14; current SHA-256=ae26a9801b8dbb495ff4e03952847516a9724042c0cfdcab273e159de0e77f14; hash_changed=False. Reports=["reports/yaml_record_review/Dl-dithiothreitol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact DTT identity passes, but final SSSOM leaks L-DTT/concentration labels and the reducing-agent role is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-b9e47fdd6cf3a713.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-4b159170f3c0b036: Reassess prediction-only role support: DL-Dithiothreitol

major / open / confirmed; issue key: mim-reconciliation-role-support-b9e47fdd6cf3a713.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-4b159170f3c0b036

Reassess prediction-only role support: DL-Dithiothreitol

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-457cad6afdbf0292 | data/ingredients/mapped/Dl-dithiothreitol.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[913],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18320","line":915,"mapping_status":"MAPPED","ontology_id":"CHEBI:18320","preferred_term":"DL-Dithiothreitol"}],"identifier":"CHEBI:18320","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":121,"edge_count":121,"occurrences":121},"occurrence_statistics":{"media_count":121,"total_occurrences":121},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:18320","ontology_label":"1,4-dithiothreitol","ontology_source":"CHEBI"},"preferred_term":"DL-Dithiothreitol","sssom_rows":[{"data_row":1076,"object_id":"CHEBI:18320","object_label":"1,4-dithiothreitol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Dl-dithiothreitol","synonym_count":22} |
| ev-e8a373a1fef710fd | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [913] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-e4f339d36a6b8de4 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Dl-dithiothreitol; data-row positions=[1076] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1076,"object_id":"CHEBI:18320","object_label":"1,4-dithiothreitol","other":"(R*,R*)-1,4-dimercapto-2,3-butanediol&#124;Cleland's reagent&#124;DTL&#124;DTT&#124;Dithiotreitol&#124;rac-Dithiothreitol&#124;rel-(2R,3R)-1,4-disulfanylbutane-2,3-diol&#124;Dithiothreitol&#124;DL-Dithiothreitol (DTT)&#124;1,4--dithiothreitol (DTT)&#124;DTT (DL-Dithiothreitol)&#124;Dithiothreitol (0.25 M)&#124;Dithiothreitol (DTT)&#124;(2R,3R)-1,4-dimercaptobutane-2,3-diol&#124;(2R,3R)-1,4-disulfanylbutane-2,3-diol&#124;2,3-DIHYDROXY-1,4-DITHIOBUTANE&#124;L-1,4-dithiothreitol&#124;L-DTT&#124;L-dithiothreitol&#124;L-threo-1,4-dimercapto-2,3-butanediol&#124;CAS:3483-12-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Dl-dithiothreitol","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-33d602525554d3cd | docs/data/mapped_ingredients.csv; CSV lines=[915] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:18320","line":915,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"121","ontology_id":"CHEBI:18320","preferred_term":"DL-Dithiothreitol","total_occurrences":"121"}] |
| ev-d91e2a19f1f7a511 | reports/yaml_record_review/Dl-dithiothreitol.md; &#96;data/ingredients/mapped/Dl-dithiothreitol.yaml&#96;:2; Verdict:4; Identity:12; Validation:27; Evidence:44; Completeness:67; Recommended Edits:76 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-f6419f956818f063 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[549,1439] | context_only | [{"current_record_sha256":"ae26a9801b8dbb495ff4e03952847516a9724042c0cfdcab273e159de0e77f14","finding_id":"SEM:e5d26724ca3365cf06a9","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"ae26a9801b8dbb495ff4e03952847516a9724042c0cfdcab273e159de0e77f14","finding_id":"SEM:2918c3788f2912e77adb","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-619046cc5ebfb316 | data/ingredients/mapped/Dl-dithiothreitol.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[913],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18320","line":915,"mapping_status":"MAPPED","ontology_id":"CHEBI:18320","preferred_term":"DL-Dithiothreitol"}],"identifier":"CHEBI:18320","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":121,"edge_count":121,"occurrences":121},"occurrence_statistics":{"media_count":121,"total_occurrences":121},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:18320","ontology_label":"1,4-dithiothreitol","ontology_source":"CHEBI"},"preferred_term":"DL-Dithiothreitol","sssom_rows":[{"data_row":1076,"object_id":"CHEBI:18320","object_label":"1,4-dithiothreitol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Dl-dithiothreitol","synonym_count":22} |
| ev-88683affae894248 | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-4b159170f3c0b036] | context_only | Predecessor structured review finding f-4b159170f3c0b036 in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-dl-dithiothreitol
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Dl-dithiothreitol (data/ingredients/mapped/Dl-dithiothreitol.yaml)'
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
summary: Per-record structured review for Dl-dithiothreitol (data/ingredients/mapped/Dl-dithiothreitol.yaml,
  record-b9e47fdd6cf3a713, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Dl-dithiothreitol.yaml
    sha256: ae26a9801b8dbb495ff4e03952847516a9724042c0cfdcab273e159de0e77f14
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
  - path: reports/yaml_record_review/Dl-dithiothreitol.md
    sha256: 5928b07d6a0172ee01de57faa0dfbebfc398c946ffdeff0816485af0344b2673
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-b9e47fdd6cf3a713
  path: data/ingredients/mapped/Dl-dithiothreitol.yaml
  label: Dl-dithiothreitol
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Dl-dithiothreitol.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Dl-dithiothreitol.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Dl-dithiothreitol.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-b9e47fdd6cf3a713
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-b9e47fdd6cf3a713
  evidence_ids:
  - ev-457cad6afdbf0292
  - ev-e8a373a1fef710fd
  - ev-e4f339d36a6b8de4
  - ev-33d602525554d3cd
  - ev-619046cc5ebfb316
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-b9e47fdd6cf3a713
  evidence_ids:
  - ev-457cad6afdbf0292
  - ev-f6419f956818f063
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-b9e47fdd6cf3a713
  evidence_ids:
  - ev-d91e2a19f1f7a511
  - ev-f6419f956818f063
  - ev-88683affae894248
evidence:
- evidence_id: ev-457cad6afdbf0292
  kind: record_content
  reference: data/ingredients/mapped/Dl-dithiothreitol.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[913],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18320","line":915,"mapping_status":"MAPPED","ontology_id":"CHEBI:18320","preferred_term":"DL-Dithiothreitol"}],"identifier":"CHEBI:18320","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":121,"edge_count":121,"occurrences":121},"occurrence_statistics":{"media_count":121,"total_occurrences":121},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:18320","ontology_label":"1,4-dithiothreitol","ontology_source":"CHEBI"},"preferred_term":"DL-Dithiothreitol","sssom_rows":[{"data_row":1076,"object_id":"CHEBI:18320","object_label":"1,4-dithiothreitol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Dl-dithiothreitol","synonym_count":22}'
  snapshot_sha256: ae26a9801b8dbb495ff4e03952847516a9724042c0cfdcab273e159de0e77f14
- evidence_id: ev-e8a373a1fef710fd
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [913]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-e4f339d36a6b8de4
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Dl-dithiothreitol; data-row positions=[1076]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1076,"object_id":"CHEBI:18320","object_label":"1,4-dithiothreitol","other":"(R*,R*)-1,4-dimercapto-2,3-butanediol|Cleland''s
    reagent|DTL|DTT|Dithiotreitol|rac-Dithiothreitol|rel-(2R,3R)-1,4-disulfanylbutane-2,3-diol|Dithiothreitol|DL-Dithiothreitol
    (DTT)|1,4--dithiothreitol (DTT)|DTT (DL-Dithiothreitol)|Dithiothreitol (0.25 M)|Dithiothreitol
    (DTT)|(2R,3R)-1,4-dimercaptobutane-2,3-diol|(2R,3R)-1,4-disulfanylbutane-2,3-diol|2,3-DIHYDROXY-1,4-DITHIOBUTANE|L-1,4-dithiothreitol|L-DTT|L-dithiothreitol|L-threo-1,4-dimercapto-2,3-butanediol|CAS:3483-12-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Dl-dithiothreitol","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-33d602525554d3cd
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[915]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:18320","line":915,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"121","ontology_id":"CHEBI:18320","preferred_term":"DL-Dithiothreitol","total_occurrences":"121"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-d91e2a19f1f7a511
  kind: prior_review
  reference: reports/yaml_record_review/Dl-dithiothreitol.md
  locator: '`data/ingredients/mapped/Dl-dithiothreitol.yaml`:2; Verdict:4; Identity:12;
    Validation:27; Evidence:44; Completeness:67; Recommended Edits:76'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 5928b07d6a0172ee01de57faa0dfbebfc398c946ffdeff0816485af0344b2673
  quote: "Recommended Edits:\n- Major: demote the L-DTT and 2R,3R-only labels in\n\
    \  `data/ingredients/mapped/Dl-dithiothreitol.yaml` to `REJECTED_LABEL` or move\n\
    \  them into provenance so a rebuild of `mappings/ingredient_mappings.sssom.tsv`\n\
    \  stops publishing them as synonyms for `CHEBI:18320`; then synchronize\n  `data/curated/mapped_ingredients.yaml`.\n\
    - Major: demote `Dithiothreitol (0.25 M)` to provenance rather than a resolving\n\
    \  synonym; then regenerate `mappings/ingredient_mappings.sssom.tsv`.\n- Major:\
    \ replace the `REDUCING_AGENT` computational role with source-backed\n  evidence\
    \ scoped to dithiothreitol, or remove the role if no support is\n  available;\
    \ then synchronize `data/curated/mapped_ingredients.yaml`."
- evidence_id: ev-f6419f956818f063
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[549,1439]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"ae26a9801b8dbb495ff4e03952847516a9724042c0cfdcab273e159de0e77f14","finding_id":"SEM:e5d26724ca3365cf06a9","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"ae26a9801b8dbb495ff4e03952847516a9724042c0cfdcab273e159de0e77f14","finding_id":"SEM:2918c3788f2912e77adb","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-619046cc5ebfb316
  kind: record_content
  reference: data/ingredients/mapped/Dl-dithiothreitol.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[913],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18320","line":915,"mapping_status":"MAPPED","ontology_id":"CHEBI:18320","preferred_term":"DL-Dithiothreitol"}],"identifier":"CHEBI:18320","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":121,"edge_count":121,"occurrences":121},"occurrence_statistics":{"media_count":121,"total_occurrences":121},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:18320","ontology_label":"1,4-dithiothreitol","ontology_source":"CHEBI"},"preferred_term":"DL-Dithiothreitol","sssom_rows":[{"data_row":1076,"object_id":"CHEBI:18320","object_label":"1,4-dithiothreitol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Dl-dithiothreitol","synonym_count":22}'
  snapshot_sha256: ae26a9801b8dbb495ff4e03952847516a9724042c0cfdcab273e159de0e77f14
- evidence_id: ev-88683affae894248
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-4b159170f3c0b036]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-4b159170f3c0b036 in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-ec54d6e79f286b1a
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-b9e47fdd6cf3a713
  evidence_ids:
  - ev-457cad6afdbf0292
  - ev-e8a373a1fef710fd
  - ev-e4f339d36a6b8de4
  - ev-33d602525554d3cd
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-4085be2d3830d0f3
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-b9e47fdd6cf3a713
  evidence_ids:
  - ev-d91e2a19f1f7a511
  - ev-457cad6afdbf0292
  - ev-f6419f956818f063
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T15:10:20Z;
    reviewed SHA-256=ae26a9801b8dbb495ff4e03952847516a9724042c0cfdcab273e159de0e77f14;
    current SHA-256=ae26a9801b8dbb495ff4e03952847516a9724042c0cfdcab273e159de0e77f14;
    hash_changed=False. Reports=["reports/yaml_record_review/Dl-dithiothreitol.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    DTT identity passes, but final SSSOM leaks L-DTT/concentration labels and the
    reducing-agent role is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d91e2a19f1f7a511
    - ev-457cad6afdbf0292
  - name: legacy-native-ids
    value: '["SEM:e5d26724ca3365cf06a9","SEM:2918c3788f2912e77adb"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-457cad6afdbf0292
    - ev-d91e2a19f1f7a511
    - ev-f6419f956818f063
- assessment_id: a-619046cc5ebfb316
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-b9e47fdd6cf3a713
  evidence_ids:
  - ev-d91e2a19f1f7a511
  - ev-619046cc5ebfb316
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d91e2a19f1f7a511
    - ev-619046cc5ebfb316
findings:
- finding_id: rec-f-4b159170f3c0b036
  issue_key: mim-reconciliation-role-support-b9e47fdd6cf3a713
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: DL-Dithiothreitol'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-b9e47fdd6cf3a713
  evidence_ids:
  - ev-d91e2a19f1f7a511
  - ev-619046cc5ebfb316
  - ev-88683affae894248
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Dl-dithiothreitol.yaml
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
    review_id: 20261011T024633Z-mim-reconcile-all-batch-05
    finding_id: f-4b159170f3c0b036
actions:
- action_id: rec-action-4b159170f3c0b036
  description: 'Reassess prediction-only role support: DL-Dithiothreitol'
  finding_ids:
  - rec-f-4b159170f3c0b036
  target_ids:
  - record-b9e47fdd6cf3a713
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Dl-dithiothreitol.yaml
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
