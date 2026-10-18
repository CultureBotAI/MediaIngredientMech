# Per-record structured review: Bis-tris (data/ingredients/mapped/Bis-tris.yaml)

- Review: 20261017T083000Z-bis-tris
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Bis-tris (data/ingredients/mapped/Bis-tris.yaml, record-50574e55a5258db4, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Bis-tris.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Bis-tris.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-50574e55a5258db4 | data/ingredients/mapped/Bis-tris.yaml | maintained | Bis-tris |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-50574e55a5258db4 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-50574e55a5258db4 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-50574e55a5258db4 | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-50574e55a5258db4.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: not_applicable. Targets: record-50574e55a5258db4.

The latest legacy review reports no outstanding finding. This run verifies local consistency only; it does not renew that earlier scientific pass.

Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-16T09:56:28Z; reviewed SHA-256=f879fd427c37bddb167a8c410d59b06bebb08b531a0b86617e75b516bf274d0a; current SHA-256=f879fd427c37bddb167a8c410d59b06bebb08b531a0b86617e75b516bf274d0a; hash_changed=False. Reports=["reports/yaml_record_review/Bis-tris.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI Bis-Tris identity, CAS, ChEBI synonyms, buffer role, structure fields, SSSOM row, occurrence count, and aggregate copy pass.

### Historical provisional-role concern

evidence: concern. Targets: record-50574e55a5258db4.

Current role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence lists and require source-backed curation support.

## Findings

### rec-f-role-50574e55a5258db4: Reassess prediction-only or empty role support: Bis-tris

major / open / confirmed; issue key: mim-reconciliation-role-support-50574e55a5258db4.

Prediction-only or empty evidence payloads remain on the named current role assertions (physicochemical_roles[0]). This confirms the local evidence gap, not that the biological role is false.

## Recommended Actions And Acceptance Checks

### rec-act-role-50574e55a5258db4

Reassess prediction-only or empty role support: Bis-tris

- Address the exact role fields and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-c17ddd3e31758c66 | data/ingredients/mapped/Bis-tris.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[594],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:41250","line":596,"mapping_status":"MAPPED","ontology_id":"CHEBI:41250","preferred_term":"Bis-Tris"}],"identifier":"CHEBI:41250","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4,"edge_count":4,"occurrences":4},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:41250","ontology_label":"bis-tris","ontology_source":"CHEBI"},"preferred_term":"Bis-Tris","sssom_rows":[{"data_row":557,"object_id":"CHEBI:41250","object_label":"bis-tris","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Bis-tris","synonym_count":7} |
| ev-68caf0aa16f1855d | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [594] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-9376822b1a3df033 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Bis-tris; data-row positions=[557] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":557,"object_id":"CHEBI:41250","object_label":"bis-tris","other":"2,2-bis(hydroxymethyl)-2,2',2''-nitrilotriethanol&#124;2-(bis(2-hydroxyethyl)amino)-2-(hydroxymethyl)-1,3-propanediol&#124;2-[BIS-(2-HYDROXY-ETHYL)-AMINO]-2-HYDROXYMETHYL-PROPANE-1,3-DIOL&#124;2-[bis(2-hydroxyethyl)amino]-2-(hydroxymethyl)propane-1,3-diol&#124;BIS-2-HYDROXY-IMINO-TRIS-HYDROXYMETHYL-METHANE&#124;bistris&#124;CAS:6976-37-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Bis-tris","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-9dd287f0e1be8659 | docs/data/mapped_ingredients.csv; CSV lines=[596] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:41250","line":596,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"4","ontology_id":"CHEBI:41250","preferred_term":"Bis-Tris","total_occurrences":"4"}] |
| ev-0083b8e92d76b452 | reports/yaml_record_review/Bis-tris.md; &#96;data/ingredients/mapped/Bis-tris.yaml&#96;:2; Verdict:4; Identity:10; Validation:24; Evidence:34; Completeness:49; Recommended Edits:55 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-faef97df8551296e | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1629] | context_only | [{"current_record_sha256":"f879fd427c37bddb167a8c410d59b06bebb08b531a0b86617e75b516bf274d0a","finding_id":"SEM:655a76e4e9d88b6b7db5","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-c3a9f1fb8ad81b15 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; current_record=data/ingredients/mapped/Bis-tris.yaml | context_only | Semantic review finding dispositions ledger |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-bis-tris
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Bis-tris (data/ingredients/mapped/Bis-tris.yaml)'
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
summary: Per-record structured review for Bis-tris (data/ingredients/mapped/Bis-tris.yaml,
  record-50574e55a5258db4, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Bis-tris.yaml
    sha256: f879fd427c37bddb167a8c410d59b06bebb08b531a0b86617e75b516bf274d0a
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
  - path: reports/yaml_record_review/Bis-tris.md
    sha256: cd963a414044de6f9bfb67cceba1de50031827cc31bdf8bfbe261d456ddff28f
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-50574e55a5258db4
  path: data/ingredients/mapped/Bis-tris.yaml
  label: Bis-tris
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bis-tris.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Bis-tris.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Bis-tris.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-50574e55a5258db4
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-50574e55a5258db4
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-50574e55a5258db4
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-50574e55a5258db4
evidence:
- evidence_id: ev-c17ddd3e31758c66
  kind: record_content
  reference: data/ingredients/mapped/Bis-tris.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[594],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:41250","line":596,"mapping_status":"MAPPED","ontology_id":"CHEBI:41250","preferred_term":"Bis-Tris"}],"identifier":"CHEBI:41250","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4,"edge_count":4,"occurrences":4},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:41250","ontology_label":"bis-tris","ontology_source":"CHEBI"},"preferred_term":"Bis-Tris","sssom_rows":[{"data_row":557,"object_id":"CHEBI:41250","object_label":"bis-tris","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Bis-tris","synonym_count":7}'
  snapshot_sha256: f879fd427c37bddb167a8c410d59b06bebb08b531a0b86617e75b516bf274d0a
- evidence_id: ev-68caf0aa16f1855d
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [594]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-9376822b1a3df033
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Bis-tris; data-row positions=[557]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":557,"object_id":"CHEBI:41250","object_label":"bis-tris","other":"2,2-bis(hydroxymethyl)-2,2'',2''''-nitrilotriethanol|2-(bis(2-hydroxyethyl)amino)-2-(hydroxymethyl)-1,3-propanediol|2-[BIS-(2-HYDROXY-ETHYL)-AMINO]-2-HYDROXYMETHYL-PROPANE-1,3-DIOL|2-[bis(2-hydroxyethyl)amino]-2-(hydroxymethyl)propane-1,3-diol|BIS-2-HYDROXY-IMINO-TRIS-HYDROXYMETHYL-METHANE|bistris|CAS:6976-37-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Bis-tris","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-9dd287f0e1be8659
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[596]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:41250","line":596,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"4","ontology_id":"CHEBI:41250","preferred_term":"Bis-Tris","total_occurrences":"4"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-0083b8e92d76b452
  kind: prior_review
  reference: reports/yaml_record_review/Bis-tris.md
  locator: '`data/ingredients/mapped/Bis-tris.yaml`:2; Verdict:4; Identity:10; Validation:24;
    Evidence:34; Completeness:49; Recommended Edits:55'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: cd963a414044de6f9bfb67cceba1de50031827cc31bdf8bfbe261d456ddff28f
  quote: 'Recommended Edits:

    - None.'
- evidence_id: ev-faef97df8551296e
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1629]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"f879fd427c37bddb167a8c410d59b06bebb08b531a0b86617e75b516bf274d0a","finding_id":"SEM:655a76e4e9d88b6b7db5","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-c3a9f1fb8ad81b15
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: current_record=data/ingredients/mapped/Bis-tris.yaml
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Semantic review finding dispositions ledger
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-1fa94cc05817a501
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-50574e55a5258db4
  evidence_ids:
  - ev-c17ddd3e31758c66
  - ev-68caf0aa16f1855d
  - ev-9376822b1a3df033
  - ev-9dd287f0e1be8659
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-a780c3f854cbd540
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: not_applicable
  summary: The latest legacy review reports no outstanding finding. This run verifies
    local consistency only; it does not renew that earlier scientific pass.
  target_ids:
  - record-50574e55a5258db4
  evidence_ids:
  - ev-0083b8e92d76b452
  - ev-c17ddd3e31758c66
  - ev-faef97df8551296e
  details: 'Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-16T09:56:28Z;
    reviewed SHA-256=f879fd427c37bddb167a8c410d59b06bebb08b531a0b86617e75b516bf274d0a;
    current SHA-256=f879fd427c37bddb167a8c410d59b06bebb08b531a0b86617e75b516bf274d0a;
    hash_changed=False. Reports=["reports/yaml_record_review/Bis-tris.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI Bis-Tris
    identity, CAS, ChEBI synonyms, buffer role, structure fields, SSSOM row, occurrence
    count, and aggregate copy pass.'
  dimensions:
  - name: legacy-native-ids
    value: '["SEM:655a76e4e9d88b6b7db5"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-c17ddd3e31758c66
    - ev-0083b8e92d76b452
    - ev-faef97df8551296e
- assessment_id: a-role-50574e55a5258db4
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Current role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence lists and require source-backed curation support.
  target_ids:
  - record-50574e55a5258db4
  evidence_ids:
  - ev-c17ddd3e31758c66
  - ev-c3a9f1fb8ad81b15
  dimensions:
  - name: legacy-disposition
    value: still_present
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c17ddd3e31758c66
    - ev-c3a9f1fb8ad81b15
findings:
- finding_id: rec-f-role-50574e55a5258db4
  issue_key: mim-reconciliation-role-support-50574e55a5258db4
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only or empty role support: Bis-tris'
  description: Prediction-only or empty evidence payloads remain on the named current
    role assertions (physicochemical_roles[0]). This confirms the local evidence gap,
    not that the biological role is false.
  target_ids:
  - record-50574e55a5258db4
  evidence_ids:
  - ev-c17ddd3e31758c66
  - ev-c3a9f1fb8ad81b15
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bis-tris.yaml
    role: maintained ingredient
  field_paths:
  - physicochemical_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
actions:
- action_id: rec-act-role-50574e55a5258db4
  description: 'Reassess prediction-only or empty role support: Bis-tris'
  finding_ids:
  - rec-f-role-50574e55a5258db4
  target_ids:
  - record-50574e55a5258db4
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bis-tris.yaml
    role: maintained ingredient
  acceptance_checks:
  - Address the exact role fields and evidence gap described in this finding; preserve
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
  with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.
```
