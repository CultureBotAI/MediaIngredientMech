# Per-record structured review: Cadmium_Acetate_Dihydrate (data/ingredients/mapped/Cadmium_Acetate_Dihydrate.yaml)

- Review: 20261017T083000Z-cadmium-acetate-dihydrate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Cadmium_Acetate_Dihydrate (data/ingredients/mapped/Cadmium_Acetate_Dihydrate.yaml, record-325728db8d6c7d72, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Cadmium_Acetate_Dihydrate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Cadmium_Acetate_Dihydrate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-325728db8d6c7d72 | data/ingredients/mapped/Cadmium_Acetate_Dihydrate.yaml | maintained | Cadmium_Acetate_Dihydrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-325728db8d6c7d72 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-325728db8d6c7d72 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-325728db8d6c7d72 | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-325728db8d6c7d72.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-325728db8d6c7d72.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T10:37:19Z; reviewed SHA-256=07cadbd336cef9129741a691cbee09dc6fe0d368df15aab884935a4ec19aefb5; current SHA-256=07cadbd336cef9129741a691cbee09dc6fe0d368df15aab884935a4ec19aefb5; hash_changed=False. Reports=["reports/yaml_record_review/Cadmium_Acetate_Dihydrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS registry and broader cadmium acetate rows pass, but the structure bundle still mixes hydrate and anhydrous PubChem fields.

## Findings

### rec-f-1b912eed168166c7: Historical review coverage and residual narrative: Cadmium_Acetate_Dihydrate

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-325728db8d6c7d72.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T10:37:19Z; reviewed SHA-256=07cadbd336cef9129741a691cbee09dc6fe0d368df15aab884935a4ec19aefb5; current SHA-256=07cadbd336cef9129741a691cbee09dc6fe0d368df15aab884935a4ec19aefb5; hash_changed=False. Reports=["reports/yaml_record_review/Cadmium_Acetate_Dihydrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS registry and broader cadmium acetate rows pass, but the structure bundle still mixes hydrate and anhydrous PubChem fields.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-2ac00cb3f64a7e08 | data/ingredients/mapped/Cadmium_Acetate_Dihydrate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[627],"raw_equal":true},"docs_rows":[{"identifier":"cas:5743-04-4","line":629,"mapping_status":"MAPPED","ontology_id":"CHEBI:232796","preferred_term":"Cadmium acetate dihydrate"}],"identifier":"cas:5743-04-4","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:232796","ontology_label":"cadmium acetate","ontology_source":"CHEBI"},"preferred_term":"Cadmium acetate dihydrate","sssom_rows":[{"data_row":608,"object_id":"CHEBI:232796","object_label":"cadmium acetate","predicate_id":"skos:closeMatch"},{"data_row":609,"object_id":"cas:5743-04-4","object_label":"Cadmium acetate dihydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cadmium_Acetate_Dihydrate","synonym_count":1} |
| ev-70ceaa80c0bea3d4 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [627] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-34a980ffc745dd35 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Cadmium_Acetate_Dihydrate; data-row positions=[608,609] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":608,"object_id":"CHEBI:232796","object_label":"cadmium acetate","other":"cadmium(2+);diacetate&#124;CAS:5743-04-4","predicate_id":"skos:closeMatch","subject_id":"MIM:Cadmium_Acetate_Dihydrate","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"},{"data_row":609,"object_id":"cas:5743-04-4","object_label":"Cadmium acetate dihydrate","other":"CAS:5743-04-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Cadmium_Acetate_Dihydrate","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-c8a6b4554d816243 | docs/data/mapped_ingredients.csv; CSV lines=[629] | supports | Published identity and count rows inspected: [{"identifier":"cas:5743-04-4","line":629,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:232796","preferred_term":"Cadmium acetate dihydrate","total_occurrences":"1"}] |
| ev-83c45ecfe71d69b9 | reports/yaml_record_review/Cadmium_Acetate_Dihydrate.md; &#96;data/ingredients/mapped/Cadmium_Acetate_Dihydrate.yaml&#96;:2; Verdict:4; Identity:11; Validation:24; Evidence:39; Completeness:58; Recommended Edits:66 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-73771277fa4267ff | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[346] | context_only | [{"current_record_sha256":"07cadbd336cef9129741a691cbee09dc6fe0d368df15aab884935a4ec19aefb5","finding_id":"SEM:e64c9edb2ade408b19da","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-cadmium-acetate-dihydrate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Cadmium_Acetate_Dihydrate (data/ingredients/mapped/Cadmium_Acetate_Dihydrate.yaml)'
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
summary: Per-record structured review for Cadmium_Acetate_Dihydrate (data/ingredients/mapped/Cadmium_Acetate_Dihydrate.yaml,
  record-325728db8d6c7d72, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Cadmium_Acetate_Dihydrate.yaml
    sha256: 07cadbd336cef9129741a691cbee09dc6fe0d368df15aab884935a4ec19aefb5
    role: target
  - path: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
    sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
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
  - path: reports/yaml_record_review/Cadmium_Acetate_Dihydrate.md
    sha256: 7cca5a27d58ca3c4b7d15f654da650ed619783c17f65d5f3c313381afcde4166
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-325728db8d6c7d72
  path: data/ingredients/mapped/Cadmium_Acetate_Dihydrate.yaml
  label: Cadmium_Acetate_Dihydrate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cadmium_Acetate_Dihydrate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Cadmium_Acetate_Dihydrate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Cadmium_Acetate_Dihydrate.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-325728db8d6c7d72
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-325728db8d6c7d72
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-325728db8d6c7d72
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-325728db8d6c7d72
evidence:
- evidence_id: ev-2ac00cb3f64a7e08
  kind: record_content
  reference: data/ingredients/mapped/Cadmium_Acetate_Dihydrate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[627],"raw_equal":true},"docs_rows":[{"identifier":"cas:5743-04-4","line":629,"mapping_status":"MAPPED","ontology_id":"CHEBI:232796","preferred_term":"Cadmium
    acetate dihydrate"}],"identifier":"cas:5743-04-4","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:232796","ontology_label":"cadmium
    acetate","ontology_source":"CHEBI"},"preferred_term":"Cadmium acetate dihydrate","sssom_rows":[{"data_row":608,"object_id":"CHEBI:232796","object_label":"cadmium
    acetate","predicate_id":"skos:closeMatch"},{"data_row":609,"object_id":"cas:5743-04-4","object_label":"Cadmium
    acetate dihydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cadmium_Acetate_Dihydrate","synonym_count":1}'
  snapshot_sha256: 07cadbd336cef9129741a691cbee09dc6fe0d368df15aab884935a4ec19aefb5
- evidence_id: ev-70ceaa80c0bea3d4
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [627]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-34a980ffc745dd35
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Cadmium_Acetate_Dihydrate; data-row positions=[608,609]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":608,"object_id":"CHEBI:232796","object_label":"cadmium
    acetate","other":"cadmium(2+);diacetate|CAS:5743-04-4","predicate_id":"skos:closeMatch","subject_id":"MIM:Cadmium_Acetate_Dihydrate","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"},{"data_row":609,"object_id":"cas:5743-04-4","object_label":"Cadmium
    acetate dihydrate","other":"CAS:5743-04-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Cadmium_Acetate_Dihydrate","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-c8a6b4554d816243
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[629]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:5743-04-4","line":629,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:232796","preferred_term":"Cadmium
    acetate dihydrate","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-83c45ecfe71d69b9
  kind: prior_review
  reference: reports/yaml_record_review/Cadmium_Acetate_Dihydrate.md
  locator: '`data/ingredients/mapped/Cadmium_Acetate_Dihydrate.yaml`:2; Verdict:4;
    Identity:11; Validation:24; Evidence:39; Completeness:58; Recommended Edits:66'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 7cca5a27d58ca3c4b7d15f654da650ed619783c17f65d5f3c313381afcde4166
  quote: "Recommended Edits:\n- Major: update `chemical_properties` in\n  `data/ingredients/mapped/Cadmium_Acetate_Dihydrate.yaml`\
    \ so `pubchem_cid`,\n  `molecular_formula`, `inchi`, and `smiles` consistently\
    \ describe CAS\n  `5743-04-4` / PubChem CID 6537495, or clear the derived structure\
    \ fields if\n  the curation standard does not accept that PubChem compound; then\
    \ run\n  `just sync-curated` and focused strict/SSSOM validation."
- evidence_id: ev-73771277fa4267ff
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[346]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"07cadbd336cef9129741a691cbee09dc6fe0d368df15aab884935a4ec19aefb5","finding_id":"SEM:e64c9edb2ade408b19da","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-be07a7b8aabad3a4
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-325728db8d6c7d72
  evidence_ids:
  - ev-2ac00cb3f64a7e08
  - ev-70ceaa80c0bea3d4
  - ev-34a980ffc745dd35
  - ev-c8a6b4554d816243
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-b870a336119e4f36
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-325728db8d6c7d72
  evidence_ids:
  - ev-83c45ecfe71d69b9
  - ev-2ac00cb3f64a7e08
  - ev-73771277fa4267ff
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T10:37:19Z;
    reviewed SHA-256=07cadbd336cef9129741a691cbee09dc6fe0d368df15aab884935a4ec19aefb5;
    current SHA-256=07cadbd336cef9129741a691cbee09dc6fe0d368df15aab884935a4ec19aefb5;
    hash_changed=False. Reports=["reports/yaml_record_review/Cadmium_Acetate_Dihydrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS
    registry and broader cadmium acetate rows pass, but the structure bundle still
    mixes hydrate and anhydrous PubChem fields.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-83c45ecfe71d69b9
    - ev-2ac00cb3f64a7e08
  - name: legacy-native-ids
    value: '["SEM:e64c9edb2ade408b19da"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-2ac00cb3f64a7e08
    - ev-83c45ecfe71d69b9
    - ev-73771277fa4267ff
findings:
- finding_id: rec-f-1b912eed168166c7
  issue_key: mim-reconciliation-historical-review-coverage-and-r-325728db8d6c7d72
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Cadmium_Acetate_Dihydrate'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T10:37:19Z;
    reviewed SHA-256=07cadbd336cef9129741a691cbee09dc6fe0d368df15aab884935a4ec19aefb5;
    current SHA-256=07cadbd336cef9129741a691cbee09dc6fe0d368df15aab884935a4ec19aefb5;
    hash_changed=False. Reports=["reports/yaml_record_review/Cadmium_Acetate_Dihydrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS
    registry and broader cadmium acetate rows pass, but the structure bundle still
    mixes hydrate and anhydrous PubChem fields.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-325728db8d6c7d72
  evidence_ids:
  - ev-83c45ecfe71d69b9
  - ev-2ac00cb3f64a7e08
  - ev-73771277fa4267ff
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cadmium_Acetate_Dihydrate.yaml
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
  with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.
```
